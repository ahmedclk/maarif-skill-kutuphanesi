# DNAMATHOS tasarım dili 2.0 (16:9 ekran PDF'i)

Üç ilke: **önce okunabilirlik**, **karakter**, **marka çağrışımı**. Dil üç kaynaktan birleşti: içerik sayfalarının sadeliği (Sarmal), yazı tipi rolleri ve el yazısı yönlendirmeleri (Defter), lacivert ve safran renk blokları (Afiş). Uygulama: `assets/dnamathos.css`, bileşenler: `scripts/dna.py`, yazı tipleri: `assets/fontlar/` (SIL Açık Font Lisansı; lisans metinleri aynı klasörde).

## 1. Sayfa

297 × 167 mm (1123 × 632 px). Her slayt tek sayfa; taşma, kesilme, kayma yok. İçerik slaytlarında 52 px lacivert üst şerit; içerik iç boşluğu 26 px üst, 46 px yan.

## 2. Renk

| Ad | Değer | Kullanım |
| --- | --- | --- |
| Lacivert | #14213d | Ana metin, üst şerit, koyu bloklar |
| Safran | #fca311 | Kapak üst bloğu, konu paneli, Kaydet kartı, vurgu, tüyo notu, etkin düğme |
| Krem | #fdf6e8 | İçerik slaytlarının zemini |
| Hardal | #8a4f00 | Açık zeminde turuncu tonlu etiket yazısı |
| İkincil | #4a5570 | Açıklama ve küçük yazılar |
| Mürekkep | #1f4fa0 | Açık zeminde el yazısı notlar |
| Doğru / yanlış | #0b6157 on #e1f3f0 · #b3401a on #fdece6 | Yalnız doğru ve yanlış kartlarında, işaretle (✓ ✗) birlikte; başka kutuda kullanılmaz |
| Sık yapılan hata kutusu | Beyaz zemin, lacivert sol kenar, hardal etiket | Paletin dışına çıkmaz; pembe ya da kiremit zemin kullanılmaz |

**Karşıtlık kuralları (ölçüldü):** lacivert yazı krem zeminde 14,9:1, beyaz zeminde 16:1; safran yazı lacivert zeminde ve lacivert yazı safran zeminde 7,9:1; hardal krem zeminde 6,1:1. **Safran, açık zeminde yazı rengi olmaz** (beyazda 2:1); açık zeminde yalnız dolgu, vurgu ve çizgidir.

**Dağılım:** Bir derste koyu (lacivert) ve sıcak (safran) bloklar bir ritim kurar: kapak ikisi birden; ısınma ve kavrama testi kapağı lacivert; konu kartı solda safran panel; Kaydet kartı safran; soru, cevap ve ödev slaytları krem. Aynı renkte iki tam blok art arda en fazla üç kez gelir.

## 3. Yazı tipi rolleri

| Rol | Yazı tipi | Nerede |
| --- | --- | --- |
| Başlık | Fraunces 800 (italik 600/800) | Slayt başlıkları, ısınma soruları, Kaydet maddeleri, kapak; marka "DNA*mathos*" |
| Gövde | Atkinson Hyperlegible Next 400/700 | Soru metni, açıklama, kural cümlesi |
| Rakam | Inter 400/700 (gövde ailesine gömülü) | Gövdedeki bütün rakamlar; Atkinson'ın çizgili sıfırı saat ve ondalıkta yadırganır |
| El yazısı | Caveat 600/700 | Öğretmen notları ("kat mı, bölen mi?"), slogan, tüyo; **yalnız kısa notlarda**, gövde metninde asla |
| Etiket | IBM Plex Mono 500/600 | Haplar, çıktı kodu, bileşen ve güçlük çipleri, "ÖNCE SEN", "ÇÖZÜM" |
| Formül | KaTeX | Matematik ifadeleri; ℕ ℤ ℚ ℝ için DejaVu Sans |

**Boyutlar:** gövde en az 17 px (soru metni 21–22 px), başlık 30–58 px, ısınma sorusu 48 px, etiket en az 11 px. `tasma-denetimi.js` bu alt sınırları denetler.

## 4. Marka imzaları

- **DNA sarmalı:** kapakta büyük figür; üst şeritte ilerleme göstergesi (basamaklar ders ilerledikçe safrana boyanır).
- **Marka yazısı:** "DNA" Fraunces 800, "mathos" Fraunces italik 600 safran.
- **Fosforlu kalem vurgusu:** anahtar sözcüğün alt yarısında safran şerit; slaytta en fazla bir kez.
- **Çerçeveli haplar:** konu, soru, biçim ve çıktı etiketleri; yön bildiren haplarda ince ok.
- **El yazısı not:** slayt başına en fazla bir; hafifçe eğik.

