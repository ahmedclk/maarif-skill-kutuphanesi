#!/usr/bin/env python3
"""Örnek: 6. sınıf MAT.6.1.4 (ortak kat ve ortak bölen) için haftalık kavrama testi ve ders başı hızlı tekrar.

maarif-kavrama-testi ve maarif-hizli-tekrar skill'lerinin kurallarıyla üretilmiştir. Bütün cevaplar aşağıda kodla
hesaplanır ve assert ile denetlenir.
Çıktılar: kavrama_testi_ogrenci.pdf, kavrama_testi_ogretmen.pdf, hizli_tekrar_kartlari.pdf, hizli_tekrar_ogretmen.pdf
"""
import html, math, os
from playwright.sync_api import sync_playwright

KL = os.path.dirname(os.path.abspath(__file__))
E = html.escape
bol = lambda n: [d for d in range(1, n + 1) if n % d == 0]
ortak_bolen = lambda a, b: sorted(set(bol(a)) & set(bol(b)))
ortak_kat = lambda a, b, ust: [k for k in range(1, ust + 1) if k % a == 0 and k % b == 0]

# ---------------- Kavrama testi ----------------
assert ortak_kat(6, 8, 50) == [24, 48]
assert ortak_bolen(9, 16) == [1]
ob = ortak_bolen(24, 36); assert ob == [1, 2, 3, 4, 6, 12]
siralar = [d for d in ob if d >= 2]
assert all(24 % n == 0 and 36 % n == 0 for n in siralar)

SORULAR = [
 {"no": 1, "tur": "Küme sorusu", "bilesen": "6.1.4-a, 6.1.4-b",
  "metin": "Sayı doğrusunda 6'nın katlarını doğrunun üstünde, 8'in katlarını altında işaretle. 1 ile 50 arasında hem 6'nın hem 8'in katı olan sayıları yaz.",
  "ek": "doğru", "a": "Ortak katlar:", "b": "Bu sayıları nasıl buldun? Bir cümleyle yaz.",
  "cevap": "24 ve 48", "kabul": ["İkisinin de katı oldukları için; iki sıradaki işaretlerin çakıştığı yerler.", "24, 6 · 4 ve 8 · 3 olduğu için; 48 de 24'ün iki katı."],
  "red": ["6 ile 8'i çarptım (48'i bulur ama 24'ü kaçırır).", "Hesapladım."],
  "hatalar": [("Yalnız 48", "Çarpımı ortak kat sanıyor; ilk ortak katı kaçırıyor. Sayı doğrusundaki çakışmaları birlikte sayın."), ("2, 4 gibi bölenler", "Ortak katı ortak bölenle karıştırıyor. Tanımı 'ikisinin de katı' cümlesiyle yeniden kurun.")],
  "en_zor": "Biri ötekini bölmeyen iki sayı (6 ve 8)."},
 {"no": 2, "tur": "Küme sorusu", "bilesen": "6.1.4-a, 6.1.4-c",
  "metin": "Ece, “9 ile 16'nın hiç ortak böleni yoktur.” diyor. Ece'ye katılıyor musun?",
  "a": "Katılıyorum / Katılmıyorum:", "b": "Neden? 9 ile 16'nın bölenlerini kullanarak açıkla.",
  "cevap": "Katılmıyorum; 1 her iki sayıyı da böler. Ortak bölenleri yalnız 1'dir, yani 9 ile 16 aralarında asaldır.",
  "kabul": ["9'un bölenleri 1, 3, 9; 16'nın bölenleri 1, 2, 4, 8, 16; ortak olan 1.", "1 her sayıyı böler, bu yüzden ortak bölen yok denemez."],
  "red": ["Katılıyorum, çünkü biri tek biri çift.", "Katılmıyorum (gerekçesiz)."],
  "hatalar": [("Katılıyorum", "1'i bölen saymıyor. Bölen listesini 1'den başlatarak yeniden yazdırın."), ("Ortak bölen 3", "Bölenleri karıştırıyor; 3, 16'yı bölmez. Bölmeyi denetletin.")],
  "en_zor": "Ortak böleni yalnız 1 olan (aralarında asal) çift."},
 {"no": 3, "tur": "Aktarım sorusu", "bilesen": "6.1.4-a, 6.1.4-c",
  "metin": "Bir bahçıvan 24 lale ve 36 sümbül dikecek. Her sırada aynı sayıda lale ve aynı sayıda sümbül olacak, hiç çiçek artmayacak. En az 2 sıra olacaksa kaç sıra yapabilir?",
  "a": "Olabilecek sıra sayıları:", "b": "Bu sayıların neden uygun olduğunu açıkla.",
  "cevap": "2, 3, 4, 6 ya da 12 sıra.",
  "kabul": ["Sıra sayısı hem 24'ü hem 36'yı bölmeli; ikisinin ortak bölenleri 2, 3, 4, 6, 12.", "Örneğin 6 sırada her sırada 4 lale ve 6 sümbül olur."],
  "red": ["Yalnız 12 (tek bir cevap verir; en büyüğü sorulmadı).", "72 sıra (ortak katı alır)."],
  "hatalar": [("72 ya da 144", "Bölme gerektiren durumda kata gidiyor. 'Eşit paylaştırma' bölmedir; bölen sorusu olduğunu birlikte bulun."), ("Yalnız 12", "Tek cevap arıyor; bütün ortak bölenleri listeletin.")],
  "en_zor": "Derste görülmemiş bağlamda ortak bölenin seçilmesi."},
 {"no": 4, "tur": "Tekrar sorusu", "bilesen": "6.1.2-ç",
  "metin": "Önermeyi tamamla: “Bir doğal sayı 9'a tam bölünüyorsa ……'e de tam bölünür.”",
  "a": "Boşluğa gelen sayı:", "b": "Neden? Bir örnekle göster.",
  "cevap": "3",
  "kabul": ["9, 3'ün katı olduğu için; örneğin 27 hem 9'a hem 3'e bölünür.", "Rakamları toplamı 9'un katıysa 3'ün de katıdır."],
  "red": ["Tersini söyler: 3'e bölünen 9'a da bölünür (12 karşı örnektir)."],
  "hatalar": [("9 dışında bir sayı (ör. 6)", "Kuralları karıştırıyor; 9 = 3 · 3 ilişkisini gösterin.")],
  "en_zor": "Bölünebilme kuralları arasındaki ilişki (2 hafta önce işlendi)."},
]


