#!/usr/bin/env python3
"""Örnek: 7. sınıf Ders 6 (MAT.7.1.2 rasyonel sayıların ondalık gösterimi) — konu özeti skill'inin haftalık paketi.

70 dakikalık ders (2 × 35): ısınma (8 soru) → 3 konu ve soru çifti → Kaydet ve slogan → kavrama testi (4) → ödev.
Program: https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/463 (11.11.2026'da okundu). Devir çizgisi programda
geçmez; devirli gösterim "…" ile yazılır. Bütün sayılar aşağıda kodla hesaplanır ve assert ile denetlenir.

Kullanım: python3 uret.py [--skill <dnamathos-pdf-tasarimi klasörü>] [--katex <katex/dist>]
Çıktılar: DNAMATHOS_7_Ders6_Ondalik.pdf (ders), DNAMATHOS_7_Ders6_Ogretmen.pdf, DNAMATHOS_7_Ders6_Kavrama.pdf (A4),
          cevaplar.json (sızıntı denetimi), kavrama_sonuc.json (örnek sonuçlar), slogan_bankasi.json
"""
import argparse, html, json, os, subprocess, sys
from fractions import Fraction as F

KL = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--skill", default=os.environ.get("DNA_SKILL", os.path.join(KL, "..", "..", "markalar", "dnamathos", "dnamathos-pdf-tasarimi")))
ap.add_argument("--katex", default=next((p for p in [os.path.join(KL, "..", "..", "node_modules", "katex", "dist"), "/home/claude/yazili/node_modules/katex/dist"] if os.path.exists(p)), ""))
a = ap.parse_args()
SK = os.path.join(os.path.abspath(a.skill), "scripts")
sys.path.insert(0, SK)
import dna
from slayt_uret import font_css
E = html.escape


# ---------------- Matematik: uzun bölme ----------------
def bol(pay, payda, en_cok=60):
    """Pozitif kesrin ondalık açılımı: (tam kısım, ön basamaklar, devreden blok, kalanlar)."""
    tam, k = divmod(pay, payda)
    basamak, kalanlar, gorulen = [], [k], {}
    while k and k not in gorulen and len(basamak) < en_cok:
        gorulen[k] = len(basamak)
        d, k = divmod(k * 10, payda)
        basamak.append(d); kalanlar.append(k)
    if not k:
        return tam, basamak, [], kalanlar
    i = gorulen[k]
    return tam, basamak[:i], basamak[i:], kalanlar


def yaz(pay, payda, tekrar=2):
    t, on, dev, _ = bol(pay, payda)
    s = "".join(map(str, on)) + "".join(map(str, dev)) * (tekrar if dev else 0)
    return f"{t}," + s + ("…" if dev else "") if (on or dev) else str(t)


def basamak_no(pay, payda, n):
    t, on, dev, _ = bol(pay, payda)
    return on[n - 1] if n <= len(on) else dev[(n - len(on) - 1) % len(dev)]


onuncu_kuvvet = lambda q: any((10 ** k) % F(q).denominator == 0 for k in range(12))

# Konu ve ders soruları
assert yaz(3, 8) == "0,375" and F(3, 8) == F(375, 1000)
assert not onuncu_kuvvet(F(1, 3)) and yaz(1, 3) == "0,33…"
assert yaz(7, 8) == "0,875" and yaz(9, 20) == "0,45" and F(9, 20) == F(45, 100)
t, on, dev, kal = bol(4, 11); assert (on, dev) == ([], [3, 6]) and kal[:3] == [4, 7, 4]
assert basamak_no(4, 11, 20) == 6
assert bol(1, 3)[3] == [1, 1] and bol(2, 11)[3][:3] == [2, 9, 2]
assert yaz(5, 6) == "0,833…" and bol(5, 6)[1:3] == ([8], [3])
assert yaz(1, 16) == "0,0625" and onuncu_kuvvet(F(1, 16))
assert yaz(7, 40) == "0,175" and onuncu_kuvvet(F(7, 40)) and 40 > 3
# Kavrama testi
assert bol(5, 12)[1:3] == ([4, 1], [6]) and yaz(5, 12, 3) == "0,41666…"
assert yaz(7, 32) == "0,21875" and onuncu_kuvvet(F(7, 32))
assert yaz(2, 3, 3) == "0,666…" and 3 * F(666, 1000) == F(1998, 1000) < 2
assert abs(F(-7, 2)) == F(7, 2) > abs(2)
# Isınma
assert abs(-7) + abs(3) == 10 and (-5 < -2) and F(-3, 4) > -1 and F(-3, 4) < 0
assert F(1, 2) < F(3, 4) < 1 and (-1 + 0) / 2 == -0.5 and yaz(7, 10) == "0,7"
assert [x for x in (F(-4), F(0), F(7), F(5, 2)) if x.denominator != 1] == [F(5, 2)]
# Hedefli soru bankası
assert yaz(11, 20) == "0,55" and yaz(5, 8) == "0,625" and F(3, 4) == F(75, 100)
assert bol(1, 6)[1:3] == ([1], [6]) and bol(1, 6)[3] == [1, 4, 4]
assert bol(5, 11)[2] == [4, 5] and bol(7, 12)[1:3] == ([5, 8], [3])
assert onuncu_kuvvet(F(9, 25)) and not onuncu_kuvvet(F(2, 9)) and onuncu_kuvvet(F(3, 40)) and yaz(3, 40) == "0,075"
assert yaz(1, 8) == "0,125" and sorted(set(bol(1, 7)[3][:-1])) == [1, 2, 3, 4, 5, 6]
assert abs(F(-5, 2)) > abs(F(3, 2))
fr = lambda p, q: f"$\\dfrac{{{p}}}{{{q}}}$"

