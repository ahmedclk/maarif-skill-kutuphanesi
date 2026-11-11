# Tasarım ilkeleri

## 1. Omurga: her şey bir çıktıya bağlıdır

Kütüphanenin bütün skill'leri aynı soruyla başlar: *Bu ürün hangi öğrenme çıktısının hangi süreç bileşenine hizmet ediyor?* Cevap TYMM sayfasından gelir. Bu yüzden her skill'in Adım 0'ı `ortak/maarif/cerceve.md` ve `ortak/maarif/tymm-erisim.md` dosyalarını okutur ve her skill'in doğrulama kapısında "Maarif bağı" (Kapı C) vardır.

## 2. Ortak iskelet

| Adım | İçerik | Kaynak ilke |
| --- | --- | --- |
| 0 Yönlendirme (sessiz) | Omurga + ders dosyası okunur; ders dosyası yoksa şablonla çalışılır ve not düşülür | k12 "Route silently", rehber "progressive disclosure" |
| 1 Netleştirme | En çok bir soru; skill yüklendikten sonra; gerisi varsayılan | k12 "Load BEFORE asking" |
| 2 Programa dayandırma | Çıktı, bileşen, sınır, programlar arası bileşenler sayfadan; erişim yoksa not, uydurma yok | k12 "works without connector" |
| 3 (gerekirse) Odak onayı | Anlama kontrolünde bileşen öğretmene onaylatılır | k12 CFU Step 3 |
| 4 Üretim | Tek ortak kaynak (JSON) → belgeler; ortak içerik bir kez yazılır | k12 lesson.json |
| 5 Doğrulama kapısı | Dosyalar yazıldıktan **sonra** okunur; Kapı A tek cevap, B çeldirici, C Maarif bağı; betikler | k12 verification gate, rehber "deterministic scripts" |
| 6 Kapanış | En çok iki somut seçenek; iç düzen anlatılmaz | k12 Close |

## 3. Aşamalı açılım (üç katman)

1. **Üst bilgi** (her zaman yüklü): ad ve açıklama; Claude skill'i bununla seçer. Açıklama: ne yapar + ne zaman (Türkçe tetikleyiciler) + ne için değil (kardeş skill adıyla).
2. **SKILL.md gövdesi** (skill seçilince): adımlar ve değişmez kurallar; ayrıntı yok.
3. **references/ ve scripts/** (gerektiğinde): ders dosyası, ortak başvurular, şemalar, betikler.

## 4. Ders bazlı başvuru dosyaları

Her skill'in `references/dersler/<ders>.md` dosyası vardır ve skill'in genel adımlarını o dersin pedagojisiyle doldurur. Aynı dersin bilgisi birden çok skill'de gerekiyorsa `ortak/dersler/<ders>/` altına konur; skill'in ders dosyası ona yönlendirir. Yeni ders: `docs/yeni-ders-ekleme.md`.

## 5. Tek kaynak, dağıtımda kopya

Kaynak depoda ortak dosyalar bir kez yazılır. `araclar/paketle.py`, her skill'in andığı ortak dosyaları ve betikleri o skill'in klasörüne kopyalar; böylece claude.ai'ye tek başına yüklenen bir skill de eksiksiz çalışır. Ortak dosya değişince bütün skill'ler yeniden paketlenir.

## 6. Adlandırma

- Maarif skill'leri `maarif-` ile, marka skill'leri marka adıyla başlar (`dnamathos-`).
- Ad, öğretmenin işini söyler: `maarif-ortak-yazili`, `maarif-anlama-kontrolu`. Yöntem ya da araç adı (`remotion-…`) ve İngilizce terim (`cfu`, `rubric`) kullanılmaz.
- ASCII, kebab-case; Türkçe harfler sadeleştirilir (ç→c, ğ→g, ı→i, ö→o, ş→s, ü→u).
- Bir ad bir iş: aynı işi iki skill yapmaz; sınır açıklamadaki "… için değil" cümlesiyle çizilir.

## 7. Marka ile pedagoji ayrıdır

Pedagojik kurallar Maarif skill'lerinde, görünüm ve üretim marka skill'inde durur. Başka bir okul ya da öğretmen kendi marka skill'ini yazarak bütün Maarif skill'lerini kendi tasarımıyla kullanabilir.
