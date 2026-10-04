# PROTOCOLO OBLIGATORIO DE QC AUDIOVISUAL Y RETENCIÓN

Este protocolo se ejecuta AUTOMÁTICAMENTE antes de aprobar cualquier MASTER FINAL, render o versión destinada a Facebook Reels, YouTube Shorts u otra plataforma vertical.

Ningún video puede considerarse FINAL hasta superar esta auditoría.

## 1. REGLA GENERAL

El sistema no debe limitarse a comprobar que:

- el guion esté correcto;
- el audio esté presente;
- las escenas hayan sido generadas;
- los subtítulos existan;
- el video pueda reproducirse.

Debe evaluar activamente si la pieza tiene suficiente capacidad de RETENCIÓN.

El criterio principal es:

¿Existe algún momento donde un espectador pueda aburrirse, dejar de mirar, dejar de leer o anticipar demasiado fácilmente lo que viene?

Si la respuesta es SÍ, se debe corregir antes de exportar.

## 2. AUDITORÍA DE APERTURA — 0.00 A 5.00 S

Los primeros 5 segundos son un gate duro independiente. Evaluar el RENDER REAL, no solo el guion.

### 2.1 FIRST SECOND — 0.00 A 1.00 S
Conflicto, promesa, consecuencia o contradicción perceptible; Milo/objeto/acción reconocibles; cero introducción prescindible.

### 2.2 OPEN LOOP — antes de 3.00 S
Debe existir una pregunta mental simple implícita que obligue a continuar.

### 2.3 PROGRESIÓN — antes de 5.00 S
Nueva información, consecuencia, complicación o cambio de estado. Repetición visual, microzoom o movimiento cosmético no cuentan.

### 2.4 EARLY_RETENTION_SCORE
FIRST_FRAME 20 + CLARIDAD 15 + CURIOSIDAD 20 + CONTRADICCIÓN 15 + PROGRESIÓN_0_5 20 + CAMBIO_VISUAL 10. PASS ≥90. VIRALITY no compensa este gate.

### 2.5 AUTOCORRECCIÓN
Fallo visual: corregir 0–5 s, regenerar solo assets afectados, recalcular mapas/timecodes si aplica, re-renderizar y reauditar. Fallo estructural de guion ya congelado: EARLY_RETENTION_SCRIPT_FAIL → invalidar ganador → volver automáticamente a FASE 1. No alterar silenciosamente el guion congelado ni pedir microdecisiones.

Prohibido PASS_WITH_OBSERVATION.

## 3. CONTROL DE SILENCIOS Y ESPACIOS MUERTOS

Analizar toda la pista de voz.

Detectar silencios entre frases.

Regla orientativa. Silencios de:

- 0.00–0.35 s → normales;
- 0.35–0.60 s → revisar;
- 0.60–0.80 s → conservar solo si tienen intención;
- >0.80 s → deben justificarse explícitamente como pausa cómica, dramática o de payoff.

No acumular pausas largas repetidamente.

La duración final debe provenir del ritmo natural de la historia y no de espacios vacíos.

Cuando sea posible: recortar silencios antes que acelerar artificialmente la voz.

No destruir pausas que sean esenciales para un remate.

## 4. DENSIDAD DE ESTÍMULO VISUAL

El video no debe permanecer demasiado tiempo con una composición visual prácticamente idéntica.

Revisar ventanas consecutivas de aproximadamente 2–4 segundos.

Preguntar: ¿Cambió algo visualmente significativo?

Puede cambiar: expresión; pose; escala; encuadre; cámara; objeto; acción; dirección corporal; profundidad; composición; interacción con el entorno.

No es obligatorio cambiar de escena continuamente. Se busca: microvariación visual controlada.

Evitar: edición hiperactiva; efectos sin motivación; memes insertados arbitrariamente; imágenes aleatorias; zooms constantes; transiciones llamativas sin razón narrativa.

La identidad Milo debe seguir siendo limpia y reconocible.

## 5. PUNTOS DE RENOVACIÓN VISUAL

En historias de aproximadamente 20–35 segundos, identificar al menos: Hook visual. Primer cambio de situación. Punto de escalada. Punto previo al payoff. Remate.

En una pieza de ~25–30 segundos debe existir normalmente un cambio visual significativo aproximadamente cada 3–5 segundos.

No se requiere corte completo. Puede ser simplemente: plano medio → close-up; personaje → objeto; objeto → personaje; cámara estable → pequeño push-in; expresión neutra → reacción.

## 6. PROTOCOLO DE SUBTÍTULOS

Los subtítulos son parte de la narrativa, no un elemento accesorio. Deben auditarse VISUALMENTE después de renderizar.

### 6.1 Legibilidad

Comprobar en simulación de pantalla móvil: tamaño suficiente; peso tipográfico suficiente; contraste; separación del fondo; contorno o sombra cuando sea necesaria; ausencia de elementos que interfieran detrás.

