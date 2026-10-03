# MILO SEEDS — PARTE 01

Banco: `2.0.0`
Registros: `0001–0100`

## REGLAS

- Datos canónicos.
- No inventar campos.
- No recalcular seed_hash.
- El seed_id puede normalizarse desde el encabezado lógico/registro según `18_SEED_HEADER_NORMALIZATION.md`.

# MILO-S0001 — Plato tapado: la primera vez

```json
{
  "seed_id": "MILO-S0001",
  "seed_hash": "113739653e9bcae9dac5a65e3a8a091062ce065d4835511ecc46e8ec6e43927f",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "primera_vez",
  "titulo": "Plato tapado: la primera vez",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo interpreta el silencio como distancia. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo interpreta el silencio como distancia",
  "accion_visible": "papá deja la cena aunque Milo llega tarde",
  "objeto_emocional": "plato tapado",
  "giro_posible": "el plato demuestra que alguien contó con su regreso",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "papá"
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
      "reconocimiento": "Milo interpreta el silencio como distancia",
      "conflicto": "Milo interpreta el silencio como distancia",
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "el plato demuestra que alguien contó con su regreso",
      "visual": "papá deja la cena aunque Milo llega tarde",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde",
      "objeto": "plato tapado",
      "reinterpretacion": "el plato demuestra que alguien contó con su regreso",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo interpreta el silencio como distancia"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0002 — Plato tapado: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0002",
  "seed_hash": "f8da818d8dbf851bbedfbadf9a0c115490fe4ac58aa5fea8b23f5d1348171d8a",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_2",
  "titulo": "Plato tapado: la copia que no funcionó",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0002",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "plato tapado",
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

# MILO-R0003 — Plato tapado: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0003",
  "seed_hash": "cd78deb83e75744146c6041c061c4acdf40581506987eac866895adc99cea128",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_3",
  "titulo": "Plato tapado: el favor convertido en deuda",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0003",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "plato tapado",
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

# MILO-R0004 — Plato tapado: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0004",
  "seed_hash": "5043760632dbd5834ec14d8950452ea39fdf410d409bbbf675c5023ed9146948",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_4",
  "titulo": "Plato tapado: dos personas, dos necesidades",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0004",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "plato tapado",
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

# MILO-R0005 — Plato tapado: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0005",
  "seed_hash": "2341577798ca2e3de6cb4edd99362989241106a99b79f4845db726e81673c551",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_5",
  "titulo": "Plato tapado: el acuerdo que nadie había entendido",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0005",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "plato tapado",
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

# MILO-R0006 — Plato tapado: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0006",
  "seed_hash": "b350893e9d088ed7369e1daf36d8a69f64e2ad75955084605c0197c30c9accf7",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_6",
  "titulo": "Plato tapado: la ayuda que cambió algo querido",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0006",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "plato tapado",
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

# MILO-R0007 — Plato tapado: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0007",
  "seed_hash": "ee1386fb4845ad53eef42667a9f8b2293917eafbaf25be008abdbc6338ab4f69",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_7",
  "titulo": "Plato tapado: la pregunta que no quería hacer",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0007",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "plato tapado",
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

# MILO-R0008 — Plato tapado: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0008",
  "seed_hash": "3df47f272b073cef0742ba865fa11ea1c6f08bfa23c86103a4f739fc01812102",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_8",
  "titulo": "Plato tapado: el recuerdo que tenían distinto",
  "semilla": "Papá deja la cena aunque Milo llega tarde. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0008",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "papá deja la cena aunque Milo llega tarde. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "plato tapado",
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

# MILO-R0009 — Plato tapado: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0009",
  "seed_hash": "d876e97b9f09d9393b0ba0444334db43102f556398095de36438e89f2bcfab21",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_9",
  "titulo": "Plato tapado: el agradecimiento dicho demasiado tarde",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0009",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "plato tapado",
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

# MILO-R0010 — Plato tapado: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0010",
  "seed_hash": "7fb873af6e3d159e7d0d901ebee58eda7c27efa2e7cd8233e8e54b6fbacf59b6",
  "family_id": "F001",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_10",
  "titulo": "Plato tapado: el cuidado que necesitó permiso",
  "semilla": "Papá deja la cena aunque Milo llega tarde. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "papá deja la cena aunque Milo llega tarde. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "plato tapado",
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
  "replaces_seed_id": "MILO-S0010",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "el plato demuestra que alguien contó con su regreso",
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
      "hook": "Entrada posible desde plato tapado y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "papá deja la cena aunque Milo llega tarde. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja la cena aunque Milo llega tarde. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "plato tapado",
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

# MILO-S0011 — Luz del pasillo: la primera vez

```json
{
  "seed_id": "MILO-S0011",
  "seed_hash": "ffa1c171f48f4e6228326971b988e9aabac61e45916814aece56748297e78d3c",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "primera_vez",
  "titulo": "Luz del pasillo: la primera vez",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo cree que olvidó apagarla. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo cree que olvidó apagarla",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves",
  "objeto_emocional": "luz del pasillo",
  "giro_posible": "la luz acompaña una espera que nunca anunció",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "papá"
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
      "reconocimiento": "Milo cree que olvidó apagarla",
      "conflicto": "Milo cree que olvidó apagarla",
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "la luz acompaña una espera que nunca anunció",
      "visual": "papá deja una luz encendida hasta escuchar las llaves",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves",
      "objeto": "luz del pasillo",
      "reinterpretacion": "la luz acompaña una espera que nunca anunció",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo cree que olvidó apagarla"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0012 — Luz del pasillo: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0012",
  "seed_hash": "30a8e288306203bc26db12fb035be5129f6bae99641cb49b0ae2166b851962e6",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_2",
  "titulo": "Luz del pasillo: la copia que no funcionó",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0012",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "luz del pasillo",
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

# MILO-R0013 — Luz del pasillo: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0013",
  "seed_hash": "4cb12d19c141bbae06589948b0462b718badeb8a17849cf9fc1c65f36f2a5523",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_3",
  "titulo": "Luz del pasillo: el favor convertido en deuda",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0013",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "luz del pasillo",
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

# MILO-R0014 — Luz del pasillo: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0014",
  "seed_hash": "eca111e3ac504b9a32cc02ac253fa16563af2d2adbd30bbb6014dd16d6bc0b04",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_4",
  "titulo": "Luz del pasillo: dos personas, dos necesidades",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0014",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "luz del pasillo",
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

# MILO-R0015 — Luz del pasillo: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0015",
  "seed_hash": "c07e9f1b2365b8493a986b5054de22eebb28f588f58271db89cb1934fea99107",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_5",
  "titulo": "Luz del pasillo: el acuerdo que nadie había entendido",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0015",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "luz del pasillo",
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

# MILO-R0016 — Luz del pasillo: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0016",
  "seed_hash": "03a326eb783cf4c0b8278616e7df370dbec305affd27fd7c16a48f6fd3584fdb",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_6",
  "titulo": "Luz del pasillo: la ayuda que cambió algo querido",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0016",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "luz del pasillo",
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

# MILO-R0017 — Luz del pasillo: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0017",
  "seed_hash": "4da1d3ca3a7d1e9b712467c0b19b9e2fd4f7c98d943d62dd42e5b7e9c8770b24",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_7",
  "titulo": "Luz del pasillo: la pregunta que no quería hacer",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0017",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "luz del pasillo",
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

# MILO-R0018 — Luz del pasillo: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0018",
  "seed_hash": "b6f79cdc6ad95ebc3d1809f723515ed45c9614a3774364b5cde5ff6cacb82e1e",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_8",
  "titulo": "Luz del pasillo: el recuerdo que tenían distinto",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0018",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "luz del pasillo",
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

# MILO-R0019 — Luz del pasillo: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0019",
  "seed_hash": "aedf911257c57d870ce44dbac5e54ed6b15b1aab4e60957a44db21b7d0a8d78f",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_9",
  "titulo": "Luz del pasillo: el agradecimiento dicho demasiado tarde",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0019",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "luz del pasillo",
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

# MILO-R0020 — Luz del pasillo: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0020",
  "seed_hash": "83f7c95df3eda059863b78eb0984b17f31b41adcb6301c3002a3e5b9dab0f25c",
  "family_id": "F002",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_10",
  "titulo": "Luz del pasillo: el cuidado que necesitó permiso",
  "semilla": "Papá deja una luz encendida hasta escuchar las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "papá deja una luz encendida hasta escuchar las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "luz del pasillo",
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
  "replaces_seed_id": "MILO-S0020",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "la luz acompaña una espera que nunca anunció",
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
      "hook": "Entrada posible desde luz del pasillo y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "papá deja una luz encendida hasta escuchar las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja una luz encendida hasta escuchar las llaves. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "luz del pasillo",
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

# MILO-S0021 — Zapatos reparados: la primera vez

```json
{
  "seed_id": "MILO-S0021",
  "seed_hash": "71a70da7a352f028e53e3b8b72e0465f66ce40632997c6c97cc86c6364403083",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "primera_vez",
  "titulo": "Zapatos reparados: la primera vez",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo siente vergüenza del remiendo. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo siente vergüenza del remiendo",
  "accion_visible": "papá repara un zapato de Milo durante la noche",
  "objeto_emocional": "zapatos reparados",
  "giro_posible": "el remiendo guarda tiempo de cuidado",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "papá"
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
      "reconocimiento": "Milo siente vergüenza del remiendo",
      "conflicto": "Milo siente vergüenza del remiendo",
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "el remiendo guarda tiempo de cuidado",
      "visual": "papá repara un zapato de Milo durante la noche",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche",
      "objeto": "zapatos reparados",
      "reinterpretacion": "el remiendo guarda tiempo de cuidado",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo siente vergüenza del remiendo"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0022 — Zapatos reparados: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0022",
  "seed_hash": "1122687ab37fbc01eebeae466e9a16f950ecea16b0530aaee5061dca3af19e2e",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_2",
  "titulo": "Zapatos reparados: la copia que no funcionó",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0022",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "zapatos reparados",
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

# MILO-R0023 — Zapatos reparados: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0023",
  "seed_hash": "5c6ea52ba1deba31ecc13087cc509c26323b070f2591ee989c8f94f1fb580a50",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_3",
  "titulo": "Zapatos reparados: el favor convertido en deuda",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0023",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "zapatos reparados",
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

# MILO-R0024 — Zapatos reparados: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0024",
  "seed_hash": "86936a6c8c7853fd8d0f80493165a9f6999916654925691a23a76f02946963eb",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_4",
  "titulo": "Zapatos reparados: dos personas, dos necesidades",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0024",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "zapatos reparados",
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

# MILO-R0025 — Zapatos reparados: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0025",
  "seed_hash": "213b447eaa3cfd0053b952098961e12c912ed9ceaf2535bc27961caf1da6a86f",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_5",
  "titulo": "Zapatos reparados: el acuerdo que nadie había entendido",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0025",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "zapatos reparados",
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

# MILO-R0026 — Zapatos reparados: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0026",
  "seed_hash": "0f3c69017aeff6010be3d9a05c8b69be448b3b34d0c4ff65c0e6413a385b6deb",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_6",
  "titulo": "Zapatos reparados: la ayuda que cambió algo querido",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0026",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "zapatos reparados",
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

# MILO-R0027 — Zapatos reparados: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0027",
  "seed_hash": "54b122f2d8e642ab80b071bfd5e79f87aa4c76ec997083d64af546fac7841bfe",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_7",
  "titulo": "Zapatos reparados: la pregunta que no quería hacer",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0027",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "zapatos reparados",
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

# MILO-R0028 — Zapatos reparados: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0028",
  "seed_hash": "73c487a5021373f64ac7c5395a9d177a57c61bd7a11e2cd40a0ad9d1f8105f67",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_8",
  "titulo": "Zapatos reparados: el recuerdo que tenían distinto",
  "semilla": "Papá repara un zapato de Milo durante la noche. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0028",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "papá repara un zapato de Milo durante la noche. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "zapatos reparados",
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

# MILO-R0029 — Zapatos reparados: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0029",
  "seed_hash": "08e0ce96a1d69dd7d5fc3c29957835dd926de58accd2c1a317e339044412277a",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_9",
  "titulo": "Zapatos reparados: el agradecimiento dicho demasiado tarde",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0029",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "zapatos reparados",
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

# MILO-R0030 — Zapatos reparados: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0030",
  "seed_hash": "13d1a395066d4efa4db5efee6431aa6bafc6bfa538192608b400022c2ddd8b89",
  "family_id": "F003",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_10",
  "titulo": "Zapatos reparados: el cuidado que necesitó permiso",
  "semilla": "Papá repara un zapato de Milo durante la noche. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "papá repara un zapato de Milo durante la noche. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "zapatos reparados",
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
  "replaces_seed_id": "MILO-S0030",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "el remiendo guarda tiempo de cuidado",
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
      "hook": "Entrada posible desde zapatos reparados y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "papá repara un zapato de Milo durante la noche. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá repara un zapato de Milo durante la noche. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "zapatos reparados",
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

# MILO-S0031 — Paraguas: la primera vez

```json
{
  "seed_id": "MILO-S0031",
  "seed_hash": "b3e79ebfdffb275c0b8ca23ab97e13ab03ecb3df94abd5e880314be6e2190776",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "primera_vez",
  "titulo": "Paraguas: la primera vez",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo se molesta por otra recomendación. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo se molesta por otra recomendación",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo",
  "objeto_emocional": "paraguas",
  "giro_posible": "papá había visto el cielo antes de dormir",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "papá"
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
      "reconocimiento": "Milo se molesta por otra recomendación",
      "conflicto": "Milo se molesta por otra recomendación",
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "papá había visto el cielo antes de dormir",
      "visual": "papá deja el paraguas junto a la puerta de Milo",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo",
      "objeto": "paraguas",
      "reinterpretacion": "papá había visto el cielo antes de dormir",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo se molesta por otra recomendación"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0032 — Paraguas: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0032",
  "seed_hash": "3ada8f2829111aa3700f843a454c70cc17598931a3f6a5ea891c9418d3ed7357",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_2",
  "titulo": "Paraguas: la copia que no funcionó",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0032",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "paraguas",
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

# MILO-R0033 — Paraguas: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0033",
  "seed_hash": "61718c153b5f90aca93c94e67affe4f044153f326f645b699aee2c68b073cfac",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_3",
  "titulo": "Paraguas: el favor convertido en deuda",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0033",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "paraguas",
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

# MILO-R0034 — Paraguas: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0034",
  "seed_hash": "ae3a5da50d25fab88f38f626a3c53486007f2cdd4275e5251b8e1841d68be7d5",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_4",
  "titulo": "Paraguas: dos personas, dos necesidades",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0034",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "paraguas",
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

# MILO-R0035 — Paraguas: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0035",
  "seed_hash": "976b351af75a43e6ac9504c9032eeb9122a9eb95d189e9f3ee8a6d89d30e3132",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_5",
  "titulo": "Paraguas: el acuerdo que nadie había entendido",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0035",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "paraguas",
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

# MILO-R0036 — Paraguas: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0036",
  "seed_hash": "d1fe0678d856e5eba3e9b0a2e5d13d2ef252b1cad22079466d7d6ab6b995c9fa",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_6",
  "titulo": "Paraguas: la ayuda que cambió algo querido",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0036",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "paraguas",
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

# MILO-R0037 — Paraguas: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0037",
  "seed_hash": "1ecdf6ec14bdb0e73804cf46033bf564bc1d4ab0a6eecbaaca57c5f9558e8c7e",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_7",
  "titulo": "Paraguas: la pregunta que no quería hacer",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0037",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "paraguas",
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

# MILO-R0038 — Paraguas: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0038",
  "seed_hash": "adce2e6062b68d247215b286583410fe401b440d17ac40febfb3020eb1dc5c3c",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_8",
  "titulo": "Paraguas: el recuerdo que tenían distinto",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0038",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "paraguas",
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

# MILO-R0039 — Paraguas: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0039",
  "seed_hash": "055e031d1f3b0c4016d5bc30666fa0ab5279c4284e0585e060a34e1c0b2475e0",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_9",
  "titulo": "Paraguas: el agradecimiento dicho demasiado tarde",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0039",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "paraguas",
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

# MILO-R0040 — Paraguas: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0040",
  "seed_hash": "b6f99f3d5b03a9f73ecd255485d71e12915e40f7cbb3b9d02ca30507469602ed",
  "family_id": "F004",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_10",
  "titulo": "Paraguas: el cuidado que necesitó permiso",
  "semilla": "Papá deja el paraguas junto a la puerta de Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "papá deja el paraguas junto a la puerta de Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "paraguas",
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
  "replaces_seed_id": "MILO-S0040",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "papá había visto el cielo antes de dormir",
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
      "hook": "Entrada posible desde paraguas y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "papá deja el paraguas junto a la puerta de Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá deja el paraguas junto a la puerta de Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "paraguas",
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

# MILO-S0041 — Taza tibia: la primera vez

```json
{
  "seed_id": "MILO-S0041",
  "seed_hash": "bbea283e2e336da3364f1f4a28a3cfe4f6b726fb462c1352ca863b05b4c1bb88",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "primera_vez",
  "titulo": "Taza tibia: la primera vez",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo supone que no quiere conversar. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo supone que no quiere conversar",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo",
  "objeto_emocional": "taza tibia",
  "giro_posible": "la taza abre una conversación pequeña",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "papá"
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
      "reconocimiento": "Milo supone que no quiere conversar",
      "conflicto": "Milo supone que no quiere conversar",
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "la taza abre una conversación pequeña",
      "visual": "papá prepara una bebida sin interrumpir a Milo",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo",
      "objeto": "taza tibia",
      "reinterpretacion": "la taza abre una conversación pequeña",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo supone que no quiere conversar"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0042 — Taza tibia: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0042",
  "seed_hash": "bdec5d265cfb4663490eab8c411942b1b14ae173a5a8fc5c83ca162918b4b77c",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_2",
  "titulo": "Taza tibia: la copia que no funcionó",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0042",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "taza tibia",
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

# MILO-R0043 — Taza tibia: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0043",
  "seed_hash": "fcf9f9d5f7b9ae7dedf4c714568597af814d9e3615df3cb9e86ef5d26cce9878",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_3",
  "titulo": "Taza tibia: el favor convertido en deuda",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0043",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "taza tibia",
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

# MILO-R0044 — Taza tibia: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0044",
  "seed_hash": "7542157d07e1ac4651d4c0427fc50c6d31ee7669e485ea1dfdb7186c5478f0cd",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_4",
  "titulo": "Taza tibia: dos personas, dos necesidades",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0044",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "taza tibia",
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

# MILO-R0045 — Taza tibia: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0045",
  "seed_hash": "717120fb92c5545ff953829983ea59634db388ac1d17c2823141c6d1db063356",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_5",
  "titulo": "Taza tibia: el acuerdo que nadie había entendido",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0045",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "taza tibia",
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

# MILO-R0046 — Taza tibia: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0046",
  "seed_hash": "af98b1faab3f06aa23e55d3e336a4cc8ebb4acfc149d98fb7f97f6ac3fcd5755",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_6",
  "titulo": "Taza tibia: la ayuda que cambió algo querido",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0046",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "taza tibia",
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

# MILO-R0047 — Taza tibia: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0047",
  "seed_hash": "d1d27eb5c8574d6fdce6fd26e982d0b0b877e3ec5aa7a3374fcc82ad8a07d3e9",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_7",
  "titulo": "Taza tibia: la pregunta que no quería hacer",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0047",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "taza tibia",
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

# MILO-R0048 — Taza tibia: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0048",
  "seed_hash": "26e15fdf8b50f99f23335a03e66fbeb09594d6d8921db590795b65e3e35216e3",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_8",
  "titulo": "Taza tibia: el recuerdo que tenían distinto",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0048",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "taza tibia",
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

# MILO-R0049 — Taza tibia: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0049",
  "seed_hash": "6dd3b2d9f050b8104077142e8728bdc75081309c691e461740896de778460290",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_9",
  "titulo": "Taza tibia: el agradecimiento dicho demasiado tarde",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0049",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "taza tibia",
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

# MILO-R0050 — Taza tibia: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0050",
  "seed_hash": "a95230bd9d64abafc82cff9fa0273f755502566bb40e9b2861a55f21440a914d",
  "family_id": "F005",
  "territorio": "Padre y cariño",
  "angulo": "arco_causal_10",
  "titulo": "Taza tibia: el cuidado que necesitó permiso",
  "semilla": "Papá prepara una bebida sin interrumpir a Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "papá prepara una bebida sin interrumpir a Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "taza tibia",
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
  "replaces_seed_id": "MILO-S0050",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "la taza abre una conversación pequeña",
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
      "hook": "Entrada posible desde taza tibia y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "papá prepara una bebida sin interrumpir a Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Padre y cariño; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Padre y cariño",
      "conducta": "papá prepara una bebida sin interrumpir a Milo. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "taza tibia",
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

# MILO-S0051 — Bolsa de compras: la primera vez

```json
{
  "seed_id": "MILO-S0051",
  "seed_hash": "45655bef4a5690f641801f65fd59d7ec69eb73525c1176edde813dce79469145",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "primera_vez",
  "titulo": "Bolsa de compras: la primera vez",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo confunde su actividad con energía infinita. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo confunde su actividad con energía infinita",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan",
  "objeto_emocional": "bolsa de compras",
  "giro_posible": "una segunda mano cambia su tarde",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "mamá"
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
      "reconocimiento": "Milo confunde su actividad con energía infinita",
      "conflicto": "Milo confunde su actividad con energía infinita",
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "una segunda mano cambia su tarde",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan",
      "objeto": "bolsa de compras",
      "reinterpretacion": "una segunda mano cambia su tarde",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo confunde su actividad con energía infinita"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0052 — Bolsa de compras: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0052",
  "seed_hash": "44f5b84b5b8398a123fc3de2b534acea04270684814aae8c11ccc8cfda744374",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_2",
  "titulo": "Bolsa de compras: la copia que no funcionó",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0052",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "bolsa de compras",
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

# MILO-R0053 — Bolsa de compras: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0053",
  "seed_hash": "c887d7b0c79d86de5a428757d784df6001c8127504d2b5242bfb853b185f5d20",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_3",
  "titulo": "Bolsa de compras: el favor convertido en deuda",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0053",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "bolsa de compras",
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

# MILO-R0054 — Bolsa de compras: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0054",
  "seed_hash": "2bc50704f1215d65ea412150879ccf3de9f5376ecb80a591d39b1d02dd085438",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_4",
  "titulo": "Bolsa de compras: dos personas, dos necesidades",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0054",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "bolsa de compras",
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

# MILO-R0055 — Bolsa de compras: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0055",
  "seed_hash": "077d6187dbcc25368ad0315a4fed3f3f0b1f723feb590cb03ef73286df036bd2",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_5",
  "titulo": "Bolsa de compras: el acuerdo que nadie había entendido",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0055",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "bolsa de compras",
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

# MILO-R0056 — Bolsa de compras: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0056",
  "seed_hash": "a909f43c22c4d60f72ec11b191b9a97f23e07faaef07c2db9a9e0aa62cc8a91d",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_6",
  "titulo": "Bolsa de compras: la ayuda que cambió algo querido",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0056",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "bolsa de compras",
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

# MILO-R0057 — Bolsa de compras: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0057",
  "seed_hash": "906e0bc6b4b10043263105ab8416913de4c575a95ef709126e80ec33b3bfe43d",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_7",
  "titulo": "Bolsa de compras: la pregunta que no quería hacer",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0057",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "bolsa de compras",
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

# MILO-R0058 — Bolsa de compras: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0058",
  "seed_hash": "410ff417757c9ecba28581ad84ad4c199fefa94ec3fd3cd8523e25617e38c264",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_8",
  "titulo": "Bolsa de compras: el recuerdo que tenían distinto",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0058",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "bolsa de compras",
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

# MILO-R0059 — Bolsa de compras: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0059",
  "seed_hash": "1aafc5accb132b1e6cbbecb109935816d3df0dff5c9a3b9f26b72809a18b5389",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_9",
  "titulo": "Bolsa de compras: el agradecimiento dicho demasiado tarde",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0059",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "bolsa de compras",
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

# MILO-R0060 — Bolsa de compras: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0060",
  "seed_hash": "c033f38249dea7c68818f41954357b1406074b9cdba3b2d025d909510efcf4ff",
  "family_id": "F006",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_10",
  "titulo": "Bolsa de compras: el cuidado que necesitó permiso",
  "semilla": "Mamá llega y sigue guardando alimentos mientras todos descansan. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "bolsa de compras",
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
  "replaces_seed_id": "MILO-S0060",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "una segunda mano cambia su tarde",
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
      "hook": "Entrada posible desde bolsa de compras y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá llega y sigue guardando alimentos mientras todos descansan. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "bolsa de compras",
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

# MILO-R0061 — Delantal: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0061",
  "seed_hash": "17079dba8064d0888741f971db849ffc30532d564eb639d220dcde8fe2e4095d",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_1",
  "titulo": "Delantal: el gesto que llegó a la persona equivocada",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0061",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "delantal",
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

# MILO-R0062 — Delantal: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0062",
  "seed_hash": "107b5ed6df6f737d2c4b42365bbb4ad56007fd3a23bfdd2de6668b8981c043d7",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_2",
  "titulo": "Delantal: la copia que no funcionó",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0062",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "delantal",
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

# MILO-R0063 — Delantal: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0063",
  "seed_hash": "f98ae21cac1ff1ad98f7253e32c0a2cf98a45b64b2e6f88e6c48903b696b7ffd",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_3",
  "titulo": "Delantal: el favor convertido en deuda",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0063",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "delantal",
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

# MILO-R0064 — Delantal: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0064",
  "seed_hash": "bd311f5f817baba0ca9f7b8a23c07a7fd42f71731fac749c479f9c04da152dd8",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_4",
  "titulo": "Delantal: dos personas, dos necesidades",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0064",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "delantal",
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

# MILO-R0065 — Delantal: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0065",
  "seed_hash": "8a681aef6c17f84493fdd7a2ad2622c5b7efd249209bd656d7af68c1e8cda709",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_5",
  "titulo": "Delantal: el acuerdo que nadie había entendido",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0065",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "delantal",
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

# MILO-R0066 — Delantal: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0066",
  "seed_hash": "151c804a05b3b4b38cebb617c1a8f4db4b4ab0f6c10322a845ba69ca91400806",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_6",
  "titulo": "Delantal: la ayuda que cambió algo querido",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0066",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "delantal",
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

# MILO-R0067 — Delantal: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0067",
  "seed_hash": "0925ee2521a6b7a116e011e2454525fd266c8dabe6f8d46e2e830e651eedb0a4",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_7",
  "titulo": "Delantal: la pregunta que no quería hacer",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0067",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "delantal",
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

# MILO-R0068 — Delantal: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0068",
  "seed_hash": "29217b7324003ce6200091cf9c2b45d32749ae551ad3bb40301e16fdd1867616",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_8",
  "titulo": "Delantal: el recuerdo que tenían distinto",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0068",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "delantal",
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

# MILO-R0069 — Delantal: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0069",
  "seed_hash": "eed97fa14b2de44ed6637d4481968c2b620cf6cf06192214cd6e9c860427b49d",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_9",
  "titulo": "Delantal: el agradecimiento dicho demasiado tarde",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0069",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "delantal",
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

# MILO-R0070 — Delantal: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0070",
  "seed_hash": "fa8d080ec142fdc75038f7d9eb9ff765807b04c89a645745710acd5f38b225ef",
  "family_id": "F007",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_10",
  "titulo": "Delantal: el cuidado que necesitó permiso",
  "semilla": "Mamá se quita el delantal para sentarse antes de terminar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "mamá se quita el delantal para sentarse antes de terminar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "delantal",
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
  "replaces_seed_id": "MILO-S0070",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "descansar también cabe en la casa",
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
      "hook": "Entrada posible desde delantal y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "mamá se quita el delantal para sentarse antes de terminar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá se quita el delantal para sentarse antes de terminar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "delantal",
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

# MILO-S0071 — Taza olvidada: la primera vez

```json
{
  "seed_id": "MILO-S0071",
  "seed_hash": "7b0293d492f4ddde64d58578770717782bc1c603b79f14873cb97a197caf30ae",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "primera_vez",
  "titulo": "Taza olvidada: la primera vez",
  "semilla": "Mamá recalienta tres veces su bebida. Milo no nota las interrupciones. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo no nota las interrupciones",
  "accion_visible": "mamá recalienta tres veces su bebida",
  "objeto_emocional": "taza olvidada",
  "giro_posible": "servírsela a tiempo es una forma de verla",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "mamá"
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
      "reconocimiento": "Milo no nota las interrupciones",
      "conflicto": "Milo no nota las interrupciones",
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "servírsela a tiempo es una forma de verla",
      "visual": "mamá recalienta tres veces su bebida",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida",
      "objeto": "taza olvidada",
      "reinterpretacion": "servírsela a tiempo es una forma de verla",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo no nota las interrupciones"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0072 — Taza olvidada: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0072",
  "seed_hash": "88057c332909083b89902cc59b67002c70990ef001b765c3b4dfe2ac7e370f03",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_2",
  "titulo": "Taza olvidada: la copia que no funcionó",
  "semilla": "Mamá recalienta tres veces su bebida. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0072",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "mamá recalienta tres veces su bebida. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "taza olvidada",
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

# MILO-R0073 — Taza olvidada: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0073",
  "seed_hash": "0e1fe92e829587d9c38e71ae78272d76e0c5a7429df20ad7bf0017b9654780e5",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_3",
  "titulo": "Taza olvidada: el favor convertido en deuda",
  "semilla": "Mamá recalienta tres veces su bebida. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0073",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "mamá recalienta tres veces su bebida. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "taza olvidada",
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

# MILO-R0074 — Taza olvidada: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0074",
  "seed_hash": "df980e8050ced35856a648e8ab565b729f2120b15c2e0c8b3d20aa61b37282c1",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_4",
  "titulo": "Taza olvidada: dos personas, dos necesidades",
  "semilla": "Mamá recalienta tres veces su bebida. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0074",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "mamá recalienta tres veces su bebida. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "taza olvidada",
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

# MILO-R0075 — Taza olvidada: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0075",
  "seed_hash": "3de4f0444dffb8578f2fcc89119c5f5227b84c4b1be6928f6c844e409a819d76",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_5",
  "titulo": "Taza olvidada: el acuerdo que nadie había entendido",
  "semilla": "Mamá recalienta tres veces su bebida. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0075",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "mamá recalienta tres veces su bebida. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "taza olvidada",
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

# MILO-R0076 — Taza olvidada: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0076",
  "seed_hash": "52b53a48d337d3a2d3d95375dad6b57afd3ccac752fb5398f7221c58c9d75c25",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_6",
  "titulo": "Taza olvidada: la ayuda que cambió algo querido",
  "semilla": "Mamá recalienta tres veces su bebida. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0076",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "mamá recalienta tres veces su bebida. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "taza olvidada",
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

# MILO-R0077 — Taza olvidada: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0077",
  "seed_hash": "a276a7cd81656e8ef3b91411dd7487dd043f84e2950fe8cdb653bdec0f992169",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_7",
  "titulo": "Taza olvidada: la pregunta que no quería hacer",
  "semilla": "Mamá recalienta tres veces su bebida. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0077",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "mamá recalienta tres veces su bebida. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "taza olvidada",
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

# MILO-R0078 — Taza olvidada: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0078",
  "seed_hash": "14ff55f47264dae97e8af831eedc84a4dcd63175e12fc72f490dda9ad0a2e009",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_8",
  "titulo": "Taza olvidada: el recuerdo que tenían distinto",
  "semilla": "Mamá recalienta tres veces su bebida. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "mamá recalienta tres veces su bebida. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0078",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "mamá recalienta tres veces su bebida. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "taza olvidada",
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

# MILO-R0079 — Taza olvidada: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0079",
  "seed_hash": "c18c22b399e2d6d045402e3bf177033c14b9e224af9f1a07f4f87e5bba80ba9c",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_9",
  "titulo": "Taza olvidada: el agradecimiento dicho demasiado tarde",
  "semilla": "Mamá recalienta tres veces su bebida. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0079",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "mamá recalienta tres veces su bebida. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "taza olvidada",
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

# MILO-R0080 — Taza olvidada: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0080",
  "seed_hash": "7255843923ba507868c715759aa3a843c9b3e9dc53006da6071d8086cb30e756",
  "family_id": "F008",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_10",
  "titulo": "Taza olvidada: el cuidado que necesitó permiso",
  "semilla": "Mamá recalienta tres veces su bebida. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "mamá recalienta tres veces su bebida. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "taza olvidada",
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
  "replaces_seed_id": "MILO-S0080",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "servírsela a tiempo es una forma de verla",
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
      "hook": "Entrada posible desde taza olvidada y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "mamá recalienta tres veces su bebida. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá recalienta tres veces su bebida. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "taza olvidada",
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

# MILO-R0081 — Silla de cocina: el gesto que llegó a la persona equivocada

```json
{
  "seed_id": "MILO-R0081",
  "seed_hash": "29bd29ee4220a1d2336bb7e22d488d8d0cf0eb880b94ca2f95db291609f065ec",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_1",
  "titulo": "Silla de cocina: el gesto que llegó a la persona equivocada",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "conflicto": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0081",
  "cambio_causal": "Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Atribución equivocada → agradecimiento mal dirigido → reacción visible → pregunta → reconocimiento corregido.",
      "revelacion": "El reconocimiento puede incluir a quien quedó fuera de la primera explicación.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo atribuye la acción a la persona equivocada y le agradece delante de quien realmente la realizó. Al ver la reacción, pregunta quién participó en lugar de insistir en su versión.",
      "objeto": "silla de cocina",
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

# MILO-R0082 — Silla de cocina: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0082",
  "seed_hash": "bc8356a4d6b0c517b6cdc9fdb956e84e275056d3b1018815374cca775d8c3de2",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_2",
  "titulo": "Silla de cocina: la copia que no funcionó",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0082",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "silla de cocina",
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

# MILO-R0083 — Silla de cocina: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0083",
  "seed_hash": "bcb2647e8f3e34d99c6cc43fb4f2f47ab6a95682ef3d02942810d6f7f7a6c068",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_3",
  "titulo": "Silla de cocina: el favor convertido en deuda",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0083",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "silla de cocina",
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

# MILO-R0084 — Silla de cocina: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0084",
  "seed_hash": "d765b023c5e1c813da130a0dcddc5370036cd8cf3799a3d602b4a09e39c54475",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_4",
  "titulo": "Silla de cocina: dos personas, dos necesidades",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0084",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "silla de cocina",
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

# MILO-R0085 — Silla de cocina: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0085",
  "seed_hash": "28d2ca9031e3e4005f7b02047f1c126c5364a20b4db0d2d045798a03afa19f74",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_5",
  "titulo": "Silla de cocina: el acuerdo que nadie había entendido",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0085",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "silla de cocina",
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

# MILO-R0086 — Silla de cocina: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0086",
  "seed_hash": "e3a87283d6ae73bad181b4642f6a61ae182fdbdfcc2330f36337da4b434592ca",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_6",
  "titulo": "Silla de cocina: la ayuda que cambió algo querido",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0086",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "silla de cocina",
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

# MILO-R0087 — Silla de cocina: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0087",
  "seed_hash": "118a484a4fa3dfab2f34d355039763b3862905268b62c31e205db1ef56cdb0ac",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_7",
  "titulo": "Silla de cocina: la pregunta que no quería hacer",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0087",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "silla de cocina",
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

# MILO-R0088 — Silla de cocina: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0088",
  "seed_hash": "82f91c68affc047f83eb2598635fb9fcb01a3336300514dcc42ee54dacd2ed08",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_8",
  "titulo": "Silla de cocina: el recuerdo que tenían distinto",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0088",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "silla de cocina",
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

# MILO-R0089 — Silla de cocina: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0089",
  "seed_hash": "6b624af588f5f56b335ee487d2307e406f1b77ba5b8646149e63f8f287c8ec54",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_9",
  "titulo": "Silla de cocina: el agradecimiento dicho demasiado tarde",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0089",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "silla de cocina",
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

# MILO-R0090 — Silla de cocina: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0090",
  "seed_hash": "f9a05521abc11d0d836137b682e5117fc94aff776aab6febaf3dc9f1e1e32859",
  "family_id": "F009",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_10",
  "titulo": "Silla de cocina: el cuidado que necesitó permiso",
  "semilla": "Mamá escucha a todos sin ocupar su propia silla. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "mamá escucha a todos sin ocupar su propia silla. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "silla de cocina",
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
  "replaces_seed_id": "MILO-S0090",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "nadie le había dejado un momento para sentarse",
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
      "hook": "Entrada posible desde silla de cocina y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "mamá escucha a todos sin ocupar su propia silla. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá escucha a todos sin ocupar su propia silla. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "silla de cocina",
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

# MILO-S0091 — Canasta de ropa: la primera vez

```json
{
  "seed_id": "MILO-S0091",
  "seed_hash": "9f3a2477659dd2dd07b6b1830433463d48733c94f8dc6b0d3e9d7bdb07632a7d",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "primera_vez",
  "titulo": "Canasta de ropa: la primera vez",
  "semilla": "Mamá deja una canasta sin doblar. Milo interpreta el desorden como descuido. Tratamiento: Milo observa por primera vez la situación y debe comprobar su interpretación antes de actuar.",
  "conflicto": "Milo interpreta el desorden como descuido",
  "accion_visible": "mamá deja una canasta sin doblar",
  "objeto_emocional": "canasta de ropa",
  "giro_posible": "compartir la tarea libera una conversación",
  "desarrollo_requerido": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
  "milo_role": "adulto; recuerdo infantil solo si el guion lo justifica",
  "personajes_requeridos": [
    "Milo",
    "mamá"
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
      "reconocimiento": "Milo interpreta el desorden como descuido",
      "conflicto": "Milo interpreta el desorden como descuido",
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Mostrar situación → lectura inicial → detalle que contradice → pregunta o gesto concreto.",
      "revelacion": "compartir la tarea libera una conversación",
      "visual": "mamá deja una canasta sin doblar",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar",
      "objeto": "canasta de ropa",
      "reinterpretacion": "compartir la tarea libera una conversación",
      "tono": "Relación cotidiana y gesto contenido; no promesa clínica.",
      "visual": "Situación doméstica compatible con estilo ilustrado; referencias individuales pendientes.",
      "representacion": "Milo interpreta el desorden como descuido"
    },
    "comparacion_novedad": "Comparación de estructura causal con familia y banco; no embeddings ni corpus audiovisual bruto.",
    "confianza": "media",
    "metodo": "Juicio editorial asistido por modelo a nivel de familia y estructura; aritmética programática. No evaluación independiente ni predicción estadística."
  }
}
```

# MILO-R0092 — Canasta de ropa: la copia que no funcionó

```json
{
  "seed_id": "MILO-R0092",
  "seed_hash": "3a826de627aa516fcf1d7fa647f698bf18019fa92af5d81347179bca5345b9cd",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_2",
  "titulo": "Canasta de ropa: la copia que no funcionó",
  "semilla": "Mamá deja una canasta sin doblar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "conflicto": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0092",
  "cambio_causal": "Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Modelo observado → intento imperfecto → ocultamiento breve → petición de ayuda → tarea compartida.",
      "revelacion": "Comprender el gesto incluye poder aprender sin fingir que ya sabe hacerlo.",
      "visual": "mamá deja una canasta sin doblar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo intenta repetir la acción para demostrar que ya entendió, pero su intento falla. Esconde el resultado un momento y después lo muestra para pedir ayuda.",
      "objeto": "canasta de ropa",
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

# MILO-R0093 — Canasta de ropa: el favor convertido en deuda

```json
{
  "seed_id": "MILO-R0093",
  "seed_hash": "437ef2ff74c4d58c325121d3486465d62b95f7c2948984bf6640a3ad4e2ec318",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_3",
  "titulo": "Canasta de ropa: el favor convertido en deuda",
  "semilla": "Mamá deja una canasta sin doblar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "conflicto": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0093",
  "cambio_causal": "Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Gesto recibido → promesa excesiva → tarea sin terminar → conversación → acuerdo limitado y concreto.",
      "revelacion": "Agradecer un gesto no exige prometer una disponibilidad que no puede cumplir.",
      "visual": "mamá deja una canasta sin doblar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo recibe el gesto y comienza a aceptar encargos que no puede sostener por sentirse en deuda. Cuando deja una tarea a medias, reconoce lo ocurrido y acuerda qué puede ofrecer.",
      "objeto": "canasta de ropa",
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

# MILO-R0094 — Canasta de ropa: dos personas, dos necesidades

```json
{
  "seed_id": "MILO-R0094",
  "seed_hash": "075d3b2d67d5b5993b8de1583e3db6cc624e86950f744e137caeb5b18914d1ba",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_4",
  "titulo": "Canasta de ropa: dos personas, dos necesidades",
  "semilla": "Mamá deja una canasta sin doblar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "conflicto": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0094",
  "cambio_causal": "Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Respuesta uniforme → aceptación y rechazo → incomodidad → pedidos diferentes → dos acciones ajustadas.",
      "revelacion": "Una misma intención puede requerir dos formas distintas de cuidado.",
      "visual": "mamá deja una canasta sin doblar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo prepara la misma respuesta para dos familiares presentes; uno la acepta y el otro dice que necesita algo distinto. Milo se siente rechazado y luego escucha ambos pedidos antes de actuar.",
      "objeto": "canasta de ropa",
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

# MILO-R0095 — Canasta de ropa: el acuerdo que nadie había entendido

```json
{
  "seed_id": "MILO-R0095",
  "seed_hash": "cf5876c6c2be2ba0075ec707ce00046f53638284155a35fe4cc40d1f21335fa7",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_5",
  "titulo": "Canasta de ropa: el acuerdo que nadie había entendido",
  "semilla": "Mamá deja una canasta sin doblar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "conflicto": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0095",
  "cambio_causal": "Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Acuerdo ambiguo → espera mutua → objeto pendiente → versiones contradictorias → nuevo acuerdo visible.",
      "revelacion": "Decir cuándo y quién hará cada parte evita convertir un malentendido en desinterés.",
      "visual": "mamá deja una canasta sin doblar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo cree que el familiar entendió un acuerdo relacionado con la escena, pero ambos esperan que el otro actúe. Ante el objeto sin atender, repiten lo acordado y descubren dos versiones diferentes.",
      "objeto": "canasta de ropa",
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

# MILO-R0096 — Canasta de ropa: la ayuda que cambió algo querido

```json
{
  "seed_id": "MILO-R0096",
  "seed_hash": "bbe77451c01a22b45d8390f2f7d531556c54454d8bfa089eacf681ee175a38bb",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_6",
  "titulo": "Canasta de ropa: la ayuda que cambió algo querido",
  "semilla": "Mamá deja una canasta sin doblar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "conflicto": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0096",
  "cambio_causal": "Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Intervención bien intencionada → detalle desplazado → desacuerdo → explicación → decisión compartida.",
      "revelacion": "Mejorar un espacio también requiere escuchar a quien lo usa.",
      "visual": "mamá deja una canasta sin doblar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo reorganiza el espacio alrededor del objeto para ayudar sin consultar. El familiar busca un detalle que ya no está en su lugar. Milo reconoce su intervención y ambos eligen qué devolver y qué cambiar.",
      "objeto": "canasta de ropa",
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

# MILO-R0097 — Canasta de ropa: la pregunta que no quería hacer

```json
{
  "seed_id": "MILO-R0097",
  "seed_hash": "387e638ec3ce6d92d729119803c9a90af78f0a894786fcdea176983e5967fddb",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_7",
  "titulo": "Canasta de ropa: la pregunta que no quería hacer",
  "semilla": "Mamá deja una canasta sin doblar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "conflicto": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0097",
  "cambio_causal": "Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Observación parcial → explicación anticipada → pregunta sobre objeto → hecho nuevo → ayuda concreta.",
      "revelacion": "Una pregunta verificable permite sustituir una suposición por una acción útil.",
      "visual": "mamá deja una canasta sin doblar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo observa la escena desde el pasillo y ensaya una explicación. Al entrar, pregunta por un detalle concreto; el familiar responde con un hecho que Milo no había visto y le muestra la parte pendiente.",
      "objeto": "canasta de ropa",
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

# MILO-R0098 — Canasta de ropa: el recuerdo que tenían distinto

```json
{
  "seed_id": "MILO-R0098",
  "seed_hash": "19f319690aa3ac3c999e15d336525bbb6daa13e894b285649331576ed5b08e78",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_8",
  "titulo": "Canasta de ropa: el recuerdo que tenían distinto",
  "semilla": "Mamá deja una canasta sin doblar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "conflicto": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "accion_visible": "mamá deja una canasta sin doblar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0098",
  "cambio_causal": "El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Objeto presente → recuerdos diferentes → desacuerdo → evidencia disponible → reconocimiento de incertidumbre.",
      "revelacion": "Compartir recuerdos no obliga a imponer una única versión ni a inventar certezas.",
      "visual": "mamá deja una canasta sin doblar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. El objeto abre una conversación sobre una escena anterior. Milo y un familiar recuerdan decisiones distintas; buscan una foto o una marca material disponible y admiten lo que no pueden comprobar.",
      "objeto": "canasta de ropa",
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

# MILO-R0099 — Canasta de ropa: el agradecimiento dicho demasiado tarde

```json
{
  "seed_id": "MILO-R0099",
  "seed_hash": "e7dfc31e959f0e09917debca3386e4eb75fa569a93027058fe1aae2c8a74526b",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_9",
  "titulo": "Canasta de ropa: el agradecimiento dicho demasiado tarde",
  "semilla": "Mamá deja una canasta sin doblar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "conflicto": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0099",
  "cambio_causal": "Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Preparación de discurso → aplazamiento → visita termina → agradecimiento específico → respuesta contenida.",
      "revelacion": "Una frase concreta durante el encuentro puede acercar más que un discurso siempre pendiente.",
      "visual": "mamá deja una canasta sin doblar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo prepara una frase larga sobre el gesto pero sigue posponiendo decirla. El familiar comienza a recoger para terminar la visita; Milo deja el discurso a un lado y nombra una ayuda específica antes de despedirse.",
      "objeto": "canasta de ropa",
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

# MILO-R0100 — Canasta de ropa: el cuidado que necesitó permiso

```json
{
  "seed_id": "MILO-R0100",
  "seed_hash": "cefaa593c6303e3beafa594446d869d78c18f840cba62893918c2acdc66e3f11",
  "family_id": "F010",
  "territorio": "Madre y carga",
  "angulo": "arco_causal_10",
  "titulo": "Canasta de ropa: el cuidado que necesitó permiso",
  "semilla": "Mamá deja una canasta sin doblar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "conflicto": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "accion_visible": "mamá deja una canasta sin doblar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "objeto_emocional": "canasta de ropa",
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
  "replaces_seed_id": "MILO-S0100",
  "cambio_causal": "Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
  "giro_base_descartado": "compartir la tarea libera una conversación",
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
      "hook": "Entrada posible desde canasta de ropa y el desacuerdo descrito; hook aún no escrito.",
      "progresion": "Impulso de resolver → señal de incomodidad → detención → permiso o alternativa → acción respetuosa.",
      "revelacion": "Detenerse a preguntar puede cuidar tanto como intervenir.",
      "visual": "mamá deja una canasta sin doblar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "compartibilidad": "Reconocimiento de Madre y carga; destinatario todavía debe concretarse en guion."
    },
    "evidencia_afinidad": {
      "territorio": "Madre y carga",
      "conducta": "mamá deja una canasta sin doblar. Milo decide resolver la escena por su cuenta. Antes de tocar el objeto nota que el familiar retira la mano y se detiene para preguntar; recibe una preferencia concreta y ajusta su acción.",
      "objeto": "canasta de ropa",
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
