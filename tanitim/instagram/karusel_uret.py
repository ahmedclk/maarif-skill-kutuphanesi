#!/usr/bin/env python3
"""Maarif Skill Kütüphanesi tanıtım karusellerini üretir (DNAMATHOS karusel kuralları, 1080 × 1350 PNG).

Kaynak: docs/kilavuz.yaml. Çıktı: tanitim/instagram/<karusel>/karusel_NN.png, temas.png, aciklama.txt
Kullanım: python3 tanitim/instagram/karusel_uret.py
"""
import html, os, re, sys, yaml
from playwright.sync_api import sync_playwright
from PIL import Image

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CIKTI = os.path.dirname(os.path.abspath(__file__))
K = yaml.safe_load(open(os.path.join(KOK, "docs", "kilavuz.yaml"), encoding="utf-8"))
S = K["skills"]
E = html.escape
# Öğretmen satırı paleti (lacivert; sınıf paletleriyle aynı açıklık düzeni)
P = {"koyu": "#14213d", "cizgi": "#4a5570", "orta": "#d9dde6", "acik": "#f2f4f7"}

CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#888;font-family:Inter,sans-serif;color:#14213d}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{P['acik']};padding:150px 80px 150px}}
.s.koyu{{background:{P['koyu']};color:#fff}}
.hap{{position:absolute;left:80px;top:72px;font:700 26px Inter;letter-spacing:.06em;padding:12px 24px;border-radius:999px;background:{P['orta']};color:{P['koyu']}}}
.koyu .hap{{background:rgba(255,255,255,.12);color:#ffd166}}
.say{{position:absolute;right:80px;top:84px;font:600 26px Inter;color:{P['cizgi']}}}
.koyu .say{{color:#b9c2d6}}
.bar{{position:absolute;left:0;top:0;height:10px;background:#ffd166}}
.marka{{position:absolute;left:80px;bottom:70px;font:800 24px Inter;letter-spacing:.16em;color:{P['cizgi']}}}
.koyu .marka{{color:#b9c2d6}}
.kaydir{{position:absolute;right:80px;bottom:62px;display:flex;align-items:center;gap:18px;font:800 26px Inter;letter-spacing:.18em;color:{P['koyu']}}}
.koyu .kaydir{{color:#ffd166}}
.kaydir svg{{width:110px;height:24px}}
h1{{font:700 112px/1.05 Lora,serif;letter-spacing:-.01em}}
h2{{font:700 92px/1.08 Lora,serif;margin-bottom:56px}}
h1 em,h2 em{{font-style:italic;color:#ffd166}}
.s:not(.koyu) h2 em{{color:{P['cizgi']}}}
p,li{{font-size:52px;line-height:1.35}}
.alt{{font-size:54px;line-height:1.3;color:#d5dbe8;margin-top:44px;max-width:860px}}
.rakam{{position:absolute;right:90px;bottom:112px;font:700 470px/1 Lora,serif;color:rgba(74,85,112,.55);z-index:0}}
.icerik{{position:relative;z-index:1}}
.kutu{{background:#fff;border-radius:22px;padding:44px 48px;border-left:8px solid #ffd166}}
.kutu.kod{{font:500 38px/1.4 'JetBrains Mono','DejaVu Sans Mono',monospace}}
.etiket{{font:700 26px Inter;letter-spacing:.12em;text-transform:uppercase;color:{P['cizgi']};margin-bottom:14px}}
.zincir{{display:flex;flex-direction:column;gap:22px}}
.zincir div{{display:grid;grid-template-columns:300px 1fr;gap:24px;align-items:baseline;background:#fff;border-radius:18px;padding:30px 34px}}
.zincir b{{font:600 34px 'DejaVu Sans Mono',monospace;color:{P['koyu']}}}
.zincir span{{font-size:46px;line-height:1.25}}
.liste{{list-style:none;display:flex;flex-direction:column;gap:26px}}
.liste li{{display:flex;gap:22px;align-items:flex-start}}
.liste li i{{font-style:normal;flex:0 0 52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:800 30px Inter;background:#e1f3f0;color:#0b6157}}
.liste li i.x{{background:#fdece6;color:#b3401a}}
.grup{{margin-bottom:46px}}
.grup .etiket{{margin-bottom:12px}}
.grup p{{font-size:48px;line-height:1.35}}
.yan{{display:grid;grid-template-columns:1fr 1fr;gap:28px}}
.yan .k{{border-radius:22px;padding:34px}}
.yan .k p{{font-size:50px}}
.yanlis{{background:#fdece6;color:#b3401a}} .dogru{{background:#e1f3f0;color:#0b6157}}
.yan .k h3{{font:800 30px Inter;letter-spacing:.08em;margin-bottom:16px}}
.adim{{display:flex;flex-direction:column;gap:46px}}
.adim div{{display:flex;gap:28px;align-items:flex-start}}
.adim b{{flex:0 0 72px;height:72px;border-radius:50%;background:{P['koyu']};color:#ffd166;font:700 38px Lora;display:flex;align-items:center;justify-content:center}}
.adim h3{{font:700 58px Lora;margin-bottom:8px}}
.adim p{{font-size:46px;color:{P['cizgi']}}}
.ad{{font:500 30px 'DejaVu Sans Mono',monospace;color:{P['cizgi']};margin:-26px 0 40px}}
.ne{{font-size:56px;line-height:1.3;margin-bottom:60px}}
.istem{{font-size:48px;line-height:1.38}}
.mev{{margin-top:34px;display:flex;flex-wrap:wrap;gap:12px}}
.mev span{{font:600 30px 'DejaVu Sans Mono',monospace;padding:8px 16px;border-radius:10px;background:{P['orta']};color:{P['koyu']}}}
.cagri{{font:700 50px/1.3 Lora,serif;color:#ffd166;margin-top:56px}}
"""
OK = '<svg viewBox="0 0 110 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h104M94 2l12 10-12 10"/></svg>'


def slayt(i, n, hap, govde, koyu=False, rakam=None):
    son = i == n
    return (f'<section class="s{" koyu" if koyu else ""}" id="s{i}"><div class="bar" style="width:{1080 * i / n:.0f}px"></div>'
            f'<div class="hap">{E(hap)}</div><div class="say">{i} / {n}</div>'
            + (f'<div class="rakam">{rakam}</div>' if rakam else "")
            + f'<div class="icerik">{govde}</div><div class="marka">DNAMATHOS</div>'
            + ("" if son else f'<div class="kaydir">KAYDIR {OK}</div>') + "</section>")


def tanitim():
    n = 9
    sl = [
        slayt(1, n, "Öğretmenlere", "<h1>Claude'a Maarif'i <em>öğrettik</em></h1>"
              "<p class='alt'>15 skill, tek omurga: her soru bir öğrenme çıktısına bağlı.</p>", True, "15"),
        slayt(2, n, "Sorun", "<h2>Hızlı soru, <em>yanlış adres</em></h2><ul class='liste'>"
              "<li><i class='x'>✗</i><span>Hangi çıktıyı ölçtüğünü bilmez.</span></li>"
              "<li><i class='x'>✗</i><span>İçerik çerçevesi sınırını aşar.</span></li>"
              "<li><i class='x'>✗</i><span>Yazılı için çoktan seçmeli önerir.</span></li></ul>"
              "<p style='margin-top:56px;color:#4a5570'>Ama bunu nasıl çözeriz?</p>"),
        slayt(3, n, "Çözüm", "<h2>Skill: Claude'un <em>iş tarifi</em></h2>"
              "<p>Skill, Claude'un bir işi baştan sona nasıl yapacağını anlatan dosyadır.</p>"
              "<div class='kutu' style='margin-top:48px'><p>Ortak yazılı isterseniz Claude önce programı okur, sonra soruyu yazar, en son kendini denetler.</p></div>"),
        slayt(4, n, "Nasıl çalışır?", "<h2>Bir sorunun <em>kimliği</em></h2><div class='zincir'>"
              "<div><b>MAT.6.1.1</b><span>Öğrenme çıktısı</span></div>"
              "<div><b>6.1.1-a</b><span>Süreç bileşeni: varsayımda bulunur</span></div>"
              "<div><b>KB2.10.SB1</b><span>Beceri basamağı</span></div>"
              "<div><b>MEV-10</b><span>MEB kuralı: açık uçlu</span></div>"
              "<div><b>Soru 1.a</b><span>“… tahminde bulununuz.”</span></div></div>"),
        slayt(5, n, "MEB kuralları", "<h2>Mevzuata <em>uygun</em></h2><ul class='liste'>"
              "<li><i>✓</i><span>Okul yazılısı açık uçlu.</span></li>"
              "<li><i>✓</i><span>100 puan; yanlış doğruyu götürmez.</span></li>"
              "<li><i>✓</i><span>Bir ders saatine sığar.</span></li>"
              "<li><i>✓</i><span>Kısa süreli sınav notsuz.</span></li>"
              "<li><i>✓</i><span>İlkokulda sınav yok.</span></li></ul>"),
        slayt(6, n, "Kütüphane", "<h2>15 skill, <em>üç grup</em></h2>"
              + "".join(f"<div class='grup'><div class='etiket'>{E(g['ad'])}</div><p>{E(', '.join(S[s]['gorunen'] for s in g['skills']))}</p></div>" for g in K["gruplar"])),
        slayt(7, n, "Sık hata", "<h2>Test, yazılının <em>yerine geçmez</em></h2><div class='yan'>"
              "<div class='k yanlis'><h3>✗ YANLIŞ</h3><p>20 soruluk çoktan seçmeli testi okul yazılısı yapmak</p></div>"
              "<div class='k dogru'><h3>✓ DOĞRU</h3><p>Yazılıda açık uçlu sorular; test LGS hazırlığı ve taramada</p></div></div>"),
        slayt(8, n, "Başlarken", "<h2>Üç yol, <em>tek kural</em></h2><div class='adim'>"
              "<div><b>1</b><section><h3>Hazır istem</h3><p>Kopyala, doldur, yapıştır.</p></section></div>"
              "<div><b>2</b><section><h3>Skill yükle</h3><p>Zip dosyasını ayarlardan yükle.</p></section></div>"
              "<div><b>3</b><section><h3>Paket kur</h3><p>Claude Code eklentisi olarak.</p></section></div></div>"
              "<p style='margin-top:48px'>Kural: son kontrol her zaman öğretmenin.</p>"),
        slayt(9, n, "Kaydet", "<h1 style='font-size:96px'>Zümrenle <em>paylaş</em></h1>"
              "<p class='alt'>Kılavuz, kurallar ve bütün skill'ler tanıtım sayfasında.</p>"
              "<p class='cagri'>Sonraki derse hazırlanırken açmak için kaydet.</p>", True),
    ]
    alt = ["Kapak: Claude'a Maarif'i öğrettik; 15 skill, her soru bir öğrenme çıktısına bağlı.",
           "Sorun: yapay zekâ hangi çıktıyı ölçtüğünü bilmez, sınırı aşar, yazılı için çoktan seçmeli önerir.",
           "Çözüm: skill, Claude'un bir işi baştan sona nasıl yapacağını anlatan dosyadır.",
           "Bir sorunun kimliği: öğrenme çıktısı MAT.6.1.1, bileşen 6.1.1-a, beceri basamağı KB2.10.SB1, MEB kuralı MEV-10, soru 1.a.",
           "MEB kuralları: yazılı açık uçlu, 100 puan, bir ders saati, kısa süreli sınav notsuz, ilkokulda sınav yok.",
           "Kütüphane: planlama, ölçme ve değerlendirme, içerik üretimi gruplarında 15 skill.",
           "Sık hata: çoktan seçmeli test okul yazılısının yerine geçmez.",
           "Başlarken: hazır istem, skill yükleme ya da paket kurma; son kontrol öğretmenin.",
           "Kapanış: zümrenle paylaş, kaydet."]
    acik = ("Yapay zekâ soruyu hızlı yazar; ama hangi öğrenme çıktısını ölçtüğünü bilir mi?\n\n"
            "Maarif Skill Kütüphanesi'nde her ders planı, yazılı ve test önce programı okur, sonra MEB ölçme kurallarına göre yazılır ve en son kendini denetler.\n\n"
            "Sonraki derse hazırlanırken açmak için kaydet; zümrenle paylaş.\n\n#maarifmodeli #öğretmen #ölçmedeğerlendirme #yapayzeka #dnamathos")
    return "tanitim", sl, alt, acik


def kilavuz():
    sira = [s for g in K["gruplar"] for s in g["skills"]]
    n = len(sira) + 2
    grup_ad = {s: g["ad"] for g in K["gruplar"] for s in g["skills"]}
    sl = [slayt(1, n, "Kullanım kılavuzu", "<h1>Hangi iş için <em>hangi skill?</em></h1>"
                "<p class='alt'>15 skill; her birinin ne yaptığı ve hazır bir istem.</p>", True, "15")]
    alt = ["Kapak: Hangi iş için hangi skill? 15 skill ve hazır istemleri."]
    for i, s in enumerate(sira, 2):
        d = S[s]
        mev = "".join(f"<span>{c}</span>" for c in d["mevzuat"][:4])
        sl.append(slayt(i, n, grup_ad[s], f"<h2>{E(d['gorunen'])}</h2><div class='ad'>{s}</div>"
                        f"<p class='ne'>{E(d['ne_yapar'])}</p><div class='kutu'><div class='etiket'>Örnek istem</div>"
                        f"<p class='istem'>{E(d['istem'])}</p></div>" + (f"<div class='mev'>{mev}</div>" if mev else "")))
        alt.append(f"{d['gorunen']}: {d['ne_yapar']} Örnek istem: {d['istem']}")
    sl.append(slayt(n, n, "Kaydet", "<h1 style='font-size:96px'>Hepsi <em>tek sayfada</em></h1>"
                    "<p class='alt'>Ayrıntılı kılavuz, MEB kuralları ve kurulum tanıtım sayfasında.</p>"
                    "<p class='cagri'>Bu istemleri bulmak için kaydet.</p>", True))
    alt.append("Kapanış: ayrıntılı kılavuz tanıtım sayfasında; kaydet.")
    acik = ("Ortak yazılı mı, çıkış kartı mı, hata analizi mi? Her iş için ayrı bir skill var.\n\n"
            "Bu karuselde 15 skill'in her biri için ne yaptığını ve kopyalayıp kullanabileceğin bir istemi bulacaksın.\n\n"
            "Bu istemleri bulmak için kaydet.\n\n#maarifmodeli #öğretmen #dersplanı #yazılısınav #dnamathos")
    return "kilavuz", sl, alt, acik


DENETIM = """() => {
 const out=[]; let enkucuk=999;
 document.querySelectorAll('.s').forEach(s=>{
  const r=s.getBoundingClientRect();
  s.querySelectorAll('.icerik *').forEach(e=>{
   const b=e.getBoundingClientRect(); if(!b.width) return;
   if(b.left<r.left+60||b.right>r.right-60||b.top<r.top+100||b.bottom>r.bottom-100) out.push(s.id+': '+e.tagName+' '+(e.textContent||'').slice(0,30));
   if(e.childNodes.length&&[...e.childNodes].some(c=>c.nodeType===3&&c.textContent.trim())) enkucuk=Math.min(enkucuk,parseFloat(getComputedStyle(e).fontSize));
  });
 });
 return {sorun:out, enkucuk};
}"""


def sozcuk(h):
    return len(re.sub(r"<[^>]+>", " ", h).split())


def uret(ad, sl, alt, acik):
    kl = os.path.join(CIKTI, ad); os.makedirs(kl, exist_ok=True)
    for f in os.listdir(kl):
        if f.endswith(".png"): os.remove(os.path.join(kl, f))
    html_yol = os.path.join(kl, "karusel.html")
    open(html_yol, "w", encoding="utf-8").write(f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(sl)}</body></html>")
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pg.goto("file://" + html_yol); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        d = pg.evaluate(DENETIM)
        yollar = []
        for i, el in enumerate(pg.query_selector_all(".s"), 1):
            y = os.path.join(kl, f"karusel_{i:02d}.png"); el.screenshot(path=y); yollar.append(y)
        b.close()
    for i, h in enumerate(sl, 1):
        w = sozcuk(h.split('<div class="icerik">')[1].split('<div class="marka">')[0])
        if w > 40: print(f"  UYARI {ad} {i}: {w} sözcük")
    # temas tablosu
    k = 5; sat = (len(yollar) + k - 1) // k; tw, th = 216, 270
    tt = Image.new("RGB", (k * tw + (k + 1) * 12, sat * th + (sat + 1) * 12), "#cfd4de")
    for i, y in enumerate(yollar):
        im = Image.open(y).resize((tw, th)); tt.paste(im, (12 + (i % k) * (tw + 12), 12 + (i // k) * (th + 12)))
    tt.save(os.path.join(kl, "temas.png"))
    Image.open(yollar[0]).crop((34, 0, 1046, 1350)).save(os.path.join(kl, "kapak_3x4.png"))
    with open(os.path.join(kl, "aciklama.txt"), "w", encoding="utf-8") as f:
        f.write(acik + "\n\nAlternatif metinler:\n" + "\n".join(f"{i}. {t}" for i, t in enumerate(alt, 1)) + "\n")
    print(f"{ad}: {len(yollar)} slayt · güvenli alan dışı: {len(d['sorun'])} · en küçük yazı {d['enkucuk']}px")
    for s in d["sorun"][:10]: print("  ", s)


for f in (tanitim, kilavuz):
    uret(*f())
