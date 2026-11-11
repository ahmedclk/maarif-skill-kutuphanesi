#!/usr/bin/env python3
"""Örnek: 6. sınıf Ders 8 (MAT.6.1.4 ortak kat ve ortak bölen) — DNAMATHOS 2.0 tasarımıyla haftalık paket.

Akış: kapak → ısınma (6 soru + cevap) → konu 1 + soru 1 → konu 2 + soru 2 → Kaydet ve slogan → kavrama testi (4) → ödev.
Bütün sayısal cevaplar kodla hesaplanır ve assert ile denetlenir. Program sınırı: EBOB ve EKOK kavramlarına değinilmez.
Kullanım: python3 ders_uret.py   (KaTeX: ../../node_modules/katex/dist ya da --katex ile)
"""
import os, subprocess, sys
KL = os.path.dirname(os.path.abspath(__file__))
SK = os.path.join(KL, "..", "..", "markalar", "dnamathos", "dnamathos-pdf-tasarimi", "scripts")
sys.path.insert(0, SK)
import dna

bol = lambda n: [d for d in range(1, n + 1) if n % d == 0]
ob = lambda a, b: sorted(set(bol(a)) & set(bol(b)))
ok = lambda a, b, u: [x for x in range(1, u + 1) if x % a == 0 and x % b == 0]

# Isınma (önceki haftalar: 6.1.1, 6.1.2, 6.1.3)
assert [d for d in bol(24) if 5 < d < 10] == [6, 8]
assert 9 % 3 == 0 and 34 % 4 != 0 and 134 % 4 != 0
assert [x for x in (2, 3, 9, 11) if len(bol(x)) != 2] == [9]
TUR = [
 ("Hızlı hesap", "24'ün 5 ile 10 arasındaki çarpanları hangileri?", "6 ve 8", "24 = 6 · 4 = 8 · 3"),
 ("Doğru mu, yanlış mı?", "Her tek sayı asaldır.", "Yanlış", "9 tek sayıdır ama 9 = 3 · 3."),
 ("Hatayı bul", "Can: “134'ün son rakamı 4, o hâlde 134, 4'e bölünür.”", "Son iki basamağa bakılır", "34, 4'e bölünmez; bu yüzden 134 de bölünmez."),
 ("Boşluk tamamla", "Rakamları toplamı 3'ün katı olan sayı … tam bölünür.", "3'e", "Örnek: 51 → 5 + 1 = 6"),
 ("Hangisi farklı?", "2 · 3 · 9 · 11: hangisi asal değil?", "9", "9'un bölenleri 1, 3, 9."),
 ("Sloganı tamamla", "Dörde bölünme? Son iki …", "basamağa bak.", "Geçen haftanın sloganı"),
]
# Konu ve sorular
assert ok(8, 12, 60) == [24, 48]
assert ob(12, 18) == [1, 2, 3, 6]
assert [g for g in ob(16, 24) if g >= 2] == [2, 4, 8] and ob(16, 24) != [1]
# Kavrama testi
assert ok(6, 8, 50) == [24, 48] and ob(9, 16) == [1] and [d for d in ob(24, 36) if d >= 2] == [2, 3, 4, 6, 12] and 9 % 3 == 0

N = 25
NAV = lambda on: [("Isınma", "#tur", on == "tur"), ("Konu", "#konu1", on == "konu"), ("Test", "#test", on == "test"), ("Ödev", "#odev", on == "odev")]
sira = iter(range(1, N + 1))
def ser(yol, on):
    return dna.serit(yol, next(sira), N, nav=NAV(on))

g = [dna.kapak("kapak", ust="Ortak kat", alt="ortak bölen", sinif="6. sınıf", ders=8, kod="MAT.6.1.4",
               akis="Isınma · 2 konu · kavrama testi", not_el="bugün: iki sayının ortak noktası")]
next(sira)
g.append(dna.tur_kapak("tur", ser("Isınma", "tur"), len(TUR)))
for i, (bicim, soru, cevap, acik) in enumerate(TUR, 1):
    g.append(dna.tur_soru(f"tur{i}", ser(f"Isınma · {i} / {len(TUR)}", "tur"), bicim, soru, len(TUR), i,
                          not_el="20 saniye" if i == 1 else "", alt_yazi="Hata nerede? Bir cümleyle söyle." if bicim == "Hatayı bul" else ""))
    g.append(dna.tur_cevap(f"tur{i}c", ser(f"Isınma · {i} / {len(TUR)} · cevap", "tur"), cevap, acik, len(TUR), i))

g.append(dna.konu("konu1", ser("Konu 1 · Ortak kat", "konu"), 1, "Ortak kat",
    "Sayı doğrusunda 4'ün katlarını üste, 6'nın katlarını alta işaretle. Hangi sayılar iki listede de var?",
    "İki sayının da katı olan sayıya o sayıların <span class='bos'></span> denir.",
    sekil=dna.sayi_dogrusu(30, 2, 620, etiket=("4'ün katları: üste", "6'nın katları: alta")),
    yazilida="“… ortak katlarını sayı doğrusunda gösteriniz.”", kitapta="Ders kitabı, Ortak Kat ve Ortak Bölen bölümü (basılı sayfa öğretmen dosyasında)."))
