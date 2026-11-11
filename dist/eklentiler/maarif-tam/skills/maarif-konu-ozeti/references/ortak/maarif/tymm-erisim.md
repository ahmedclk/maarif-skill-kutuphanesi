# TYMM sitesinde çıktıyı bulma ve okuma

Her çalışmada zorunludur: çıktı metnini, bileşenleri ve sınırları bellekten yazma, her seferinde sayfadan al. Matematik dışı dersler için ders sayfası yolu aynıdır; ders ve sınıf kimliklerini https://tymm.meb.gov.tr/ogretim-programlari sayfasından gezerek bul.

Sitede programlar 2026'da güncellendi; çıktı metnini ve sınırları bellekten yazma, her seferinde sayfadan al.

**Erişim:** Kabuktan (curl) site engelli; yalnızca WebFetch kullanılır.

**Yol:** ders sayfası → sınıf sayfası → tema (ünite) sayfası.

| Kademe | Ders sayfası | Sınıf sayfası kimliği |
| --- | --- | --- |
| Ortaokul | https://tymm.meb.gov.tr/ogretim-programlari/ders/ortaokul-matematik-dersi | 5→/6, 6→/7, 7→/8, 8→/9 (ör. .../ogretim-programlari/ortaokul-matematik-dersi/7) |
| Ortaöğretim | https://tymm.meb.gov.tr/ogretim-programlari/ders/matematik-dersi | Hazırlık→/10, 9→/11, 10→/12, 11→/13, 12→/14 (ör. .../ogretim-programlari/matematik-dersi/12) |

- Sınıf sayfası tema bağlantılarını verir: ortaokulda `https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/<id>`, lisede `https://tymm.meb.gov.tr/matematik-dersi/unite/<id>`. Ünite kimlikleri sırasızdır; tahmin etme, sınıf sayfasından oku. Bilinenler: 6. sınıf Sayılar ve Nicelikler (1) 456, (2) 457, Veriden Olasılığa 462; 9. sınıf Sayılar 21, Nicelikler ve Değişimler 23; 10. sınıf Geometrik Şekiller 260, İstatistiksel Araştırma Süreci 271.
- Çıktı kodu MAT.[sınıf].[tema].[sıra] biçimindedir. Tema numarasını sınıf sayfasındaki "N. Tema" başlığıyla eşle. Bir tema "(1)" ve "(2)" diye iki sayfaya bölünmüş olabilir; çıktı ilk sayfada yoksa ikinciye bak.
- Kimlik eşlemesi tutmazsa ders sayfasından yeniden gez. Site açılmazsa programın PDF'ini dene (ders sayfasındaki "Programı Görüntüle"); PDF'i `../guvence/pdf-ile-calisma.md` kurallarıyla oku (çıktı tablolarını pdfplumber ile, bozuk satırları sayfa görüntüsünden). O da olmazsa kullanıcıya erişilemediğini söyle ve yalnızca onun verdiği metinle çalış.

**Okuma:** WebFetch özetleyici uzun alıntıları yaklaşık 125 karakterde keser ve uzun listeleri bazen özetler. Kelimesi kelimesine metin için "kısa ve birebir alıntıla; 100 karakterden uzunsa ardışık parçalara böl" de; tek bir bölümü ya da tek bir çıktıyı ayrı istekle al.

**Tema sayfasından alınacaklar:**

| Başlık | Kullanımı |
| --- | --- |
| Öğrenme Çıktıları ve Süreç Bileşenleri | Kod, çıktı cümlesi ve a, b, c, ç… bileşenleri birebir. Kullanıcının verdiği metinle karşılaştır; fark varsa bildir, sitedeki güncel metni esas al. |
| Tema başlığındaki kod listeleri | Alan Becerileri (MAB), Kavramsal Beceriler (KB), Eğilimler (E), SDB, Değerler (D), Okuryazarlık (OB), Disiplinler Arası ve Beceriler Arası İlişkiler, Ders Saati. Yalnızca bu listedeki kodlar o tema için kullanılabilir. |
| İçerik Çerçevesi | Kapsam sınırı. Sorular bu sınırı aşmaz. |
| Genellemeler, Anahtar Kavramlar, Sembol ve Gösterimler | Konu özeti ve soru dili; terim ve gösterimler sayfadakiyle aynı olur. |
| Öğrenme Kanıtları | Önerilen madde türleri (açık uçlu, doğru-yanlış, eşleştirme, çalışma kâğıdı, performans görevi). |
| Temel Kabuller, Ön Değerlendirme, Köprü Kurma | Ön bilgi varsayımı ve bağlam fikirleri. |
| Öğrenme-Öğretme Uygulamaları | Çıktı başına etkinlik ve sınırlamalar ("…'e girilmez", "… ile sınırlandırılır"); soru bağlamı için ilk kaynak. E, SDB, D, OB kodları burada davranışın hemen arkasında parantez içinde geçer (ör. "birbirlerini dinlemeleri (SDB2.1)", "temsiller ile çarpanları ilişkilendirmeleri (OB4)"). |
| Farklılaştırma | Zor soru (zenginleştirme) ve destek notu. |

