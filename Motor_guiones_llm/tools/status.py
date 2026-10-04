import json,pathlib,sys,time
folder=pathlib.Path(sys.argv[1]).resolve()
p=folder/'script_progress.json'
if not p.exists():raise SystemExit('NO_PROGRESS_RECORDED')
d=json.loads(p.read_text(encoding='utf8'))
for role,row in d['roles'].items():
 age=round(time.time()-row['updated_unix_s'],1)
 print(role,row['status'],'elapsed_ms='+str(row.get('elapsed_ms','pending')),'seconds_since_update='+str(age))
print('Recorded state does not prove a process is still alive.')
