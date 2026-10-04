"""Offline contract tests for SEED_SELECTION_PIPELINE.

Every assertion here is about mechanics: families stay whole, batches are
balanced, the projection is uniform, contracts are enforced, and Hermes has
no code path that can trim, rank or pick. None of it consults a score.
"""
from __future__ import annotations

import json
import pathlib
import unittest

from src import seed_pipeline as sp

HERE = pathlib.Path(__file__).resolve().parent
BANK = HERE.parent / "data" / "seeds.json"


def _bank():
    return json.loads(BANK.read_text(encoding="utf-8"))


class TestBank(unittest.TestCase):
    def test_loads_1000_seeds(self):
        self.assertEqual(len(sp.load_bank()["seeds"]), 1000)

    def test_ids_unique_and_wellformed(self):
        ids = [s["seed_id"] for s in sp.load_bank()["seeds"]]
        self.assertEqual(len(ids), 1000)
        self.assertEqual(len(set(ids)), 1000)
        for i in ids:
            self.assertRegex(i, r"^MILO-[SR]\d{4}$")

    def test_declared_count_matches(self):
        self.assertEqual(_bank()["cantidad"], 1000)


class TestProjection(unittest.TestCase):
    def test_no_desarrollo_requerido(self):
        for s in sp.load_bank()["seeds"][:50]:
            self.assertNotIn("desarrollo_requerido", sp.scout_projection(s))

    def test_keeps_required_fields(self):
        p = sp.scout_projection(sp.load_bank()["seeds"][0])
        for f in sp.SCOUT_TOP_FIELDS:
            self.assertIn(f, p)
        for f in sp.SCOUT_REVISION_FIELDS:
            self.assertIn(f, p["revision"])

    def test_shape_identical_across_seeds(self):
        seeds = sp.load_bank()["seeds"]
        shapes = {tuple(sorted(sp.scout_projection(s))) for s in seeds[:200]}
        revs = {tuple(sorted(sp.scout_projection(s)["revision"])) for s in seeds[:200]}
        self.assertEqual(len(shapes), 1, "proyeccion no uniforme")
        self.assertEqual(len(revs), 1, "revision no uniforme")

    def test_projection_is_smaller_than_full(self):
        seeds = sp.load_bank()["seeds"]
        full = sum(len(json.dumps(s, ensure_ascii=False)) for s in seeds)
        proj = sum(sp._cost([s]) for s in seeds)
        self.assertLess(proj, full * 0.6)

    def test_scout_still_sees_weak_but_eligible_seed(self):
        """MILO-S0001 (calidad 89) must reach the Scouts: Hermes cannot filter it."""
        s = [x for x in sp.load_bank()["seeds"] if x["seed_id"] == "MILO-S0001"][0]
        self.assertEqual(s["revision"]["calidad"], 89.0)
        self.assertTrue(s["revision"]["elegible"])
        self.assertIn("MILO-S0001", str(sp.scout_projection(s)))


