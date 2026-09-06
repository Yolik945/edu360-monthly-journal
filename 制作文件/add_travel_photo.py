import json, shutil, hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
backup=R/'制作文件/补图前备份';backup.mkdir(exist_ok=True)
for rel in ['制作文件/source.json','制作文件/build_magazine.py','制作文件/v2/content.py','制作文件/v2/build_print.py']:
 p=R/rel;dest=backup/p.name
 if not dest.exists():shutil.copy2(p,dest)
qa=R/'制作文件/v2/qa'
manifest=backup/'v2-section-hashes.json'
if not manifest.exists():manifest.write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in qa.glob('*.png')},indent=2),encoding='utf8')
shutil.copy2('C:/Users/ADMINI~1/AppData/Local/Temp/codex-clipboard-0aca7c24-75df-432e-a664-ab8c697693a1.jpg',R/'制作文件/photos/image110.jpeg')
p=R/'制作文件/source.json';s=json.loads(p.read_text(encoding='utf8'))
if not any(x['file']=='image110.jpeg' for x in s['photos']):s['photos'].append({'file':'image110.jpeg','size':[1280,1920],'source':'用户补充照片：山海板块第二张'})
p.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'制作文件/v2/content.py';s=p.read_text(encoding='utf8').replace('76,list(range(76,96))','76,[76,110,*range(77,96)]').replace('[76,77,79,80,83]','[76,110,77,79,80,83]').replace('range(1,110)','range(1,111)').replace('109 source photos','110 photos (109 document + 1 supplied)');p.write_text(s,encoding='utf8')
p=R/'制作文件/v2/build_print.py';s=p.read_text(encoding='utf8').replace("s='<div class=\"kicker\">TRAVEL NOTES", "s=im(110,style='width:740px;height:1110px;margin:0 auto 48px')+'<div class=\"kicker\">TRAVEL NOTES").replace('range(1,110)','range(1,111)').replace('109/109','110/110');p.write_text(s,encoding='utf8')
p=R/'制作文件/build_magazine.py';s=p.read_text(encoding='utf8')
old="p+=stage(1810,pic(76,0,0,970,556),pic(77,0,610,605,342)"
new="p+=stage(620,pic(76,0,0,970,556))\np+=stage(1190,pic(110,100,0,740,1110,rot=-2,frame=True),label('把夏天，留在风里',535,1060,3,'blue'))\np+=stage(1200,pic(77,0,0,605,342)"
assert old in s;s=s.replace(old,new)
for a,b in [('pic(79,650,610','pic(79,650,0'),('pic(80,0,1020','pic(80,0,410'),('pic(83,330,1050','pic(83,330,440'),('top:1190px;width:180px','top:580px;width:180px'),("440,1670,-4,'blue'","440,1060,-4,'blue'")]:s=s.replace(a,b)
p.write_text(s,encoding='utf8')
print('Added image110 as second travel photo in both print layouts and shared chapter data.')
