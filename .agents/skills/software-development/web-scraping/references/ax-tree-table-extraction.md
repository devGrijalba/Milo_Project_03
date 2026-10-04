# Extraer datos de una tabla web virtualizada vía el árbol de accesibilidad (AX) de computer_use

## Cuándo usar esto
Cuando extraes datos de una app web con `<table>`/datagrid **virtualizada o paginada** (Meta
Business Suite Insights, dashboards SaaS, listas con scroll infinito) y:
- Solo se ven ~3-5 filas en el viewport pero hay decenas de registros.
- No hay endpoint JSON fácil de leer (o el token/API está bloqueado).
- Ya estás dentro con el control de escritorio (`computer_use`) y el usuario está logueado.

**El vector clave:** la UI virtualizada **sigue renderizando TODAS las filas como celdas accesibles**
en el árbol de accesibilidad (AX), aunque estén fuera del viewport. `computer_use` **persiste ese AX
completo a disco** — así que puedes leer todas las filas sin scroll ni clics repetidos.

## 1. Capturar el AX completo (NO solo lo visible)
```python
computer_use capture(app=<navegador>, mode='som', max_elements=400)
```
- **`max_elements` es crítico**: su default (~100) **trunca** el AX y pierdes filas. Sube a 300–400.
- Esto escribe un JSON en:
  `C:/Users/<user>/AppData/Local/hermes/cache/computer_use/elements_<hash>.json`
- El mismo snapshot lo reporta: `(full element tree with untruncated labels saved to ... elements_<hash>.json)`.

## 2. Estructura del AX (lo que parsea el script)
Cada fila de contenido es un `DataItem` cuyo `label` concenta (separados por espacios):
```
<plataforma> <título...> <tipo> <app> Promocionar Abrir menú desplegable  <fecha> <vis> <alcance> <otros números...>
```
Ejemplo real (Meta Business Suite):
```
Facebook Mi mamá me dijo "Baja al pasillo" a las 23:41... Textopia.reels Promocionar Abrir menú desplegable  martes, 1 de septiembre 17:35 244 220 216 ...
```
→ fecha=`martes, 1 de septiembre 17:35`, vis=`244`, alcance=`220`.
- Cada fila aparece **2 veces** en el AX (celda + contenedor) → des-duplicar.
- Las columnas numéricas van en orden: `vis`, `alcance`, `espectadores`, `interacciones`, `reacciones`,
  `comentarios`, `compartidos`, `guardados`, clics, `seguidores`, `tiempo`, `reproducciones_3s`, etc.

## 3. Script reutilizable
`scripts/extract_ax_table.py` (en este skill) — genérico: recibe el `.json` del AX y cualquier
prefijo de fila (`--prefix "Facebook " "Instagram "`), extrae filas únicas, filtra ruido y ordena
por el primer número (visualizaciones). Ejecutar:
```bash
python scripts/extract_ax_table.py "C:/.../elements_<hash>.json"
```

## 4. XPath / parse del label
```python
import re
mf = re.search(r'(lunes|martes|miércoles|jueves|viernes|sábado|domingo),? \d+ de \w+ \d+:\d+', body)
title = body[:mf.start()].strip() if mf else body[:110]
nums  = re.findall(r'-?\d+', body[mf.end():] if mf else '')
vis, alc = nums[0] if nums else '0', nums[1] if len(nums)>1 else '--'
```

## Pitfalls
1. **`$HOME` / ruta MSYS no funciona dentro de Python** (`/c/...` → `FileNotFoundError`). Usar ruta
   nativa `C:/...`. Mismo problema que ffmpeg/ffprobe: herramientas nativas necesitan rutas nativas.
2. **`max_elements` bajo** corta el AX → parece que "hay 3 publicaciones" cuando en realidad hay 15.
   Subir a 300-400 y releer el JSON del disco.
3. **No contar ruido**: filas tipo "Tu historia" (0 views), "ha actualizado su foto/portada" (cambios
   de imagen), timestamps, etc. Filtrar por el título.
4. **El AX se congela en el snapshot**: si haces scroll/clic después de capturar, re-capturar para
   tener el JSON fresco.
5. **Cerrar modales/popups before capturar** (Escape o X): los modales de "vista nueva", notificaciones,
   "no es tu navegador predeterminado" tapan la tabla en el viewport (aunque el AX las incluya igual).
