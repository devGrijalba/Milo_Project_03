import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
from src.common import *
from src.contract_validator import validate
from src.timing_planner import timing
from src.scorecard import aggregate
def critic_check(report,p,c):
 if not isinstance(report,dict) or report.get('candidate_hash')!=digest(p):return ['Critic must reference exact candidate hash']
 if report.get('role')!='independent_critic':return ['Critic role must be independent_critic']
 issues=[];d=report.get('dimensions',{})
 for k in DIMENSIONS:
  item=d.get(k,{}) if isinstance(d,dict) else {};v=item.get('score')
  if not isinstance(v,(int,float)) or isinstance(v,bool) or not math.isfinite(v) or not 0<=v<=100:issues.append('Invalid creative score '+k);continue
  if not isinstance(item.get('evidence'),list) or not item['evidence'] or not all(isinstance(x,str) and x.strip() for x in item['evidence']):issues.append('Evidence missing '+k)
  if v<(c['min_milo_score'] if k=='milo' else c['min_creative_score']):issues.append('Creative score below threshold '+k)
 for k in ['facebook_viewer','cinematic_director','milo_director']:
  if not isinstance(report.get('perspectives',{}).get(k),str) or not report['perspectives'][k].strip():issues.append('Perspective missing '+k)
 if not isinstance(report.get('critical_errors'),list):issues.append('critical_errors array missing')
 elif report['critical_errors']:issues.extend(str(x) for x in report['critical_errors'])
 if report.get('novelty_checked_against_history') is not True:issues.append('History novelty check missing')
 return issues


def finalize(p,request,c,critic=None):
 errors=validate(p,request,c)
 for b in p.get('beats',[]):
  for k in ['viewer_emotion','narrator_intention','emotional_entry','emotional_exit','emphasis','pause_reason','visual_sync','forbidden_delivery']:
   if not isinstance(b.get('director_direction',{}).get(k),str) or not b['director_direction'][k].strip():errors.append('Missing director_direction '+k)
  if not isinstance(b.get('director_voice_text'),str):errors.append('Missing director_voice_text')
 if errors:return {'status':'NEEDS_SCRIPT_REVISION','technical_errors':errors,'creative_status':'NOT_EVALUATED'},p
 p=timing(p,c);errors=[]
 if p['timing']['duration_s']>c['max_duration_s']:errors.append('Estimated duration exceeds limit')
 if any(s['requires_subshot_direction'] for s in p['timing']['shots']):errors.append('Some beats need explicit subshot direction to satisfy max shot duration')
 if errors:return {'status':'NEEDS_SCRIPT_REVISION','technical_errors':errors,'creative_status':'NOT_EVALUATED'},p
 if critic is None:return {'status':'AWAITING_CREATIVE_QC','technical_errors':[],'candidate_hash':digest(p),'creative_status':'PENDING'},p
 errors,scorecard=aggregate(critic,p,c,critic_check)
 return {'status':'NEEDS_SCRIPT_REVISION' if errors else 'SCRIPT_APPROVED','technical_errors':[],'creative_errors':errors,'creative_status':'REJECTED' if errors else 'PASS','candidate_hash':digest(p),'critic_report':critic,'scorecard':scorecard},p


