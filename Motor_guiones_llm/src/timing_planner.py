import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
from src.common import *
def timing(p,c):
 p=copy.deepcopy(p);cursor=0;shots=[]
 for i,b in enumerate(p['beats']):
  duration=len(b['narration'].split())/c['words_per_second_estimate']+b.get('pause_after_s',0)
  limit=c['max_shot_s'];n=1 if i==0 and c['first_shot_exception'] else max(1,math.ceil(duration/limit))
  b['estimated_start_s']=round(cursor,3);b['estimated_end_s']=round(cursor+duration,3)
  for j in range(n):shots.append({'shot_id':b['beat_id']+f'-SH{j+1:02d}','beat_id':b['beat_id'],'estimated_start_s':round(cursor+j*duration/n,3),'estimated_end_s':round(cursor+(j+1)*duration/n,3),'composition_source':b['beat_id'],'requires_subshot_direction':n>1})
  cursor+=duration
 p['timing']={'status':'ESTIMATED_NOT_AUDIO_ALIGNED','duration_s':round(cursor,3),'words_per_second_estimate':c['words_per_second_estimate'],'shots':shots,'transition_policy':'Beat durations include transitions; dissolve windows overlap neighboring footage without shortening narration. Render must resolve exact windows after voice alignment.'}
 return p


