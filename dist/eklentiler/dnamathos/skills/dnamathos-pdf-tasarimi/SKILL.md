---
name: dnamathos-pdf-tasarimi
description: DNAMATHOS markasının 16:9 ekran PDF tasarım dili ve üretim hattıdır; konu özeti slaytlarını, yazılı kâğıtlarını, cevap anahtarlarını ve çalışma PDF'lerini safran ve lacivert renk blokları, DNA sarmalı imzası, Fraunces, Atkinson Hyperlegible Next, Caveat ve IBM Plex Mono yazı tipleriyle HTML, KaTeX ve Playwright üzerinden üretir; taşma, bağlantı ve sayfa denetimini betikle yapar. Bir Maarif skill'i (maarif-konu-ozeti, maarif-ortak-yazili, maarif-beceri-temelli-test, maarif-benzer-soru) DNAMATHOS çıktısı ürettiğinde ya da kullanıcı DNAMATHOS tasarımı, DNAMATHOS PDF'i, bu PDF'in düğmeleri, slayt düzeni veya taşma sorunu dediğinde kullan. İçeriğin pedagojisi için değil (o ilgili Maarif skill'indedir), Instagram görseli için değil (dnamathos-instagram-karusel), Word ya da PowerPoint dosyası için değil (docx, pptx).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: Python 3, Playwright (Chromium), KaTeX (npm install katex), pypdf, PyMuPDF. Yazı tipleri skill'in içinde (assets/fontlar).
metadata:
  surum: "2.0.0"
  yazar: DNAMATHOS
  marka: DNAMATHOS
  onceki_ad: maarif-matematik-icerik 7. bölüm ve maarif-konu-ozeti 8. bölüm
  kanit: 6., 9. ve 10. sınıf yazılı ve konu özeti PDF'lerinde kullanıldı (2025-2026)
---

# DNAMATHOS PDF tasarımı

Bu skill içerik üretmez; içeriği üreten Maarif skill'inin verdiğini DNAMATHOS görünümüne ve dosyasına dönüştürür. Pedagojik kurallar (soru dili, sızıntı, güçlük) içerik skill'inde kalır; burada yalnız görünüm, üretim ve dosya denetimi vardır.

## 1. Tasarım dilini oku

- `references/tasarim-dili.md`: DNAMATHOS 2.0 — renkler ve karşıtlık kuralları, yazı tipi rolleri (Fraunces başlık, Atkinson Hyperlegible Next gövde, Inter rakam, Caveat el yazısı not, IBM Plex Mono etiket), marka imzaları (DNA sarmalı, fosforlu kalem vurgusu, çerçeveli haplar), bileşenler ve soru ile tüyo kuralları.
- Konu özeti üretiliyorsa ayrıca `references/konu-ozeti-tasarimi.md`.

## 2. Üret

Üretim hattı `references/uretim-hatti.md` dosyasındadır. Hazır parçalar:

- `scripts/dna.py`: slayt bileşenleri (`kapak`, `serit`, `tur_soru`, `konu`, `soru`, `kaydet`, `kavrama`, `odev`, `sayi_dogrusu`, `tablo` …). İçerik betiği gövdeyi bu fonksiyonlarla kurar.
- `assets/dnamathos.css` ve `assets/fontlar/`: stil dosyası ve gömülü yazı tipleri (SIL Açık Font Lisansı).
- `scripts/slayt_uret.py govde.html cikti.pdf --katex <katex/dist> --goruntu <klasör>`: yazı tiplerini yükler, denetimi (`assets/tasma-denetimi.js`) çalıştırır, PDF ve slayt görüntülerini üretir. Sorun varsa 1 ile çıkar; metni kısalt, `coz_ust` değerini ayarla ya da şekli küçült ve yeniden üret.

Tam örnek: `ornekler/6-sinif-ortak-kat/ders_uret.py` (depoda; 25 slaytlık ders).

## 3. Denetle (dosya üretildikten sonra)

1. `python3 scripts/pdf_denetle.py cikti.pdf --sayfa <slayt sayısı> --sira cikti_sira.json --baslik "<başlık>"`: sayfa sayısı, bağlantı hedefleri (hatalı 0), üst veri.
2. Slayt görüntülerinden temas tablosu yap ve gözle bak; kapak, bir konu kartı, bir soru ve bir kavrama testi slaytını tam boyutta görüntüle (`references/ortak/guvence/pdf-ile-calisma.md`).
3. Öğrenci PDF'inde cevap sızıntısı içerik skill'inin `sizinti_ara.py` adımıyla denetlenir; şekillerde cevabı gösteren işaret (çevreleme, boyama) yok.

## 4. Dosya adları

`DNAMATHOS_<sınıf>_<iş>_<kapsam>.pdf` (ör. `DNAMATHOS_9_2Yazili_Ders1-16.pdf`) ve öğretmen sürümü `…_Ogretmen.pdf`; yazılıda `…_Kagit1.pdf` ve `…_Cevap_Anahtari.pdf`. Yalnız ASCII harf, rakam, alt çizgi ve tire.

## Denetim listesi

- [ ] Denetim 0 sorun (taşma yok, gövde ≥ 17 px, çözüm alanı ≥ 150 px)
- [ ] Safran açık zeminde yazı rengi olarak kullanılmadı; şekiller cevabı göstermiyor
- [ ] Sayfa sayısı akış listesiyle aynı; hatalı bağlantı 0
- [ ] Temas tablosu ve dört örnek sayfa gözle görüldü
- [ ] Dosya adları kurala uygun; birbirine bağlanan PDF'ler aynı klasörde