## 5. Bileşenler (`scripts/dna.py`)

| Fonksiyon | Slayt |
| --- | --- |
| `kapak` | Üstte safran blok (başlığın ilk kısmı), altta lacivert blok (ikinci kısmı, italik safran), ortada "DERS 08" rozeti, sağ altta sarmal |
| `serit` | Üst şerit: marka, konum, bölüm düğmeleri (Isınma · Konu · Test · Ödev), sarmal ilerleme ve sayfa |
| `tur_kapak`, `tur_soru`, `tur_cevap` | Isınma turu: lacivert soru ekranı ("20 sn" filigranı, biçim hapı, ilerleme noktaları), krem cevap ekranı |
| `konu` | Solda safran panel (Konu hapı, başlık, "Önce sen"), sağda kural, şekil, "Sık yapılan hata", "Yazılıda böyle sorulur", "Kitapta", yazı alanı ya da slogan |
| `soru` | Soru başlığı, metin ve maddeler üstte; **çözüm alanı sorunun hemen altında** (noktalı zemin, ayrı kutu yok); **tüyo aynı sayfada** sağ alt köşede safran yapışkan not |
| `kaydet` | Safran zeminde 2–4 kural ve el yazısıyla slogan |
| `kavrama_kapak`, `kavrama` | Kavrama testi: soru, "a) Cevap" ve "b) Nasıl karar verdin?" yazma çizgileri, "Eminim / Emin değilim" kutuları |
| `odev` | Kavrama testine bağlı ödev cümlesi ve isteğe bağlı ek çalışma tablosu |
| `sayi_dogrusu`, `tablo` | Şekil ve tablo yardımcıları |

## 6. Soru ve tüyo kuralları

- Çözüm alanı ayrı bir panel ya da kutu değildir; soru metninin bittiği yerden sayfanın altına kadar uzanan noktalı zemindir. `coz_ust` değeri metnin bitişine göre ayarlanır; alan en az 150 px yüksekliktedir (denetlenir).
- Tüyo başka sayfaya gitmez; aynı slaytta, sorunun okuma yolunun dışında (sağ alt) durur ve "TAKILIRSAN · TÜYO" başlığını taşır. Her zaman görünürdür; PDF katmanlarıyla gizleme Acrobat dışında güvenilir çalışmadığı için kullanılmaz. Öğretmen tüyonun görünmesini istemiyorsa tüyo yalnız öğretmen dosyasına yazılır.
- Tüyo cevabı, sonucu ya da ilk adımı vermez (konu özeti kuralı).

## 7. Şekil ve tablo

- Şekiller SVG; çizgi lacivert #14213d, vurgu safran #fca311, metin IBM Plex Mono ya da gövde yazısı en az 13 px. Ek renk gerekiyorsa: #1f6fb5, #0b7a5c, #b3401a, #6b2f91 (pastel dolgular: #e8effc, #e1f3f0, #fdece6, #f2e9f9).
- **Öğrenci slaytında şekil cevabı vermez:** işaretlenecek sayı doğrusu boş gelir; ortak noktalar çevrelenmez (`cevrele` yalnız cevap ya da öğretmen slaytında).
- Tablolar HTML (`tablo`): ince kenar, başlık satırı açık safran (#fff3d6) ve kalın.
- Soru görseli ölçütü: `references/ortak/dersler/matematik/soru-gorseli.md`.

## 8. PDF'te güvenli çizim

CSS gradient (linear, radial, repeating) ve yinelenen arka plan resmi kullanılmaz. Chrome bunları PDF'e desen dolgusu olarak yazar; bazı görüntüleyiciler deseni çözemez ve alanı renkli (çoğunlukla pembe) kutu olarak gösterir. Cevap çizgileri kenarlıktır (`.alan i`), çözüm alanının noktalı zemini tek parça SVG'dir (`--noktalar`), fosforlu kalem vurgusu iç gölgedir (`box-shadow: inset`). `pdf_denetle.py` desen dolgulu sayfayı hata sayar.

## 8a. Yazdırılabilir kâğıtlar (A4)

Kavrama testi kâğıdı ve yazılı kâğıtları A4 dikeydir; aynı renk ve yazı tipi rolleri kullanılır: başlık Fraunces, gövde Atkinson (rakamlar Inter), etiketler IBM Plex Mono; zemin beyaz, vurgu safran. Örnek: `ornekler/6-sinif-ortak-kat`.

## 9. Eski tasarım

1.x tasarımının stil dosyası ve denetimi `assets/eski/` klasöründedir; yalnız eski setleri yeniden üretmek için kullanılır.