Si el texto requiere esfuerzo consciente para leerse: FAIL.

### 6.2 Cantidad de texto

Evitar mostrar párrafos o frases excesivamente largas de una sola vez. Preferir unidades semánticas cortas.

Ejemplo — NO: "Volví treinta segundos después, por si el universo había actualizado el inventario."

PREFERIBLE: "Volví treinta segundos después…" después: "por si el universo había actualizado el inventario."

### 6.3 Beats narrativos

Los subtítulos deben respetar la estructura oral. Frases importantes pueden aparecer aisladas.

Ejemplo: "A la tercera visita…" "ya no buscaba comida." "Buscaba una explicación."

Una línea de alto impacto no debe quedar enterrada dentro de un bloque grande.

### 6.4 Sincronización

Cada subtítulo debe: entrar junto con la frase hablada; desaparecer al finalizar su unidad de significado; no adelantarse demasiado; no permanecer después de que la idea terminó; no competir con la siguiente frase.

Sincronización objetivo: sensación de correspondencia inmediata voz ↔ texto.

## 7. POSICIÓN DE SUBTÍTULOS

No colocar automáticamente los subtítulos siempre en el mismo punto. Evaluar composición de cada escena.

Objetivos: evitar interfaces de Facebook/YouTube; no tapar rostro; no tapar acción importante; mantener cercanía visual con el sujeto; reducir viajes excesivos de los ojos.

Preferencia general: tercio superior/intermedio con adaptación contextual, manteniendo safe zones. Evitar pegarlos innecesariamente al borde superior.

## 8. SAFE ZONES

Antes de exportar verificar que: ningún texto importante quede demasiado cerca de bordes; subtítulos no interfieran con botones laterales; CTA, si existe, no quede tapado; elementos clave no estén en las zonas inferiores ocupadas por UI; la cara del personaje permanezca libre.

La composición debe funcionar pensando primero en teléfono móvil.

## 9. JERARQUÍA DE FRASES

Identificar automáticamente: HOOK; ESCALADA; GIRO; FRASE MÁS DIVERTIDA; PAYOFF; FRASE FINAL.

Estas frases no tienen obligación de recibir efectos llamativos, pero sí deben tener una jerarquía perceptible mediante: aislamiento; timing; pausa; tamaño; corte; reacción; composición; cambio de plano.

## 10. PROTECCIÓN DEL PAYOFF

El remate final debe recibir atención especial.

Comprobar: que no llegue demasiado rápido; que no esté rodeado de texto innecesario; que tenga imagen coherente; que el último beat visual acompañe el chiste; que exista suficiente espacio temporal para procesarlo; que el video no termine antes de que el cerebro complete el remate.

Cuando una frase final sea el punchline principal: preferir presentarla sola.

Después del punchline puede existir una micro pausa de procesamiento si mejora la comedia.

## 11. CONTROL DE MONOTONÍA

Antes de aprobar, visualizar el video SIN AUDIO. Preguntar: ¿Seguiría ocurriendo algo visualmente comprensible? Si durante varios segundos consecutivos la respuesta es NO: revisar composición o movimiento.

Después visualizarlo SOLO CON AUDIO. Preguntar: ¿La historia sigue funcionando perfectamente sin las imágenes? Si ambas capas funcionan independientemente y juntas se potencian: PASS.

## 12. CONTROL DE SUBTÍTULOS SIN AUDIO

Ver el video completamente silenciado. Debe ser posible: seguir la historia; entender las frases; leer cómodamente; identificar el remate. Esto es crítico porque parte del público de Facebook puede comenzar la reproducción sin sonido. Si la historia pierde sentido únicamente por depender del audio: FAIL.

## 13. CONTROL DE AUDIO

Revisar: claridad de voz; ausencia de clipping; ruido; respiraciones molestas; saltos audibles entre cortes; volumen consistente; silencios excesivos; inteligibilidad desde altavoz de teléfono.

Objetivo aproximado de loudness para master social: -14 a -17 LUFS integrados. True Peak recomendado: ≤ -1 dBTP. No normalizar agresivamente si deteriora la voz.

## 14. DURACIÓN

No existe una duración obligatoria. La regla es: el video debe durar exactamente lo que necesita la historia y nada más.

Después del primer render comprobar: ¿Se pueden eliminar 1–3 segundos sin perder comprensión, timing o comedia? Si SÍ: hacer una versión más ajustada. No acelerar la voz solo para reducir duración.

## 15. AUDITORÍA DE RETENCIÓN SIMULADA

Antes de aprobar el MASTER FINAL, revisar cronológicamente:

