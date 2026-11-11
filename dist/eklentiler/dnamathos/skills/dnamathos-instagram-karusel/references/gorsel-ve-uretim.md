# Görsel, tasarım dili ve üretim

## Görsel

Görsel süs değil, anlatının taşıyıcısıdır; `references/ortak/dersler/matematik/soru-gorseli.md` ölçütü burada da geçerlidir: görsel bilgi taşır, cevabı erkenden vermez, ölçeğe sadıktır.

- Her adım slaytında mümkünse bir görsel: sayı doğrusu, alan modeli, şekil, tablo, adım adım işlem kutusu, karşılaştırma (doğru / yanlış yan yana).
- Aynı görsel karusel boyunca değişerek ilerleyebilir (ör. aynı kare her slaytta bir parçası boyanarak); bu, kaydırmayı ödüllendirir.
- Doğru / yanlış karşılaştırmasında yeşil ✓ ve kiremit ✗ kullanılır; renk tek başına anlam taşımaz, işaret de bulunur.
- Şekiller matplotlib ya da SVG ile çizilir; etiketler telefonda okunur büyüklükte (en az 36 px).
- Gerçek kişi fotoğrafı, marka logosu ya da başka bir hesabın içeriği kullanılmaz.

## Tasarım dili ve üretim

**Boyut:** 1080 × 1350 px (4:5 dikey), sRGB PNG. İlk slayt bütün karuselin oranını belirler; bütün slaytlar aynı boyutta üretilir. Profil ızgarası kapağı 3:4 kırpar (her yandan yaklaşık 34 px), bu yüzden kapağın kenarlarına önemli öğe konmaz.

**Renkler:** Sabit marka renkleri bütün sınıflarda aynıdır: metin lacivert #14213d, ikincil #4a5570, tek vurgu safran #fca311 (DNAMATHOS tasarım dili 2.0). Zemin ve çizgi renkleri sınıfın paletinden gelir (`profil-izgarasi.md`). Doğru / yanlış kartlarında anlam rengi korunur (yeşil #0b6157 / #e1f3f0, kiremit #b3401a / #fdece6) ve her zaman ✓ / ✗ işaretiyle birlikte kullanılır.

**Zemin:** Kapak ve kapanış sınıfın koyu tonunda, beyaz yazı ve safran vurguyla; içerik slaytları sınıfın açık tonunda, lacivert yazıyla. Konu etiketi hapı ve ilerleme çubuğu sınıfın orta tonunda; formül kutusu kenarı ve çizimlerdeki ana çizgi sınıfın çizgi tonunda. Bir karuselde başka renk ailesi kullanılmaz. Rehberlik gönderisinin zemininde ayrıca sınıf rengine boyanmış bir doğa fotoğrafı bulunur (`profil-izgarasi.md`).

**Yazı (DNAMATHOS 2.0 rolleri):** Başlıklar Fraunces 800 (kapakta 96–120 px, içerikte 64–80 px; ikinci kısım Fraunces italik ve vurgu renginde); gövde Atkinson Hyperlegible Next 40–48 px, rakamlar Inter; etiket ve sayaçlar IBM Plex Mono; kısa notlar ve slogan Caveat (slayt başına en çok bir not). Satır aralığı 1,3–1,4. Formüller KaTeX ile, gövdeden bir boy büyük. Yazı tipi dosyaları `dnamathos-pdf-tasarimi` skill'inin `assets/fontlar` klasöründedir; o skill yüklü değilse aynı aileler Google Fonts'tan indirilir.

**Karşıtlık:** Safran, sınıfların koyu tonları üzerinde 4,6:1 verir; bu yüzden koyu zeminde safran yalnız büyük yazıda (≥ 48 px başlık ve vurgu sözcüğü) ve kalın 26 px'lik KAYDIR işaretinde kullanılır; koyu zeminde gövde yazısı beyazdır. Açık ve orta zeminde safran yazı rengi olmaz; yalnız dolgu, vurgu şeridi ve çizgidir.

**Sabit öğeler (her slayt):**
- Üstte ince ilerleme çubuğu ya da "3 / 9" sayacı.
- Sol üstte konu etiketi hapı (ör. "LGS · Üslü İfadeler"); kapakta bunun yerine sütun etiketi ("Konu anlatımı") durur (`profil-izgarasi.md`).
- Sol altta küçük "DNAMATHOS" yazısı (kapakta "Sınıf · Konu" satırının altında); logo büyütülmez.
- Son slayt dışında sağ altta kaydırma işareti: büyük harf ve geniş harf aralıklı "KAYDIR" yazısı (IBM Plex Mono 600, 26 px, harf aralığı 0,18 em) ve yanında 110 px uzunluğunda ince çizgi ok (3 px, yuvarlak uçlu). Renk açık ve orta zeminde sınıfın koyu tonu, koyu zeminde safrandır. Daire, dolgulu düğme ya da "→" karakteri kullanılmaz; yeniden kanca satırlarındaki ok da aynı ince çizgi oktur.
- Kenar boşlukları 80 px; içerik bir ızgaraya oturur, öğeler hizalıdır.

**Kart bileşenleri:** formül kutusu (vurgu renginde 4 px sol kenar), "Dikkat" kutusu (kiremit zemin), "Doğru ✓ / Yanlış ✗" yan yana kartlar, numaralı adım rozetleri, özet kartında 2–4 maddelik kural listesi.

**Üretim hattı:**
- Python ile tek HTML dosyası üret: her slayt 1080 × 1350 px'lik bir `section`; KaTeX auto-render (yerel node_modules/katex); fontlar yerel.
- Playwright Chromium ile her slaytın ekran görüntüsünü `device_scale_factor=1` ve tam 1080 × 1350 boyutta PNG olarak al (`karusel_01.png` … `karusel_09.png`).
- JS ile taşma denetimi: hiçbir öğe slaytın ya da güvenli alanın dışına çıkmasın; en küçük yazı boyutunu ölç ve 40 px'in altındaysa uyar.
- Bütün slaytları tek bir temas tablosunda (contact sheet) yan yana göster ve gözle kontrol et; telefon boyutunda (yaklaşık 390 px genişlik) küçültülmüş bir kopyada da okunurluğa bak.
- Kapağın 3:4 kırpılmış hâlini ayrıca üret ve güvenli alanı kontrol et.
