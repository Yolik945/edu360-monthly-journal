'use client';
/* oxlint-disable next/no-img-element -- Photos are already resized and encoded as WebP for this static publication. */

import { ArrowRight, ArrowUpRight, Expand } from 'lucide-react';
import data from './journal-data.json';

type Chapter = (typeof data)[number];

export function StoryContent({ chapter, page, onPhoto, onNext }: {
  chapter: Chapter;
  page: number;
  onPhoto: (photo: number) => void;
  onNext: () => void;
}) {
  return <div className={`story-scroll story-${chapter.id}`}>
    <header className="story-opening">
      <div className="story-folio" aria-hidden="true"><span>CHAPTER</span><b>{String(page).padStart(2, '0')}</b><span>SUMMER / 2026</span></div>
      <div className="story-opening-copy">
        <p className="overline">360教育在线 <span>/</span> {chapter.kicker.split(' / ')[1]}</p>
        <h2>{chapter.title.split('\n').map((line, i) => <span key={line} className={i ? 'accent-word' : ''}>{line}</span>)}</h2>
        <p className="story-lead">{chapter.desc}</p>
        <div className="story-opening-foot"><span>{String(chapter.notes.length).padStart(2, '0')} 段记录 <i>/</i> {chapter.photos.length} 张照片</span><span>夏日现场 <ArrowUpRight size={17}/></span></div>
      </div>
    </header>
    <div className="story-articles">
      {chapter.notes.map((note, i) => <article className="story-group" key={note.name}>
        <div className="story-margin">
          <p className="story-index"><span>{String(i + 1).padStart(2, '0')}</span><span> / {String(chapter.notes.length).padStart(2, '0')}</span></p>
          <h3>{note.name}</h3>
          <p className="story-note">{note.text}</p>
          <span className="story-margin-rule" aria-hidden="true"/>
        </div>
        <div className={`photo-gallery ${note.photos.length === 1 ? 'single' : ''} ${chapter.id === 'people' ? 'portraits' : ''}`}>
          {note.photos.map((num, j) => <figure key={num} className={`${j === 0 && note.photos.length > 2 ? 'gallery-lead' : ''} ${num === 110 ? 'travel-feature' : ''}`}>
            <button onClick={() => onPhoto(num)} aria-label={`查看${note.name}照片${j + 1}`}>
              <img src={`/photos/${num}.webp`} alt={`${note.name} · 照片${j + 1}`} loading="lazy"/>
              <span className="photo-expand"><Expand size={17}/></span>
            </button>
            {num === 110 && <div className="travel-feature-copy" aria-hidden="true"><span>OUT OF OFFICE</span><p>把夏天，<br/>留在风里。</p><span>SUMMER<br/>COLLECTION / 2026</span></div>}
            <figcaption><span>{String(chapter.photos.indexOf(num) + 1).padStart(2, '0')} <i>/</i> {String(chapter.photos.length).padStart(2, '0')}</span><span>{num === 110 ? '把生活，交还给山海' : note.name.split(' · ')[0]}</span></figcaption>
          </figure>)}
        </div>
      </article>)}
    </div>
    <footer className="story-bottom">
      <span className="overline">{page === data.length ? 'UNTIL NEXT TIME' : 'TO BE CONTINUED'}</span>
      <p>{page === data.length ? '盛夏的故事，未完待续。' : '收藏这一程，\n继续下一页。'}</p>
      <button className="read-button" onClick={onNext}>{page === data.length ? '回到封面' : '翻到下一章'}<ArrowRight size={20}/></button>
      <div className="story-colophon"><span>360教育在线 · 行政中心</span><span>2026 夏季刊 / {String(page).padStart(2, '0')}</span></div>
    </footer>
  </div>;
}