# ---------------- İçerik ----------------
# Isınma: geçen hafta (Ders 5: 7.1.1-c) 4 soru; 2–3 hafta önce (7.1.1-b, 7.1.1-a) 3 soru; ön koşul (6. sınıf 6.1.5) 1 soru.
TUR = [  # biçim, bileşen, ne zaman, soru, cevap, açıklama, yanlış cevaba tek cümle
 ("Hızlı hesap", "7.1.1-c", "geçen hafta", "Sayı doğrusunda −1 ile 0'ın tam ortasındaki sayı hangisi?", "−0,5", "−1 ile 0 arasındaki uzaklığın yarısı: $-\\dfrac{1}{2}$", "“0,5” diyene: “Sıfırın hangi yanındayız?”"),
 ("Hızlı hesap", "7.1.1-b", "2 hafta önce", "|−7| + |3| kaç eder?", "10", "|−7| = 7 ve |3| = 3", "“−4” diyen mutlak değeri almadan topluyor: “|−7| neyin uzunluğu?”"),
 ("Doğru mu, yanlış mı?", "7.1.1-c", "geçen hafta", f"{fr('-3', 4)} sayısı sayı doğrusunda −1 ile 0 arasındadır.", "Doğru", "−1 < $-\\dfrac{3}{4}$ < 0", "“Yanlış” diyene: “$-\\dfrac{3}{4}$, −1'den büyük mü küçük mü?”"),
 ("Hangisi farklı?", "7.1.1-a", "3 hafta önce", "−4 · 0 · 7 · 2,5: hangisi tam sayı değil?", "2,5", "−4, 0 ve 7 tam sayıdır; 2,5 değildir.", "“0” diyene: “Sıfır pozitif değil ama tam sayı mı?”"),
 ("Hatayı bul", "7.1.1-c", "geçen hafta", "Ece: “$\\dfrac{1}{2}$ ile 1 arasında hiç rasyonel sayı yoktur.”", "Var: örneğin $\\dfrac{3}{4}$", "İki rasyonel sayı arasında daima bir rasyonel sayı bulunur.", "Ardışık tam sayılarla karıştırıyor: “Ortalarındaki sayı ne?”"),
 ("Hızlı hesap", "6.1.5", "6. sınıf", f"{fr(7, 10)} sayısını ondalık gösterimle yaz.", "0,7", "Onda yedi", "“7,10” diyene: “Kaç tane onda bir var?”"),
 ("Hatayı bul", "7.1.1-b", "2 hafta önce", "Mert: “|−4| = −4, çünkü mutlak değer sayıyı değiştirmez.”", "|−4| = 4", "Mutlak değer sıfıra uzaklıktır; uzaklık negatif olmaz.", "“Uzaklık negatif olabilir mi?”"),
 ("Sloganı tamamla", "7.1.1-c", "geçen hafta", "Her rasyonel sayının sayı doğrusunda bir … var.", "yeri", "Geçen haftanın sloganı", "Ardından: “$\\dfrac{2}{3}$'ün yeri neresi?”"),
]
for i in range(1, len(TUR)):
    assert TUR[i][1] != TUR[i - 1][1], f"art arda aynı bileşen: {i}"
assert sum(t[2] == "geçen hafta" for t in TUR) == 4 and len({t[0] for t in TUR}) >= 2 and any(t[0] == "Hatayı bul" for t in TUR)

SLOGAN = {"slogan": "Kalan tekrar ederse basamaklar devreder.",
          "kural": "Bölmede daha önce çıkmış bir kalan yeniden çıkarsa bölümdeki basamaklar da aynı sırayla yeniden gelir; ondalık gösterim devirlidir.",
          "karsi": "Kalan 0 olursa bölme biter ve gösterim sonludur ($\\dfrac{3}{8}$ = 0,375); slogan bu durumu dışarıda bırakır, yanlış sonuç verdirmez.",
          "neden": "Neden aynı kalan aynı basamakları getirir? Çünkü aynı kalanla aynı bölme yeniden başlar; her adım öncekinin aynısıdır."}
assert len(SLOGAN["slogan"].split()) <= 8 and bol(3, 8)[3][-1] == 0
REDDEDILEN = [("“Uzun ondalık devirlidir.”", "Yanlış: $\\dfrac{7}{32}$ = 0,21875 uzun ama sonludur."),
              ("“Paydası büyükse devirli.”", "Yanlış: $\\dfrac{7}{40}$ sonlu, $\\dfrac{1}{3}$ devirli; paydanın büyüklüğü belirlemez.")]

