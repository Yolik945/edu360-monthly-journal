import json,html
from pathlib import Path
R=Path(__file__).resolve().parents[2];O=R/'成品/第二版';O.mkdir(exist_ok=True)
D=json.loads((R/'制作文件/v2/content.json').read_text(encoding='utf8'));S=json.loads((R/'制作文件/source.json').read_text(encoding='utf8'))
files={int(p['file'].split('.')[0][5:]):p['file'] for p in S['photos']};sizes={int(p['file'].split('.')[0][5:]):p['size'] for p in S['photos']};used=[]
def im(n,cls='',style='',cap=''):
 used.append(n)
 return f'<figure class="{cls}" style="{style}" data-photo="{n}"><img src="../../制作文件/photos/{files[n]}" alt="照片{n}">'+(f'<figcaption>{cap}</figcaption>' if cap else '')+'</figure>'
def row(ids,weights=None,cls='',heights=None):
 weights=weights or [1]*len(ids)
 return '<div class="photo-row '+cls+'" style="grid-template-columns:'+ ' '.join(str(x)+'fr' for x in weights)+'">'+''.join(im(n,style=(f'height:{heights[i]}px' if heights else '')) for i,n in enumerate(ids))+'</div>'
def head(i,large=False):
 d=D[i];title=d['title'].replace('\n','<br>')
 return f'<div class="chapter-head"><div class="eyebrow"><span>{d["kicker"]}</span><span>360 / SUMMER 2026</span></div><h2 class="{"huge" if large else ""}">{title}</h2><p class="lead">{d["desc"]}</p></div>'
def note(t,txt=''):
 return f'<div class="note"><h3>{t}</h3>'+(f'<p>{txt}</p>' if txt else '')+'</div>'