Sayfa bazı başlıkları boş bırakabilir ("-"); boşsa not et, uydurma.

**Tema sayfasının başlık sırası** (6. sınıf, 1. Tema sayfasında 11.11.2026'da doğrulandı): Ders Saati · Alan Becerileri · Kavramsal Beceriler · Eğilimler · Programlar Arası Bileşenler (Sosyal-Duygusal Öğrenme Becerileri, Değerler, Okuryazarlık Becerileri) · Disiplinler Arası İlişkiler · Beceriler Arası İlişkiler · Öğrenme Çıktıları ve Süreç Bileşenleri · İçerik Çerçevesi (Genellemeler, Anahtar Kavramlar, Sembol ve Gösterimler) · Öğrenme Kanıtları (Ölçme ve Değerlendirme) · Öğrenme-Öğretme Yaşantıları (Temel Kabuller, Ön Değerlendirme Süreci, Köprü Kurma, Öğrenme-Öğretme Uygulamaları) · Farklılaştırma (Zenginleştirme, Destekleme). Bir skill bir başlığı kullanıyorsa onu bu adla anar.

## Ders bazında alan becerisi sayfaları

| Ders | Kod öneki | Sayfa |
| --- | --- | --- |
| Türkçe | TAB | https://tymm.meb.gov.tr/beceriler/turkce-alan-becerileri |
| Matematik | MAB | https://tymm.meb.gov.tr/beceriler/matematik-alan-becerileri |
| Fen Bilimleri | FBAB | https://tymm.meb.gov.tr/beceriler/fen-bilimleri-alan-becerileri |
| Sosyal Bilimler | SBAB | https://tymm.meb.gov.tr/beceriler/sosyal-bilimler-alan-becerileri |
| Sanat | SAB | https://tymm.meb.gov.tr/beceriler/sanat-alan-becerileri |
| Beden Eğitimi, Oyun ve Spor | BEOSAB | https://tymm.meb.gov.tr/beceriler/beden-egitimi-oyun-ve-spor-alan-becerileri |
| Bilişim Teknolojileri ve Yazılım | BTYAB | https://tymm.meb.gov.tr/beceriler/bilisim-teknolojileri-ve-yazilim-alan-becerileri |
| Tasarım | TSRMAB | https://tymm.meb.gov.tr/beceriler/tasarim-alan-becerileri |
| Din Eğitimi ve Öğretimi | DAB | https://tymm.meb.gov.tr/beceriler/din-egitimi-ve-ogretimi-alan-becerileri |
| Yabancı Dil | YDAB | https://tymm.meb.gov.tr/beceriler/yabanci-dil-alan-becerileri |

Programlar arası bileşenler: https://tymm.meb.gov.tr/beceriler/kavramsal-beceriler · /beceriler/egilimler · /beceriler/sosyal-duygusal-ogrenme-becerileri · /beceriler/erdem-deger-eylem-cercevesi · /beceriler/okuryazarlik-becerileri. Ortak metin: https://tymm.meb.gov.tr/ortak-metin.

## Bağlantı yoksa

TYMM sayfası açılamıyor ve program PDF'i de yoksa skill durmaz: öğretmenin verdiği çıktı metniyle çalışır, kodu ve bileşenleri öğretmene bir satırla doğrulatır ve öğretmen çıktısının sonuna şu notu ekler: "Çıktı ve bileşenler TYMM sayfasından doğrulanamadı; öğretmenin verdiği metne dayanır." Hangi sayfanın okunup okunmadığını anlatan başka bir açıklama yazılmaz. Okunmamış bir sayfaya atıf yapılmaz, kod uydurulmaz.
