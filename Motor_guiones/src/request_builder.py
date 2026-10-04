import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
from src.common import *
from src.seed_selector import select
def prepare(c,episode,seed_id=None,topic='',history=None):
 if not re.fullmatch(r'EP\d{4}',episode):raise ValueError('Episode must match EP0001')
 selected=select(c,seed_id,topic,history);ctx=context(c)
 return {'request_version':'1.0.0','episode_id':episode,'seed_selection':selected,'context':ctx,'history':history or [],'constraints':{k:c[k] for k in ['max_shot_s','first_shot_exception','max_duration_s','music','sfx']},'instructions':(ROOT/'prompts/writer.md').read_text(encoding='utf8'),'previous_candidate':None,'revision_feedback':None}


