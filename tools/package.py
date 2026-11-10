"""Build a skills-only plugin ZIP from an explicit payload allowlist."""
from pathlib import Path
import subprocess,sys,json,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'tools/validate.py')],check=True,cwd=ROOT)
m=json.loads((ROOT/'plugin.json').read_text());dest=ROOT/'dist';dest.mkdir(exist_ok=True);archive=dest/(m['name']+'-'+m['version']+'.zip')
# Include the complete audited public tree so packaged documentation and manual
# validation commands remain usable. No scripts run automatically on install.
from validate import files
payload=files()
payload=sorted(payload,key=lambda p:p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in payload:
  info=zipfile.ZipInfo(p.relative_to(ROOT).as_posix(),date_time=(2026,11,11,0,0,0));info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,p.read_bytes())
sha=lambda b:hashlib.sha256(b).hexdigest()
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
 assert 'plugin.json' in z.namelist()
 assert 'tools/validate.py' in z.namelist() and 'docs/README.ko.md' in z.namelist()
 for p in payload:assert z.read(p.relative_to(ROOT).as_posix())==p.read_bytes()
# Re-run checks against the actual extracted ZIP, not just the source tree.
import tempfile
with tempfile.TemporaryDirectory(prefix='2d-rpg-plugin-check-') as temp:
 with zipfile.ZipFile(archive) as z:z.extractall(temp)
 subprocess.run([sys.executable,str(Path(temp)/'tools/validate.py')],check=True,cwd=temp)
receipt={'version':m['version'],'zip':archive.name,'bytes':archive.stat().st_size,'sha256':sha(archive.read_bytes()),'files':{p.relative_to(ROOT).as_posix():sha(p.read_bytes()) for p in payload},'crc':'passed','allArchivedBytesMatch':True,'scope':'No .git, private profile, original game, hooks, MCP, credentials or generation tools included'}
(dest/(archive.name+'.sha256')).write_text(receipt['sha256']+'  '+archive.name+'\n')
(dest/(archive.stem+'.manifest.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='files'},ensure_ascii=False,indent=2))
