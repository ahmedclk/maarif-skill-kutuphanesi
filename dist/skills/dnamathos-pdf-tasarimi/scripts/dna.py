#!/usr/bin/env python3
"""DNAMATHOS 2.0 slayt bileşenleri.

İçerik skill'leri slaytları bu fonksiyonlarla kurar, sonra slayt_uret.py ile PDF'e çevirir:

    import sys; sys.path.insert(0, "<skill>/scripts")
    import dna
    g = dna.kapak(sinif="6. sınıf", ders=8, ust="Ortak kat", alt="ortak bölen", kod="MAT.6.1.4", akis="Isınma · 2 konu · kavrama testi")
    g += dna.konu(...)
    open("govde.html", "w").write(g)
    # python3 slayt_uret.py govde.html cikti.pdf --katex node_modules/katex/dist

Bütün metinler HTML olarak verilir (KaTeX için $...$ kullanılabilir). Kaçış gerekiyorsa dna.k() kullan.
"""
import html, math

k = html.escape
OK = '<svg viewBox="0 0 60 14"><path d="M2 7h52M46 2l8 5-8 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


def sarmal(w=150, h=28, basamak=8, dolu=None, renk="#fca311", ip="#ffffff"):
    """DNA sarmalı. dolu=None ise bütün basamaklar renkli; sayı verilirse ilerleme göstergesi olur."""
    y = lambda x: h / 2 + (h / 2 - 4) * math.sin(x / w * 3 * math.pi)
    p1 = " ".join(f"{x},{y(x):.1f}" for x in range(0, w + 1, 3))
    p2 = " ".join(f"{x},{h - y(x):.1f}" for x in range(0, w + 1, 3))
    r = []
    for i in range(basamak):
        x = 8 + i * (w - 16) / (basamak - 1)
        c = renk if dolu is None or i < dolu else "rgba(255,255,255,.25)"
        r.append(f'<line x1="{x:.1f}" y1="{y(x):.1f}" x2="{x:.1f}" y2="{h - y(x):.1f}" stroke="{c}" stroke-width="2.6" stroke-linecap="round"/>')
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">{"".join(r)}'
            f'<polyline points="{p1}" fill="none" stroke="{ip}" stroke-width="2"/><polyline points="{p2}" fill="none" stroke="{renk}" stroke-width="2"/></svg>')


def serit(yol, sira, toplam, nav=None, kimlik=None):
    """Üst şerit. nav: [(etiket, '#hedef', secili_mi)]. İlerleme sarmalı sira/toplam oranında dolar."""
    dolu = round(8 * sira / max(toplam, 1))
    navh = "".join(f'<a href="{h}" class="{"on" if on else ""}">{k(e)}</a>' for e, h, on in (nav or []))
    return (f'<div class="serit"><span class="marka">DNA<i>mathos</i></span><span class="yol">{yol}</span>'
            f'{f"<span class=nav>{navh}</span>" if navh else ""}<span class="sag">{sarmal(150, 28, 8, dolu)}<span>{sira}/{toplam}</span></span></div>')


def _s(sinif, kimlik, icerik):
    return f'<section class="s {sinif}" id="{kimlik}">{icerik}</section>'


def kapak(kimlik="kapak", ust="", alt="", sinif="", ders=1, kod="", akis="", not_el=""):
    return _s("kapak", kimlik,
              f'<div class="ust">{f"<div class=el>{not_el}</div>" if not_el else ""}<h1>{ust}</h1><div class="bilgi"><span class="hap">{sinif} {OK}</span><span class="hap">Ders {ders}</span></div></div>'
              f'<div class="rozet"><small>DERS</small><b>{ders:02d}</b></div>'
              f'<div class="alt"><h1>{alt}</h1><div class="bilgi"><span class="hap">{kod} {OK}</span>{f"<span class=hap>{akis}</span>" if akis else ""}</div>'
              f'<div class="sarmal">{sarmal(260, 74, 10)}</div><div class="marka">DNA<i>mathos</i></div></div>')


def _noktalar(n, sira):
    return '<div class="noktalar">' + "".join(f'<i class="{"on" if j < sira else ""}"></i>' for j in range(n)) + "</div>"


