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

# --- 2. İstem kütüphanesi: istemler/<skill>.md -----------------------------
IS = yaml.safe_load(open(os.path.join(KOK, "docs", "istemler.yaml"), encoding="utf-8"))
SEKME = {s["id"]: s["ad"] for s in IS["sekmeler"]}
skill_istem = {}
for x in IS["istemler"]:
    skill_istem.setdefault(x["skill"], []).append(x)
for s, xs in skill_istem.items():
    m = [f"# {s} — hazır istemler", "", "> Bu dosya `docs/istemler.yaml` dosyasından üretilir; elle düzenlenmez.", "",
         "Köşeli parantezleri doldurup kopyala. Skill yüklü değilse istemin başına şunu ekle: \"Maarif Modeli'ne uygun çalış; çıktıları TYMM sayfasından doğrula.\"", ""]
    for x in xs:
        m += [f"## {x['baslik']}", "", x["aciklama"], "", "```", x["istem"], "```", ""]
    open(os.path.join(KOK, "istemler", f"{s}.md"), "w", encoding="utf-8").write("\n".join(m))

# --- 3. Tanıtım sayfası (panel düzeni) -------------------------------------
GRUP_KISA = {"Planlama": "plan", "Ölçme ve değerlendirme": "olcme", "İçerik üretimi": "icerik"}
liste = lambda xs: "".join(f"<li>{E(x)}</li>" for x in xs)
yer = lambda s: re.sub(r"\[([^\]]+)\]", r'<span class="yer">[\1]</span>', E(s))
IK = {
 "basla": '<path d="M4 12h14M13 6l6 6-6 6"/>',
 "yenilikler": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
 "skiller": '<rect x="4" y="4" width="7" height="7" rx="2"/><rect x="13" y="4" width="7" height="7" rx="2"/><rect x="4" y="13" width="7" height="7" rx="2"/><rect x="13" y="13" width="7" height="7" rx="2"/>',
 "istemler": '<path d="M5 7l5 5-5 5M12 17h7"/>',
 "kurallar": '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 12h7M9 16h7"/>',
 "akislar": '<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="12" r="2.5"/><circle cx="6" cy="18" r="2.5"/><path d="M8.5 6h4a3 3 0 0 1 3 3v.5M15.5 14.5V15a3 3 0 0 1-3 3h-4"/>',
 "dosyalar": '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
 "ipuclari": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
 "destek": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"/>',
}
svg = lambda k: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IK[k]}</svg>'
MENU = [("Başla", [("basla", "Başla", ""), ("yenilikler", "Yenilikler", str(len(IS["yenilikler"])))]),
        ("Kütüphane", [("skiller", "Skill'ler", str(len(S))), ("istemler", "İstemler", str(len(IS["istemler"]))), ("kurallar", "MEB kuralları", str(len(MEV))), ("akislar", "İş akışları", str(len(akis)))]),
        ("Yardım", [("dosyalar", "Dosyalar", ""), ("ipuclari", "İpuçları", ""), ("destek", "Destek", "")])]
menu_html = "".join(f'<div class="grup">{E(g)}</div>' + "".join(f'<a href="#{k}">{svg(k)}<span>{E(ad)}</span>{f"<span class=sayi>{n}</span>" if n else ""}</a>' for k, ad, n in xs) for g, xs in MENU)

def sarmal_svg(w=200, h=40, n=10):
    import math
    y = lambda x: h / 2 + (h / 2 - 4) * math.sin(x / w * 3 * math.pi)
    p1 = " ".join(f"{x},{y(x):.1f}" for x in range(0, w + 1, 4)); p2 = " ".join(f"{x},{h - y(x):.1f}" for x in range(0, w + 1, 4))
    r = "".join(f'<line x1="{8 + i * (w - 16) / (n - 1):.1f}" y1="{y(8 + i * (w - 16) / (n - 1)):.1f}" x2="{8 + i * (w - 16) / (n - 1):.1f}" y2="{h - y(8 + i * (w - 16) / (n - 1)):.1f}" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>' for i in range(n))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">{r}<polyline points="{p1}" fill="none" stroke="var(--metin)" stroke-width="2"/><polyline points="{p2}" fill="none" stroke="currentColor" stroke-width="2"/></svg>'

def bas(etiket, baslik, alt):
    return f'<p class="ust-etiket">{etiket}</p><h1>{baslik}</h1><p class="alt-yazi">{alt}</p>'

def mev_cip(c):
    return f'<a class="cip" href="#{c.lower()}" title="{E(re.sub(r"[*`]", "", MEV[c]["kural"]))}">{c}</a>'

