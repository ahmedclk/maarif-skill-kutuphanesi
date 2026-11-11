---
name: maarif-beceri-temelli-test
description: Maarif Modeli çıktılarına bağlı, LGS ve beceri temelli sınav tarzında çoktan seçmeli test hazırlar; bağlamlı ve görselli maddeler, her biri belirli bir öğrenci hatasından doğan çeldiriciler, dengeli cevap dağılımı, güçlük etiketi ve çeldirici açıklamalı cevap anahtarı üretir; her maddenin tek savunulabilir cevabı olduğunu yazıldıktan sonra doğrular. Netleştirici soru sormadan önce yükle. MEB mevzuatına göre okul yazılısı yerine kullanılamaz; LGS ve TYT hazırlığı, tarama ya da notsuz kısa süreli sınav içindir. Tetikleyiciler - LGS tarzı test hazırla, 20 soruluk tarama testi, beceri temelli soru, yeni nesil soru, konu testi, çoktan seçmeli deneme, kazanım testi. Açık uçlu ortak yazılı için değil (maarif-ortak-yazili), verilen soruların ikizini üretmek için değil (maarif-benzer-soru), 1–3 maddelik puansız anlama kontrolü için değil (maarif-anlama-kontrolu).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: TYMM sayfaları için web erişimi; Python 3 (cevap dağılımı ve güçlük denetimi). PDF için marka skill'i ya da pdf skill'i.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: TYMM öğrenme çıktıları ve süreç bileşenleri; MEB LGS ve beceri temelli örnek soruları
  dersler: matematik (tam); diğerleri şablonla
---

# Maarif beceri temelli test

Amaç: Öğrencinin bilgiyi bağlamdan ve görselden okuyup karar verdiği, işlem yükü az ve akıl yürütme yükü yüksek maddelerden oluşan bir test. Her madde bir çıktıya ve bileşene bağlıdır; her çeldirici bir öğrenci hatasını görünür kılar, böylece test sonuçları `maarif-hata-analizi` için kullanılabilir veri üretir.

Dil: `references/ortak/uslup/turkce-yazim.md`; öğretmene giden metin `references/ortak/uslup/onyargisiz-dil.md` ve `references/ortak/uslup/ilerleme-ve-kapanis.md`.

## Adım 0 — Yönlendirme (sessiz)

1. `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`, `references/ortak/maarif/meb-olcme-mevzuati.md`.
2. Ders dosyası: matematik → `references/dersler/matematik.md` (şimdi oku). Yoksa `references/ortak/dersler/_sablon.md` ve anahtara not.

## Adım 1 — Netleştirme (en fazla bir soru)

**Mevzuat sınırı:** Okul yazılıları açık uçludur ve cevabı öğrenci oluşturur (MEV-10, MEV-12). Öğretmen bu testi puanlanan okul yazılısı olarak isterse bunu tek cümleyle söyle ve `maarif-ortak-yazili` skill'ini öner; test LGS ve TYT hazırlığı, tarama ya da notsuz kısa süreli sınav (MEV-40) olarak hazırlanır ve kâğıdın başlığı bunu belirtir ("Tarama testi", "LGS hazırlık"). İlkokul (1–4) için test üretilmez (MEV-41); öğretmene gözlem aracı ya da `maarif-anlama-kontrolu` önerilir.

Sınıf ya da çıktı belli değilse sor. Varsayılanlar sessizce: ortaokulda 4 seçenek, 20 madde (tarama testi) ya da istenen sayı; sınav türü istekten (LGS, okul testi, TYT).

## Adım 2 — Programa dayandır

Her çıktı için birebir çıktı, bileşenler, sınırlar ve gösterimler. Yalnız yazılıda ölçülebilen bileşenler maddeye dönüşür (`references/ortak/maarif/cerceve.md` 8. bölüm).

## Adım 3 — Madde planı

Yazmadan önce tablo: no · çıktı · bileşen · bağlam alanı · görsel türü · hedef güçlük · hedef hata (en zor çeldiricinin temsil edeceği yanılgı). İki satırın odağı aynı olmaz. Madde sayısı 10'dan fazlaysa ve öğretmen ortamdaysa plan tek mesajla gösterilir; onay beklenmeden de ilerlenebilir.

## Adım 4 — Maddeleri yaz

Kurallar ders dosyasının gösterdiği çoktan seçmeli madde dosyasındadır: kök, seçenek, çeldirici, test bütünü. Her çeldiriciyi yazmadan önce hatasını adlandır ve kökün sayılarına uygulayarak değerini **hesapla**; sonra seçenek yap. Sayısal sonuçlar kodla doğrulanır.

## Adım 5 — Cevap anahtarı ve denetim betikleri

- Anahtar: doğru seçenek · çıktı ve bileşen · güçlük (Z · Y · C) · kısa çözüm · her çeldiricinin hatası.
- `python3 scripts/cevap_dagilimi.py <ANAHTAR> --secenek 4` 0 ihlal.

## Adım 6 — Üretim

Öğrenci test kâğıdı ve öğretmen cevap anahtarı ayrı dosyalar. Marka skill'i yüklüyse onun tasarımı (DNAMATHOS: `dnamathos-pdf-tasarimi`); yoksa pdf skill'i. Optik form gerekiyorsa son sayfada A–D işaretleme tablosu.

## Adım 7 — Doğrulama (dosyalar üretildikten sonra)

`references/ortak/guvence/dogrulama-kapisi.md` dosyasını şimdi oku ve **her maddeye** Kapı A, B ve C'yi uygula; notları geçici dosyaya yaz. Alt ajan varsa yalnız öğrenci kâğıdını ver, her maddede savunabildiği bütün seçenekleri bildirmesini iste. Ardından:

- `python3 scripts/tymm_kod_denetle.py <anahtar> --veri references/veri` 0 hata.
- Öğrenci kâğıdında çıktı kodu, güçlük ya da hata adı yok.

İki kapıdan geçmemiş bir testi teslim etmek kritik hatadır.

## Adım 8 — Kapanış

Teslimde: madde sayısı, çıktı dağılımı, güçlük dağılımı. En fazla iki somut seçenek: "Sonuçları girerseniz hata analizini çıkarayım mı?" (maarif-hata-analizi) ya da "En zor beş madde için ikiz soru seti hazırlayayım mı?" (maarif-benzer-soru).

## Denetim listesi

- [ ] Her madde bir çıktıya ve bileşene bağlı; sınır aşılmamış
- [ ] Her çeldirici adı konmuş bir hatadan hesaplandı
- [ ] Tek savunulabilir cevap (Kapı A) ve ulaşılabilir çeldirici (Kapı B) her maddede
- [ ] Cevap dağılımı dengeli; görselli madde en az yarısı
- [ ] Kod denetimi 0 hata
