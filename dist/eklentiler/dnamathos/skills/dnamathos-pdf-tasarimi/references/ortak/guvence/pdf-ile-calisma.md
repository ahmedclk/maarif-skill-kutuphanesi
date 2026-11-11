# PDF ile çalışma: kaynak okuma ve çıktı denetimi

Bütün skill'lerde geçerlidir. Kaynak: `maarif-matematik-icerik` 7. bölüm.

Kullanıcı kaynak olarak PDF ya da sayfa görüntüsü verir (MEB ders kitabı, MEB örnek yazılısı, program PDF'i, yayınevi sayfaları); DNAMATHOS çıktısı da PDF'tir. Kütüphaneyi işe göre seç:

| İş | Araç |
| --- | --- |
| Metin, tablo, sayfa yerleşimi, sözcük koordinatı | `pdfplumber` (`page.extract_text()`, `page.extract_tables()`, `page.extract_words()`) |
| Hızlı ham metin, sayfa sayısı, üst veri, bağlantı denetimi, birleştirme, bölme, döndürme, kırpma | `pypdf` |
| Sayfayı görüntüye çevirme (şekil, kesir, üs ve tablo okuma; çıktıyı gözle denetleme) | PyMuPDF: `import pymupdf` (eski adı `fitz`); yüklü değilse `pip install --break-system-packages pymupdf`, o da olmazsa `pdftoppm -r 110` |
| DNAMATHOS slaytı üretme | HTML + KaTeX + Playwright (`dnamathos-pdf-tasarimi` skill'i); reportlab kullanılmaz, çünkü formül dizgisi ve tasarım dili HTML'dedir |

**Kaynak PDF'i okuma**
- Önce sayfa sayısını ve her sayfanın ilk birkaç satırını dök (pypdf); bu dökümden dersin ya da soruların hangi sayfalarda olduğunu bul. Büyük PDF'in tamamını görüntüye çevirme.
- Gerekli sayfaları 110–150 dpi görüntüle ve Read ile gözle oku: `page.get_pixmap(dpi=130).save(...)`. Sık yazılı bir bölge için `clip=pymupdf.Rect(x0, y0, x1, y1)` ile yalnız o bölgeyi yüksek çözünürlükte çıkar.
- Metin çıkarımında kesir, üs ve kök bozulur ("5 2" = 2/5, "2 1/12" = 2^(1/12) olabilir). Kesir, üs, kök ve aralık içeren her ifadeyi sayfa görüntüsünden doğrula; şekil üzerindeki değerleri yalnız görüntüden al.
- Tablolar: önce `extract_tables()`; hücreler kayıyorsa `page.within_bbox((x0, top, x1, bottom))` ile tabloyu kırp ve `{"vertical_strategy": "lines", "horizontal_strategy": "lines", "snap_tolerance": 3, "intersection_tolerance": 15}` ayarlarını dene; sonucu görüntüyle karşılaştır.
- **Taranmış sayfa:** `extract_text()` boş dönüyorsa ya da `(cid:NN)` dizileriyle doluysa sayfa görüntüdür ve OCR yoktur. Sayfayı görüntüye çevirip gözle oku; okunamayan sayı ya da sözcüğü tahminle doldurma. Belirsiz kalan değeri ya kullanıcıya sor ya da teslim mesajında hangi yorumu aldığını yaz.
- Kullanıcının gönderdiği sayfa fotoğraflarını (webp, jpg) PIL ile PNG'ye çevir ve önce küçük resimlerden bir temas tablosu yap; hangi görüntünün hangi sayfa ya da set olduğunu bununla eşle, sonra gereken sayfaları tek tek oku.
- Basılı sayfa numarası PDF sayfa sırasından farklı olabilir; atıflarda basılı numarayı kullan.
- Dışarıdan indirilen PDF'i ayrı ve boş bir klasöre koy; onu okuyan Python betiklerini başka klasörde tut ve `python -I` ile çalıştır.

**Çıktı PDF'ini denetleme (teslimden önce)**
- pypdf ile sayfa sayısı slayt listesindeki sayıya eşit olmalı; her `/Link` açıklamasının hedefi (`/Dest` ya da adlandırılmış hedef) var olmalı; bağlantı sayısı ve hatalı bağlantı sayısı yazdırılır (hedef 0).
- İstenen nicelik korunur: kullanıcı soru sayısı verdiyse (ör. "60 soru", "tek PDF") bunu kodda assert ile denetle ve PDF'ten metin çıkarıp soru numaralarını say. Kapsam, kullanıcıya sormadan küçültülmez.
- PyMuPDF ile kapak, bir soru, bir cevap anahtarı ve son sayfayı görüntüleyip gözle bak; temas tablosu bunun yerine geçmez, onu tamamlar.
- Üst veri: pypdf `add_metadata({"/Title": ..., "/Author": "DNAMATHOS"})`.
- Birden çok PDF'i birleştirmek gerekiyorsa (pypdf `PdfWriter`), adlandırılmış hedefler ve iç bağlantılar kayabilir; mümkünse tek HTML'den tek PDF üret, birleştirdiysen bağlantıları yeniden denetle.
- Bir betik hata verirse stderr'den kök nedeni bul ve yöntemi değiştir; aynı kodu tekrar çalıştırma.
