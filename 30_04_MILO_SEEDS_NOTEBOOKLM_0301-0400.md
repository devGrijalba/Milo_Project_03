# MILO SEEDS — PARTE 04

Banco: `2.0.0`
Registros: `0301–0400`

## REGLAS

- Datos canónicos.
- No inventar campos.
- No recalcular seed_hash.
- El seed_id puede normalizarse desde el encabezado lógico/registro según `18_SEED_HEADER_NORMALIZATION.md`.

# MILO-S0301 — Teléfono: la primera vez

```json
{
  "seed_id": "MILO-S0301",
  "seed_hash": "2102628a3793d2713bb1a87fb3596c894ee39d95b36c61e225590f1ab9c806c7",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "primera_vez",
  "titulo": "Teléfono: la primera vez",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Convierte un silencio en una historia completa. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "convierte un silencio en una historia completa",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta",
  "objeto_emocional": "teléfono",
  "giro_posible": "deja espacio para preguntar sin inventar motivos",
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
      "reconocimiento": "convierte un silencio en una historia completa",
      "conflicto": "convierte un silencio en una historia completa",
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "deja espacio para preguntar sin inventar motivos",
      "visual": "Milo vuelve a mirar una conversación sin respuesta",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta",
      "objeto": "teléfono",
      "reinterpretacion": "deja espacio para preguntar sin inventar motivos",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "convierte un silencio en una historia completa"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0302 — Teléfono: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0302",
  "seed_hash": "03f5deab5f80398c308449b5fcbc2621ef830de88284e4d65b9861ac735617f7",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_2",
  "titulo": "Teléfono: la copia que no funcionó",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0302",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "teléfono",
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

# MILO-R0303 — Teléfono: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0303",
  "seed_hash": "24075359639682faac41c596fcbc35cab6b5d9a9634b3e74e99b742b0df6e7d6",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_3",
  "titulo": "Teléfono: el favor convertido en deuda",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0303",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "teléfono",
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

# MILO-R0304 — Teléfono: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0304",
  "seed_hash": "0d850dc9c9801a04552f4260be9a5e046c6ca0130b81be62099309f62b805687",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_4",
  "titulo": "Teléfono: dos personas, dos necesidades",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0304",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "teléfono",
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

# MILO-R0305 — Teléfono: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0305",
  "seed_hash": "9d870029b54a7302080dabbc23abac46c10b7599642f64b0795b3e88219345cc",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_5",
  "titulo": "Teléfono: el acuerdo que nadie había entendido",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0305",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "teléfono",
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

# MILO-R0306 — Teléfono: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0306",
  "seed_hash": "76f8e799be103c61a10ad8faa2ceb3015cd55011c09be4b3cd93960525f7a1e5",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_6",
  "titulo": "Teléfono: la ayuda que cambió algo querido",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0306",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "teléfono",
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

# MILO-R0307 — Teléfono: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0307",
  "seed_hash": "a12ad5d52c0c6bbfc4325d95e2db323abe3f60b7ab1909a3facfe3fbe13f5eaf",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_7",
  "titulo": "Teléfono: la pregunta que no quería hacer",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0307",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "teléfono",
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

# MILO-R0308 — Teléfono: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0308",
  "seed_hash": "f1928059bc9012b1ad3adafeea3623b6a66a1e752a3acfef220cce0278dfc195",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_8",
  "titulo": "Teléfono: el recuerdo que tenían distinto",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0308",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "teléfono",
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

# MILO-R0309 — Teléfono: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0309",
  "seed_hash": "9442f9a5e5775386a7c1cdaab25e09bd372729447017a7d45671e03550ec3450",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_9",
  "titulo": "Teléfono: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0309",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "teléfono",
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

# MILO-R0310 — Teléfono: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0310",
  "seed_hash": "408d2b6d1c005da227c2ee11cceda329b8f2151f99046c5c33d85ddae8b4357f",
  "family_id": "F031",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_10",
  "titulo": "Teléfono: el cuidado que necesitó permiso",
  "semilla": "Milo vuelve a mirar una conversación sin respuesta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo vuelve a mirar una conversación sin respuesta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "teléfono",
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
  "replaces_seed_id": "MILO-S0310",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "deja espacio para preguntar sin inventar motivos",
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
      "hook": "Entrada posible desde teléfono y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo vuelve a mirar una conversación sin respuesta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo vuelve a mirar una conversación sin respuesta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "teléfono",
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

# MILO-R0311 — Llaves: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0311",
  "seed_hash": "0202f6d3467ff9811ec5364e9ea2eedc8c7ed0d5d443b3fd16910ff992ae4a42",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_1",
  "titulo": "Llaves: el gesto que llegó a la persona equivocada",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0311",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "llaves",
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

# MILO-R0312 — Llaves: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0312",
  "seed_hash": "9284a78225537e938bcf82829b7e07487aa6b2978ed62441ba1f8fcb3e876783",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_2",
  "titulo": "Llaves: la copia que no funcionó",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0312",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "llaves",
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

# MILO-R0313 — Llaves: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0313",
  "seed_hash": "217eb492e96c800f4348993d80010d9ebd9d7db47ba43d344873f3d1061bc399",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_3",
  "titulo": "Llaves: el favor convertido en deuda",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0313",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "llaves",
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

# MILO-R0314 — Llaves: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0314",
  "seed_hash": "cbfc6da93beb3ee9bebb2f2fd5d897b81ef66a091ce90665ff506e6bdc49f3e3",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_4",
  "titulo": "Llaves: dos personas, dos necesidades",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0314",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "llaves",
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

# MILO-R0315 — Llaves: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0315",
  "seed_hash": "805651408fa56421ba17cc6adeddbe271849cc71c2e5346a846d3caa303b5d93",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_5",
  "titulo": "Llaves: el acuerdo que nadie había entendido",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0315",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "llaves",
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

# MILO-R0316 — Llaves: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0316",
  "seed_hash": "42b37362d03a4355da6fd74ec75bf57c030bcfaed999b2fe992fcf8b24df1f53",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_6",
  "titulo": "Llaves: la ayuda que cambió algo querido",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0316",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "llaves",
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

# MILO-R0317 — Llaves: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0317",
  "seed_hash": "81f9140f41dde8dbc82b167d4d1021f0108a037c30cff8d590c100f6acddddbb",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_7",
  "titulo": "Llaves: la pregunta que no quería hacer",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0317",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "llaves",
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

# MILO-R0318 — Llaves: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0318",
  "seed_hash": "588a5ca79588ecc2e19e4d8d269d6d2667bb6276d14cac86618f8ed2e8513e8d",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_8",
  "titulo": "Llaves: el recuerdo que tenían distinto",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0318",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "llaves",
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

# MILO-R0319 — Llaves: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0319",
  "seed_hash": "1f614dd06085e84296f05d37d4a6defd79d51f506b21d01349ccd10785e7503f",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_9",
  "titulo": "Llaves: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0319",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "llaves",
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

# MILO-R0320 — Llaves: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0320",
  "seed_hash": "1c6edebf06239485f451ca5ca796287f1e2f707f86bc8b593af32d6ba30a7f55",
  "family_id": "F032",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_10",
  "titulo": "Llaves: el cuidado que necesitó permiso",
  "semilla": "Milo revisa varias veces dónde dejó las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo revisa varias veces dónde dejó las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "llaves",
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
  "replaces_seed_id": "MILO-S0320",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "un lugar concreto reduce una preocupación cotidiana",
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
      "hook": "Entrada posible desde llaves y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo revisa varias veces dónde dejó las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo revisa varias veces dónde dejó las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "llaves",
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

# MILO-S0321 — Ventana: la primera vez

```json
{
  "seed_id": "MILO-S0321",
  "seed_hash": "de4762ad5b51700ef94724d8315f5cc707f353aa32d96611dcf5d58f3747ca29",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "primera_vez",
  "titulo": "Ventana: la primera vez",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Teme cada respuesta posible. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "teme cada respuesta posible",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil",
  "objeto_emocional": "ventana",
  "giro_posible": "decide decir una sola frase honesta",
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
      "reconocimiento": "teme cada respuesta posible",
      "conflicto": "teme cada respuesta posible",
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "decide decir una sola frase honesta",
      "visual": "Milo ensaya frente a la ventana una conversación difícil",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil",
      "objeto": "ventana",
      "reinterpretacion": "decide decir una sola frase honesta",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "teme cada respuesta posible"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0322 — Ventana: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0322",
  "seed_hash": "cdc390d7669bb22a5269f54c9a3aeba99563ab48afc2e1e97862fb814c57f500",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_2",
  "titulo": "Ventana: la copia que no funcionó",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0322",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "ventana",
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

# MILO-R0323 — Ventana: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0323",
  "seed_hash": "bfc7cc3536e00502a1fbda4358979c1a44020e09144ea5deaabf6987dd3046e9",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_3",
  "titulo": "Ventana: el favor convertido en deuda",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0323",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "ventana",
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

# MILO-R0324 — Ventana: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0324",
  "seed_hash": "8cbc3b65251df9ae1da87176cf925e5650d7c49357b5351418a75df92ad1fbbe",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_4",
  "titulo": "Ventana: dos personas, dos necesidades",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0324",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "ventana",
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

# MILO-R0325 — Ventana: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0325",
  "seed_hash": "b2251da7a9c4ec71213b3d5567f7079c6c55d4338eee1d7d80b52f1e4c3314b6",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_5",
  "titulo": "Ventana: el acuerdo que nadie había entendido",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0325",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "ventana",
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

# MILO-R0326 — Ventana: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0326",
  "seed_hash": "40ef43bbd4a05905ba6fe2ea6267c167d7a44375cebb003c3b7452c06e07e70a",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_6",
  "titulo": "Ventana: la ayuda que cambió algo querido",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0326",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "ventana",
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

# MILO-R0327 — Ventana: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0327",
  "seed_hash": "8ea282c1b74b97f630c236b57248c31d7f1ef8573fc7c34a1b5099f4f1da9a1f",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_7",
  "titulo": "Ventana: la pregunta que no quería hacer",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0327",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "ventana",
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

# MILO-R0328 — Ventana: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0328",
  "seed_hash": "5a0b3435256ba79e86ef789e3d98cef313e076577cc6e428f4e6ee4d4bec6e92",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_8",
  "titulo": "Ventana: el recuerdo que tenían distinto",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0328",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "ventana",
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

# MILO-R0329 — Ventana: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0329",
  "seed_hash": "eb742229053077a5770b6fbe72a554fe1e1309e1e722d854f2024119286015b7",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_9",
  "titulo": "Ventana: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0329",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "ventana",
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

# MILO-R0330 — Ventana: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0330",
  "seed_hash": "c7302d1e83682d25d8dbbca400759d4524e40770686a2c282359c483970aecd8",
  "family_id": "F033",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_10",
  "titulo": "Ventana: el cuidado que necesitó permiso",
  "semilla": "Milo ensaya frente a la ventana una conversación difícil. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo ensaya frente a la ventana una conversación difícil. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "ventana",
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
  "replaces_seed_id": "MILO-S0330",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "decide decir una sola frase honesta",
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
      "hook": "Entrada posible desde ventana y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo ensaya frente a la ventana una conversación difícil. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo ensaya frente a la ventana una conversación difícil. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "ventana",
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

# MILO-S0331 — Cuaderno: la primera vez

```json
{
  "seed_id": "MILO-S0331",
  "seed_hash": "a051158165da8d74b15e54b12624e1c9c32024540ae64981bbb98b56d3c7db56",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "primera_vez",
  "titulo": "Cuaderno: la primera vez",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Ninguna parece suficientemente segura. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "ninguna parece suficientemente segura",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje",
  "objeto_emocional": "cuaderno",
  "giro_posible": "elige una versión clara sin prometer un resultado",
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
      "reconocimiento": "ninguna parece suficientemente segura",
      "conflicto": "ninguna parece suficientemente segura",
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "elige una versión clara sin prometer un resultado",
      "visual": "Milo escribe diez versiones del mismo mensaje",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje",
      "objeto": "cuaderno",
      "reinterpretacion": "elige una versión clara sin prometer un resultado",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "ninguna parece suficientemente segura"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0332 — Cuaderno: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0332",
  "seed_hash": "221126aca8d035df365bb68d42ced2154b367c82120c10bbd1c23e82c2d6e0a5",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_2",
  "titulo": "Cuaderno: la copia que no funcionó",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0332",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "cuaderno",
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

# MILO-R0333 — Cuaderno: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0333",
  "seed_hash": "2b7bbc9768f4b81d8a1d542227457fce417ebdc595b80a62df29d8ca5ad45e53",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_3",
  "titulo": "Cuaderno: el favor convertido en deuda",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0333",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "cuaderno",
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

# MILO-R0334 — Cuaderno: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0334",
  "seed_hash": "e61ad844b8119155ed277c758a087dccb990ccd4d41b9198a370fbbdc64e66e7",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_4",
  "titulo": "Cuaderno: dos personas, dos necesidades",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0334",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "cuaderno",
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

# MILO-R0335 — Cuaderno: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0335",
  "seed_hash": "8ba33b38a609e9e1f2dfafdd1060a0b05629b46fec7c4b41063b91032b2eefc4",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_5",
  "titulo": "Cuaderno: el acuerdo que nadie había entendido",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0335",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "cuaderno",
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

# MILO-R0336 — Cuaderno: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0336",
  "seed_hash": "a49d4a9b81a6a19e8a7ac0778dcf6cf4d43e1395b6520e05230297714bd3fc86",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_6",
  "titulo": "Cuaderno: la ayuda que cambió algo querido",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0336",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "cuaderno",
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

# MILO-R0337 — Cuaderno: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0337",
  "seed_hash": "ef893a68bcf182e4e82802f1237cf9f16e01d449ac517b147c5bdc2bed7ba57d",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_7",
  "titulo": "Cuaderno: la pregunta que no quería hacer",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0337",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "cuaderno",
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

# MILO-R0338 — Cuaderno: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0338",
  "seed_hash": "b7ed7ce901b1725a21915772563e1fb8e4f9f82569dada8c01689fac2857aa01",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_8",
  "titulo": "Cuaderno: el recuerdo que tenían distinto",
  "semilla": "Milo escribe diez versiones del mismo mensaje. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0338",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo escribe diez versiones del mismo mensaje. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "cuaderno",
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

# MILO-R0339 — Cuaderno: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0339",
  "seed_hash": "748ad14b4e0fc6187093152bea2c4c5230a9c61b58f8497af6acf267e5d68c4b",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_9",
  "titulo": "Cuaderno: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0339",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "cuaderno",
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

# MILO-R0340 — Cuaderno: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0340",
  "seed_hash": "8928d0407b34d43f7575d40757cd657eecb0f057647addf20cec7a32e4ef9728",
  "family_id": "F034",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_10",
  "titulo": "Cuaderno: el cuidado que necesitó permiso",
  "semilla": "Milo escribe diez versiones del mismo mensaje. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo escribe diez versiones del mismo mensaje. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "cuaderno",
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
  "replaces_seed_id": "MILO-S0340",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "elige una versión clara sin prometer un resultado",
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
      "hook": "Entrada posible desde cuaderno y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo escribe diez versiones del mismo mensaje. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo escribe diez versiones del mismo mensaje. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "cuaderno",
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

# MILO-S0341 — Reloj de cocina: la primera vez

```json
{
  "seed_id": "MILO-S0341",
  "seed_hash": "6daf54e48d5cde8f7246682313513996ea50dd2eaef3018a0b6bf3be02cf5cd7",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "primera_vez",
  "titulo": "Reloj de cocina: la primera vez",
  "semilla": "Milo mira la hora mientras espera una llamada. La espera ocupa toda la tarde. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "la espera ocupa toda la tarde",
  "accion_visible": "Milo mira la hora mientras espera una llamada",
  "objeto_emocional": "reloj de cocina",
  "giro_posible": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "reconocimiento": "la espera ocupa toda la tarde",
      "conflicto": "la espera ocupa toda la tarde",
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "vuelve a una tarea mientras conserva la posibilidad de hablar",
      "visual": "Milo mira la hora mientras espera una llamada",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada",
      "objeto": "reloj de cocina",
      "reinterpretacion": "vuelve a una tarea mientras conserva la posibilidad de hablar",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "la espera ocupa toda la tarde"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0342 — Reloj de cocina: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0342",
  "seed_hash": "a8f58c89b1e8daa28be691519de843f44661fc62f49fc875912534c82d445c6a",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_2",
  "titulo": "Reloj de cocina: la copia que no funcionó",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0342",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "reloj de cocina",
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

# MILO-R0343 — Reloj de cocina: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0343",
  "seed_hash": "aa2452de8e96c94abce59c2da2893dfbbd0e404448801a5cee279da4a99e87a6",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_3",
  "titulo": "Reloj de cocina: el favor convertido en deuda",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0343",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "reloj de cocina",
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

# MILO-R0344 — Reloj de cocina: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0344",
  "seed_hash": "0dd31fe2474796d15d1cdebba2b20f12d2e1dc2776382bbde4089166187b972a",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_4",
  "titulo": "Reloj de cocina: dos personas, dos necesidades",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0344",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "reloj de cocina",
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

# MILO-R0345 — Reloj de cocina: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0345",
  "seed_hash": "63ed296505cecc0a64e98e7e4bf1f4843afd1d03124581b561e99b0ae26083ef",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_5",
  "titulo": "Reloj de cocina: el acuerdo que nadie había entendido",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0345",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "reloj de cocina",
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

# MILO-R0346 — Reloj de cocina: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0346",
  "seed_hash": "5c7adf3722f13936f448cc926fe3354a50a7cf3336b0d9c7e08d95aac4ef0a38",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_6",
  "titulo": "Reloj de cocina: la ayuda que cambió algo querido",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0346",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "reloj de cocina",
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

# MILO-R0347 — Reloj de cocina: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0347",
  "seed_hash": "749ae136eaba6e153d0fde938aa393558b23c897f4775143b950ac3f4a111155",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_7",
  "titulo": "Reloj de cocina: la pregunta que no quería hacer",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0347",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "reloj de cocina",
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

# MILO-R0348 — Reloj de cocina: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0348",
  "seed_hash": "b2ca7c048606285fb1ab2142a4894433c8b5e39fac285e57e8f8cb57ba857b16",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_8",
  "titulo": "Reloj de cocina: el recuerdo que tenían distinto",
  "semilla": "Milo mira la hora mientras espera una llamada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0348",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo mira la hora mientras espera una llamada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "reloj de cocina",
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

# MILO-R0349 — Reloj de cocina: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0349",
  "seed_hash": "038173c4e3c2bef65ae8a24749b439c0515ed87a09e0fd1aaac960d4bf185716",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_9",
  "titulo": "Reloj de cocina: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0349",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "reloj de cocina",
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

# MILO-R0350 — Reloj de cocina: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0350",
  "seed_hash": "79101657a16e4d954ebd002b76c9bc7caeb65d822f8918d58aef4c571bc38c61",
  "family_id": "F035",
  "territorio": "Sobrepensamiento",
  "angulo": "arco_causal_10",
  "titulo": "Reloj de cocina: el cuidado que necesitó permiso",
  "semilla": "Milo mira la hora mientras espera una llamada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo mira la hora mientras espera una llamada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "reloj de cocina",
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
  "replaces_seed_id": "MILO-S0350",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "vuelve a una tarea mientras conserva la posibilidad de hablar",
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
      "hook": "Entrada posible desde reloj de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo mira la hora mientras espera una llamada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Sobrepensamiento; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Sobrepensamiento",
      "conducta": "Milo mira la hora mientras espera una llamada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "reloj de cocina",
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

# MILO-S0351 — Puerta cerrada: la primera vez

```json
{
  "seed_id": "MILO-S0351",
  "seed_hash": "c73ccda49e5e20793ae378f36c84051dece7f6dec13b0d7e4df8513aec51ed85",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "primera_vez",
  "titulo": "Puerta cerrada: la primera vez",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Teme que la familia lo tome como rechazo. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "teme que la familia lo tome como rechazo",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta",
  "objeto_emocional": "puerta cerrada",
  "giro_posible": "explica cuándo volverá y cumple",
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
      "reconocimiento": "teme que la familia lo tome como rechazo",
      "conflicto": "teme que la familia lo tome como rechazo",
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "explica cuándo volverá y cumple",
      "visual": "Milo pide un rato a solas y cierra la puerta",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta",
      "objeto": "puerta cerrada",
      "reinterpretacion": "explica cuándo volverá y cumple",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "teme que la familia lo tome como rechazo"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0352 — Puerta cerrada: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0352",
  "seed_hash": "24b9f2b92c8074a4c063d8b1f2d6efd571ad8e2208751bb48efa3a6b1f38068c",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_2",
  "titulo": "Puerta cerrada: la copia que no funcionó",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0352",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "puerta cerrada",
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

# MILO-R0353 — Puerta cerrada: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0353",
  "seed_hash": "432ec690801c29e93e223a595e6c1e49791b639e49d1fe0cd64e047a8ec62480",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_3",
  "titulo": "Puerta cerrada: el favor convertido en deuda",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0353",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "puerta cerrada",
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

# MILO-R0354 — Puerta cerrada: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0354",
  "seed_hash": "1a399278cd518e5fece8c90102cbdfc121cc68494cb9cce66a13856cccaad65f",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_4",
  "titulo": "Puerta cerrada: dos personas, dos necesidades",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0354",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "puerta cerrada",
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

# MILO-R0355 — Puerta cerrada: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0355",
  "seed_hash": "540fac06d03af176426d3625c10b9ddd76d43df2d1d058d00ef1be0b3690d836",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_5",
  "titulo": "Puerta cerrada: el acuerdo que nadie había entendido",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0355",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "puerta cerrada",
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

# MILO-R0356 — Puerta cerrada: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0356",
  "seed_hash": "462140c24fd91886d68f60b8ce4abde3163800ded1f85c357bfd76830fc02f38",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_6",
  "titulo": "Puerta cerrada: la ayuda que cambió algo querido",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0356",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "puerta cerrada",
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

# MILO-R0357 — Puerta cerrada: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0357",
  "seed_hash": "3cd1031e154ad33ae82ce16c3eead87642fc5c742995c8aeb92957657142497b",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_7",
  "titulo": "Puerta cerrada: la pregunta que no quería hacer",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0357",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "puerta cerrada",
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

# MILO-R0358 — Puerta cerrada: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0358",
  "seed_hash": "bc18ef2d43c191b301d0ba9ccef4f822c2ac156d4646720913a6a43aa24342ba",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_8",
  "titulo": "Puerta cerrada: el recuerdo que tenían distinto",
  "semilla": "Milo pide un rato a solas y cierra la puerta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0358",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo pide un rato a solas y cierra la puerta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "puerta cerrada",
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

# MILO-R0359 — Puerta cerrada: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0359",
  "seed_hash": "3d4027ca99fac55e86dc155ab592212ff918939472965925c58cd2bde1190c0f",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_9",
  "titulo": "Puerta cerrada: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0359",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "puerta cerrada",
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

# MILO-R0360 — Puerta cerrada: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0360",
  "seed_hash": "69e17e237d2dc660b9199232ab89df644d4c9268df2add08fb5868f470a6e09d",
  "family_id": "F036",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_10",
  "titulo": "Puerta cerrada: el cuidado que necesitó permiso",
  "semilla": "Milo pide un rato a solas y cierra la puerta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo pide un rato a solas y cierra la puerta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "puerta cerrada",
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
  "replaces_seed_id": "MILO-S0360",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "explica cuándo volverá y cumple",
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
      "hook": "Entrada posible desde puerta cerrada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo pide un rato a solas y cierra la puerta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide un rato a solas y cierra la puerta. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "puerta cerrada",
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

# MILO-S0361 — Teléfono boca abajo: la primera vez

```json
{
  "seed_id": "MILO-S0361",
  "seed_hash": "8b75b7b79712e0253a93301add9a189ec9b3e72b7c864bd9cf6c50aa6945160b",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "primera_vez",
  "titulo": "Teléfono boca abajo: la primera vez",
  "semilla": "Milo silencia el teléfono durante la cena. Siente culpa por no responder inmediatamente. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "siente culpa por no responder inmediatamente",
  "accion_visible": "Milo silencia el teléfono durante la cena",
  "objeto_emocional": "teléfono boca abajo",
  "giro_posible": "acuerda atender después sin desaparecer",
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
      "reconocimiento": "siente culpa por no responder inmediatamente",
      "conflicto": "siente culpa por no responder inmediatamente",
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "acuerda atender después sin desaparecer",
      "visual": "Milo silencia el teléfono durante la cena",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena",
      "objeto": "teléfono boca abajo",
      "reinterpretacion": "acuerda atender después sin desaparecer",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "siente culpa por no responder inmediatamente"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0362 — Teléfono boca abajo: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0362",
  "seed_hash": "300e90613b17f1d25382610eba36555b1b1fedfd9a18381844c30e70e34f1a00",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_2",
  "titulo": "Teléfono boca abajo: la copia que no funcionó",
  "semilla": "Milo silencia el teléfono durante la cena. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0362",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo silencia el teléfono durante la cena. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0363 — Teléfono boca abajo: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0363",
  "seed_hash": "b7d78c9a38e2687df933b90b8b9488c2f21396152e0c9e8af911794d3017e02a",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_3",
  "titulo": "Teléfono boca abajo: el favor convertido en deuda",
  "semilla": "Milo silencia el teléfono durante la cena. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0363",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo silencia el teléfono durante la cena. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0364 — Teléfono boca abajo: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0364",
  "seed_hash": "ba03641022c5b6e024c3e0c65cff449352de3dff7982ce8217963ce6f38e9db3",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_4",
  "titulo": "Teléfono boca abajo: dos personas, dos necesidades",
  "semilla": "Milo silencia el teléfono durante la cena. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0364",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo silencia el teléfono durante la cena. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0365 — Teléfono boca abajo: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0365",
  "seed_hash": "8e993a0944b0d39181547177d4e30772e86b84acb432222a34e4f1578ac10c1e",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_5",
  "titulo": "Teléfono boca abajo: el acuerdo que nadie había entendido",
  "semilla": "Milo silencia el teléfono durante la cena. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0365",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo silencia el teléfono durante la cena. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0366 — Teléfono boca abajo: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0366",
  "seed_hash": "6ed93341adfb335129927a5ff89d810f0553a7928da881c4a149cdc0acb32a0a",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_6",
  "titulo": "Teléfono boca abajo: la ayuda que cambió algo querido",
  "semilla": "Milo silencia el teléfono durante la cena. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0366",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo silencia el teléfono durante la cena. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0367 — Teléfono boca abajo: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0367",
  "seed_hash": "486540a0443370ffe3ccb29ba71b43734ea3ba29a3c734818f15b3c113316520",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_7",
  "titulo": "Teléfono boca abajo: la pregunta que no quería hacer",
  "semilla": "Milo silencia el teléfono durante la cena. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0367",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo silencia el teléfono durante la cena. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0368 — Teléfono boca abajo: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0368",
  "seed_hash": "16c32eb5bff7ac34b58313156dd6d3394cb9f4fe28d420abf0de35aa3b974392",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_8",
  "titulo": "Teléfono boca abajo: el recuerdo que tenían distinto",
  "semilla": "Milo silencia el teléfono durante la cena. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo silencia el teléfono durante la cena. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0368",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo silencia el teléfono durante la cena. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0369 — Teléfono boca abajo: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0369",
  "seed_hash": "9190193a0707a7c049fd861ad0fa2290787354a217a7f3516dd200a289b0090e",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_9",
  "titulo": "Teléfono boca abajo: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo silencia el teléfono durante la cena. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0369",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo silencia el teléfono durante la cena. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0370 — Teléfono boca abajo: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0370",
  "seed_hash": "e220ccecd4d7d55439406fde1a3d9041fbeaeaf40d923e842c562d7aa6111f61",
  "family_id": "F037",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_10",
  "titulo": "Teléfono boca abajo: el cuidado que necesitó permiso",
  "semilla": "Milo silencia el teléfono durante la cena. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo silencia el teléfono durante la cena. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "teléfono boca abajo",
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
  "replaces_seed_id": "MILO-S0370",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "acuerda atender después sin desaparecer",
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
      "hook": "Entrada posible desde teléfono boca abajo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo silencia el teléfono durante la cena. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo silencia el teléfono durante la cena. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "teléfono boca abajo",
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

# MILO-R0371 — Silla: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0371",
  "seed_hash": "a94e99e0ee13e29b9cb552c522bcf8c66b666f93f69636e4320d91515e668253",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_1",
  "titulo": "Silla: el gesto que llegó a la persona equivocada",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0371",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "silla",
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

# MILO-R0372 — Silla: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0372",
  "seed_hash": "cc6cfdbcca2cfe4e2d0a7111edcadf337c85140cdc5dc682ebc22ad0b2eab7c8",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_2",
  "titulo": "Silla: la copia que no funcionó",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0372",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "silla",
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

# MILO-R0373 — Silla: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0373",
  "seed_hash": "719daed58bfd3ce69e4011ec3401b20fc022397fdc54287d706f10efada2ff81",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_3",
  "titulo": "Silla: el favor convertido en deuda",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0373",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "silla",
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

# MILO-R0374 — Silla: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0374",
  "seed_hash": "40f1c9c1d5b3fc6a23d6bed6bee42e8e292c328f27af854ae52f46000461044f",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_4",
  "titulo": "Silla: dos personas, dos necesidades",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0374",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "silla",
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

# MILO-R0375 — Silla: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0375",
  "seed_hash": "5a6fbadb75c80143ea8f14e5b4b7a08d45b97df87a160fd95224d467f04828f1",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_5",
  "titulo": "Silla: el acuerdo que nadie había entendido",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0375",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "silla",
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

# MILO-R0376 — Silla: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0376",
  "seed_hash": "ab019d654ba55268982b6c334bc26ca6ed8ca4490f339f94a84fc8bcc8905e29",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_6",
  "titulo": "Silla: la ayuda que cambió algo querido",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0376",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "silla",
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

# MILO-R0377 — Silla: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0377",
  "seed_hash": "e8bcccaf58f8a7d5d5c2197522c2d41d62e774ed5e02b148e18c882aeb23f922",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_7",
  "titulo": "Silla: la pregunta que no quería hacer",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0377",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "silla",
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

# MILO-R0378 — Silla: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0378",
  "seed_hash": "0267e18e6b10d0d9f9db14ab125f0c068d78f2eb692cdf4306e85dd122c16b65",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_8",
  "titulo": "Silla: el recuerdo que tenían distinto",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0378",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "silla",
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

# MILO-R0379 — Silla: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0379",
  "seed_hash": "090f9d5311184e5a02ce3706cdebff9750a432afaa478c8de04b5765a9892657",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_9",
  "titulo": "Silla: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0379",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "silla",
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

# MILO-R0380 — Silla: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0380",
  "seed_hash": "f2ecccfd1f18214b42f60d888c5cf85ae1043c253763212fb85de96f58a9551d",
  "family_id": "F038",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_10",
  "titulo": "Silla: el cuidado que necesitó permiso",
  "semilla": "Milo deja de ceder siempre su lugar cómodo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo deja de ceder siempre su lugar cómodo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "silla",
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
  "replaces_seed_id": "MILO-S0380",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "pedir turnos reparte el descanso",
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
      "hook": "Entrada posible desde silla y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo deja de ceder siempre su lugar cómodo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo deja de ceder siempre su lugar cómodo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "silla",
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

# MILO-S0381 — Bolsa prestada: la primera vez

```json
{
  "seed_id": "MILO-S0381",
  "seed_hash": "9f8e8a7fa22164505051635b31200beb4598ebc9470a06bd308944a0c6255141",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "primera_vez",
  "titulo": "Bolsa prestada: la primera vez",
  "semilla": "Milo pide que devuelvan algo que necesita. Teme una discusión. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "teme una discusión",
  "accion_visible": "Milo pide que devuelvan algo que necesita",
  "objeto_emocional": "bolsa prestada",
  "giro_posible": "un pedido concreto evita acumular resentimiento",
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
      "reconocimiento": "teme una discusión",
      "conflicto": "teme una discusión",
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "un pedido concreto evita acumular resentimiento",
      "visual": "Milo pide que devuelvan algo que necesita",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita",
      "objeto": "bolsa prestada",
      "reinterpretacion": "un pedido concreto evita acumular resentimiento",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "teme una discusión"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0382 — Bolsa prestada: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0382",
  "seed_hash": "4163929cc41dc61f2bb970bae8a52a96dc5bb0650c024e80502f72a8a6e3fb57",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_2",
  "titulo": "Bolsa prestada: la copia que no funcionó",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0382",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "bolsa prestada",
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

# MILO-R0383 — Bolsa prestada: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0383",
  "seed_hash": "52ffe98c8df5134293874563d0dcda6238c70c6376560fe658866ec8bf00f59d",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_3",
  "titulo": "Bolsa prestada: el favor convertido en deuda",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0383",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "bolsa prestada",
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

# MILO-R0384 — Bolsa prestada: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0384",
  "seed_hash": "253df86d181f79ec8d0eebbf8576ef5e2c1f8221b847ad5b7352f20b868d385d",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_4",
  "titulo": "Bolsa prestada: dos personas, dos necesidades",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0384",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "bolsa prestada",
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

# MILO-R0385 — Bolsa prestada: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0385",
  "seed_hash": "b53d6b1d16b65dc34a22780d11330d6166781f533c7f727334634dfe646ea8f0",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_5",
  "titulo": "Bolsa prestada: el acuerdo que nadie había entendido",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0385",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "bolsa prestada",
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

# MILO-R0386 — Bolsa prestada: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0386",
  "seed_hash": "6bbac7ba05aab63c397827cf8f65ceee7ef697b909c2330a6711e9490aaa1399",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_6",
  "titulo": "Bolsa prestada: la ayuda que cambió algo querido",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0386",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "bolsa prestada",
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

# MILO-R0387 — Bolsa prestada: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0387",
  "seed_hash": "a67121e4d73c256a56efc817e047b960ff8ef02d87180b4473b20f09da6dc813",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_7",
  "titulo": "Bolsa prestada: la pregunta que no quería hacer",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0387",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "bolsa prestada",
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

# MILO-R0388 — Bolsa prestada: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0388",
  "seed_hash": "053784f1e8c28ae30f88d5fe9b2028b644b961183575629465c70ece309e755e",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_8",
  "titulo": "Bolsa prestada: el recuerdo que tenían distinto",
  "semilla": "Milo pide que devuelvan algo que necesita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0388",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo pide que devuelvan algo que necesita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "bolsa prestada",
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

# MILO-R0389 — Bolsa prestada: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0389",
  "seed_hash": "e75a5af589e727d2867101f15e085e248b2ca50f0fa029be955c98ca8f7cb001",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_9",
  "titulo": "Bolsa prestada: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0389",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "bolsa prestada",
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

# MILO-R0390 — Bolsa prestada: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0390",
  "seed_hash": "f85e8f7e4dd47bf7eb62b8f9c62ef8b13403c3c044beeeb5f7bf908ee111b581",
  "family_id": "F039",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_10",
  "titulo": "Bolsa prestada: el cuidado que necesitó permiso",
  "semilla": "Milo pide que devuelvan algo que necesita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo pide que devuelvan algo que necesita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "bolsa prestada",
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
  "replaces_seed_id": "MILO-S0390",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "un pedido concreto evita acumular resentimiento",
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
      "hook": "Entrada posible desde bolsa prestada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo pide que devuelvan algo que necesita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo pide que devuelvan algo que necesita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "bolsa prestada",
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

# MILO-S0391 — Calendario: la primera vez

```json
{
  "seed_id": "MILO-S0391",
  "seed_hash": "1b9736f32f480d245b3c6c9a0843f1596c24e3c8ad45aab9d14ca68ff6c69977",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "primera_vez",
  "titulo": "Calendario: la primera vez",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Confunde disponibilidad con cariño. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "confunde disponibilidad con cariño",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir",
  "objeto_emocional": "calendario",
  "giro_posible": "ofrece otro momento que sí puede sostener",
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
      "reconocimiento": "confunde disponibilidad con cariño",
      "conflicto": "confunde disponibilidad con cariño",
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "ofrece otro momento que sí puede sostener",
      "visual": "Milo rechaza un compromiso que no puede cumplir",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir",
      "objeto": "calendario",
      "reinterpretacion": "ofrece otro momento que sí puede sostener",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "confunde disponibilidad con cariño"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0392 — Calendario: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0392",
  "seed_hash": "e0ac96bfb41a5228c6bb24b826d1ecc0f5b196b0bf232bd185b14d06f8846006",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_2",
  "titulo": "Calendario: la copia que no funcionó",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0392",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "calendario",
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

# MILO-R0393 — Calendario: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0393",
  "seed_hash": "3fb1a0fc7e6ab23ed1a73db8d8b593aa99977a9d1dfe265da97b6bfe3e9ac2ca",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_3",
  "titulo": "Calendario: el favor convertido en deuda",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0393",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "calendario",
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

# MILO-R0394 — Calendario: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0394",
  "seed_hash": "12c09054f4163f6a7794f8e5c0e022a0e0c8455e5d97f698bc346ec0a3abf590",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_4",
  "titulo": "Calendario: dos personas, dos necesidades",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0394",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "calendario",
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

# MILO-R0395 — Calendario: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0395",
  "seed_hash": "4c2e7506e390f8c713ae0c14e95421f59481c1f09de595d9b7dd90990cea3dfe",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_5",
  "titulo": "Calendario: el acuerdo que nadie había entendido",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0395",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "calendario",
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

# MILO-R0396 — Calendario: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0396",
  "seed_hash": "336e38030caafcc9defe97e9fd3ab9c6b3e7be13a02fce9aa59f63e6506a169a",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_6",
  "titulo": "Calendario: la ayuda que cambió algo querido",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0396",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "calendario",
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

# MILO-R0397 — Calendario: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0397",
  "seed_hash": "388ed2487bdf6bc66575b287d2f0498fe7a16dd164ca087c2f27f79d71d541d2",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_7",
  "titulo": "Calendario: la pregunta que no quería hacer",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0397",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "calendario",
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

# MILO-R0398 — Calendario: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0398",
  "seed_hash": "e61e8fa4ad93f426942214c1c4292a0cd0e2ea4d3f5e73d8bb8319660ccbfbed",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_8",
  "titulo": "Calendario: el recuerdo que tenían distinto",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0398",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "calendario",
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

# MILO-R0399 — Calendario: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0399",
  "seed_hash": "1fed006712ce2b8bd7dee8452d1d0d7a51285d22a7059a588e4eebc7109a681b",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_9",
  "titulo": "Calendario: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0399",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "calendario",
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

# MILO-R0400 — Calendario: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0400",
  "seed_hash": "8d79dab21eb595c370fa70cc71f033e828663f7703f286872c2eb014c739dccc",
  "family_id": "F040",
  "territorio": "Límites cotidianos",
  "angulo": "arco_causal_10",
  "titulo": "Calendario: el cuidado que necesitó permiso",
  "semilla": "Milo rechaza un compromiso que no puede cumplir. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo rechaza un compromiso que no puede cumplir. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "calendario",
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
  "replaces_seed_id": "MILO-S0400",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "ofrece otro momento que sí puede sostener",
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
      "hook": "Entrada posible desde calendario y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo rechaza un compromiso que no puede cumplir. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Límites cotidianos; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Límites cotidianos",
      "conducta": "Milo rechaza un compromiso que no puede cumplir. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "calendario",
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
