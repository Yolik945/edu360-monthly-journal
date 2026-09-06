from pathlib import Path
import json,base64,html,math

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'成品'
src=json.loads((ROOT/'source.json').read_text(encoding='utf-8'))
files={int(p['file'].split('.')[0][5:]):p['file'] for p in src['photos']}
used=[]

def pic(n,x,y,w,h,cap='',rot=0,fit='cover',pos='50% 50%',frame=False):
    used.append(n)
    cl='photo paper' if frame else 'photo'
    ih=h-44 if cap else h
    return f'<figure class="{cl}" data-photo="{n}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)"><img src="../制作文件/photos/{files[n]}" style="height:{ih}px;object-fit:{fit};object-position:{pos}" alt="资料照片 {n}">'+(f'<figcaption>{cap}</figcaption>' if cap else '')+'</figure>'

def stage(h,*items,cls=''):
    return f'<div class="stage {cls}" style="height:{h}px">'+''.join(items)+'</div>'

def label(t,x,y,rot=0,color='orange'):
    return f'<span class="sticker {color}" style="left:{x}px;top:{y}px;transform:rotate({rot}deg)">{t}</span>'

def textblock(t,cls='body'):
    return f'<p class="{cls}">{t}</p>'

def heading(num,en,title,sub,cls=''):
    return f'<header class="chapter-head {cls}"><div class="eyebrow"><span>{num} / {en}</span><span>360 SUMMER JOURNAL</span></div><h2>{title}</h2><p class="dek">{sub}</p></header>'

def story(k,title,meta,body):
    return f'<div class="story"><div class="story-index">{k}</div><div><div class="meta">{meta}</div><h3>{title}</h3><p class="body">{body}</p></div></div>'

def trio(a,b,c,mode=0,caps=('', '', '')):
    if mode==0:
        return stage(895,pic(a,0,0,650,480,caps[0]),pic(b,555,400,415,350,caps[1],2,frame=True),pic(c,18,520,500,330,caps[2],-2,frame=True))
    return stage(960,pic(a,330,0,640,430,caps[0]),pic(b,10,120,390,250,caps[1],-2,frame=True),pic(c,200,470,740,440,caps[2]),label('GLOBAL DIALOGUE' if a==55 else 'ON THE ROAD',0,830,-5))

