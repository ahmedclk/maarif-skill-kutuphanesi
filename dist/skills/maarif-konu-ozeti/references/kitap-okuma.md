# Ders kitabını okuma ve programla doğrulama

Kaynak: `maarif-konu-ozeti` 1. ve 2. bölüm (DNAMATHOS).

Kitap PDF'i büyük olabilir (50 MB, 80 sayfa). `references/ortak/guvence/pdf-ile-calisma.md` kurallarını uygula: önce `pypdf` ile her sayfanın metninden kısa bir döküm al ve dersin sayfalarını bul; Bilgi kutularının ve tabloların metnini `pdfplumber` ile çıkar; yalnız dersin sayfalarını PyMuPDF ile (`import pymupdf`, 110–130 dpi; yoksa `pdftoppm -r 110`) görüntüleyip modelleri, şekilleri ve tabloları gözle oku. Metin çıkarımında kesirler bozulur ("5 2" = 2/5 olabilir); kesir ve üs içeren her ifadeyi görüntüden doğrula. Taranmış sayfada (`extract_text()` boş ya da `(cid:NN)` dolu) metin uydurulmaz; sayfa görüntüden okunur.

**Sayfa numarası:** PDF'in sayfa sırası kitabın basılı sayfa numarası değildir (ör. PDF'in 4. sayfası kitabın 89. sayfası). Slaytlarda her zaman basılı sayfa numarasını kullan; eşlemeyi sayfa altındaki numaradan çıkar.

**Tema numarası:** Kitabın tema numarası TYMM sitesindekiyle aynı olmayabilir (ör. 6. sınıf kitabının 3. teması sitede 1. Tema'nın ikinci sayfasıdır, MAT.6.1.5–6.1.8). Kitabın konu başlıklarını TYMM'deki İçerik Çerçevesiyle eşle ve sitedeki kodları kullan; farkı teslim mesajında bir satırla belirt.

**MEB kitabının bölümleri ve özette kullanımı:**

| Kitaptaki bölüm | Ne işe yarar | Özette kullanımı |
| --- | --- | --- |
| Hazır mıyız? | Ön bilgi denetimi | Yalnız temaya giriş dersinde, en fazla 2 hızlı soruluk tek slayt; takvim sıkışıksa atılır |
| Başlayalım | Temaya giriş bağlamı | Kapakta tek cümlelik merak sorusu |
| Etkinlik | Kavramın keşfi | Etkinliğin ulaştığı fikir, tek modelle özetlenir; "Kitapta: Etkinlik 2, s. 91" atıfı |
| Bilgi kutusu | Kural ve tanım | Konu kartının çekirdeği; kitabın terim ve gösterimiyle, kısaltılarak |
| Örnek | Çözümlü uygulama | Konu kartında bir kısa örnek; diğerleri "Kitapta" atıfıyla |
| Problem / Gerçek yaşam problemleri | Adım adım problem çözme | Ders sorularına model; çözüm adımları (anla → plan → çöz → kontrol et) öğretmen PDF'inde |
| Performans görevi | Uzun süreli çalışma | Derste yapılmaz |
| Ölçme ve değerlendirme soruları | Tema sonu soruları | Ders sorularına model; tekrar dersinde özgün benzerleri çözdürülür |

**Telif ve görsel:** Kitabın görsellerini, fotoğraflarını ve sayfalarını slayta kopyalama. Modeli (onluk blok, sayı doğrusu, alan modeli, şerit) kendi çiziminle yeniden kur; kitaptaki soruya sayfa ve numarasıyla atıf yap. Kitaptaki bir soruyu derste kullanmak gerekiyorsa özünü koruyan, sayı ve bağlamı değişmiş özgün bir benzerini yaz.

Kitabın başlıkları çıktı kodu vermez. Dersin kapsamını TYMM tema sayfasındaki öğrenme çıktıları ve süreç bileşenleriyle eşle (erişim yolu ve okuma notları: `references/ortak/maarif/tymm-erisim.md`). Her kitap bölümünün hangi çıktı ve bileşene hizmet ettiğini yaz.

- İçerik Çerçevesi ve Öğrenme-Öğretme Uygulamalarındaki sınırlamalar ("…'e girilmez", "… ile sınırlandırılır") konu özetinin ve soruların sınırıdır.
- Kitap ile TYMM arasında terim ya da gösterim farkı varsa özette TYMM'nin güncel metnini esas al, kitabın kullandığı adı parantezde ver ve farkı teslim mesajında belirt.
- Kitabın yöntemini izle (ör. kesirlerde bölmede "paydaları eşitle, payları böl"); başka bir kısa yolu yalnız öğretmen notunda karşılaştırma için an.
- Bileşenleri beceri basamaklarına bağla (`references/ortak/dersler/matematik/beceri-eslemesi.md`); her konu kartının "Yazılıda böyle sorulur" kutusu bu eşlemeden doğar.
