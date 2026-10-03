# MILO SEEDS — PARTE 07

Banco: `2.0.0`
Registros: `0601–0700`

## REGLAS

- Datos canónicos.
- No inventar campos.
- No recalcular seed_hash.
- El seed_id puede normalizarse desde el encabezado lógico/registro según `18_SEED_HEADER_NORMALIZATION.md`.

# MILO-S0601 — Vaso de agua: la primera vez

```json
{
  "seed_id": "MILO-S0601",
  "seed_hash": "4051636f46921e2e7b7058b7cc03aa920ffab51db189788b554105fd30bc63f8",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "primera_vez",
  "titulo": "Vaso de agua: la primera vez",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Teme no saber qué decir. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "teme no saber qué decir",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos",
  "objeto_emocional": "vaso de agua",
  "giro_posible": "una presencia sencilla permite empezar",
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
      "reconocimiento": "teme no saber qué decir",
      "conflicto": "teme no saber qué decir",
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "una presencia sencilla permite empezar",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos",
      "objeto": "vaso de agua",
      "reinterpretacion": "una presencia sencilla permite empezar",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "teme no saber qué decir"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0602 — Vaso de agua: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0602",
  "seed_hash": "99c01cbeac74ac0b6f19db1fdbe0b0c35547eda65bf4551e31a1dc1b7dece0fc",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_2",
  "titulo": "Vaso de agua: la copia que no funcionó",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0602",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "vaso de agua",
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

# MILO-R0603 — Vaso de agua: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0603",
  "seed_hash": "382ea1894dffd398c01da75ca20bcfb76b615779f29b62b3d90dbc0ee302f1b4",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_3",
  "titulo": "Vaso de agua: el favor convertido en deuda",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0603",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "vaso de agua",
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

# MILO-R0604 — Vaso de agua: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0604",
  "seed_hash": "96ddbe1845a954ebc9b3d35cc0000217196e11a0de62c6940b5ee6d33dca8c6e",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_4",
  "titulo": "Vaso de agua: dos personas, dos necesidades",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0604",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "vaso de agua",
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

# MILO-R0605 — Vaso de agua: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0605",
  "seed_hash": "e48c7b99ad32f1da1972f219921f87e3cc75b93b93aa3e12f628e5d75f3c634d",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_5",
  "titulo": "Vaso de agua: el acuerdo que nadie había entendido",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0605",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "vaso de agua",
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

# MILO-R0606 — Vaso de agua: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0606",
  "seed_hash": "6457182cd5ceac5a5fe457714277bd1d55a4eeb3f248bd41e684872759918c41",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_6",
  "titulo": "Vaso de agua: la ayuda que cambió algo querido",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0606",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "vaso de agua",
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

# MILO-R0607 — Vaso de agua: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0607",
  "seed_hash": "cdb45eaafe3f7e980f7dccf4a77692d68823961faf2eb0be2b87c2c00fd94891",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_7",
  "titulo": "Vaso de agua: la pregunta que no quería hacer",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0607",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "vaso de agua",
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

# MILO-R0608 — Vaso de agua: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0608",
  "seed_hash": "ace5e63428378df5e16d95f0db5c19c2d2f6e87a5b216fdf0e3c8a8b338764b1",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_8",
  "titulo": "Vaso de agua: el recuerdo que tenían distinto",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0608",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "vaso de agua",
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

# MILO-R0609 — Vaso de agua: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0609",
  "seed_hash": "bca36d508a502e26d2936644d05ee57fcb51710f3a4da60fa8dc83007536708e",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_9",
  "titulo": "Vaso de agua: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0609",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "vaso de agua",
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

# MILO-R0610 — Vaso de agua: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0610",
  "seed_hash": "d1ccbe7b3d31346e2bc9e3e9e551e40f82333a571f0dec80dea3ab7f7e682631",
  "family_id": "F061",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_10",
  "titulo": "Vaso de agua: el cuidado que necesitó permiso",
  "semilla": "Milo recibe a alguien y ofrece agua antes de consejos. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo recibe a alguien y ofrece agua antes de consejos. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "vaso de agua",
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
  "replaces_seed_id": "MILO-S0610",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "una presencia sencilla permite empezar",
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
      "hook": "Entrada posible desde vaso de agua y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo recibe a alguien y ofrece agua antes de consejos. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo recibe a alguien y ofrece agua antes de consejos. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "vaso de agua",
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

# MILO-S0611 — Sofá: la primera vez

```json
{
  "seed_id": "MILO-S0611",
  "seed_hash": "9cfb06b8caa68dd15fbbb984fdf4270fb2552bfb849dc540b0bf716f8a1e2217",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "primera_vez",
  "titulo": "Sofá: la primera vez",
  "semilla": "Milo hace espacio para una visita callada. Interpreta su silencio como incomodidad. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "interpreta su silencio como incomodidad",
  "accion_visible": "Milo hace espacio para una visita callada",
  "objeto_emocional": "sofá",
  "giro_posible": "pregunta si prefiere hablar o estar acompañado",
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
      "reconocimiento": "interpreta su silencio como incomodidad",
      "conflicto": "interpreta su silencio como incomodidad",
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "pregunta si prefiere hablar o estar acompañado",
      "visual": "Milo hace espacio para una visita callada",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada",
      "objeto": "sofá",
      "reinterpretacion": "pregunta si prefiere hablar o estar acompañado",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "interpreta su silencio como incomodidad"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0612 — Sofá: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0612",
  "seed_hash": "94b3c514c478b0cc3822a080223fa7de501612561647709934bbe18ac587ddd2",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_2",
  "titulo": "Sofá: la copia que no funcionó",
  "semilla": "Milo hace espacio para una visita callada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0612",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo hace espacio para una visita callada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "sofá",
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

# MILO-R0613 — Sofá: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0613",
  "seed_hash": "335a248b68d8f958c5303268433223d86f9d6821c89bb5884dbb2b706604cc70",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_3",
  "titulo": "Sofá: el favor convertido en deuda",
  "semilla": "Milo hace espacio para una visita callada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0613",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo hace espacio para una visita callada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "sofá",
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

# MILO-R0614 — Sofá: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0614",
  "seed_hash": "e65de4aeebf290167f9a7376d6a2d28cd78e47e9968eac5d333686b31de0c613",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_4",
  "titulo": "Sofá: dos personas, dos necesidades",
  "semilla": "Milo hace espacio para una visita callada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0614",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo hace espacio para una visita callada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "sofá",
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

# MILO-R0615 — Sofá: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0615",
  "seed_hash": "a0f71d0f1094293560f97d6bfc69e87984c6d45e53fbea18c0982c5cecd6aba8",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_5",
  "titulo": "Sofá: el acuerdo que nadie había entendido",
  "semilla": "Milo hace espacio para una visita callada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0615",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo hace espacio para una visita callada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "sofá",
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

# MILO-R0616 — Sofá: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0616",
  "seed_hash": "3a18426eb96ef8f329ceb631ba604c38c2b74b13d8a469c28e5ef2fcbaee41e3",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_6",
  "titulo": "Sofá: la ayuda que cambió algo querido",
  "semilla": "Milo hace espacio para una visita callada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0616",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo hace espacio para una visita callada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "sofá",
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

# MILO-R0617 — Sofá: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0617",
  "seed_hash": "376eebf5872a87666526d3e979cb039367edf01aa27dd77e657ae2f2e0bf63d4",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_7",
  "titulo": "Sofá: la pregunta que no quería hacer",
  "semilla": "Milo hace espacio para una visita callada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0617",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo hace espacio para una visita callada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "sofá",
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

# MILO-R0618 — Sofá: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0618",
  "seed_hash": "9eb09bc786a17813aaf02710d041ffba56abbea046423bfcdbbcd423b7c6317c",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_8",
  "titulo": "Sofá: el recuerdo que tenían distinto",
  "semilla": "Milo hace espacio para una visita callada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo hace espacio para una visita callada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0618",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo hace espacio para una visita callada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "sofá",
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

# MILO-R0619 — Sofá: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0619",
  "seed_hash": "264fafe738a3506733af129467c1e7d421b50a2b8908c210717e0e255f48be4c",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_9",
  "titulo": "Sofá: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo hace espacio para una visita callada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0619",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo hace espacio para una visita callada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "sofá",
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

# MILO-R0620 — Sofá: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0620",
  "seed_hash": "d16d8a32ea352abc5b6c2f7035bc9ec7958ed0f1a33233583dab69421a3fa673",
  "family_id": "F062",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_10",
  "titulo": "Sofá: el cuidado que necesitó permiso",
  "semilla": "Milo hace espacio para una visita callada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo hace espacio para una visita callada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "sofá",
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
  "replaces_seed_id": "MILO-S0620",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "pregunta si prefiere hablar o estar acompañado",
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
      "hook": "Entrada posible desde sofá y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo hace espacio para una visita callada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo hace espacio para una visita callada. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "sofá",
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

# MILO-S0621 — Llamada: la primera vez

```json
{
  "seed_id": "MILO-S0621",
  "seed_hash": "ff4989273f40f7fcd6b8514bc0a7b35afc8811ac213863a78d7f2c9a3241415b",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "primera_vez",
  "titulo": "Llamada: la primera vez",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Piensa que no tiene nada que ofrecer. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "piensa que no tiene nada que ofrecer",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes",
  "objeto_emocional": "llamada",
  "giro_posible": "una conversación cotidiana también sostiene amistad",
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
      "reconocimiento": "piensa que no tiene nada que ofrecer",
      "conflicto": "piensa que no tiene nada que ofrecer",
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "una conversación cotidiana también sostiene amistad",
      "visual": "Milo posterga una llamada hasta tener noticias importantes",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes",
      "objeto": "llamada",
      "reinterpretacion": "una conversación cotidiana también sostiene amistad",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "piensa que no tiene nada que ofrecer"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0622 — Llamada: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0622",
  "seed_hash": "ffb6ad2935510d1191cb354193b06038af6b8265e1ac96f065461c19daba06ca",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_2",
  "titulo": "Llamada: la copia que no funcionó",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0622",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "llamada",
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

# MILO-R0623 — Llamada: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0623",
  "seed_hash": "fff195cdddc99af92ecd594ae54e04dfb587a0b5e5002bbf49270d1751020ca1",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_3",
  "titulo": "Llamada: el favor convertido en deuda",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0623",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "llamada",
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

# MILO-R0624 — Llamada: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0624",
  "seed_hash": "f396cf4cd741a327167ac02d19d7b13489030b52cc10c3937464f6d88626b012",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_4",
  "titulo": "Llamada: dos personas, dos necesidades",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0624",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "llamada",
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

# MILO-R0625 — Llamada: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0625",
  "seed_hash": "7ed5ae57bb3863039e0a167038c611676303d9c7b86c3d0857eecc8b08a4f456",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_5",
  "titulo": "Llamada: el acuerdo que nadie había entendido",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0625",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "llamada",
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

# MILO-R0626 — Llamada: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0626",
  "seed_hash": "e48e87053d998ccf50daa98693e6960c7dc52d9c4912ce8bb59ecb73c46c3ddd",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_6",
  "titulo": "Llamada: la ayuda que cambió algo querido",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0626",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "llamada",
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

# MILO-R0627 — Llamada: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0627",
  "seed_hash": "101758f86b8a8d65e38a54f5eac34e05d63b3daac2637bcd1577b0ab81db0837",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_7",
  "titulo": "Llamada: la pregunta que no quería hacer",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0627",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "llamada",
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

# MILO-R0628 — Llamada: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0628",
  "seed_hash": "781ab99b52a90303046fc879bcb67b489241b2266596ca148881ac4c635399d5",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_8",
  "titulo": "Llamada: el recuerdo que tenían distinto",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0628",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "llamada",
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

# MILO-R0629 — Llamada: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0629",
  "seed_hash": "cdb703dd79ae8cf4d47ebcec9e83be48a945e5395242304e43adb977e49bd83b",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_9",
  "titulo": "Llamada: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0629",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "llamada",
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

# MILO-R0630 — Llamada: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0630",
  "seed_hash": "dff3d8a3a7cc01ce236af4e133afb057b6761e9a74639d29361e5c4772ba32ef",
  "family_id": "F063",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_10",
  "titulo": "Llamada: el cuidado que necesitó permiso",
  "semilla": "Milo posterga una llamada hasta tener noticias importantes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo posterga una llamada hasta tener noticias importantes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "llamada",
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
  "replaces_seed_id": "MILO-S0630",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "una conversación cotidiana también sostiene amistad",
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
      "hook": "Entrada posible desde llamada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo posterga una llamada hasta tener noticias importantes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo posterga una llamada hasta tener noticias importantes. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "llamada",
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

# MILO-S0631 — Juego de mesa: la primera vez

```json
{
  "seed_id": "MILO-S0631",
  "seed_hash": "56f94e928a03c4ec149a6ccd11572755834f282309e36db40baf34c54b804ca1",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "primera_vez",
  "titulo": "Juego de mesa: la primera vez",
  "semilla": "Milo retoma un juego con una visita. Cree que deben resolver primero todas sus diferencias. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "cree que deben resolver primero todas sus diferencias",
  "accion_visible": "Milo retoma un juego con una visita",
  "objeto_emocional": "juego de mesa",
  "giro_posible": "compartir una actividad abre un contacto pequeño",
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
      "reconocimiento": "cree que deben resolver primero todas sus diferencias",
      "conflicto": "cree que deben resolver primero todas sus diferencias",
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "compartir una actividad abre un contacto pequeño",
      "visual": "Milo retoma un juego con una visita",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita",
      "objeto": "juego de mesa",
      "reinterpretacion": "compartir una actividad abre un contacto pequeño",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "cree que deben resolver primero todas sus diferencias"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0632 — Juego de mesa: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0632",
  "seed_hash": "d6a89f6cc4eb179a8d13c96ae69d7769d30a378364ccf32376b87751e0e99715",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_2",
  "titulo": "Juego de mesa: la copia que no funcionó",
  "semilla": "Milo retoma un juego con una visita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo retoma un juego con una visita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0632",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo retoma un juego con una visita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "juego de mesa",
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

# MILO-R0633 — Juego de mesa: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0633",
  "seed_hash": "a1ca94e0ad9b015a7d9e77ffd100aed1c8732c5691590520ad4006faf34c5f7c",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_3",
  "titulo": "Juego de mesa: el favor convertido en deuda",
  "semilla": "Milo retoma un juego con una visita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo retoma un juego con una visita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0633",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo retoma un juego con una visita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "juego de mesa",
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

# MILO-R0634 — Juego de mesa: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0634",
  "seed_hash": "32e12a44d6d57b0ca8c2de0e26ce931b7752970f7b8466303ce91f874c5da6c9",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_4",
  "titulo": "Juego de mesa: dos personas, dos necesidades",
  "semilla": "Milo retoma un juego con una visita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo retoma un juego con una visita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0634",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo retoma un juego con una visita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "juego de mesa",
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

# MILO-R0635 — Juego de mesa: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0635",
  "seed_hash": "a85bd6aa926252176c3fe4af0b2c6b7f2ae72bd243e5eadcbfa01df17b6e4428",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_5",
  "titulo": "Juego de mesa: el acuerdo que nadie había entendido",
  "semilla": "Milo retoma un juego con una visita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo retoma un juego con una visita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0635",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo retoma un juego con una visita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "juego de mesa",
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

# MILO-R0636 — Juego de mesa: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0636",
  "seed_hash": "fd6ced2d594d6f4dba511a81baf634561503f1c289bb53f209b96e20004b0716",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_6",
  "titulo": "Juego de mesa: la ayuda que cambió algo querido",
  "semilla": "Milo retoma un juego con una visita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo retoma un juego con una visita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0636",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo retoma un juego con una visita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "juego de mesa",
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

# MILO-R0637 — Juego de mesa: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0637",
  "seed_hash": "5260300b24ef5f7ad69a0d55d51274ca2e3f1b03b1b246f0700792164a895187",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_7",
  "titulo": "Juego de mesa: la pregunta que no quería hacer",
  "semilla": "Milo retoma un juego con una visita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo retoma un juego con una visita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0637",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo retoma un juego con una visita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "juego de mesa",
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

# MILO-R0638 — Juego de mesa: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0638",
  "seed_hash": "975544507d6a5c4bcd5953de0eea3e906259ac71c1617e28a7d7d98c45fc911d",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_8",
  "titulo": "Juego de mesa: el recuerdo que tenían distinto",
  "semilla": "Milo retoma un juego con una visita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo retoma un juego con una visita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0638",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo retoma un juego con una visita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "juego de mesa",
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

# MILO-R0639 — Juego de mesa: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0639",
  "seed_hash": "27c84d4979ff3904e8aa29193d58da6c68ef32fb8092b18ab3abaf8ed724e7b1",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_9",
  "titulo": "Juego de mesa: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo retoma un juego con una visita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo retoma un juego con una visita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0639",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo retoma un juego con una visita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "juego de mesa",
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

# MILO-R0640 — Juego de mesa: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0640",
  "seed_hash": "eff96b153b22be31ebba77b18a2bdd9958d48ccbefcf212a4030752aa2cb34df",
  "family_id": "F064",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_10",
  "titulo": "Juego de mesa: el cuidado que necesitó permiso",
  "semilla": "Milo retoma un juego con una visita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo retoma un juego con una visita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "juego de mesa",
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
  "replaces_seed_id": "MILO-S0640",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "compartir una actividad abre un contacto pequeño",
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
      "hook": "Entrada posible desde juego de mesa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo retoma un juego con una visita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo retoma un juego con una visita. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "juego de mesa",
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

# MILO-S0641 — Plato extra: la primera vez

```json
{
  "seed_id": "MILO-S0641",
  "seed_hash": "aed96ae13fad8e8d7f46c26c05f33153ab82e10a3c756da324ccd779bcd1a6f0",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "primera_vez",
  "titulo": "Plato extra: la primera vez",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Teme invadir. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "teme invadir",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano",
  "objeto_emocional": "plato extra",
  "giro_posible": "ofrece sin exigir aceptar ni explicar",
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
      "reconocimiento": "teme invadir",
      "conflicto": "teme invadir",
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "ofrece sin exigir aceptar ni explicar",
      "visual": "Milo prepara una porción adicional para alguien cercano",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano",
      "objeto": "plato extra",
      "reinterpretacion": "ofrece sin exigir aceptar ni explicar",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "teme invadir"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0642 — Plato extra: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0642",
  "seed_hash": "56655803b134955d4149120160a3abd003f38ae9d0609b0527bc953b23ae78c0",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_2",
  "titulo": "Plato extra: la copia que no funcionó",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0642",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "plato extra",
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

# MILO-R0643 — Plato extra: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0643",
  "seed_hash": "87ebd523d13626946592886e3033e2332fc6aa389d5278e2e306fc399bafd318",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_3",
  "titulo": "Plato extra: el favor convertido en deuda",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0643",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "plato extra",
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

# MILO-R0644 — Plato extra: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0644",
  "seed_hash": "3c1e35e775f8d4a8ae689da6718da66baa8ce1153a8e713fc396f227db94d5e5",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_4",
  "titulo": "Plato extra: dos personas, dos necesidades",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0644",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "plato extra",
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

# MILO-R0645 — Plato extra: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0645",
  "seed_hash": "3a6584074773749295a5d54e19a84f016d92227acbcb94e1e5ca42c930b5966f",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_5",
  "titulo": "Plato extra: el acuerdo que nadie había entendido",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0645",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "plato extra",
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

# MILO-R0646 — Plato extra: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0646",
  "seed_hash": "1e64e696dd8d5a1fad1252f3833e8890669fc6be39d77f1b7e81043c4b710264",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_6",
  "titulo": "Plato extra: la ayuda que cambió algo querido",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0646",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "plato extra",
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

# MILO-R0647 — Plato extra: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0647",
  "seed_hash": "a9fcea4d60a9fbf3ce0d4d02ee93ea43718d2e3ba84c7cc0f4f3dfea86a48e93",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_7",
  "titulo": "Plato extra: la pregunta que no quería hacer",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0647",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "plato extra",
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

# MILO-R0648 — Plato extra: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0648",
  "seed_hash": "572dd538ec5c06dca62c63052222ec21bbcfcd2f6521323c650ec56dedd097f9",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_8",
  "titulo": "Plato extra: el recuerdo que tenían distinto",
  "semilla": "Milo prepara una porción adicional para alguien cercano. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0648",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo prepara una porción adicional para alguien cercano. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "plato extra",
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

# MILO-R0649 — Plato extra: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0649",
  "seed_hash": "6183545617f9f49ce555d1b86797b0d5d2680331607c68eba6b039570ccda317",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_9",
  "titulo": "Plato extra: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0649",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "plato extra",
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

# MILO-R0650 — Plato extra: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0650",
  "seed_hash": "2f21ba74b8327d51aef86e52dd483de45cc3cb45bc1b655a7963b20d7c10f44d",
  "family_id": "F065",
  "territorio": "Amistad en casa",
  "angulo": "arco_causal_10",
  "titulo": "Plato extra: el cuidado que necesitó permiso",
  "semilla": "Milo prepara una porción adicional para alguien cercano. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo prepara una porción adicional para alguien cercano. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "plato extra",
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
  "replaces_seed_id": "MILO-S0650",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "ofrece sin exigir aceptar ni explicar",
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
      "hook": "Entrada posible desde plato extra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo prepara una porción adicional para alguien cercano. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Amistad en casa; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Amistad en casa",
      "conducta": "Milo prepara una porción adicional para alguien cercano. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "plato extra",
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

# MILO-R0651 — Manta: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0651",
  "seed_hash": "b6979e331c740ea484d6ca591d674fbad6d081742323be4ebbb99ccbef397cb0",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_1",
  "titulo": "Manta: el gesto que llegó a la persona equivocada",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0651",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "manta",
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

# MILO-R0652 — Manta: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0652",
  "seed_hash": "f3322fbb24ed97ac84a4518c200e7a0c07a6425a4c4ecb3f9be067a885d34209",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_2",
  "titulo": "Manta: la copia que no funcionó",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0652",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "manta",
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

# MILO-R0653 — Manta: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0653",
  "seed_hash": "9bfafe92be138de37bc7373444a7ba2cc1032ebfc71af43394015a9ff4c9fc1d",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_3",
  "titulo": "Manta: el favor convertido en deuda",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0653",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "manta",
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

# MILO-R0654 — Manta: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0654",
  "seed_hash": "691f2d48793ebfa812754b1063ce310cff8de7b6e188a867a72e72052b8f58d7",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_4",
  "titulo": "Manta: dos personas, dos necesidades",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0654",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "manta",
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

# MILO-R0655 — Manta: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0655",
  "seed_hash": "631b0afcc683026410a92a1cc4efd6c232483c0b841a538c324147750d917c4d",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_5",
  "titulo": "Manta: el acuerdo que nadie había entendido",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0655",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "manta",
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

# MILO-R0656 — Manta: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0656",
  "seed_hash": "435c616b3882c4558406747bc2a3c8d5b2d66833df3ed750c1ee2ae22882624c",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_6",
  "titulo": "Manta: la ayuda que cambió algo querido",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0656",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "manta",
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

# MILO-R0657 — Manta: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0657",
  "seed_hash": "620f90fd010cd051504c26c9236f657dbfe44ad8e19733e408401e5c0013ebf7",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_7",
  "titulo": "Manta: la pregunta que no quería hacer",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0657",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "manta",
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

# MILO-R0658 — Manta: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0658",
  "seed_hash": "718e6f5d73dd06238d1ee124cbe925a73c317080877850f7a6c68838aa62c864",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_8",
  "titulo": "Manta: el recuerdo que tenían distinto",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0658",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "manta",
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

# MILO-R0659 — Manta: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0659",
  "seed_hash": "5313d16dc1156d070b937d496cdac68c62c2796de904a40817e9b446ce0ffc84",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_9",
  "titulo": "Manta: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0659",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "manta",
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

# MILO-R0660 — Manta: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0660",
  "seed_hash": "5b84ccce00686aef83a98a77027ac25d68a66227a1439b6f24955224207f2c34",
  "family_id": "F066",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_10",
  "titulo": "Manta: el cuidado que necesitó permiso",
  "semilla": "Milo cubre a quien se quedó dormido en el sofá. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo cubre a quien se quedó dormido en el sofá. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "manta",
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
  "replaces_seed_id": "MILO-S0660",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "un gesto pequeño puede ser suficiente",
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
      "hook": "Entrada posible desde manta y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo cubre a quien se quedó dormido en el sofá. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo cubre a quien se quedó dormido en el sofá. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "manta",
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

# MILO-S0661 — Bandeja: la primera vez

```json
{
  "seed_id": "MILO-S0661",
  "seed_hash": "e17695a9bc53f00e1e9c27e255cfc59fbeb77714492264d95abbca4ca3e16439",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "primera_vez",
  "titulo": "Bandeja: la primera vez",
  "semilla": "Milo lleva comida a quien está descansando. Espera un agradecimiento inmediato. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "espera un agradecimiento inmediato",
  "accion_visible": "Milo lleva comida a quien está descansando",
  "objeto_emocional": "bandeja",
  "giro_posible": "pregunta qué necesita sin cobrar emoción",
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
      "reconocimiento": "espera un agradecimiento inmediato",
      "conflicto": "espera un agradecimiento inmediato",
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "pregunta qué necesita sin cobrar emoción",
      "visual": "Milo lleva comida a quien está descansando",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando",
      "objeto": "bandeja",
      "reinterpretacion": "pregunta qué necesita sin cobrar emoción",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "espera un agradecimiento inmediato"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0662 — Bandeja: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0662",
  "seed_hash": "35a02656a7ace8a10848376937a80328e3976ad185473d683b354ef8c5fa7d6a",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_2",
  "titulo": "Bandeja: la copia que no funcionó",
  "semilla": "Milo lleva comida a quien está descansando. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0662",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo lleva comida a quien está descansando. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "bandeja",
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

# MILO-R0663 — Bandeja: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0663",
  "seed_hash": "d6ad0bc878aca5efbfce7e07bad4bedf89f1731026a2bfe75c38f39cdcf516dd",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_3",
  "titulo": "Bandeja: el favor convertido en deuda",
  "semilla": "Milo lleva comida a quien está descansando. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0663",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo lleva comida a quien está descansando. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "bandeja",
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

# MILO-R0664 — Bandeja: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0664",
  "seed_hash": "2dc918aea8b7168e5ee3a4e9dfa73b337145871ff2a54c0fb88546650be3bde1",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_4",
  "titulo": "Bandeja: dos personas, dos necesidades",
  "semilla": "Milo lleva comida a quien está descansando. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0664",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo lleva comida a quien está descansando. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "bandeja",
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

# MILO-R0665 — Bandeja: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0665",
  "seed_hash": "cfad4f72c934e7c9837a1c5ecf428c964642e304897b0cea2a302ec9fc686f78",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_5",
  "titulo": "Bandeja: el acuerdo que nadie había entendido",
  "semilla": "Milo lleva comida a quien está descansando. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0665",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo lleva comida a quien está descansando. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "bandeja",
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

# MILO-R0666 — Bandeja: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0666",
  "seed_hash": "0b73ab3911c5382678b4886b63c42d7b6f2fa59d111024b538204756ca09751a",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_6",
  "titulo": "Bandeja: la ayuda que cambió algo querido",
  "semilla": "Milo lleva comida a quien está descansando. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0666",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo lleva comida a quien está descansando. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "bandeja",
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

# MILO-R0667 — Bandeja: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0667",
  "seed_hash": "bede617ac04315681aae0638f7adcc00574191acb9c16f6091b708f7121ad136",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_7",
  "titulo": "Bandeja: la pregunta que no quería hacer",
  "semilla": "Milo lleva comida a quien está descansando. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0667",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo lleva comida a quien está descansando. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "bandeja",
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

# MILO-R0668 — Bandeja: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0668",
  "seed_hash": "01d115db3fb25791ead8b693c9c967aed77dd4d7cbd009ff26654cbdd23430aa",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_8",
  "titulo": "Bandeja: el recuerdo que tenían distinto",
  "semilla": "Milo lleva comida a quien está descansando. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo lleva comida a quien está descansando. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0668",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo lleva comida a quien está descansando. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "bandeja",
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

# MILO-R0669 — Bandeja: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0669",
  "seed_hash": "227241d6df2a3fcf6e11f601a4ead19dc7cf34352a534c91e125057ba0440708",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_9",
  "titulo": "Bandeja: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo lleva comida a quien está descansando. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0669",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo lleva comida a quien está descansando. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "bandeja",
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

# MILO-R0670 — Bandeja: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0670",
  "seed_hash": "07cdecd4680b40b2dae588526220a178472f3b64a0ae6e81d57015f12aac1ae9",
  "family_id": "F067",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_10",
  "titulo": "Bandeja: el cuidado que necesitó permiso",
  "semilla": "Milo lleva comida a quien está descansando. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo lleva comida a quien está descansando. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "bandeja",
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
  "replaces_seed_id": "MILO-S0670",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "pregunta qué necesita sin cobrar emoción",
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
      "hook": "Entrada posible desde bandeja y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo lleva comida a quien está descansando. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo lleva comida a quien está descansando. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "bandeja",
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

# MILO-S0671 — Escoba: la primera vez

```json
{
  "seed_id": "MILO-S0671",
  "seed_hash": "f6a4fe2c18c8af2eacd5699ddaabe856623b2fe2594e007cf1cb61214a3f4a37",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "primera_vez",
  "titulo": "Escoba: la primera vez",
  "semilla": "Milo empieza una tarea que otro hace siempre. Teme hacerla diferente. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "teme hacerla diferente",
  "accion_visible": "Milo empieza una tarea que otro hace siempre",
  "objeto_emocional": "escoba",
  "giro_posible": "pide orientación y asume una parte estable",
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
      "reconocimiento": "teme hacerla diferente",
      "conflicto": "teme hacerla diferente",
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "pide orientación y asume una parte estable",
      "visual": "Milo empieza una tarea que otro hace siempre",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre",
      "objeto": "escoba",
      "reinterpretacion": "pide orientación y asume una parte estable",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "teme hacerla diferente"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0672 — Escoba: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0672",
  "seed_hash": "656fdc9be20452cd4d79cdd3a3f9f4a00e60905721a5e74d891b68fd78e1b446",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_2",
  "titulo": "Escoba: la copia que no funcionó",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0672",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "escoba",
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

# MILO-R0673 — Escoba: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0673",
  "seed_hash": "9fc184307809379f48bb8ee132e9fe66e777d4d33b30b74b7acbb1067415b28c",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_3",
  "titulo": "Escoba: el favor convertido en deuda",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0673",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "escoba",
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

# MILO-R0674 — Escoba: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0674",
  "seed_hash": "45b750c55fd6b987037658e4a9a9c143c6b08be49b6b0bd1fca6638c636de167",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_4",
  "titulo": "Escoba: dos personas, dos necesidades",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0674",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "escoba",
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

# MILO-R0675 — Escoba: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0675",
  "seed_hash": "e8fa533a6d0609e34e80047a6c80e5b1b7078498945b9dcace74ca30419df6c2",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_5",
  "titulo": "Escoba: el acuerdo que nadie había entendido",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0675",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "escoba",
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

# MILO-R0676 — Escoba: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0676",
  "seed_hash": "4331688fcbf6b7f2d3025721e08dba138c78db5a51d654707b352949b76c054b",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_6",
  "titulo": "Escoba: la ayuda que cambió algo querido",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0676",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "escoba",
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

# MILO-R0677 — Escoba: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0677",
  "seed_hash": "d979152fae0f4d21ba366be18e992cfd9f70593ed839a07e1f60ff308df38182",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_7",
  "titulo": "Escoba: la pregunta que no quería hacer",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0677",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "escoba",
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

# MILO-R0678 — Escoba: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0678",
  "seed_hash": "05ff789e2e6992645f7629ad4cb62fe2e3af4a34c30b6a0bc7ef1642e53eac75",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_8",
  "titulo": "Escoba: el recuerdo que tenían distinto",
  "semilla": "Milo empieza una tarea que otro hace siempre. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0678",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo empieza una tarea que otro hace siempre. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "escoba",
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

# MILO-R0679 — Escoba: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0679",
  "seed_hash": "8c2e771b93733b72e6a4909045fe51e141faa06812d20b7c211947f6cd607068",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_9",
  "titulo": "Escoba: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0679",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "escoba",
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

# MILO-R0680 — Escoba: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0680",
  "seed_hash": "fc61b72a985c1d47a53dc3adf69d9f64318a8b0793c301925d88b52718708376",
  "family_id": "F068",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_10",
  "titulo": "Escoba: el cuidado que necesitó permiso",
  "semilla": "Milo empieza una tarea que otro hace siempre. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo empieza una tarea que otro hace siempre. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "escoba",
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
  "replaces_seed_id": "MILO-S0680",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "pide orientación y asume una parte estable",
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
      "hook": "Entrada posible desde escoba y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo empieza una tarea que otro hace siempre. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo empieza una tarea que otro hace siempre. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "escoba",
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

# MILO-R0681 — Jarra: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0681",
  "seed_hash": "c807dd0da42220bddd5b24d74423027f7a71d2054ad5bed206c6a0347a6cfe2c",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_1",
  "titulo": "Jarra: el gesto que llegó a la persona equivocada",
  "semilla": "Milo deja agua al alcance de un familiar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0681",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "Milo deja agua al alcance de un familiar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "jarra",
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

# MILO-R0682 — Jarra: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0682",
  "seed_hash": "aa1028f90d834771e9972eb2453d21e8be911cedcae54e13c1dae6288309b034",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_2",
  "titulo": "Jarra: la copia que no funcionó",
  "semilla": "Milo deja agua al alcance de un familiar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0682",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo deja agua al alcance de un familiar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "jarra",
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

# MILO-R0683 — Jarra: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0683",
  "seed_hash": "fccd5bf4b3b683db7c4a4bc5d3242a8987d59985b68dbbb5707a57e89c56c939",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_3",
  "titulo": "Jarra: el favor convertido en deuda",
  "semilla": "Milo deja agua al alcance de un familiar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0683",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo deja agua al alcance de un familiar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "jarra",
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

# MILO-R0684 — Jarra: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0684",
  "seed_hash": "dcdf9161815a1227224f80ae0d6992dad63f3bba120fa96046ee9849e92c65a2",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_4",
  "titulo": "Jarra: dos personas, dos necesidades",
  "semilla": "Milo deja agua al alcance de un familiar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0684",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo deja agua al alcance de un familiar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "jarra",
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

# MILO-R0685 — Jarra: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0685",
  "seed_hash": "6e97e56f2fe3cdbc0136b30ad6ef06de791728833f74beace644bea8922b9a4e",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_5",
  "titulo": "Jarra: el acuerdo que nadie había entendido",
  "semilla": "Milo deja agua al alcance de un familiar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0685",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo deja agua al alcance de un familiar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "jarra",
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

# MILO-R0686 — Jarra: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0686",
  "seed_hash": "fb748ec97b4298b35bfc021d09c330014278eeb87e04ba923409e3530432eb1f",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_6",
  "titulo": "Jarra: la ayuda que cambió algo querido",
  "semilla": "Milo deja agua al alcance de un familiar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0686",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo deja agua al alcance de un familiar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "jarra",
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

# MILO-R0687 — Jarra: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0687",
  "seed_hash": "ff993e44e9a53c50336f26f14bb52f27b84948b4fbbd38a9d4b355c4f3b81213",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_7",
  "titulo": "Jarra: la pregunta que no quería hacer",
  "semilla": "Milo deja agua al alcance de un familiar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0687",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo deja agua al alcance de un familiar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "jarra",
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

# MILO-R0688 — Jarra: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0688",
  "seed_hash": "c4a2de748c6ec4f07f9f7238c04fe73815230f7d1bc521603127f099d9ee6876",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_8",
  "titulo": "Jarra: el recuerdo que tenían distinto",
  "semilla": "Milo deja agua al alcance de un familiar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo deja agua al alcance de un familiar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0688",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo deja agua al alcance de un familiar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "jarra",
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

# MILO-R0689 — Jarra: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0689",
  "seed_hash": "ad7fd99f5e9e44701d0c6c41a5327770022e7df28877316a43f308bd61f0715c",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_9",
  "titulo": "Jarra: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo deja agua al alcance de un familiar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0689",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo deja agua al alcance de un familiar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "jarra",
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

# MILO-R0690 — Jarra: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0690",
  "seed_hash": "d7fa70dc55463e3a139979336a3887f8ac2272edae78b65f57d5b2b2ce0c001c",
  "family_id": "F069",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_10",
  "titulo": "Jarra: el cuidado que necesitó permiso",
  "semilla": "Milo deja agua al alcance de un familiar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo deja agua al alcance de un familiar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "jarra",
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
  "replaces_seed_id": "MILO-S0690",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "la atención puede ser concreta y discreta",
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
      "hook": "Entrada posible desde jarra y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo deja agua al alcance de un familiar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo deja agua al alcance de un familiar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "jarra",
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

# MILO-S0691 — Almohada: la primera vez

```json
{
  "seed_id": "MILO-S0691",
  "seed_hash": "3bc7c941740a491149860f73422432b46414b3b69143313c54d76eeefc53f7cb",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "primera_vez",
  "titulo": "Almohada: la primera vez",
  "semilla": "Milo prepara un rincón cómodo para conversar. Quiere resolver el problema de quien llega. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "quiere resolver el problema de quien llega",
  "accion_visible": "Milo prepara un rincón cómodo para conversar",
  "objeto_emocional": "almohada",
  "giro_posible": "escucha antes de proponer soluciones",
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
      "reconocimiento": "quiere resolver el problema de quien llega",
      "conflicto": "quiere resolver el problema de quien llega",
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "escucha antes de proponer soluciones",
      "visual": "Milo prepara un rincón cómodo para conversar",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar",
      "objeto": "almohada",
      "reinterpretacion": "escucha antes de proponer soluciones",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "quiere resolver el problema de quien llega"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0692 — Almohada: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0692",
  "seed_hash": "f390cbac099c9e4e9efacfed69c4040131cc52acc5d2dfe8f7f230b1e62a098e",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_2",
  "titulo": "Almohada: la copia que no funcionó",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0692",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "almohada",
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

# MILO-R0693 — Almohada: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0693",
  "seed_hash": "96c28048575c6dcffd04ba6ca5aa9a0c505cfc72938a4d53b8e754cd1b586e4b",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_3",
  "titulo": "Almohada: el favor convertido en deuda",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0693",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "almohada",
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

# MILO-R0694 — Almohada: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0694",
  "seed_hash": "f76b54b5e761bfe7c96434baa9fdaeaa9cb02b27497c2a5e67532241e6494c97",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_4",
  "titulo": "Almohada: dos personas, dos necesidades",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0694",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "almohada",
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

# MILO-R0695 — Almohada: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0695",
  "seed_hash": "8e63289cfdee260ac38f8c2c18b425754fddb69d61d2ef1d454179688e564b74",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_5",
  "titulo": "Almohada: el acuerdo que nadie había entendido",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0695",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "almohada",
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

# MILO-R0696 — Almohada: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0696",
  "seed_hash": "21c22b2822cf6d179aecbb29316fc5968b147f5af895cbac848bc2b47595a25d",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_6",
  "titulo": "Almohada: la ayuda que cambió algo querido",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0696",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "almohada",
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

# MILO-R0697 — Almohada: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0697",
  "seed_hash": "87f99f52d8f473e229c393b16c06321901fb086dab0e4abc9fdbea528ca92006",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_7",
  "titulo": "Almohada: la pregunta que no quería hacer",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0697",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "almohada",
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

# MILO-R0698 — Almohada: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0698",
  "seed_hash": "9ab1b726f9f6278488e79e10ff271f3f5f659698f2ceb97fcc0a54554000e8c5",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_8",
  "titulo": "Almohada: el recuerdo que tenían distinto",
  "semilla": "Milo prepara un rincón cómodo para conversar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0698",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "Milo prepara un rincón cómodo para conversar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "almohada",
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

# MILO-R0699 — Almohada: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0699",
  "seed_hash": "0bd7990a30cbca627ba8b1c54d203b4eab7924174a19550d94481595f231f3aa",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_9",
  "titulo": "Almohada: el agradecimiento dicho demasiado tarde",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0699",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "almohada",
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

# MILO-R0700 — Almohada: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0700",
  "seed_hash": "d536a65c041df4f8e2e09b79dc300e24b9ceb20cc52074979925627754da60ee",
  "family_id": "F070",
  "territorio": "Cuidado recíproco",
  "angulo": "arco_causal_10",
  "titulo": "Almohada: el cuidado que necesitó permiso",
  "semilla": "Milo prepara un rincón cómodo para conversar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "Milo prepara un rincón cómodo para conversar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "almohada",
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
  "replaces_seed_id": "MILO-S0700",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "escucha antes de proponer soluciones",
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
      "hook": "Entrada posible desde almohada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "Milo prepara un rincón cómodo para conversar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Cuidado recíproco; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Cuidado recíproco",
      "conducta": "Milo prepara un rincón cómodo para conversar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "almohada",
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