def sec(id,p,cls=''):return f'<section id="{id}" class="{cls}">{p}</section>'
css='''
*{box-sizing:border-box}html,body{margin:0;background:#d8dcd2;font-family:"Microsoft YaHei",Arial,sans-serif;color:#101514}main{width:1080px;overflow:hidden;background:#f8faf4;margin:auto}h1,h2,h3,p,figure{margin:0}section{padding:62px 50px 70px;position:relative}.ink{background:#101514;color:#f8faf4}.lime{background:#d6ff49}.blue{background:#2857ec;color:#fff}.gray{background:#e9ede4}.orange{background:#ff9068}.eyebrow{font:22px Arial,"Microsoft YaHei",sans-serif;display:flex;justify-content:space-between;letter-spacing:1px;font-weight:700}.chapter-head h2{font-size:84px;letter-spacing:-5px;line-height:1.13;margin:35px 0 30px;font-weight:900}.chapter-head h2.huge{font-size:115px;letter-spacing:-7px}.lead{font-size:32px;line-height:1.7;margin-bottom:35px}.chapter-head{margin-bottom:35px}figure{overflow:hidden;position:relative;background:#e3e7dd}figure img{width:100%;height:100%;display:block;object-fit:cover}figure.contain img{object-fit:contain}figcaption{background:#101514;color:#fff;font-size:22px;padding:15px 18px;line-height:1.5}.photo-row{display:grid;gap:12px;align-items:stretch;margin:18px 0}.photo-row figure{height:250px}.photo-row.tall figure{height:470px}.photo-row.medium figure{height:335px}.photo-row.auto{align-items:start}.photo-row.auto figure{height:auto;background:transparent}.photo-row.auto img{height:auto}.photo-row.auto figcaption{height:auto}.feature{width:1080px;margin:35px -50px 28px}.feature img{height:auto}.note{margin:33px 0 22px}.note h3{font-size:39px;font-weight:900;line-height:1.4;letter-spacing:-1px}.note p{font-size:30px;line-height:1.7;margin-top:12px}.mini{font-size:24px;line-height:1.65}.quote{font-size:46px;line-height:1.5;font-weight:700;letter-spacing:-1px}.quote cite{display:block;font-size:24px;font-style:normal;font-weight:400;margin-top:24px}.flex{display:flex;gap:35px;align-items:center;margin:35px 0}.flex>*{flex:1;min-width:0}.flex figure{height:530px}.slim{width:700px}.ruler{height:3px;background:currentColor;margin:35px 0}.kicker{font:22px Arial,"Microsoft YaHei";letter-spacing:2px;margin-bottom:16px}.group{padding:32px 0 28px;border-top:1px solid #10151444}.group-title{display:flex;align-items:center;gap:25px;margin-bottom:22px}.group-title b{font:84px Arial;font-weight:900;letter-spacing:-4px;color:#2857ec}.group-title h3{font-size:41px;line-height:1.3}.group-title span{display:block;font-size:26px;font-weight:500;margin-top:10px}.group>p{font-size:30px;line-height:1.7;margin-bottom:25px}.route{display:flex;gap:15px;flex-wrap:wrap;font-size:27px;line-height:1.6;padding:25px 0;border-top:2px solid;border-bottom:2px solid;margin:30px 0}.route b{font-weight:500}.route span{color:#2857ec}.fullword{font:150px Arial;font-weight:900;letter-spacing:-9px;line-height:.85;margin:25px 0;color:#d6ff49}.film{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:18px;background:#101514}.film figure{height:290px}.film .wide{grid-column:1/-1;height:520px}.film:before{content:'● FM / 海外专场';grid-column:1/-1;color:#d6ff49;font:22px Arial,"Microsoft YaHei";letter-spacing:3px;padding:5px 0 12px}.film:after{content:'360 EDUCATION ONLINE     /     CONVERSATIONS THAT CONNECT';grid-column:1/-1;color:#fff9;font:16px Arial;letter-spacing:1px;padding:8px 0 4px}.support-label{font-size:23px;letter-spacing:2px;margin-top:35px;padding-top:22px;border-top:1px solid #fff4}.stats{display:grid;grid-template-columns:1fr 1fr 1fr;padding:30px 0;border-top:2px solid;border-bottom:2px solid;margin:25px 0}.stats b{display:block;font:85px Arial;font-weight:900;letter-spacing:-4px}.stats span{font-size:27px}.kol-item{display:grid;grid-template-columns:230px 1fr;gap:25px;align-items:center;margin:38px 0}.kol-item figure img{height:auto}.kol-item h3{font-size:33px;line-height:1.4;margin-bottom:16px}.kol-item p{font-size:26px;line-height:1.7}.kol-item b{font:62px Arial;font-weight:900;display:block;margin-bottom:20px;color:#2857ec}.sport-grid{display:grid;grid-template-columns:245px 1fr;gap:20px}.sport-grid>.poster{height:530px;align-self:center}.sport-grid>.poster img{object-fit:contain}.sport-grid .photo-row figure{height:530px}.travel-head{padding:0;height:1400px;background:#101514;color:white}.travel-head figure{position:absolute;inset:0;height:1400px;background:#101514}.travel-head img{object-position:66% center}.travel-head:after{content:'';position:absolute;inset:0;background:linear-gradient(#061712bd,transparent 60%,#061712b8)}.travel-head .chapter-head{position:absolute;inset:60px 50px;z-index:2}.travel-head h2{font-size:139px;line-height:1.1;letter-spacing:-8px;margin-top:85px}.travel-head .lead{position:absolute;bottom:0;max-width:850px;color:white}.travel-label{font-size:82px;font-weight:900;line-height:1.12;letter-spacing:-4px;margin:35px 0}.photo-mosaic{display:grid;grid-template-columns:repeat(12,1fr);gap:14px;margin:22px 0}.photo-mosaic figure{min-width:0}.portrait-note{display:grid;grid-template-columns:repeat(2,1fr);gap:38px 30px;margin-top:35px}.person{border-top:2px solid #101514;padding-top:18px}.person figure{height:490px}.person h3{font-size:46px;margin:20px 0 10px}.person .role{font-size:25px;color:#38571d;line-height:1.65;min-height:78px}.person .bio{font-size:28px;line-height:1.7;margin-top:18px}.letter-grid{display:grid;grid-template-columns:1fr 1fr;gap:30px}.letter-grid figure{height:842px;background:transparent}.letter-grid img{object-fit:contain}.running{padding:24px 50px;background:#d6ff49;display:flex;justify-content:space-between;align-items:center;font-size:26px;letter-spacing:2px}.cover{height:1550px;padding:48px 50px;background:#101514;color:#fff}.cover .top{display:flex;justify-content:space-between;align-items:center;font-size:26px}.cover .brand{font-size:38px;font-weight:900}.cover .cover-photo{position:absolute;left:430px;top:215px;width:650px;height:835px}.cover .cover-photo img{object-position:58% 48%}.cover h1{position:relative;font-size:192px;letter-spacing:-12px;line-height:1.04;margin-top:120px;z-index:2;width:460px;font-weight:900}.cover h1 .outline{color:transparent;-webkit-text-stroke:2px white}.cover h1 .accent{color:#d6ff49}.cover .cover-photo2{position:absolute;left:465px;top:1000px;width:615px;height:345px;border:12px solid #101514;border-right:0}.cover .cover-note{position:absolute;left:50px;top:1010px;width:390px;font-size:29px;line-height:1.65}.cover .cover-note b{font-size:33px;color:#d6ff49;display:block;margin-bottom:25px}.cover .cover-foot{position:absolute;bottom:55px;left:50px;right:50px;display:flex;align-items:end;justify-content:space-between;border-top:1px solid #fff6;padding-top:30px}.cover .cover-foot b{font:62px Arial;font-weight:900;letter-spacing:-3px;line-height:1}.cover .cover-foot span{font-size:25px;line-height:1.7}.intro{padding:65px 50px}.intro h2{font-size:57px;line-height:1.4;font-weight:900;letter-spacing:-2px}.intro p{font-size:31px;line-height:1.75;margin-top:25px}.end{background:#d6ff49;padding:90px 50px}.end h2{font-size:108px;line-height:1.15;font-weight:900;letter-spacing:-6px}.end p{font-size:32px;line-height:1.8;margin-top:30px}.end .endline{font:150px Arial;font-weight:900;letter-spacing:-10px;margin-top:60px;border-bottom:3px solid;padding-bottom:35px}
'''
p=[]
p.append('<section class="cover" id="cover"><div class="top"><span class="brand">360教育在线</span><span>2026 夏季刊 / 集团季刊</span></div>'+im(7,'cover-photo')+'<h1>盛夏<br><span class="outline">我们</span><br><span class="accent">在场.</span></h1>'+im(77,'cover-photo2')+'<div class="cover-note"><b>融通中外<br>研途新篇</b>每一次奔赴，<br>都值得被记住。</div><div class="cover-foot"><b>OUR SUMMER,<br>TOGETHER.</b><span>院校之间，城市之间，<br>你我之间。</span></div></section>')
p.append('<section class="intro lime" id="intro"><div class="eyebrow"><span>卷首 / 这个夏天的我们</span><span>2026</span></div><h2 style="margin-top:35px">走进现场，看见彼此。</h2><p>从福州峰会到各地巡讲，从曼谷交流到镜头前的海外对话，我们持续连接院校与学子。也在一次次复盘、成长与相聚中，看见团队的力量。</p><p>致敬奔走在一线的你，感谢在幕后全力支撑的伙伴。一起翻开这份夏日记录。</p></section>')
# Summit: giant title, full event, spoken words and intimate production details.
s=head(0,True)+im(8,'feature',cap='第八届高校研究生招生工作交流会 / 福州')
s+='<div class="flex">'+im(7,style='height:415px')+'<div class="quote">“AI不仅是工具层面的革新，更是重塑招生逻辑、提升组织效能的核心引擎。”<cite>360教育在线创始人 付嘉</cite></div></div>'
s+=note('变革之声',D[0]['notes'][1]['text'])+row([6,9],[1.1,1],'medium')
s+=note('圆桌沙龙',D[0]['notes'][2]['text'])+im(10,'feature',cap='一次交流，让新的可能发生。')
s+='<div class="support-label">BACKSTAGE / 从准备到相聚</div><div class="photo-mosaic">'+im(1,style='grid-column:span 3;height:380px')+im(2,style='grid-column:span 5;height:380px')+im(4,style='grid-column:span 4;height:380px')+im(3,style='grid-column:span 6;height:360px')+im(5,style='grid-column:span 6;height:360px')+'</div>'
p.append(sec('summit',s,'ink'))
# Roadshow rhythm is directional and dense, with group photos protected at natural ratios.
s=head(1)+ '<div class="route"><b>长沙</b><span>→</span><b>广州</b><span>→</span><b>济南</b><span>→</span><b>杭州</b><span>→</span><b>南京</b><span>→</span><b>太原</b></div>'
for i,n in enumerate(D[1]['notes']):
 name=n['name'].split(' · ');s+=f'<div class="group"><div class="group-title"><b>0{i+1}</b><h3>{name[0]}<span>{name[1]}</span></h3></div><p>{n["text"]}</p>'
 if i==0:s+=row([12],[1],'auto')+row([11,13],[1.3,1],'medium')
 elif i==1:s+=row([15,18],[1,1],'auto')+row([16,14,17],[1.2,1,1],'medium')
 elif i==2:s+=row([20,22],[1,1],'auto')+row([19,21],[1,1],'tall')
 else:s+=im(25,'feature')+row([23,24],[1,1],'medium')
 s+='</div>'
