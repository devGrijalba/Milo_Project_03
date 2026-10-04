"""Adapter dispatch. Resolves WHICH provider implements the call contract.

src/provider.py keeps the subprocess/Hermes route untouched.
src/ds_provider.py implements the same call() for DeepSeek over CDP.

The seam is here so orchestrator and multiagent keep importing `call` from
provider and never learn which backend is active: switching to DeepSeek is a
config value, not a code change in fourteen modules.

    provider = "deepseek_cdp"  -> src.ds_provider.call
    provider = "hermes_subprocess" (default) -> the subprocess call below
"""
import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
from src.common import *

# Keys a SCRIPT_ENGINE role payload must carry to be executable at all.
BASE_PACKAGE_KEY='base_package'
# Roles whose payload legitimately carries the candidate instead of a base package.
CANDIDATE_ROLES=('script_critic',)

def validate_payload(role,payload):
 """Return the list of missing required keys. Empty means executable."""
 if not isinstance(payload,dict):return ['payload must be an object']
 if role=='script_synthesizer':
  missing=[k for k in ('base_package','specialist_reports') if not isinstance(payload.get(k),dict) or not payload[k]]
  if not missing and len(payload['specialist_reports'])!=5:missing.append('five_specialist_reports')
  return missing
 if role in CANDIDATE_ROLES:
  # Presence, not truthiness: an empty candidate is a real value the validator
  # must reject with a proper message, not a reason to demand the payload again.
  return [k for k in ('candidate','candidate_hash') if payload.get(k) is None or k not in payload]
 return [k for k in (BASE_PACKAGE_KEY,) if not payload.get(k)]

def call_subprocess(command,payload,timeout,role=None):
 if not command or not isinstance(command,list) or not all(isinstance(s,str) for s in command):raise ValueError('PROVIDER_NOT_CONFIGURED: configure command as argv array')
 if role:
  missing=validate_payload(role,payload)
  if missing:raise ValueError('HERMES_TASK_BLOCKED:MISSING_SCRIPT_REQUEST_CONTEXT:'+','.join(missing))
 r=subprocess.run(command,input=json.dumps(payload,ensure_ascii=False),text=True,encoding='utf8',capture_output=True,timeout=timeout,check=False,shell=False)
 if r.returncode:raise RuntimeError('Provider failed with exit code '+str(r.returncode))
 result=json.loads(r.stdout)
 # A worker block is propagated as a failure, never handed upward as a candidate.
 if isinstance(result,dict) and result.get('status')=='HERMES_TASK_BLOCKED':raise ValueError('HERMES_TASK_BLOCKED:'+str(result.get('reason') or 'unknown'))
 return result


def call(command,payload,timeout,role=None,config_path=None,session_name=None):
 """Active provider. Reads `provider` from config.

 Defaults to the subprocess route when the key is absent, so a config without an
 explicit `provider` keeps the original behaviour. Only "deepseek_cdp" selects the
 DeepSeek route.

 `session_name` is the LOGICAL owner of the tab (e.g. "specialist_hook"). It is
 ignored by the subprocess route and honoured by the DeepSeek route, which maps
 it to a physical tab through the pool. The caller never learns the tab id.
 """
 name=None
 try:
  c=config(config_path)
  name=c.get('provider') if isinstance(c,dict) else None
 except Exception:
  pass
 if name=='deepseek_cdp':
  from src.ds_provider import call as ds_call
  return ds_call(command,payload,timeout,role=role,config_path=config_path,
                 session_name=session_name)
 return call_subprocess(command,payload,timeout,role=role)


