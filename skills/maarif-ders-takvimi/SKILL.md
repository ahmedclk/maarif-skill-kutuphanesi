---
name: maarif-ders-takvimi
description: Sınava ya da dönem sonuna kalan haftalara göre Maarif Modeli çıktılarını derslere dağıtan haftalık ders takvimini hazırlar; her dersin çıktısını, süreç bileşenlerini, ders kitabı sayfalarını, tekrar ve yazılı provası haftalarını ve kaynak kitaptan ödev sayfalarını gösterir. Netleştirici soru sormadan önce yükle. Tetikleyiciler - yazılıya 8 hafta var dersleri planla, bu konuları haftalara dağıt, ortak sınav senaryosuna göre takvim, yıllık ya da dönemlik plan, haftalık özel ders planı, hangi hafta hangi konu. Tek bir dersin ayrıntılı planı için değil (maarif-ders-plani), slayt ya da konu özeti için değil (maarif-konu-ozeti), program okuma tek başına isteniyorsa değil (maarif-cikti-cozumleme).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: TYMM sayfaları için web erişimi; ders kitabı ya da kaynak kitap içindekiler sayfası PDF ya da görüntü olarak verilebilir.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: Türkiye Yüzyılı Maarif Modeli, TYMM öğretim programları ve MEB ortak sınav senaryoları
  dersler: matematik (tam); diğerleri şablonla
  kanit: 6. sınıf (2. yazılı, 16 ders) ve 9. sınıf (2. yazılı, 16 ders) takvimlerinde kullanıldı
---

# Maarif ders takvimi

Amaç: Kalan süreye sığan, sınavın ölçeceği bileşenleri önceleyen ve her haftası bir çıktıya bağlı bir takvim. Takvim öğretmenin saklayacağı ve haftalık açacağı bir tablodur; öteki skill'ler (konu özeti, ders planı, yazılı) her haftanın satırını girdi olarak alır.

Öğretmene giden metin `references/ortak/uslup/onyargisiz-dil.md`, `references/ortak/uslup/turkce-yazim.md` ve `references/ortak/uslup/ilerleme-ve-kapanis.md` kurallarına uyar.

## Adım 0 — Yönlendirme (sessiz)

1. `references/ortak/maarif/cerceve.md` ve `references/ortak/maarif/tymm-erisim.md` dosyalarını oku.
2. Dersin dosyasını oku: matematik → `references/dersler/matematik.md`. Ders dosyası yoksa `references/ortak/dersler/_sablon.md` başlıklarını izle ve takvimin altına "ders dosyası yok" notunu ekle.
3. Aynı oturumda `maarif-cikti-cozumleme` bir `cikti.json` ürettiyse onu kullan; programı yeniden okuma.

## Adım 1 — Girdiler ve netleştirme (en fazla bir soru)

| Girdi | Yoksa |
| --- | --- |
| Sınıf ve ders | İstekten ya da kitaptan çıkar; çıkmıyorsa sor (tek soru budur) |
| Sınava kalan hafta ve haftalık ders saati | Varsayılan: dönem sonuna kalan hafta, haftada 1 ders |
| Sınav konu listesi ya da MEB ortak sınav senaryosu | Takvim temadaki bütün çıktıları kapsar |
| Ders kitabı (PDF) | Kitap sayfası sütunu "—" kalır |
| Kaynak kitap içindekiler sayfası | Ödev sütunu yazılmaz; uydurulmaz |
| Önceki takvim ya da "sonraki derste" notu | Baştan başlanır |

MEB mevzuatına göre okul sınavları il zümresinin hazırladığı ve okul zümresinin seçtiği senaryoya göre yapılır ve bir dönemde iki yazılı vardır (MEV-14, MEV-15, `references/ortak/maarif/meb-olcme-mevzuati.md`); takvim seçilen senaryoyu esas alır. Senaryo tablosu ikincil bir kaynaktan geliyorsa (sosyal medya, yayınevi) bunu takvimde bir satırla belirt.