css=r'''
*{box-sizing:border-box}html,body{margin:0;padding:0;background:#e9e6df}body{font-family:"Microsoft YaHei",sans-serif;color:#17203b;-webkit-font-smoothing:antialiased}main{width:1080px;margin:auto;background:#f6f3e9;overflow:hidden}h1,h2,h3,p,figure{margin:0}section{position:relative;padding:70px 55px 80px}section.dark{background:#203bd3;color:#fff}section.ink{background:#17203b;color:#fff}section.lightblue{background:#e8edff}section.peach{background:#ffe3d1}section.white{background:#fffcf6}.eyebrow{display:flex;justify-content:space-between;font-size:21px;letter-spacing:2px;font-weight:700;font-family:Arial,"Microsoft YaHei",sans-serif}.chapter-head{padding-bottom:40px}.chapter-head h2{font-size:76px;line-height:1.24;letter-spacing:-3px;margin-top:37px;font-weight:900}.chapter-head .dek{font-size:29px;line-height:1.7;margin-top:22px;opacity:.85}.body{font-size:33px;line-height:1.75;letter-spacing:.1px;margin:12px 0 28px;overflow-wrap:break-word}.small{font-size:26px;line-height:1.65}.meta{font-size:25px;color:#2547ef;font-weight:700;letter-spacing:1px;margin:8px 0 18px}.dark .meta,.ink .meta{color:#d9f06a}.story{display:flex;gap:26px;margin:44px 0 34px}.story-index{flex-shrink:0;width:82px;font-family:Arial,sans-serif;font-size:78px;font-weight:900;color:#2547ef;line-height:1.1}.story h3{font-size:46px;line-height:1.4;letter-spacing:-1px}.story .body{font-size:31px;margin:18px 0 0}.stage{position:relative;width:970px;margin:22px 0 30px}.photo{position:absolute;overflow:hidden;background:#fff;color:#17203b}.photo img{display:block;width:100%;image-rendering:auto}.photo.paper{outline:10px solid #fff;box-shadow:0 10px 28px #17203b22;overflow:visible}.photo figcaption{font-size:21px;line-height:44px;padding:0 14px;white-space:nowrap;overflow:hidden;background:#fff}.sticker{position:absolute;z-index:3;background:#f97c45;color:#17203b;padding:17px 28px;font-size:26px;font-weight:700;letter-spacing:2px;white-space:nowrap}.sticker.lime{background:#dcf173}.sticker.blue{background:#2547ef;color:white}.mini-title{font-size:38px;line-height:1.5;margin:38px 0 14px}.split-note{display:grid;grid-template-columns:1fr 1fr;gap:38px;margin:36px 0}.split-note p{font-size:28px;line-height:1.7}.quote{font-size:44px;line-height:1.55;padding:32px 0 36px;border-top:2px solid currentColor;border-bottom:2px solid currentColor;margin:32px 0}.quote span{display:block;font-size:25px;margin-top:20px}.tagrow{display:flex;flex-wrap:wrap;gap:12px;margin:24px 0}.tagrow span{font-size:25px;border:1px solid currentColor;padding:11px 20px;border-radius:40px}.rule{height:1px;background:currentColor;opacity:.25;margin:32px 0}.ribbon{font-size:26px;letter-spacing:3px;white-space:nowrap;background:#dbef71;color:#17203b;padding:20px 0;text-align:center}.section-end{display:flex;justify-content:space-between;font-size:22px;letter-spacing:2px;margin-top:36px;padding-top:23px;border-top:1px solid #80808066}.star{font-family:Arial,sans-serif;font-size:90px;line-height:1}.cover{height:1460px;padding:55px;background:#f6f3e9}.cover-art{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.cover:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#f6f3e980,transparent 65%);pointer-events:none}.cover>*:not(.cover-art){position:relative;z-index:1}.brand{font-size:38px;font-weight:900;letter-spacing:-1px}.brand small{font-size:20px;letter-spacing:3px;margin-left:25px;font-weight:500}.issue{display:flex;justify-content:space-between;font:23px Arial,sans-serif;letter-spacing:3px;margin-top:32px}.cover h1{font-size:151px;line-height:1.12;letter-spacing:-9px;font-weight:900;margin-top:96px;color:#203bd3}.cover h1 em{font-style:normal;color:#17203b}.cover .cover-line{font-size:35px;line-height:1.7;margin-top:36px}.cover-bottom{position:absolute!important;left:55px;bottom:60px;right:55px}.cover-bottom .big-en{font-size:65px;font-weight:900;line-height:1.03;letter-spacing:-3px;font-family:Arial,sans-serif}.cover-bottom p{font-size:25px;margin-top:25px}.intro-title{font-size:54px;line-height:1.5;margin-top:25px}.intro .body{font-size:32px}.index-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;border-top:1px solid #17203b;padding-top:25px;margin-top:42px}.index-strip b{font:56px Arial;color:#2547ef}.index-strip p{font-size:26px;line-height:1.6;margin-top:12px}.chapter-number{position:absolute;right:45px;top:120px;font:190px Arial;color:#ffffff17}.travel-note{position:absolute;font-size:30px;line-height:1.65}.big-statement{font-size:67px;line-height:1.38;font-weight:900;letter-spacing:-2px}.profile-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:50px 34px;margin-top:36px}.profile{position:relative}.profile .portrait{height:465px;position:relative;background:#fff}.profile .portrait img{width:100%;height:100%;object-fit:cover;object-position:center 35%}.profile h3{font-size:43px;margin-top:26px}.profile .role{font-size:25px;line-height:1.6;margin-top:10px;min-height:80px;color:#2547ef;font-weight:700}.profile .bio{font-size:28px;line-height:1.7;margin-top:16px}.num-tag{position:absolute;left:0;bottom:0;background:#d9ef73;padding:12px 23px;font:32px Arial}.metrics{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;border-top:1px solid #17203b;border-bottom:1px solid #17203b;padding:28px 0;margin:35px 0}.metrics b{display:block;font:70px Arial;font-weight:800;color:#2547ef}.metrics span{font-size:26px}.caption-note{font-size:22px;line-height:1.65;opacity:.7}.kol-entry{display:flex;align-items:center;gap:28px;margin:36px 0}.kol-entry .number{font-size:60px;font-family:Arial;font-weight:900;color:#2547ef}.kol-entry h3{font-size:35px;line-height:1.55}.kol-entry p{font-size:25px;line-height:1.6}.footer{padding:90px 55px 70px;background:#203bd3;color:#fff}.footer h2{font-size:95px;line-height:1.3;letter-spacing:-4px}.footer .body{margin-top:45px}.footer .footer-mark{font-size:165px;font-family:Arial;font-weight:900;letter-spacing:-9px;margin-top:50px;line-height:1}.footer .byline{font-size:26px;text-align:right;margin-top:30px}.footer .foot{margin-top:50px;border-top:1px solid #ffffff70;padding-top:25px;display:flex;justify-content:space-between;font-size:22px}
'''

