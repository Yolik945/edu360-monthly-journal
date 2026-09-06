const fs=require('fs'),path=require('path');
const sharp=require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=__dirname,out=path.join(root,'../成品'),dest=path.join(out,'按栏目分图');
fs.mkdirSync(dest,{recursive:true});
const groups=[['00_封面与卷首',['cover','intro']],['01_福州峰会',['summit']],['02_研招巡讲',['roadshow']],['03_国际合作',['international']],['04_半年度复盘',['midyear']],['05_海外全开麦',['live']],['06_海外内容推广',['kol']],['07_管培生成长',['trainee']],['08_健康团建',['sport']],['09_员工旅行',['travel']],['10_定制周边',['goods']],['11_新人报到',['people']],['12_公益与卷尾',['charity','end']]];
(async()=>{
 for(const [name,ids] of groups){let h=0,layers=[];for(const id of ids){const input=path.join(root,'qa',id+'.png');const meta=await sharp(input).metadata();layers.push({input,left:0,top:h});h+=meta.height;} await sharp({create:{width:1080,height:h,channels:3,background:'#f6f3e9'}}).composite(layers).jpeg({quality:93,chromaSubsampling:'4:4:4'}).toFile(path.join(dest,name+'.jpg'));}
 let html=fs.readFileSync(path.join(out,'夏季刊_排版源文件.html'),'utf8');
 html=html.replace(/src="(\.\.\/制作文件\/[^\"]+)"/g,(_,rel)=>{const local=path.resolve(out,rel),mime=local.endsWith('.png')?'image/png':'image/jpeg';return 'src="data:'+mime+';base64,'+fs.readFileSync(local).toString('base64')+'"';});
 fs.writeFileSync(path.join(out,'夏季刊_排版源文件.html'),html);
 const png=path.join(out,'360教育在线_2026夏季刊_完整长图.png');
 const meta=await sharp(png,{limitInputPixels:false}).metadata();
 const audit=JSON.parse(fs.readFileSync(path.join(root,'render-audit.json'),'utf8'));
 for(const [id,y] of [['cover',200],['summit',1800],['people',500],['roadshow',2850]]){const sec=audit.sections.find(x=>x.id===id);await sharp(png,{limitInputPixels:false}).extract({left:0,top:sec.y+y,width:1080,height:800}).toFile(path.join(root,'qa','detail-'+id+'.png'));}
 const qaImages=['cover','summit','international','people'];let layers=[],maxh=0;
 for(let i=0;i<qaImages.length;i++){const file=path.join(root,'qa',qaImages[i]+'-small.jpg'),m=await sharp(file).metadata();layers.push({input:file,left:i*400,top:0});maxh=Math.max(maxh,m.height);}
 await sharp({create:{width:1600,height:maxh,channels:3,background:'#dedbd3'}}).composite(layers).jpeg({quality:90}).toFile(path.join(out,'夏季刊_版式速览.jpg'));
 console.log(JSON.stringify({width:meta.width,height:meta.height,panels:groups.length,portableHtml:!html.includes('src="../')},null,2));
})().catch(e=>{console.error(e);process.exit(1)});
