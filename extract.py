from zipfile import ZipFile
from lxml import etree
from pathlib import Path
import json
from PIL import Image,ImageOps,ImageDraw,ImageFont
base=Path.cwd(); out=base/'制作文件'; out.mkdir(exist_ok=True); assets=out/'photos'; assets.mkdir(exist_ok=True)
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
with ZipFile(base/'夏季刊.docx') as z:
 rels={r.get('Id'):r.get('Target') for r in etree.fromstring(z.read('word/_rels/document.xml.rels'))}
 root=etree.fromstring(z.read('word/document.xml'))
 rows=[]
 for i,p in enumerate(root.xpath('//w:body//w:p',namespaces=ns)):
  txt=''.join(p.xpath('.//w:t/text()',namespaces=ns))
  imgs=[rels[x] for x in p.xpath('.//a:blip/@r:embed',namespaces=ns)]
  if txt or imgs: rows.append({'paragraph':i,'text':txt,'images':imgs})
 photos=[]
 for n in z.namelist():
  if n.startswith('word/media/'):
   path=assets/Path(n).name; path.write_bytes(z.read(n))
   try:
    im=Image.open(path); photos.append({'file':path.name,'size':im.size})
   except: pass
 (out/'source.json').write_text(json.dumps({'paragraphs':rows,'photos':photos},ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'paragraphs':rows,'photos':photos},ensure_ascii=False,indent=2))
 font=ImageFont.truetype('C:/Windows/Fonts/msyh.ttc',18)
 photos.sort(key=lambda p:int(p["file"].split(".")[0][5:]))
 for start in range(0,len(photos),20):
  subset=photos[start:start+20]; sheet=Image.new('RGB',(1200,280*((len(subset)+3)//4)),'#eeeeee'); d=ImageDraw.Draw(sheet)
  for j,p in enumerate(subset):
   im=ImageOps.exif_transpose(Image.open(assets/p['file'])).convert('RGB'); im.thumbnail((286,240))
   x=(j%4)*300;y=(j//4)*280;sheet.paste(im,(x+(300-im.width)//2,y))
   d.text((x+8,y+245),p['file']+' '+str(p['size']),font=font,fill='black')
  sheet.save(out/f'contact-{start//20+1}.jpg')

