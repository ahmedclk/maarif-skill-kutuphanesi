# DNAMATHOS üretim hattı

- Python ile HTML üret, KaTeX auto-render (yerel node_modules/katex), Playwright Chromium ile `page.pdf(width="297mm", height="167mm", print_background=True, prefer_css_page_size=True)`.
- İç bağlantılar `href="#id"`; dosyalar arası bağlantılar `https://dnamathos.invalid/goto/<dosya>` ile yazılıp pypdf ile `/GoToR` (`/F dosya`, `/D [0 /Fit]`) yapılır. Her bağlantının hedefini ve her slayta ulaşılabildiğini denetle. Dosyalar arası butonlar için PDF'lerin aynı klasörde olması gerekir; bunu kullanıcıya söyle.
- JS ile taşma denetimi: son öğenin alt sınırı kabın alt sınırını geçmesin; `.katex` içini sınır denetiminden çıkar; yatay taşmayı ayrıca denetle. Şekil yüksekliği en az 34 mm; sığmıyorsa metni kısalt.
- Matematikte `<` yerine `\lt` yaz. `.fbox` adlı CSS sınıfı kullanma (KaTeX `\boxed` ile çakışır). `.katex{white-space:nowrap}` ile formül bölünmesini engelle. Kesirli çok satırlı ifadeler `\begin{aligned}…\\[5pt]…\end{aligned}` ile; kesirsiz uzun eşitlikleri ayrı `$…$` satırlarına böl.
- Her slaytın ekran görüntüsünü al, temas tablosu (contact sheet) yap ve gözle kontrol et.
- Sınavlar ve cevap anahtarları ayrı PDF'ler olarak teslim edilir.
