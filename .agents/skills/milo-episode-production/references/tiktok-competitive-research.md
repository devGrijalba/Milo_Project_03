# TikTok competitive research — referentes de storytelling emocional

Pipeline validado para investigar cuentas/nichos de referencia en TikTok (hooks, estructuras, duraciones, engagement) y usar los hallazgos como insumo del performance loop (§5 de milo-story-performance-loop). Ejecutado y verificado sobre el nicho relatos/reflexiones; el procedimiento es genérico.

## 1. Pipeline (CDP sobre Chrome con `--remote-debugging-port=9222`)

1. **Búsqueda**: con la pestaña de resultados de búsqueda de TikTok abierta, extraer tarjetas vía `Runtime.evaluate`: `document.querySelectorAll('a[href*="/video/"]')`, dedupe por ID del href, y guardar `{id, ctx}` con el `innerText` del contenedor (trae plays/likes visibles). Persistir `tiktok_search.json`.
2. **Metadatos por video**: navegar la MISMA pestaña a `https://www.tiktok.com/@x/video/<id>` y leer el JSON hidratado `__UNIVERSAL_DATA_FOR_REHYDRATION__`. Extraer: `author.uniqueId`, `desc`, `stats` (playCount/diggCount/commentCount/shareCount), `video.duration` y `video.subtitleInfos` (URLs de subtítulos). Persistir `tiktok_videos.json`.
3. **Transcripciones**: de `subtitleInfos` tomar la entrada con `Format == 'webvtt'` y descargarla con curl + header `Referer: https://www.tiktok.com/`. Son transcripciones reales con timestamps — mejor que whisper para benchmarking. Persistir `tt_subs/<id>.vtt` y consolidar en `tt_transcripts.json` (`{t, txt}` por cue).
4. **Métrica**: engagement = (likes + 3·comentarios + 5·shares) / plays. Comentarista intensivo (series episódicas) dispara el término de comentarios 10x.

## 2. Pitfalls (ambos costaron un ciclo de depuración)

- **La clave del JSON es `'webapp.video-detail'` (minúsculas)**, no `webapp.video-detail`-con-mayúsculas del patrón Next.js clásico: buscar la clave con `Object.keys(scope).find(k => k.toLowerCase().includes('video-detail'))` en vez de una clave hardcodeada, porque TikTok renombra el scope sin aviso.
- **Polling, nunca sleep fijo tras `Page.navigate`**: TikTok hidrata el JSON asincrónicamente; un `time.sleep(7)` fijo lee la página a medio hidratar (`nojson`/`noitem` falsos). Sondear cada ~3s hasta 45s evaluando el JS y avanzando solo cuando el item existe.
- El endpoint `/@x/video/<id>` con usuario placeholder funciona para metadatos; para comentarios hace falta navegar al video real (pendiente de implementar).
- VTT parse: los cues son líneas alternadas `timestamp` → `texto`; filtrar líneas vacías y convertir a segundos.

## 3. Hallazgos del nicho (muestra de 5 referentes, engagement 7.7–14.9%)

Reglas destiladas que validan/ajustan el motor narrativo de MILO — ver `TT_STORYTELLING_INVESTIGACION.md` en `D:/hermes/MILO/reloj_pkg/` para la muestra completa.

- **Hook emocional directo en 0–2s**: pregunta dolorosa universal ('¿Cuál ha sido el momento más duro de tu vida?' a los 0.8s) o apelación en segunda persona ('A mi abuelo… te busco en el silencio' a los 1.1s). Nunca contexto primero. Confirma el umbral HOOK ≤1s / cambio <5s del §7 del performance loop.
- **El objeto concreto es el ancla emocional**: los top usan un objeto/situación tangible como vehículo (maleta marrón, tres papas, manos marcadas). Primero imagen material, después reflexión — coincide con la REGLA DEL OBJETO PROTAGONISTA.
- **Dos formatos viables con engagement opuesto**: micro monólogo/testimonio de 31–60s (engagement ~15%, ideal para compartir) vs episódico narrado de 3–5.5min con capítulos (engagement 7.7–14.2% pero ~10x comentarios por play, ideal para seguidores). Elegir por objetivo: compartir vs conversión a seguidor.
- **Estructura del monólogo ganador (60s)**: apelación directa (0–2s) → evocación sensorial → recuerdo concreto compartido → arrepentimiento ('nunca te dije… pensé que habría más tiempo') → cierre espiritual sin CTA explícito (el CTA es compartir el propio duelo).
- **Estructura del testimonio ganador (31s)**: cadena de preguntas del entrevistador, respuestas crudas sin pulir — la imperfección del habla ES la credibilidad.
- **El formato episódico retiene con un giro cada ~30s** ('pero no fuiste', 'su abuelo estaba solo') y genera la mayor conversación por play.