def tur_kapak(kimlik, serit_html, n, aciklama="Bakmadan cevapla. Geçen hafta ve daha öncesinden karışık."):
    return _s("tur koyu", kimlik, serit_html + f'<div class="ic"><span class="hap" style="color:var(--safran)">Isınma</span><div class="soru">5 dakika, <span class="vurgu">{n} soru</span></div><div class="alt-yazi">{aciklama}</div></div>{_noktalar(n, 0)}')


def tur_soru(kimlik, serit_html, bicim, soru, n, sira, not_el="", alt_yazi=""):
    return _s("tur koyu", kimlik, serit_html + '<div class="filigran">20 sn</div>'
              f'<div class="ic"><span class="hap" style="color:var(--safran)">{bicim}</span><div class="soru">{soru}</div>{f"<div class=alt-yazi>{alt_yazi}</div>" if alt_yazi else ""}</div>'
              f'{f"<div class=\'el not-el\'>{not_el}</div>" if not_el else ""}{_noktalar(n, sira - 1)}')


def tur_cevap(kimlik, serit_html, cevap, aciklama, n, sira):
    return _s("tur", kimlik, serit_html + f'<div class="ic"><span class="hap" style="color:var(--hardal)">Cevap</span><div class="cevap">{cevap}</div><div class="alt-yazi">{aciklama}</div></div>{_noktalar(n, sira)}')


def konu(kimlik, serit_html, no, baslik, once, kural, sekil="", yazilida="", kitapta="", hata="", slogan="", yazi_alani=True):
    sag = f'<div class="kural">{kural}</div>'
    if sekil: sag += f'<div class="sekil">{sekil}</div>'
    if hata: sag += f'<div class="hata"><span class="etk">Sık yapılan hata</span>{hata}</div>'
    if yazilida: sag += f'<div class="not"><span class="etk">Yazılıda böyle sorulur</span>{yazilida}</div>'
    if kitapta: sag += f'<div class="kitapta">Kitapta: {kitapta}</div>'
    if yazi_alani and not slogan: sag += '<div class="yazi-alani"></div>'
    if slogan: sag += f'<div class="slogan"><span class="mono">HAFTANIN SLOGANI</span><span class="el"><span class="vurgu">{slogan}</span></span></div>'
    return _s("konu", kimlik, serit_html + f'<div class="izgara"><div class="sol"><span class="hap">Konu {no}</span><h2>{baslik}</h2><div class="once"><span class="etk">Önce sen</span>{once}</div></div><div class="govde">{sag}</div></div>')


def soru(kimlik, serit_html, no, baslik, metin, maddeler="", cipler=(), tuyo="", coz_ust=300):
    """Çözüm alanı sorunun altındadır (coz_ust: alanın üst kenarı, px). Tüyo aynı sayfada, sağ altta."""
    c = "".join(f'<span class="hap">{x}</span>' for x in cipler)
    return _s("soru", kimlik, serit_html + f'<div class="ic"><div class="bas"><span class="hap">Soru {no}</span><h2>{baslik}</h2></div><div class="metin">{metin}</div>'
              f'{f"<div class=madde>{maddeler}</div>" if maddeler else ""}{f"<div class=cipler>{c}</div>" if c else ""}</div>'
              f'<div class="coz" style="top:{coz_ust}px"><span class="mono">ÇÖZÜM</span></div>'
              + (f'<div class="tuyo"><span class="mono">TAKILIRSAN · TÜYO</span><span class="el">{tuyo}</span></div>' if tuyo else ""))


def kaydet(kimlik, serit_html, maddeler, slogan):
    return _s("kaydet altin", kimlik, serit_html + '<div class="ic"><span class="hap">Kaydet</span><ul>' + "".join(f"<li>{m}</li>" for m in maddeler) +
              f'</ul><div class="el">slogan → {slogan}</div></div>')


def kavrama_kapak(kimlik, serit_html, turler, n=4):
    return _s("tur koyu", kimlik, serit_html + '<div class="ic"><span class="hap" style="color:var(--safran)">Kavrama testi</span><div class="soru">Bu dersi <span class="vurgu">kontrol edelim</span></div>'
              f'<div class="alt-yazi">{n} soru · 12 dakika · not yok. Her soruda cevabını ve nasıl karar verdiğini yaz.</div><div class="alt-yazi mono">{" · ".join(turler)}</div></div>')


