# DNAMATHOS üretim hattı (2.0)

1. **Gövde:** `scripts/dna.py` fonksiyonlarıyla slaytları kur (her slayt `<section class="s …" id="…">`). Sayılar ve cevaplar içerik betiğinde kodla hesaplanıp assert ile denetlenir.
2. **PDF:** `python3 scripts/slayt_uret.py govde.html cikti.pdf --katex <katex/dist> --goruntu <klasör> --baslik "<başlık>"`. Betik yazı tiplerini `assets/fontlar/` klasöründen yükler, KaTeX'i işler, `assets/tasma-denetimi.js` ile denetler (slayt dışına taşma, gövde < 17 px, etiket < 11 px, soru metninin çözüm alanına binmesi, çözüm alanı < 150 px), 297 × 167 mm PDF ve slayt görüntüleri üretir. Sorun varsa 1 ile çıkar.
3. **Bağlantı ve sayfa:** `python3 scripts/pdf_denetle.py cikti.pdf --sayfa <N> --sira cikti_sira.json --baslik "<başlık>"` (önceki/sonraki düğmeli eski düzende `--gezinme` de ver). Dosyalar arası bağlantılar `https://dnamathos.invalid/goto/<dosya>` ile yazılıp pypdf ile `/GoToR` yapılır; PDF'ler aynı klasörde durmalıdır. Betik desen dolgusunu da arar: CSS gradient ve yinelenen arka plan PDF'e desen olarak geçer ve bazı okuyucularda (telefon ve tablet görüntüleyicileri) renkli kutu olarak görünür. Çizgileri kenarlıkla, noktalı zemini tek parça SVG ile, vurguyu iç gölgeyle çiz; "Desen dolgusu: yok" görmeden teslim etme.
4. **Gözle kontrol:** slayt görüntülerinden temas tablosu; kapak, bir konu kartı, bir soru ve bir kavrama testi slaytı tam boyutta görüntülenir.

KaTeX notları: matematikte `<` yerine `\lt`; `.katex{white-space:nowrap}`; kesirli çok satırlı ifadeler `aligned` ile; `.fbox` adlı sınıf kullanılmaz.
