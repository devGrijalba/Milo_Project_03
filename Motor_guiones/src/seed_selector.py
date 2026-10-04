import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
from src.common import *

REQUIRED_SEED_FIELDS=('seed_id','family_id','territorio','semilla','revision')
REQUIRED_REVISION_FIELDS=('elegible','compuesto','calidad','afinidad')

def _validate_bank(bank):
 if not isinstance(bank,dict) or not isinstance(bank.get('seeds'),list):raise ValueError('INVALID_SEED_BANK')
 if bank.get('cantidad') not in (None,len(bank['seeds'])):raise ValueError('SEED_BANK_COUNT_MISMATCH')
 seen=set()
 for s in bank['seeds']:
  if not isinstance(s,dict):raise ValueError('INVALID_SEED_RECORD')
  missing=[k for k in REQUIRED_SEED_FIELDS if k not in s]
  if missing:raise ValueError('SEED_FIELDS_MISSING:'+','.join(missing))
  if s['seed_id'] in seen:raise ValueError('DUPLICATE_SEED_ID:'+s['seed_id'])
  seen.add(s['seed_id'])
  q=s.get('revision') or {};missing=[k for k in REQUIRED_REVISION_FIELDS if k not in q]
  if missing:raise ValueError('SEED_REVISION_FIELDS_MISSING:'+s['seed_id']+':'+','.join(missing))
 return bank

def select(c,seed_id=None,topic='',history=None):
 p=pathlib.Path(c['seed_bank']);b=_validate_bank(read(p if p.is_absolute() else ROOT/p));h=history or []
 used={x.get('seed_id') for x in h};recent={x.get('family_id') for x in h[-10:]};arcs=[x.get('narrative_cluster_id') for x in h[-10:]]
 candidates=[]
 for s in b['seeds']:
  q=s.get('revision',{});arc=s.get('narrative_cluster_id')
  if s['seed_id'] in used or s['family_id'] in recent or (arc and arcs.count(arc)>=2):continue
  if not q.get('elegible') or q.get('compuesto',0)<85 or q.get('calidad',0)<80 or q.get('afinidad',0)<85:continue
  if seed_id and s['seed_id']!=seed_id:continue
  if topic and topic.casefold() not in (s['territorio']+' '+s['semilla']).casefold():continue
  candidates.append(s)
 if not candidates:raise ValueError('NO_ELIGIBLE_SEED')
 s=sorted(candidates,key=lambda x:(-x['revision']['compuesto'],x['seed_id']))[0]
 return {'bank_version':b['version'],'seed':s,'seed_hash':digest(s)}
