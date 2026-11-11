---
name: maarif-hata-analizi
description: Bir öğrencinin ya da sınıfın yanlış yaptığı soruları, deneme veya yazılı sonucunu, ödevini ya da çözüm kâğıdı fotoğrafını inceleyip hataları türlerine ve Maarif çıktı ile süreç bileşenine göre sınıflandırır; tekrarlayan örüntüleri bulur, telafi anlatımı, kolaydan zora kontrol soruları, kendi cümleleriyle anlatma görevi, ustalık ölçütü ve aralıklı tekrar takvimi hazırlar; öğretmen ya da koç raporu ve isteğe bağlı veli özeti verir. Tetikleyiciler - bu öğrencinin hatalarını analiz et, deneme sonucuna göre telafi planı, nerede yanlış yapıyor, yanlış yaptığı sorular, sınıfın yazılı sonuçları, eksik kazanım analizi. Yeni test ya da yazılı için değil (maarif-beceri-temelli-test, maarif-ortak-yazili), yalnız ikiz soru isteniyorsa değil (maarif-benzer-soru), derste anlama kontrolü için değil (maarif-anlama-kontrolu).
license: Apache-2.0. DeepTutor (HKUDS) yönlendirmeli öğrenme istemlerinden uyarlanmıştır ve değiştirilmiştir. Ayrıntı - LICENSE ve NOTICE.
compatibility: Çözüm kâğıdı fotoğrafı ya da sonuç tablosu (PDF, görüntü, xlsx, csv) verilebilir. TYMM sayfaları için web erişimi.
metadata:
  surum: "2.0.0"
  yazar: DNAMATHOS
  omurga: TYMM öğrenme çıktısı ve süreç bileşeni; süreç odaklı değerlendirme ve destekleme
  dersler: matematik (tam); diğerleri şablonla
  onceki_ad: ogrenci-hata-analizi 1.x
  uyarlama: HKUDS/DeepTutor (Apache-2.0)
---

# Maarif hata analizi ve telafi

Amaç: Hatayı öğrenme fırsatına çevirmek. Her hata bir çıktının bir bileşenine bağlanır; telafi, tekrarlayan örüntülere kurulur ve bir bileşen ancak kanıtla kapanmış sayılır. Koçluk, özel ders ve sınıf düzeyinde kullanılır.

**Önyargısız dil ve kişisel veri her yerde:** `references/ortak/uslup/onyargisiz-dil.md` ve `references/ortak/guvence/kvkk-ve-telif.md`. Öğrenci takma adla anılır; öğrenciyi suçlayan, etiketleyen ya da başkasıyla karşılaştıran ifade kullanılmaz.

## Adım 0 — Yönlendirme (sessiz)

1. `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`.
2. Ders dosyası: matematik → `references/dersler/matematik.md` (şimdi oku). Yoksa `references/ortak/dersler/_sablon.md`.
3. Görüntü ya da PDF ise `references/ortak/guvence/pdf-ile-calisma.md`; çok satırlı sonuç tablosu ise veriyi dosyaya al ve kodla say (sohbette elle sayma).

## Adım 1 — Girdi

Yanlış ya da boş bırakılan sorular; öğrencinin cevapları ve doğru cevaplar; varsa çözüm kâğıdı fotoğrafı ve sonuç tablosu; sınıf ve hedef (LGS, okul yazılısı). Soruların kendisi yoksa yalnız onu iste.

## Adım 2 — Her yanlışı yeniden çöz ve programa bağla

Soruyu doğru çöz; sorunun çıktısını ve bileşenini eşle. Öğrencinin cevabına nasıl ulaşmış olabileceğini geriye doğru bul: işaretlediği seçenek hangi hatanın sonucu? Çözüm kâğıdı varsa hatanın oluştuğu adımı göster. Emin değilsen "olası" de ve öğrenciye sorulacak bir kontrol sorusu öner. Kanıt olmadan kesin hüküm verilmez.

## Adım 3 — Sınıflandır

| Tür | Belirti | Telafi yaklaşımı |
| --- | --- | --- |
| Yapısal | Kavram ya da ön bilgi eksik (çoğunlukla önceki sınıf çıktısı) | Konuyu farklı bir temsille yeniden kur; ön koşul çıktıyı kodla adlandır ve yokla |
| Sapma | Kavram biliniyor, işlem ya da aktarım hatası (işaret, basamak kaydırma) | Kısa kontrol alışkanlığı; 3–5 benzer işlem |
| Uygulama | Kural biliniyor, yeni bağlama ya da problem kurgusuna aktarılamıyor | Kolaydan zora bağlamlı problemler |
| Üstbilişsel | Süre yönetimi, soruyu tam okumama, kontrol etmeme, emin olmadan işaretleme (SDB1.2 Kendini Düzenleme ile ilişkili) | Soru okuma ve kontrol stratejisi; süreli kısa denemeler |