parts=[]
parts.append('''<section class="cover" id="cover"><img class="cover-art" src="../制作文件/cover-art.png" alt="蓝色环带与橙色夏日圆球"><div class="brand">360教育在线 <small>集团季刊</small></div><div class="issue"><span>2026 · 夏季刊</span><span>SUMMER EDITION ↗</span></div><h1>盛夏，<br><em>我们在场。</em></h1><p class="cover-line">融通中外 · 研途新篇<br>把每一次奔赴，写进这个夏天。</p><div class="cover-bottom"><div class="big-en">A SUMMER<br>OF CONNECTIONS.</div><p>院校之间，城市之间，你我之间。</p></div></section>''')
parts.append('''<section class="intro white" id="intro"><div class="eyebrow"><span>卷首 / EDITOR’S LETTER</span><span>夏日进行时</span></div><h2 class="intro-title">那些热烈的日常，<br>汇成我们的盛夏故事。</h2><p class="body">从福州峰会到各地研招宣讲，从曼谷的高校交流到镜头前的海外院校对话，这个夏天，我们持续连接院校与学子，也在复盘、成长和相聚中，看见彼此的力量。</p><p class="body">致敬每一位奔走在一线的你，也感谢每一位在幕后全力支撑的伙伴。一起翻开这份夏日记录。</p><div class="index-strip"><div><b>01—03</b><p>连接院校<br>峰会 / 巡讲 / 国际交流</p></div><div><b>04—06</b><p>探索新路<br>经营 / 直播 / 内容传播</p></div><div><b>07—12</b><p>看见彼此<br>成长 / 生活 / 温暖同行</p></div></div></section>''')

