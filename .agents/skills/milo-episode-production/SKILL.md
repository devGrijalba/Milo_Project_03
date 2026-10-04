---
name: milo-episode-production
description: 'DEPRECATED SHIM — redirects to the single source of truth in D:/hermes/MILO/10_CADENA. Use when any MILO/EP/Flow/render/publishing task appears.'
---

# DEPRECATED SHIM

Este skill **no contiene lógica de producción**. No hay reglas aquí.

La fuente oficial y única es:

```
D:/hermes/MILO/10_CADENA/
├── CONTRACT.md              contrato vigente (ley)
├── CONTRACT.json            contrato legible por máquina
├── milo_ctx.py              doctor read-only (primera acción)
├── guards/                  gates + parsers + tests
├── skills/                  skills de cadena
└── specs/REVIEW_V2_1/       memoria + auditoría + contrato vigente
```

## Redirección obligatoria

0. **Verifica que la raíz sigue existiendo antes de seguir el redirect.** Si
   `D:/hermes/MILO/10_CADENA/CONTRACT.md` no está, la cadena fue movida o archivada
   y este shim ya no describe el estado real. Reporta dónde vive ahora la cadena y
   para — no ejecutes `milo_ctx.py` desde memoria de otra sesión, ni lo reconstruyas
   desde este archivo. Una carpeta etiquetada `OLD`/`ARCHIVE` con fecha es resultado
   de una limpieza masiva, no prueba de que el proyecto esté retirado: dilo y pregunta.
1. Leer `D:/hermes/MILO/10_CADENA/CONTRACT.md`.
2. Ejecutar `python D:/hermes/MILO/10_CADENA/milo_ctx.py`.
3. Seguir la `next_action` impresa.

Si el contrato no se puede leer o el doctor no corre, decirlo con todas las letras y parar. No improvisar reglas, rutas, estados ni gates desde el chat, desde memoria del chat o desde este archivo.

## Lo único que este shim conserva

- El nombre `milo-episode-production` (compatibilidad con llamadas antiguas).
- Un puntero al contrato.

Nada más. Cualquier conflicto entre este shim y `10_CADENA/CONTRACT.md` lo resuelve `CONTRACT.md`.
