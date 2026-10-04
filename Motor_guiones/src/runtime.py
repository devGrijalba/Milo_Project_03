"""Per-role content-addressed cache and live progress; no provider-specific API."""
import pathlib,time,threading,json,hashlib
from src.common import read,write,digest
LOCK=threading.RLock()
def event(folder,role,status,**extra):
 if folder is None:return
 p=pathlib.Path(folder)/'script_progress.json'
 with LOCK:
  d=read(p) if p.exists() else {'roles':{}}
  d['roles'][role]={'status':status,'updated_unix_s':time.time(),**extra}
  write(p,d)
def runtime_fingerprint():
 root=pathlib.Path(__file__).resolve().parents[1]
 files=list((root/'src').glob('*.py'))+list((root/'prompts').glob('*.md'))+list((root/'docs').glob('*.md'))+list((root/'schemas').glob('*.json'))
 result={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
 config=root.parents[1]/'agente/config.json'
 if config.exists():
  c=read(config);result['hermes_runtime']={k:c.get(k) for k in ['model','critic_model','provider','hermes_command','critic_command','timeout_s']}
 for name in ['WORKER.md','hermes_adapter.py']:
  p=root.parents[1]/'agente'/name
  if p.exists():result['adapter/'+name]=hashlib.sha256(p.read_bytes()).hexdigest()
 return result

def cached_call(command,payload,timeout,role,folder,invoke,max_bytes=None):
 key=digest({'contract':'script-optimization-1.3.0','command':command,'payload':payload,'timeout':timeout,'runtime':runtime_fingerprint()})
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
