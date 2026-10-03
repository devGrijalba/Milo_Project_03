# MILO SEEDS — PARTE 08

Banco: `2.0.0`
Registros: `0701–0800`

## REGLAS

- Datos canónicos.
- No inventar campos.
- No recalcular seed_hash.
- El seed_id puede normalizarse desde el encabezado lógico/registro según `18_SEED_HEADER_NORMALIZATION.md`.

# MILO-R0701 — Sillón: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0701",
  "seed_hash": "8f29143dcec7c2fa08bcc3d7f9dbc2c2ad393a5b44b066e314691d96f6ab59ff",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_1",
  "titulo": "Sillón: el gesto que llegó a la persona equivocada",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "sillón",
  "giro_posible": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
  "desarrollo_requerido": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0701",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC01",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "sillón",
      "reinterpretacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0702 — Sillón: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0702",
  "seed_hash": "cf2db47cb4620ab8ce82f1eee981521f603b8e7d633b258533d335ae3094fd93",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_2",
  "titulo": "Sillón: la copia que no funcionó",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "sillón",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0702",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "sillón",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0703 — Sillón: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0703",
  "seed_hash": "388db1ed2796e4328362175ff1a27e28904694b6599eb1e53ed886c529a9b50c",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_3",
  "titulo": "Sillón: el favor convertido en deuda",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "sillón",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0703",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "sillón",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0704 — Sillón: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0704",
  "seed_hash": "eca0cefee68c0064efe772012f98df0f244688887a3a343121a35c86c1b288f1",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_4",
  "titulo": "Sillón: dos personas, dos necesidades",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "sillón",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0704",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "sillón",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0705 — Sillón: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0705",
  "seed_hash": "eea422ac790bd7ab15f094016a993f5a157e430e5bf41053d971b268bce3e9c6",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_5",
  "titulo": "Sillón: el acuerdo que nadie había entendido",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "sillón",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0705",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "sillón",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0706 — Sillón: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0706",
  "seed_hash": "f69518b563550022b298179d44ced743e6777a4a09b152a9ad00af9f0dce5ef4",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_6",
  "titulo": "Sillón: la ayuda que cambió algo querido",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "sillón",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0706",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "sillón",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0707 — Sillón: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0707",
  "seed_hash": "391d07f97fd669cf8876a398b67f1d8f0b302fc3744caa9bf12d6145e636851e",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_7",
  "titulo": "Sillón: la pregunta que no quería hacer",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "sillón",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0707",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "sillón",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0708 — Sillón: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0708",
  "seed_hash": "2fbc826deb9768454da187c572106fd898c725ae5935c545fa9ba850aed7a657",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_8",
  "titulo": "Sillón: el recuerdo que tenían distinto",
  "semilla": "Milo se sienta antes de acabar sus pendientes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "sillón",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0708",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo se sienta antes de acabar sus pendientes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "sillón",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0709 — Sillón: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0709",
  "seed_hash": "d0a5150c7df2bc3141b6bc217f8e90a7e152f7bb598c8ada479c0636ae173e51",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_9",
  "titulo": "Sillón: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "sillón",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0709",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "sillón",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0710 — Sillón: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0710",
  "seed_hash": "ec8901233a4fc67a35f4152bc47887aedb28447c355445871f3be0fe34f73cee",
  "family_id": "F071",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_10",
  "titulo": "Sillón: el cuidado que necesitó permiso",
  "semilla": "Milo se sienta antes de acabar sus pendientes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo se sienta antes de acabar sus pendientes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "sillón",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0710",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "reorganiza tareas sin castigarse",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde sillón y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo se sienta antes de acabar sus pendientes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se sienta antes de acabar sus pendientes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "sillón",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-S0711 — Lista: la primera vez

