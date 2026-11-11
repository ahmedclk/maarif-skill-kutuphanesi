# Haftalık paket: ısınma turu ve kavrama testi

Konu özeti her ders için varsayılan olarak üç parçalı bir paket üretir: **ders başı ısınma turu**, **konu özeti** ve **ders sonu kavrama testi**. Ödev kartı da kavrama testinin sonucuna bağlanır. Kurallar `maarif-hizli-tekrar` ve `maarif-kavrama-testi` skill'leriyle ortaktır ve bu skill'in içindedir; o skill'lerin yüklü olması gerekmez.

## Ne zaman üretilmez?

Öğretmen "yalnız özet", "ısınma olmasın" ya da "kavrama testi olmasın" derse ilgili parça atlanır ve teslimde bir satırla söylenir. İlkokulda (1–4) kavrama testi üretilmez (MEV-41); ısınma turu sınav adı taşımayan bir oyun etkinliği olarak kalır.

## 1. Isınma turu (dersin ilk 5 dakikası)

- Kurallar: `references/ortak/haftalik/hizli-tekrar-bicimleri.md` ve `references/ortak/haftalik/slogan-olcutu.md`; matematik ayrıntısı `references/ortak/dersler/matematik/kavrama-ve-tekrar.md` ("Hızlı tekrar").
- Soru sayısı: 6 (ders süresi 70 dakika ve üstüyse 8). Her soru ≤ 20 saniye; en az iki biçim, en az bir "hatayı bul".
- Seçim:
  - Öğrenci geçmişi (`kavrama_gecmisi.json`) varsa `python3 scripts/tekrar_sec.py --hafta <hafta> --gecmis kavrama_gecmisi.json` ile.
  - Yoksa takvimden: yarısı geçen dersten, kalanı 2–4 ve 8 hafta önceki derslerden; aynı konudan art arda iki soru yok.
  - **Temanın ilk dersi ya da üretilen setin 1. dersi:** önceki ders yoksa tur, önceki sınıfın ön koşul çıktısını yoklar ("Hazır mıyız?" kartının yerine geçer).
- Son soru, bir önceki dersin sloganını tamamlatır (ilk derste atlanır).
- Slaytlar: kapak ("Isınalım"), her soru ve ardından cevap ekranı; konu özetinin tasarımıyla, kapaktan hemen sonra.

## 2. Haftanın sloganı

- Her dersin Kaydet kartının altında tek bir slogan bulunur. Slogan Kaydet kartındaki kurallardan birini kısaltır ve beş denetimden geçer (slogan ölçütü).
- Öğretmen dosyasında slogan dört satırla verilir: slogan · tam kural · sınır ya da karşı örnek · neden sorusu ve cevabı.
- Sloganlar ders ders `slogan_bankasi.json` dosyasında birikir; sonraki dersin ısınma turu bunu kullanır.

## 3. Kavrama testi (dersin son 12 dakikası)

- Kurallar: `references/ortak/haftalik/kavrama-testi-tasarimi.md`, `references/ortak/haftalik/kavrama-karar-kurali.md`, `references/ortak/haftalik/kavrama-cikti-bicimi.md`; matematik ayrıntısı `references/ortak/dersler/matematik/kavrama-ve-tekrar.md` ("Kavrama testi").
- **Yazılı provası sorusunun yerini alır.** Normal derslerde Kaydet kartından sonra tüyosuz yazılı provası yerine 4 soruluk kavrama testi gelir: 2 küme sorusu (cevap ve gerekçe), 1 aktarım sorusu ve 1 tekrar sorusu. Aktarım sorusu yazılı provasının işini görür: bütüncül, tüyosuz ve MEB yönerge dilindedir.
- **Tekrar dersi** (sınavdan önceki son ders): kavrama testi yerine yazılı provası kalır; tekrar dersinin kendisi ölçme dersidir.
- Biçim: slaytlarda her soru bir ekran ve yazma alanı (çevrim içi derste tabletle doldurulur); ayrıca yazdırılabilir A4 öğrenci kâğıdı (`DNAMATHOS_<sınıf>_<kapsam>_Kavrama.pdf` gibi, tek dosyada bütün derslerin kâğıtları, her ders yeni sayfada).
- Öğretmen dosyasına: doğru cevaplar, kabul edilen ve edilmeyen gerekçeler, sık hatalı cevaplar, her bileşen için 3 soruluk hedefli soru bankası ve boş `kavrama_sonuc.json` şablonu.

## 4. Ödev kartı

- Kavrama testi üretildiyse ödev kartı şunu der: "Bu haftanın ödevi kavrama testinden sonra verilecek. Geçtiğin konudan ödev yok; takıldığın yere birkaç hedefli soru gelecek."
- Kaynak kitaptan bölüm ve sayfa aralığı **isteğe bağlı ek çalışma** olarak kalır (içindekiler sayfasından; uydurulmaz).
- Öğretmen sonuçları girince: `python3 scripts/kavrama_karari.py kavrama_sonuc.json --gecmis kavrama_gecmisi.json`. Hedefli ödev öğretmen dosyasındaki soru bankasından seçilir; haftalık en çok 6 soru.

## 5. Süre bütçesi

| Ders süresi | Isınma | Konu ve soru çiftleri | Kaydet ve slogan | Kavrama testi | Ödev |
| --- | --- | --- | --- | --- | --- |
| 40 dk | 5 dk (6 soru) | 2–3 çift | 2 dk | 12 dk | 1 dk |
| 70 dk (2 × 35) | 5 dk (8 soru) | 3–4 çift | 2 dk | 12 dk | 1 dk |

Süre yetmiyorsa önce konu kartı sayısı azaltılır; ısınma ve kavrama testi kısaltılmaz.