SORULAR = [  # ders soruları: öğretmen çözümü ile
 dict(no=1, baslik="Terzinin kumaşları", bil="7.1.2-a", guc="Orta · Z2 Y açık C G",
      metin=f"Bir terzi 7 m kumaşı 8 eşit parçaya, 9 m kumaşı 20 eşit parçaya ayırıyor. Ali, “{fr(9, 20)} sayısının paydası 10'un kuvveti değil; bu yüzden ondalık gösterimi yoktur.” diyor.",
      madde="a) Her iki durumda bir parçanın uzunluğunu bölme işlemiyle bulup ondalık gösterimle yazınız.<br>b) Ali'nin görüşüne katılıp katılmadığınızı gerekçesiyle açıklayınız.",
      tuyo="b'de Ali'nin cümlesindeki “bu yüzden” sözcüğüne odaklan: ilk kısım doğru mu, sonuç ondan çıkıyor mu?", coz=336,
      cozum=["a) 7 ÷ 8 = 0,875 m (4 puan); 9 ÷ 20 = 0,45 m (4 puan).", f"b) Katılmıyorum: {fr(9, 20)} = {fr(45, 100)}; payda 100'e genişletilebilir ve bölme 0,45'te biter. Her rasyonel sayının bölmeyle bulunan bir ondalık gösterimi vardır (2 puan)."]),
 dict(no=2, baslik="Kalanlar ne söylüyor?", bil="7.1.2-a · 7.1.2-b", guc="Zor · Z2 Y kapalı C A",
      metin=f"{fr(4, 11)} sayısının ondalık gösterimi bölme işlemiyle bulunacaktır.",
      madde="a) Bölmeyi her adımdaki kalanı yazarak sürdürünüz ve ondalık gösterimi yazınız.<br>b) Gösterimin devirli olduğunu kalanları kullanarak açıklayınız.<br>c) Virgülden sonraki 20. basamakta hangi rakamın bulunduğunu gerekçesiyle yazınız.",
      tuyo="c'de 20 basamağı tek tek yazmak yerine hangi basamaklarda aynı rakamın çıktığına bak.", coz=316,
      cozum=["a) Kalanlar 4 → 7 → 4 → 7 …; bölüm 0,3636… (3 puan).", "b) 4 kalanı ikinci kez çıktı; aynı kalanla aynı bölme yeniden başlar, 3 ve 6 sırayla tekrar eder (3 puan).",
             "c) Tek sıradaki basamaklar 3, çift sıradakiler 6'dır; 20 çift olduğu için 6 (4 puan)."]),
 dict(no=3, baslik="Deniz'in varsayımı", bil="7.1.2-b · 7.1.2-c", guc="Zor · Z3 Y açık C G",
      metin="Deniz, “Paydası büyük olan kesrin ondalık gösterimi devirli olur.” diyor.",
      madde=f"a) {fr(1, 3)} ve {fr(7, 40)} sayılarının ondalık gösterimlerini bularak Deniz'in varsayımını sınayınız.<br>b) Deniz'in varsayımına katılıp katılmadığınızı gerekçesiyle açıklayınız.<br>c) Önermeyi tamamlayınız: “Paydası 10'un bir kuvvetine genişletilebilen bir rasyonel sayının ondalık gösterimi …… .”",
      tuyo="Bir iddiayı çürütmek için tek bir karşı örnek yeter.", coz=342,
      cozum=[f"a) {fr(1, 3)} = 0,333… (devirli); {fr(7, 40)} = 0,175 (sonlu) (4 puan).", "b) Katılmıyorum: 40, 3'ten büyük olduğu hâlde gösterim sonlu; 3 küçük olduğu hâlde devirli. Belirleyen paydanın büyüklüğü değil (3 puan).",
             f"c) sonludur; örneğin {fr(7, 40)} = {fr(175, 1000)} (3 puan)."]),
]

