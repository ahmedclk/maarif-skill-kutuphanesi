# Maarif Skill Kütüphanesi

Türkiye Yüzyılı Maarif Modeli'ne (TYMM) dayanan, öğretmenlerin Claude ile kullanacağı skill'ler. Her skill bir öğretmen işini (ders planı, ortak yazılı, anlama kontrolü, performans görevi, hata analizi…) baştan sona yapar ve ürettiği her şeyi **bir öğrenme çıktısına ve onun süreç bileşenlerine** bağlar.

> **MEB ölçme kuralları:** Sorular Millî Eğitim Bakanlığı Ölçme ve Değerlendirme Yönetmeliği, Yazılı ve Uygulamalı Sınavlar Yönergesi ve Kılavuzuna uyar: okul yazılısı açık uçludur, 100 puan üzerindendir, bir ders saatine sığar; kısa süreli sınav notsuzdur; ilkokulda sınav yapılmaz. Ayrıntı: [ortak/maarif/meb-olcme-mevzuati.md](ortak/maarif/meb-olcme-mevzuati.md).

> **Omurga:** Bu kütüphanede hiçbir ürün programdan bağımsız değildir. Çıktı metni, bileşenler, içerik çerçevesi sınırları ve programlar arası bileşenler (eğilim, SDB, değer, okuryazarlık) her çalışmada TYMM sayfasından alınır; bellekten yazılmaz, uydurulmaz. Ayrıntı: [ortak/maarif/cerceve.md](ortak/maarif/cerceve.md).

## Ne alırsınız?

| İş | Skill | Öğretmenin eline geçen |
| --- | --- | --- |
| Programı okumak | `maarif-cikti-cozumleme` | Çıktı kartı: birebir çıktı, bileşen–beceri basamağı eşlemesi, sınırlar, ölçülebilirlik |
| Haftalara dağıtmak | `maarif-ders-takvimi` | Sınava kalan haftalara göre ders takvimi ve ödev sayfaları |
| Ders planlamak | `maarif-ders-plani` | Ders planı + öğrenci çalışma kâğıdı + gözlem formu |
| Derse hazırlanmak | `maarif-derse-hazirlik` | Kilit görev üzerine birlikte düşünme ve 200–300 sözcüklük hazırlık notu |
| Farklılaştırmak | `maarif-farklilastirma` | Destekleme, temel, zenginleştirme için üç kâğıt ve öğretmen planı |
| Anlamayı yoklamak | `maarif-anlama-kontrolu` | 1–3 maddelik kontrol ve cevapları okuma kılavuzu |
| Haftalık kavrama | `maarif-kavrama-testi` | 4–5 soruluk notsuz test, öğrenci başına karar, yalnız takılan bileşenlere hedefli ödev |
| Ders başı tekrar | `maarif-hizli-tekrar` | 5 dakikalık karışık soru turu ve karşı örnekle sınanmış haftanın sloganı |
| Konu özeti | `maarif-konu-ozeti` | Haftalık ders slaytları, yazılı tüyoları, ödev kartı, öğretmen dosyası |
| Ortak yazılı | `maarif-ortak-yazili` | Senaryoya uyan kâğıt seti, cevap anahtarı, kapsama tablosu |
| Beceri temelli test | `maarif-beceri-temelli-test` | LGS tarzı test ve çeldirici açıklamalı anahtar |
| Performans görevi | `maarif-performans-gorevi` | Görev kâğıdı, dereceli puanlama anahtarı, gözlem ve öz değerlendirme formları |
| İkiz soru | `maarif-benzer-soru` | Aynı bileşeni ölçen özgün benzer sorular ve çözümler |
| Hata analizi | `maarif-hata-analizi` | Koç raporu, telafi çalışma sayfası, tekrar takvimi, veli özeti |
| Anlatım videosu | `maarif-anlatim-videosu` | Sahne planı, seslendirme metni, Remotion kodu |
| DNAMATHOS PDF | `dnamathos-pdf-tasarimi` | 16:9 marka PDF'i, taşma ve bağlantı denetimi |
| DNAMATHOS Instagram | `dnamathos-instagram-karusel` | Üçlü ızgara satırı: karusel, rehberlik, gerçek hayat |

**Öğretmen kılavuzu:** [docs/kilavuz.md](docs/kilavuz.md) · **Tanıtım sayfası:** `docs/index.html` (GitHub Pages) · **Instagram karuselleri:** [tanitim/instagram/](tanitim/instagram/)

