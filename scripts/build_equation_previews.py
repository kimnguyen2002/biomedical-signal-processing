"""Export equation previews without requiring network requests from the reader."""
from pathlib import Path
import json,re,nbformat,yaml
ROOT=Path(__file__).resolve().parents[1];BOOK=ROOT/'book';data={}
toc=yaml.safe_load((BOOK/'_toc.yml').read_text())
files=set()
def collect(node):
 if isinstance(node,dict):
  if 'file' in node:files.add(node['file'])
  for v in node.values():collect(v)
 elif isinstance(node,list):
  for v in node:collect(v)
collect(toc)
for p in BOOK.rglob('*.ipynb'):
 if p.relative_to(BOOK).with_suffix('').as_posix() not in files:continue
 nb=nbformat.read(p,as_version=4);text='\n\n'.join(c.source for c in nb.cells if c.cell_type=='markdown');page=p.relative_to(BOOK).with_suffix('.html').as_posix()
 for m in re.finditer(r'\(eq-([\d-]+)\)=\s*\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}',text,re.S):
  data[page+'#eq-'+m.group(1)]={'tex':r'\begin{equation*}'+m.group(2)+r'\end{equation*}'}
 # A subsection reference previews its first displayed equation, when present.
 for m in re.finditer(r'\(sec-([\d-]+)\)=\n(.*?)(?=\n\(sec-|\Z)',text,re.S):
  eq=re.search(r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}|(?m:^\$\$\s*\n)(.*?)(?m:\n\$\$\s*$)',m.group(2),re.S)
  if eq:
   tex=eq.group(0)
   if tex.startswith('$$'):tex=tex.strip()[2:-2].strip()
   data[page+'#sec-'+m.group(1)]={'tex':tex}
(BOOK/'_static/equation-previews-data.js').write_text('window.BSP_EQUATION_PREVIEWS = '+json.dumps(data,ensure_ascii=False)+';\n')
print('Exported',len(data),'equation and subsection previews.')