# 01 Summit: establishing view, details, speaker, roundtable and group portrait.
p=heading('01','THE SUMMIT','在福州，<br>共话教育的下一程','第八届高校研究生招生工作交流会')
p+='<div class="tagrow"><span>2026.07.09</span><span>福州</span><span>360教育在线 × 福耀科技大学</span></div>'
p+=textblock('以“新质强国，智汇未来”为主题，全国高校研究生招生工作负责人齐聚榕城，围绕研究生教育转型与招生变革交流经验、碰撞观点。')
p+=stage(1220,pic(5,0,0,970,560),pic(1,20,425,250,378,'入场，开启新一程',-3,frame=True),pic(2,315,605,315,280,'会务现场'),pic(3,655,650,315,280,'迎接远道而来的伙伴'),pic(4,315,920,640,275),label('HELLO, FUZHOU',35,1110,-4))
p+='<div class="quote">“AI不仅是工具层面的革新，<br>更是重塑招生逻辑、提升组织效能的核心引擎。”<span>—— 360教育在线创始人 付嘉</span></div>'
p+=textblock('开幕致辞中，付嘉以《洪流之上的守护与远方，现代大学品牌的社会责任与数字升维》为题，分享人工智能在教育领域的演进与应用。')
p+=stage(735,pic(7,0,0,620,410),pic(6,490,385,480,320),'<div class="travel-note" style="left:660px;top:65px;width:295px">从技术应用<br>到招生逻辑<br><br><b style="color:#dcf173">让新的可能<br>走向真实场景 ↗</b></div>')
p+='<h3 class="mini-title">圆桌沙龙 / 把问题聊深，把未来看远</h3>'
p+=textblock('天津大学肖松山、华南理工大学阮向前、上海财经大学韩云炜、浙江理工大学朱恩泽、山东科技大学马睿娟、天津理工大学郭凯等嘉宾，围绕招生选拔、培养质量、学科建设与产教融合展开对话。')
p+=stage(1080,pic(8,0,0,680,453),pic(9,565,375,405,270,rot=2,frame=True),pic(10,0,600,760,465),label('明年，再续精彩！',580,963,-5,'lime'))
parts.append('<section class="dark" id="summit">'+p+'</section>')

# 02 Roadshow: deliberately different arrangements for each university.
p=heading('02','ON THE ROAD','研招的夏天，<br>我们一直在路上','2027级研究生招生宣讲咨询会 · 夏季巡讲记录')
p+='<div class="ribbon">长沙 → 广州 → 济南 → 杭州 → 南京 → 太原</div>'
p+=story('A','融通中外，研途新篇','广东外语外贸大学 · 长沙站','走进长沙，解读招生政策、专业优势与培养特色。宣讲结束后，咨询仍在继续，每一次耐心解答，都在帮助学子把未来看得更清楚。')
p+=trio(12,13,11,0,('相聚长沙','面对面答疑','宣讲现场'))
p+=story('B','智领未来，菁聚上财','上海财经大学 · 广州站 & 济南站','从花城到泉城，招生团队围绕学科实力、就业前景与奖助体系展开分享，把学子关心的问题带到现场，一一回应。')
p+=stage(1340,pic(15,0,0,640,465),pic(16,680,130,290,350,pos='45% 50%'),pic(14,0,520,460,340),pic(17,500,530,470,350),pic(18,100,900,650,435),label('两座城市，同样热烈',440,25,-4))
p+=story('C','研路星辰，电亮青春','西安电子科技大学 · 杭州场 & 南京场','带着电子信息领域的学科积淀，西电走进杭州与南京。招生老师分享前沿专业与培养特色，与同学们聊技术、聊选择，也聊更远的未来。')
p+=stage(1140,pic(20,0,0,725,405),pic(19,700,290,245,340,rot=3,frame=True),pic(21,15,520,255,365,rot=-3,frame=True),pic(22,310,660,660,475),label('把热爱，带向下一站',285,472,-3,'blue'))
p+=story('D','晋研逐梦，翼起南航','南京航空航天大学 · 太原站','从飞行器设计到航空宇航科学，南航研招团队为山西学子带来专业分享。现场的专注与提问，让关于蓝天和星辰的梦想更加具体。')
p+=trio(25,23,24,1,('太原站现场','晋研逐梦，翼起南航','认真记录每一个选择'))
parts.append('<section id="roadshow">'+p+'</section>')