```json
{
  "seed_id": "MILO-S0711",
  "seed_hash": "b7acfc7bb341476f138eef825f11540fb4d859e01915bdbdbb975f7c08ae9978",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "primera_vez",
  "titulo": "Lista: la primera vez",
  "semilla": "Milo mira pendientes al final del día. Solo ve lo que falta. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "solo ve lo que falta",
  "accion_visible": "Milo mira pendientes al final del día",
  "objeto_emocional": "lista",
  "giro_posible": "registra una tarea terminada y deja otra para mañana",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo"
  ],
  "personajes_secundarios": "Resolver identidad y disponibilidad de referencias desde canon antes de producir; no inventar anclas aprobadas.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PENDING_SCRIPT_REVIEW",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 85,
    "compuesto": 88.75,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "solo ve lo que falta",
      "conflicto": "solo ve lo que falta",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "registra una tarea terminada y deja otra para mañana",
      "visual": "Milo mira pendientes al final del día",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día",
      "objeto": "lista",
      "reinterpretacion": "registra una tarea terminada y deja otra para mañana",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "solo ve lo que falta"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0712 — Lista: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0712",
  "seed_hash": "df605d8d86ef6251b22c06054dbca80acdbb23e78215a57534a3f505f9bbad4c",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_2",
  "titulo": "Lista: la copia que no funcionó",
  "semilla": "Milo mira pendientes al final del día. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo mira pendientes al final del día. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "lista",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0712",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo mira pendientes al final del día. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "lista",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0713 — Lista: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0713",
  "seed_hash": "222a3b7e782edece18663402fe1e6d5c8cb2992781c2aee0df1a545ccfc87d8b",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_3",
  "titulo": "Lista: el favor convertido en deuda",
  "semilla": "Milo mira pendientes al final del día. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo mira pendientes al final del día. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "lista",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0713",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo mira pendientes al final del día. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "lista",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0714 — Lista: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0714",
  "seed_hash": "ab54d79ac53acef3d074f0ae7682b1fa7d56ce4895fa2c88b84a5814a7f582aa",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_4",
  "titulo": "Lista: dos personas, dos necesidades",
  "semilla": "Milo mira pendientes al final del día. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo mira pendientes al final del día. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "lista",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0714",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo mira pendientes al final del día. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "lista",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0715 — Lista: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0715",
  "seed_hash": "40f013a2cc8572ed84e3d1083b6420647a17f6b3c3ee27181f050f678a88badb",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_5",
  "titulo": "Lista: el acuerdo que nadie había entendido",
  "semilla": "Milo mira pendientes al final del día. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo mira pendientes al final del día. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "lista",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0715",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo mira pendientes al final del día. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "lista",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0716 — Lista: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0716",
  "seed_hash": "8c5c0d9d3ebc059dfa231520d79ccb70d7369059bed5c54a7996d67059938a87",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_6",
  "titulo": "Lista: la ayuda que cambió algo querido",
  "semilla": "Milo mira pendientes al final del día. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo mira pendientes al final del día. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "lista",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0716",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo mira pendientes al final del día. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "lista",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0717 — Lista: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0717",
  "seed_hash": "f490237681d22a950507d80cedf49a58c00076d559bea5b0728613ea3a5e96a0",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_7",
  "titulo": "Lista: la pregunta que no quería hacer",
  "semilla": "Milo mira pendientes al final del día. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo mira pendientes al final del día. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "lista",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0717",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo mira pendientes al final del día. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "lista",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0718 — Lista: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0718",
  "seed_hash": "76395b379a020e60391caf1dcfa3eb5b3e873af69f54aed46495d1000963ca3d",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_8",
  "titulo": "Lista: el recuerdo que tenían distinto",
  "semilla": "Milo mira pendientes al final del día. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo mira pendientes al final del día. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "lista",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0718",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo mira pendientes al final del día. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "lista",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0719 — Lista: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0719",
  "seed_hash": "fac47a23748866d30834940328b09b1050ef193f13fcadc8cadb1a0b75746ef4",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_9",
  "titulo": "Lista: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo mira pendientes al final del día. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo mira pendientes al final del día. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "lista",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0719",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo mira pendientes al final del día. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "lista",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0720 — Lista: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0720",
  "seed_hash": "d2924bed36f260ba458ef06c90229338ba52460f100c72c62b4f2d2abb92a8c6",
  "family_id": "F072",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_10",
  "titulo": "Lista: el cuidado que necesitó permiso",
  "semilla": "Milo mira pendientes al final del día. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo mira pendientes al final del día. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "lista",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0720",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "registra una tarea terminada y deja otra para mañana",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde lista y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo mira pendientes al final del día. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo mira pendientes al final del día. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "lista",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-S0721 — Lámpara: la primera vez

```json
{
  "seed_id": "MILO-S0721",
  "seed_hash": "945ef8197ec3743fe6e00f12f84a659fc298ef64c069ab3d75e317a1831efa14",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "primera_vez",
  "titulo": "Lámpara: la primera vez",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Teme perder control durante la noche. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "teme perder control durante la noche",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo",
  "objeto_emocional": "lámpara",
  "giro_posible": "anota el siguiente paso y se permite dormir",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo"
  ],
  "personajes_secundarios": "Resolver identidad y disponibilidad de referencias desde canon antes de producir; no inventar anclas aprobadas.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PENDING_SCRIPT_REVIEW",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 85,
    "compuesto": 88.75,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "teme perder control durante la noche",
      "conflicto": "teme perder control durante la noche",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "anota el siguiente paso y se permite dormir",
      "visual": "Milo apaga la luz aunque no resolvió todo",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo",
      "objeto": "lámpara",
      "reinterpretacion": "anota el siguiente paso y se permite dormir",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "teme perder control durante la noche"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0722 — Lámpara: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0722",
  "seed_hash": "570070d40f436dcf0e9d1244e4746833cdaec45e0bc7134aee10d8cf280ffe06",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_2",
  "titulo": "Lámpara: la copia que no funcionó",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0722",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "lámpara",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0723 — Lámpara: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0723",
  "seed_hash": "6600177aa7a61b884b9d1dcb553142fe82561dcfb1a4bd7581a0dfabbbc069ff",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_3",
  "titulo": "Lámpara: el favor convertido en deuda",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0723",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "lámpara",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0724 — Lámpara: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0724",
  "seed_hash": "0f0f266b2e0c417eff141069e6aa26713f23395e9cbcb1038e79f1a9beb8e3b8",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_4",
  "titulo": "Lámpara: dos personas, dos necesidades",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0724",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "lámpara",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0725 — Lámpara: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0725",
  "seed_hash": "300dc50f04420d5cee90664b953e8a0b004d26dc11a99591ebd652f34b0b73d0",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_5",
  "titulo": "Lámpara: el acuerdo que nadie había entendido",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0725",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "lámpara",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0726 — Lámpara: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0726",
  "seed_hash": "1ac6fe056c3f38450a400d781343b10feeb1b324021fe40326d79d843ca1e3cb",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_6",
  "titulo": "Lámpara: la ayuda que cambió algo querido",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0726",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "lámpara",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0727 — Lámpara: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0727",
  "seed_hash": "c0e696fb691f81361e6b9df18e007891f36bbe6ce9843ef9de50594773105a0e",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_7",
  "titulo": "Lámpara: la pregunta que no quería hacer",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0727",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "lámpara",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0728 — Lámpara: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0728",
  "seed_hash": "2cf26c9fd53d47eaba09f52cfe7ef9e8ae30e11a28bfaa9461789128fdde994c",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_8",
  "titulo": "Lámpara: el recuerdo que tenían distinto",
  "semilla": "Milo apaga la luz aunque no resolvió todo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0728",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo apaga la luz aunque no resolvió todo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "lámpara",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0729 — Lámpara: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0729",
  "seed_hash": "4641f99ccb90f43f5f6a7ea453b3d5f18c61c5f51499fd915671ae306b5ae84f",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_9",
  "titulo": "Lámpara: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0729",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "lámpara",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0730 — Lámpara: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0730",
  "seed_hash": "7f3e7883832d540b7ceeb56c1097e947ab58b562b2bf478fdf77f97ac699c721",
  "family_id": "F073",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_10",
  "titulo": "Lámpara: el cuidado que necesitó permiso",
  "semilla": "Milo apaga la luz aunque no resolvió todo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo apaga la luz aunque no resolvió todo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "lámpara",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0730",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "anota el siguiente paso y se permite dormir",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde lámpara y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo apaga la luz aunque no resolvió todo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo apaga la luz aunque no resolvió todo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "lámpara",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0731 — Taza de café: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0731",
  "seed_hash": "8ed3433979586d27113a9feb0939a53dd1ba1c18121ff86aaadc73aa78f9ce34",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_1",
  "titulo": "Taza de café: el gesto que llegó a la persona equivocada",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "taza de café",
  "giro_posible": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
  "desarrollo_requerido": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0731",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC01",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "taza de café",
      "reinterpretacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0732 — Taza de café: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0732",
  "seed_hash": "9bd6108e7c5337b8bacbc182a561f2d7cad52d714cd2366200b25c5f56115660",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_2",
  "titulo": "Taza de café: la copia que no funcionó",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0732",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "taza de café",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0733 — Taza de café: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0733",
  "seed_hash": "cab77cecb3f109969d10f92b5f233fd5c1f24d188070f089512dbfcd4785d7ee",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_3",
  "titulo": "Taza de café: el favor convertido en deuda",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0733",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "taza de café",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0734 — Taza de café: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0734",
  "seed_hash": "a40895db54e9718db064cfb71751bbe4358de7d6c4dde819c8060c497ac811ad",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_4",
  "titulo": "Taza de café: dos personas, dos necesidades",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0734",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "taza de café",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0735 — Taza de café: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0735",
  "seed_hash": "f87a49518e09cdfeb0ea6ada2bf289f63ba946b72dd2dabd5743114052c2fb77",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_5",
  "titulo": "Taza de café: el acuerdo que nadie había entendido",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0735",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "taza de café",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0736 — Taza de café: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0736",
  "seed_hash": "f745dda2dc7af25186bb0844727acfe927ce1123c7572cf3b8561cd1aec43afb",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_6",
  "titulo": "Taza de café: la ayuda que cambió algo querido",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0736",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "taza de café",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0737 — Taza de café: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0737",
  "seed_hash": "d0bb238cdd750bb42c752e0aea48081ea3bf373053b71f30d404e08263d7178a",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_7",
  "titulo": "Taza de café: la pregunta que no quería hacer",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0737",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "taza de café",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0738 — Taza de café: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0738",
  "seed_hash": "4010f733f4decec1a04afa0f4527062cc22ece2c717f29c8f99006c4f19e5d9b",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_8",
  "titulo": "Taza de café: el recuerdo que tenían distinto",
  "semilla": "Milo prepara otra bebida para seguir despierto. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0738",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo prepara otra bebida para seguir despierto. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "taza de café",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0739 — Taza de café: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0739",
  "seed_hash": "4a2eb0d0842872620d8a4e7867db8288c4ae6349c8bd7a6a6004758d41cd03be",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_9",
  "titulo": "Taza de café: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0739",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "taza de café",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0740 — Taza de café: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0740",
  "seed_hash": "cd85fd6f9efd28272d980f7d663c7f1d98b6360e09f4350365cda194aea9c7ae",
  "family_id": "F074",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_10",
  "titulo": "Taza de café: el cuidado que necesitó permiso",
  "semilla": "Milo prepara otra bebida para seguir despierto. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo prepara otra bebida para seguir despierto. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "taza de café",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0740",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "elige parar una tarea no urgente",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde taza de café y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo prepara otra bebida para seguir despierto. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo prepara otra bebida para seguir despierto. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "taza de café",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0741 — Ventana abierta: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0741",
  "seed_hash": "d155dde63d5a8b80584f803186b9b8a60de9d255a013101ec5f4d0ca447f61da",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_1",
  "titulo": "Ventana abierta: el gesto que llegó a la persona equivocada",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
  "desarrollo_requerido": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0741",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC01",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "ventana abierta",
      "reinterpretacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0742 — Ventana abierta: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0742",
  "seed_hash": "7e05c7f02dad9cae2ef89025eb18eb09d92cb3dd8142f6357d99e66ff9edb0b7",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_2",
  "titulo": "Ventana abierta: la copia que no funcionó",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0742",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0743 — Ventana abierta: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0743",
  "seed_hash": "1079e79a1e9f6f0974dd519410a87d8108066b9c01d268f54c2e2908abc26a77",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_3",
  "titulo": "Ventana abierta: el favor convertido en deuda",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0743",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0744 — Ventana abierta: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0744",
  "seed_hash": "2be94a091e236c452eb7564ecb312b4d6a1aedc0aa3422cde8e1367b1acfdebb",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_4",
  "titulo": "Ventana abierta: dos personas, dos necesidades",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0744",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0745 — Ventana abierta: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0745",
  "seed_hash": "98128b105ade2cef049a0a61c28a078312b562282d5598b81483f0511d8e9c13",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_5",
  "titulo": "Ventana abierta: el acuerdo que nadie había entendido",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0745",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0746 — Ventana abierta: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0746",
  "seed_hash": "77928865a691334b7dd0944f11b054a8df2dd9c43b0262761399bf3ea533e143",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_6",
  "titulo": "Ventana abierta: la ayuda que cambió algo querido",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0746",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0747 — Ventana abierta: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0747",
  "seed_hash": "f5ab0ff800a16dae0c916b7bdcc37aba3aaf6c37e0ceeee59488123bbda7aa36",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_7",
  "titulo": "Ventana abierta: la pregunta que no quería hacer",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0747",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0748 — Ventana abierta: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0748",
  "seed_hash": "1b048ce32f8b3d52d535fc2246a4af00e754f58024de80f79963df0880740f25",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_8",
  "titulo": "Ventana abierta: el recuerdo que tenían distinto",
  "semilla": "Milo se toma unos minutos mirando el patio. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0748",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo se toma unos minutos mirando el patio. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0749 — Ventana abierta: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0749",
  "seed_hash": "6afceb5529dc1afcab6ae04efed3f8d470fd7ef36fcd25bd1cf7a6d20f7d5e75",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_9",
  "titulo": "Ventana abierta: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0749",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0750 — Ventana abierta: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0750",
  "seed_hash": "eb441ee179fee150eec3ddd1e06e4f25a85e31e5f07ea9460b89b6e8ff92143d",
  "family_id": "F075",
  "territorio": "Descanso y valor",
  "angulo": "arco_causal_10",
  "titulo": "Ventana abierta: el cuidado que necesitó permiso",
  "semilla": "Milo se toma unos minutos mirando el patio. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo se toma unos minutos mirando el patio. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "ventana abierta",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "OMS"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0750",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "vuelve a su actividad con una decisión más pequeña",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde ventana abierta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo se toma unos minutos mirando el patio. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Descanso y valor; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Descanso y valor",
      "conducta": "Milo se toma unos minutos mirando el patio. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "ventana abierta",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-S0751 — Herramienta prestada: la primera vez

