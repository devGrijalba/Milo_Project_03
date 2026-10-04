# -*- coding: utf-8 -*-
"""Extrae las filas de una tabla web desde el JSON del árbol de accesibilidad (AX)
que computer_use guarda en disco (elements_<hash>.json).

Genérico: sirve para cualquier tabla/página virtualizada cuyas filas aparezcan como
`DataItem` con un label concatenado que empiece por un prefijo reconocible.
Diseñado para Meta Business Suite (prefijos "Facebook "/"Instagram "), pero adaptable.

Uso:
  python extract_ax_table.py <elements_*.json> [prefijos...]
    prefijos (opcional): uno o más strings que inician cada fila. Default: "Facebook " "Instagram ".

Requiere que el label de cada fila contenga: <prefijo...> <título...> <fecha> <n1> <n2> ...
Donde n1 = métrica principal (visualizaciones) y n2 = secundaria (alcance).
"""
import json, sys, re

def load_labels(path, prefixes):
    d = json.load(open(path, encoding='utf-8'))
    out = []
    def walk(o):
        if isinstance(o, dict):
            if ('label' in o and isinstance(o['label'], str)
                    and len(o['label']) > 40
                    and o['label'].startswith(prefixes)):
                out.append(o['label'])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for i in o:
                walk(i)
    walk(d)
    return out

def parse(r, prefixes):
    # detectar cuál prefijo abre la fila
    pf = next((p for p in prefixes if r.startswith(p)), '?')
    body = r[len(pf):].strip()
    # fecha: "lunes, 1 de septiembre 17:35" (patrón día-de-mes-hora)
    mf = re.search(r'(lunes|martes|miércoles|jueves|viernes|sábado|domingo),? \d+ de \w+ \d+:\d+', body)
    title = body[:mf.start()].strip() if mf else body[:110]
    fecha = mf.group(0) if mf else '?'
    nums = body[mf.end():].strip() if mf else ''
    vals = re.findall(r'-?\d+', nums)
    vis = vals[0] if vals else '0'
    alc = vals[1] if len(vals) > 1 else '--'
    return {'plataforma': pf.strip(), 'fecha': fecha, 'vis': vis, 'alcance': alc, 'titulo': title}

def main():
    if len(sys.argv) < 2:
        print("Uso: python extract_ax_table.py <elements_*.json> [prefijos...]"); return
    prefixes = tuple(sys.argv[2:]) or ('Facebook ', 'Instagram ')
    for path in sys.argv[1:2]:
        labels = load_labels(path, prefixes)
        seen, rows = set(), []
        for l in labels:
            key = l[:45]
            if key in seen:
                continue
            seen.add(key)
            rows.append(parse(l, prefixes))
        # filtrar ruido (cambios de foto/portada, historias vacías, genéricos)
        ruido = ('ha actualizado su foto', 'ha actualizado su foto del perfil', 'Tu historia')
        contenido = [r for r in rows if not any(x in r['titulo'] for x in ruido)]
        print("\n=== %s: %d contenido único (de %d total) ===" % (path.split('\\')[-1], len(contenido), len(rows)))
        def key(r):
            try: return int(r['vis'])
            except: return 0
        for r in sorted(contenido, key=key, reverse=True):
            print("%-8s | %-26s | Vis:%-5s | Alcance:%-5s | %s" %
                  (r['plataforma'], r['fecha'], r['vis'], r['alcance'], r['titulo'][:65]))

if __name__ == '__main__':
    main()
