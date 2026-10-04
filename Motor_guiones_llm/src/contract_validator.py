import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
from src.common import *
def validate(p,request,c):
 errors=[]
 def require(ok,message):
  if not ok:errors.append(message)
 if not isinstance(p,dict):return ['Package must be JSON object']
 require(p.get('episode_id')==request['episode_id'],'Episode mismatch')
 sel=request['seed_selection'];require(p.get('seed_id')==sel['seed']['seed_id'],'Seed mismatch');require(p.get('bank_version')==sel['bank_version'],'Bank version mismatch')
 require(p.get('seed_hash')==sel['seed_hash'],'Seed snapshot hash mismatch')
 require(p.get('seed_snapshot')==sel['seed'],'Seed snapshot changed')
 for k in ['title','central_conflict','payoff','share_recipient','novelty_justification']:
  require(isinstance(p.get(k),str) and bool(p[k].strip()),'Missing '+k)
 hooks=p.get('hooks',[]);require(isinstance(hooks,list) and len(hooks)==3,'Exactly 3 hooks required')
 if isinstance(hooks,list):
  for h in hooks:require(isinstance(h,dict) and all(isinstance(h.get(k),str) and h[k].strip() for k in ['id','text','reason']),'Hook needs id text reason')
  ids=[h.get('id') for h in hooks if isinstance(h,dict)];require(len(set(ids))==len(ids),'Duplicate hook IDs');require(p.get('selected_hook_id') in ids,'Selected hook absent')
 beats=p.get('beats',[]);require(isinstance(beats,list) and len(beats)>=4,'At least 4 beats required')
 all_ids=[];words=0
 worlds=request['context']['worlds']['worlds']
 if isinstance(beats,list):
  for i,b in enumerate(beats):
   if not isinstance(b,dict):errors.append('Beat must be object');continue
   all_ids.append(b.get('beat_id'));tag=f'Beat {i+1}: '
   for k in ['beat_id','function','narration','new_information','visual_action','voice_intention','text_emphasis','narration_visual_link']:
    require(isinstance(b.get(k),str) and bool(b[k].strip()),tag+'missing '+k)
   text=b.get('narration','');words+=len(str(text).split())
   require(not re.search(r'\[|<break',str(text)),tag+'Narration must be clean text; voice tags belong to voice engine')
   require(b.get('world_id') in worlds,tag+'unknown world')
   chars=b.get('characters');require(isinstance(chars,list) and bool(chars),tag+'characters required')
   shot=b.get('shot',{});require(isinstance(shot,dict),tag+'shot object required')
   if isinstance(shot,dict):
    require(shot.get('scale') in request['context']['canon']['shot_scales'],tag+'unknown shot scale')
    require(shot.get('motion') in ['push_in','pull_out','pan','still','reveal','parallax'],tag+'unknown motion')
    require(isinstance(shot.get('motion_reason'),str) and bool(shot['motion_reason'].strip()),tag+'motion motivation required')
    require(isinstance(shot.get('continuity'),str) and bool(shot['continuity'].strip()),tag+'continuity required')
    require(shot.get('subtitle_safe_top') is True,tag+'top subtitle safe area required')
   trans=b.get('transition',{});require(isinstance(trans,dict),tag+'transition required')
   if isinstance(trans,dict):
    require(trans.get('type') in ['cut','match_cut','dissolve','motivated_blur'],tag+'unknown transition')
    d=trans.get('duration_s');require(isinstance(d,(int,float)) and not isinstance(d,bool) and math.isfinite(d) and 0<=d<=.6,tag+'transition duration invalid')
    require(bool(trans.get('reason')),tag+'transition motivation missing')
    if trans.get('type')=='cut':require(d==0,tag+'cut must have zero overlap')
   pause=b.get('pause_after_s',0);require(isinstance(pause,(int,float)) and not isinstance(pause,bool) and math.isfinite(pause) and 0<=pause<=1,tag+'pause target invalid')
  require(len(all_ids)==len(set(all_ids)) and all(all_ids),'Duplicate/missing beat IDs')
  narr=[b.get('narration') for b in beats if isinstance(b,dict)];require(len(narr)==len(set(narr)),'Repeated narration')
  if hooks and beats and isinstance(beats[0],dict):
   selected=next((h for h in hooks if isinstance(h,dict) and h.get('id')==p.get('selected_hook_id')),None)
   if selected:require(beats[0].get('narration')==selected['text'],'First beat must use selected hook')
 require(p.get('music') is False and p.get('sfx') is False,'Music/SFX must be disabled')
 require(words>0,'Empty narration')
 return errors


