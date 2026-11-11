# Matematik: robotiklik ve güçlük denetimi (üretimden önce)

Soruları yazınca kendine şu tabloyu çıkar ve sorun varsa düzelt:

| Denetim | Eşik |
| --- | --- |
| Alt madde sayılarının dağılımı | Tek tip değil; 3+ maddeli sorular ortaokulda ≤ 1/3, lisede ≤ 1/2 |
| Süreç dili | Yönergede bileşen adı yok; yalnızca `meb-soru-dili.md` dosyasındaki MEB süreç ifadeleri |
| Bileşen zinciri | Her soruda 1–3 komşu bileşen; maddeler birikimli |
| Matematiksel çekirdek | Her soruda bir kavrayış noktası; tek başına rutin hesap sorusu yok |
| Kâğıt seti | Her kâğıt senaryoya birebir uyuyor; yazılıda ölçülen her bileşen setin toplamında ≥ 1 |
| Görsel | Her kâğıtta ≥ 3 görselli soru (ortaokulda ≥ 4); her görsel çözüm için gereken bilgiyi taşıyor ve cevabı vermiyor; aynı görsel türü bir kâğıtta tekrar etmiyor; her çıktı sette en az bir kez görselli soruyla ölçülüyor |
| Art arda aynı yapı | Yok |
| Kalıp tekrarı | Aynı kalıp ≤ 2 |
| Kişi iddiası açılışı | ≤ 2 soru |
| Bileşen etiketleri | Her biri programın fiiliyle; aynı etiket ≤ 2 kez |
| İçerik çerçevesi | Sınır dışı soru ve gösterim yok (görseller dâhil) |
| Konu özeti | Hiçbir sorunun cevabını vermiyor |
| Öğretmen üslubu | Soru bağlamında ve maddelerde kalın, italik ya da renk vurgusu yok (MEB'in sabit biçimleri dışında); konu özeti soruyla açılıyor ve bir kartta tek fikir var; boş övgü yok |
| Güçlük etiketi | Her alt maddede Z · Y · C yazılı ve karar tablosuyla tutarlı |
| Güçlük payı | Kolay %15–25, orta %45–55, zor %25–35 (her kâğıt); kâğıtlar arasındaki fark her düzeyde ≤ 10 puan |
| Merdiven | Zor madde son maddede; lisede kolay madde tek başına soru değil |
| Puan aralıkları | Alt madde ve soru puanları `guclugu-belirleme.md` dosyasındaki aralıklarda; soru toplamı 10–20 |

Güçlük payını kodla hesapla (alt madde güçlüğü × puan) ve assert ile denetle.

Mümkünse bu denetimi soruları görmemiş ayrı bir ajana yaptır.