p.append(sec('road',s))
s=head(2)+im(27,'feature')+'<div class="fullword">BKK → SHA</div>'+note(D[2]['notes'][0]['name'],D[2]['notes'][0]['text'])
s+='<div class="photo-mosaic">'+im(26,style='grid-column:span 4;height:535px')+im(28,style='grid-column:span 8;height:535px')+im(29,style='grid-column:span 12;height:430px')+'</div>'
s+=note(D[2]['notes'][1]['name'],D[2]['notes'][1]['text'])+im(30,'feature')+row([31,32,33],[1,1,1],'medium')
p.append(sec('global',s,'blue'))
s=head(3)+im(39,'feature')+note('相聚南京，让经验流动',D[3]['notes'][0]['text'])+row([34,35,36],[1.2,1,1],'medium')+row([37,38],[.65,1.35],'tall')
s+=note('把讨论落到下一步',D[3]['notes'][1]['text'])+row([40,41],[1,1],'medium')
s+='<div class="flex">'+im(42,style='height:400px')+'<div class="quote">把想法说出来。<br>把共识带回去。<br>把行动做下去。</div></div>'+row([43,44,45],[1,1,1],'tall')
s+=note('充电之后，再出发',D[3]['notes'][2]['text'])+row([46,47],[1.4,.65],'tall')+row([48,49],[1.1,1],'medium')
p.append(sec('reset',s,'gray'))
s=head(4)
for ids,n in zip([[52,50,51],[55,54,53],[57,56,58]],D[4]['notes']):
 s+=note(n['name'],n['text'])+'<div class="film">'+im(ids[0],'wide')+im(ids[1])+im(ids[2])+'</div>'
