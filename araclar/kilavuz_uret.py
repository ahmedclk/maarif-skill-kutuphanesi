#!/usr/bin/env python3
"""Öğretmen kılavuzunu ve tanıtım sayfasını tek kaynaktan üretir.

Kaynaklar: docs/kilavuz.yaml (skill rehberi), ortak/maarif/meb-olcme-mevzuati.md (MEV kuralları),
docs/is-akislari.md (iş akışları), paketler/*.yaml.
Çıktılar:
  docs/kilavuz.md          öğretmen kullanım kılavuzu (GitHub'da okunur)
  docs/index.html          GitHub Pages tanıtım sayfası (tam HTML belgesi)
  --parca DOSYA            aynı sayfanın gövde parçası (Claude artifact önizlemesi için)

Kullanım: python3 araclar/kilavuz_uret.py [--depo kullanici/depo] [--parca yol.html]
"""
import argparse, glob, html, json, os, re, sys
import yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import KOK

ap = argparse.ArgumentParser()
ap.add_argument("--depo", default="")
ap.add_argument("--parca")
a = ap.parse_args()

K = yaml.safe_load(open(os.path.join(KOK, "docs", "kilavuz.yaml"), encoding="utf-8"))
S = K["skills"]
E = html.escape
DEPO = a.depo.strip("/")
GH = f"https://github.com/{DEPO}" if DEPO else ""


def gh(yol):
    """Depo içindeki bir dosyanın GitHub adresi; depo verilmediyse None."""
    return f"{GH}/blob/main/{yol}" if GH else None


def ham(yol):
    return f"{GH}/raw/main/{yol}" if GH else None


# --- MEV kuralları ---------------------------------------------------------
mev_md = open(os.path.join(KOK, "ortak", "maarif", "meb-olcme-mevzuati.md"), encoding="utf-8").read()
MEV = {}
bolum = None
for satir in mev_md.splitlines():
    m = re.match(r"## \d+\. (.+)", satir)
    if m:
        bolum = m.group(1)
    m = re.match(r"\| (MEV-\d+) \| (.+?) \| (.+?) \|$", satir)
    if m:
        MEV[m.group(1)] = {"kural": m.group(2), "dayanak": m.group(3), "bolum": bolum}


