---
name: maarif-konu-ozeti
description: MEB ders kitabına ve TYMM programına dayanan, haftalık ders için kısa konu anlatımı özet slaytları hazırlar; her konu kartının ardından yazılı tarzı bir soru, Sokratik öğretmen notu, yazılı tüyosu, Kaydet kartı ve haftanın sloganı, kavrama testine bağlı ödev kartı ve ayrı bir öğretmen çözüm dosyası üretir. Varsayılan olarak her derse ders başı ısınma turu (aralıklı tekrar) ve ders sonu 4 soruluk kavrama testi de ekler; yalnız özet istenirse bunları atlar. Soru sormadan, kapsamı kitaptan ve programdan kendisi belirleyerek çalışır. Tetikleyiciler - bu temanın konu özetini hazırla, haftalık ders paketi, ders anlatım sunumu, yazılıya kadar haftalık ders slaytları, kitabın bu sayfaları için ders sunumu, özel ders slaytı, ders 1-16 sunumları. Tek ders planı belgesi için değil (maarif-ders-plani), yalnız takvim için değil (maarif-ders-takvimi), sınav kâğıdı için değil (maarif-ortak-yazili), Instagram içeriği için değil (dnamathos-instagram-karusel).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: Python 3, Playwright (Chromium), KaTeX, pypdf ve PyMuPDF. TYMM sayfaları için web erişimi. Görsel tasarım için bir marka skill'i (DNAMATHOS için dnamathos-pdf-tasarimi) önerilir.
metadata:
  surum: "2.1.0"
  yazar: DNAMATHOS
  omurga: TYMM öğrenme çıktıları ve süreç bileşenleri; MEB ortak yazılı yönerge dili
  dersler: matematik (tam); diğerleri şablonla
  onceki_ad: maarif-konu-ozeti 1.x (tasarım ve üretim dnamathos-pdf-tasarimi skill'ine taşındı)
  kanit: 6. sınıf (16 ders, 2. yazılı) ve 9. sınıf (16 ders, 2. yazılı) setlerinde kullanıldı
---

# Maarif konu özeti

Amaç: Haftada bir saatlik derste ders kitabındaki konuyu kısa ve öz anlatmak ve her kavramın hemen ardından öğrenciye ortak yazılının istediği biçimde soru çözdürmek. Öğrenci yalnız konuyu öğrenmez; varsayımı sınamayı, önerme tamamlamayı, gerekçelendirmeyi ve çözümünü açıklamayı her derste çalışır. Haftalık süre azdır; bu yüzden özet kısa, ağırlık soru çözümündedir. Anlatım Sokratiktir (`references/ortak/uslup/ogretmen-uslubu.md`): her kavram bir soruyla açılır, küçük adımlarla ve somut örnekle kurulur; yanlış cevap düzeltilmeden önce teşhis edilir.

İçerik dört kaynağa dayanır: (1) öğretmenin paylaştığı ders kitabı, (2) TYMM tema sayfası, (3) MEB yazılı soru üslubu, (4) marka tasarım dili. Akış **soru sormadan ve onay beklemeden** baştan sona yürütülür; kararlar teslim mesajında yazılır.

## Adım 0 — Yönlendirme (sessiz)

1. **Omurga:** `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`.
2. **Haftalık paket:** `references/haftalik-paket.md` dosyasını oku; ısınma turu, slogan, kavrama testi ve ödev kartı kuralları oradadır. Öğretmen "yalnız özet" demedikçe paket üretilir.
3. **Ders:** `references/dersler/<ders>.md` dosyasını şimdi oku (matematik → `references/dersler/matematik.md`); soru üslubu, güçlük ve görsel kuralları oradan gelir. Ders dosyası yoksa `references/ortak/dersler/_sablon.md` başlıklarını izle.
4. **Tasarım:** Kullanıcının marka skill'i yüklüyse (DNAMATHOS → `dnamathos-pdf-tasarimi`) görsel düzen, üretim hattı ve PDF denetimi oradan alınır. Yoksa sade 16:9 HTML slayt ve PDF üretilir; `references/ortak/guvence/pdf-ile-calisma.md` yine uygulanır.
5. Aynı oturumda bir takvim (maarif-ders-takvimi), `cikti.json` (maarif-cikti-cozumleme), `kavrama_gecmisi.json` ya da `slogan_bankasi.json` varsa onu kullan.

## Adım 1 — Kapsamı ve takvimi kendin belirle (soru sorma)

- **Tek soru istisnası:** Ders kitabı hiç paylaşılmadıysa yalnız onu iste. Sınıf, tema ya da çıktı kitaptan ve TYMM'den anlaşılabiliyorsa sorma.
- **Kapsam:** Tema verilirse temadaki bütün dersler; sayfa aralığı ya da çıktı verilirse yalnız onlar; "ilk 5 ders" gibi bir sayı verilirse planın o kısmı.
- **Takvim:** Sınava kalan hafta ve konu listesi verildiyse ders sayısı buna göre belirlenir: haftada bir ders; son ders genel tekrar ve yazılı provası. Sığmıyorsa küçük iki çıktı ya da bir çıktının iki kısmı birleşir; sığıyorsa en kalabalık çıktıya ikinci ders verilir. Takvim verilmediyse: her çıktı bir ders, bileşeni 8'den fazla olan çıktı en çok iki ders. (Ayrıntılı dağıtım `maarif-ders-takvimi` skill'indedir.)
- **Önceki dersler:** "Sonraki derste" notundan devam edilir; aynı konu tekrar anlatılmaz.

