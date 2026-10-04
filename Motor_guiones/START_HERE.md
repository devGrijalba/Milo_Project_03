# Actualización 1.3.0
Leer docs/OPTIMIZATION_1.3.0.md antes de las instrucciones históricas. Síntesis recibe contexto completo y cinco informes; cada crítico devuelve exactamente un pase. Usar caché y progreso, no reconstruir el módulo.

# Inicio para Hermes

Trabajar desde SCRIPT_ENGINE; leer README.md, config/engine.json y prompts. Usar la semilla y contexto reales, no reconstruir otros motores.

## Ruta con Hermes como escritor

1. Preparar el contexto:
```bash
python src/engine.py prepare --episode EP0100 --seed MILO-S0001 --out out/EP0100/request.json
```
2. Hermes lee el request y ejecuta prompts/writer.md. Escribe su candidato JSON en out/EP0100/candidate.json respetando seed_snapshot y seed_hash.
3. Validar y exportar:
```bash
python src/engine.py check --request out/EP0100/request.json --candidate out/EP0100/candidate.json --out out/EP0100
```
4. Si queda AWAITING_CREATIVE_QC, un pase de crítico separado recibe el paquete exportado con tiempos, su candidate_hash del QC y el contexto. Sigue prompts/critic.md y escribe critic.json. No usar un crítico sintético.
5. Aplicar el crítico:
```bash
python src/engine.py check --request out/EP0100/request.json --candidate out/EP0100/candidate.json --critic out/EP0100/critic.json --out out/EP0100
```
6. Corregir hasta 3 rondas cuando corresponda. Nunca cambiar a mano el estado para superar el gate.

## Ruta automatizada con proveedor

En config/engine.json, writer_command y critic_command son listas argv. Ejemplo de estructura (adaptador propio del runtime, no archivo incluido):
`["python", "D:/runtime/hermes_writer_adapter.py"]`.

El adaptador recibe una petición JSON completa por stdin y devuelve JSON puro por stdout. El escritor produce el contrato; el crítico produce el reporte. Mantener diagnóstico en stderr y no exponer credenciales. No se prescribe un modelo o API no autorizado.

Con ambos adaptadores conectados:
```bash
python src/engine.py run --episode EP0100 --topic "Padre y cariño" --out out/EP0100
```

Salida exit 0 solo SCRIPT_APPROVED; exit 2 pendiente/revisión; exit 3 error/proveedor ausente. Una salida pendiente no autoriza producción.

## Pruebas
```bash
python -m unittest discover -s tests -v
```

Ejemplo EP0099 únicamente demuestra el contrato y permanece pendiente de crítica; no usarlo como episodio original aprobado.

## Canon vivo

Cambiar canon/worlds/mining en configuración por rutas absolutas o relativas a SCRIPT_ENGINE. Los snapshots incluidos corresponden al ZIP recibido. No elevar un cambio del snapshot a canon global sin el flujo de proyecto.