# 03 International.
p=heading('03','ACROSS BORDERS','让教育的连接，<br>跨越国界','国际合作 & 海外院校交流 · 夏季纪实')
p+=story('↗','中泰高校交流 · MOU签约','中国高校代表团访问泰国 · 曼谷','福州大学代表团访问泰国易三仓大学，围绕学术交流、学生联合培养与科研合作深入探讨，并签署MOU合作备忘录。360教育在线在曼谷提供接待服务，支持高校交流。')
p+=stage(1100,pic(27,0,0,680,510),pic(26,650,330,300,444,rot=2,frame=True),pic(28,0,565,605,454),pic(29,635,820,335,250),label('BANGKOK · CONNECTED',18,1020,-3,'lime'))
p+=story('↗','上海外国语大学来访交流','围绕国际中文教育，共探合作空间','上海外国语大学中文学院·国际文化交流学院陈院长带队来访，双方就国际中文教育、海外办学合作与文化交流活动展开座谈。')
p+=stage(1080,pic(30,200,0,770,510),pic(31,0,445,410,274,rot=-2,frame=True),pic(32,450,555,520,347),pic(33,0,760,450,300),label('面对面，打开新可能',440,950,3,'blue'))
parts.append('<section class="lightblue" id="international">'+p+'</section>')

# 04 Midyear.
p=heading('04','RESET & RESTART','复盘之后，<br>带着共识再出发','2026年半年度经营管理会 · 南京')
p+=textblock('年中相聚南京，各地伙伴开启联合办公，在面对面交流中复盘上半年得失、聚焦全年目标，讨论下半年的业务方向与行动。')
p+=stage(1310,pic(39,0,0,970,600),pic(34,0,645,570,425),pic(37,620,545,330,480,rot=3,frame=True),pic(35,0,1110,300,200),pic(36,330,1110,300,200),pic(38,660,1110,310,200),label('相聚，是为了更好地出发',20,535,-3))
p+='<h3 class="mini-title">把讨论落到下一步</h3>'+textblock('从业务数据到市场趋势，从问题诊断到解决方案，大家围绕研招业务、国际化布局、数字化能力与团队建设深入研讨。')
p+=stage(1350,pic(40,0,0,620,465),pic(42,555,405,415,311,rot=2,frame=True),pic(41,0,505,510,382),pic(43,0,945,300,400),pic(44,335,910,300,400),pic(45,670,950,300,400),label('让想法，变成行动 ↗',530,785,-4,'lime'))
p+='<h3 class="mini-title">认真工作，也一起好好充电</h3>'+textblock('羽毛球赛场上释放压力，观影时光里放松身心。在共同工作的节奏之外，也为下一程积攒能量。')
p+=stage(1100,pic(46,0,0,630,470),pic(47,650,155,310,487,rot=2,frame=True),pic(48,0,510,585,329),pic(49,415,750,555,350),label('RECHARGED',20,930,-5,'lime'))
parts.append('<section class="ink" id="midyear">'+p+'</section>')

# 05 Interviews.
p=heading('05','ON AIR','全开麦，<br>听见更大的世界','FM我的大学全开麦 · 海外专场')
p+=textblock('从镜头前的对话出发，走近海外院校的教学特色、校园生活与发展机会。海外专场首期聚焦泰国易三仓大学，打开了解院校的新窗口。')
p+=story('01','泰国易三仓大学','首期上线 · 深入了解校园与专业','围绕全英文授课、国际化校园、专业设置与校友资源展开分享，让院校信息更直观，也更贴近学子的真实问题。')
p+=trio(52,51,50,0,('对话现场','交流留念','来访合影'))
p+=story('02','澳门圣若瑟大学','招生处处长李处 · 院校交流','围绕海外教育资源开展交流，以访谈和分享呈现院校特色。')
p+=trio(55,53,54,1,('镜头前的深度交流','参访交流','相聚留影'))
p+=story('03','麦考瑞大学','中国区负责人 Joanna · 院校交流','继续拓展对话，让更多优质海外院校被看见、被了解。')
p+=trio(57,58,56,0,('FM我的大学全开麦','院校交流','来访合影'))
parts.append('<section class="white" id="live">'+p+'</section>')

