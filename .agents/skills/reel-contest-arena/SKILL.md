---
name: reel-contest-arena
description: "Use when the user asks for a video script of any kind."
version: 0.4.0
author: Hermes Agent
license: MIT
---

# Reel Contest Arena

Core principle: no single LLM crowns a script. This skill is the MANDATORY entry point for every script request: no script is delivered without passing CREATE → VERIFY → QUALIFY → (REWRITE + DUEL when competing versions exist). Four LLMs (ChatGPT, DeepSeek, Gemini, Grok) create, audit, and blind-judge in the same Chrome window (port 9222, separate tabs), and the winner emerges from order-reversed pairwise duels — never from one 0–100 opinion.

## When to Use

- User asks which script version, hook, or rewrite is best.
- Any "pick the winner" decision across LLM proposals.
- Validating a publish verdict (PUBLICAR) before spending on production.

## Hard Constraints

- All four AIs live as tabs in the ONE kit Chrome (port 9222, profile `.chrome-chatgpt`). Never the daily Brave. Sequential turns only — one poller at a time, even across tabs.
- Transport: `tasks/multi_inject.js` (adapters for chatgpt/deepseek/gemini/grok) + `tasks/contract_block.txt` (`prepend_contract:true` for audits). ChatGPT-only loop: `tasks/script_rev_inject.js`. Both end `process.exit()`, never `browser.close()`.
- Blindness: duel prompts carry NO author names, only A/B texts. Each pair judged TWICE (A-vs-B and B-vs-A). A vote that flips with order = discarded (position bias).
- Judges never vote on their own work.
- Artifacts idempotent in `out/`: `<id>__<platform>.md` + `<!-- hash duration -->`. Never overwrite valid captures.

## Workflow (OBLIGATORIO, sin salidas anticipadas)

Every script request runs ALL five phases in order. Delivering a script after QUALIFY without DUEL is a violation. Phase-gate checklist (all boxes required before delivery):

1. **CREATE.** One V1 per LLM in its own thread (or a single human draft). Save `out/<id>_v1__<platform>.md`.
1B. **SELF-AUDIT (own V1, fixed format).** Cada LLM se autoevalúa: STRENGTHS / WEAKNESSES / RISKS / IMPROVEMENT. Sin complacencia.
2. **VERIFY.** Strict contract audit (`prepend_contract:true`): gates (originality, factuality, hook-payoff, feasibility) + 0–4 items with quoted evidence + AI-genericity flags + verdict READY/OPTIMIZE/REWRITE/HOLD. Any critical FAIL = HOLD, out of the contest.
3. **QUALIFY.** Survivors get a publish rating (0–100/dimension + PUBLICAR/OPTIMIZAR/NO PUBLICAR + one-line motive). Rank, but do NOT crown yet. Score the viral-editor set: hook ≤3s scroll-stop; progressive tension (misterio→pistas→escalada→revelación parcial→pregunta abierta); cinematic visual states; character identity (never plot-tools); theory-generating anomaly ("¿cómo es posible eso?"); non-generic CTA (never "¿qué opinas?"). NOTE: legacy shortcut — new runs MUST use `tasks/qualify_template.txt` (gates + 0–4 items with quotes, totals computed in code per cinematic-reels-system, never by the LLM).
4. **RETENTION MAP (mandatory).** Temporal map before rewriting: 0–3s hook, 5–15s primera anomalía, 15–30s escalada, últimos 5s payoff + comentario. Marcar valles (beats que solo informan). Feeds REWRITE.
5. **REWRITE.** Each LLM rewrites applying ONLY its own audit fixes. Output: script text only (~30s), no scores. Save `out/<id>_v2__<platform>.md`.
5B. **CROSS-REVIEW (attack others).** Cada LLM revisa historias ajenas buscando por qué fallarían. Prohibido 'me gusta/está bien'.
6. **DUEL (mandatory).** Round-robin pairs × 2 orders. Judge prompt: "Dos guiones de 30s para Facebook Reels. A: … B: … Vota el mejor por especificidad, payoff y no-cliché. Responde con: GANADOR: A|B + motivo con evidencia + PUNTOS DÉBILES del ganador + CONFIANZA (alta/media/baja). Variables: Hook, Retention, Character Fit, Originality, Emotional Payoff, Production Feasibility." Tally wins; head-to-head breaks ties. Save `out/duel*.md`.
7. **LINE-EDIT (winner only).** Micro-copy pass on the winner before FINAL qualify: semantic precision of every line (no physically-odd phrasing), closing bridge before the CTA, CTA strength. Rewrite weak lines only, facts preserved. Checklist: semantic precision per line; closing bridge before CTA; theory-generating CTA; minimal character identity; one impossibility/anomaly intact. Save `out/<id>_lineedit__<platform>.md`. 8. RED TEAM (winner only): misión destruir el guion antes de producción; hallazgo crítico → REWRITE; si sobrevive → FINAL. Save `out/<id>_redteam__<platform>.md`.
9. **FINAL WRITER (synthesis, not copy).** Sintetiza la mejor solución desde propuestas + críticas + scores + duelo.
10. **MEMORY UPDATE.** Tras aprobar: winning/failure patterns + memoria de dominio.

