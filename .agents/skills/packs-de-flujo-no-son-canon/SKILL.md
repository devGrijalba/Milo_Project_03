---
name: packs-de-flujo-no-son-canon
description: 'Use when a delivered "base pack" carries another identity.'
---

# Un pack de motor no es el canon del proyecto

## El error que previene

Un archivo entregado como "pack base de Flow", "motor base", o "versión anterior"
puede contener **tecnología reutilizable + la identidad completa de otro proyecto**.
Confundir ambas cosas contamina el canon del proyecto destino de forma silenciosa:
los archivos son válidos, los scripts corren, los gates pasan — y el personaje
generado es el equivocado.

La forma de detectarlo no es el nombre del archivo: es leer `PROJECT_ID`, el
índice de canon o el `registry` del pack y ver **a qué proyecto apunta el contenido**.

## Procedimiento

1. **Clasificar por contenido, no por nombre.** El nombre dice de dónde viene;
   el contenido dice de quién es. Un `MILO_001_MASTER_FRONT.png` dentro del pack
   de otro proyecto no es canon de Milo.
2. **Generar inventario de 3 categorías ANTES de mover un solo archivo:**
   - `REUSE_TECHNICAL` — bridge, protocolo, guard, locks, gates, validadores,
     schema de registry, documentación de la extensión.
   - `RESEARCH_ONLY` — experimentos con cuota consumida, logs de error, evidencia
     técnica. Se guardan con `SOURCE_PROJECT` y `CANON_AUTHORITY=NONE` explícitos.
   - `DO_NOT_IMPORT` — personajes, imágenes, escenarios, mundos, estilos,
     manifests de episodio, prompts narrativos del otro proyecto.
3. **Comparar por hash, no por ruta.** Un archivo puede estar ya migrado con otro
   nombre. SHA-256 sobre el árbol del destino revela qué se solapa de verdad.
4. **Reimplementar el schema, nunca copiar el contenido.** Si el pack trae un
   `registry.json` con `attribute_contract` + `verified`, se copia la
   *estructura* a un registry nuevo con `items: []` y su propio `_id`.
5. **Declarar la frontera en el canon.** Un archivo de declaraciones en
   `01_CANON/rules/` lista qué fuente externa aporta tecnología y qué no aporta
   identidad. Así una mención futura es documentación, no contaminación.

## Los tres sitios donde la contaminación se esconde

- **Un id hardcodeado en código activo** — p. ej. `project: 'el-observador/primera-generacion'`
  en un cliente de generación. No aparece en el canon, no lo grep un test de
  archivos, pero envía a un proyecto ajeno.
- **Una carpeta "legacy" dentro del motor activo** — `tools/_legacy/` sigue siendo
  escaneada como ruta viva aunque contenga código muerto.
- **El propio verificador** — al buscar marcadores ajenos, los encuentra en los
  comentarios que explican por qué están excluidos. Hay que exentar comentarios y
  carpetas de research/archive, o el gate falla siempre y se apaga.

## Verificación obligatoria

El resultado esperado es **que ninguna ruta activa resuelva identidad ajena**.
Eso se comprueba, no se promete:

- check de marcadores de identidad foránea en código activo (excluye comentarios)
- check de que todas las rutas del índice de canon apuntan a `01_CANON/`
- `project_doctor`, `verify-portable`, gates y dry-run

## Lo que sí se hereda de un motor ajeno

La **evidencia medida con cuota real**. Un experimento de otro proyecto que
midió comportamiento del *modelo* (no de su identidad) es conocimiento
transferible: hipótesis valuable, pendiente de validar con el proyecto destino.
Marcarlo como hipótesis transferible, nunca como regla del proyecto destino.