def sayi_dogrusu():
    w, x0, x1 = 760, 110, 740
    sx = lambda v: x0 + (x1 - x0) * v / 50
    s = [f'<svg viewBox="0 0 {w} 110" role="img" aria-label="0\'dan 50\'ye sayı doğrusu; 5\'er aralıkla numaralı, her tam sayıda küçük çentik var."><title>0 ile 50 arası sayı doğrusu</title>',
         f'<line x1="{x0}" y1="55" x2="{x1}" y2="55" stroke="#14213d" stroke-width="2"/>']
    for v in range(0, 51):
        h = 9 if v % 5 else 14
        s.append(f'<line x1="{sx(v):.1f}" y1="{55 - h}" x2="{sx(v):.1f}" y2="{55 + h}" stroke="#14213d" stroke-width="{1.6 if v % 5 == 0 else 1}"/>')
        if v % 5 == 0:
            s.append(f'<text x="{sx(v):.1f}" y="92" font-size="14" text-anchor="middle" fill="#14213d">{v}</text>')
    s.append('<text x="0" y="20" font-size="13" fill="#4a5570">6\'nın katları: üste</text><text x="0" y="108" font-size="13" fill="#4a5570">8\'in katları: alta</text></svg>')
    return "".join(s)


CSS_A4 = """
@page{size:A4;margin:16mm 16mm 14mm}
*{box-sizing:border-box}body{font:11pt/1.45 Inter,sans-serif;color:#14213d;margin:0}
h1{font:700 20pt Lora,serif;margin:0}
.ust{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.5pt solid #14213d;padding-bottom:6pt;margin-bottom:8pt}
.ust small{color:#4a5570;font-size:9pt;letter-spacing:.12em;text-transform:uppercase;font-weight:700}
.ad{display:flex;gap:24pt;margin:6pt 0 10pt;font-size:10.5pt}.ad span{flex:1;border-bottom:1pt solid #9aa3b5;padding-bottom:2pt}
.yon{background:#f2f4f7;border-left:3pt solid #ffd166;padding:6pt 9pt;font-size:10pt;margin-bottom:10pt}
.soru{break-inside:avoid;border:1pt solid #d9dde6;border-radius:6pt;padding:8pt 11pt;margin-bottom:7pt;position:relative}
.soru h2{font:700 11.5pt Inter;margin:0 0 4pt;padding-right:118pt}
.guven{position:absolute;right:10pt;top:9pt;font-size:9pt;color:#4a5570;display:flex;gap:8pt}
.guven span::before{content:"";display:inline-block;width:9pt;height:9pt;border:1pt solid #4a5570;border-radius:2pt;margin-right:3pt;vertical-align:-1pt}
.alan{margin-top:6pt;font-size:10pt;font-weight:600}
.satir{border-bottom:1pt dotted #9aa3b5;height:16pt}
svg{width:100%;height:auto;margin-top:2pt}
.dna{margin-top:8pt;font:800 8pt Inter;letter-spacing:.18em;color:#4a5570}
table{border-collapse:collapse;width:100%;font-size:9.5pt;margin:4pt 0 8pt}th,td{border:1pt solid #d9dde6;padding:4pt 6pt;text-align:left;vertical-align:top}th{background:#f2f4f7}
.k{break-inside:avoid;margin-bottom:10pt}.k h2{font:700 12pt Lora,serif;margin:0 0 3pt}.etk{font-size:9pt;color:#4a5570}
ul{margin:2pt 0 4pt;padding-left:14pt}
h3{font:700 10pt Inter;margin:6pt 0 2pt;text-transform:uppercase;letter-spacing:.08em;color:#4a5570}
"""


