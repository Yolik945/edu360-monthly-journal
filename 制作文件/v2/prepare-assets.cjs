const fs=require('fs'),path=require('path');
const sharp=require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const root=path.resolve(__dirname,'../..'),dest=path.join(root,'动态夏季刊/public/photos');fs.mkdirSync(dest,{recursive:true});
(async()=>{for(const file of fs.readdirSync(path.join(root,'制作文件/photos'))){const num=parseInt(file.slice(5));if(!num)continue;await sharp(path.join(root,'制作文件/photos',file)).rotate().resize({width:1800,height:2400,fit:'inside',withoutEnlargement:true}).webp({quality:89}).toFile(path.join(dest,num+'.webp'));}console.log('109 photos prepared')})()
