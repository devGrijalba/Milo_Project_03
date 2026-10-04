# CHROME_CDP_INJECTION_PROTOCOL (v028 — único, canónico)

Chrome (`--remote-debugging-port`, mismo `user-data-dir` siempre) es infraestructura crítica de Milo, no herramienta auxiliar. Toda automatización — panel LLM o Flow — usa este protocolo y su recuperación. Nada de implementaciones paralelas.

## 1. Conexión / reconexión

Conectar por CDP; si `ECONNREFUSED`, relanzar Chrome con el mismo `user-data-dir` y reintentar. JAMÁS `browser.close()` sobre el Chrome compartido (mata todas las pestañas); cerrar solo las pages abiertas por el worker.

## 2. Descubrimiento e identificación

Localizar la pestaña por substring de URL. La IDENTIDAD del modelo la da la pestaña que produjo la respuesta, nunca la etiqueta `MODELO:` que el modelo escriba (etiqueta errónea = defecto formal menor, no exclusión).

## 3. Contrato de inyección verificada — `inject(page, text)`

Única función de inyección para ChatGPT, Gemini, Grok, DeepSeek y el composer de Flow. Ningún paso se asume: cada uno se verifica.

1. Resolver el composer: el `textarea` / `[contenteditable]` visible más bajo en viewport, no readonly/disabled.
2. `focus()` + llenado (setter de prototipo + evento `input`, o `execCommand insertText` en contenteditables).
3. LEER DE VUELTA el valor realmente presente en el composer y compararlo con el texto enviado (igualdad, no proxy de longitud): master >1000 chars, envíos cortos >200. Si no coincide → abortar el envío y reintentar SOLO ese destino. `type()` que no deja valor es fallo, no envío.
4. Pausa humana 8–15 s (chats LLM) o ~1 s escalonado (prompts Flow entre workers).
5. Envío: `Enter` de teclado real por CDP (en chats React el typing/Enter sintético no entra — teclado Playwright).
6. Envío verificado: el composer debe vaciarse (<20 chars) Y la página debe avanzar de estado (nuevo mensaje / generación en curso). Input vacío sin avance = envío fallido.

## 4. Detección de respuesta (a prueba de eco)

El mensaje inyectado contiene los mismos marcadores que se sondean (EN ESPERA, PLANO, JSON de voz), así que la presencia de marcadores NUNCA es DONE. DONE = crecimiento real sobre la base registrada al enviar + contenido genuino (FASE 1: línea `HOOK:` no-placeholder; FASE 2: `PLANO 01`; Flow: ausencia de `%` dos sondeos seguidos), confirmado por lectura estable posterior. Umbrales de crecimiento por modelo (un respondedor compacto termina muy por debajo del umbral de uno verboso). Sondeo ~2 s por modelo; extracción inmediata a disco + aviso en el acto (los avisos de fin de proceso no sirven para seguimiento por modelo). STALL = sin actividad a los 5 min → verificar entrega antes de esperar más.

## 5. Continuidad de pestaña

`goto`/recargar una pestaña con conversación la mata y el prompt se pierde. FASE 2 siempre en la MISMA pestaña de FASE 1; pestaña nueva recibe el MASTER primero, jamás la ganadora sola. Rondas frescas usan pestañas nuevas; las extracciones en disco sobreviven a la muerte de Chrome y abaratan la reconstrucción (reenvío master-first).

## 6. Recuperación de Chrome completo

Si Chrome muere: relanzar con el mismo `user-data-dir`, reconstruir cada conversación inyectando primero el MASTER, continuar aprovechando las respuestas ya guardadas en disco. Prohibido `browser.close()` (ver §1).

## 7. LLM_RECOVERY_ESCALATION (única recuperación, reemplaza al "preguntar al panel" informal)

Tras ≥3 fallos en el mismo paso CDP (mismo error, loops de duplicados, selectores que fallan, topes de reintento):

1. PAUSAR el loop (prohibido depurar en bucle eterno; tope 3 intentos por archivo/paso). Ante pestaña con estado degradado (grilla vacía que en otra pestaña sí muestra datos, visor que no abre, srcs rotando), NO depurar el estado: cerrar, abrir página fresca y regenerar/reintentar ahí.
2. Crear INCIDENT_PACKET: qué se intentaba, evidencia (mensajes de error, DOM observado, lo ya probado).
3. Inyectarlo al panel LLM como pregunta técnica autocontenida (sin contexto de episodio).
4. Sintetizar las respuestas en UNA solución, probarla, verificarla.
5. Registrarla en los cuatro lugares (skill canónica, copia espejo en `docs/skills/` del repo, `docs/WORKFLOW.md`, entrada fechada en `docs/CHANGELOG_vNNN.md`) y continuar.

Flow reutiliza ESTA recuperación — no tiene regla propia.