KT = [  # kavrama testi
 dict(no=1, tur="Küme sorusu", bil=["7.1.2-a", "7.1.2-b"], metin=f"{fr(5, 12)} sayısının ondalık gösterimini bölme işlemiyle bul. Bu gösterim sonlu mu, devirli mi?",
      cevap="0,41666… ; devirli", kabul=["Bölmede 8 kalanı tekrar etti; bu yüzden 6 basamağı sürekli gelir.", "Kalanlar 5, 2, 8, 8, … ; 8 tekrar ettiği için devirli."],
      red=["Devirli, çünkü uzun.", "0,416 (bölmeyi erken kesiyor, devri görmüyor)."],
      hatalar=[("0,4166 ya da 0,417", "Bölmeyi kesip yuvarlıyor; kalanı izlemiyor. Kalan sütununu birlikte doldurun."), ("Devirli değil, çünkü 4 ve 1 tekrar etmiyor", "Devrin virgülden hemen sonra başlaması gerektiğini sanıyor; 5/6 örneğine dönün.")],
      en_zor="Devrin virgülden hemen sonra başlamadığı sayı."),
 dict(no=2, tur="Küme sorusu", bil=["7.1.2-b", "7.1.2-c"], metin=f"Ece, “{fr(7, 32)} = 0,21875 uzun bir ondalık gösterim; o hâlde devirlidir.” diyor. Ece'ye katılıyor musun?",
      cevap="Katılmıyorum; gösterim sonludur.", kabul=["Bölme beş basamakta bitiyor (kalan 0); hiçbir kalan tekrar etmiyor.", "32, 100 000'in böleni; payda 10'un kuvvetine genişletilebilir."],
      red=["Katılmıyorum (gerekçesiz).", "Katılıyorum, çünkü 5 basamak var."],
      hatalar=[("Katılıyorum", "Uzunluğu devirle karıştırıyor. 1/16 ile 1/3'ü yan yana bölün: hangisi biter?")],
      en_zor="Uzun ama sonlu gösterim."),
 dict(no=3, tur="Aktarım sorusu", bil=["7.1.2-a", "7.1.2-c"], metin="Bir manav 2 kg fındığı 3 eşit pakete ayırdı. Terazinin ekranında her paket için 0,666 kg yazıyor. Selin, “Her paket tam olarak 0,666 kg'dır.” diyor. Bir paketin ağırlığının ondalık gösterimini bulunuz ve Selin'in ifadesini değerlendiriniz.",
      cevap="0,666… kg (devirli); Selin haklı değil.", kabul=["2 ÷ 3'te kalan hep 2; gösterim bitmez. Terazi yalnız üç basamak gösterir.", "3 · 0,666 = 1,998; 2 kg'ı vermez."],
      red=["Haklı, çünkü terazi öyle gösteriyor.", "Haklı değil (gerekçesiz)."],
      hatalar=[("Selin haklı", "Ekrandaki yaklaşık değeri tam değer sanıyor. 3 · 0,666'yı hesaplatın.")],
      en_zor="Derste görülmemiş bağlamda devirli gösterimin yaklaşık değerle karıştırılması."),
 dict(no=4, tur="Tekrar sorusu", bil=["7.1.1-b"], islendi=4, metin="Sayı doğrusunda −3,5 ve 2 sayılarından hangisi sıfıra daha uzaktır? Mutlak değer kullanarak gösteriniz.",
      cevap="−3,5", kabul=["|−3,5| = 3,5 ve |2| = 2; 3,5 > 2.", "−3,5 sıfırdan 3,5 birim, 2 ise 2 birim uzakta."],
      red=["2, çünkü pozitif sayı daha büyüktür."],
      hatalar=[("2", "Büyüklük ile sıfıra uzaklığı karıştırıyor. İki sayıyı sayı doğrusunda işaretletip birimleri saydırın.")],
      en_zor="Negatif sayının mutlak değerinin daha büyük olduğu çift."),
]
assert [k["tur"] for k in KT].count("Küme sorusu") == 2 and len(KT) == 4

BANKA = [
 ("7.1.2-a", f"{fr(11, 20)} sayısını bölme işlemiyle ondalık gösterimle yaz.", "0,55"),
 ("7.1.2-a", f"{fr(5, 8)} sayısını iki yolla (genişletme ve bölme) ondalık gösterimle yaz.", "0,625"),
 ("7.1.2-a", "3 L su 4 bardağa eşit bölünüyor. Bir bardaktaki su kaç litredir? Ondalık gösterimle yaz.", "0,75 L"),
 ("7.1.2-b", f"{fr(1, 6)} bölmesini kalanlarla yaz. Hangi kalan tekrar ediyor?", "0,1666… ; kalan 4"),
 ("7.1.2-b", f"{fr(5, 11)} sayısının ondalık gösteriminde tekrar eden basamakları yaz.", "4 ve 5 (0,4545…)"),
 ("7.1.2-b", f"{fr(7, 12)} sayısının ondalık gösteriminde devir hangi basamaktan başlar?", "0,58333… ; 3. basamaktan"),
 ("7.1.2-c", f"{fr(9, 25)}, {fr(2, 9)} ve {fr(3, 40)} sayılarından hangilerinin ondalık gösterimi sonludur? Gerekçesiyle yaz.", "9/25 = 0,36 ve 3/40 = 0,075"),
 ("7.1.2-c", "Can, “0,125 uzun bir gösterim, devirlidir.” diyor. Can'ın hatasını açıkla.", "Sonludur; 1/8 = 0,125"),
 ("7.1.2-c", "1 ÷ 7 bölmesinde sıfırdan farklı en çok kaç kalan çıkabilir? Bu, gösterimin neden ya bittiğini ya da tekrar ettiğini nasıl açıklar?", "6 (1–6); kalan ya 0 olur ya tekrar eder"),
 ("7.1.1-b", "−2,5 ile 1,5'ten hangisi sıfıra daha uzaktır? Mutlak değerle göster.", "−2,5"),
 ("7.1.1-b", "|−6| − |−2| işleminin sonucunu bul.", "4"),
]

# ---------------- Ders PDF'i ----------------
N = 1 + 1 + 2 * len(TUR) + 6 + 1 + 1 + len(KT) + 1
NAV = lambda on: [("Isınma", "#tur", on == "tur"), ("Konu", "#konu1", on == "konu"), ("Test", "#test", on == "test"), ("Ödev", "#odev", on == "odev")]
sira = iter(range(1, N + 1))
ser = lambda yol, on: dna.serit(yol, next(sira), N, nav=NAV(on))

