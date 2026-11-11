# Matematik: beceri temelli çoktan seçmeli madde

Kaynak: `benzer-soru-uretimi` skill'inin çeldirici kuralları ve `dnamathos-instagram-karusel` skill'indeki LGS tarzı tanımı (DNAMATHOS), k12-teacher-skills doğrulama kapısıyla birleştirildi.

## Beceri temelli madde nedir?

MEB'in LGS ve beceri temelli örnek sorularındaki gibi: **bağlamlı, çoğunlukla görselli, tek doğru seçenekli; işlem yükü az, akıl yürütme yükü yüksek.** Bilgi, bağlamdan ve görselden okunur; öğrenci bir karar verir. Gerçek bir LGS sorusu birebir kullanılmaz; benzer yapıda özgün madde yazılır ve "LGS tarzı" denir.

## Kök

- Bağlam düz metin, kısa; istenen ayrı satırda: "Buna göre … kaçtır?", "Buna göre aşağıdakilerden hangisi … ?"
- Olumsuz kök ("hangisi **değildir**") sınavda en çok bir iki kez ve olumsuz sözcük altı çizili ya da kalın (MEB'in sabit biçimi).
- Kökte anahtarın dayandığı özellik adıyla geçer (doğrulama kapısı A).
- Öncüllü maddelerde (I, II, III) her öncül tek bir yargıdır; seçenekler "Yalnız I", "I ve II" biçiminde.
- Kademe cümle sınırı `references/ortak/uslup/turkce-yazim.md`.

## Seçenekler ve çeldiriciler

- Ortaokul ve LGS 4 seçenek (A–D); TYT/AYT 5 seçenek (A–E).
- Her yanlış seçenek belirli ve makul bir öğrenci hatasını temsil eder: işaret hatası, işlem önceliğini atlama, birim dönüştürmeyi unutma, kökü yarım okuma, kesirde payları ve paydaları ayrı toplama, ortak kat yerine çarpım alma. Çeldirici, bu kökün sayılarına hata uygulanınca varılan değerdir (doğrulama kapısı B).
- En az bir çeldirici ön koşul eksiğini, en az biri sınıf düzeyindeki karışıklığı yansıtır.
- Seçenekler uzunluk, ayrıntı ve biçimde birbirine benzer; doğru seçenek daha uzun ya da daha ayrıntılı değildir. Sayısal seçenekler küçükten büyüğe sıralanır.
- Eşdeğer biçimler (1/2 ve 0,5) aynı maddede iki seçenek olmaz.
- Seçeneklerde ipucu yoktur. Doğru cevaplar A–D arasında dengeli dağılır: `scripts/cevap_dagilimi.py`.

## Test bütünü

- Her madde bir çıktıya ve 1–2 bileşene bağlıdır; etiket öğretmen anahtarındadır, öğrenci kâğıdında değil.
- Testte en az yarısı görselli (tablo, grafik, şekil, ekran); aynı görsel türü art arda gelmez.
- Güçlük Z · Y · C kuralıyla okunur (`guclugu-belirleme.md`); hedef dağılım kolay ~%25, orta ~%50, zor ~%25. Çoktan seçmelide C = G (genel gerekçe) yerine "öncülleri gerekçeyle sınama" zor sayılır.
- Bağlamlar farklı alanlardan; kişi adları tekrar etmez.

## Cevap anahtarı

Her madde için: doğru seçenek · çıktı ve bileşen · güçlük · kısa çözüm · her çeldiricinin hangi hatadan doğduğu (tek satır).
