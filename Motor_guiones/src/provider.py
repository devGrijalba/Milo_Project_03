"""Adapter for agent commands. No shell. Refuses stub payloads before spending a session.

A stub such as {'role':'script_writer','instructions':'Reply with JSON only.'} is
a structural defect, not a creative one: it gives the worker nothing to act on,
and the worker answers with a blockage. Spending a 2-5 minute session to learn
that locally is waste, so it is rejected here, before the subprocess runs.
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

def call(command,payload,timeout,role=None):
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