g = [dna.kapak("kapak", ust="Ondalık gösterim", alt="biter mi, döner mi?", sinif="7. sınıf", ders=6, kod="MAT.7.1.2",
               akis="Isınma · 3 konu · kavrama testi", not_el="bugün: bölmenin sırrı kalanda")]
next(sira)
g.append(dna.tur_kapak("tur", ser("Isınma", "tur"), len(TUR)))
for i, (bicim, _, _, soru, cevap, acik, _) in enumerate(TUR, 1):
    g.append(dna.tur_soru(f"tur{i}", ser(f"Isınma · {i} / {len(TUR)}", "tur"), bicim, soru, len(TUR), i,
                          not_el="20 saniye" if i == 1 else "", alt_yazi="Hata nerede? Bir cümleyle söyle." if bicim == "Hatayı bul" else ""))
    g.append(dna.tur_cevap(f"tur{i}c", ser(f"Isınma · {i} / {len(TUR)} · cevap", "tur"), cevap, acik, len(TUR), i))

K1 = dna.tablo(["Kesir", "Paydayı 10'un kuvvetine genişlet", "Bölme işlemi yap"], [[fr(3, 8), "", ""], [fr(1, 3), "", ""]])
g.append(dna.konu("konu1", ser("Konu 1 · Bölmeyle ondalık gösterim", "konu"), 1, "Bölmeyle ondalık gösterim",
    f"{fr(3, 8)} sayısını iki yolla ondalık gösterimle yaz: paydayı 1000'e genişlet ya da 3'ü 8'e böl. Aynı sonuca ulaşıyor musun? Aynısını {fr(1, 3)} için dene.",
    "Bir rasyonel sayının ondalık gösterimini bulmak için <span class='bos'></span> paydaya böleriz. Paydası 10'un kuvvetine genişletilemeyen sayılarda da bu yol çalışır.",
    sekil=K1, yazilida="“… sayısının ondalık gösterimini bölme işlemi yaparak bulunuz.”", kitapta="Rasyonel sayıların ondalık gösterimi bölümü."))
d = SORULAR[0]; g.append(dna.soru("soru1", ser("Konu 1 · Soru 1", "konu"), 1, d["baslik"], d["metin"], d["madde"], (d["bil"], d["guc"]), tuyo=d["tuyo"], coz_ust=d["coz"]))
K2 = dna.tablo(["Bölme", "1. kalan", "2. kalan", "3. kalan", "4. kalan"], [[f"1 ÷ 3", "", "", "", ""], ["2 ÷ 11", "", "", "", ""]])
g.append(dna.konu("konu2", ser("Konu 2 · Devirli ondalık gösterim", "konu"), 2, "Devirli ondalık gösterim",
    f"{fr(1, 3)} ve {fr(2, 11)} için bölmeyi sürdür; her adımda kalanı tabloya yaz. Kalanlarda ne fark ediyorsun?",
    "Bölmede daha önce çıkmış bir kalan yeniden çıkarsa bölümdeki basamaklar <span class='bos'></span>. Bu gösterime devirli ondalık gösterim denir ve 0,333… gibi yazılır.",
    sekil=K2, hata=f"Devri yanlış basamaktan başlatmak: {fr(5, 6)} = 0,8333… gösteriminde 8 tekrar etmez. Peki hangi basamağın tekrar ettiğini neye bakarak anlarsın?",
    yazilida="“… ondalık gösteriminin devirli olduğunu bölme işlemindeki kalanları kullanarak açıklayınız.”"))
d = SORULAR[1]; g.append(dna.soru("soru2", ser("Konu 2 · Soru 2", "konu"), 2, d["baslik"], d["metin"], d["madde"], (d["bil"], d["guc"]), tuyo=d["tuyo"], coz_ust=d["coz"]))
g.append(dna.konu("konu3", ser("Konu 3 · Sonlu mu, devirli mi?", "konu"), 3, "Sonlu mu, devirli mi?",
    "Bölmede kalan her zaman bölenden küçüktür. Bir sayıyı 7'ye bölerken en çok kaç farklı kalan çıkabilir? Bu, bölmenin sonu için ne söyler?",
    "Bölme ya biter ya da bir kalan tekrar eder. Bu yüzden her rasyonel sayının ondalık gösterimi ya sonludur ya da devirlidir.",
    hata=f"Uzun bir gösterimi devirli sanmak: {fr(1, 16)} = 0,0625 uzundur ama biter. Peki bir gösterimin devirli olduğuna neye bakarak karar verirsin?",
    yazilida="“… sayılarından hangilerinin ondalık gösteriminin devirli olduğunu gerekçesiyle belirleyiniz.”"))
