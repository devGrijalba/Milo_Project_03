---
name: multiagent-policy
description: "Use when a task repeats N times or splits into streams."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Politica de delegacion a multiagentes

## Cuando delegar SIEMPRE

Delegar es la opcion por defecto cuando se cumple **cualquiera** de estas:

| Señal | Ejemplo real |
|---|---|
| **N operaciones identicas** | Verificar 13 imagenes ancla una por una |
| **N archivos que leer y resumir** | Auditar 110 archivos de un paquete |
| **2+ flujos independientes** | Analizar personaje y ambientes a la vez |
| **Trabajo tediouso, veraz y de bajo riesgo** | Enumerar refs, medir dimensiones, listar hashes |
| **Contexto que no cabe comodo** | Analizar corpus de videos enteros |

El criterio no es "es mucho trabajo". Es **"cada unidad de trabajo es repetitiva y el
resultado se puede resumir en pocas lineas"**. Ahi el Fan-Out paga.

## Cuando NO delegar

- Una sola llamada a herramienta.
- Trabajo que necesita **interaccion del usuario** (los subagentes no pueden preguntar).
- Decisiones editoriales: que universo, que imagen, que criterio de aprobacion.
- Efectos externos que exijan verificacion (subir, publicar, escribir en otro sitio).
- Si una unidad necesita el resultado de otra (dependencia real, no paralelismo).

## Como delegar bien

1. **Un hijo por unidad de trabajo**, no uno que haga todo. N imagenes -> N hijos.
   Un hijo con 13 tareas es un hijo lento; 13 hijos de 1 imagen saturan el limite.
2. **Cada hijo recibe TODO el contexto.** No conoce esta conversacion. Pasa rutas
   absolutas, criterio de exito, y el formato exacto de salida que esperas.
3. **El resultado viaja por archivo, no por resumen.** Cuando la salida importa
   (JSON, tabla, medida), el hijo **escribe un archivo** y devuelve solo la ruta.
   Un resumen de 300 lineas de un hijo es tan inutil como no tener respuesta.
4. **El padre verifica antes de afirmar.** Un resumen de hijo es auto-informe, no
   hecho. Si el hijo dice "generado", comprueba el hash, el tamano, la fecha.
5. **No delegar el juicio.** Delega la ejecucion. El veredicto es del padre.

## Limites

- `delegation.max_concurrent_children` es el tope duro. Reparte en tandas si te pasas.
- Cada hijo tiene su propia sesion de terminal: no comparten cwd ni procesos.
- Un hijo que deriva: `action='steer'` con una instruccion concreta, no "lo haz mejor".
- **Timeout por hijo: 600 s.** Pasado ese limite el hijo muere y pierdes su trabajo.
  Un hijo que hace mas de ~6 llamadas de vision_analyze no llega. Reparte o reduce.

## ANTES de despachar: fan-out real, no solapado

**Un hijo por unidad de trabajo, y comprueba que no se solapan entre tandas.**

| Regla | Motivo |
|---|---|
| 1 hijo = 1 imagen, no 2 | Dos imagenes por hijo serializa el trabajo: la mitad del tiempo espera |
| Antes de la 2a tanda, `action='list'` | Despachar sin listar duplica el trabajo y multiplica el gasto |
| Deten los redundantes con `action='stop'` | Un hijo parado a tiempo no cobra los 600 s completos |
| El cuello de botella suele ser la herramienta, no el numero de hijos | Ver abajo |

## vision_analyze: protocolo obligatorio (medido 2026-09-29)

`vision_analyze` tarda **30-120 s por llamada** y **expira con archivos > 300-400 KB**.
La longitud del PROMPT tambien cuenta: 304 KB + pregunta corta pasa, 411 KB + pregunta
de 90 palabras falla.

**Preparar SIEMPRE con el modulo, nunca a mano:**

```bash
python ~/AppData/Local/hermes/vision-prep.py <imagen> class|describe|read
python ~/AppData/Local/hermes/vision-prep.py <imagen> --crop X:Y:W:H -o salida.jpg
```

| Nivel | Ancho | Uso |
|---|---|---|
| `class` | 300 px (~18 KB) | que hay aqui, contar, clasificar |
| `describe` | 560 px (~85 KB) | descripcion visual, materiales, luz |
| `read` | 900 px (~300 KB) | texto pequeno, letras, numeros |

**Reglas que no se negocian:**

1. **Recortar ANTES de escalar.** Escalar la imagen entera destruye detalle fino: a 300 px
   NO se leen los letreros de una placa, a 941 px si. Para texto pequeno, recortar.
2. **Una pregunta por llamada, corta.** "Describe el tipo de calle" funciona. Una de
   90 palabras agota el presupuesto aunque la imagen sea pequena.
3. **NO superponer cuadrículas.** `drawgrid` de 10% hace fallar la llamada con timeout
   (patron fino confunde al modelo). Para medir, pedir PORCENTAJES desde el borde.
4. **`drawtext` no funciona en Windows**: fontconfig no encuentra fuente y ffmpeg
   aborta con SIGSEGV. Etiquetar en el prompt, no en la imagen.
5. **Los subagentes NO preparan imagenes.** Leen proxies ya hechos y devuelven un
   archivo. Si un hijo escribe su propio script de reescalado, el trabajo se duplica
   y el limite de 600 s lo mata (medido: 9 hijos, 0 resultados).
6. **Medir es en dos pasos:** leer el % desde el borde -> convertir a pixeles de la
   ORIGINAL -> recortar esa zona para verificar. Verificar con un recorte de la zona
   aislada: si ahi esta lo que se busca, las coordenadas estan bien.

## La trampa real: vision_analyze

`vision_analyze` tarda **30-120 s por llamada** y **expira con PNG grandes** (1.5-2 MB).
Un hijo que analiza 2 imagenes con los originales se pasa de 600 s y muere.

**Prepara los proxies UNA vez, tu, antes de delegar:**

```bash
mkdir -p /tmp/proxy
ffmpeg -y -loglevel error -i "origen.png" -vf "scale=560:-2" -q:v 6 "/tmp/proxy/nombre.jpg"
```

625 KB para 17 imagenes. Pasa las rutas de los proxies en el `context` de cada hijo.

Verificar que el proxy sirve: los hijos que reciben JPEG de 10-85 KB no reintentan y no
inventan scripts de resize propios.

## Cuando un hijo muere por timeout

- No lo re-despachas: vuelve a morir igual. El problema es la latencia, no la tarea.
- Baja el trabajo por hijo (menos imagenes) o usa proxies mas pequenos.
- Si el trabajo es pequeno, **hazlo tu**: dos llamadas tuyas ganan a dos hijos de 10 min.

## Anti-patrones

| Anti-patron | Por que falla | Que hacer |
|---|---|---|
| Delegar una sola tarea | El overhead de crear el hijo supera el trabajo | hacerlo aqui |
| Delegar y creer el resumen | Es auto-informe; puede mentir | verificar el artefacto |
| Delegar N tareas a 1 hijo | Se serializa dentro del hijo | 1 hijo por tarea |
| Delegar la decision editorial | El hijo no conoce al usuario ni el canon | decidir, luego delegar la ejecucion |
| Devolver la salida completa en el resumen | Inunda el contexto del padre | que el hijo escriba a disco |

## Verificacion antes de reportar

Antes de decir "hecho", comprobar por medios propios:

- Si son archivos: existen, con el tamano y fecha esperados.
- Si es codigo: `node --check` / import real / ejecucion real, no lectura.
- Si es una cifra: releerla del dato, no del resumen.
- Si es una decision: nombrarla como decision, con su motivo.
