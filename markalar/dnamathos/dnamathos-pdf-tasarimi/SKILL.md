---
name: dnamathos-pdf-tasarimi
description: DNAMATHOS markasının 16:9 ekran PDF tasarım dili ve üretim hattıdır; konu özeti slaytlarını, yazılı kâğıtlarını, cevap anahtarlarını ve çalışma PDF'lerini lacivert üst şerit, menü ve iki panelli slayt düzeniyle HTML, KaTeX ve Playwright üzerinden üretir; taşma, bağlantı ve sayfa denetimini betikle yapar. Bir Maarif skill'i (maarif-konu-ozeti, maarif-ortak-yazili, maarif-beceri-temelli-test, maarif-benzer-soru) DNAMATHOS çıktısı ürettiğinde ya da kullanıcı DNAMATHOS tasarımı, DNAMATHOS PDF'i, bu PDF'in düğmeleri, slayt düzeni veya taşma sorunu dediğinde kullan. İçeriğin pedagojisi için değil (o ilgili Maarif skill'indedir), Instagram görseli için değil (dnamathos-instagram-karusel), Word ya da PowerPoint dosyası için değil (docx, pptx).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: Python 3, Playwright (Chromium), KaTeX (npm install katex), pypdf, PyMuPDF; Inter, Lora ve DejaVu Sans yazı tipleri.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  marka: DNAMATHOS
  onceki_ad: maarif-matematik-icerik 7. bölüm ve maarif-konu-ozeti 8. bölüm
  kanit: 6., 9. ve 10. sınıf yazılı ve konu özeti PDF'lerinde kullanıldı (2025-2026)
---

# DNAMATHOS PDF tasarımı

Bu skill içerik üretmez; içeriği üreten Maarif skill'inin verdiğini DNAMATHOS görünümüne ve dosyasına dönüştürür. Pedagojik kurallar (soru dili, sızıntı, güçlük) içerik skill'inde kalır; burada yalnız görünüm, üretim ve dosya denetimi vardır.

## 1. Tasarım dilini oku

- `references/tasarim-dili.md`: sayfa (297 × 167 mm), renkler, yazı tipleri, üst şerit, soru slaytı, diğer slaytlar, şekil, soru görseli ve tablo kuralları. Her çıktının rengi belge boyunca aynı kalır.
- Konu özeti üretiliyorsa ayrıca `references/konu-ozeti-tasarimi.md` (konu kartı, tüyo kutusu, ödev kartı, öğretmen PDF'i düğmeleri).

## 2. Üret

Üretim hattı `references/uretim-hatti.md` dosyasındadır. Hazır parçalar:

- `assets/dnamathos-slayt.css`: konu özeti ve yazılı slaytlarının sınanmış stil sayfası (sınıf adları: `.slide`, `.band`, `.left`, `.kleft`, `.kright`, `.qbody`, `.sol`, `.kural`, `.kex`, `.write` …). `.fbox` adlı sınıf kullanılmaz (KaTeX `\boxed` ile çakışır).
- `assets/tasma-denetimi.js`: KaTeX'i işleyip her slaytta taşma, kart dışına çıkma ve küçük şekil sorunlarını listeleyen denetim.
- `scripts/slayt_uret.py govde.html cikti.pdf --katex <katex/dist> --goruntu <klasör>`: gövdeyi sarar, denetimi çalıştırır, PDF ve slayt görüntülerini üretir. Taşma varsa 1 ile çıkar; metni kısalt ya da şekli küçült, yeniden üret.

Slayt sırası içerik skill'inin akış listesinden üretilir; her slaytın önceki ve sonraki düğmesi bu listeden hesaplanır. Dosyalar arası düğmeler `https://dnamathos.invalid/goto/<dosya>` ile yazılır ve üretimden sonra pypdf ile `/GoToR` bağlantısına çevrilir; bunun için PDF'ler aynı klasörde durmalıdır (kullanıcıya söylenir).

## 3. Denetle (dosya üretildikten sonra)

1. `python3 scripts/pdf_denetle.py cikti.pdf --sayfa <akış listesindeki slayt sayısı> --baslik "<başlık>"`: sayfa sayısı, iç ve dosyalar arası bağlantı hedefleri (hatalı 0), üst veri.
2. Slayt görüntülerinden temas tablosu (contact sheet) yap ve gözle bak; ayrıca kapak, bir soru, bir cevap anahtarı ve son sayfayı PyMuPDF ile görüntüle (`references/ortak/guvence/pdf-ile-calisma.md`).
3. Öğrenci PDF'inde cevap sızıntısı içerik skill'inin `sizinti_ara.py` adımıyla denetlenir.

## 4. Dosya adları

`DNAMATHOS_<sınıf>_<iş>_<kapsam>.pdf` (ör. `DNAMATHOS_9_2Yazili_Ders1-16.pdf`) ve öğretmen sürümü `…_Ogretmen.pdf`; yazılıda `…_Kagit1.pdf` ve `…_Cevap_Anahtari.pdf`. Yalnız ASCII harf, rakam, alt çizgi ve tire.

## Denetim listesi

- [ ] Taşma 0 (betik çıkış kodu 0)
- [ ] Sayfa sayısı akış listesiyle aynı; hatalı bağlantı 0
- [ ] Temas tablosu ve dört örnek sayfa gözle görüldü
- [ ] Dosya adları kurala uygun; birbirine bağlanan PDF'ler aynı klasörde