# İstemler
istem_kart = []
for n, x in enumerate(IS["istemler"]):
    istem_kart.append(f'''<article class="istem" data-sekme="{x['sekme']}"><h3>{E(x['baslik'])}</h3><p class="ne">{E(x['aciklama'])}</p>
<div class="kutu"><pre id="ist{n}">{yer(x['istem'])}</pre><div class="alt"><a class="skill" href="#{x['skill']}">{x['skill']}</a><button type="button" class="kopyala" data-hedef="ist{n}">Kopyala</button></div></div></article>''')
sekme_btn = lambda hedef, ler: (f'<div class="sekmeler" role="group" aria-label="Süzgeç" data-hedef="{hedef}"><button type="button" data-sekme="hepsi" aria-pressed="true">Tümü</button>'
                                 + "".join(f'<button type="button" data-sekme="{i}" aria-pressed="false">{E(a)}</button>' for i, a in ler) + "</div>")

# Skill kartları
skill_kart = []
for g in K["gruplar"]:
    for s in g["skills"]:
        d = S[s]
        zipl = ham(f"dist/zip/{s}.zip")
        skill_kart.append(f'''<article class="skill-kart" id="{s}" data-sekme="{GRUP_KISA[g['ad']]}"><h3>{E(d['gorunen'])}</h3><code class="ad">{s}</code><p>{E(d['ne_yapar'])}</p>
<div class="cipler">{"".join(mev_cip(c) for c in d["mevzuat"]) or '<span class="cip">Ölçme ürünü üretmez</span>'}</div>
<details><summary>Nasıl kullanılır?</summary><dl><dt>Ne zaman</dt><dd><ul>{liste(d['ne_zaman'])}</ul></dd><dt>Siz verin</dt><dd><ul>{liste(d['verin'])}</ul></dd>
<dt>Siz alırsınız</dt><dd><ul>{liste(d['alirsiniz'])}</ul></dd><dt>Örnek istem</dt><dd>{yer(d['istem'])}</dd><dt>Kontrol edin</dt><dd>{E(d['kontrol'])}</dd>
<dt>Sonra</dt><dd><a href="#{d['sonraki']}">{E(S[d['sonraki']]['gorunen'])}</a></dd></dl>{f'<p class="not-satiri"><a href="{zipl}" target="_blank" rel="noopener">Skill dosyasını indir (.zip)</a></p>' if zipl else ""}</details></article>''')

mev_satir = "".join(f'<tr id="{c.lower()}"><th scope="row">{c}</th><td>{md_satir(v["kural"])}</td><td class="dayanak">{E(v["dayanak"])}</td></tr>' for c, v in MEV.items())
akis_html = "".join(f'<section class="akis"><h3>{E(b)}</h3><ol>' + "".join(f"<li>{md_satir(x)}</li>" for x in ad) + "</ol></section>" for b, ad in akis)
paket_html = "".join(f'<tr><th scope="row">{E(p["ad"])}</th><td>{E(p["aciklama"])}</td><td>{len(p["skills"])}</td></tr>' for p in paketler)
dosya_satir = "".join(f'<tr><th scope="row">{s}</th><td>{E(S[s]["gorunen"])}</td><td>' + (f'<a href="{ham(f"dist/zip/{s}.zip")}" target="_blank" rel="noopener">İndir</a>' if GH else f"<code>dist/zip/{s}.zip</code>") + "</td></tr>" for g in K["gruplar"] for s in g["skills"])
kaynak = lambda yol, metin: (f'<a href="{gh(yol)}" target="_blank" rel="noopener">{metin}</a>' if GH else f"<code>{yol}</code>")
FORM = "Skill:\nSınıf ve ders:\nİstem (kısaca):\nÜrün işinizi gördü mü? (evet / kısmen / hayır)\nProgram uyumu doğru muydu? (çıktı, bileşen, sınır)\nDüzeltmek zorunda kaldığınız yer:\nÖğrencilerde gözlediğiniz:"