```json
{
  "seed_id": "MILO-S0751",
  "seed_hash": "046482434ec3a1ba885ba0e54b4487c83dfe30da57de77fe822927b8b0550356",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "primera_vez",
  "titulo": "Herramienta prestada: la primera vez",
  "semilla": "Milo devuelve una herramienta limpia. Cree que gracias basta siempre. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "cree que gracias basta siempre",
  "accion_visible": "Milo devuelve una herramienta limpia",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "reconocer el préstamo también implica cuidar lo recibido",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo"
  ],
  "personajes_secundarios": "Resolver identidad y disponibilidad de referencias desde canon antes de producir; no inventar anclas aprobadas.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PENDING_SCRIPT_REVIEW",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 85,
    "compuesto": 88.75,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "cree que gracias basta siempre",
      "conflicto": "cree que gracias basta siempre",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "reconocer el préstamo también implica cuidar lo recibido",
      "visual": "Milo devuelve una herramienta limpia",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia",
      "objeto": "herramienta prestada",
      "reinterpretacion": "reconocer el préstamo también implica cuidar lo recibido",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "cree que gracias basta siempre"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0752 — Herramienta prestada: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0752",
  "seed_hash": "f56b16113018fa9372f2903dd3a2d9eecf3e794bd84a8d552ca3b9e5868f894e",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_2",
  "titulo": "Herramienta prestada: la copia que no funcionó",
  "semilla": "Milo devuelve una herramienta limpia. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0752",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo devuelve una herramienta limpia. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0753 — Herramienta prestada: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0753",
  "seed_hash": "ece1c410959d99fb4dde678a95fee69b5f1170fa6a15acbc21643023416f7c14",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_3",
  "titulo": "Herramienta prestada: el favor convertido en deuda",
  "semilla": "Milo devuelve una herramienta limpia. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0753",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo devuelve una herramienta limpia. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0754 — Herramienta prestada: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0754",
  "seed_hash": "2febb4e8bc364df7c893d74cf6981cc5822803703ba5354cf8ac649018d6ceb3",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_4",
  "titulo": "Herramienta prestada: dos personas, dos necesidades",
  "semilla": "Milo devuelve una herramienta limpia. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0754",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo devuelve una herramienta limpia. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0755 — Herramienta prestada: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0755",
  "seed_hash": "4c12f0beacfe8d1208a14ee3b607f7d334b1366e422d055ba84d029b09140fcf",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_5",
  "titulo": "Herramienta prestada: el acuerdo que nadie había entendido",
  "semilla": "Milo devuelve una herramienta limpia. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0755",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo devuelve una herramienta limpia. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0756 — Herramienta prestada: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0756",
  "seed_hash": "8114c37fe099a0a51aea11403913bbbc43869f1d77d05375aae8ed43430fe670",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_6",
  "titulo": "Herramienta prestada: la ayuda que cambió algo querido",
  "semilla": "Milo devuelve una herramienta limpia. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0756",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo devuelve una herramienta limpia. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0757 — Herramienta prestada: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0757",
  "seed_hash": "a9db58a4834392a0288190656b626c71fe4fd0d9d320154869335d2341882001",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_7",
  "titulo": "Herramienta prestada: la pregunta que no quería hacer",
  "semilla": "Milo devuelve una herramienta limpia. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0757",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo devuelve una herramienta limpia. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0758 — Herramienta prestada: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0758",
  "seed_hash": "914b7b1a62a69160df8fbbf65bdd9fbb94474f919c2361f862da2940b042062f",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_8",
  "titulo": "Herramienta prestada: el recuerdo que tenían distinto",
  "semilla": "Milo devuelve una herramienta limpia. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo devuelve una herramienta limpia. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0758",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo devuelve una herramienta limpia. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0759 — Herramienta prestada: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0759",
  "seed_hash": "4a09f55ec2c4809bf6644c747d923f20e3d929d2778f6af4adea1d21d7765d57",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_9",
  "titulo": "Herramienta prestada: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo devuelve una herramienta limpia. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0759",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo devuelve una herramienta limpia. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0760 — Herramienta prestada: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0760",
  "seed_hash": "7117b5079f57e69af15a445ae328aef8d9994ff0af30d9a22f8fb89feaa76e9a",
  "family_id": "F076",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_10",
  "titulo": "Herramienta prestada: el cuidado que necesitó permiso",
  "semilla": "Milo devuelve una herramienta limpia. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo devuelve una herramienta limpia. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "herramienta prestada",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0760",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "reconocer el préstamo también implica cuidar lo recibido",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde herramienta prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo devuelve una herramienta limpia. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo devuelve una herramienta limpia. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "herramienta prestada",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-S0761 — Plato lavado: la primera vez

```json
{
  "seed_id": "MILO-S0761",
  "seed_hash": "08d6ec5068237399b88a5a3a3c790f11d9932baf8572b37fd5a6d86e509c9eb0",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "primera_vez",
  "titulo": "Plato lavado: la primera vez",
  "semilla": "Milo lava el plato de quien cocinó. Espera encontrar una frase perfecta. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "espera encontrar una frase perfecta",
  "accion_visible": "Milo lava el plato de quien cocinó",
  "objeto_emocional": "plato lavado",
  "giro_posible": "su acción acompaña un agradecimiento sencillo",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo"
  ],
  "personajes_secundarios": "Resolver identidad y disponibilidad de referencias desde canon antes de producir; no inventar anclas aprobadas.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PENDING_SCRIPT_REVIEW",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 85,
    "compuesto": 88.75,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "espera encontrar una frase perfecta",
      "conflicto": "espera encontrar una frase perfecta",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "su acción acompaña un agradecimiento sencillo",
      "visual": "Milo lava el plato de quien cocinó",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó",
      "objeto": "plato lavado",
      "reinterpretacion": "su acción acompaña un agradecimiento sencillo",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "espera encontrar una frase perfecta"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0762 — Plato lavado: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0762",
  "seed_hash": "bcafbd39320af761d73ec060f0f7021234f85a797fb6ddf2b333f2942a597814",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_2",
  "titulo": "Plato lavado: la copia que no funcionó",
  "semilla": "Milo lava el plato de quien cocinó. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0762",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo lava el plato de quien cocinó. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "plato lavado",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0763 — Plato lavado: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0763",
  "seed_hash": "6347624a36cb1f1578d2c893ae1c4b91d474e53b96ec4c87127c69963f74127a",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_3",
  "titulo": "Plato lavado: el favor convertido en deuda",
  "semilla": "Milo lava el plato de quien cocinó. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0763",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo lava el plato de quien cocinó. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "plato lavado",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0764 — Plato lavado: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0764",
  "seed_hash": "3ac534300424f88d16951f85d91d2af944602f69a1f475a4ca21a34e509fa768",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_4",
  "titulo": "Plato lavado: dos personas, dos necesidades",
  "semilla": "Milo lava el plato de quien cocinó. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0764",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo lava el plato de quien cocinó. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "plato lavado",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0765 — Plato lavado: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0765",
  "seed_hash": "18dca81d27812e4d38956b4a545a91abe3bd99a034064cde63b1b559b0bd753e",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_5",
  "titulo": "Plato lavado: el acuerdo que nadie había entendido",
  "semilla": "Milo lava el plato de quien cocinó. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0765",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo lava el plato de quien cocinó. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "plato lavado",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0766 — Plato lavado: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0766",
  "seed_hash": "75360f2555e322c62b117fa49ed2d16bee1546eb1b4330daa3be923f8f93113f",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_6",
  "titulo": "Plato lavado: la ayuda que cambió algo querido",
  "semilla": "Milo lava el plato de quien cocinó. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0766",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo lava el plato de quien cocinó. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "plato lavado",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0767 — Plato lavado: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0767",
  "seed_hash": "786e690c25a0771fab350ff0036e1e0ca612312b7dfc2be65fc77c00887f4622",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_7",
  "titulo": "Plato lavado: la pregunta que no quería hacer",
  "semilla": "Milo lava el plato de quien cocinó. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0767",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo lava el plato de quien cocinó. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "plato lavado",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0768 — Plato lavado: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0768",
  "seed_hash": "4ad1cccec45a5e0bd1e4733131ec6b2ee7fe587b8740614e9c97f4494b01e507",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_8",
  "titulo": "Plato lavado: el recuerdo que tenían distinto",
  "semilla": "Milo lava el plato de quien cocinó. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo lava el plato de quien cocinó. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0768",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo lava el plato de quien cocinó. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "plato lavado",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0769 — Plato lavado: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0769",
  "seed_hash": "f7bf2b8b214c645fe5c6a07f6e81b0364a97162547fffcbe6342dd39f36c49a4",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_9",
  "titulo": "Plato lavado: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo lava el plato de quien cocinó. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0769",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo lava el plato de quien cocinó. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "plato lavado",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0770 — Plato lavado: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0770",
  "seed_hash": "abecceff08fb5cb41e2c37c1e708c194f1bfc5542e99510d074742f1679a6754",
  "family_id": "F077",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_10",
  "titulo": "Plato lavado: el cuidado que necesitó permiso",
  "semilla": "Milo lava el plato de quien cocinó. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo lava el plato de quien cocinó. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "plato lavado",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0770",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "su acción acompaña un agradecimiento sencillo",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde plato lavado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo lava el plato de quien cocinó. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo lava el plato de quien cocinó. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "plato lavado",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0771 — Nota: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0771",
  "seed_hash": "f89f5bf04a22cf630703f13c9653cb6106be3d8aebf3fe30aa3ea1a238508338",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_1",
  "titulo": "Nota: el gesto que llegó a la persona equivocada",
  "semilla": "Milo deja una nota de agradecimiento. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "nota",
  "giro_posible": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
  "desarrollo_requerido": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0771",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC01",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo deja una nota de agradecimiento. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "nota",
      "reinterpretacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0772 — Nota: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0772",
  "seed_hash": "3f93e62f4ff48c60be3a312791b1331f076fe43f033a64a4e429991fdcac1000",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_2",
  "titulo": "Nota: la copia que no funcionó",
  "semilla": "Milo deja una nota de agradecimiento. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "nota",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0772",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo deja una nota de agradecimiento. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "nota",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0773 — Nota: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0773",
  "seed_hash": "c3b56c0d18b546504f6c0b71d4620af8a3e1ae32857d1855e5828ed0ddd7ce5d",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_3",
  "titulo": "Nota: el favor convertido en deuda",
  "semilla": "Milo deja una nota de agradecimiento. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "nota",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0773",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo deja una nota de agradecimiento. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "nota",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0774 — Nota: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0774",
  "seed_hash": "acb36e5d8b3fa6514d8926443a4aa2b6567c45e8de86903eea1f6c76118ff69e",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_4",
  "titulo": "Nota: dos personas, dos necesidades",
  "semilla": "Milo deja una nota de agradecimiento. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "nota",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0774",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo deja una nota de agradecimiento. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "nota",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0775 — Nota: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0775",
  "seed_hash": "9481df9b38c31426f08f2406914e714a0880e15d1eb2c7d7731a392fd7e66c85",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_5",
  "titulo": "Nota: el acuerdo que nadie había entendido",
  "semilla": "Milo deja una nota de agradecimiento. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "nota",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0775",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo deja una nota de agradecimiento. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "nota",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0776 — Nota: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0776",
  "seed_hash": "69edc1a7deae9866ffcc3eb59ee46344a48a81dde9e0588f36f680c0e790a67a",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_6",
  "titulo": "Nota: la ayuda que cambió algo querido",
  "semilla": "Milo deja una nota de agradecimiento. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "nota",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0776",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo deja una nota de agradecimiento. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "nota",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0777 — Nota: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0777",
  "seed_hash": "2f23cf9a957acf0af26c7183921f1635261311d9a38c09abcff397160c31472e",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_7",
  "titulo": "Nota: la pregunta que no quería hacer",
  "semilla": "Milo deja una nota de agradecimiento. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "nota",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0777",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo deja una nota de agradecimiento. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "nota",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0778 — Nota: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0778",
  "seed_hash": "0af069bae0a233c25ab6bed982300794ba28590dc766eb6b8b88f07789e0848d",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_8",
  "titulo": "Nota: el recuerdo que tenían distinto",
  "semilla": "Milo deja una nota de agradecimiento. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo deja una nota de agradecimiento. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "nota",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0778",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo deja una nota de agradecimiento. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "nota",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0779 — Nota: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0779",
  "seed_hash": "69eeeaff766baf0e84e9a666fb0b12758336925d728a102873e97e4bc202cfde",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_9",
  "titulo": "Nota: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo deja una nota de agradecimiento. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "nota",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0779",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo deja una nota de agradecimiento. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "nota",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0780 — Nota: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0780",
  "seed_hash": "1f053da185baa3fe8b04ce92e027651062a5ac6f595b66c708cb4bf29cfe70a0",
  "family_id": "F078",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_10",
  "titulo": "Nota: el cuidado que necesitó permiso",
  "semilla": "Milo deja una nota de agradecimiento. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo deja una nota de agradecimiento. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "nota",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0780",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "nombra una ayuda específica sin exagerar",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde nota y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo deja una nota de agradecimiento. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo deja una nota de agradecimiento. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "nota",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0781 — Planta regalada: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0781",
  "seed_hash": "b50c3c20953a302dc451f357cde94f0330cc7f958257a8e1c6661919eda2a803",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_1",
  "titulo": "Planta regalada: el gesto que llegó a la persona equivocada",
  "semilla": "Milo cuida una planta que recibió. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo cuida una planta que recibió. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
  "desarrollo_requerido": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0781",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC01",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo cuida una planta que recibió. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "planta regalada",
      "reinterpretacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0782 — Planta regalada: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0782",
  "seed_hash": "6cfff04ea5662ab78cbb2866b3281240dde137d22e504e297ef5052917f5da4b",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_2",
  "titulo": "Planta regalada: la copia que no funcionó",
  "semilla": "Milo cuida una planta que recibió. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo cuida una planta que recibió. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0782",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo cuida una planta que recibió. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "planta regalada",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0783 — Planta regalada: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0783",
  "seed_hash": "bb40928e1f785df5df944a68ea29e4998d478ee18ea43519ce4991828f095f44",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_3",
  "titulo": "Planta regalada: el favor convertido en deuda",
  "semilla": "Milo cuida una planta que recibió. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo cuida una planta que recibió. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0783",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo cuida una planta que recibió. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "planta regalada",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0784 — Planta regalada: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0784",
  "seed_hash": "937a82f6fb58bce1fa23c30211f6b1d46997a0648538ad0c4c7bb06be7cf490f",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_4",
  "titulo": "Planta regalada: dos personas, dos necesidades",
  "semilla": "Milo cuida una planta que recibió. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo cuida una planta que recibió. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0784",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo cuida una planta que recibió. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "planta regalada",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0785 — Planta regalada: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0785",
  "seed_hash": "830d367f7fd5c9feb3e9dfb86ba8f34e88a69a306f102774dd6dda39556b9839",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_5",
  "titulo": "Planta regalada: el acuerdo que nadie había entendido",
  "semilla": "Milo cuida una planta que recibió. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo cuida una planta que recibió. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0785",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo cuida una planta que recibió. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "planta regalada",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0786 — Planta regalada: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0786",
  "seed_hash": "4c12d59bd9e452326e1a5bbf7fcfad488c605063a0f5c86021f99871bbd2974e",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_6",
  "titulo": "Planta regalada: la ayuda que cambió algo querido",
  "semilla": "Milo cuida una planta que recibió. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo cuida una planta que recibió. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0786",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo cuida una planta que recibió. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "planta regalada",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0787 — Planta regalada: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0787",
  "seed_hash": "c8b321fd95e49445e9f31083479b61a8c03f3b9b111a093e9f4a1119a4e2a051",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_7",
  "titulo": "Planta regalada: la pregunta que no quería hacer",
  "semilla": "Milo cuida una planta que recibió. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo cuida una planta que recibió. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0787",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo cuida una planta que recibió. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "planta regalada",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0788 — Planta regalada: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0788",
  "seed_hash": "bd50b8eeeff2098d88a2c7799066312d2e6c7c4408768168af52600cebe49f9c",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_8",
  "titulo": "Planta regalada: el recuerdo que tenían distinto",
  "semilla": "Milo cuida una planta que recibió. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo cuida una planta que recibió. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0788",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo cuida una planta que recibió. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "planta regalada",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0789 — Planta regalada: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0789",
  "seed_hash": "144081b6b89d9e0bce68dadc8684793c6fab3840b048eb5579dda2eed03ba1d7",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_9",
  "titulo": "Planta regalada: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo cuida una planta que recibió. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo cuida una planta que recibió. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0789",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo cuida una planta que recibió. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "planta regalada",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0790 — Planta regalada: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0790",
  "seed_hash": "9503799e3886a042e8bac987c93c0279747bad7cc1bde66136761a90275900db",
  "family_id": "F079",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_10",
  "titulo": "Planta regalada: el cuidado que necesitó permiso",
  "semilla": "Milo cuida una planta que recibió. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo cuida una planta que recibió. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "planta regalada",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0790",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "compartir cómo creció vuelve visible su atención",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde planta regalada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo cuida una planta que recibió. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo cuida una planta que recibió. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "planta regalada",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0791 — Asiento reservado: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0791",
  "seed_hash": "73103a0106c5e0f8fa9ab3719d18f0480522f5bf73c3725b5e0aed101cdf39ae",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_1",
  "titulo": "Asiento reservado: el gesto que llegó a la persona equivocada",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
  "desarrollo_requerido": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0791",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC01",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "asiento reservado",
      "reinterpretacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0792 — Asiento reservado: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0792",
  "seed_hash": "40404b289d298b118cb342cd1f3cb1e703a7f5d66802f97f8869c7a1b0c7972b",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_2",
  "titulo": "Asiento reservado: la copia que no funcionó",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
  "desarrollo_requerido": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0792",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC02",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0793 — Asiento reservado: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0793",
  "seed_hash": "6da2979f13f9c012135614b0b2e0d43873ce7be38eadd733b277ae9dc44d25e7",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_3",
  "titulo": "Asiento reservado: el favor convertido en deuda",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
  "desarrollo_requerido": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0793",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC03",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0794 — Asiento reservado: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0794",
  "seed_hash": "3e4313b530aed470766089f154f20193367cf26c4d8b5b1d104e21c97360a580",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_4",
  "titulo": "Asiento reservado: dos personas, dos necesidades",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Una misma intención puede requerir dos formas distintas de cuidado.",
  "desarrollo_requerido": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0794",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC04",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0795 — Asiento reservado: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0795",
  "seed_hash": "4b9770c642466b984346a5fa6d1ab807a30baa5db443911b4213612cb1d24bcb",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_5",
  "titulo": "Asiento reservado: el acuerdo que nadie había entendido",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
  "desarrollo_requerido": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0795",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC05",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0796 — Asiento reservado: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0796",
  "seed_hash": "54cd9ee2bea8f8c96aa09d767c38186ad003353c01a5152494402973abfeee86",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_6",
  "titulo": "Asiento reservado: la ayuda que cambió algo querido",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Mejorar un espacio también requiere escuchar a quien lo usa.",
  "desarrollo_requerido": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0796",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC06",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0797 — Asiento reservado: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0797",
  "seed_hash": "af87783677988f8a585777eadb91ea890ebe456d18ba6a695a41ce9286b30a67",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_7",
  "titulo": "Asiento reservado: la pregunta que no quería hacer",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
  "desarrollo_requerido": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0797",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC07",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0798 — Asiento reservado: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0798",
  "seed_hash": "97b9aa7198346856034379c4fb924ac06232dfee78b6494fd88f89cfd0c33712",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_8",
  "titulo": "Asiento reservado: el recuerdo que tenían distinto",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
  "desarrollo_requerido": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "descubrimiento",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0798",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC08",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0799 — Asiento reservado: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0799",
  "seed_hash": "ab9c2ed4225863cc08668975f4a1e0f0193ed8f5118f4dabfd1c728db1dc415d",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_9",
  "titulo": "Asiento reservado: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
  "desarrollo_requerido": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "representacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0799",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC09",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0800 — Asiento reservado: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0800",
  "seed_hash": "042c758876c45b6d39436a5450f617b1a6dcc6e40531c3daec227ba7a42d55e3",
  "family_id": "F080",
  "territorio": "Gratitud concreta",
  "angulo": "arco_causal_10",
  "titulo": "Asiento reservado: el cuidado que necesitó permiso",
  "semilla": "Milo guarda un lugar para quien antes se lo guardaba. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo guarda un lugar para quien antes se lo guardaba. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "asiento reservado",
  "giro_posible": "Detenerse a preguntar puede cuidar tanto como intervenir.",
  "desarrollo_requerido": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "familiar presente por resolver desde canon"
  ],
  "personajes_secundarios": "En ausencia/duelo, el interlocutor es un familiar presente: no hacer hablar a alguien fallecido. En infancia, conservar rol infantil y adulto responsable. Identidad visual por resolver.",
  "world_candidates": [
    "kitchen_day",
    "living_room_day",
    "bedroom_day",
    "home_entrance_day",
    "hallway_day",
    "patio_day"
  ],
  "motor_editorial": "identificacion",
  "destinatario_emocional": "Alguien que reconoce esta tensión doméstica; concretarlo durante estrategia, sin CTA obligatorio.",
  "fuentes_tematicas": [
    "BASE_MINERIA",
    "CANON",
    "GG_GRATITUD"
  ],
  "procedencia": "ficcion_original_inspirada_en_temas; no historia extraída de la fuente",
  "estado": "EDITORIAL_ELIGIBLE",
  "qc_editorial": "PROVISIONAL_SEED_PASS_NOT_SCRIPT_APPROVAL",
  "duracion": "Estimar desde guion y pausas; ajustar al audio real.",
  "restricciones": [
    "No convertir cuidado en justificación de daño.",
    "No presentar pensamientos o diagnósticos como hechos.",
    "No repetir la misma familia en episodios consecutivos.",
    "Subtítulos superiores; imagen sin texto incrustado.",
    "Música y SFX desactivados."
  ],
  "replaces_seed_id": "MILO-S0800",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "la otra persona reconoce la reciprocidad",
  "narrative_cluster_id": "ARC10",
  "revision": {
    "quality_notes": {
      "reconocimiento": 4.5,
      "conflicto": 4.5,
      "hook": 4.5,
      "progresion": 4.5,
      "revelacion": 4.5,
      "visual": 4.5,
      "compartibilidad": 4
    },
    "affinity_notes": {
      "territorio": 4.5,
      "conducta": 4.5,
      "objeto": 4.5,
      "reinterpretacion": 4.5,
      "tono": 4.5,
      "visual": 4.5,
      "representacion": 4.5
    },
    "calidad": 89.0,
    "afinidad": 90.0,
    "novedad": 80,
    "compuesto": 88.0,
    "nivel": "PRIORITARIA",
    "elegible": true,
    "bloqueos": [],
    "evidencia_calidad": {
      "reconocimiento": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "hook": "Entrada posible desde asiento reservado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo guarda un lugar para quien antes se lo guardaba. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Gratitud concreta; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Gratitud concreta",
      "conducta": "Milo guarda un lugar para quien antes se lo guardaba. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "asiento reservado",
      "reinterpretacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción."
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```