# 06 KOL.
p=heading('06','CONTENT IN MOTION','从真实日常，<br>打开泰国留学','KOL / KOC 海外内容推广矩阵 · 泰国首站')
p+=textblock('携手小红书达人，用校园Plog、探校vlog与院校解析，把海外学习和生活的细节带到更多人面前。')
p+='<div class="metrics"><div><b>1,064</b><span>累计点赞</span></div><div><b>342</b><span>累计收藏</span></div><div><b>67</b><span>累计评论</span></div></div><p class="caption-note">按本期资料中三条内容的数据加总，非实时数据。</p>'
kol=[(59,'01','芹菜（泰国留学中）','泰国留学期末Plog','从教室到校园，记录学习与生活的真实日常。','129 赞 · 33 藏 · 17 评'),(60,'02','湄南河罗非鱼','泰国居然藏着一座城堡大学？','走进易三仓大学，用探校vlog打开校园空间。','263 赞 · 118 藏 · 35 评'),(61,'03','在逃波仔（学习版）','花园式学府，等你来','以校园风光与学习环境，呈现海外院校的新选择。','672 赞 · 191 藏 · 15 评')]
for n,k,name,title,desc,stat in kol:
    p+=f'<div class="kol-entry"><div class="number">{k}</div><div><h3>{name}</h3><p>{title}</p></div></div>'
    p+=stage(725,pic(n,0 if n!=60 else 130,0,840,685,rot=-1 if n==59 else 1 if n==61 else 0,fit='contain',frame=True),label(stat,420 if n!=60 else 20,650,-3,'blue'))
    p+=textblock(desc)
parts.append('<section class="peach" id="kol">'+p+'</section>')

# 07 Trainees.
p=heading('07','NEW ENERGY','新星登场，<br>成长正在发生','管培生交流会 · 青春正当时')
p+=textblock('趣味破冰与PDP性格测试拉近距离，自我介绍让彼此找到共同话题。往届优秀管培生分享从职场新人到业务骨干的成长经验，新伙伴也写下自己的职业目标。')
p+=stage(1470,pic(62,0,0,760,506),pic(64,530,445,425,284,rot=3,frame=True),pic(65,0,580,490,310),pic(63,100,960,720,455),pic(66,480,750,490,330),label('保持好奇，勇敢试试。',0,1390,-4,'lime'))
p+='<div class="quote">在360教育在线，<br>找到属于自己的赛道。<span>愿每一次尝试，都成为成长的一步。</span></div>'
parts.append('<section class="dark" id="trainee">'+p+'</section>')

# 08 Sport. Full original event poster is retained within the designed layout.
p=heading('08','ENERGY CLUB','工作全力以赴，<br>快乐也要尽兴','暑假前健康团建 · 羽毛球活动')
p+=textblock('忙完招生季与峰会筹备，伙伴们走上球场。挥拍、奔跑、扣杀，在一来一回中释放压力，也在欢声笑语里拉近距离。')
p+=stage(1220,pic(67,0,0,270,585,fit='contain'),pic(70,305,0,665,382),pic(68,325,465,290,465,rot=-3,frame=True),pic(69,665,430,280,500,rot=3,frame=True),pic(71,0,1000,455,220),pic(72,490,985,480,235),label('READY? PLAY!',15,740,-7,'blue'))
p+=stage(1030,pic(73,0,0,605,455),pic(74,425,400,545,305,rot=2,frame=True),pic(75,0,665,610,345),label('充电完成，继续出发 ↗',545,875,-5))
parts.append('<section class="lightblue" id="sport">'+p+'</section>')

