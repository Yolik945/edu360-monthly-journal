// Render a static review document from the actual story component and built CSS.
const fs=require('fs'),path=require('path'),Module=require('module'),{pathToFileURL}=require('url');
const root=path.resolve(__dirname,'../动态夏季刊'),requireSite=Module.createRequire(path.join(root,'package.json'));
const ts=requireSite('typescript'),React=requireSite('react'),{renderToStaticMarkup}=requireSite('react-dom/server');
const source=path.join(root,'app/story-content.tsx'),mod=new Module(source);
mod.filename=source;mod.paths=Module._nodeModulePaths(path.dirname(source));
mod._compile(ts.transpileModule(fs.readFileSync(source,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,jsx:ts.JsxEmit.ReactJSX,esModuleInterop:true}}).outputText,source);
const {StoryContent}=mod.exports,data=require(path.join(root,'app/journal-data.json'));
const assets=path.join(root,'dist/client/_next/static/css');
const css=fs.readdirSync(assets).filter(n=>n.endsWith('.css')).map(n=>fs.readFileSync(path.join(assets,n),'utf8')).join('\n');
const {chromium}=require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const sharp=require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 for(const [id,width,height] of [['travel',1280,1100],['travel',390,844],['summit',1280,1100]]){
  const chapter=data.find(d=>d.id===id),page=data.indexOf(chapter)+1;
  let markup=renderToStaticMarkup(React.createElement(StoryContent,{chapter,page,onPhoto:()=>{},onNext:()=>{}}));
  markup=markup.replace(/src="\/photos\/([^\"]+)"/g,(_,name)=>`src="${pathToFileURL(path.join(root,'public/photos',name)).href}"`).replaceAll('loading="lazy"','loading="eager"');
  const html=`<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>${css}</style><body><div data-slot="sheet-content" class="story-panel theme-${chapter.color} still" style="height:${height}px;display:flex;flex-direction:column;gap:0"><div class="panel-head story-toolbar"><div><div data-slot="sheet-title">${chapter.kicker}</div><div data-slot="sheet-description">360教育在线 · 2026夏季刊</div></div><button class="story-close">返回主视觉 ×</button></div>${markup}</div></body></html>`;
  const file=path.join(root,'work',`story-${id}-${width}.html`);fs.writeFileSync(file,html);
  const p=await browser.newPage({viewport:{width,height}});await p.goto(pathToFileURL(file).href);await p.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(im=>im.decode()))});
  await p.screenshot({path:path.join(__dirname,'qa',`story-${id}-${width}.png`)});
  if(id==='travel'&&width===1280){await p.locator('.travel-feature').screenshot({path:path.join(__dirname,'qa/story-new-photo.png')});}
  await p.close();
 }
 await browser.close();
 for(const [rel,out] of [['qa/travel.png','qa/v1-travel-added.jpg'],['v2/qa/travel.png','qa/v2-travel-added.jpg']])await sharp(path.join(__dirname,rel)).extract({left:0,top:0,width:1080,height:1600}).resize({width:675}).jpeg({quality:90}).toFile(path.join(__dirname,out));
 console.log('Static story review images and print photo crops rendered.');
})().catch(e=>{console.error(e);process.exit(1)});