govde = f'''<div class="kabuk">
<aside class="panel" aria-label="Menü">
  <a class="marka" href="#basla"><b>DNA</b><i>mathos</i><span>MAARİF</span></a>
  <div class="karsilama"><div class="selam">Merhaba öğretmenim<small>{len(S)} SKILL · {len(MEV)} MEB KURALI</small></div><div class="el">her soru bir çıktıya bağlı</div>
    <a class="cta" href="#istemler"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 7h11l-3-3M17 17H6l3 3"/></svg>İstemlere geç</a></div>
  <nav class="menu">{menu_html}</nav>
  <div class="sarmal">{sarmal_svg()}</div>
</aside>
<main class="gorunum">
<section id="g-basla">
  <div class="kahraman"><div>{bas("Öğretmenler için Claude skill'leri", "Programdan soruya, <em>her adımı Maarif'e bağlı.</em>", E(K["tanitim"]))}
    <a class="cta" href="#istemler" style="display:inline-flex">İstemlere göz at</a> <span class="el-not">önce çıktı kartını iste</span></div>
    <figure class="zincir"><figcaption>Bir yazılı sorusunun kimliği</figcaption><ol>
      <li><span class="kod">MAT.6.1.4</span><span>Ortak kat ve ortak böleni yorumlayabilme</span><small>Öğrenme çıktısı · TYMM</small></li>
      <li><span class="kod">6.1.4-a</span><span>Verilen iki sayının ortak katlarını ve ortak bölenlerini inceler.</span><small>Süreç bileşeni</small></li>
      <li><span class="kod">KB2.4</span><span>Çözümleme</span><small>Beceri</small></li>
      <li><span class="kod">MEV-10</span><span>Açık uçlu; cevabı öğrenci oluşturur</span><small>MEB yazılı kuralı</small></li>
      <li class="son"><span class="kod">Soru 1.a</span><span>“… birlikte kalktığı saatleri yazınız.”</span><small>Öğrenciye giden yönerge</small></li></ol></figure></div>
  <h2 class="bolum">Dört ilke</h2>
  <div class="ilkeler">{"".join(f'<div class="ilke"><h3>{E(i["baslik"])}</h3><p>{E(i["metin"])}</p></div>' for i in K["ilkeler"])}</div>
  <h2 class="bolum">Her skill aynı yolu izler</h2>
  <ol class="iskelet"><li><strong>Programı okur</strong><span>Maarif çerçevesi ve ders dosyası</span></li><li><strong>En çok bir soru sorar</strong><span>Yalnız ürünü değiştirecekse</span></li><li><strong>Programa dayandırır</strong><span>Çıktı, bileşen ve sınırlar sayfadan</span></li><li><strong>Üretir</strong><span>Tek kaynaktan bütün belgeler</span></li><li><strong>Denetler</strong><span>Tek cevap, çeldirici, kod, puan, sızıntı, MEB</span></li><li><strong>Teslim eder</strong><span>Kısa özet, en çok iki öneri</span></li></ol>
  <h2 class="bolum">Haftalık döngü</h2>
  <ol class="dongu"><li><b>Isınma</b><small>5 dk, geçen haftalar</small></li><li><b>Konu</b><small>kart ve ardındaki soru</small></li><li><b>Kaydet</b><small>kural ve slogan</small></li><li><b>Kavrama testi</b><small>4 soru, notsuz</small></li><li><b>Hedefli ödev</b><small>yalnız takılan yere</small></li></ol>
  <p class="not-satiri">Konu özeti istediğinizde bu döngünün tamamı tek istekle gelir.</p>
</section>
<section id="g-yenilikler" hidden>{bas("Yenilikler", "Neler değişti?", "Kütüphanenin son sürümleri.")}
  {"".join(f'<article class="yenilik"><time>{E(y["tarih"])}</time><div><h3>{E(y["baslik"])}</h3><p>{E(y["metin"])}</p></div></article>' for y in IS["yenilikler"])}</section>
<section id="g-istemler" hidden>{bas("İstem kütüphanesi", "Claude'a ne yazmalı?", 'Kopyala, Claude\'a yapıştır. <span class="yer">[Safran]</span> yerleri kendi bilginle değiştir.')}
  {sekme_btn("istem-izgara", SEKME.items())}<div class="izgara" id="istem-izgara">{"".join(istem_kart)}</div></section>
<section id="g-skiller" hidden>{bas("Skill kataloğu", "Hangi iş için hangi skill?", "Her skill bir öğretmen işini baştan sona yapar ve ürettiği her şeyi bir öğrenme çıktısına bağlar.")}
  {sekme_btn("skill-izgara", [("plan", "Planlama"), ("olcme", "Ölçme ve değerlendirme"), ("icerik", "İçerik üretimi")])}<div class="izgara" id="skill-izgara">{"".join(skill_kart)}</div></section>
<section id="g-kurallar" hidden>{bas("MEB ölçme kuralları", "Soru yazarken uyulan kurallar", 'Ölçme ve Değerlendirme Yönetmeliği, Yazılı ve Uygulamalı Sınavlar Yönergesi ve Kılavuzundan madde özetleri. Birebir metin: <a href="https://odsgm.meb.gov.tr/meb_iys_dosyalar/2024_02/07101329_odsgm_mevzuat_kitapcigi.pdf" target="_blank" rel="noopener">ODSGM mevzuat kitapçığı</a>.')}
  <div class="tablo-kap"><table><thead><tr><th scope="col">Kod</th><th scope="col">Kural</th><th scope="col">Dayanak</th></tr></thead><tbody>{mev_satir}</tbody></table></div></section>
<section id="g-akislar" hidden>{bas("İş akışları", "Skill'leri sırayla kullanın", "Aynı sohbette çalıştırın; bir skill'in ürünü sonrakinin girdisidir.")}<div class="akislar">{akis_html}</div></section>
<section id="g-dosyalar" hidden>{bas("Dosyalar", "Kurulum ve indirme", "Üç yoldan biriyle başlayın.")}
  <ol class="uc-yol">{"".join(f'<li><h3>{E(k["baslik"])}</h3><p>{E(k["metin"])}</p></li>' for k in K["kurulum"])}</ol>
  <h2 class="bolum">Skill dosyaları</h2><div class="tablo-kap"><table><thead><tr><th scope="col">Skill</th><th scope="col">Ad</th><th scope="col">Dosya</th></tr></thead><tbody>{dosya_satir}</tbody></table></div>
  <h2 class="bolum" style="margin-top:26px">Paketler</h2><div class="tablo-kap"><table><thead><tr><th scope="col">Paket</th><th scope="col">İçerik</th><th scope="col">Skill</th></tr></thead><tbody>{paket_html}</tbody></table></div>
  <p class="not-satiri">Ayrıntılı kılavuz: {kaynak("docs/kilavuz.md", "docs/kilavuz.md")} · Katalog: {kaynak("KATALOG.md", "KATALOG.md")} · Lisans: {kaynak("LISANS.md", "LISANS.md")}</p></section>
<section id="g-ipuclari" hidden>{bas("İpuçları", "Daha iyi sonuç için", "Kısa ve işe yarar alışkanlıklar.")}
  <ol class="ipuclari">{liste(IS["ipuclari"])}</ol><h2 class="bolum">Sık sorulanlar</h2>{"".join(f'<details class="sss"><summary>{E(q["soru"])}</summary><p>{E(q["cevap"])}</p></details>' for q in K["sss"])}</section>
<section id="g-destek" hidden>{bas("Destek", "Geri bildirim ve katkı", "Bir skill'i sınıfta denediyseniz bu formu doldurup bize iletin; sorunlar ders dosyasına ya da teste dönüşür.")}
  <div class="form"><pre id="form">{E(FORM)}</pre><button type="button" class="kopyala" data-hedef="form">Kopyala</button></div>
  <p class="not-satiri">Katkı kuralları: {kaynak("KATKI.md", "KATKI.md")}. Ders planı, farklılaştırma, derse hazırlık ve anlama kontrolü skill'leri anthropics/k12-teacher-skills (Apache-2.0) çalışmasından uyarlanmıştır. Program metinleri Millî Eğitim Bakanlığına aittir.</p></section>
</main></div>'''

