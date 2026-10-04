# MILO_SUBTITLE_QC_V1 — Protocolo maestro de subtítulos (v2: margen superior + consistencia)

Obligatorio para todos los videos verticales de Milo (Facebook Reels, YouTube Shorts y similares).

Objetivo: máxima legibilidad en móvil; identidad visual consistente; buena retención; subtítulos limpios; correcta jerarquía narrativa; cero interferencia con rostro, acciones o interfaz de plataforma; consistencia visual entre episodios.

## 1. PRINCIPIO GENERAL

Los subtítulos deben ayudar a consumir el video más rápido. Nunca deben: distraer; competir con Milo; parecer publicidad genérica; verse infantiles; saturar visualmente; convertirse en el elemento principal de la escena.

Identidad: LIMPIA + CLARA + MODERNA + LEGIBLE + SUTIL.

## 2. COLOR PRINCIPAL

BLANCO como sistema principal. No usar automáticamente: amarillo, verde, rojo, azul, múltiples colores, degradados, colores palabra por palabra. Alternativos solo con razón narrativa concreta.

## 3. CONTRASTE

Texto blanco + contorno oscuro fino + sombra suave opcional. El contorno refuerza sin convertirse en línea negra gruesa: percibir primero el texto blanco, no el borde.

## 4. TAMAÑO

Evaluar en teléfono móvil. Para 1080×1920: lectura inmediata, resistente a compresión de Facebook, sin sentirse pequeño ni dominar la escena. Un subtítulo aprobado en episodio anterior sirve como referencia de escala para los siguientes.

## 5. AJUSTE DE TAMAÑO

Si se percibe ligeramente pequeño: +10–15% primero. Saltos ≥20% solo ante falla evidente.

## 6. PESO TIPOGRÁFICO

SEMIBOLD / BOLD MODERADO. Evitar Thin, Light, Extra Light, condensadas. Presencia tras compresión.

## 7. TIPOGRAFÍA

Sans serif, clara, moderna, compacta, legible. Consistente entre episodios. (Milo: Arial Bold.)

## 8. MÁXIMO DE LÍNEAS

2 líneas máximo; preferencia 1. Nunca párrafos.

## 9. LONGITUD DE BLOQUE

Unidades breves. NO: "Volví treinta segundos después, por si el universo había actualizado el inventario." PREFERIBLE: "Volví treinta segundos después…" + "por si el universo había actualizado el inventario."

## 10. FRAGMENTACIÓN SEMÁNTICA

Cortar por intención, respiración, ritmo, significado, pausa, remate — nunca por caracteres. Cada bloque = idea completa.

## 11. JERARQUÍA NARRATIVA

Identificar hook, setup, escalada, giro, frase importante, payoff, punchline. Las importantes pueden ir solas.

## 12. PAYOFF

Punchline final solo, con tiempo para leerse y procesarse.

## 13. POSICIÓN VERTICAL

Tercio superior-intermedio. Prohibido usar posición fija sin evaluar la escena.

## 13B. PLATFORM SAFE ZONE RULE (regla fija)

Para 1080×1920 los subtítulos viven preferentemente en mitad superior / centro-alto: centro del bloque entre Y ≈ 250 y Y ≈ 1050. No bajar de Y ≈ 1150–1200 ni invadir el último 15–20% derecho. El último 25–30% inferior no es posición habitual.

LOWER_SUBTITLE_POSITION = EXCEPTION, NOT DEFAULT. Toda excepción (p. ej. close-up con rostro arriba) requiere PLATFORM_UI_SAFE_ZONE_CHECK visual contra overlays de Facebook Reels y YouTube Shorts; si hay riesgo de superposición: SAFE_ZONE = FAIL. Antes una composición visible que una "bonita" tapada.

## 14. MARGEN SUPERIOR (regla nueva)

No pegar al borde superior. Para 1080×1920: respiración mínima ~150 px; objetivo 170–220 px desde el borde, salvo composición que exija otra ubicación. Si se percibe demasiado cercano al borde: TOP_MARGIN_QC = FAIL aunque siga dentro del frame.

## 15. RELACIÓN CON MILO

Texto relacionado con el área de acción; evitar recorridos de ojos innecesarios.

## 16. SAFE ZONES

Nunca donde UI cubra: extremo superior/inferior/derecho, descripción, botones, indicadores.

## 17. ROSTRO Y ACCIÓN

Prohibido tapar ojos, boca, rostro, manos importantes, objeto narrativo, acción principal. En conflicto: mover el texto.

## 18. SINCRONÍA

Entrar con la frase; sin adelantos/retrasos, sin permanecer tras la idea, sin pisar la siguiente.