d = SORULAR[2]; g.append(dna.soru("soru3", ser("Konu 3 · Soru 3", "konu"), 3, d["baslik"], d["metin"], d["madde"], (d["bil"], d["guc"]), tuyo=d["tuyo"], coz_ust=d["coz"]))
g.append(dna.kaydet("kaydet", ser("Kaydet", "konu"), ["Ondalık gösterim: payı paydaya böl.", "Bir kalan yeniden çıkarsa basamaklar da yeniden gelir.", "Her rasyonel sayının gösterimi ya sonlu ya devirlidir."], SLOGAN["slogan"]))
g.append(dna.kavrama_kapak("test", ser("Kavrama testi", "test"), ["2 küme sorusu", "1 aktarım sorusu", "1 tekrar sorusu"]))
for k in KT:
    g.append(dna.kavrama(f"test{k['no']}", ser(f"Kavrama testi · {k['no']} / 4", "test"), k["no"], 4, k["metin"]))
g.append(dna.odev("odev", ser("Bu hafta", "odev"),
    "Bu haftanın ödevi kavrama testinden sonra verilecek. Geçtiğin konudan ödev yok; takıldığın yere birkaç hedefli soru gelecek.",
    [("Kaynak kitap · Rasyonel sayıların ondalık gösterimi", "öğretmen yazar")], sonraki="Rasyonel sayıları karşılaştırma ve sıralama (MAT.7.1.3)."))
assert next(sira, None) is None, "slayt sayısı N ile tutmuyor"

# sözcük sınırı: konu kartı metni ≤ 60 sözcük
import re
for parca in g:
    if 'class="s konu"' in parca:
        duz = re.sub(r"<[^>]+>|\$[^$]*\$", " ", parca.split('class="govde"')[0].split('class="once"')[1]) + " " + re.sub(r"<[^>]+>|\$[^$]*\$", " ", parca.split('class="kural"')[1].split("</div>")[0])
        assert len(duz.split()) <= 60, len(duz.split())

BOSLUK = {"konu1": "payı", "konu2": "yeniden gel"}
for parca in g:
    for kim, c in BOSLUK.items():
        if f'id="{kim}"' in parca:
            assert c not in re.sub(r"<[^>]+>", " ", parca).lower(), f"{kim}: boşluğun cevabı kartta görünüyor"
govde = os.path.join(KL, "ders6_govde.html")
open(govde, "w", encoding="utf-8").write("".join(g))
PDF = os.path.join(KL, "DNAMATHOS_7_Ders6_Ondalik.pdf")
r = subprocess.run([sys.executable, os.path.join(SK, "slayt_uret.py"), govde, PDF, "--katex", a.katex,
                    "--goruntu", os.path.join(KL, "goruntu"), "--baslik", "DNAMATHOS 7. sınıf Ders 6 · Ondalık gösterim"])
os.remove(govde)
if os.path.exists(PDF[:-4] + ".html"): os.remove(PDF[:-4] + ".html")
if r.returncode: sys.exit("Ders PDF'inde taşma sorunu var.")

# ---------------- A4 belgeler ----------------
CSS_A4 = font_css() + open(os.path.join(KL, "a4.css"), encoding="utf-8").read()


def a4(ad, govde):
    yol = os.path.join(KL, ad + ".html")
    open(yol, "w", encoding="utf-8").write(f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><title>{ad}</title>"
        f"<link rel='stylesheet' href='file://{a.katex}/katex.min.css'><style>{CSS_A4}</style>"
        f"<script src='file://{a.katex}/katex.min.js'></script><script src='file://{a.katex}/contrib/auto-render.min.js'></script></head><body>{govde}</body></html>")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto("file://" + yol); pg.wait_for_load_state("networkidle")
        pg.evaluate("renderMathInElement(document.body,{delimiters:[{left:'$',right:'$',display:false}],throwOnError:true})")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=os.path.join(KL, ad + ".pdf"), print_background=True, prefer_css_page_size=True)
        b.close()
    os.remove(yol)


def kavrama_kagidi():
    s = ['<div class="ust"><h1>Bu dersi kontrol edelim</h1><small>7. sınıf · Ondalık gösterim · Ders 6</small></div>',
         '<div class="ad"><span>Ad:</span><span>Tarih:</span></div>',
         '<div class="yon">Her soruda cevabını yaz, sonra nasıl karar verdiğini bir cümleyle açıkla. Sağdaki kutulardan birini işaretle: ne kadar eminsin? Süre: 12 dakika. Not verilmez.</div>']
    for k in KT:
        s.append(f'<div class="soru"><div class="guven"><span>Eminim</span><span>Emin değilim</span></div><h2>{k["no"]}. {k["metin"]}</h2>'
                 '<div class="alan">a) Cevap:</div><div class="satir"></div><div class="satir"></div>'
                 '<div class="alan">b) Nasıl karar verdin? Bir cümleyle yaz.</div><div class="satir"></div><div class="satir"></div><div class="satir"></div></div>')
    return "".join(s) + '<div class="dna">DNA<i>mathos</i></div>'


