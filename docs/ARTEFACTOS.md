# Artefactos y entrega — Milo_Project_03

> Cargar solo cuando la tarea tenga que producir o entregar algo.

## Qué es una entrega

**Render final = MP4 + README + Copy + post + 3 bloques.**

**Regla dura: no entregar NADA solo con el MP4.** La entrega cierra en la fase de
README / Copy / post / 3 bloques. Un MP4 sin eso es un trabajo a medias.

## Formato

- `MEDIA:` con **ruta absoluta exacta** por cada entregable. El audio siempre
  descargable.
- Prompts en bloques de código.
- Sin previews HTML salvo pedido explícito.
- Revisiones en `.zip`, nunca RAR.

## Verificación

- **Un render sin inspeccionar no está verificado.** Un gate que no se ejecutó no es un
  gate. Si no se corrió, no se afirma.
- **Reportes honestos**: si algo falló, se dice. Sin falsos OK.
- **Nada a medias**: si la voz falla, se entrega el script + `VOICE_TEXT_BLOCKED`, no un
  audio truncado.
- Reportes de fallo con 8 secciones: objetivo, entorno, pasos OK/FALLÓ, tipo, evidencia
  literal, hecho vs hipótesis, propuesta, confianza.

## Flujo MILO

1. Validar la interpretación del guion —quién escribe cada mensaje, orden, beats de
   susto— **antes** del render.
2. Mostrar frames antes del OK.
3. Subtítulos **siempre arriba**, nunca abajo.

## Repo público

Este proyecto está conectado a un repositorio **público** de GitHub. Cualquier
credencial, token, cookie, `.env` o perfil de navegador que se añada al árbol acaba
publicado. Para material sensible: `D:\03_Pruebas\cdp-chrome-clean`, que es hermano del
repo y git no lo ve.

## Comandos

```bash
# Motor
python Motor_guiones/tests/gate_v2.py
python Motor_guiones/tools/validate_package.py <pkg>.json

# Vocal
python tools/ds_inject.py --probe
```