## Módulos virales (contenido corto de alta retención)

1. **SIMULACIÓN DE AUDIENCIA.** Antes de calificar, simula primera vista por tramos: 0–3s (¿qué detiene el scroll? ¿pregunta inmediata? ¿anomalía/conflicto/promesa?), 3–15s (¿la curiosidad sube? ¿cada frase aporta info nueva? ¿riesgo de abandono y dónde?), mitad (¿nueva pregunta? ¿escalada? ¿necesidad de llegar al final?), últimos segundos (¿el payoff recompensa? ¿genera comentarios/teorías?).
2. **MYSTERY DENSITY.** Cuenta las preguntas que el guion abre cada ~10s (pregunta inicial, pistas nuevas, contradicciones, info incompleta, elementos inexplicables), cada una con su cita. Un guion de misterio debe abrir más preguntas de las que responde.
3. **PRUEBA DE IMAGEN MENTAL.** Por escena: ¿puedo imaginar un plano de cámara? Si no, exige objeto concreto, acción observable o elemento simbólico. Prohíbe frases abstractas.
4. **FINAL VIRAL.** El último 10% debe traer revelación, nueva pregunta, contradicción o invitación a teorías. Nunca un cierre genérico.
5. **REGLA DE PRESERVACIÓN.** No tocar líneas con alto impacto visual, alta curiosidad, frases memorables o identidad narrativa. Toda reescritura de una línea fuerte exige justificar por qué la nueva genera mayor tensión. (Refuerza: reescribir solo beats 0–1.)
6. **CURIOSITY GAP POR FRASE.** Línea por línea: ¿informa / abre pregunta / sube tensión / es reemplazable? Marcar y reescribir las que solo informan.
7. **MISTERIO CREÍBLE.** Cada anomalía: ¿imaginable? ¿explicación posible aunque no revelada? ¿preguntas sin romper la suspensión de incredulidad? Nada aleatorio sin conexión causal.
8. **PAYOFF ANTES DEL CTA.** El final resuelve parcialmente una pregunta Y abre una nueva; la pregunta nace del misterio, nunca un 'Comenta tu teoría' suelto.

## Multi-Chrome (4 ventanas, 16 carriles)

Cuatro Chromes: puertos 9222–9225, un perfil por ventana (`.chrome-chatgpt`, `.chrome-grok2/3/4`). Cada IA logueada en las 4 ventanas con cuenta DISTINTA (misma cuenta no multiplica límites). Lanzar con `launch-browsers.bat` (9222) + `launch-extra-chromes.bat` (9223–9225); el usuario loguea cada perfil una vez.

`tasks/multi_inject.js`: round-robin de puertos por plataforma; `task.port` fija puerto para continuidad de hilo (misma conversación); ante `RATE_LIMITED` (límite en pantalla o en respuesta) failover automático al siguiente puerto. Stuck-tab (SUBMIT_NO_CLEAR sin texto de límite): no es la cuenta, es la pestaña — mover la tarea a un hilo sano en otro puerto con prompt autocontenido (fixes embebidos, sin referencias a 'tu auditoría anterior'). Bloqueo temporizado: si el límite indica espera (ej. 13h), ese puerto queda bloqueado ese tiempo (`tasks/port_state.json`) y la rotación lo salta hasta liberarse. Gemini: ante cualquier dificultad (respuestas cortas, eco, mismatch, hilo trabado), abrir hilo fresco y reinyectar. Sin restricción de modelo: vale cualquier variante que responda.

## Pipeline editorial viral (orden obligatorio)