## Adım 2 — Kitabı oku ve programla doğrula

`references/kitap-okuma.md` dosyasını oku ve uygula: dersin sayfalarını bul, kesir ve üsleri sayfa görüntüsünden doğrula, basılı sayfa numarasını kullan, kitabın tema numarasını sitedeki kodla eşle. Her kitap bölümünün hangi çıktıya ve bileşene hizmet ettiğini yaz. İçerik Çerçevesi ve uygulamalardaki sınırlar, özetin ve soruların sınırıdır. Kitabın görselleri kopyalanmaz (`references/ortak/guvence/kvkk-ve-telif.md`).

## Adım 3 — Ders planı ve akış

`references/ders-akisi.md`: ısınma turu; her konu kartının hemen ardından o konunun sorusu; Kaydet kartı ve haftanın sloganı; kavrama testi (tekrar dersinde yazılı provası); ödev. Bir derste en çok 4 konu kartı ve 3–4 ders sorusu (tekrar dersinde 7–8). Süre bütçesi `references/haftalik-paket.md` 5. bölümdedir. Plan tablosu öğretmen dosyasına girer.

## Adım 4 — Konu kartları

`references/konu-karti.md`: kart metni en çok 60 sözcük; "Önce sen" sorusu; kural en çok 2 cümle; "Yazılıda böyle sorulur" kutusu (bileşen ve MEB yönerge dili); "Kitapta" atıfı; gerektiğinde "Peki … olsaydı?" ile biten "Sık yapılan hata". Kartlar hiçbir sorunun cevabını vermez. Her derste en az bir kartta kural, öğrencinin tamamlayacağı boşluklu önermedir.

## Adım 5 — Ders soruları ve yazılı tüyoları

`references/ders-sorulari-ve-tuyo.md`. Her soru 1–3 komşu bileşen taşır; her derste en az bir varsayım sınama ya da kişi iddiası, bir boşluklu önerme ve bir "gerekçesiyle açıklayınız" maddesi bulunur. Konu sorularında tüyo vardır; aynı slaytta sağ alt köşede durur ve cevabı, sonucu ya da ilk adımı vermez. Çözüm alanı sorunun hemen altındadır. Güçlük Z · Y · C kuralıyla belirlenir (ders dosyasında). Ders soruları ve yazılı provası MEB yazılı kurallarına uyar: açık uçlu ya da kısa cevaplı, bileşenin bilişsel düzeyinde (MEV-10, MEV-11, MEV-13, `references/ortak/maarif/meb-olcme-mevzuati.md`).

## Adım 6 — Isınma turu, slogan ve kavrama testi

`references/haftalik-paket.md` 1–3. bölümler. Isınma soruları ve kavrama testi soruları kodla çözülür; slogan beş denetimden geçer; kavrama testinin her küme sorusu kümesinin en zor durumunu cevap ve gerekçeyle yoklar.

