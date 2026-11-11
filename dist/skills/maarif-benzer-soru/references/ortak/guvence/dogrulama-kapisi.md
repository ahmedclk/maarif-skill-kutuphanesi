# Doğrulama kapısı (dosyalar yazıldıktan sonra)

Uyarlama: k12-teacher-skills k12-check-for-understanding skill'inin doğrulama dosyası (Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · Apache-2.0). Türkçeye çevrildi, Maarif ölçütleriyle genişletildi.

Bu dosya üretim sırasında okunmaz; öğrenciye giden dosya **yazıldıktan sonra** açılır. Erken okunursa, yazmak istediğinin işaretlendiği bir listeye dönüşür. Kapı, dosyayı metin olarak geri okur, notları yazdırır ve dosya varken çalışır. Öğretmen bu adımı görmez; "denetledim ve şunu buldum" anlatılmaz.

Alt ajan aracı varsa ona **yalnız öğrenci dosyasını** ver (cevap anahtarı, öğretmen notu, bağlam yok) ve her maddeyi çözmesini, savunabildiği her seçeneği bildirmesini iste. Taze okur, kastettiğin cevaba doğru akıl yürütemez.

## Kapı A — Tek savunulabilir cevap

Her çoktan seçmeli maddede her seçenek (çeldiriciler dâhil) için yalnız kökün ve görselin söylediğine dayanarak "bu seçenek doğrudur" demenin en güçlü gerekçesini bir satırla yaz. Notları geçici bir dosyaya yaz (öğretmenin klasörüne değil). Ayakta kalan gerekçe sayısını say.

- **Tam bir** → geçer.
- **İki ya da daha fazla** → madde yazıldığı gibi cevaplanamaz. Onarım sırası: (1) anahtarın dayandığı özelliği köke yaz; (2) seçeneği çıkar.
- **Hiç** → ya görselin metni eksiktir (görseli göremeyen öğrenci neyle karar verecek?) ya da anahtar yanlıştır.

İkinci doğru cevabın sık kaynakları: çarpanların sırası bir uzlaşımdır (3 × 4 ve 4 × 3 aynı sayıdır); eşdeğer biçimler tek cevaptır (1/2, 0,5, 2/4, %50); doğru hükme yanlış gerekçeyle varan seçenekler; yuvarlama, birim ve belirtilmemiş duyarlık.

Açık uçlu maddelerde Kapı A şudur: cevap anahtarındaki tam puanlı yanıt tek midir, yoksa anahtarın kabul etmediği ama matematiksel olarak doğru başka bir yanıt var mıdır? Varsa anahtar genişletilir.

## Kapı B — Her çeldirici, bir öğrencinin akıl yürütmesinin vardığı yerdir

Önce kökteki nicelikleri, istediğin hâliyle değil yazıldığı hâliyle hesapla (farklar, oranlar, toplamlar, koordinatlar); birkaç satır `python3 -c` yeter. Sonra her çeldirici için adı konan hatayı bu niceliklere uygula ve hangi seçeneğe vardığını yaz.

- **Kendi seçeneğine** → geçer.
- **Başka bir seçeneğe** → kalır; seçenek ya da hata açıklaması düzeltilir.
- **Hata bu köke uygulanamıyor** → çeldirici seçilemez; bu kökün üretebileceği bir hatayla değiştirilir.

## Kapı C — Maarif bağı (bu kütüphanenin eki)

- Her madde ve her etkinlik, etiketindeki çıktıya ve bileşen harfine gerçekten hizmet ediyor; etiket süs değil.
- Kullanılan her kod tema sayfasında var (`scripts/tymm_kod_denetle.py` ile denetlenir).
- İçerik Çerçevesindeki sınır aşılmamış; terim ve gösterimler sayfadakiyle aynı.
- Öğrenci dosyasında cevap, çözüm ya da cevabı ele veren biçim (kalın, renk) yok.
- **MEB mevzuatı** (`../maarif/meb-olcme-mevzuati.md`): ürün bir okul yazılısıysa maddeler açık uçlu ya da kısa cevaplı, yalnız kısa cevaplı değil, çoktan seçmeli yok (MEV-10…MEV-12); her madde bileşenin bilişsel düzeyinde (MEV-13); kâğıt bir ders saatine sığıyor ve cevap alanı yeterli (MEV-16, MEV-17). Ürün kısa süreli sınavsa notsuz (MEV-40); ilkokul için sınav ya da çoktan seçmeli yok (MEV-41).

## Kapılardan sonra

Bulunanları düzelt, dosyaları yeniden yaz ve değişen her şeyde kapıları yeniden çalıştır; onarılan bir kök önceden sağlam olan bir çeldiriciyi bozabilir. Madde hâlâ kalıyorsa yamamaya devam etme, maddeyi değiştir. Öğretmenin ilk gördüğü sürüm düzeltilmiş sürümdür.