## 19. DURACIÓN DE LECTURA

Suficiente para leer cómodamente; retirar al perder relevancia.

## 20. HOOK

Primer subtítulo rápido con la voz; nada de segundos iniciales sin texto si hay narración.

## 21. MAYÚSCULAS

Sentence case general; mayúsculas solo énfasis excepcional.

## 22. PALABRAS DESTACADAS

No colorear. Antes: timing, aislamiento, fragmentación, pausa, posición.

## 23. ANIMACIÓN

Mínima: aparición inmediata, fade rápido, corte limpio. Sin rebotes/zooms/karaoke.

## 24. FONDO DETRÁS DEL TEXTO

Sin cajas negras estándar. Antes: contorno, sombra, reposicionamiento.

## 25. REVISIÓN EN MÓVIL

A escala smartphone: ¿lectura inmediata? ¿esfuerzo? ¿demasiado arriba? ¿contorno ok? ¿compite con Milo? ¿fondo reduce contraste? Duda = MOBILE_READABILITY FAIL.

## 26. TEST SIN AUDIO

Silenciado: situación, progresión, historia, payoff comprensibles. Si no: SUBTITLE_QC FAIL.

## 27. TEST DE SCROLL

Sin concentración: si hay que detenerse a leer → corregir.

## 28. FACEBOOK

Tamaño ligeramente generoso, peso suficiente, blanco, contorno limpio, máx 2 líneas, lectura inmediata. Asumir compresión.

## 29. YOUTUBE SHORTS

Mismo sistema; revisar zona inferior/derecha por UI.

## 30. PROTECCIÓN DE IDENTIDAD

Nada TikTok genérico: ni multicolor, ni emojis, ni palabras enormes, ni estilos cambiantes, ni zoom por palabra.

## 31. CONSISTENCIA ENTRE EPISODIOS (regla nueva)

Un sub visual aprobado (tamaño, peso, contorno, sombra, separación, posición base) es baseline: mantenerlo salvo razón concreta. Medir SERIES_CONSISTENCY contra episodios recientes.

## 32. QC TÉCNICO

[ ] Ortografía · [ ] Gramática · [ ] Sin duplicadas/faltantes · [ ] Sin caracteres extraños · [ ] Sin cortes incorrectos · [ ] Máx 2 líneas · [ ] Longitud · [ ] Safe zone · [ ] Margen superior · [ ] Posición baja solo como excepción con UI check · [ ] Sin tapar rostro/acción · [ ] Sincronía · [ ] Tamaño · [ ] Peso · [ ] Contraste · [ ] Posición · [ ] Punchline aislado · [ ] Consistencia con anteriores.

## 33. QC VISUAL

Render real revisado físicamente. EL RENDER REAL ES LA FUENTE DE VERDAD.

## 34. ESTÁNDAR VISUAL MILO

Blanco · Semibold/Bold moderado · contorno fino + sombra opcional · 1 línea (máx 2) · tercio superior-intermedio contextual · margen superior 170–220 px · animación mínima · limpio/minimalista.

## 35. SISTEMA DE RESULTADO

SUBTITLE_QC: COLOR · SIZE · WEIGHT · CONTRAST · POSITION · TOP_MARGIN · LOWER_POSITION (DEFAULT top / EXCEPTION con UI check) · SAFE_ZONE · TIMING · SEGMENTATION · SPELLING · MOBILE_READABILITY · PAYOFF_HIERARCHY · SERIES_CONSISTENCY = PASS / FAIL. Todos los críticos en PASS.

## 37. ALINEACIÓN DE FRONTERAS CONTRA QC CON TOLERANCIA

Cuando el QC cuenta palabras por cue con tolerancia (p. ej. word-start ±50 ms), generar los cortes con el MISMO predicado del QC, no con otro: asignar cada palabra al primer cue cuyo `[start−tol, end+tol)` contenga su start, todo en ms enteros (el float-dust de segundos convierte un borde exacto en doble-conteo silencioso). Y retroceder cada fin de bloque a `(siguiente palabra − tol − 1 ms)` — incluyendo contra la primera palabra del cue siguiente — para que ninguna palabra cuente en dos bloques. Un cue cuyo fin pise el start del siguiente falla overlap aunque el texto esté bien: el fin manda, no el texto.

## 36. REGLA FINAL + ENTENDERSE SIN ESFUERZO + ACOMPAÑAR LA VOZ + RESPETAR LA ESCENA + RESPETAR SAFE ZONES + MANTENER LA IDENTIDAD DE MILO. Solo entonces: SUBTITLE_MASTER_QC = PASS.