Bir yanlışta birden fazla tür varsa asıl neden birincil türdür. Hata adı gözlenen davranışla yazılır ("ortak kat yerine çarpımı alıyor"), etiketle değil.

## Adım 4 — Örüntü

Bileşen × hata türü tablosu (kodla say). Tek seferlik hataları tekrarlayan örüntülerden ayır; telafi planını tekrarlayan örüntüler üzerine kur ve öncelik sırası ver (yazılı ağırlığı yüksek bileşen ve yapısal hatalar önce).

## Adım 5 — Telafi içeriği

Her örüntü için:

1. **Kısa anlatım** (`references/ortak/uslup/ogretmen-uslubu.md`): soruyla açılış, somut örnek, doğru tanım, 1–2 örnek, sık yapılan yanlış ve "Peki … olsaydı?" sorusu.
2. **Kontrol soruları:** kolaydan zora 3–5 soru, çözümleriyle; çoktan seçmelide her çeldirici belirli bir hatayı temsil eder (`maarif-benzer-soru` kuralları, ders dosyasında).
3. **Kendi cümleleriyle anlatma görevi:** konuyu kendi sözleriyle anlattıracak bir soru; değerlendirme: sade dille anlatabiliyor mu, önemli bir eksik var mı, yanlış anlama var mı?

## Adım 6 — Ustalık kapısı

Bir bileşen, öğrencinin **farklı biçimdeki en az iki soruyu** doğru çözmesi ya da kavramı kendi sözleriyle doğru anlatmasıyla kapanır; tek doğru cevap yetmez. Bileşen kapanmadan sonraki konuya geçme önerilmez. Öğrenci bir sorunun hatalı olduğunu söylerse önce soru kontrol edilir; gerçekten hatalıysa o yanlış analizden çıkar.

## Adım 7 — Tekrar takvimi

Kapanan bileşenler için aralıklı tekrar: başlangıç 1, 3, 7 ve 14 gün; öğrencinin haftalık ders düzenine göre uyarlanır. Her tekrarda kısa kavram özeti, sık hata hatırlatması ve 1–2 karma soru.

## Adım 8 — Çıktı

1. **Öğretmen ya da koç raporu:** hata tablosu, örüntüler, öncelik, telafi planı, ustalık durumu (bileşen · kapandı / sürüyor).
2. **Öğrenci çalışma sayfası:** telafi anlatımı, kontrol soruları, kendi cümleleriyle anlatma görevi.
3. **İsteğe bağlı veli özeti:** teknik terimsiz, 4–6 cümle, en az bir somut güçlü yön ve evde yapılabilecek bir şey; başka öğrencilerle karşılaştırma yok.

Mevzuat (`references/ortak/maarif/meb-olcme-mevzuati.md`): rapor öğretmenin kendi kullanımı içindir (MEV-32); puanlanan kâğıda yazılacak bireysel geri bildirim notları ve telafi önerisi içerir (MEV-30, MEV-31); öğrenci adlı sıralı liste, şubeler ya da okullar arası karşılaştırma ve sıralama üretilmez (MEV-33).

Sınıf verisi verildiyse rapor bileşen bazında sınıf tablosu da içerir ve destekleme grubunu önerir (`maarif-farklilastirma` ile sürdürülebilir).

## Adım 9 — Doğrulama

- Her yanlışın yeniden çözümü kodla ya da elle doğrulandı; "olası" denen yerlerde kontrol sorusu var.
- Kontrol sorularına `references/ortak/guvence/dogrulama-kapisi.md` Kapı A ve B uygulandı.
- Raporda önyargılı sözcük yok (onyargisiz-dil listesinde arama); gerçek ad yok.

## Adım 10 — Kapanış

En fazla iki somut seçenek: "En sık iki örüntü için ikiz soru seti çıkarayım mı?" (maarif-benzer-soru) ya da "Destekleme grubu için bu derse farklılaştırılmış bir çalışma kâğıdı hazırlayayım mı?" (maarif-farklilastirma).