1. Género del guion (ajusta criterios: misterio, humor, etc.).
2. AUDITORÍA DE VIRALIDAD: ¿scroll-stop en 3s? ¿pregunta abierta inicial? ¿cada frase sube curiosidad o solo informa? ¿pregunta nueva cada 5–10s? ¿el final obliga a teorizar?
3. SIMULACIÓN DE ESPECTADOR (ver Módulos virales §1).
4. MAPA DE RETENCIÓN (0–3 hook / 5–15 anomalía / 15–30 escalada / últimos 5s payoff).
5. OBJETOS NARRATIVOS: por objeto — ¿visual? ¿genera preguntas? ¿significado? ¿escena memorable? Fortalecer antes de eliminar.
6. PERSONAJES CON FUNCIÓN: testigo/víctima con historia previa, motivo, acceso privilegiado, rasgo memorable — nunca solo 'un X dijo…'.
7. FINAL + scores + TABLA obligatoria (Elemento|Estado|Acción: Hook, Misterio inicial, Pistas, Personajes, Escenas visuales, Giro final, Comentarios esperados) + mejoras que suban tensión/claridad/misterio/emoción sin perder la esencia.
Pregunta guía de toda revisión: '¿hará que alguien deje de deslizar, vea hasta el final y escriba una teoría?'

## STORY DNA + Contamination (v2.1)

STORY DNA EXTRACTION antes de CREATE (núcleo, verdad humana, conflicto, motor, objeto, imagen, promesa, payoff, riesgos; preservar, no convertir — como campos del prompt CREATE, no ronda extra). IDEA PRESERVATION CHECK antes de aprobar. PROMPT CONTAMINATION: brief-info repetida sin función → marcar y limpiar. Toda regla crítica vive en CREATE+VERIFY+REWRITE.

## Council v3.2 (multi-agent evaluation)

Orden: IDEA → DNA → WRITERS → SELF AUDIT → CROSS REVIEW → SPECIALISTS → DUEL → RED TEAM → FINAL WRITER → MEMORY UPDATE. Especialistas por dimensión, no estilo.

## Council v3 (roles + contratos + memoria)

Roles: research, story_dna, writers, retention, emotion, originality, red_team, showrunner (ver D:/hermes/operator-kit/council/agents/agent_roles.md). Contratos: objetivo, evidencia, score, problemas, recomendación. Duelos con orden invertido + supervivencia al red team. Memoria: winning/failure_patterns.json (sembrados de actas; update por episodio).

## CORE / DOMAIN routing (v3.1)

El Core es genérico (no conoce personajes/mundos). Antes de CREATE: identificar dominio → cargar solo sus contratos (`D:/hermes/operator-kit/domains/<dominio>/`) → correr la arena. Dominios character-driven pasan EMBODIMENT CHECK antes de FINAL (FAIL → REWRITE). Jamás contaminar prompts generales con reglas de dominio.

## MILO DOMAIN OVERRIDE v3.40 (takes precedence over generic mandatory-duel wording)

For Project Milo, use D:/hermes/operator-kit/council/MILO_CORE_V340_ACTIVE.md. Generic CREATE→VERIFY→QUALIFY→REWRITE→DUEL remains for other domains; Milo uses Human Insight → Mechanism → Silent Visual → Structure Gate → optional Voice Pass → Milo Voice Gate → Red Team → Micro-Fix/Skip → Final Editor → Qualify → Memory. DUEL optional (only 2 genuinely different candidates within 3 points). R001 voice/humanity reference; R017 mechanical/iconicity reference.

## V3.13 — Contradiction-first

Ideas nacen de contradicción (deseo→exceso→contradicción→frase→objeto), no de objeto. PHRASE SURVIVAL gatea antes de Story Architect. Banco estructurado en `memory/phrase_bank.json`.

## V3.12 — Compresión viral

PHRASE SURVIVAL (90/70) + VISUAL WORD (palabra imaginable o ICONIC capado). Una historia excelente se comprime a una frase y sigue funcionando.

## V3.11 — Recall (tri-state, universo primero, rescate)

Gate KILL/OPTIMIZE/PASS + puerta de rescate (Desire≥85+Extreme≥70+Irony≥75 → OPTIMIZE obligatorio). OBJECT UNIVERSE VALIDATOR antes de puntuar. Bandas por dimensión; altos para publicar, nunca para explorar.

## V3.13 — Contradiction-first

Generar desde la contradicción: deseo → exceso → contradicción → frase → objeto (nunca objeto primero). PHRASE SURVIVAL antes de Story Architect; sin frase superviviente no hay guion.

## V3.12 — Irony gate (solo criterio)

