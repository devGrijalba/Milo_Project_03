#!/usr/bin/env python3
"""Sincroniza las skills del proyecto con el catalogo de Hermes.

REGLA DE MEMBRESIA (declarada por el usuario): una skill entra al proyecto si
el proyecto la USA. La membresia se deriva de referencias reales en los
archivos del proyecto, no de una lista escrita a mano -- asi una skill nueva
que el proyecto menciona queda dentro sin que nadie la agregue.

Como se decide:
  1. MENCION: toda skill nombrada en AGENTS.override.md, docs/, tools/,
     Motor_guiones/ o un bundle instalado es miembro automatico.
  2. EXPLICITA: las que el usuario fijo (CDP e inyeccion a DeepSeek/ChatGPT).
  3. El manifiesto se REGENERA desde la resolucion, no se edita a mano.

Politica de edicion: el catalogo de Hermes es el maestro. Si un archivo de la
copia del proyecto difiere del maestro, se reporta como DIVERGENCIA y no se
sobrescribe salvo que se pase --adoptar. Asi una edicion local nunca se
sobrescribe en silencio ni se pierde por sorpresa.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

CATALOG = Path(r"C:\Users\Ivan\AppData\Local\hermes\skills")
BUNDLES = Path(r"C:\Users\Ivan\AppData\Local\hermes\skill-bundles")
PROJ = Path(r"D:\03_Pruebas\Milo_Project_03")
SKILLS_DIR = PROJ / ".agents" / "skills"
MANIFEST = SKILLS_DIR / "MANIFEST.json"

SCAN_DIRS = ["docs", "tools", "Motor_guiones"]
SCAN_FILES = ["AGENTS.override.md", "README.md"]

# El usuario fijo esta lista: CDP e inyeccion a DeepSeek y ChatGPT.
EXPLICIT = {
    "chrome-cdp-automation": "exigido: transporte CDP",
    "universal-dom-injector": "exigido: inyeccion en web chats",
    "llm-browser-injection": "exigido: consultar LLM web (DeepSeek/ChatGPT)",
    "cdp-injection-handshake": "exigido: handshake CDP de inyeccion",
    "live-window-triage": "exigido: leer una pagina ya abierta",
    "browser-session-observation": "exigido: sesion de navegador",
    "chrome-extension-forensics": "exigido: extensiones de Chrome",
    "web-scraping": "exigido: scraping con DevTools",
}

# Skills cuyo NOMBRE colisiona con prosa o URLs comunes. Mencionarlas no significa
# usarlas: "de GitHub" y una URL de repo no son la skill `github`.
# Se exige que la mencion parezca un uso tecnico, no una palabra en un parrafo.
NEEDS_TECHNICAL_USE = {
    "github",
    "hermes-agent",
    "web",
    "research",
    "domain",
    "note-taking",
    "gifs",
    "apple",
    "crypto",
    "oil-gas",
    "trading",
    "gaming",
    "email",
    "productivity",
}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def catalog_index() -> dict[str, Path]:
    """nombre -> dir de la skill (la de categoria mas especifica si hay colision)."""
    idx: dict[str, Path] = {}
    for p in CATALOG.rglob("SKILL.md"):
        d = p.parent
        prev = idx.get(d.name)
        if prev is None or len(d.parts) < len(prev.parts):
            idx[d.name] = d
    return idx


def hash_tree(root: Path) -> dict[str, str]:
    out = {}
    for f in sorted(root.rglob("*")):
        if f.is_file() and "__pycache__" not in f.parts:
            out[str(f.relative_to(root)).replace("\\", "/")] = sha(f)
    return out


def project_text() -> str:
    """Todo el texto del proyecto que puede nombrar skills."""
    chunks = []
    for rel in SCAN_FILES:
        p = PROJ / rel
        if p.exists():
            chunks.append(p.read_text(encoding="utf-8", errors="replace"))
    for d in SCAN_DIRS:
        base = PROJ / d
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in {".md", ".py", ".json", ".txt", ".yaml", ".yml"}:
                chunks.append(p.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(chunks)


def bundle_skills() -> set[str]:
    found = set()
    if not BUNDLES.exists():
        return found
    for y in BUNDLES.glob("*.yaml"):
        for line in y.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*-\s*([a-z0-9][a-z0-9\-]*)\s*$", line)
            if m:
                found.add(m.group(1))
    return found


def technical_use(low_text: str, name: str) -> bool:
    """Para skills de nombre ambiguo, exige una mencion que parezca uso tecnico.

    'de GitHub' en un parrafo no es la skill github. Una URL de repo tampoco.
    Se acepta 'skill github', '/github', 'github-auth', o backticks: `github`.
    """
    n = re.escape(name.lower())
    patterns = [
        rf"skill{chr(32)}`?{n}`?",          # skill github
        rf"/{n}\b",                          # /github  (slash command)
        rf"`{n}`",                           # `github` en codigo
        rf"{n}[-_]",                         # github-auth, github_pr
        rf"[a-z0-9-]{n}\b",                  # prefijo: my-github-thing
    ]
    return any(re.search(p, low_text) for p in patterns)


def resolve_members(cat: dict[str, Path], text: str, bundles: set[str]):
    why: dict[str, str] = {}
    low = text.lower()

    for name in cat:
        if re.search(rf"(?<![a-z0-9-]){re.escape(name.lower())}(?![a-z0-9-])", low):
            if name in NEEDS_TECHNICAL_USE and not technical_use(low, name):
                continue          # mencion en prosa: no es uso
            why[name] = "mencionada en el proyecto"

    for name in bundles:
        if name in cat:
            why.setdefault(name, "usada en un bundle instalado")

    for name, motivo in EXPLICIT.items():
        if name in cat:
            why[name] = motivo

    return set(why), why


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--adoptar", action="store_true",
                    help="sobrescribe divergencias locales con el catalogo (el catalogo manda)")
    args = ap.parse_args()

    if not CATALOG.exists():
        raise SystemExit(f"catalogo no encontrado: {CATALOG}")
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    cat = catalog_index()
    text = project_text()
    bundles = bundle_skills()
    members, why = resolve_members(cat, text, bundles)

    old_manifest = {}
    if MANIFEST.exists():
        old_manifest = json.loads(MANIFEST.read_text(encoding="utf-8")).get("skills", {})

    added, kept, diverged, removed = [], [], [], []

    for name in sorted(members):
        src = cat[name]
        tgt = SKILLS_DIR / src.relative_to(CATALOG)
        if not tgt.exists():
            shutil.copytree(src, tgt)
            added.append(name)
        else:
            kept.append(name)
            if hash_tree(src) != hash_tree(tgt):
                if args.adoptar:
                    shutil.rmtree(tgt)
                    shutil.copytree(src, tgt)
                    diverged.append(f"{name} (ADOPTADO del catalogo)")
                else:
                    diverged.append(f"{name} (copia local distinta del catalogo)")

    for name in sorted(set(old_manifest) - members):
        removed.append(name)

    manifest = {"version": 2, "source_root": str(CATALOG),
                "policy": "membresia por referencia en el proyecto; el catalogo es el maestro",
                "skills": {}}
    for name in sorted(members):
        src = cat[name]
        tgt = SKILLS_DIR / src.relative_to(CATALOG)
        if tgt.exists():
            manifest["skills"][name] = {
                "origin": str(src),
                "origin_rel": str(src.relative_to(CATALOG)).replace("\\", "/"),
                "why": why.get(name, ""),
                "files": hash_tree(tgt),
            }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"catalogo: {len(cat)} skills | miembros del proyecto: {len(members)}")
    print(f"nuevas copiadas : {len(added)}")
    print(f"ya presentes    : {len(kept)}")
    print(f"divergentes     : {len(diverged)}")
    print(f"ya no referidas : {len(removed)}")
    for n in diverged:
        print(f"   DIVERGE {n}")
    for n in removed:
        print(f"   SALE   {n}")
    for n in added:
        print(f"   NUEVA  {n}  ({why.get(n,'')})")
    print("\n--adoptar sobrescribe las divergentes con el catalogo")
    return 0


if __name__ == "__main__":
    sys.exit(main())