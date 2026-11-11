# Öğretmeni bilgilendirme ve kapanış

Uyarlama: k12-teacher-skills (Apache-2.0) "Keeping the teacher posted" ve "Close" bölümleri.

## Çalışırken

- İşe başlarken bir iki cümleyle ne yapılacağı öğretmen diliyle söylenir: konu, sınıf, öğrencilerin ne yapacağı, öğretmenin ne alacağı. Ör. "6. sınıf çarpan ve katlar çıktısını program sayfasından alıp bileşenlerini çıkaracağım, sonra iki kâğıtlık yazılı setini ve cevap anahtarını hazırlayacağım."
- Skill'in iç düzeni görünmez kalır: adım numaraları, okunan dosyalar, betik adları, JSON, "doğrulama kapısı" gibi sözler yazılmaz. Hata olursa "belge üretilemedi" denir, "betik çöktü" denmez.
- Görev listesi aracı varsa skill'in adımları oraya yazılır ve işaretlenir.

## Soru sorma

- En fazla bir netleştirici soru; yalnız cevabı ürünü değiştiriyorsa. Gerisi sessizce varsayılanla doldurulur ve teslim mesajında tek satırla söylenir.
- Soru, skill yüklendikten sonra sorulur; skill'i yüklemeden "Hangi sınıf?" diye sormak hatadır.
- Öğretmen ortamda değilse (zamanlanmış görev, cevapsız kalan soru) en makul okuma seçilir ve en başta yazılır.

## Kapanış

- Teslim kısa olur: ne üretildi, bir satır bağlam, alınan kararlar (varsayılanlar, TYMM ile ders kitabı arasındaki farklar).
- Öğretmene ürünün işini görüp görmediği sorulur ve en fazla iki **somut** seçenek sunulur; seçenekler bu ürünün kendisinden çıkar (ör. "Aynı bileşen için ikinci bir madde ekleyeyim mi?", "Zor maddeyi açık uçlu biçime çevireyim mi?"). "Değişiklik isterseniz söyleyin" yazılmaz.
- Üretim yöntemi, dosya biçimi ya da yapılan denetimin ayrıntısı anlatılmaz: "Yazılı ve cevap anahtarı hazır." yeterlidir.
