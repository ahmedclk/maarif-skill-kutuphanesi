// DNAMATHOS slayt taşma denetimi (page.evaluate ile çalıştırılır). KaTeX auto-render çağrısını da içerir.

() => { const problems_pre = [];
  renderMathInElement(document.body, {delimiters:[{left:'$',right:'$',display:false}], throwOnError:true});document.querySelectorAll('.kleft,.kright').forEach(b=>{const r=b.getBoundingClientRect();[...b.children].forEach(e=>{const q=e.getBoundingClientRect();if(q.bottom>r.bottom+1)problems_pre.push(b.closest('.slide').id+' kart taşıyor');});});document.querySelectorAll('.kfig').forEach(f=>{if(f.querySelector('svg')&&f.getBoundingClientRect().height<18*96/25.4)problems_pre.push(f.closest('.slide').id+' şekil küçük '+Math.round(f.getBoundingClientRect().height));});
  const mm = 96/25.4, problems = problems_pre;
  document.querySelectorAll('.qslide').forEach(sl => {
    const qb = sl.querySelector('.qbody'), fig = qb.querySelector('.fig');
    let ok = false;
    for (const c of ['fs14','fs13','fs115']) {
      qb.className = 'qbody ' + c;
      if (fig) {
        fig.style.flex = '0 0 0px'; fig.style.height = '0px';
        const last = qb.lastElementChild, cs = getComputedStyle(last);
        const free = qb.getBoundingClientRect().bottom - last.getBoundingClientRect().bottom - parseFloat(cs.marginBottom);
        if (free >= 26*mm) { fig.style.height = Math.min(free, 60*mm) + 'px'; fig.style.flex = '0 0 auto'; ok = true; break; }
      } else if (qb.lastElementChild.getBoundingClientRect().bottom <= qb.getBoundingClientRect().bottom + 1) { ok = true; break; }
    }
    sl.dataset.fs = qb.className;
    if (!ok) problems.push(sl.id + ' taşıyor');
  });
  // genel taşma kontrolü: her slayttaki öğeler sayfa sınırı içinde mi
  document.querySelectorAll('.slide').forEach(sl => {
    const r = sl.getBoundingClientRect();
    sl.querySelectorAll('*').forEach(e => {
      if (e.closest('.katex') && !e.classList.contains('katex')) return;
      const b = e.getBoundingClientRect();
      if (b.width === 0 || b.height === 0) return;
      if (b.right > r.right + 1 || b.bottom > r.bottom + 1 || b.left < r.left - 1) problems.push(sl.id + ' sınır dışı: ' + e.className);
    });
    sl.querySelectorAll('.oc, .tile, .left, .qbody, .kleft, .kright, .sol, .tbody, .write, .kural, .kex').forEach(e => {
      if (e.scrollHeight > e.clientHeight + 1) problems.push(sl.id + ' iç taşma: ' + e.className);
    });
    // butonlar ile şekil/metin çakışması
    const nav = sl.querySelector('.qnav'), qb = sl.querySelector('.qbody');
    if (nav && qb && qb.getBoundingClientRect().bottom > nav.getBoundingClientRect().top + 1) problems.push(sl.id + ' butonlarla çakışma');
    if (qb && qb.lastElementChild.getBoundingClientRect().bottom > nav.getBoundingClientRect().top + 1) problems.push(sl.id + ' metin butonlara değiyor');
    sl.querySelectorAll('.oc').forEach(c => { const l=c.lastElementChild; if (l.getBoundingClientRect().bottom > c.getBoundingClientRect().bottom - 2) problems.push(sl.id+' özet kartı taşıyor'); });
  });
  document.querySelectorAll('.katex').forEach(k => {
    const box = k.closest('.left, .oc, .tile, td, th, .dleft, .dright, .home');
    if (box && k.getBoundingClientRect().right > box.getBoundingClientRect().right + 1) problems.push((k.closest('.slide')||{}).id + ' formül yatay taşıyor: ' + k.textContent.slice(0,30));
  });
  document.querySelectorAll('.left .part, .left p, .left .prem').forEach(e => {
    if (e.scrollWidth > e.clientWidth + 1) problems.push(e.closest('.slide').id + ' satır yatay taşıyor');
  });
  if (document.querySelector('.katex-error')) problems.push('KaTeX hatası');
  return {problems, sizes: [...document.querySelectorAll('.qslide')].map(s => s.id + ':' + s.dataset.fs)};
}