p.append(sec('air',s))
s=head(5)+'<div class="stats"><div><b>1,064</b><span>累计点赞</span></div><div><b>342</b><span>累计收藏</span></div><div><b>67</b><span>累计评论</span></div></div><p class="mini">按本期资料三条内容加总，非实时数据。</p>'
for i,n in enumerate(D[5]['notes']):s+='<div class="kol-item"><div><b>0'+str(i+1)+'</b><h3>'+n['name']+'</h3><p>'+n['text']+'</p></div>'+im(n['photos'][0])+'</div>'
p.append(sec('content',s,'lime'))
s=head(6)+im(65,'feature')+'<div class="flex"><div class="quote">保持好奇，<br>勇敢试试。<cite>找到属于自己的赛道。</cite></div>'+im(64,style='height:360px')+'</div>'+row([62,63],[1,1],'medium')+row([66],[1],'auto')
p.append(sec('grow',s))
s=head(7,True)+im(74,'feature')+'<div class="sport-grid">'+im(67,'poster')+'<div>'+row([68,69],[1,1],'tall')+'</div></div>'+row([70,71],[1,1],'medium')+im(73,'feature')+row([72,75],[1,1],'medium')+'<div class="fullword" style="color:#101514">READY? PLAY!</div>'
p.append(sec('play',s,'lime'))
p.append(sec('travel-opening',im(76)+head(8),'travel-head'))
s=im(110,style='width:740px;height:1110px;margin:0 auto 48px')+'<div class="kicker">TRAVEL NOTES / 城市之外</div>'+row([77],[1],'auto')+'<div class="photo-mosaic">'+im(79,style='grid-column:span 4;height:560px')+im(80,style='grid-column:span 4;height:560px')+im(83,style='grid-column:span 4;height:560px')+'</div>'
s+='<h3 class="travel-label">海风一吹，<br>快乐有了形状。</h3>'+im(81,'feature')+'<div class="photo-mosaic">'+im(78,style='grid-column:span 8;height:525px')+im(84,style='grid-column:span 4;height:525px')+im(82,style='grid-column:span 4;height:515px')+im(85,style='grid-column:span 8;height:515px')+'</div>'
s+='<h3 class="travel-label">向山野走去，<br>把视野再打开一点。</h3>'+im(86,'feature')+'<div class="photo-mosaic">'+im(89,style='grid-column:span 4;grid-row:span 2;height:740px')+im(87,style='grid-column:span 8;height:363px')+im(88,style='grid-column:span 8;height:363px')+'</div>'
s+=note('小小快乐，也值得被记住。')+row([90,91,92],[1,1,1],'tall')+row([93,94,95],[1,1,1],'tall')
p.append(sec('travel',s,'ink'))
s=head(9)+'<div class="photo-mosaic">'+im(96,style='grid-column:span 6;height:650px')+im(97,style='grid-column:span 6;height:650px')+'</div>'+note('01 / 定制水杯','桌面上、出差途中，记得好好喝水。')
s+='<div class="photo-row tall" style="grid-template-columns:1fr 1fr">'+im(98,style='height:720px')+im(99,style='height:720px')+'</div>'+note('02 / 定制包袋','通勤出门、周末出游，快乐随身携带。')
p.append(sec('goods',s,'orange'))
s=head(10)+'<div class="portrait-note">'
for n in D[10]['notes']:
 name,role=n['name'].split(' · ',1);s+='<article class="person">'+im(n['photos'][0],'contain' if n['photos'][0]==101 else '')+f'<h3>{name}</h3><p class="role">{role.replace(" · ","<br>")}</p><p class="bio">{n["text"]}</p></article>'