# 09 Travel. Photos grouped by visible scenes; no invented destinations.
p=heading('09','OUT OF OFFICE','把生活，<br>交还给山海','员工旅行印记 · 这个夏天的另一面')
p+=textblock('放下键盘、背起行囊，走向城市之外。看过的风景、一起出发的人，还有偶然遇到的美好，都是属于我们的夏日收藏。')
p+=stage(620,pic(76,0,0,970,556))
p+=stage(1190,pic(110,100,0,740,1110,rot=-2,frame=True),label('把夏天，留在风里',535,1060,3,'blue'))
p+=stage(1200,pic(77,0,0,605,342),pic(79,650,0,295,440,rot=2,frame=True),pic(80,0,410,285,505),pic(83,330,440,430,575,rot=-2,frame=True),'<div class="travel-note" style="left:785px;top:580px;width:180px">走进<br>陌生城市<br><br>遇见<br>另一种<br>日常</div>',label('收集路上的好风景',440,1060,-4,'blue'))
p+='<div class="big-statement">海风一吹，<br>快乐就有了形状。</div>'
p+=stage(1600,pic(78,0,0,630,420),pic(84,685,140,265,354,rot=3,frame=True),pic(81,300,550,670,506),pic(82,0,475,255,440),pic(85,0,1125,680,453),label('SEA YOU SOON',655,1230,7))
p+='<div class="big-statement">向山野走去，<br>把视野再打开一点。</div>'
p+=stage(1370,pic(86,0,0,690,518),pic(89,650,410,300,420,rot=3,frame=True),pic(87,0,585,600,337),pic(88,255,960,715,464),label('WANDER MORE',5,1140,-7,'blue'))
p+='<h3 class="mini-title">旅途里的小小快乐，也值得被记住。</h3>'
p+=stage(1675,pic(90,0,0,410,555,rot=-2,frame=True),pic(91,470,30,305,460),pic(92,655,585,315,472,rot=2,frame=True),pic(93,0,675,310,465),pic(94,345,635,275,400),pic(95,240,1170,390,520,rot=-2,frame=True),label('下一站，继续一起出发',455,1450,-5,'lime'))
parts.append('<section class="white" id="travel">'+p+'</section>')

# 10 Merchandise: rely on visible and supplied product identity, omit unverified materials.
p=heading('10','SUMMER GOODS','把喜欢，<br>装进日常','360教育在线专属定制周边 · 上新预告')
p+=textblock('一只水杯，陪你认真补水；一只随行包，装下通勤与出游的小物。把属于360教育在线的标识，带进每一天的生活。')
p+=stage(1100,pic(96,0,0,520,695),pic(97,570,140,370,495,rot=3,frame=True),'<div class="travel-note" style="left:540px;top:790px;width:410px"><b style="font-size:46px">01 / 定制水杯</b><br>桌面上、出差途中，<br>记得好好喝水。</div>',label('GOOD DAY, GOOD MOOD',15,910,-4,'blue'))
p+=stage(1180,pic(99,500,0,440,660,rot=2,frame=True),pic(98,0,430,460,690,rot=-2,frame=True),'<div class="travel-note" style="left:0;top:80px;width:435px"><b style="font-size:46px">02 / 定制包袋</b><br>通勤出门、周末出游，<br>轻松装下今天的快乐。</div>',label('快乐，随身携带',535,890,5,'lime'))
parts.append('<section class="peach" id="goods">'+p+'</section>')

# 11 New colleagues. All six names, departments, roles and portraits match document order.
p=heading('11','HELLO, NEW FRIENDS','新朋友，<br>很高兴与你共事','本期新入职伙伴 · 欢迎加入360教育在线')
p+=textblock('从南京总部到各地分公司，新伙伴带着不同的经历与热爱相聚于此。接下来，一起工作，一起成长。')
people=[(100,'刘丽','湖北公司 · 武汉','大客户经理','很荣幸加入团队，期待和大家一起共事，也请各位前辈多多关照。'),(101,'王碧涵','总裁办 · 南京','总裁助理','我是Sofia，也可以叫我CC。很高兴和大家共事，希望尽快融入团队。'),(102,'唐兰兰','四川公司 · 成都','大客户经理','可以叫我兰兰，喜欢登山徒步。期待工作中并肩前行，生活中也能一起游玩。'),(103,'吴林','产研中心 · 南京','AI产品经理','专注AI产品的规划与落地，欢迎交流AI工具应用的想法，也欢迎看球搭子。'),(104,'胡家文','湖南公司 · 长沙','大客户经理','来自湖南益阳，很荣幸加入360教育在线这个大家庭，往后请多多指教。'),(105,'宋宜珠','山东公司 · 济南','大客户经理','很高兴来到充满活力的团队，希望未来与大家一起学习、一起进步。')]
p+='<div class="profile-grid">'
for k,(n,name,dep,role,bio) in enumerate(people,1):
    used.append(n)
    fit='contain' if n==101 else 'cover'
    p+=f'<article class="profile"><div class="portrait"><img data-photo="{n}" src="../制作文件/photos/{files[n]}" style="object-fit:{fit}" alt="{name}"><span class="num-tag">0{k} ↗</span></div><h3>{name}</h3><p class="role">{dep}<br>{role}</p><p class="bio">{bio}</p></article>'
