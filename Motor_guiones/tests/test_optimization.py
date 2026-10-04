import unittest,pathlib,tempfile,copy,json,sys
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src import multiagent as ma,provider,orchestrator as o,runtime
from src.common import read,config,digest,DIMENSIONS
from src.request_builder import prepare
class Optimization(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.f=pathlib.Path(self.tmp.name)
  self.c=config();self.req=prepare(self.c,'EP0099','MILO-S0001');self.cand=read(ROOT/'examples/EP0099_candidate.json');self.base=ma.base_package(self.req)
  for role,key,_ in ma.SPECIALISTS:self.c[key]=['fake',role]
  self.c['synthesizer_command']=['fake','synth'];self.c['critic_command']=['fake','critic']
 def report(self,p,score=96):
  row={'review_id':p['review_pass_id'],'role':'independent_critic','candidate_hash':p['candidate_hash'],'rubric_version':'1.0.0','confidence':'high','critical_errors':[],'novelty_checked_against_history':True,'canon_comparison':'SYNTHETIC','mining_comparison':'SYNTHETIC','history_comparison':'SYNTHETIC','perspectives':{k:'SYNTHETIC' for k in ['facebook_viewer','cinematic_director','milo_director']},'dimensions':{k:{'score':score,'evidence':['SYNTHETIC'],'beat_ids':['B01'],'improvement':'none'} for k in DIMENSIONS}}
  return {'reviews':[row]}
 def test_actual_synthesis_payload_passes_guard(self):
  def fake(cmd,p,t,role=None):
   self.assertEqual(provider.validate_payload(role,p),[]);return self.cand
  with patch.object(ma,'call',fake):ma.synthesize(self.c,self.base,{name:{'role':name} for name,_,_ in ma.SPECIALISTS},30)
 def test_scoped_context_preserves_canon_seed(self):
  scoped=ma.scoped_base(self.base,'script_hook_specialist')
  self.assertEqual(scoped['seed_snapshot'],self.base['seed_snapshot']);self.assertEqual(scoped['context']['canon'],self.base['context']['canon']);self.assertLess(len(json.dumps(scoped)),len(json.dumps(self.base))*.6)
  self.assertEqual(self.base['context']['mining'],self.req['context']['mining'])
 def test_complete_pipeline_and_cache(self):
  calls=[]
  def fake(cmd,p,t,role=None):
   self.assertEqual(provider.validate_payload(role,p),[]);calls.append(role)
   if role=='script_synthesizer':return copy.deepcopy(self.cand)
   if role=='script_critic':return self.report(p)
   return {'role':role,'proposals':['bounded'],'evidence':[],'risks':[],'handoff':'ok'}
  with patch.object(ma,'call',fake),patch.object(o,'call',fake):
   self.assertEqual(o.run(self.req,self.c,self.f)['status'],'SCRIPT_APPROVED');self.assertEqual(len(calls),7)
   self.assertEqual(o.run(self.req,self.c,self.f)['status'],'SCRIPT_APPROVED');self.assertEqual(len(calls),7)
  self.assertFalse((self.f/'script_optimization.lock').exists());self.assertEqual(read(self.f/'script_progress.json')['roles']['orchestrator']['status'],'SCRIPT_APPROVED')
 def test_second_pass_only_separate_session(self):
  payloads=[]
  def fake(cmd,p,t,role=None):
   if role=='script_synthesizer':return copy.deepcopy(self.cand)
   if role=='script_critic':payloads.append(p);return self.report(p,91)
   return {'role':role}
  with patch.object(ma,'call',fake),patch.object(o,'call',fake):self.assertEqual(o.run(self.req,self.c,self.f)['status'],'SCRIPT_APPROVED')
  self.assertEqual(len(payloads),2);self.assertNotIn('reviews',payloads[1]);self.assertNotEqual(payloads[0]['review_pass_id'],payloads[1]['review_pass_id'])
 def test_no_unchanged_review_loop(self):
  count=[]
  def fake(cmd,p,t,role=None):
   if role=='script_synthesizer':return copy.deepcopy(self.cand)
   if role=='script_critic':
    count.append(role);r=self.report(p);r['reviews'][0]['dimensions']['visual']['score']=80;return r
   return {'role':role}
  with patch.object(ma,'call',fake),patch.object(o,'call',fake):r=o.run(self.req,self.c,self.f)
  self.assertEqual(len(count),1);self.assertEqual(r['status'],'NEEDS_SCRIPT_REVISION');self.assertIn('NO_APPLICABLE',r['optimization_block'])
 def test_partial_resume(self):
  calls=[];fail={'on':True}
  def fake(cmd,p,t,role=None):
   calls.append(role)
   if role=='script_structure_specialist' and fail['on']:raise ValueError('failure')
   return {'role':role}
  with patch.object(ma,'call',fake):
   with self.assertRaises(ma.ScriptStageBlocked):ma.parallel_specialists(self.c,self.base,30,folder=self.f)
   fail['on']=False;ma.parallel_specialists(self.c,self.base,30,folder=self.f)
  self.assertEqual(len(calls),6)
 def test_oversize_saved_and_blocked(self):
  with patch.object(ma,'call',lambda *a,**kw:{'text':'x'*9000}):
   with self.assertRaisesRegex(ma.ScriptStageBlocked,'TOO_LARGE'):ma.parallel_specialists(self.c,self.base,30,folder=self.f)
  self.assertTrue(list((self.f/'script_rejected_outputs').glob('*.json')))
 def test_cache_tamper_blocks(self):
  invoke=lambda *a,**kw:{'ok':True}
  runtime.cached_call(['x'],{'a':1},3,'role',self.f,invoke)
  p=next((self.f/'script_cache/role').glob('*.json'));d=read(p);d['result']={'ok':False};p.write_text(json.dumps(d))
  with self.assertRaisesRegex(ValueError,'TAMPERED'):runtime.cached_call(['x'],{'a':1},3,'role',self.f,invoke)
 def test_cache_input_change_calls_again(self):
  calls=[]
  def invoke(*a,**kw):calls.append(1);return {'ok':True}
  runtime.cached_call(['x'],{'a':1},3,'role',self.f,invoke);runtime.cached_call(['x'],{'a':2},3,'role',self.f,invoke);self.assertEqual(len(calls),2)
 def test_duplicate_review_response_blocks(self):
  with patch.object(o,'call',lambda *a,**kw:{'reviews':[{},{}]}):
   with self.assertRaisesRegex(ValueError,'ONE_REVIEW'):o._critic_once(self.c,self.req,self.cand,self.f,0,o._metrics(),30)
 def test_failure_progress_and_lock(self):
  with patch.object(ma,'call',side_effect=ValueError('offline blocked')):
   with self.assertRaises(ma.ScriptStageBlocked):o.run(self.req,self.c,self.f)
  self.assertFalse((self.f/'script_optimization.lock').exists());self.assertEqual(read(self.f/'script_failure.json')['status'],'SCRIPT_STAGE_BLOCKED')
if __name__=='__main__':unittest.main()