g.append(dna.soru("soru1", ser("Konu 1 · Soru 1", "konu"), 1, "Durak çizelgesi",
    "Bir otobüs 8 dakikada bir, diğeri 12 dakikada bir duraktan kalkıyor. İkisi saat 09.00'da birlikte kalktı.",
    "a) 10.00'a kadar iki otobüsün birlikte kalktığı saatleri yazınız.\nb) Bulduğunuz saatlerin neden ortak kat olduğunu gerekçesiyle açıklayınız.",
    ("6.1.4-a · 6.1.4-c", "Orta · Z2 Y açık C A"), tuyo="Gerekçede tanımı kullan: bu saat hangi iki sayının katına denk geliyor?", coz_ust=300))
g.append(dna.konu("konu2", ser("Konu 2 · Ortak bölen", "konu"), 2, "Ortak bölen",
    "12'nin ve 18'in bölenlerini tabloya yaz. Hangi sayılar iki satırda da var?",
    "İki sayıyı da bölen sayıya o sayıların <span class='bos'></span> denir. Ortak böleni yalnız 1 olan iki sayıya <span class='bos'></span> sayılar denir.",
    sekil=dna.tablo(["Sayı", "Bölenleri"], [["12", "&nbsp;" * 40], ["18", ""]]),
    hata="Ortak böleni ortak katla karıştırmak: 36, 12'nin ve 18'in ortak katıdır; ikisini de bölmez.",
    yazilida="“… ortak bölenlerini tablo ya da çizimle gösteriniz.”", slogan="Ortak kat ikisinin de katı."))
g.append(dna.soru("soru2", ser("Konu 2 · Soru 2", "konu"), 2, "Kalem ve silgi grupları",
    "Bir öğretmen 16 kalem ve 24 silgiyi hiç artmadan gruplara ayıracak. Her grupta eşit sayıda kalem ve eşit sayıda silgi olacak; en az 2 grup oluşacak.",
    "a) Kaç grup oluşturulabilir? Bütün olasılıkları yazınız.\nb) 16 ile 24 aralarında asal mıdır? Gerekçesiyle açıklayınız.",
    ("6.1.4-a · 6.1.4-c", "Zor · Z2 Y açık C G"), tuyo="“Bütün olasılıklar” istendiğinde soruda verilen koşulu (en az 2 grup) yeniden oku.", coz_ust=318))
g.append(dna.kaydet("kaydet", ser("Kaydet", "konu"), ["Ortak kat: iki sayının da katı.", "Ortak bölen: iki sayıyı da böler.", "Ortak böleni yalnız 1 ise: aralarında asal."],
                    "Ortak kat ikisinin de katı."))
g.append(dna.kavrama_kapak("test", ser("Kavrama testi", "test"), ["2 küme sorusu", "1 aktarım sorusu", "1 tekrar sorusu"]))
KT = ["1 ile 50 arasında hem 6'nın hem 8'in katı olan sayıları yaz.",
      "Ece, “9 ile 16'nın hiç ortak böleni yoktur.” diyor. Ece'ye katılıyor musun?",
      "Bir bahçıvan 24 lale ve 36 sümbülü, her sırada aynı sayıda lale ve aynı sayıda sümbül olacak, hiç çiçek artmayacak şekilde dikecek. En az 2 sıra olacaksa kaç sıra yapabilir?",
      "Önermeyi tamamla: “Bir doğal sayı 9'a tam bölünüyorsa ……'e de tam bölünür.”"]
for i, q in enumerate(KT, 1):
    g.append(dna.kavrama(f"test{i}", ser(f"Kavrama testi · {i} / 4", "test"), i, 4, q))
g.append(dna.odev("odev", ser("Bu hafta", "odev"),
    "Bu haftanın ödevi kavrama testinden sonra verilecek. Geçtiğin konudan ödev yok; takıldığın yere birkaç hedefli soru gelecek.",
    [("Kaynak kitap · Ortak Kat ve Ortak Bölen", "öğretmen yazar")], sonraki="Asal çarpanlar ve ortak bölen ilişkisi."))
assert next(sira, None) is None, "slayt sayısı N ile tutmuyor"

govde = os.path.join(KL, "ders8_govde.html")
open(govde, "w", encoding="utf-8").write("".join(g))
katex = next((p for p in [os.path.join(KL, "..", "..", "node_modules", "katex", "dist"), "/home/claude/yazili/node_modules/katex/dist"] if os.path.exists(p)), None)
r = subprocess.run([sys.executable, os.path.join(SK, "slayt_uret.py"), govde, os.path.join(KL, "DNAMATHOS_6_Ders8_OrtakKat.pdf"),
                    "--katex", katex, "--goruntu", os.path.join(KL, "goruntu"), "--baslik", "DNAMATHOS 6. sınıf Ders 8 · Ortak kat ve ortak bölen"])
os.remove(govde)
for f in ("DNAMATHOS_6_Ders8_OrtakKat.html",):
    p = os.path.join(KL, f)
    if os.path.exists(p): os.remove(p)
sys.exit(r.returncode)
