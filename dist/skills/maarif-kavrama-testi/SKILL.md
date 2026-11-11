---
name: maarif-kavrama-testi
description: Haftalık konu bittikten sonra öğrencinin konuyu kavrayıp kavramadığını en az soruyla ölçen 4–5 soruluk, 10–15 dakikalık, notsuz kavrama testi hazırlar; haftanın süreç bileşenlerini kümeleyip her kümede en zor durumu cevap ve gerekçe isteyen iki katmanlı sorularla yoklar, bir aktarım sorusu ve önceki haftalardan bir tekrar sorusu ekler; sonuçlardan öğrenci başına geçti, kısa telafi ya da yeniden ele al kararı ve yalnız takılan bileşenler için hedefli kısa ödev üretir. Netleştirici soru sormadan önce yükle. Tetikleyiciler - konuyu anladı mı test et, haftalık kontrol, hafta sonu testi, az soruyla kavrama ölçümü, konu bitti öğrenci hazır mı, ödevi azaltmak istiyorum, sonuçlara göre ödev ver. Ders sonu 1–3 maddelik çıkış kartı için değil (maarif-anlama-kontrolu), puanlanan okul yazılısı için değil (maarif-ortak-yazili), LGS tarama testi için değil (maarif-beceri-temelli-test), ders başı hızlı soru turu ve slogan için değil (maarif-hizli-tekrar).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: TYMM sayfaları için web erişimi; Python 3 (karar ve tekrar betikleri).
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: TYMM süreç bileşenleri; MEB kısa süreli sınav (notsuz, anında geri bildirim)
  dersler: matematik (tam); diğerleri şablonla
  kanit: taslak
---

# Maarif kavrama testi

Amaç: Haftanın konusunu öğrencinin gerçekten kavrayıp kavramadığını **en az soruyla** öğrenmek ve ödevi bu sonuca göre **en aza indirmek**. Test notsuzdur; MEB mevzuatındaki kısa süreli sınavın karşılığıdır: birkaç soru, kısa süre, anında geri bildirim (MEV-40, `references/ortak/maarif/meb-olcme-mevzuati.md`). Programdaki öğrenme kanıtları arasında da izleme testi yer alır.

Öğrenciye ve öğretmene giden metin `references/ortak/uslup/onyargisiz-dil.md`, `references/ortak/uslup/turkce-yazim.md` ve `references/ortak/uslup/ilerleme-ve-kapanis.md` kurallarına uyar. Öğrenci verisi takma adla işlenir (`references/ortak/guvence/kvkk-ve-telif.md`).

## Adım 0 — Yönlendirme (sessiz)

1. **Omurga:** `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`, `references/ortak/maarif/meb-olcme-mevzuati.md`.
2. **Ders:** `references/dersler/<ders>.md` dosyasını şimdi oku (matematik → `references/dersler/matematik.md`). Okumadan soru tasarlamak kritik hatadır. Ders dosyası yoksa `references/ortak/dersler/_sablon.md` ile çalış ve öğretmen kâğıdına not ekle.
3. **Tasarım kuralları:** `references/test-tasarimi.md` ve `references/karar-kurali.md` dosyalarını oku.
4. Aynı oturumda bir takvim, `cikti.json` ya da önceki haftaların sonuç dosyası (`kavrama_gecmisi.json`) varsa onu kullan.

## Adım 1 — Netleştirme (en fazla bir soru)