p+='</div>'
parts.append('<section id="people">'+p+'</section>')

# 12 Letters: whole photos, no crop and no claims beyond source.
p=heading('12','A LITTLE WARMTH','教育的温度，<br>藏在一笔一画里','360教育在线 · 教育公益在行动')
p+=textblock('认真写下的字，细心画出的花，都让这份夏日记录多了一份温暖。我们相信，教育的善意，会在一次次真诚的回应中继续传递。')
p+=stage(1900,pic(106,0,0,440,783,rot=-2,fit='contain',frame=True),pic(107,515,90,440,783,rot=2,fit='contain',frame=True),pic(108,0,935,440,783,rot=-2,fit='contain',frame=True),pic(109,515,1020,440,783,rot=2,fit='contain',frame=True),label('每一份心意，都值得珍藏。',205,855,-3,'lime'))
parts.append('<section class="lightblue" id="charity">'+p+'</section>')
parts.append('''<footer class="footer" id="end"><div class="eyebrow"><span>卷尾 / UNTIL NEXT TIME</span><span>2026 · SUMMER</span></div><h2 style="margin-top:65px">盛夏的故事，<br>未完待续。</h2><p class="body">一路奔赴的脚步，全力以赴的日常，汇成这个夏天被看见的360教育在线。</p><p class="body">把夏日的热忱带向下一程。<br>时序向秋，我们下期再见。</p><p class="byline">360教育在线 · 行政中心</p><div class="footer-mark">SEE YOU ↗</div><div class="foot"><span>360教育在线 · 让教育更有温度</span><span>集团季刊 / 2026夏季刊</span></div></footer>''')

assert set(used)==set(files),f'Missing: {set(files)-set(used)} Extra: {set(used)-set(files)}'
assert len(used)==len(set(used)), 'Repeated source images'
parts[0]=parts[0].replace('院校之间，城市之间，你我之间。','院校之间，城市之间，<br>你我之间。')
css+='''
.cover{height:1780px}
.cover-art{top:525px;bottom:auto;height:1350px;object-fit:cover}
.cover:after{background:linear-gradient(180deg,#f6f3e9 0%,#f6f3e9 26%,transparent 43%)}
.cover .cover-line{max-width:690px}
.cover-bottom{left:0!important;right:0!important;bottom:0!important;padding:32px 55px 35px;background:#203bd3;color:#fff;display:flex;align-items:flex-end;justify-content:space-between;gap:30px}
.cover-bottom .big-en{font-size:48px;line-height:1.06;letter-spacing:-2px}
.cover-bottom p{font-size:23px;width:310px;line-height:1.6;margin-bottom:3px}
'''
doc='<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=1080"><title>360教育在线 · 2026夏季刊</title><style>'+css+'</style></head><body><main>'+''.join(parts)+'</main></body></html>'
(OUT/'夏季刊_排版源文件.html').write_text(doc,encoding='utf-8')
(ROOT/'photo-usage.json').write_text(json.dumps({'total':len(files),'used':len(used),'missing':list(set(files)-set(used)),'sequence':used},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Built magazine with {len(used)} / {len(files)} photos.')