def md_satir(s):
    """Basit Markdown biçimini (kalın, kod) HTML'ye çevirir."""
    s = E(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


# --- İş akışları -----------------------------------------------------------
akis = []
for blok in re.split(r"\n## ", open(os.path.join(KOK, "docs", "is-akislari.md"), encoding="utf-8").read())[1:]:
    bas, *govde = blok.split("\n")
    adimlar = [re.sub(r"^\d+\. ", "", g) for g in govde if re.match(r"^\d+\. ", g)]
    akis.append((bas.strip(), adimlar))

paketler = [yaml.safe_load(open(p, encoding="utf-8")) for p in sorted(glob.glob(os.path.join(KOK, "paketler", "*.yaml")))]

# --- 1. docs/kilavuz.md ----------------------------------------------------
L = [f"# {K['baslik']}: öğretmen kullanım kılavuzu", "",
     "> Bu dosya `docs/kilavuz.yaml` dosyasından `araclar/kilavuz_uret.py` ile üretilir; elle düzenlenmez.", "",
     K["tanitim"], "", "## Dört ilke", ""]
for i in K["ilkeler"]:
    L.append(f"- **{i['baslik']}.** {i['metin']}")
L += ["", "## Kurulum", ""]
for n, k in enumerate(K["kurulum"], 1):
    L.append(f"{n}. **{k['baslik']}:** {k['metin']}")
L += ["", "## Hangi iş için hangi skill?", ""]
for g in K["gruplar"]:
    L += [f"### {g['ad']}", "", "| Skill | Ne yapar |", "| --- | --- |"]
    for s in g["skills"]:
        L.append(f"| [{S[s]['gorunen']}](#{s}) · `{s}` | {S[s]['ne_yapar']} |")
    L.append("")
L += ["## Skill'ler tek tek", ""]
for g in K["gruplar"]:
    for s in g["skills"]:
        d = S[s]
        L += [f"### {d['gorunen']}", f"<a id=\"{s}\"></a>`{s}`", "", d["ne_yapar"], "",
              "**Ne zaman kullanılır?**", ""] + [f"- {x}" for x in d["ne_zaman"]] + [
              "", "**Siz verin:**", ""] + [f"- {x}" for x in d["verin"]] + [
              "", "**Siz alırsınız:**", ""] + [f"- {x}" for x in d["alirsiniz"]] + [
              "", "**Örnek istem:**", "", "```", d["istem"], "```", "",
              f"**Kontrol edin:** {d['kontrol']}", ""]
        if d["mevzuat"]:
            L += ["**Uyduğu MEB kuralları:**", ""] + [f"- {c}: {re.sub(r'[*]', '', MEV[c]['kural'])}" for c in d["mevzuat"]] + [""]
        L += [f"**Sonra:** [{S[d['sonraki']]['gorunen']}](#{d['sonraki']})", ""]
L += ["## İş akışları", ""]
for bas, adimlar in akis:
    L += [f"### {bas}", ""] + [f"{n}. {x}" for n, x in enumerate(adimlar, 1)] + [""]
L += ["## MEB ölçme kuralları (özet)", "",
      "Tam tablo ve dayanaklar: `ortak/maarif/meb-olcme-mevzuati.md`.", "", "| Kod | Kural |", "| --- | --- |"]
for c, v in MEV.items():
    L.append(f"| {c} | {v['kural']} |")
L += ["", "## Sık sorulanlar", ""]
for q in K["sss"]:
    L += [f"**{q['soru']}**", "", q["cevap"], ""]
open(os.path.join(KOK, "docs", "kilavuz.md"), "w", encoding="utf-8").write("\n".join(L))

# --- 2. Tanıtım sayfası ----------------------------------------------------
GRUP_KISA = {"Planlama": "plan", "Ölçme ve değerlendirme": "olcme", "İçerik üretimi": "icerik"}


def liste(xs):
    return "".join(f"<li>{E(x)}</li>" for x in xs)


def mev_cip(c):
    return f'<a class="mev" href="#{c.lower()}" title="{E(re.sub(r"[*`]", "", MEV[c]["kural"]))}">{c}</a>'


kartlar = []
for g in K["gruplar"]:
    for s in g["skills"]:
        d = S[s]
        zip_link = ham(f"dist/zip/{s}.zip")
        zip_html = f'<a class="ikincil" href="{zip_link}" target="_blank" rel="noopener">Skill dosyası (.zip)</a>' if zip_link else ""
        mev = "".join(mev_cip(c) for c in d["mevzuat"]) or '<span class="yok">Ölçme ürünü üretmez</span>'
        kartlar.append(f'''
<article class="kart" id="{s}" data-grup="{GRUP_KISA[g['ad']]}" data-ara="{E((d['gorunen'] + ' ' + s + ' ' + d['ne_yapar'] + ' ' + ' '.join(d['ne_zaman'])).lower())}">
  <header><h3>{E(d['gorunen'])}</h3><code class="ad">{s}</code></header>
  <p class="ne">{E(d['ne_yapar'])}</p>
  <div class="mevler" aria-label="Uyduğu MEB kuralları">{mev}</div>
  <details>
    <summary>Nasıl kullanılır?</summary>
    <dl>
      <dt>Ne zaman</dt><dd><ul>{liste(d['ne_zaman'])}</ul></dd>
      <dt>Siz verin</dt><dd><ul>{liste(d['verin'])}</ul></dd>
      <dt>Siz alırsınız</dt><dd><ul>{liste(d['alirsiniz'])}</ul></dd>
      <dt>Örnek istem</dt><dd><div class="istem"><p id="i-{s}">{E(d['istem'])}</p><button type="button" class="kopyala" data-hedef="i-{s}">Kopyala</button></div></dd>
      <dt>Kontrol edin</dt><dd>{E(d['kontrol'])}</dd>
      <dt>Sonra</dt><dd><a href="#{d['sonraki']}">{E(S[d['sonraki']]['gorunen'])}</a></dd>
    </dl>
    {zip_html}
  </details>
</article>''')

mev_satir = []
for c, v in MEV.items():
    mev_satir.append(f'<tr id="{c.lower()}"><th scope="row">{c}</th><td>{md_satir(v["kural"])}</td><td class="dayanak">{E(v["dayanak"])}</td></tr>')

akis_html = "".join(
    f'<section class="akis"><h3>{E(b)}</h3><ol>' +
    "".join(f"<li>{md_satir(x)}</li>" for x in ad) + "</ol></section>" for b, ad in akis)

paket_html = "".join(
    f'<tr><th scope="row"><code>{E(p["ad"])}</code></th><td>{E(p["aciklama"])}</td><td class="sayi">{len(p["skills"])}</td></tr>' for p in paketler)

sss_html = "".join(f"<details class=\"sss\"><summary>{E(q['soru'])}</summary><p>{E(q['cevap'])}</p></details>" for q in K["sss"])

github_btn = (f'<a class="birincil" href="{GH}" target="_blank" rel="noopener">GitHub deposunu aç</a>' if GH
              else '<a class="birincil" href="#kurulum">Kurulumu gör</a>')
kaynak_link = lambda yol, metin: (f'<a href="{gh(yol)}" target="_blank" rel="noopener">{metin}</a>' if GH else f"<code>{yol}</code>")

STIL = open(os.path.join(KOK, "docs", "site", "stil.css"), encoding="utf-8").read()
BETIK = open(os.path.join(KOK, "docs", "site", "betik.js"), encoding="utf-8").read()

govde = f'''
<header class="ust">
  <div class="ust-ic">
    <a class="marka" href="#ust"><span class="dna">DNAMATHOS</span><span class="ayrac">·</span>Maarif Skill Kütüphanesi</a>
    <nav aria-label="Bölümler"><a href="#skiller">Skill'ler</a><a href="#kurallar">MEB kuralları</a><a href="#akislar">İş akışları</a><a href="#kurulum">Kurulum</a><a href="#sss">SSS</a></nav>
  </div>
</header>
<main id="ust">
<section class="kahraman bant">
  <div class="ic kahraman-ic">
    <div class="kahraman-metin">
      <p class="ust-etiket">Öğretmenler için Claude skill'leri</p>
      <h1>Programdan soruya, <em>her adımı Maarif'e bağlı.</em></h1>
      <p class="giris">{E(K['tanitim'])}</p>
      <div class="dugmeler">{github_btn}<a class="ikincil" href="#skiller">Skill'leri incele</a></div>
      <ul class="rakamlar" aria-label="Kütüphane özeti">
        <li><strong>{len(S)}</strong> skill</li><li><strong>{len(MEV)}</strong> MEB kuralı</li><li><strong>{len(paketler)}</strong> paket</li>
      </ul>
    </div>
    <figure class="zincir" aria-label="Bir sorunun programa bağlanma zinciri">
      <figcaption>Bir yazılı sorusunun kimliği</figcaption>
      <ol>
        <li><span class="kod">MAT.6.1.1</span><span>Karşılaştığı problem durumlarında bir doğal sayının çarpan ve katlarına yönelik muhakeme yapabilme</span><small>Öğrenme çıktısı · TYMM</small></li>
        <li><span class="kod">6.1.1-a</span><span>Karşılaştığı durumlarda bir doğal sayının çarpan ve katlarına yönelik varsayımlarda bulunur.</span><small>Süreç bileşeni · birebir</small></li>
        <li><span class="kod">KB2.10.SB1</span><span>Çıkarım Yapma · varsayımda bulunma</span><small>Beceri basamağı</small></li>
        <li><span class="kod">MEV-10</span><span>Açık uçlu; cevabı öğrenci oluşturur</span><small>MEB yazılı kuralı</small></li>
        <li class="son"><span class="kod">Soru 1.a</span><span>“… sayısının katlarına ilişkin bir tahminde bulununuz.”</span><small>Öğrenciye giden yönerge</small></li>
      </ol>
    </figure>
  </div>
</section>

<section class="bant acik">
  <div class="ic">
    <h2>Dört ilke</h2>
    <div class="ilkeler">{"".join(f'<div class="ilke"><h3>{E(i["baslik"])}</h3><p>{E(i["metin"])}</p></div>' for i in K["ilkeler"])}</div>
  </div>
</section>

<section class="bant" id="nasil">
  <div class="ic">
    <h2>Her skill aynı yolu izler</h2>
    <ol class="iskelet">
      <li><strong>Programı okur</strong><span>Maarif çerçevesi ve dersin başvuru dosyası</span></li>
      <li><strong>En çok bir soru sorar</strong><span>Yalnız ürünü değiştirecekse</span></li>
      <li><strong>Programa dayandırır</strong><span>Çıktı, bileşen ve sınırlar TYMM sayfasından</span></li>
      <li><strong>Üretir</strong><span>Tek kaynaktan bütün belgeler</span></li>
      <li><strong>Denetler</strong><span>Tek cevap, çeldirici, kod, puan, sızıntı, MEB kuralları</span></li>
      <li><strong>Teslim eder</strong><span>Kısa özet ve en çok iki somut öneri</span></li>
    </ol>
  </div>
</section>

<section class="bant acik" id="skiller">
  <div class="ic">
    <div class="baslik-satir">
      <h2>Hangi iş için hangi skill?</h2>
      <div class="suzgec" role="group" aria-label="Skill grubunu seç">
        <button type="button" class="secili" data-grup="hepsi" aria-pressed="true">Hepsi</button>
        <button type="button" data-grup="plan" aria-pressed="false">Planlama</button>
        <button type="button" data-grup="olcme" aria-pressed="false">Ölçme ve değerlendirme</button>
        <button type="button" data-grup="icerik" aria-pressed="false">İçerik üretimi</button>
      </div>
    </div>
    <label class="ara" for="ara">Ara <input id="ara" type="search" placeholder="ör. çıkış kartı, yazılı, BEP" autocomplete="off"></label>
    <div class="kartlar">{"".join(kartlar)}</div>
    <p class="bos" id="bos" hidden>Bu aramaya uyan skill yok. Başka bir sözcük deneyin.</p>
  </div>
</section>

<section class="bant" id="kurallar">
  <div class="ic">
    <h2>MEB ölçme ve değerlendirme kuralları</h2>
    <p class="aciklama">Skill'ler soru hazırlarken Millî Eğitim Bakanlığı Ölçme ve Değerlendirme Yönetmeliği, Yazılı ve Uygulamalı Sınavlar Yönergesi ve Kılavuzundaki bu kurallara uyar. Kurallar madde özetidir; birebir metin için <a href="https://odsgm.meb.gov.tr/meb_iys_dosyalar/2024_02/07101329_odsgm_mevzuat_kitapcigi.pdf" target="_blank" rel="noopener">ODSGM mevzuat kitapçığına</a> bakın.</p>
    <div class="tablo-kap"><table class="mev-tablo">
      <thead><tr><th scope="col">Kod</th><th scope="col">Kural</th><th scope="col">Dayanak</th></tr></thead>
      <tbody>{"".join(mev_satir)}</tbody>
    </table></div>
  </div>
</section>

<section class="bant acik" id="akislar">
  <div class="ic">
    <h2>İş akışları</h2>
    <p class="aciklama">Aynı sohbette sırayla çalıştırın; bir skill'in ürünü sonrakinin girdisidir.</p>
    <div class="akislar">{akis_html}</div>
  </div>
</section>

<section class="bant" id="kurulum">
  <div class="ic">
    <h2>Kurulum: üç yol</h2>
    <ol class="kurulum">{"".join(f'<li><h3>{E(k["baslik"])}</h3><p>{E(k["metin"])}</p></li>' for k in K["kurulum"])}</ol>
    <h3 class="alt">Paketler</h3>
    <div class="tablo-kap"><table class="paket-tablo"><thead><tr><th scope="col">Paket</th><th scope="col">İçerik</th><th scope="col">Skill</th></tr></thead><tbody>{paket_html}</tbody></table></div>
    <p class="aciklama">Ayrıntılı kılavuz: {kaynak_link("docs/kilavuz.md", "docs/kilavuz.md")} · Katalog: {kaynak_link("KATALOG.md", "KATALOG.md")} · Katkı kuralları: {kaynak_link("KATKI.md", "KATKI.md")}</p>
  </div>
</section>

<section class="bant acik" id="sss">
  <div class="ic dar">
    <h2>Sık sorulanlar</h2>
    {sss_html}
  </div>
</section>
</main>
<footer class="alt-bilgi">
  <div class="ic">
    <p><strong>DNAMATHOS</strong> · Maarif Skill Kütüphanesi. Program metinleri ve kodları Millî Eğitim Bakanlığına aittir (<a href="https://tymm.meb.gov.tr" target="_blank" rel="noopener">tymm.meb.gov.tr</a>).</p>
    <p>Ders planı, farklılaştırma, derse hazırlık ve anlama kontrolü skill'leri <a href="https://github.com/anthropics/k12-teacher-skills" target="_blank" rel="noopener">anthropics/k12-teacher-skills</a> (Apache-2.0) çalışmasından uyarlanmıştır. Lisans ayrıntısı: {kaynak_link("LISANS.md", "LISANS.md")}.</p>
  </div>
</footer>
'''

bas = '''<title>Maarif Skill Kütüphanesi</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Maarif Modeli'ne bağlı, MEB ölçme kurallarına uygun öğretmen skill'leri.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;700&family=Fraunces:ital,wght@0,600;0,800;1,600&family=IBM+Plex+Mono:wght@500;600&family=Caveat:wght@700&family=Inter:wght@400;700&display=swap">
'''
parca = bas + f"<style>{STIL}</style>\n" + govde + f"\n<script>{BETIK}</script>\n"
tam = ('<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + bas + f"<style>{STIL}</style>\n</head>\n<body>\n" + govde + f"\n<script>{BETIK}</script>\n</body>\n</html>\n")
open(os.path.join(KOK, "docs", "index.html"), "w", encoding="utf-8").write(tam)
open(os.path.join(KOK, "docs", ".nojekyll"), "w").write("")
if a.parca:
    open(a.parca, "w", encoding="utf-8").write(parca)
print(f"kilavuz.md ve index.html üretildi · {len(S)} skill · {len(MEV)} MEV kuralı · depo: {DEPO or 'yok'}")
