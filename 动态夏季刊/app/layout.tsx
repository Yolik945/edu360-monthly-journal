import type {Metadata} from 'next';
import './globals.css';
export const metadata:Metadata={title:'盛夏在场 · 360教育在线2026夏季刊',description:'院校之间，城市之间，你我之间。翻阅360教育在线的夏日故事：高校合作、研招巡讲、海外交流与团队生活。'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="zh-CN"><body>{children}</body></html>}