s+='</div>';p.append(sec('people',s))
s=head(11)+'<div class="letter-grid">'+''.join(im(n) for n in [106,107,108,109])+'</div>'
p.append(sec('warm',s,'gray'))
p.append('<section class="end" id="end"><div class="eyebrow"><span>卷尾 / UNTIL NEXT TIME</span><span>2026 SUMMER</span></div><h2 style="margin-top:55px">盛夏的故事，<br>未完待续。</h2><p>一路奔赴的脚步，全力以赴的日常，<br>汇成这个夏天被看见的360教育在线。</p><p>把夏日的热忱带向下一程。<br>时序向秋，我们下期再见。</p><div class="endline">SEE YOU ↗</div><p style="font-size:25px;text-align:right">360教育在线 · 行政中心</p></section>')
assert set(used)==set(range(1,111)),set(range(1,111))-set(used)
(O/'夏季刊_视觉升级版.html').write_text('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>360教育在线 · 夏季刊视觉升级版</title><meta name="viewport" content="width=1080"><style>'+css+'</style></head><body><main>'+''.join(p)+'</main></body></html>',encoding='utf8')
(R/'制作文件/v2/photo-audit.json').write_text(json.dumps({'unique':len(set(used)),'placements':len(used),'missing':[]},ensure_ascii=False),encoding='utf8')
print('Visual edition built: 110/110 unique photos')