- 0–1.5 s: ¿Detiene scroll?
- 1.5–5 s: ¿Se entiende rápidamente la situación?
- 5–10 s: ¿Existe progresión?
- 10–15 s: ¿La historia sigue escalando?
- 15–20 s: ¿Existe renovación visual o narrativa?
- 20 s → final: ¿Se está construyendo claramente hacia un payoff?
- Últimos 2–3 s: ¿El remate recibe suficiente atención?

Cualquier tramo débil debe corregirse antes de exportar.

## 16. SIMULACIÓN DE ABANDONO

Identificar internamente el segundo más probable de abandono. Responder internamente: "Si tuviera que dejar este video en un punto, ¿en cuál sería?" Luego analizar por qué: pausa; monotonía; exceso de explicación; falta de cambio visual; subtítulo largo; baja legibilidad; acción repetida; payoff demasiado predecible. Corregir ese tramo.

## 17. PROTECCIÓN CONTRA SOBREEDICIÓN

La optimización de retención NO autoriza convertir Milo en contenido visualmente caótico.

Evitar: zooms en cada palabra; múltiples sonidos virales; emojis constantes; stickers; flashes; memes; cortes cada 0.5 segundos; textos enormes arbitrarios; movimientos sin lógica.

La edición debe sentirse: simple + precisa + intencional.

## 18. INSPECCIÓN DEL RENDER REAL

No aprobar únicamente a partir del timeline, código o configuración. Después de renderizar: abrir el archivo final; revisar frame real; revisar primeros 3 segundos; revisar subtítulos; revisar sincronización; revisar zonas seguras; revisar tramo medio; revisar payoff; revisar últimos frames; comprobar audio real. El archivo renderizado es la única fuente final de verdad.

## 19. CHECKLIST FINAL OBLIGATORIO

Antes de marcar FINAL_APPROVED = TRUE deben cumplirse todos:

- [ ] Hook visual fuerte en 0–1.5 s
- [ ] Situación comprensible inmediatamente
- [ ] Sin silencios accidentales largos
- [ ] Ritmo sostenido
- [ ] No existe monotonía visual prolongada
- [ ] Cambios visuales suficientes
- [ ] Subtítulos grandes y legibles en móvil
- [ ] Contraste adecuado
- [ ] Texto correctamente fragmentado
- [ ] Sin bloques excesivamente largos
- [ ] Sin errores ortográficos
- [ ] Sin errores gramaticales
- [ ] Sin palabras cortadas incorrectamente
- [ ] Sin texto tapando rostro/acción
- [ ] Safe zones correctas
- [ ] Sincronía voz-subtítulo correcta
- [ ] Frases clave tienen jerarquía
- [ ] Payoff visualmente protegido
- [ ] Remate tiene tiempo para procesarse
- [ ] Audio limpio
- [ ] Volumen consistente
- [ ] Video funciona sin audio
- [ ] Video funciona auditivamente sin imagen
- [ ] No existe sobreedición
- [ ] No hay frames accidentales o glitches
- [ ] Duración ajustada
- [ ] Render final revisado físicamente

Si cualquier punto crítico falla: FINAL_APPROVED = FALSE. Corregir y volver a renderizar.

## 20. REGLA DE NO CONFORMIDAD

Está PROHIBIDO entregar un video como MASTER FINAL diciendo simplemente: "render completado"; "QC PASS"; "sin errores técnicos".

El QC debe evaluar simultáneamente: TÉCNICA (resolución, fps, codec, audio, integridad). LINGÜÍSTICA (ortografía, gramática, subtítulos). VISUAL (composición, legibilidad, continuidad). NARRATIVA (hook, escalada, ritmo, payoff). RETENCIÓN (posibles puntos de abandono). PLATAFORMA (visualización móvil y safe zones).

Solamente si las seis categorías aprueban se permite: MASTER_QC = PASS.

## 21. REPORTE FINAL DE QC

Cada video terminado debe generar un reporte mínimo:

MASTER_QC: PASS / FAIL
HOOK: PASS / FAIL
RITMO: PASS / FAIL
VISUAL: PASS / FAIL
SUBTÍTULOS: PASS / FAIL
ORTOGRAFÍA: PASS / FAIL
AUDIO: PASS / FAIL
PAYOFF: PASS / FAIL
SAFE_ZONES: PASS / FAIL
MOBILE_READABILITY: PASS / FAIL
RETENTION_RISK: BAJO / MEDIO / ALTO

DURACIÓN FINAL:
FPS:
RESOLUCIÓN:
LUFS:
TRUE PEAK:

PUNTO MÁS DÉBIL DETECTADO:
CORRECCIÓN REALIZADA:
SEGUNDO ESTIMADO DE MAYOR RIESGO DE ABANDONO:
MOTIVO:

Solo después de esta auditoría el video puede considerarse listo para publicación.

---

Filosofía permanente Milo:

GUION GANADOR + EJECUCIÓN VISUAL + SUBTÍTULOS + RITMO + PAYOFF = MASTER FINAL.

