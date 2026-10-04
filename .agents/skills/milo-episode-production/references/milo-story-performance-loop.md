# milo-story-performance-loop v1.0 — ciclo adversarial multi-LLM basado en evidencia

Reemplaza la dependencia de un solo LLM que genera un guion y se autocalifica. La unidad que compite es CONCEPTO + apertura 0–5 s + motor de escalada + payoff (nunca el guion aislado).

## 1. Candidatos independientes

Hermes genera ≥3 candidatos independientes (conceptos distintos, no variantes del mismo). Cada candidato trae: concepto, apertura 0–5 s completa (primer frame, hook/voz, conflicto, open loop, progresión), motor de escalada, payoff, guion con conteo/duración. Se persiste `01_historia/candidate_pool.json` (uno por candidato, con todos los campos).

## 2. Opening Lab (por candidato, antes de competir)

Mínimo 3 aperturas 0–5 s MATERIALMENTE diferentes por candidato (distinto primer frame, distinto conflicto/contradicción, distinto open loop). Cada apertura se puntúa con HOOK_SCORE y EARLY_RETENTION_SCORE. Elegible solo si HOOK_SCORE ≥85 y EARLY_RETENTION_SCORE ≥90. Regla anti-compensación: un hook mediocre NO se compensa con un viral global alto — la apertura debe pasar por sí sola.

## 3. Revisión adversarial (evidencia, no opiniones)

El panel LLM ataca cada candidato elegible y Hermes defiende con evidencia: cada ataque/defensa cita segundos concretos 0–5 s, el motor de escalada y el payoff. Sin citas = descartado como ruido. Se persiste `01_historia/adversarial_reviews.json` (ataques, defensas, veredicto por candidato).

## 4. Selección

Gana el candidato con mejor evidencia neta (apertura + escalada + payoff + supervivencia adversarial). Se persiste `01_historia/selection.json` (ganador, motivos citables, perdedores con causa) y `01_historia/story_evidence.md` (resumen humano-legible de por qué gana). Solo el ganador pasa a FASE 2 / packaging.

## 5. Performance feedback loop

Tras publicar, las métricas reales del video (retención 0–5 s, completitud, compartidos) se anexan a `story_evidence.md` y alimentan los umbrales futuros: un patrón ganador/perdedor repetido ajusta pesos con evidencia, nunca por intuición.

## 6. AUTO-RECOVERY general (Hermes no se detiene ante lo solucionable)

Ante cualquier bloqueo que Hermes pueda razonablemente solucionar por sí mismo: detectarlo → formularlo técnicamente → inyectarlo a los LLM disponibles (vía `chrome-cdp-injection.md`, contrato `inject()`) → contrastar soluciones → aplicar la de MENOR RIESGO → re-ejecutar QA → continuar automáticamente. `LLM_RECOVERY_ESCALATION` (§7 del protocolo CDP) es la instanciación de este loop para fallos de automatización. El humano queda ÚNICAMENTE para lo realmente irresoluble o lo que requiera información, credenciales o decisiones externas que Hermes no posee. Pedir intervención por un fallo corregible cuenta como fallo del protocolo.

## 7. Estructura narrativa fija

HOOK → SITUACIÓN → DECISIÓN → ESCALADA → CONSECUENCIA → RECONTEXTUALIZACIÓN → REMATE, con hook perceptible ≤1 s, open loop ≤3 s y cambio significativo antes de 5 s. Los umbrales viven en el Master y en HARD_GATES; este archivo no los duplica, los invoca.
