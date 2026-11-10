"""Offline structural/public-boundary checks. Not behavioral or runtime certification."""
from pathlib import Path
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
TOP={'README.md','LICENSE','PRIVACY.md','SECURITY.md','SUBMISSION.md','VALIDATION.md','.gitignore','plugin.json'}
PREFIXES=('skills/game-production-handbook/','assets/','tools/','tests/','docs/','.agents/plugins/','.github/workflows/')
def files():
 return sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts and 'dist' not in p.relative_to(ROOT).parts and '__pycache__' not in p.parts)
def local(value,owner=ROOT):
 assert not re.match(r'^[a-z]+:',value),value
 p=(owner/value).resolve();assert p.is_relative_to(ROOT),value;assert p.is_file(),value;assert not p.is_symlink(),value;return p
manifest=json.loads((ROOT/'plugin.json').read_text());assert manifest['$schema']=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',manifest['name']);assert re.fullmatch(r'\d+\.\d+\.\d+',manifest['version']);assert manifest['license']=='MIT';assert manifest['author']['name']
assert 'mcpServers' not in manifest and not (ROOT/'mcp.json').exists() and not (ROOT/'hooks').exists()
interface=manifest['extensions']['com.openai']['interface']
for k,limit in [('displayName',30),('shortDescription',30),('longDescription',4000),('developerName',80)]:assert 0<len(interface[k])<=limit,(k,len(interface[k]))
assert len(interface['defaultPrompt'])<=3 and all(len(s)<=128 for s in interface['defaultPrompt'])
for k in ['composerIcon','logo']:
 assert interface[k].startswith('./');p=local(interface[k]);assert p.stat().st_size<=5*1024**2;svg=ET.fromstring(p.read_text());w=float(svg.attrib['width']);h=float(svg.attrib['height']);assert w==h and w>=48
market=json.loads((ROOT/'.agents/plugins/marketplace.json').read_text());assert market['plugins'][0]['name']==manifest['name'];entry=market['plugins'][0];assert entry['source']=={'source':'local','path':'./'};assert entry['policy']['installation']=='AVAILABLE' and entry['policy']['authentication']=='ON_INSTALL'
skills=list((ROOT/'skills').glob('*/SKILL.md'));assert len(skills)==1
for p in skills:
 text=p.read_text();assert text.startswith('---\n');front=text.split('---',2)[1];assert re.search(r'^name: [a-z0-9-]+$',front,re.M);assert re.search(r'^description: .+',front,re.M);assert '2D' in front
links=0
for p in files():
 rel=p.relative_to(ROOT).as_posix();assert rel in TOP or rel.startswith(PREFIXES),rel;assert not p.is_symlink(),rel
 # SVG/text source only; no archives, binaries or game asset payloads.
 assert p.suffix.lower() not in {'.zip','.mp4','.webm','.png','.webp','.jpg','.sqlite','.db'},rel
 text=p.read_text()
 for pattern in [r'/Users/',r'C:\\Users\\',r'-----BEGIN .*PRIVATE KEY-----',r'gh[pousr]_[A-Za-z0-9]{20,}',r'sk-[A-Za-z0-9_-]{24,}']:
  # Patterns themselves are permitted only in this validator, not in the payload.
  if rel=='tools/validate.py':continue
  assert not re.search(pattern,text),('private material/secret pattern',rel)
 if p.suffix=='.md':
  for target in re.findall(r'\]\(([^)]+)\)',text):
   if re.match(r'^[a-z]+:',target):continue
   target=target.split('#')[0]
   if not target:continue
   from urllib.parse import unquote
   local(unquote(target),p.parent);links+=1
print(json.dumps({'status':'passed','scope':'offline structure, local links and public-boundary scan only','files':len(files()),'skills':len(skills),'localLinks':links,'version':manifest['version']}))
