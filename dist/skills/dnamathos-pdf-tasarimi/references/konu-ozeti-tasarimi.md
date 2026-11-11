# Konu özeti tasarımı (DNAMATHOS)

Kaynak: `maarif-konu-ozeti` 8. bölüm. Genel tasarım dili `tasarim-dili.md` dosyasındadır; bu dosya konu özetine özgü eklerdir.

**Tasarım:** `tasarim-dili.md` dosyasındaki DNAMATHOS tasarım dili (297 × 167 mm 16:9, renkler, yazı tipleri, üst şerit, menü ve iki panelli slayt, şekil ve tablo kuralları). Ders özetine özgü olarak:

- Birden çok ders tek PDF'te verilir; üst şeritte "KONU ÖZETİ · TEMA N · DERS M · N. SINIF MATEMATİK", düğmeler: Ana, Konu, Sorular, Ödev ve ders düğmeleri (D1, D2, …). Öğretmen PDF'inde: Ana, Plan, Notlar, Çözümler ve ders düğmeleri.
- Kapak, dersin akışını gösterir: konu başlıkları ve her birinin altında kiremit renkli "↳ Soru N" satırı; ikinci sütunda Kaydet, yazılı provası ve ödev.
- Konu kartlarında sağ panelin üstü boş yazı alanıdır; ekranda paylaşılıp tablet kalemiyle (Notability) üzerine yazılır. Yazı alanı en az panelin yarısıdır.
- "Yazılıda böyle sorulur" kutusu gri-lacivert zeminde (#e6e9f0 / #2e3a55), "Kitapta" atıfı yeşil (#0b6157), "Sık yapılan hata" ve "Yazılı tüyosu" sarı (#ffd166 kenarlı, #fffbea zemin).
- Şekillerde boyalı bölgeler ekranda seçilecek kadar doygun pastel renklerde olur (ör. #bcd0f3, #f8c9b8, #bfe5dc, #ffe29a).
- Ödev kartındaki boş satırlar kalemle yazılacak kadar geniş (en az 12 mm yüksekliğinde, altı çizgili).
- Dosyalar: `DNAMATHOS_<sınıf>_Tema<N>_Ders<ilk>-<son>.pdf` (öğrenci, ekranda) ve `…_Ogretmen.pdf`.

**Üretim hattı:** Python ile HTML, KaTeX, Playwright ile PDF; slayt sırası dersin akış listesinden üretilir ve her slaytın önceki ve sonraki düğmesi bu listeden hesaplanır (tüyolu kopya akışa girmez, yalnız "Tüyo →" ile açılır). İç bağlantılar pypdf ile denetlenir (her bağlantının hedefi ve her slayta ulaşılabilirlik); JS ile taşma denetimi, her slaytın ekran görüntüsü ve temas tablosu (`uretim-hatti.md`). Teslimden önce iki PDF de "Çıktı PDF'ini denetleme" adımlarından geçer (`references/ortak/guvence/pdf-ile-calisma.md`): sayfa sayısı akış listesine eşit, hatalı bağlantı 0, öğretmen PDF'inde her ders sorusunun çözümü var, birkaç sayfa PyMuPDF ile görüntülenip gözle bakıldı.

**Haftalık paket slaytları:**
- **Isınma turu:** kapak koyu zeminde "Isınalım" ve soru sayısı; her soru açık zeminde tek ekran, sol üstte biçim hapı (Hızlı hesap, Hatayı bul…), altta ilerleme noktaları; cevap ekranı ayrı slayt. Soru metni en az 30 pt.
- **Slogan:** Kaydet kartının altında sarı vurgu çizgili tek satır; Lora italik.
- **Kavrama testi:** kapak "Bu dersi kontrol edelim" ve dört sorunun türleri; her soru bir slayt: soru, "a) Cevap" ve "b) Nasıl karar verdin?" yazma alanları, sağ üstte "Eminim / Emin değilim" kutuları. Puan, düzey ve kod yazılmaz.
- **Yazdırılabilir kâğıt:** A4 dikey, tek yaprak (ön ve arka), her ders yeni sayfa; `ornekler/6-sinif-ortak-kat` kâğıdı örnek düzendir.
