import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
from src.common import *
def export(folder,p,q):
 folder=pathlib.Path(folder);eid=p.get('episode_id','EP0000');write(folder/(eid+'_script_package_v01.json'),p);write(folder/(eid+'_script_qc_v01.json'),q)
 if isinstance(p.get('beats'),list):
  (folder/(eid+'_guion_v01.md')).write_text('# '+p.get('title','Guion')+'\n\nEstado: '+q['status']+'\n\n'+'\n\n'.join(b.get('narration','') for b in p['beats'] if isinstance(b,dict)),encoding='utf8')
  (folder/(eid+'_storyboard_v01.md')).write_text('# Storyboard\n\n'+'\n\n'.join('## '+b.get('beat_id','')+'\n'+json.dumps(b,ensure_ascii=False,indent=2) for b in p['beats'] if isinstance(b,dict)),encoding='utf8')