def ogretmen():
    li = lambda xs: "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
    s = ['<div class="ust"><h1>Ders 6 · öğretmen dosyası</h1><small>7. sınıf · MAT.7.1.2 · 70 dk</small></div>',
         '<table><tr><th>Çıktı</th><td>MAT.7.1.2 Gerçek yaşam durumlarında rasyonel sayıların ondalık gösterimlerini yansıtabilme (KB2.15 Yansıtma)</td></tr>'
         '<tr><th>Bileşenler</th><td>a) Bölme işlemini kullanarak her rasyonel sayının bir ondalık gösterimi olduğunu inceler. · b) Rasyonel sayıların ondalık gösterimlerinden bazılarının devirli olduğuna dair çıkarım yapar. · c) Her rasyonel sayının devirli ya da devirsiz ondalık açılımları olduğunu değerlendirir.</td></tr>'
         '<tr><th>Program notu</th><td>Bu çıktıda sınırlama cümlesi yok. Uygulama önerisi: paydası 10\'un kuvveti olarak yazılabilen ve yazılamayan sayılarda pay paydaya bölünür; 0,99999… sayısının 1\'e eşitliği sınıf tartışması olarak önerilir. Devir çizgisi programın Sembol ve Gösterimler listesinde yok; öğrenci belgelerinde “…” kullanıldı.</td></tr>'
         '<tr><th>Kaynak</th><td>TYMM 7. sınıf 1. Tema (1) sayfası, 11.11.2026. Ders kitabı paylaşılmadı: kart altındaki “Kitapta” satırları bölüm adını verir, basılı sayfa numarasını kitap gelince yazın.</td></tr></table>',
         '<h2>Ders planı (2 × 35 dk)</h2><table><tr><th>Dk</th><th>Bölüm</th><th>Bileşen</th><th>Not</th></tr>'
         '<tr><td>0–5</td><td>Isınma, 8 soru</td><td>7.1.1-a, b, c · 6.1.5</td><td>Her soru 20 sn; cevap ekranında tek cümle.</td></tr>'
         '<tr><td>5–20</td><td>Konu 1 + Soru 1</td><td>7.1.2-a</td><td>Önce sen: iki yolu karşılaştırma.</td></tr>'
         '<tr><td>20–37</td><td>Konu 2 + Soru 2</td><td>7.1.2-a, b</td><td>Kalan tablosu tahtada.</td></tr>'
         '<tr><td>37–55</td><td>Konu 3 + Soru 3</td><td>7.1.2-b, c</td><td>Varsayım sınama; isterseniz 0,999… tartışması (zenginleştirme).</td></tr>'
         '<tr><td>55–57</td><td>Kaydet ve slogan</td><td>—</td><td></td></tr><tr><td>57–69</td><td>Kavrama testi</td><td>7.1.2-a, b, c · 7.1.1-b</td><td>Notsuz.</td></tr><tr><td>69–70</td><td>Ödev kartı</td><td>—</td><td>Ödev test sonucuna bağlı.</td></tr></table>',
         '<h2>Kartlardaki boşluklar</h2><table><tr><th>Kart</th><th>Cevap</th><th>Sokratik not</th></tr>'
         f'<tr><td>Konu 1</td><td>payı</td><td>{fr(1, 3)} satırında genişletme sütunu boş kalır: “Neden 10, 100, 1000\'e genişletemedik? Bölme yine de çalıştı mı?”</td></tr>'
         '<tr><td>Konu 2</td><td>da yeniden gelir (tekrar eder)</td><td>Kalan sütununu öğrenci doldurur; “Bu kalanı daha önce gördük mü?” diye sorun.</td></tr>'
         '<tr><td>Konu 3</td><td>—</td><td>Önce sen: 7\'ye bölmede en çok 6 farklı sıfırdan büyük kalan (1–6) çıkar; 7. adımda ya 0 gelmiş ya bir kalan tekrar etmiştir. Hata kutusunun cevabı: kalanların tekrar edip etmediğine bakılır.</td></tr></table>',
         '<h2>Ders soruları · adım puanlı çözüm (her soru 10 puan)</h2>']
    for d in SORULAR:
        s.append(f'<div class="k"><h3>Soru {d["no"]} · {d["baslik"]} · {d["bil"]} · {d["guc"]}</h3>{li(d["cozum"])}<div class="etk">Tüyo: {d["tuyo"]}</div></div>')
    s.append('<h2>Isınma · cevap listesi</h2><table><tr><th>#</th><th>Biçim</th><th>Bileşen</th><th>Ne zaman</th><th>Cevap</th><th>Yanlış cevaba tek cümle</th></tr>' +
             "".join(f"<tr><td>{i}</td><td>{t[0]}</td><td>{t[1]}</td><td>{t[2]}</td><td>{t[4]}</td><td>{t[6]}</td></tr>" for i, t in enumerate(TUR, 1)) + "</table>")
    s.append(f'<h2>Haftanın sloganı</h2><table><tr><th>Slogan</th><td>{SLOGAN["slogan"]}</td></tr><tr><th>Tam kural</th><td>{SLOGAN["kural"]}</td></tr>'
             f'<tr><th>Sınır</th><td>{SLOGAN["karsi"]}</td></tr><tr><th>Neden sorusu</th><td>{SLOGAN["neden"]}</td></tr></table>'
             '<table><tr><th>Denetimden geçemeyen öneri</th><th>Neden</th></tr>' + "".join(f"<tr><td>{x}</td><td>{y}</td></tr>" for x, y in REDDEDILEN) + "</table>")
    s.append('<h2>Kavrama testi · anahtar</h2><div class="etk">Her soruda cevap ve gerekçe ayrı: 1 doğru, 0,5 yarım, 0 yanlış ya da boş. Güven: eminim 1, emin değilim 0. Karar: <code>kavrama_karari.py</code>.</div>')
    for k in KT:
        s.append(f'<div class="k"><h3>Soru {k["no"]} · {k["tur"]} · {", ".join(k["bil"])}</h3><b>Cevap:</b> {k["cevap"]}<div class="etk">En zor durum: {k["en_zor"]}</div>'
                 f'<b>Kabul edilen gerekçe</b>{li(k["kabul"])}<b>Kabul edilmeyen</b>{li(k["red"])}'
                 '<table><tr><th>Sık hatalı cevap</th><th>Neyi gösterir, ne yapılır</th></tr>' + "".join(f"<tr><td>{x}</td><td>{y}</td></tr>" for x, y in k["hatalar"]) + "</table></div>")
    s.append('<h2>Hedefli soru bankası</h2><table><tr><th>Bileşen</th><th>Soru</th><th>Cevap</th></tr>' + "".join(f"<tr><td>{b}</td><td>{q}</td><td>{c}</td></tr>" for b, q, c in BANKA) + "</table>")
    s.append('<h2>Bileşen kapsaması</h2><table><tr><th>Bileşen</th><th>Konu kartı</th><th>Ders sorusu</th><th>Kavrama testi</th><th>Banka</th></tr>' +
             "".join(f"<tr><td>{b}</td><td>{kk}</td><td>{', '.join(str(d['no']) for d in SORULAR if b in d['bil'])}</td><td>{', '.join(str(k['no']) for k in KT if b in k['bil'])}</td><td>{sum(x[0] == b for x in BANKA)}</td></tr>"
                     for b, kk in [("7.1.2-a", "1"), ("7.1.2-b", "2"), ("7.1.2-c", "3"), ("7.1.1-b", "—")]) + "</table>")
    s.append('<h2>Karar kuralı</h2>Bileşen puanı ≥ 0,85 geçti (ödev yok) · 0,5–0,85 kısa telafi (2 soru) · &lt; 0,5 yeniden ele al (telafi ve 3 soru). Emin ama yanlış cevap en az “yeniden ele al”dır. Haftalık ödev en çok 6 soru.')
    return "".join(s)