## Adım 2 — Programa dayandır

Her çıktı için birebir metin, bileşenler ve sınırlar tema sayfasından alınır (`tymm-erisim.md`). Her bileşen için ölçülebilirlik (yazılı · süreç · performans) çıktı kartındaki gibi işaretlenir. Kitap tema numarası siteyle tutmuyorsa sitedeki kodu kullan ve farkı not et.

## Adım 3 — Dağıt

Kurallar `references/dagitim-kurallari.md` dosyasındadır; önce onu oku. Özet:

- Haftada bir ders varsayılır; sınavdan önceki son ders genel tekrar ve yazılı provasıdır.
- Konular sığmıyorsa küçük iki çıktı ya da bir çıktının iki kısmı birleştirilir; sığıyorsa en kalabalık çıktıya (bileşen sayısı en büyük) ikinci ders verilir.
- Senaryodaki soru ağırlığı yüksek çıktı önce ve daha uzun işlenir; yazılıda ölçülmeyen bileşen tekrar haftasına konmaz.
- Her ders satırı en çok 4 konu kartına ve 4–5 soruya sığmalıdır (ders süresi 40 dk; ders saati farklıysa orantıla).

## Adım 4 — Takvim tablosu

Sütunlar: hafta · tarih (verildiyse) · ders no · konu başlığı · çıktı kodu ve bileşen harfleri · beceri · kitap bölümü ve basılı sayfa · ödev (kaynak kitap, bölüm, sayfa aralığı) · not (tekrar, prova, birleşik ders).

Ödev sütunu yalnız içindekiler sayfasından okunur: bölümün başladığı sayfadan bir sonraki bölümün başladığı sayfanın bir eksiğine kadar. İki kaynak kitap verildiyse iki sütun açılır. Tema Değerlendirme ve Bağlam Temelli Sorular tekrar ya da karma derslere verilir; aynı bölüm iki kez verilmez.

Teslim biçimi: öğretmen tabloyu saklayıp güncelleyecekse tablo türünden (Sheets) bir artifact; bu tür yoksa .xlsx (xlsx skill) ya da Markdown tablo. Takvimin altında bir "kapsama özeti" bulunur: çıktı · bileşen · hangi derste.

## Adım 5 — Doğrulama

- Kapsama: Sınav konu listesindeki her çıktı ve yazılıda ölçülen her bileşen en az bir derste var; hiçbir ders TYMM sınırını aşan bir konu taşımıyor. Bunu kodla say (bileşen → ders eşlemesi; eksik 0).
- Hafta sayısı verilen sayıya eşit; son ders tekrar ve prova.
- Ödev sayfaları içindekiler görüntüsüyle birebir; her biri yeniden okunup karşılaştırıldı.
- `python3 scripts/tymm_kod_denetle.py <takvim dosyası> --veri references/veri` 0 hata.

## Adım 6 — Kapanış

Takvimi bir satırla sun ve aldığın kararları yaz (birleşik dersler, ikinci ders verilen çıktı, kitap ile site farkı). En fazla iki somut seçenek: "İlk üç dersin konu özeti slaytlarını hazırlayayım mı?" (maarif-konu-ozeti) ya da "1. dersin ayrıntılı planını çıkarayım mı?" (maarif-ders-plani).

## Denetim listesi

- [ ] Kodlar ve bileşenler sayfadan; kitap tema farkı not edildi
- [ ] Senaryo ağırlığı ve kalan hafta dağıtıma yansıdı; son ders tekrar ve prova
- [ ] Her ders 40 dakikaya sığıyor (en çok 4 konu kartı, 4–5 soru)
- [ ] Ödev sayfaları uydurma değil; aynı bölüm iki kez yok
- [ ] Kapsama eksiği 0; kod denetimi 0 hata
