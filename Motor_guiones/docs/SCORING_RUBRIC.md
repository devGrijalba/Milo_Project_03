# Score de guion antes de producción — rúbrica 1.0.0

Mínimo 90/100 (equivale a 9/10). Se aplica al guion y su dirección, no a la semilla. El score del banco no autoriza producción.

## Dimensiones

| Dimensión | Criterios verificables en guion |
|---|---|
| hook | Entrada inmediata; conflicto reconocible; promesa concreta; primer frame planificado; payoff cumple la promesa |
| narrative | Causalidad, información nueva, progresión, loops resueltos y cierre ganado |
| emotion | Conducta específica, credibilidad, emoción contenida, sin manipulación o moraleja hueca |
| visual | Cada frase tiene apoyo visual; objeto con función; variación de plano; continuidad y espacio superior |
| voice | Intención interpretable; ritmo y pausas justificadas; claridad oral; no evaluar audio inexistente |
| editing | Movimiento/transición motivados; orden coherente; planos realizables y ritmo estimado |
| shareability | Destinatario concreto; identificación y frase/gesto que representa al espectador; CTA opcional |
| milo | Canon de personajes, mundo doméstico ilustrado, tono, lenguaje de objetos y mecanismos documentados en minería |

## Anclas de puntuación

0–39: criterio ausente o contradicción grave. 40–59: defecto estructural. 60–74: potencial con debilidades claras. 75–84: funcional pero genérico o incompleto. 85–89: sólido con una debilidad concreta aún pendiente. 90–94: todos los elementos relevantes sostenidos por evidencia, sin defecto material. 95–100: solución excepcional y comparación específica que justifica esa diferencia; no usar como premio automático.

Cada nota requiere evidencia citando beat_ids válidos, explicación y mejora pendiente (puede decir «ninguna material identificada», con motivo). No puntuar por longitud, cantidad de campos o apariencia profesional. Las notas son juicios editoriales; no porcentajes de retención o probabilidad de viralidad.

## Tres perspectivas y compuesto

Espectador Facebook = 30% hook + 25% narrativa + 20% emoción + 25% compartibilidad.
Director cinematográfico = 30% narrativa + 30% visual + 25% montaje + 15% voz.
Director Milo = 60% afinidad Milo + 20% emoción + 20% visual.
Compuesto = 40% espectador + 30% cinematográfico + 30% Milo.

## Gate estricto

Todas las dimensiones ≥90, todas las perspectivas ≥90 y compuesto ≥90; cero errores críticos; controles técnicos aprobados; confianza media/alta; evidencia e historial consultados. Un promedio alto no rescata una dimensión baja.

Un pase analítico por llamada. Segundo pase adversarial solo ante disparadores del orquestador (90–92, confianza no alta, desacuerdo o candidato reparado), sin mostrar las notas del primero al segundo. Cuando hay dos, se conserva el mínimo de ambos por dimensión. Si difieren más de 8 puntos, reevaluar y documentar el desacuerdo; no promediarlo para aprobar. Puede usarse el mismo modelo en contextos separados: eso no constituye independencia humana.

Máximo tres rondas de corrección. Sin superar el gate, NEEDS_SCRIPT_REVISION y prohibido comenzar voz, imagen o render como producción aprobada. No reducir el mínimo para cerrar el ciclo. Falta de evidencia/QA se mantiene pendiente.

## Afinidad con Milo y originalidad

Comparar con canon y reglas de minería incluidos, citando el mecanismo y su manifestación en beats. Ejemplo: objeto concreto como prueba de cuidado, no nombrar «familia» para obtener afinidad. Compatibilidad con Milo no significa copiar EP0002. Comparar conflicto, secuencia de decisiones, revelación y cierre con historial; separar afinidad de repetición. Sin historial declarar su ausencia y alcance limitado de novedad, nunca originalidad absoluta.

## Calibración pendiente

Se recomienda un conjunto de referencia etiquetado por el usuario con guiones fuertes, débiles, redundantes y ajenos al canon. Medir falsos PASS, consistencia entre evaluaciones y concordancia con decisiones humanas. Después relacionar dimensiones con métricas reales de episodios, sin asumir causalidad. Este paquete publica protocolo; no afirma que se haya realizado esa calibración.

## Investigación consultada

- https://developers.openai.com/api/docs/guides/evaluation-best-practices — rúbricas, sesgo de posición/verbosidad y calibración de jueces.
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — combinar gates deterministas y evaluación basada en modelos; criterios claros y casos de fallo.

El umbral 90 y los pesos son decisiones editoriales del proyecto, no umbrales demostrados por esas fuentes.