class TestBatching(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seeds = sp.load_bank()["seeds"]
        cls.batches = sp.build_batches(cls.seeds)

    def test_four_batches(self):
        self.assertEqual(len(self.batches), 4)

    def test_no_seed_lost_or_duplicated(self):
        all_ids = [s["seed_id"] for b in self.batches for s in b]
        self.assertEqual(len(all_ids), 1000)
        self.assertEqual(len(set(all_ids)), 1000)

    def test_no_family_split(self):
        fam = {}
        for s in self.seeds:
            fam.setdefault(s["family_id"], set()).add(s["seed_id"])
        for b in self.batches:
            present = {}
            for s in b:
                present.setdefault(s["family_id"], set()).add(s["seed_id"])
            for fid, ids in present.items():
                self.assertEqual(ids, fam[fid],
                                 "familia %s partida entre lotes" % fid)

    def test_balanced_within_tolerance(self):
        sizes = [sp._cost(b) for b in self.batches]
        lo, hi = min(sizes), max(sizes)
        self.assertLessEqual(hi - lo, lo * 0.20, "lotes desbalanceados: %s" % sizes)

    def test_deterministic(self):
        again = sp.build_batches(self.seeds)
        for a, b in zip(self.batches, again):
            self.assertEqual([s["seed_id"] for s in a], [s["seed_id"] for s in b])

    def test_each_batch_fits_a_64k_window(self):
        for i, b in enumerate(self.batches, start=1):
            self.assertLess(sp._cost(b) // 4, 64000,
                            "lote %d excede la ventana" % i)

    def test_manifest_records_mechanical_basis(self):
        man = sp.batch_manifest(self.seeds, self.batches)
        self.assertEqual(man["batch_count"], 4)
        self.assertEqual(man["expected_semifinalists"], 60)
        self.assertEqual(man["deterministic_inputs"], ["family_id", "projected_size_chars"])


class TestScoutContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        seeds = sp.load_bank()["seeds"]
        cls.batches = sp.build_batches(seeds)
        cls.allowed = [[s["seed_id"] for s in b] for b in cls.batches]

    def _good(self, allowed, n=15):
        return {"candidates": [
            {"rank": i + 1, "seed_id": sid, "why_selected": "porque",
             "strengths": ["a"], "risks": ["b"]}
            for i, sid in enumerate(allowed[:n])]}

    def test_accepts_valid_15(self):
        ok, probs = sp.validate_scout_output(self._good(self.allowed[0]), self.allowed[0])
        self.assertTrue(ok, probs)

    def test_rejects_14(self):
        ok, probs = sp.validate_scout_output(self._good(self.allowed[0], 14), self.allowed[0])
        self.assertFalse(ok)
        self.assertTrue(any("WRONG_COUNT" in p for p in probs))

    def test_rejects_16(self):
        ok, _ = sp.validate_scout_output(self._good(self.allowed[0], 16), self.allowed[0])
        self.assertFalse(ok)

    def test_rejects_hallucinated_id(self):
        payload = self._good(self.allowed[0])
        payload["candidates"][3]["seed_id"] = "MILO-S9999"
        ok, probs = sp.validate_scout_output(payload, self.allowed[0])
        self.assertFalse(ok)
        self.assertTrue(any("NOT_IN_BATCH" in p for p in probs))

    def test_rejects_id_from_another_batch(self):
        payload = self._good(self.allowed[0])
        payload["candidates"][0]["seed_id"] = self.allowed[1][0]
        ok, _ = sp.validate_scout_output(payload, self.allowed[0])
        self.assertFalse(ok)

    def test_rejects_duplicates(self):
        payload = self._good(self.allowed[0])
        payload["candidates"][1]["seed_id"] = payload["candidates"][0]["seed_id"]
        ok, probs = sp.validate_scout_output(payload, self.allowed[0])
        self.assertFalse(ok)
        self.assertTrue(any("DUPLICATE_IDS" in p for p in probs))

    def test_rejects_missing_reason_field(self):
        payload = self._good(self.allowed[0])
        del payload["candidates"][0]["why_selected"]
        ok, _ = sp.validate_scout_output(payload, self.allowed[0])
        self.assertFalse(ok)


class TestSemifinalists(unittest.TestCase):
    def _outs(self):
        seeds = sp.load_bank()["seeds"]
        batches = sp.build_batches(seeds)
        outs = []
        for b in batches:
            outs.append({"candidates": [
                {"rank": i + 1, "seed_id": s["seed_id"], "why_selected": "x",
                 "strengths": [], "risks": []} for i, s in enumerate(b[:15])]})
        return outs

    def test_sixty_collected(self):
        ids = sp.collect_semifinalists(self._outs())
        self.assertEqual(len(ids), 60)

    def test_nothing_trimmed_or_deduped(self):
        expected = [c["seed_id"] for o in self._outs() for c in o["candidates"]]
        self.assertEqual(sp.collect_semifinalists(self._outs()), expected)

    def test_short_list_fails_loudly(self):
        outs = self._outs()
        outs[3]["candidates"] = outs[3]["candidates"][:14]
        with self.assertRaises(ValueError):
            sp.collect_semifinalists(outs)

    def test_no_trim_parameter_exists(self):
        """The API must not offer a way to drop candidates."""
        import inspect
        self.assertEqual(
            [p for p in inspect.signature(sp.collect_semifinalists).parameters
             if p in ("top", "limit", "n", "keep", "trim", "drop")],
            [])


class TestHydration(unittest.TestCase):
    def test_returns_original_records_with_desarrollo(self):
        bank = sp.load_bank()
        ids = [s["seed_id"] for s in bank["seeds"][:3]]
        full = sp.hydrate(bank, ids)
        self.assertEqual([s["seed_id"] for s in full], ids)
        for rec in full:
            if "desarrollo_requerido" in rec:
                self.assertTrue(rec["desarrollo_requerido"])

    def test_qc_sees_more_than_scouts(self):
        bank = sp.load_bank()
        ids = [s["seed_id"] for s in bank["seeds"][:60]]
        full = sp.hydrate(bank, ids)
        qc_chars = sum(len(json.dumps(s, ensure_ascii=False)) for s in full)
        scout_chars = sum(sp._cost([s]) for s in bank["seeds"][:60])
        self.assertGreater(qc_chars, scout_chars,
                           "el juez debe ver MAS informacion que los Scouts")

    def test_missing_id_fails(self):
        bank = sp.load_bank()
        with self.assertRaises(ValueError):
            sp.hydrate(bank, ["MILO-S0001", "MILO-S9999"])


class TestQcContract(unittest.TestCase):
    def setUp(self):
        self.ids = [s["seed_id"] for s in sp.load_bank()["seeds"][:60]]

    def _good(self):
        return {
            "top_15": [{"seed_id": i, "why": "a"} for i in self.ids[:15]],
            "top_5": [{"seed_id": i, "why": "a"} for i in self.ids[:5]],
            "top_3": [{"seed_id": i, "why": "a"} for i in self.ids[:3]],
            "winner": {"seed_id": self.ids[0], "why": "a"},
        }

    def test_accepts_valid_funnel(self):
        ok, probs = sp.validate_qc_output(self._good(), self.ids)
        self.assertTrue(ok, probs)

    def test_rejects_winner_outside_60(self):
        p = self._good()
        p["winner"]["seed_id"] = "MILO-S0999"
        ok, probs = sp.validate_qc_output(p, self.ids)
        self.assertFalse(ok)
        self.assertTrue(any("WINNER_NOT_IN_60" in x for x in probs))

    def test_rejects_winner_outside_top_3(self):
        p = self._good()
        p["winner"]["seed_id"] = self.ids[10]
        ok, probs = sp.validate_qc_output(p, self.ids)
        self.assertFalse(ok)

    def test_rejects_unnested_funnel(self):
        p = self._good()
        p["top_5"] = [{"seed_id": i} for i in self.ids[15:20]]
        ok, probs = sp.validate_qc_output(p, self.ids)
        self.assertFalse(ok)
        self.assertIn("FUNNEL_5_NOT_IN_15", probs)

    def test_rejects_wrong_stage_sizes(self):
        p = self._good()
        p["top_15"] = p["top_15"][:14]
        ok, probs = sp.validate_qc_output(p, self.ids)
        self.assertFalse(ok)
        self.assertTrue(any("top_15_WRONG_COUNT" in x for x in probs))


class TestSelectedSeedDocument(unittest.TestCase):
    def test_shape(self):
        doc = sp.selected_seed_document("EP0001", "MILO-S0007")
        self.assertEqual(doc, {
            "episode_id": "EP0001", "seed_id": "MILO-S0007",
            "selected_by": "deepseek_seed_qc", "status": "SEED_APPROVED"})

    def test_attribution_is_deepseek(self):
        self.assertEqual(sp.selected_seed_document("E", "MILO-S0001")["selected_by"],
                         "deepseek_seed_qc")


if __name__ == "__main__":
    unittest.main()
