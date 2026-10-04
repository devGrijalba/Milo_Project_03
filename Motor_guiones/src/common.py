import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
DIMENSIONS=['hook','narrative','emotion','visual','voice','editing','shareability','milo']
def read(p):return json.loads(pathlib.Path(p).read_text(encoding='utf8'))


def write(p,d):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True);temp=p.with_suffix(p.suffix+'.tmp');temp.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');temp.replace(p)


def digest(d):return hashlib.sha256(json.dumps(d,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def config(path=None):
 c=read(path or ROOT/'config/engine.json');return c


def context(c):
 # Paths relative to module root; a caller may supply absolute paths to live project canon.
 def path(v):return pathlib.Path(v) if pathlib.Path(v).is_absolute() else ROOT/v
 result={'canon':read(path(c['canon'])),'worlds':read(path(c['worlds'])),'mining':path(c['mining']).read_text(encoding='utf8')}
 for key in ['characters','anchors']:
  if c.get(key):result[key]=read(path(c[key]))
 return result


