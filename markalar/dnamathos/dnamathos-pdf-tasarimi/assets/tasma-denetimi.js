// DNAMATHOS 2.0 slayt denetimi (page.evaluate ile çalıştırılır).
// KaTeX auto-render varsa çalıştırır; sonra her slaytta: (1) metin öğeleri slaytın ve kendi kutusunun dışına taşıyor mu,
// (2) gövde yazısı 17 px'ten, etiketler 11 px'ten küçük mü, (3) soru metni çözüm alanının üstüne biniyor mu.
() => {
  if (window.renderMathInElement) renderMathInElement(document.body, {delimiters:[{left:'$',right:'$',display:false}], throwOnError:true});
  const sorun = []; let enkucuk = 99;
  const etiketSinif = ['mono','etk','hap','marka','yol','nav','sag','noktalar','rozet'];
  document.querySelectorAll('.s').forEach(s => {
    const r = s.getBoundingClientRect();
    s.querySelectorAll('*').forEach(e => {
      if (e.closest('.filigran,svg,.katex-mathml')) return;
      const b = e.getBoundingClientRect(); if (!b.width || !b.height) return;
      const metin = [...e.childNodes].some(c => c.nodeType === 3 && c.textContent.trim());
      if (!metin) return;
      if (b.left < r.left - 1 || b.right > r.right + 1 || b.top < r.top - 1 || b.bottom > r.bottom + 1)
        sorun.push(`${s.id}: slayt dışına taşıyor → "${e.textContent.trim().slice(0, 40)}"`);
      const fs = parseFloat(getComputedStyle(e).fontSize);
      if (e.closest('.katex')) return;
      const etiket = etiketSinif.some(c => e.closest('.' + c)) || ['SMALL','TH'].includes(e.tagName);
      if (!etiket) { enkucuk = Math.min(enkucuk, fs); if (fs < 17) sorun.push(`${s.id}: gövde yazısı ${fs}px (en az 17)`); }
      else if (fs < 11) sorun.push(`${s.id}: etiket ${fs}px (en az 11)`);
      if (e.scrollHeight > e.clientHeight + 2 && getComputedStyle(e).overflow === 'hidden') sorun.push(`${s.id}: kutu içinde taşma`);
    });
    const coz = s.querySelector('.coz'), ic = s.querySelector('.ic');
    if (coz && ic) {
      const son = [...ic.querySelectorAll('*')].reduce((m, e) => Math.max(m, e.getBoundingClientRect().bottom), 0);
      if (son > coz.getBoundingClientRect().top - 6) sorun.push(`${s.id}: soru metni çözüm alanına biniyor (coz_ust değerini artır)`);
      if (coz.getBoundingClientRect().height < 150) sorun.push(`${s.id}: çözüm alanı ${Math.round(coz.getBoundingClientRect().height)}px (en az 150)`);
    }
  });
  return {problems: [...new Set(sorun)], enkucuk};
}