## Adım 7 — Ödev kartı

`references/odev-karti.md` ve `references/haftalik-paket.md` 4. bölüm. Kavrama testi üretildiyse ödev kartı ödevi testin sonucuna bağlar; kaynak kitap sayfaları isteğe bağlı ek çalışmadır. Öğretmen sonuçları verirse `python3 scripts/kavrama_karari.py kavrama_sonuc.json --gecmis kavrama_gecmisi.json` ile öğrenci başına karar ve hedefli ödev çıkarılır. Ödev yalnız kaynak kitabın içindekiler sayfasından okunur; sayfa ya da test numarası uydurulmaz, özgün ödev sorusu yazılmaz. Kaynak kitap yoksa yalnız onu sor.

## Adım 8 — Öğretmen dosyası

`references/ogretmen-dosyasi.md`: takvim, ders planı tabloları, boşluklu önermelerin cevapları, Sokratik öğretmen notları, her sorunun adım puanlı çözümü ve tüyosu, ısınma turu cevap listesi, slogan satırları, kavrama testi anahtarı ve hedefli soru bankası, bileşen kapsama tablosu. Öğrenci dosyasında cevap yoktur.

## Adım 9 — Üretim

Marka skill'inin üretim hattıyla (DNAMATHOS: `dnamathos-pdf-tasarimi`). Üç dosya: öğrenci PDF'i (ısınma, konu, kavrama testi slaytları), öğretmen PDF'i ve yazdırılabilir kavrama testi kâğıtları. Her ders sorusunun, ısınma sorusunun ve kavrama testi sorusunun sayıları ve çözümleri kodla hesaplanır; içerik dosyasında assert ile denetlenir (bileşen kapsaması, sözcük sınırları, puan toplamları).

## Adım 10 — Doğrulama (dosyalar üretildikten sonra)

1. `references/denetim.md` tablosunu üretilmiş dosyalar üzerinde çalıştır.
2. `references/ortak/guvence/dogrulama-kapisi.md` dosyasını şimdi oku; Kapı A ve C'yi her ders sorusuna ve kavrama testi sorusuna, Kapı C'yi konu kartlarına ve ısınma sorularına uygula.
3. Sızıntı: cevap anahtarındaki ayırt edici dizgeleri `cevaplar.json` dosyasına yaz ve `python3 scripts/sizinti_ara.py <öğrenci PDF> cevaplar.json` çalıştır; sonuç 0.
4. `python3 scripts/tymm_kod_denetle.py <öğrenci PDF> --veri references/veri` 0 hata.
5. Paket: her normal derste ısınma turu (6–8 soru, en az iki biçim, art arda aynı konu yok) ve 4 soruluk kavrama testi (2 küme, 1 aktarım, 1 tekrar) var; tekrar dersinde yazılı provası var; her derste denetlenmiş bir slogan var (kodla say).
6. Mümkünse sızıntı ve matematik denetimini dosyayı görmemiş ayrı bir ajana yaptır.

## Adım 11 — Teslim

`references/teslim.md`: kısa teslim mesajı; ders sayısı ve haftalara dağılım, kitap ile TYMM arasındaki tema ya da terim farkları, plandan ayrılan noktalar, paketten atlanan parçalar. En fazla iki somut seçenek (ör. "16. dersin yazılı provasını ortak yazılı biçiminde ayrı bir kâğıt yapayım mı?" — maarif-ortak-yazili).

## Denetim listesi

- [ ] Ders dosyası ve omurga okundu; kod ve bileşenler sayfadan
- [ ] Her konu kartının ardında soru
- [ ] Isınma turu, slogan ve kavrama testi her normal derste; tekrar dersinde yazılı provası
- [ ] Ödev kartı kavrama testine bağlı; kaynak kitap sayfaları isteğe bağlı
- [ ] Kart ≤ 60 sözcük, "Önce sen" var, sızıntı yok; Kaydet kartında denetlenmiş slogan
- [ ] Tüyo cevabı ya da ilk adımı vermiyor
- [ ] Ödev sayfaları içindekilerle birebir
- [ ] Sızıntı 0, kod denetimi 0 hata, PDF bağlantıları 0 hata