Si cualquiera de esos cinco falla, no hay QC PASS.

## 22. REGLAS DE ENDURECIMIENTO (revisiones sucesivas)

Límite de repetición visual: si durante más de 3–5 segundos predominan la misma composición, mismo personaje y mismo objeto sin cambio significativo, marcar VISUAL_VARIATION = FAIL.

Subtítulos con criterio móvil cuantificable: además de "legibles", exigir revisión real a escala de teléfono y marcar MOBILE_READABILITY = FAIL si el tamaño/peso obliga a esforzarse para leer.

Control de correcciones sucesivas: después de 2–3 iteraciones, entrar en modo POLISH_ONLY — solo se permiten ajustes pequeños de ritmo, subtítulos, escala o timing; queda prohibido rehacer guion o estilo si ya están aprobados.

STOP RULE: si GUION, IDENTIDAD, AUDIO, PAYOFF y COHERENCIA VISUAL están en PASS, las siguientes versiones solo pueden corregir fallos marcados específicamente por QC. No se permiten cambios creativos adicionales sin una razón medible.

## 23. ACTUALIZACIÓN DE CONSISTENCIA DE MASTER (serie)

Un master no se evalúa solo como video aislado: debe aprobar como parte de la serie MILO.

### Control de audio entre episodios

Target Milo: −16.5 LUFS integrados. Rango normal: −16 a −17. Máximo tolerable sin corrección obligatoria: −14 a −18. Fuera de −14..−18: LOUDNESS_QC = FAIL. True peak ≤ −1 dBTP, preferencia de serie −1 a −2.

### Consistencia entre episodios

Comparar cada master con al menos un episodio reciente aprobado: nivel de voz, loudness, tamaño/contorno/posición de subs, duración de lectura, densidad visual, velocidad narrativa. Sin saltos bruscos → SERIES_CONSISTENCY = PASS / FAIL.

### Regla de normalización

Audio válido pero fuera del baseline: PASS_WITH_LEVEL_OBSERVATION, corregir antes de exportar si aún es posible. No re-renderizar solo por diferencias menores si el master está completo y la voz es limpia y audible.

### Control de pausas

Clasificar cada silencio >0.60 s como NARRATIVE_PAUSE (prepara punchline, procesa reacción, incomodidad cómica, cambio de idea, protege final) o DEAD_AIR. Solo DEAD_AIR se recorta obligatoriamente. NO RECORTAR POR DURACIÓN.

### Control de variación visual

En ventanas de 3–5 s debe haber modificación perceptible (encuadre, expresión, pose, objeto, movimiento, escala, composición, acción). Pero un plano puede durar más si hay acción interna, cambio de expresión, tensión creciente, preparación de remate o repetición-chiste. STATIC_FRAME ≠ AUTOMATIC_FAIL: evaluar función narrativa.

### Control de hook

Separar HOOK_TEXT y HOOK_VISUAL; un verbal fuerte no compensa un visual débil. Ideal: ambos PASS.

### Control del final

Últimos 2–3 s independientes: ¿punchline terminó? ¿personaje reacciona? ¿espectador procesa? ¿corte apresurado? ¿pausa intencional? → ENDING_PROCESSING_TIME = PASS / FAIL.

### Control de master contra baseline

Comparar resolución, fps, volumen, subs, posición, contraste, ritmo, duración, complejidad visual. Sentirse misma serie ≠ ser idénticos.

### Reporte final extendido

Al §21 se agregan: LOUDNESS_TARGET · LOUDNESS_ACTUAL · TRUE_PEAK · AUDIO_SERIES_CONSISTENCY · SUBTITLE_TOP_MARGIN · SUBTITLE_SERIES_CONSISTENCY · HOOK_TEXT · HOOK_VISUAL · DEAD_AIR_DETECTED · NARRATIVE_PAUSES_DETECTED · ENDING_PROCESSING_TIME · SERIES_CONSISTENCY.

### Regla final

TECHNICAL_QC = PASS + SUBTITLE_QC = PASS + RETENTION_QC = PASS + SERIES_CONSISTENCY = PASS. Solo entonces: MASTER_QC = PASS.

## 24. MASTER FREEZE + VARIANTES EXPERIMENTALES

MASTER FREEZE RULE: una historia con SCRIPT_PASS + MASTER_QC_PASS queda congelada. Cualquier cambio posterior que altere hook, cuerpo, payoff o voz es una VARIANTE EXPERIMENTAL, nunca una corrección del master aprobado (nuevo slot/archivo, voz y render independientes; el master original se conserva como CONTROL).

Las recomendaciones de VIRAL_STORY_SCORE posteriores a un master aprobado no lo invalidan: se archivan como hipótesis A/B para futuras pruebas, con su propio brief y sin tocar el paquete congelado.