for b in ("7.1.2-a", "7.1.2-b", "7.1.2-c"):
    assert any(b in d["bil"] for d in SORULAR) and any(b in k["bil"] for k in KT) and sum(x[0] == b for x in BANKA) >= 3, b

a4("DNAMATHOS_7_Ders6_Kavrama", kavrama_kagidi())
a4("DNAMATHOS_7_Ders6_Ogretmen", ogretmen())

# ---------------- Veri dosyaları ----------------
json.dump(["0,875", "0,45", "0,3636", "0,175", "0,41666", "0,666…", "sonludur; örneğin"], open(os.path.join(KL, "cevaplar.json"), "w", encoding="utf-8"), ensure_ascii=False)
json.dump({"6": {"slogan": SLOGAN["slogan"], "cikti": "MAT.7.1.2"}, "5": {"slogan": "Her rasyonel sayının sayı doğrusunda bir yeri var.", "cikti": "MAT.7.1.1"}},
          open(os.path.join(KL, "slogan_bankasi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sonuc = {"hafta": 6, "sinif": 7, "cikti": ["MAT.7.1.2"],
         "sorular": {f"S{k['no']}": dict(tur={"Küme sorusu": "kume", "Aktarım sorusu": "aktarim", "Tekrar sorusu": "tekrar"}[k["tur"]], bilesenler=k["bil"], **({"islendi": k["islendi"]} if "islendi" in k else {})) for k in KT},
         "ogrenciler": {
          "Öğrenci A": {"S1": {"cevap": 1, "gerekce": 1, "emin": 1}, "S2": {"cevap": 1, "gerekce": 1, "emin": 1}, "S3": {"cevap": 1, "gerekce": 1, "emin": 1}, "S4": {"cevap": 1, "gerekce": 1, "emin": 1}},
          "Öğrenci B": {"S1": {"cevap": 1, "gerekce": 0.5, "emin": 1}, "S2": {"cevap": 0, "gerekce": 0, "emin": 1}, "S3": {"cevap": 1, "gerekce": 1, "emin": 0}, "S4": {"cevap": 1, "gerekce": 1, "emin": 1}},
          "Öğrenci C": {"S1": {"cevap": 0, "gerekce": 0, "emin": 0}, "S2": {"cevap": 0, "gerekce": 0, "emin": 1}, "S3": {"cevap": 0, "gerekce": 0, "emin": 1}, "S4": {"cevap": 0, "gerekce": 0, "emin": 0}}}}
json.dump(sonuc, open(os.path.join(KL, "kavrama_sonuc.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"Üretildi: ders ({N} slayt), öğretmen dosyası, kavrama kâğıdı, cevaplar.json, kavrama_sonuc.json, slogan_bankasi.json")