def kavrama(kimlik, serit_html, no, toplam, soru_html, b_etiket="Nasıl karar verdin?"):
    return _s("kavrama", kimlik, serit_html + f'<div class="ic"><span class="hap" style="color:var(--hardal)">Kavrama testi · Soru {no}/{toplam}</span><h2>{soru_html}</h2>'
              f'<div class="satir">a) Cevap<div class="alan kisa"></div></div><div class="satir">b) {b_etiket} <small>BİR CÜMLEYLE</small><div class="alan"></div></div></div>'
              '<div class="guven"><span>Eminim</span><span>Emin değilim</span></div>')


def odev(kimlik, serit_html, ana, satirlar, sonraki=""):
    """satirlar: [(bölüm, sayfa)] isteğe bağlı ek çalışma; ana: kavrama testine bağlı ödev cümlesi."""
    tab = "".join(f"<tr><td>{a}</td><td>{b}</td><td><span class='kutu'></span></td></tr>" for a, b in satirlar)
    return _s("odev", kimlik, serit_html + f'<div class="ic"><span class="hap" style="color:var(--hardal)">Bu hafta</span><div class="ana">{ana}</div>'
              + (f'<table><tr><th>İsteğe bağlı ek çalışma</th><th>Sayfa</th><th>Yapıldı</th></tr>{tab}</table>' if satirlar else "")
              + (f'<div class="not" style="margin-top:14px"><span class="etk">Sonraki derste</span>{sonraki}</div>' if sonraki else "") + "</div>")


def sayi_dogrusu(ust=30, adim_etiket=2, w=600, ustte=(), altta=(), cevrele=(), etiket=("", ""), aciklama=""):
    """Sayı doğrusu. ustte/altta: işaretlenecek sayılar (öğrenci slaytında genellikle boş bırakılır; cevabı vermesin).
    cevrele: yalnız öğretmen ya da cevap slaytında kullanılır."""
    x0, x1 = 24, w - 24
    sx = lambda v: x0 + (x1 - x0) * v / ust
    s = [f'<svg viewBox="0 0 {w} 104" width="{w}" height="104" role="img" aria-label="{k(aciklama or f"0 ile {ust} arası sayı doğrusu")}">',
         f'<line x1="{x0}" y1="52" x2="{x1}" y2="52" stroke="#14213d" stroke-width="2"/>']
    for v in range(0, ust + 1):
        uzun = v % adim_etiket == 0
        s.append(f'<line x1="{sx(v):.1f}" y1="{45 if uzun else 47}" x2="{sx(v):.1f}" y2="{59 if uzun else 57}" stroke="#14213d" stroke-width="{1.6 if uzun else 1}"/>')
        if uzun:
            s.append(f'<text x="{sx(v):.1f}" y="80" font-size="14" text-anchor="middle" fill="#14213d" font-family="IBM Plex Mono, monospace">{v}</text>')
    for v in ustte: s.append(f'<circle cx="{sx(v):.1f}" cy="32" r="6.5" fill="#fca311" stroke="#14213d" stroke-width="1.2"/>')
    for v in altta: s.append(f'<rect x="{sx(v) - 6:.1f}" y="88" width="12" height="12" rx="2" fill="#14213d"/>')
    for v in cevrele: s.append(f'<rect x="{sx(v) - 12:.1f}" y="20" width="24" height="82" rx="12" fill="none" stroke="#fca311" stroke-width="2.4" stroke-dasharray="4 3"/>')
    if etiket[0]: s.append(f'<text x="{x0}" y="16" font-size="13" fill="#4a5570" font-family="IBM Plex Mono, monospace">{k(etiket[0])}</text>')
    if etiket[1]: s.append(f'<text x="{x1}" y="16" font-size="13" text-anchor="end" fill="#4a5570" font-family="IBM Plex Mono, monospace">{k(etiket[1])}</text>')
    return "".join(s) + "</svg>"


def tablo(baslik_satir, satirlar):
    """Basit HTML tablo (table.dna). Öğrencinin dolduracağı hücreler için boş dize ver."""
    h = "<table class='dna'><tr>" + "".join(f"<th>{x}</th>" for x in baslik_satir) + "</tr>"
    for r in satirlar:
        h += "<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>"
    return h + "</table>"