Gate en VERIFY (`council/MILO_V310_GATE.md`): desire ≥70, extreme ≥80 (muere <60), irony ≥80, contradicción ≥75, LITERAL SUCCESS ≥70. Ideas declaran DESIRE/FUNCTION/EXTREME/IRONY. Fixtures R017-R019.

## V3.9 — Function Inversion

Gate pre-publicación (`council/FUNCTION_INVERSION_GATE.md`): el objeto debe ganar por exceso de función, no por rotura. Absurdity check: demasiado bueno > demasiado destructivo. FAIL → Micro-Fix.

## V3.8 — Surgeon + Editor + DNA Score

STORY SURGEON entre VERIFY y DUEL (`agents/story_surgeon_agent.md`): READY o 1 fix; si toca estructura → REWRITE, no cirugía. Editor-in-Chief (`council/EDITOR_IN_CHIEF.md`): pondera críticas, no promedia; desempata por DNA SCORE; documenta qué se descartó. MILO DNA SCORE (`council/MILO_DNA_SCORE.md`): 5×20; <80 vuelve a Micro-Fix.

## Micro-Fix Agent v1.0 (tras RED TEAM, antes de QUALIFY)

Protocolo: `council/MILO_MICRO_FIX_PROTOCOL_v1.md`. Solo si total>75 + idea PASS + red team fixable + rewrite_risk low. DNA LOCK previo obligatorio (`agents/dna_lock_agent.md`). NO-TOCAR si >90 sin hallazgo crítico. DELTA REVIEW: si la claridad mata la rareza → RECHAZAR. Fixes exitosos a `memory/micro_fix_learnings.json`.

## Puertas v3.5 (antes y durante el council)

UNIVERSE GATE (`council/UNIVERSE_GATE.md`): valida mundo antes de escribir — sin nombres ajenos, reglas Milo, física cotidiana, sin lore externo. FAIL = idea descartada.
REGLA CAUSAL: defecto → decisión → consecuencia inevitable. El fracaso jamás es casualidad ni mala suerte del mueble.
REGLA ANTAGONISTA: el objeto inicia, escala y ejecuta el giro final; si desaparece del frame decisivo, REWRITE.
Calidades separadas: idea (¿vale invertir?) → historia (¿puede ser viral?) → video (¿puede producirse? → `agents/video_readiness_audit_agent.md`).

## Filtro rápido + niveles v3.6

FAST VIRAL FILTER antes de escribir (`v3_6/protocols/FAST_VIRAL_FILTER.md`): 6 preguntas, falla 3 = DESCARTAR. Inversión por niveles: C descarte · B normal · A pipeline completo · S máxima. Audience simulation solo A/S.

## 3 LLMs estándar + paralelismo (v3.6)

Rotación fija: ChatGPT + Gemini + DeepSeek (Qwen retirado 2026-09-11, Grok pausado). Duelos: 3 pares × 2 órdenes = 6 votos; qualify cruzado en ciclo de 3.
Paralelismo real con `tasks/parallel_inject.js`: agrupa tasks por plataforma y lanza un `multi_inject` por LLM en paralelo (3×). Regla de seguridad: misma plataforma = secuencial en su hijo (un poller por conversación); plataformas distintas = concurrentes (pestañas distintas). Fases paralelizables: ideas, V1, verify, V2, duelos (por juez), qualifies, fixes. Secuenciales: red team después del duelo, final writer después del RT, micro-fix después del qualify.

## Funnel Milo V2 (v3.4)

Rotación fija: ChatGPT + Gemini + DeepSeek (Qwen retirado 2026-09-11, Grok pausado). Duelos: 3 pares × 2 órdenes = 6 votos; qualify cruzado en ciclo de 3.
Paralelismo real con `tasks/parallel_inject.js`: agrupa tasks por plataforma y lanza un `multi_inject` por LLM en paralelo (3×). Regla de seguridad: misma plataforma = secuencial en su hijo (un poller por conversación); plataformas distintas = concurrentes (pestañas distintas). Fases paralelizables: ideas, V1, verify, V2, duelos (por juez), qualifies, fixes. Secuenciales: red team después del duelo, final writer después del RT, micro-fix después del qualify.)

El Council v3.2 no corre sobre todas las ideas: GENERACIÓN MULTI-LLM → IDEA QUALITY GATE (identificación, hook visual, giro, producción) → STORY COUNCIL → VIRAL GATES → VIDEO READINESS → producción. Ver `protocolos/MILO_V2_PRODUCTION_FUNNEL.md` e `IDEA_GENERATION_MULTI_LLM_PROTOCOL.md`. Agentes: insight, comedia, visual, viral, guardián Milo, arquitecto, director, QA, aprendizaje (`agents/`, `architecture/`).

