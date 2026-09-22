"""Validate generated pages, metadata, internal destinations and sitemap."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from collections import Counter,deque
import json,xml.etree.ElementTree as ET
ROOT=Path(__file__).parent/'dist'
ORIGIN=json.loads((Path(__file__).parent/'site_config.json').read_text(encoding='utf-8'))['origin']
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.meta={};self.canonical=[];self.h1=0;self.links=[];self.ids=[];self.images=[];self.schemas=[];self.capture=None;self.buf='';self.title='';self.feed(text)
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t=='meta':self.meta[a.get('name',a.get('property'))]=a.get('content','')
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if t=='a':self.links.append(a.get('href',''))
  if t=='h1':self.h1+=1
  if t=='img':self.images.append(a)
  if t=='title' or (t=='script' and a.get('type')=='application/ld+json'):self.capture=t;self.buf=''
 def handle_data(self,d):
  if self.capture:self.buf+=d
 def handle_endtag(self,t):
  if t==self.capture:
   if t=='title':self.title=self.buf
   else:self.schemas.append(json.loads(self.buf))
   self.capture=None
pages={}
for f in ROOT.rglob('index.html'):
 path='/'+str(f.relative_to(ROOT)).removesuffix('index.html');pages[path]=Page(f.read_text())
for path,p in pages.items():
 assert p.h1==1,(path,'h1')
 assert p.canonical==[ORIGIN+path],(path,'canonical')
 assert p.title and p.meta.get('description'),path
 assert len(p.ids)==len(set(p.ids)),(path,'duplicate ids')
 assert any(x.get('@type')=='WebPage' for x in p.schemas[0]['@graph']),path
 for img in p.images:
  assert img.get('alt') and img.get('width') and img.get('height'),(path,'image')
 for link in p.links:
  if link.startswith('/') and not link.startswith('//'):
   target=unquote(urlsplit(link).path)
   assert target in pages or (ROOT/target.lstrip('/')).is_file(),(path,target)
for attr in ['title','description']:
 vals=Counter(p.title if attr=='title' else p.meta['description'] for p in pages.values())
 assert max(vals.values())==1,(attr,'duplicates')
urls=[x.text for x in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls)==len(set(urls))
expected={ORIGIN+path for path,p in pages.items() if not p.meta['robots'].startswith('noindex')}
assert set(urls)==expected
seen={'/'};queue=deque(['/'])
while queue:
 for link in pages[queue.popleft()].links:
  path=urlsplit(link).path
  if path in pages and path not in seen:seen.add(path);queue.append(path)
assert all(url.removeprefix(ORIGIN) in seen for url in urls),'orphaned indexable page'
print(json.dumps({'pages_checked':len(pages),'sitemap_urls':len(urls),'broken_internal_links':0,'duplicate_titles':0,'duplicate_descriptions':0,'orphaned_indexable_pages':0,'single_h1_and_canonical':True,'structured_data_json':'valid','public_access':'Not checked here; requires Sites access verification','ranking_and_core_web_vitals':'Not measured'},ensure_ascii=False))
