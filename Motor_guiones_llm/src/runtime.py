"""Per-role content-addressed cache and live progress; no provider-specific API."""
import pathlib,time,threading,json,hashlib,sys
from src.common import read,write,digest
LOCK=threading.RLock()
ROOT=pathlib.Path(__file__).resolve().parents[1]

def event(folder,role,status,**extra):
 if folder is None:return
 p=pathlib.Path(folder)/'script_progress.json'
 with LOCK:
  d=read(p) if p.exists() else {'roles':{}}
  d['roles'][role]={'status':status,'updated_unix_s':time.time(),**extra}
  write(p,d)

# Files whose CONTENT defines provider behaviour. Changing any of them must
# invalidate the cache, because a cached result from a different writer is not
# the same result.
#   Fase 0 -> the Hermes subprocess adapter (WORKER.md / hermes_adapter.py)
#   Fase 1 -> the DeepSeek CDP route
PROVIDER_SOURCES=('src/ds_provider.py','tools/ds_session.py','tools/ds_extract.py')

def provider_fingerprint():
 out={}
 for rel in PROVIDER_SOURCES:
  p=ROOT/rel
  if p.exists():out[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
 return out

def runtime_fingerprint():
 files=list((ROOT/'src').glob('*.py'))+list((ROOT/'prompts').glob('*.md'))+list((ROOT/'docs').glob('*.md'))+list((ROOT/'schemas').glob('*.json'))
 result={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
 result['deepseek_provider']=provider_fingerprint()
 result['active_provider']=read(ROOT/'config/engine.json').get('provider')
 return result

def cached_call(command,payload,timeout,role,folder,invoke,max_bytes=None,session_name=None):
 key=digest({'contract':'script-optimization-1.3.0','command':command,'payload':payload,'timeout':timeout,'session_name':session_name,'runtime':runtime_fingerprint()})
 cache=pathlib.Path(folder)/'script_cache'/role/(key+'.json') if folder is not None else None
 if cache and cache.exists():
  d=read(cache)
  if d.get('input_hash')!=key or d.get('result_hash')!=digest(d.get('result')):raise ValueError('SCRIPT_CACHE_TAMPERED:'+role)
  event(folder,role,'CACHED',input_hash=key)
  return d['result']
 event(folder,role,'RUNNING',input_hash=key)
 start=time.monotonic()
 try:
  result=invoke(command,payload,timeout,role=role)
  size=len(json.dumps(result,ensure_ascii=False).encode('utf8'))
  if not isinstance(result,dict):raise ValueError('SCRIPT_RESULT_NOT_OBJECT:'+role)
  if result.get('status') in ['HERMES_TASK_BLOCKED','HERMES_CAPABILITY_BLOCKED']:raise ValueError('SCRIPT_ROLE_BLOCKED:'+role)
  if max_bytes and size>max_bytes:
   if folder is not None:write(pathlib.Path(folder)/'script_rejected_outputs'/(role+'_'+key+'.json'),result)
   raise ValueError('SPECIALIST_OUTPUT_TOO_LARGE:'+role+':'+str(size))
  if cache:write(cache,{'input_hash':key,'result_hash':digest(result),'result':result})
  event(folder,role,'COMPLETED',elapsed_ms=int((time.monotonic()-start)*1000),output_bytes=size,input_hash=key)
  return result
 except Exception as exc:
  event(folder,role,'BLOCKED',elapsed_ms=int((time.monotonic()-start)*1000),reason=str(exc))
  raise