Tam liste ve açıklamalar: [KATALOG.md](KATALOG.md). Eski skill adlarının karşılıkları: [ESKI-YENI.md](ESKI-YENI.md).

## Nasıl kullanılır? (üç düzey)

1. **Hazır istem:** [istemler/](istemler/) klasöründen bir istemi kopyalayıp Claude'a yapıştırın. Kurulum gerekmez.
2. **Skill yükleme:** `dist/zip/<skill>.zip` dosyasını Claude ayarlarındaki skill bölümünden yükleyin. Claude, isteğiniz skill'in açıklamasına uyduğunda onu kendiliğinden kullanır.
3. **Paket (Claude Code eklentisi):** depoyu pazar yeri olarak ekleyip bir paketi kurun (`maarif-ogretmen-temel`, `maarif-olcme-degerlendirme`, `maarif-icerik-uretimi`, `dnamathos`, `maarif-tam`).

Ayrıntı ve iş akışı tarifleri: [docs/kullanim.md](docs/kullanim.md), [docs/is-akislari.md](docs/is-akislari.md).

## Depo düzeni

```
ortak/            Bütün skill'lerin paylaştığı başvurular (tek kaynak)
  maarif/         Model bileşenleri, kodlar, TYMM erişimi
  uslup/          Öğretmen üslubu, önyargısız dil, Türkçe yazım, ilerleme ve kapanış
  guvence/        Doğrulama kapısı, KVKK ve telif, PDF ile çalışma
  dersler/        Ders bazlı ortak bilgi (matematik) ve yeni ders şablonu
  betikler/       Deterministik denetimler (kod, güçlük, cevap dağılımı, sızıntı)
veri/tymm/        Makinece okunur program verisi (kodlar, 6. ve 9. sınıf matematik)
skills/           Maarif skill'leri (her biri SKILL.md + references/ + gerekirse scripts/)
markalar/         Marka skill'leri (DNAMATHOS)
paketler/         Paket tanımları
testler/          Tetikleme testleri, ölçüt tabloları, yargıç istemi, protokol
istemler/         Kopyala-yapıştır istemler
docs/             Kullanım, iş akışları, tasarım ilkeleri, yeni ders ekleme
araclar/          denetle.py · paketle.py · katalog.py
dist/             Üretilen dağıtım (paketle.py çıktısı)
```

Her skill aynı iskeleti izler (Adım 0 yönlendirme → netleştirme → programa dayandırma → üretim → doğrulama kapısı → kapanış) ve her skill'in kendi `references/dersler/<ders>.md` dosyası vardır. Ayrıntı: [docs/tasarim-ilkeleri.md](docs/tasarim-ilkeleri.md).

## Geliştirme

```
python3 araclar/denetle.py      # skill rehberi ve kütüphane kuralları
python3 araclar/paketle.py      # dist/ üretir (ortak başvurular her skill'e kopyalanır)
python3 araclar/denetle.py --dagitim
python3 araclar/katalog.py      # KATALOG.md ve katalog.json
python3 araclar/kilavuz_uret.py --depo KULLANICI/DEPO   # docs/kilavuz.md ve docs/index.html
python3 tanitim/instagram/karusel_uret.py              # Instagram karuselleri
```

**Tanıtım sayfasını yayımlamak:** GitHub'da depo ayarlarında *Pages → Deploy from a branch → main / docs* seçin. Sayfa `https://KULLANICI.github.io/DEPO/` adresinde açılır.

Katkı kuralları: [KATKI.md](KATKI.md). Lisans: [LISANS.md](LISANS.md).

## Kaynaklar ve teşekkür

- [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) (Apache-2.0): ders planı, farklılaştırma, derse hazırlık ve anlama kontrolü skill'leri ile doğrulama kapısı buradan uyarlandı. Ayrıntı: [NOTICE](NOTICE).
- Anthropic, *The Complete Guide to Building Skills for Claude*: adlandırma, açıklama, aşamalı açılım ve test kuralları.
- [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) (CC BY-SA 4.0): katalog ve "kanıt temelli skill" düşüncesi için esin kaynağı; içerik kopyalanmadı.
- HKUDS/DeepTutor (Apache-2.0): ikiz soru, hata analizi ve video skill'lerinin ilk sürümleri.
- MEB, TYMM öğretim programları: https://tymm.meb.gov.tr
- MEB ODSGM, Mevzuat Kitapçığı (2024): Ölçme ve Değerlendirme Yönetmeliği, Yazılı ve Uygulamalı Sınavlar Yönergesi ve Kılavuzu.