## Visual finalize gate (v3.3)

Ningún guion se aprueba sin VISUAL PAYOFF DESIGN (final emocional / visual / memorable) + REGLA 17 (último plano = imagen describible, con ironía, memorable sin narración). Acciones internas → observables. Auditor visual entre FINAL SCRIPT y VIDEO DIRECTOR.

## Delivery Gate

A script is delivered ONLY with: V1 file + 4 qualify verdicts + V2 rewrites + 12 duel files (4 LLMs) + declared WINNER + winner text file + FINAL qualify of the winner (0–100/dimension + verdict across the 4 LLMs, `out/<id>_FINAL__<platform>.md`). Missing any piece = work incomplete, say so plainly and continue.

## Final Message (mandatory)

Every completed run ends with the WINNER script text in full + its FINAL scores (one line per LLM + verdicts). Never close with files alone.

## Terminal State (when the run is DONE)

DONE requires ALL four: (1) improved version(s) saved (V2+ rewrites), (2) full duel set run (12 files, 4 LLMs) with WINNER declared, (3) FINAL qualify of the winner across the 4 LLMs saved (`out/<id>_FINAL__<platform>.md`) or consolidated acta, (4) winner text + final scores delivered IN CHAT. Missing any piece = INCOMPLETE: say so plainly and continue. Never present partial results as final.

## Arena a 4 LLMs (Qwen ocupa el slot de Grok)

Grok pausado por límites; Qwen (chat.qwen.ai, adaptador verificado end-to-end) ocupa su slot: ChatGPT/DeepSeek/Gemini/Qwen con matriz completa de 12.

## Post-FINAL: production layer (video)

El Council termina en guion + acta. Producir corre en `D:/hermes/operator-kit/agents/video_director_agent.md` bajo `protocolos/video_generation_contract.md`; patrones en `memory/video_winning_patterns.json` (success_rate solo con dato real). Milo converge con producción existente (milo-episode-production §5b–§6).

## Duel Matrix (4 LLMs → 6 pairs × 2 = 12 turns)

| Pair | Judge (not author) |
|---|---|
| Grok-vs-Gemini | ChatGPT |
| Grok-vs-ChatGPT | DeepSeek |
| Grok-vs-DeepSeek | Gemini |
| Gemini-vs-ChatGPT | DeepSeek |
| Gemini-vs-DeepSeek | Grok |
| ChatGPT-vs-DeepSeek | Gemini |

Generate tasks with node (JSON.stringify — never hand-build; python3 may be broken on this host). Run sequentially: `node tasks/multi_inject.js tasks/duel*.json`. Tally `GANADOR:` lines per file; map A/B back to authors.

## Verdict Rules

- Winner = most duel wins; tie → direct head-to-head result; still tied → human decides.
- Report: wins per version + deciding duel quote + file paths. One line per loser, no eulogies.
- Feed the winner back as V(n+1) into `script-revision-chatgpt` for the next loop.

## Proven Baseline (Faro 001, 2026-09-11)

Qualify: ChatGPT 87, Grok 88, Gemini 79, DeepSeek 76. Strict audit flipped three approvals to REWRITE/OPTIMIZE. Duel 12/12 order-stable → Grok V2 wins (sensory specificity: borde roto, olor a quemado, nota a medias, pluma húmeda). Files: `out/faro_*`, `out/duel*`, `out/script_rev_*`.

## Red Flags

- Crowning from a single LLM's 0–100.
- Judge voting on own text.
- Unblinded duels (names in prompt).
- Single-order votes presented as consensus.
- Two pollers on 9222 at once.

## Consolidación V3.14–V3.25 (council Milo, 2026-09-11)

