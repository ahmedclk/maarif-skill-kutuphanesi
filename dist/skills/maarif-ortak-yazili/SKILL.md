---
name: maarif-ortak-yazili
description: MEB ortak yazılı (ortak sınav) senaryosuna birebir uyan, açık uçlu yazılı sınav kâğıtları ve cevap anahtarları hazırlar; çıktıları TYMM sayfasından doğrular, süreç bileşenlerini kâğıt setinin toplamında kapsar, MEB soru üslubunu ve görsel ölçütünü uygular, güçlüğü Z Y C kuralıyla belirler ve puanlama anahtarı ile kapsama tablosu verir. Netleştirici soru sormadan önce yükle. Tetikleyiciler - 1. dönem 2. yazılı hazırla, ortak sınav senaryosuna göre soru yaz, açık uçlu yazılı, yazılı provası, kâğıt seti ve cevap anahtarı, bu senaryoya göre 4 kâğıt. Çoktan seçmeli LGS tarzı test için değil (maarif-beceri-temelli-test), verilen bir sorunun ikizini üretmek için değil (maarif-benzer-soru), 1–3 maddelik anlama kontrolü için değil (maarif-anlama-kontrolu), performans görevi için değil (maarif-performans-gorevi).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: TYMM sayfaları için web erişimi; Python 3 (puan ve güçlük denetimi). PDF üretimi için bir marka skill'i (DNAMATHOS için dnamathos-pdf-tasarimi) ya da pdf skill'i.
metadata:
  surum: "2.0.0"
  yazar: DNAMATHOS
  omurga: TYMM öğrenme çıktıları ve süreç bileşenleri; MEB ortak yazılı senaryoları ve Yazılıya Hazırlanıyorum örnekleri
  dersler: matematik (tam); diğerleri şablonla
  onceki_ad: maarif-matematik-icerik 1.x (yazılı kısmı; tasarım dnamathos-pdf-tasarimi skill'ine taşındı)
  kanit: 6., 9. ve 10. sınıf yazılı setlerinde kullanıldı (2025-2026)
---

# Maarif ortak yazılı

Amaç: Öğretmenin verdiği senaryoya birebir uyan, deneyimli bir öğretmenin elinden çıkmış gibi duran ve MEB örnek yazılılarına benzeyen sınav kâğıtları. Kapsama tek kâğıtta değil **kâğıt setinin bütününde** sağlanır; her kâğıt yine tek başına tam ve dengeli bir sınavdır. Senaryo, çıktı listesi, soru sayısı ve puan dağılımı her çalışmada öğretmenden alınır; bu dosyada tutulmaz.

Bütün içerikte öğretmen notları ve "Sık yapılan hata" kutuları `references/ortak/uslup/ogretmen-uslubu.md` üslubundadır; sınav kâğıdının soru dili ise MEB üslubundadır (ders dosyası). Dil: `references/ortak/uslup/turkce-yazim.md`.

## Adım 0 — Yönlendirme (sessiz)

1. **Omurga:** `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md` ve `references/ortak/maarif/meb-olcme-mevzuati.md` (MEB yazılı sınav kuralları; bu skill'in bağlayıcı sınırı).
2. **Ders:** `references/dersler/<ders>.md` dosyasını şimdi oku (matematik → `references/dersler/matematik.md`). Ders dosyası, soru yazımının bütün kurallarını hangi ortak dosyadan alacağını söyler. Okumadan soru yazmak kritik hatadır. Ders dosyası yoksa `references/ortak/dersler/_sablon.md` ile çalış ve cevap anahtarına not ekle.
3. Aynı oturumda `cikti.json` varsa onu kullan.

## Adım 1 — Netleştirme (en fazla bir soru)

Senaryo tablosu (çıktı başına soru sayısı) yoksa yalnız onu iste; çıktı listesi senaryodan çıkar. Kâğıt sayısını sorma, Adım 3'te sen belirlersin. Senaryo ikincil bir kaynaktan geliyorsa bunu kapsama planında belirt.

## Adım 2 — Programa dayandır ve bileşenleri eşle

Her çıktı için tema sayfasından birebir: çıktı, bileşenler, İçerik Çerçevesi sınırları, gösterimler, Öğrenme-Öğretme Uygulamalarındaki sınırlamalar, temanın kod listeleri. Öğretmenin verdiği metinle fark varsa bildir ve sitedeki güncel metni esas al. Her bileşeni beceri basamağına bağla ve "yazılıda ölçülür" ya da "performansa bırakılır" diye işaretle (ders dosyasındaki eşleme).

## Adım 3 — Kâğıt seti ve kapsama planı (soru yazmadan önce)

Kâğıt sayısı kuralı ders dosyasındadır (matematikte k değerleri ve ⌈bileşen ÷ k⌉ formülü). Planı öğretmene tablo olarak göster: çıktı · ölçülen bileşen sayısı · k · gereken soru · senaryodaki soru · kâğıt; sınırlayan çıktıyı belirt. Öğretmen ortamdaysa ve set 3 kâğıttan büyükse planı onaylat; değilse plana göre devam et ve teslimde yaz.

## Adım 4 — Soruları yaz

**Mevzuat sınırı (`references/ortak/maarif/meb-olcme-mevzuati.md`):** sorular açık uçludur, gerekirse kısa cevaplı madde eklenir ama kâğıt yalnız kısa cevaplı olamaz (MEV-10, MEV-11); çoktan seçmeli, doğru-yanlış ve eşleştirme kullanılmaz (MEV-12); her madde etiketindeki bileşenin bilişsel düzeyindedir (MEV-13); soru sayısı seçilen senaryoya uyar (MEV-14); kâğıt bir ders saatinde çözülebilir (MEV-16) ve her maddenin altında yeterli cevap alanı vardır (MEV-17); kâğıtta çıktı ifadesi yazılmaz (MEV-18).

Ders dosyasının gösterdiği ortak dosyalarla: soru yazım ölçütü, yapı çeşitliliği, kalıp kataloğu, kademe üslubu, ölçülenin soru üzerinde gösterilmesi ve görsel ölçütü. Telif: MEB ve yayınevi soruları model alınır, birebir kullanılmaz (`references/ortak/guvence/kvkk-ve-telif.md`). Gerçek veri kullanılıyorsa kaynağı açılıp doğrulanır.

## Adım 5 — Cevap anahtarı, güçlük ve puan

Sıra değişmez: önce MEB tarzında adım puanlı cevap anahtarı, sonra güçlük anahtardan okunur, en son puan verilir. Her alt madde için Z · Y · C değerlerini yaz ve `maddeler.json` dosyasına kaydet; ardından:

`python3 scripts/guclugu_hesapla.py maddeler.json --kademe ortaokul|lise --yazili`

`--yazili` ayrıca mevzuatı denetler: her maddenin `tur` alanı (`acik`, `kisa`) ve tahmini `sure_dk` değeri; çoktan seçmeli ya da eşleştirme maddesi, yalnız kısa cevaplı kâğıt ve 40 dakikayı aşan kâğıt ihlaldir. Puan 100 üzerindendir ve yanlış cevap doğruyu götürmez (MEV-19).

İhlal 0 olana kadar puanı ya da soruyu düzelt. Adım puanlarının toplamı madde puanına eşit olmalı (içerik dosyasında assert).

## Adım 6 — Robotiklik denetimi (üretimden önce)

Ders dosyasının gösterdiği robotiklik ve güçlük denetim tablosunu çıkar ve sorun varsa düzelt. Mümkünse bu denetimi soruları görmemiş ayrı bir ajana yaptır.

## Adım 7 — Üretim

Sınav kâğıtları ve cevap anahtarları ayrı dosyalardır. Marka skill'i yüklüyse (DNAMATHOS: `dnamathos-pdf-tasarimi`) onun tasarım dili ve üretim hattı; yoksa pdf skill'i ile sade A4 ya da 16:9 PDF. Cevap anahtarında her maddenin altında, puanlanan kâğıtta öğrenciye yazılacak bir **öğretmen notu** önerisi bulunur (eksik ya da yanlış öğrenmeye yönelik, MEV-30). Cevap anahtarının sonunda puanlama tablosu ve kapsama tablosu (satırlar bileşenler, sütunlar kâğıtlar, hücrelerde "K2 · 3.1").

## Adım 8 — Doğrulama (dosyalar üretildikten sonra)

1. `references/ortak/guvence/dogrulama-kapisi.md` dosyasını şimdi oku; Kapı A'yı (açık uçlu biçimi) ve Kapı C'yi her maddeye uygula. Alt ajan varsa yalnız sınav kâğıdını ona çözdür; bulduğu her alternatif doğru cevap cevap anahtarına eklenir ya da kök düzeltilir.
2. `python3 scripts/tymm_kod_denetle.py <kâğıt PDF'leri> --veri references/veri` 0 hata.
3. `python3 scripts/sizinti_ara.py <kâğıt PDF> cevaplar.json` 0.
4. Kapsama: yazılıda ölçülen her bileşen setin toplamında en az bir kez (kodla say). Senaryo uyumu: her kâğıtta çıktı başına soru sayısı senaryoyla aynı (assert).
5. PDF denetimi: `references/ortak/guvence/pdf-ile-calisma.md` "Çıktı PDF'ini denetleme".

## Adım 9 — Kapanış

Teslimde: kâğıt sayısı ve gerekçesi (sınırlayan çıktı), setin güçlük payları, TYMM ile öğretmen metni arasındaki farklar, yazılı dışı bırakılan bileşenler. En fazla iki somut seçenek: "Yazılı dışı kalan bileşenler için bir performans görevi hazırlayayım mı?" (maarif-performans-gorevi) ya da "Kâğıt 1'in her sorusu için bir ikiz soru seti çıkarayım mı?" (maarif-benzer-soru).

## Denetim listesi

- [ ] Çıktı ve bileşenler sayfadan; yazılı dışı bileşenler işaretli
- [ ] Kapsama planı gösterildi; her kâğıt senaryoya birebir uyuyor
- [ ] Robotiklik tablosu temiz; görsel sayısı ve çeşitliliği eşikte
- [ ] Mevzuat: açık uçlu esas, yalnız kısa cevaplı değil, çoktan seçmeli yok, bilişsel düzey uygun, 40 dakikaya sığıyor, cevap alanı yeterli
- [ ] Güçlük betiği (--yazili) 0 ihlal; adım puanları toplamı tutuyor
- [ ] Doğrulama kapısı geçti; kod denetimi ve sızıntı 0
