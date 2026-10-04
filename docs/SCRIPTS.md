# Temporales y scripts — Milo_Project_03

> Cargar solo cuando la tarea implicar escribir o ejecutar código.
> Complementa `AGENTS.md`, que es el índice raíz.

Adoptada tras medir el desperdicio real: **133 scripts de un solo uso** acumulados en
`TMPDIR` durante la sesión de implementación, frente a **1** herramienta reutilizable.

## El principio

**Un script que se ejecuta una vez y se tira no es un script: es un accidente con pasos.**

Escribir un `.py` desechable cuesta ~3 llamadas (escribir, leer, corregir). Usar una
herramienta cuesta 1. La diferencia se paga en cada tarea repetida.

## Regla de oro

> **Antes de escribir un script, pregúntate si esto ya lo hace una herramienta.
> Si no, escríbelo en `tools/` de una vez, no en `TMPDIR`.**

`TMPDIR` es para archivos de datos: JSON de salida, capturas, exports, DBs.
**Nunca** para código.

## Dónde va cada cosa

| Qué | Dónde | Por qué |
|---|---|---|
| Script que se reutiliza | `tools/<nombre>.py` | Vive con el proyecto, versionado |
| Script de una sola ejecución que NO se reutilizará | **no se escribe** | Ejecuta el comando directo en `terminal` |
| Datos de salida, capturas, JSON | `TMPDIR` | Regenerable, no vale versionarlo |
| Config con parámetros descubiertos | `tools/<nombre>_selectors.json` | Se reutiliza, se versiona |
| Texto largo a inyectar / prompts | `tools/prompts/*.txt` | Editable sin tocar código |

La regla del medio es la que casi nunca se cumple y la que más cuesta: **antes de crear
`algo.py`, pregunta si el trabajo cabe en un comando de `terminal`**. Si cabe, el script
no debería existir.

## Ciclo de vida de una herramienta

1. **Descubrir e implementar en un solo paso.** Nada de script de sondeo desechable
   seguido del script real. Si necesitas explorar el DOM, el propio script final debe
   sondear y guardar lo descubierto (`--probe`) en lugar de que un script aparte lo haga.
2. **Guardar lo descubierto.** Selectores, IDs, URLs, puertos: a `*.json` en `tools/`, no
   a variables en el `.py`. La segunda vez ya no se sondea.
3. **Probar con ejecución real, cronometrando.** Un script que nunca se ejecutó no es una
   herramienta, es una suposición. Mide y pega el número.
4. **Documentar el fallo que motivó el read-back.** No "hice validaciones", sino
   "sin read-back exacto, un prompt truncado se envía en silencio y parece un error del
   sitio".
5. **Parametrizar lo que va a cambiar.** Prompt, URL, puerto, timeout: argumentos, no
   constantes a editar.

## Reglas de implementación

- **Errores de sintaxis se pagan carísimos.** Dos bugs de escritura introducidos por mí
  costaron 5 llamadas de lectura/parcheo. Escribe el bloque que se ejecuta al final en
  Python, no anidado dentro de un f-string de JavaScript: las llaves dobles `{{}}` y los
  paréntesis se confunden silenciosamente. Sustituye por `JS.replace("TOKEN", valor)`.
- **Caracteres no-ASCII en el código, verificados.** Al redactar se me colaron `首` y
  `体育` en docstrings: invisibles en revisión y romperían el archivo en otro entorno.
  Aplica el grep **solo a código** (`.py`, `.json`, `.js`), nunca a `.md` — en
  documentación los caracteres son texto legítimo, y una regla que siempre marca algo
  es una regla que la gente apaga.
  ```bash
  grep -nP '[\x{4e00}-\x{9fff}\x{3040}-\x{30ff}\x{ac00}-\xd7af}]' <archivo.py>
  ```
- **El read-back es obligatorio** en cualquier herramienta que escriba en un servicio
  externo: si lo que hay en el destino no coincide con lo que se iba a escribir, abortar
  sin enviar. Un prompt a medias es peor que no enviar nada.
- **Nada de magic numbers sin nombre.** `stable >= 2` es `STABLE_READS = 2` con el motivo
  en el comentario.

## Antes de escribir código: checklist

1. ¿Ya existe una herramienta en `tools/` que haga esto? → úsala.
2. ¿Cabe en un comando de `terminal`? → no escribas nada.
3. ¿Es un dato, no un programa? → va a `TMPDIR`.
4. ¿Lo voy a usar otra vez? → `tools/`, con argumentos.
5. ¿No es ninguna de las anteriores? → entonces probablemente no necesita existir.

## Para esta sesión en concreto

El fallo fue escribir `inject_ds.py` (sondeo) + `inject_ds2.py` (inyección) cuando
`tools/ds_inject.py` hace ambas cosas en una sola invocación con `--probe`, y además
guarda `ds_selectors.json` para no volver a sondear. Verificado: **9 segundos** de la
llamada al texto capturado.

Regla derivada: **un solo script por tarea, no una cadena de scripts desechables.**

## Herramientas del proyecto

| Herramienta | Para qué |
|---|---|
| `tools/ds_inject.py` | Inyectar prompts en DeepSeek por CDP (`--probe`, `--text`, `--file`) |
| `.agents/skills/sync_skills.py` | Detectar y reparar deriva de las 35 skills vendorizadas |
| `Motor_guiones/tools/select_seed.py` | Seleccionar semilla del banco canónico |
| `Motor_guiones/tools/validate_package.py` | Validación mecánica de un paquete de guion |
| `Motor_guiones/tests/gate_v2.py` | Gate de regresión del motor (25 comprobaciones) |