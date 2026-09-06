const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const sharp=require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=__dirname, out=path.join(root,'../成品');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true,args:['--disable-gpu']});
 const page=await browser.newPage({viewport:{width:1080,height:1500},deviceScaleFactor:1});
 await page.goto(pathToFileURL(path.join(out,'夏季刊_排版源文件.html')).href);
 await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(im=>im.decode().catch(()=>{})))});
 const audit=await page.evaluate(()=>({width:document.querySelector('main').scrollWidth,height:document.querySelector('main').scrollHeight,images:[...document.images].map(x=>({id:x.dataset.photo||x.closest('[data-photo]')?.dataset.photo,loaded:x.complete&&x.naturalWidth>0})),sections:[...document.querySelector('main').children].map(el=>({id:el.id,y:el.offsetTop,height:el.offsetHeight})),overflows:[...document.querySelectorAll('h1,h2,h3,p,figcaption')].filter(el=>el.scrollWidth>el.clientWidth+2).map(el=>el.textContent)}));
 fs.writeFileSync(path.join(root,'render-audit.json'),JSON.stringify(audit,null,2));
 await page.screenshot({path:path.join(out,'360教育在线_2026夏季刊_完整长图.png'),fullPage:true,timeout:120000});
 await page.locator('#cover').screenshot({path:path.join(out,'夏季刊_封面预览.png')});
 for(const s of audit.sections){
  await page.locator('#'+s.id).screenshot({path:path.join(root,'qa',s.id+'.png'),timeout:60000});
  await sharp(path.join(root,'qa',s.id+'.png')).resize({width:400}).jpeg({quality:82}).toFile(path.join(root,'qa',s.id+'-small.jpg'));
 }
 await browser.close();
 await sharp(path.join(out,'360教育在线_2026夏季刊_完整长图.png'),{limitInputPixels:false}).jpeg({quality:93,chromaSubsampling:'4:4:4'}).toFile(path.join(out,'360教育在线_2026夏季刊_完整长图.jpg'));
 console.log(JSON.stringify({height:audit.height,sections:audit.sections,loaded:audit.images.every(x=>x.loaded),overflows:audit.overflows},null,2));
})().catch(e=>{console.error(e);process.exit(1)});
