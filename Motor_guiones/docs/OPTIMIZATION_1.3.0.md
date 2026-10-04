# Guion 1.3.0 — optimización implementada

Cinco especialistas conservados. Canon/personajes/semilla/constraints/history intactos; mining se reduce a párrafos completos relacionados por términos de semilla/territorio, hasta 3500 bytes, con declaración explícita de selección incompleta. Síntesis y crítico reciben el contexto completo. No se acredita novedad absoluta a partir de excerpts.

Especialistas: propuestas <=3, evidencia/riesgos <=6, handoff, instrucción <=600 palabras y límite duro de 6000 bytes de JSON UTF-8. Una respuesta excesiva se conserva y bloquea sin truncarla ni reintentar automáticamente. Este límite no controla los tokens de razonamiento internos del proveedor. El sintetizador recibe contrato de writer y schema reales; el guard valida base_package y cinco informes.

Una revisión por llamada. Segunda independiente cuando hay scores 90–92, confianza no alta, desacuerdo o candidato reparado, en todos los intentos. Sesiones separadas reciben el mismo candidato/contexto, sin notas de otro crítico. Scorecard original >=90 por dimensión/perspectiva/compuesto y cero críticos preservado. No se revisa otra vez un candidato sin cambio o sin repair aplicable. Errores técnicos terminan antes de pagar crítico.

script_cache: claves por payload/command/timeout/runtime del modelo/proveedor y contratos/código. Hashes del resultado verificados. Cada especialista completado se guarda inmediatamente; si falla otro, reanudar reutiliza los completos. Síntesis, críticas y repairs también tienen caché. Los informes anteriores extensos del ZIP no se importan como aprobados automáticamente.

script_progress.json se actualiza por tarea: RUNNING, COMPLETED, CACHED, BLOCKED. script_failure.json registra fallos; script_stage_metrics.json registra etapa completada. script_optimization.lock exclusivo y separado de locks históricos. No borrar production.lock antiguo; detener procesos antes de instalar. Estado RUNNING persistido no prueba que el proceso siga vivo. El hilo espera a trabajadores ya iniciados al fallar: conserva resultados sin dejar procesos huérfanos; no hay cancelación instantánea de sesiones externas.

Concurrencia y timeout conservados (5 y 2700s en la base recibida); modelo/proveedor no se modifican. Comparar concurrencia solo en una prueba real autorizada. Este parche no promete minutos concretos ni cambia max_duration_s=45 de esta base; la compatibilidad con el objetivo 24–32s de voz debe pasar su gate existente.