Haftanın konusu ya da çıktısı belli değilse yalnız onu sor. Varsayılanlar sessizce: 4 soru (bileşen kümesi 4'ten fazlaysa 5), 12 dakika, birebir ders. İlkokulda test üretilmez (MEV-41); bunu tek cümleyle söyle ve gözlem etkinliği öner.

## Adım 2 — Programa dayandır

Haftanın çıktıları için tema sayfasından birebir: bileşenler, İçerik Çerçevesi, uygulamalardaki sınırlamalar (ör. "… kavramlarına değinilmez"). Sınır dışı bir soru, en az soruyla ölçme amacını boşa çıkarır; sınırlar sorunun da sınırıdır.

## Adım 3 — Bileşen haritası ve kümeler

`test-tasarimi.md` 1. bölümü: bileşenleri birbirine dayanma ilişkisine göre 2–4 kümeye ayır; her kümenin **en zor yapısal durumunu** yaz. Yazılıda ölçülemeyen bileşen (grup tartışması, veri toplama) teste alınmaz; öğretmen kâğıdında "gözlemle izlenir" diye görünür.

## Adım 4 — Soruları yaz

`test-tasarimi.md` 2. bölümündeki dört soru türüyle:

1. **Küme soruları (2–3):** her biri bir kümenin en zor durumunu iki katmanlı biçimde yoklar: cevap + tek cümlelik gerekçe.
2. **Aktarım sorusu (1):** aynı fikir, öğrencinin derste görmediği bir bağlamda.
3. **Tekrar sorusu (1):** önceki haftalardan, `kavrama_gecmisi.json` varsa en çok "kısa telafi" ya da "yeniden ele al" kalan bileşenden; yoksa 2–4 hafta önceki konudan.
4. Her sorunun yanında öğrencinin işaretleyeceği **güven kutusu**: "Eminim / Emin değilim".

Kurallar: sayılar ve cevaplar kodla hesaplanır; her sorunun cevabı tek ve savunulabilir; öğrenci cümleleri kademe sınırında. Test notsuz olduğu için biçim serbesttir (açık uçlu, gerekçeli doğru-yanlış, gerekçeli eşleştirme, hatayı bulma), ama her soru düşünceyi göstermelidir: yalnız işaretleme isteyen soru yazılmaz.

## Adım 5 — Çıktı

`references/cikti-bicimi.md` dosyasını oku. Üç parça:

1. **Öğrenci kâğıdı:** 4–5 soru, cevap ve gerekçe alanı, güven kutuları; başlık "Bu haftayı kontrol edelim". Puan, düzey ya da kod yazılmaz.
2. **Öğretmen anahtarı:** her soru için doğru cevap, kabul edilen gerekçeler, sık hatalı cevaplar ve neyi gösterdikleri; soru → bileşen eşlemesi; karar tablosu.
3. **Sonuç şablonu:** `kavrama_sonuc.json` (öğretmen her öğrenci için cevap ve gerekçe doğruluğunu ve güveni girer; biçim `karar-kurali.md` dosyasında).

DNAMATHOS tasarımı istenirse ve `dnamathos-pdf-tasarimi` yüklüyse onun tasarımıyla; değilse sade A4 HTML ya da PDF.

## Adım 6 — Sonuçtan karar ve hedefli ödev (öğretmen sonuçları verince)

`python3 scripts/kavrama_karari.py kavrama_sonuc.json --gecmis kavrama_gecmisi.json` çalıştır. Betik her öğrenci ve bileşen için kararı verir, ödev sayısını hesaplar ve geçmiş dosyasını günceller (`karar-kurali.md`):

- **Geçti:** o bileşenden ödev yok.
- **Kısa telafi:** 2 hedefli soru; biri farklı biçimde.
- **Yeniden ele al:** kısa telafi kartı (en çok 60 sözcük, Sokratik) ve 3 hedefli soru; sonraki derste ilk 5 dakika.
- Haftalık ödev üst sınırı 6 soru; aşılırsa öncelik "emin ama yanlış" bileşenlerde.
- Haftanın bileşenlerinin yarısında ya da fazlasında puan 0,5'in altındaysa öğrenci için **konu yeniden işlenir**; ödev 3 soruyla sınırlanır.

Hedefli soruları kendin yaz: aynı bileşen, aynı yapısal durum, bağlam ve sayılar farklı (ikiz soru ilkesi; ayrı bir skill gerekmez). Kurallar ders dosyasında.

## Adım 7 — Doğrulama (dosyalar yazıldıktan sonra)

1. `references/ortak/guvence/dogrulama-kapisi.md` dosyasını şimdi oku; Kapı A ve C'yi her soruya uygula. Alt ajan varsa yalnız öğrenci kâğıdını ona çözdür.
2. Kapsama: her küme bir soruda; aktarım ve tekrar sorusu var; soru sayısı 4–5 (kodla say).
3. `python3 scripts/tymm_kod_denetle.py <öğretmen anahtarı> --veri references/veri` 0 hata.
4. Öğrenci kâğıdında cevap, kod ya da puan yok.

## Adım 8 — Kapanış

Teslimde: soru sayısı, kümeler ve her sorunun hangi kümeyi yokladığı tek tabloda. En fazla iki somut seçenek: "Sonuçları girerseniz öğrenci başına ödevi çıkarayım mı?" ya da "Haftanın hızlı tekrar turunu ve sloganını hazırlayayım mı?" (maarif-hizli-tekrar).

## Denetim listesi

- [ ] 4–5 soru; her bileşen kümesi bir soruda; aktarım ve tekrar sorusu var
- [ ] Her küme sorusu en zor durumu ve gerekçeyi istiyor
- [ ] Sınır aşılmamış; tek savunulabilir cevap
- [ ] Test notsuz; öğrenci kâğıdında puan ve düzey yok
- [ ] Karar betiği çalıştı; ödev ≤ 6 soru ve yalnız takılan bileşenlerde