- V3.14 memoria conceptual: `memory/contradiction_atlas.json` (desire/extreme/contradiction/visual_word/universality/object_family/winning_objects). Transfer validado 10/12 del patrón.
- V3.15 autodepuración: PATTERN DISTANCE (90 nuevo principio / 70 familia / <70 superficial no cuenta); `memory/atlas_saturation_v315.json` (desponderar sostener/inmovilizar, proteger/endurecer, ordenar/sellar).
- V3.16 HUMAN GROUNDING: deseo en frase cotidiana, cadena mecánica visible, cero laboratorio/metáfora. V3.17 VISUAL CAUSALITY (≥80, sin fuerza invisible) + WORD DIVERSITY (bloque/ladrillo/pieza/muro/roca/piedra/mármol/soldó/taco/moho/pantano penalizan).
- V3.18 OBEDIENCE (¿cumplió literalmente, demasiado bien? <70 no TOP) + ICONICITY GAP (qué falta al 91). V3.19 ICONICITY POTENTIAL=(UD+VWP+CC+EC)/4 + LIFT SENSITIVITY (tesoro escondido).
- V3.20 puertas secuenciales: OBEDIENCE≥80 → Lift → ICONICITY≥80 → producción. V3.21 HUMAN STAKES/ACHIEVEMENT LOSS (logro consumado destruido 90+; sin logro previo no hay 90+).
- V3.22 ICONICITY MODEL FROZEN (`council/MILO_V322_ICONICITY_MODEL.md` + `MILO_CORE_V322_FROZEN.md`): HD.18+FE.12+OB.10+AL.18+CD.15+PS.17+VWP.10; Desire+Loss+Phrase=53%. Descartes: HD<70, AL<60, FE<70, PS<70, VWP<60, OB<75.
- V3.23 conversión: SCRIPT SURVIVAL pre-Architect + ANTI-ANIMISM post-Writer (pasiva refleja, 0 verbos intención) + MATERIAL RULE (mismo material en estado extremo: surcos/losa/pasas ✅; material nuevo ❌) + CONTRADICTION DISTANCE (r≈0.75 con iconicidad; sin palabra concreta no convierte).
- V3.24 cascada + SEED GATE (FE≥80/IRONY≥80/OB≥80/GROUNDING≥75/MATERIAL≥80; rescate 76-79 solo si IRONY≥84): GPT deseo-logro-pérdida → Gemini imagen-frase → DeepSeek física-gate → Hermes consolida. POTENTIAL × EXECUTION. R025: caída semilla→guion eliminada (+1.2/+3.7 vs -19).
- V3.25 STAKE DOMAIN FILTER (`MILO_CORE_V325_FROZEN.md`): pérdida que interrumpe necesidad (comer/vestir/higiene/descansar/trabajar/crear/comunicar/proteger) → continuar; estética → bajar prioridad. R027: físico 92.0/85.9 vs estético 87.0/~80. R028: stake alto eleva HD/AL pero CD/PS siguen siendo el muro; mejor guion 84.34, R017 (91.74) intacto.
- Referente canónico: R017 grapadora 91.74 (frase sola 94.8). Regla de producción: juez estricto con reglas duras EN SEMILLA, no solo en duelo.

## Consolidación V3.26–V3.30 (élite, 2026-09-11)

- V3.26 WORD LIFT + banco `memory/iconic_visual_word_bank.json` (85 palabras, lift medio +3.7; yeso +13, nudo/losa/teja +8). REGLA: banco solo para palabra débil; si la original ya es concreta (tapón 91), no tocar (-8).
- V3.27→v3.28 VISUAL WORD corregida: el lift léxico B→A falla (pergamino -3.8 por material); solo refinar DENTRO de categoría (nudo→trenza +5.0). La palabra élite nace de la física, no del tesauro.
- V3.29→v3.30 FORM EMERGENCE (puerta dura): palabra final = SUSTANTIVO con silueta (armadura/tapón/cicatriz/trenza). Corte validado DISCOVERED 82-96 vs WEAK 56-64. Sin sustantivo-objeto no hay 90+.
- TRÍPODE ÉLITE (confirmado): forma emergente (necesaria, no suficiente; L1 84.40 con VWP 86) + inversión inesperada + logro consumado destruido. R017 91.74 las tiene las tres.
- R031: FE/AL ya a nivel élite; brecha restante CD+PS. R028: stake alto eleva HD/AL, mejor guion 84.34; inflación semilla persiste (95→81) → juez estricto EN SEMILLA.

## V3.31 — Trípode élite + doble gate ciego: forma + inversión inesperada + logro consumado = techo 84-86 (Y1 85.66). Para 90+: espectador ciego (resultado no predecible) + frase sola (contradicción sin imagen).

## R032 (400 semillas): mejor guion 83.88 (tapón), R017 +7.86. Mecánica resuelta (FE/OB/AL 84-88); brecha = CD/PS/VWP + novedad. El 91.7 semilla no sobrevivió (palabra reciclada). Juez estricto en semilla siempre.

## V3.35 — No fantasy escape: forma primero sin deseo = espectaculo, no Milo. Orden: deseo + material + forma.
