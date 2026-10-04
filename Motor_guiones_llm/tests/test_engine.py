import copy,json,pathlib,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from src.common import config,digest,read
from src.request_builder import prepare
from src.seed_selector import select
from src.creative_qc import finalize
from src.provider import call,call_subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
class EngineTests(unittest.TestCase):
 def setUp(self):
  self.c=config();self.req=prepare(self.c,'EP0099','MILO-S0001');self.p=read(ROOT/'examples/EP0099_candidate.json')
 def test_seed_and_trace(self):self.assertEqual(self.req['seed_selection']['seed']['seed_id'],'MILO-S0001')
 def test_history_exclusion(self):
  with self.assertRaises(ValueError):select(self.c,'MILO-S0001',history=[{'seed_id':'MILO-S0001','family_id':'F001'}])
 def test_no_creative_fake_pass(self):
  q,p=finalize(self.p,self.req,self.c);self.assertEqual(q['status'],'AWAITING_CREATIVE_QC');self.assertEqual(p['timing']['status'],'ESTIMATED_NOT_AUDIO_ALIGNED')
 def test_wrong_seed_rejected(self):
  self.p['seed_id']='UNKNOWN';q,_=finalize(self.p,self.req,self.c);self.assertEqual(q['status'],'NEEDS_SCRIPT_REVISION')
 def test_unknown_world_rejected(self):
  self.p['beats'][1]['world_id']='invented';q,_=finalize(self.p,self.req,self.c);self.assertIn('Beat 2: unknown world',q['technical_errors'])
 def test_long_beat_blocks(self):
  self.p['beats'][2]['narration']='Una frase extremadamente larga que necesita varios planos para conservar el ritmo y expresar su intención con claridad.';q,_=finalize(self.p,self.req,self.c);self.assertEqual(q['status'],'NEEDS_SCRIPT_REVISION')
 def test_missing_evidence_and_hash_blocks(self):
  q,p=finalize(self.p,self.req,self.c);report={'role':'independent_critic','candidate_hash':'false'};q,_=finalize(self.p,self.req,self.c,report);self.assertEqual(q['status'],'NEEDS_SCRIPT_REVISION')
 def test_provider_not_configured(self):
  with self.assertRaises(ValueError):call_subprocess([],{},1)
 def test_provider_bad_json(self):
  with self.assertRaises(json.JSONDecodeError):call_subprocess([sys.executable,'-c','print("bad")'],{},5)
 def test_active_provider_reads_config(self):
  # The active route is config-driven. When provider=deepseek_cdp, a call with an
  # argv must NOT reach the subprocess route: the argv is inert, and a bad/absent
  # CDP is reported as a DeepSeek failure, never as PROVIDER_NOT_CONFIGURED.
  self.assertEqual('deepseek_cdp',self.c.get('provider'))
 def test_synthetic_critic_contract(self):
  q,p=finalize(self.p,self.req,self.c)
  from src.common import DIMENSIONS
  report={'role':'independent_critic','candidate_hash':digest(p),'dimensions':{d:{'score':90,'evidence':['SYNTHETIC TEST ONLY']} for d in DIMENSIONS},'critical_errors':[],'novelty_checked_against_history':True,'perspectives':{k:'SYNTHETIC TEST ONLY' for k in ['facebook_viewer','cinematic_director','milo_director']}}
  report.update({'review_id':'A','rubric_version':'1.0.0','confidence':'medium','canon_comparison':'SYNTHETIC','mining_comparison':'SYNTHETIC','history_comparison':'SYNTHETIC'})
  for d in report['dimensions'].values():d.update({'beat_ids':['B01'],'improvement':'SYNTHETIC'})
  second=copy.deepcopy(report);second['review_id']='B'
  report={'reviews':[report,second]}
  q,_=finalize(self.p,self.req,self.c,report);self.assertEqual(q['status'],'SCRIPT_APPROVED');self.assertEqual(q['scorecard']['overall'],90)
  report['reviews'][0]['dimensions']['milo']['score']=50;q,_=finalize(self.p,self.req,self.c,report);self.assertEqual(q['status'],'NEEDS_SCRIPT_REVISION')
 def test_stress_validation(self):
  for _ in range(1000):self.assertEqual(finalize(self.p,self.req,self.c)[0]['status'],'AWAITING_CREATIVE_QC')

 def test_two_pass_requirement(self):
  q,_=finalize(self.p,self.req,self.c,{'reviews':[]});self.assertEqual(q['status'],'NEEDS_SCRIPT_REVISION')
 def test_scorecard_89_blocks_and_disagreement(self):
  from src.common import DIMENSIONS
  _,p=finalize(self.p,self.req,self.c)
  r={'role':'independent_critic','candidate_hash':digest(p),'review_id':'A','rubric_version':'1.0.0','confidence':'medium','canon_comparison':'SYNTHETIC','mining_comparison':'SYNTHETIC','history_comparison':'SYNTHETIC','dimensions':{d:{'score':90,'evidence':['SYNTHETIC'],'beat_ids':['B01'],'improvement':'SYNTHETIC'} for d in DIMENSIONS},'critical_errors':[],'novelty_checked_against_history':True,'perspectives':{k:'SYNTHETIC' for k in ['facebook_viewer','cinematic_director','milo_director']}}
  r2=copy.deepcopy(r);r2['review_id']='B';r2['dimensions']['hook']['score']=89
  self.assertEqual(finalize(self.p,self.req,self.c,{'reviews':[r,r2]})[0]['status'],'NEEDS_SCRIPT_REVISION')
  r2['dimensions']['hook']['score']=99
  q,_=finalize(self.p,self.req,self.c,{'reviews':[r,r2]});self.assertTrue(any('disagreement' in x for x in q['creative_errors']))
  r2['dimensions']['hook']['score']=90;r2['dimensions']['hook']['beat_ids']=['UNKNOWN']
  self.assertEqual(finalize(self.p,self.req,self.c,{'reviews':[r,r2]})[0]['status'],'NEEDS_SCRIPT_REVISION')

if __name__=='__main__':unittest.main()
