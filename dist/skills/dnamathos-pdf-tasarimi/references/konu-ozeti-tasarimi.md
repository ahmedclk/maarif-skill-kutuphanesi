# Konu özeti tasarımı (DNAMATHOS 2.0)

Genel dil `tasarim-dili.md`; bileşenler `scripts/dna.py`. Konu özetine özgü kurallar:

- **Akış ve renk ritmi:** kapak (safran + lacivert) → ısınma kapağı ve soruları (lacivert), cevapları (krem) → konu kartı (safran panel) ve sorusu (krem) → … → Kaydet (safran) → kavrama testi kapağı (lacivert) ve soruları (krem) → ödev (krem).
- **Üst şerit düğmeleri:** Isınma · Konu · Test · Ödev; bulunulan bölüm safran. Birden çok ders tek PDF'teyse şeride ders düğmeleri (D1, D2, …) eklenir. Öğretmen PDF'inde: Plan · Notlar · Çözümler · Test anahtarı.
- **Kapak:** başlığın iki kısmı iki blokta (ör. "Ortak kat" / "ortak bölen"); hap satırları: sınıf ve ders, çıktı kodu ve dersin akışı ("Isınma · 2 konu · kavrama testi"); el yazısıyla tek satırlık "bugün:" notu.
- **Konu kartı:** sol panelde konu hapı, başlık ve "Önce sen" sorusu; sağda kural (boşluklu önerme `<span class="bos"></span>`), şekil, gerekirse "Sık yapılan hata", "Yazılıda böyle sorulur", "Kitapta". Kalan alan tablet kalemiyle yazılacak noktalı yazı alanıdır. Son konu kartında yazı alanının yerine haftanın sloganı gelir.
- **Soru slaytı:** çözüm alanı sorunun altında; tüyo aynı sayfada sağ altta (`tasarim-dili.md` 6. bölüm). Çipler: bileşen harfleri ve Z · Y · C güçlüğü.
- **Ödev kartı boş satırları** kalemle yazılacak genişlikte (en az 12 mm).
- **Dosyalar:** `DNAMATHOS_<sınıf>_<kapsam>.pdf` (öğrenci, ekranda), `…_Ogretmen.pdf`, `…_Kavrama.pdf` (A4, yazdırılabilir).

**Üretim:** `dna.py` ile gövde, `slayt_uret.py` ile PDF ve slayt görüntüleri (denetim çıktısı 0 sorun olmalı), `pdf_denetle.py --sira` ile sayfa ve bağlantı denetimi, temas tablosu ve gözle kontrol. Örnek: `ornekler/6-sinif-ortak-kat/ders_uret.py`.
