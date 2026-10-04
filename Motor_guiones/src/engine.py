import argparse,copy,hashlib,json,math,pathlib,re,subprocess,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from src.common import *
from src.request_builder import prepare
from src.creative_qc import finalize
from src.exporter import export
from src.orchestrator import run
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--config');sub=ap.add_subparsers(dest='op',required=True)
 for name in ['prepare','run']:
  a=sub.add_parser(name);a.add_argument('--episode',required=True);a.add_argument('--seed');a.add_argument('--topic',default='');a.add_argument('--history');a.add_argument('--out',required=True)
 a=sub.add_parser('check');a.add_argument('--request',required=True);a.add_argument('--candidate',required=True);a.add_argument('--critic');a.add_argument('--out',required=True)
 args=ap.parse_args();c=config(args.config)
 try:
  if args.op in ['prepare','run']:
   req=prepare(c,args.episode,args.seed,args.topic,read(args.history) if args.history else [])
   if args.op=='prepare':write(args.out,req);print('REQUEST_READY');return
   qc=run(req,c,args.out)
  else:
   req=read(args.request);qc,p=finalize(read(args.candidate),req,c,read(args.critic) if args.critic else None);export(args.out,p,qc)
  print(qc['status']);sys.exit(0 if qc['status']=='SCRIPT_APPROVED' else 2)
 except (ValueError,RuntimeError,subprocess.TimeoutExpired,OSError) as e:print(str(e),file=sys.stderr);sys.exit(3)


if __name__=='__main__':main()
