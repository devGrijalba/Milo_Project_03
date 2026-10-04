"""Script-only acceptance. No media stages; original request remains unchanged."""
import argparse,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from src.common import read,config
from src.orchestrator import run
p=argparse.ArgumentParser();p.add_argument('--request',required=True);p.add_argument('--out',required=True);a=p.parse_args()
request_path=pathlib.Path(a.request).resolve();out=pathlib.Path(a.out).resolve()
if request_path.parent==out:raise SystemExit('USE_SEPARATE_SCRIPT_REVISION_FOLDER')
r=run(read(request_path),config(),out);print(json.dumps(r,ensure_ascii=False,indent=2));sys.exit(0 if r['status']=='SCRIPT_APPROVED' else 2)