STIL = open(os.path.join(KOK, "docs", "site", "stil.css"), encoding="utf-8").read()
BETIK = open(os.path.join(KOK, "docs", "site", "betik.js"), encoding="utf-8").read()
bas_html = '''<title>Maarif Skill Kütüphanesi</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Maarif Modeli'ne bağlı, MEB ölçme kurallarına uygun öğretmen skill'leri.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;700&family=Fraunces:ital,wght@0,600;0,800;1,600&family=IBM+Plex+Mono:wght@500;600&family=Caveat:wght@700&family=Inter:wght@400;700&display=swap">
'''
parca = bas_html + f"<style>{STIL}</style>\n" + govde + f"\n<script>{BETIK}</script>\n"
tam = ('<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + bas_html + f"<style>{STIL}</style>\n</head>\n<body>\n" + govde + f"\n<script>{BETIK}</script>\n</body>\n</html>\n")
open(os.path.join(KOK, "docs", "index.html"), "w", encoding="utf-8").write(tam)
open(os.path.join(KOK, "docs", ".nojekyll"), "w").write("")
if a.parca:
    open(a.parca, "w", encoding="utf-8").write(parca)
print(f"kilavuz.md, istemler/*.md ve index.html üretildi · {len(S)} skill · {len(IS['istemler'])} istem · {len(MEV)} MEV kuralı · depo: {DEPO or 'yok'}")