def ogrenci():
    s = ['<div class="ust"><h1>Bu haftayı kontrol edelim</h1><small>6. sınıf · Ortak kat ve ortak bölen</small></div>',
         '<div class="ad"><span>Ad:</span><span>Tarih:</span></div>',
         '<div class="yon">Her soruda cevabını yaz, sonra nasıl karar verdiğini bir cümleyle açıkla. Sağdaki kutulardan birini işaretle: ne kadar eminsin? Süre: 12 dakika.</div>']
    for q in SORULAR:
        ek = sayi_dogrusu() if q.get("ek") == "doğru" else ""
        s.append(f'<div class="soru"><div class="guven"><span>Eminim</span><span>Emin değilim</span></div><h2>{q["no"]}. {E(q["metin"])}</h2>{ek}'
                 f'<div class="alan">a) {E(q["a"])}</div><div class="satir"></div>'
                 f'<div class="alan">b) {E(q["b"])}</div><div class="satir"></div><div class="satir"></div><div class="satir"></div></div>')
    s.append('<div class="dna">DNAMATHOS</div>')
    return "".join(s)


def ogretmen():
    s = ['<div class="ust"><h1>Kavrama testi · öğretmen anahtarı</h1><small>6. sınıf · 8. hafta · notsuz</small></div>',
         '<table><tr><th>Çıktı</th><td>MAT.6.1.4 Günlük hayat problemleri ya da matematiksel durumlar üzerinden ortak kat ve ortak böleni yorumlayabilme</td></tr>'
         '<tr><th>Kümeler</th><td>Küme 1: a (inceler) + b (temsil eder) · Küme 2: a + c (kendi ifadesiyle açıklar) · Tekrar: 6.1.2-ç</td></tr>'
         '<tr><th>Sınır</th><td>EBOB ve EKOK kavramlarına değinilmez; ortak böleni yalnız 1 olan sayıların aralarında asal olma durumu tartışılır (Öğrenme-Öğretme Uygulamaları).</td></tr>'
         '<tr><th>Puanlama</th><td>Her soruda cevap ve gerekçe ayrı: 1 doğru, 0,5 yarım, 0 yanlış ya da boş. Güven: eminim 1, emin değilim 0. Karar ve ödev: <code>kavrama_karari.py</code>.</td></tr></table>']
    for q in SORULAR:
        s.append(f'<div class="k"><h2>Soru {q["no"]} · {E(q["tur"])}</h2><div class="etk">Bileşen: {q["bilesen"]} · En zor durum: {E(q["en_zor"])}</div>'
                 f'<h3>Doğru cevap</h3>{E(q["cevap"])}<h3>Kabul edilen gerekçeler</h3><ul>' + "".join(f"<li>{E(x)}</li>" for x in q["kabul"]) +
                 '</ul><h3>Kabul edilmeyen</h3><ul>' + "".join(f"<li>{E(x)}</li>" for x in q["red"]) +
                 '</ul><h3>Sık hatalı cevap → neyi gösterir, ne yapılır</h3><table>' + "".join(f"<tr><td style='width:28%'>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in q["hatalar"]) + "</table></div>")
    s.append('<div class="k"><h2>Hedefli soru bankası (sonuçtan sonra seçin)</h2><table><tr><th>Bileşen</th><th>Soru</th><th>Cevap</th></tr>' +
             "".join(f"<tr><td>{b}</td><td>{E(t)}</td><td>{E(c)}</td></tr>" for b, t, c in BANKA) + '</table></div>')
    s.append('<div class="k"><h2>Karar kuralı</h2>Bileşen puanı ≥ 0,85 geçti (ödev yok) · 0,5–0,85 kısa telafi (2 soru) · &lt; 0,5 yeniden ele al (telafi kartı ve 3 soru). Emin ama yanlış cevap en az “yeniden ele al”dır. Haftalık ödev en çok 6 soru.</div>')
    return "".join(s)


assert ortak_kat(10, 15, 60) == [30, 60] and ortak_kat(4, 10, 60) == [20, 40, 60] and ortak_bolen(18, 27) == [1, 3, 9]
assert ortak_bolen(20, 30) == [1, 2, 5, 10] and ortak_kat(12, 18, 72) == [36, 72] and ortak_bolen(8, 15) == [1]
BANKA = [
 ("6.1.4-a", "10 ile 15'in 1 ile 60 arasındaki ortak katlarını yaz.", "30, 60"),
 ("6.1.4-a", "18 ile 27'nin ortak bölenlerini yaz.", "1, 3, 9"),
 ("6.1.4-a", "20 kalem ve 30 silgi, artmadan eşit gruplara ayrılacak. Grup sayısı kaç olabilir? (En az 2 grup)", "2, 5, 10"),
 ("6.1.4-b", "4'ün ve 10'un katlarını 60'a kadar iki satırlık tabloya yaz; ortak olanları daire içine al.", "20, 40, 60"),
 ("6.1.4-b", "8'in ve 15'in bölenlerini iki çember içine yaz; ortak olanı ortaya yerleştir.", "Yalnız 1 ortada"),
 ("6.1.4-c", "Can, “12 ile 18'in ortak katı 6'dır.” diyor. Can'ın hatasını açıkla ve iki ortak kat yaz.", "6 ortak bölendir; ortak katlar 36, 72"),
 ("6.1.4-c", "“Ortak kat” ile “ortak bölen” arasındaki farkı kendi cümlelerinle bir örnekle anlat.", "Açık uçlu; tanım ve örnek"),
 ("6.1.2-ç", "“3'e bölünen her sayı 9'a da bölünür.” Doğru mu? Bir örnekle göster.", "Yanlış; 12"),
]

# ---------------- Hızlı tekrar (9. hafta dersi başı) ----------------
assert ortak_kat(4, 6, 29) == [12, 24]
assert ortak_kat(8, 12, 30) == [24] and ortak_bolen(8, 12) == [1, 2, 4]
assert [p for p in [(6, 35), (8, 15), (9, 21), (4, 9)] if math.gcd(*p) != 1] == [(9, 21)]
assert [d for d in bol(36) if d > 10] == [12, 18, 36]
assert 12 % 3 == 0 and 12 % 9 != 0 and 9 % 2 == 1 and 9 % 3 == 0
TUR = [
 ("Hızlı hesap", "6.1.4-a", "geçen hafta", "4 ile 6'nın 30'dan küçük ortak katları?", "12 ve 24", "“24” diyen ilk ortak katı kaçırıyor: “24'ten küçük ortak kat var mı?”"),
 ("Doğru mu, yanlış mı?", "6.1.3", "2 hafta önce", "Her tek sayı asaldır.", "Yanlış: 9 tek ama 3 · 3.", "“Doğru” diyene: “9'u böl bakalım.”"),
 ("Hatayı bul", "6.1.4-c", "geçen hafta", "Elif: “8 ile 12'nin ortak katı 4'tür.”", "4 ortak bölendir; ortak kat 24.", "Kat ile böleni karıştıran: “4, 8'in katı mı?”"),
 ("Boşluk tamamla", "6.1.2", "4 hafta önce", "Son iki basamağı 4'e bölünen sayı … tam bölünür.", "4'e", "“2'ye” diyen de haklı ama eksik: “Daha güçlüsü?”"),
 ("Hangisi farklı?", "6.1.4-a", "geçen hafta", "Hangi çift aralarında asal değil? 6–35 · 8–15 · 9–21 · 4–9", "9–21 (ikisi de 3'e bölünür)", "“Ortak böleni yalnız 1 mi?” diye denetletin."),
 ("Hızlı hesap", "6.1.1", "8 hafta önce", "36'nın 10'dan büyük çarpanları?", "12, 18, 36", "36'yı unutan: “36, 36'nın çarpanı mı?”"),
 ("Doğru mu, yanlış mı?", "6.1.2", "4 hafta önce", "3'e bölünen her sayı 9'a da bölünür.", "Yanlış: 12.", "Önermenin tersini doğru sanıyor: “Geçen hafta hangisini tamamlamıştık?”"),
 ("Sloganı tamamla", "6.1.4", "geçen hafta", "Ortak kat … katı.", "ikisinin de", "Ardından neden sorusu."),
]
SLOGAN = {"slogan": "Ortak kat ikisinin de katı.", "kural": "İki sayının ortak katı, her iki sayının da katı olan sayıdır.",
          "karsi": "4 ile 6 için 8 yalnız 4'ün katıdır, ortak kat değildir; slogan bunu doğru biçimde dışarıda bırakır.",
          "neden": "6 ile 8'in ortak katı 2 olabilir mi? Hayır: 2, 6'nın da 8'in de katı değildir; ikisini de böler, yani ortak bölendir."}
assert 8 % 4 == 0 and 8 % 6 != 0 and 2 % 6 != 0 and 6 % 2 == 0 and 8 % 2 == 0
REDDEDILEN = [("“Ortak kat büyükten büyük, ortak bölen küçükten küçük.”", "4 ile 8'de 8 ortak kattır ve büyük sayıya eşittir; slogan yanlış sonuç verdirir."),
              ("“Çarp, ortak katı bul.”", "Çarpım ortak kattır ama ilk ortak kat değildir (6 · 8 = 48, oysa 24 de ortak kat); öğrenciyi tek cevaba iter.")]
assert ortak_kat(4, 8, 8) == [8] and 24 < 48

CSS_K = """
@page{size:297mm 167mm;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Inter,sans-serif}
.k{width:297mm;height:167mm;padding:16mm 20mm;position:relative;break-after:page;background:#f2f4f7;color:#14213d;display:flex;flex-direction:column;justify-content:center}
.k.koyu{background:#14213d;color:#fff}
.etk{position:absolute;left:20mm;top:12mm;font:700 12pt Inter;letter-spacing:.08em;background:#d9dde6;color:#14213d;padding:2mm 4mm;border-radius:20mm}
.koyu .etk{background:rgba(255,255,255,.12);color:#ffd166}
.no{position:absolute;right:20mm;top:13mm;font:600 12pt Inter;color:#4a5570}.koyu .no{color:#b9c2d6}
.dots{position:absolute;left:20mm;bottom:12mm;display:flex;gap:2.5mm}.dots i{width:3.2mm;height:3.2mm;border-radius:50%;background:#d9dde6}.dots i.on{background:#ffd166}
.dna{position:absolute;right:20mm;bottom:11mm;font:800 9pt Inter;letter-spacing:.18em;color:#4a5570}
h1{font:700 44pt/1.1 Lora,serif;margin:0}h1 em{color:#ffd166}
.soru{font:600 34pt/1.25 Inter;max-width:240mm}
.cevap{font:700 38pt/1.2 Lora,serif}.acik{font-size:20pt;color:#4a5570;margin-top:5mm}
.koyu .acik{color:#d5dbe8}
.slogan{font:700 48pt/1.1 Lora,serif;color:#ffd166}.neden{font-size:20pt;margin-top:8mm;color:#d5dbe8;max-width:230mm}
"""


def kartlar():
    n = len(TUR)
    nokta = lambda i: '<div class="dots">' + "".join(f'<i class="{"on" if j < i else ""}"></i>' for j in range(n)) + "</div>"
    s = [f'<section class="k koyu"><div class="etk">Isınalım</div><h1>5 dakika, <em>{n} soru</em></h1><div class="acik">Bakmadan cevapla. Geçen hafta ve daha öncesinden karışık.</div>{nokta(0)}<div class="dna">DNAMATHOS</div></section>']
    for i, (bicim, b, ne, soru, cevap, _) in enumerate(TUR, 1):
        s.append(f'<section class="k"><div class="etk">{E(bicim)}</div><div class="no">{i} / {n}</div><div class="soru">{E(soru)}</div>{nokta(i - 1)}<div class="dna">DNAMATHOS</div></section>')
        s.append(f'<section class="k"><div class="etk">Cevap</div><div class="no">{i} / {n}</div><div class="cevap">{E(cevap)}</div>{nokta(i)}<div class="dna">DNAMATHOS</div></section>')
    s.append(f'<section class="k koyu"><div class="etk">Haftanın sloganı</div><div class="slogan">{E(SLOGAN["slogan"])}</div><div class="neden">Neden? {E(SLOGAN["neden"].split("?")[0])}?</div>{nokta(n)}<div class="dna">DNAMATHOS</div></section>')
    return "".join(s)


def tur_ogretmen():
    s = ['<div class="ust"><h1>Hızlı tekrar · öğretmen listesi</h1><small>6. sınıf · 9. hafta ders başı · notsuz</small></div>',
         '<table><tr><th>#</th><th>Biçim</th><th>Soru</th><th>Cevap</th><th>Bileşen</th><th>İşlendi</th><th>Yanlış cevaba tek cümle</th></tr>' +
         "".join(f"<tr><td>{i}</td><td>{E(a)}</td><td>{E(c)}</td><td>{E(d)}</td><td>{E(b)}</td><td>{E(ne)}</td><td>{E(f)}</td></tr>" for i, (a, b, ne, c, d, f) in enumerate(TUR, 1)) + "</table>",
         '<div class="k"><h2>Dağılım</h2>Geçen hafta 4 · 2–4 hafta önce 3 · 8 hafta önce 1. Aynı konudan art arda iki soru yok; altı farklı biçim.</div>',
         f'<div class="k"><h2>Haftanın sloganı</h2><table><tr><th>Slogan</th><td>{E(SLOGAN["slogan"])}</td></tr><tr><th>Tam kural</th><td>{E(SLOGAN["kural"])}</td></tr>'
         f'<tr><th>Karşı örnek</th><td>{E(SLOGAN["karsi"])}</td></tr><tr><th>Neden sorusu</th><td>{E(SLOGAN["neden"])}</td></tr></table></div>',
         '<div class="k"><h2>Denetimden geçemeyen slogan önerileri</h2><table>' + "".join(f"<tr><td style='width:38%'>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in REDDEDILEN) + '</table></div>']
    return "".join(s)


def pdf(ad, govde, css, kat=None):
    yol = os.path.join(KL, ad + ".html")
    open(yol, "w", encoding="utf-8").write(f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><title>{ad}</title><style>{css}</style></head><body>{govde}</body></html>")
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto("file://" + yol); pg.evaluate("document.fonts.ready")
        pg.pdf(path=os.path.join(KL, ad + ".pdf"), print_background=True, prefer_css_page_size=True)
        b.close()
    os.remove(yol)


pdf("kavrama_testi_ogrenci", ogrenci(), CSS_A4)
pdf("kavrama_testi_ogretmen", ogretmen(), CSS_A4)
pdf("hizli_tekrar_kartlari", kartlar(), CSS_K)
pdf("hizli_tekrar_ogretmen", tur_ogretmen(), CSS_A4)
print("Örnekler üretildi.")
