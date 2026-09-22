"""Static release checks. Does not replace live headers or penetration testing."""
from html.parser import HTMLParser
from pathlib import Path
from security_policy import CSP, HEADERS
import json,re
root=Path(__file__).parent/'dist'
class Check(HTMLParser):
 def __init__(self):super().__init__();self.policy=False
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  assert not any(k.lower().startswith('on') for k in a),'inline handler'
  assert 'style' not in a,'inline style'
  if t=='meta' and a.get('http-equiv')=='Content-Security-Policy':assert a['content']==CSP;self.policy=True
  if t=='script':
   assert a.get('src')=='/app.js' or a.get('type') in ('application/json','application/ld+json'),'unexpected script'
  if t in ('iframe','object','embed','base'):raise AssertionError('unexpected embedded resource')
  if t=='form':assert a.get('action','').startswith('/') and not a['action'].startswith('//')
  if t in ('script','img') and 'src' in a:assert a['src'].startswith('/') and not a['src'].startswith('//')
for p in root.rglob('*.html'):
 c=Check();c.feed(p.read_text());assert c.policy,p
assert (root/'_headers').read_text()==HEADERS
for p in root.rglob('*'):
 if p.is_file():
  assert not any(x.startswith('.') for x in p.relative_to(root).parts),p
  assert p.suffix in ('.html','.css','.js','.webp','.svg','.xml','.txt',''),p
  if p.suffix in ('.html','.js','.css'):
   data=p.read_text();assert not re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bsk-[A-Za-z0-9]{32,}',data),'possible secret'
js=(root/'app.js').read_text()
assert not any(s in js for s in ('innerHTML','document.write','eval(','new Function('))
print('PASS: all HTML pages have CSP; no inline handlers, unexpected executable scripts, remote images/scripts, secret patterns or source files in public output.')
