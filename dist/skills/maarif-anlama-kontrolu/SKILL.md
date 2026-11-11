---
name: maarif-anlama-kontrolu
description: Bir öğrenme çıktısının tek bir süreç bileşeni için 1–3 maddelik anlama kontrolü ya da çıkış kartı hazırlar; çeldiriciler belgelenmiş öğrenci yanılgılarından gelir ve öğretmen kılavuzu her olası cevabın neyi gösterdiğini ve sonraki öğretim adımını söyler. Netleştirici soru sormadan önce yükle. Şu an matematik içindir; başka derslerde skill'i anmadan normal yardım et. Tetikleyiciler - çıkış kartı hazırla, anlama kontrolü, konuya geçmeden kim anladı görmek istiyorum, ders sonu hızlı yoklama, ön değerlendirme sorusu, tanılayıcı soru. Puanlanan sınav, test ya da alıştırma seti değildir; numaralı test ya da yalın cevap anahtarı başka iştir (maarif-beceri-temelli-test, maarif-ortak-yazili, maarif-benzer-soru). Ders planı (maarif-ders-plani, kendi çıkış kartını taşır), farklılaştırma (maarif-farklilastirma) ya da derse hazırlık (maarif-derse-hazirlik) için değil.
license: Apache-2.0. k12-teacher-skills (Copyright 2026 Anthropic, PBC; Copyright 2026 Learning Commons) k12-check-for-understanding skill'inden uyarlanmıştır ve değiştirilmiştir. Ayrıntı - LICENSE ve NOTICE.
compatibility: TYMM sayfaları için web erişimi. Kısa bir öğrenci kâğıdı ve öğretmen kılavuzu üretir.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: TYMM öğrenme çıktısı ve süreç bileşeni; süreç odaklı değerlendirme
  dersler: matematik
  uyarlama: anthropics/k12-teacher-skills k12-check-for-understanding (Apache-2.0)
---

# Maarif anlama kontrolü

Bir çıktı için, öğretmenin anlatmak üzere olduğu ya da yeni anlattığı bir derste kullanılacak 1–3 maddelik kontrol: **tek bir süreç bileşenine** odaklanır, çeldiricileri gerçek öğrenci hatalarından gelir ve bir öğretmen kılavuzu her cevabın neyi gösterdiğini ve ne yapılacağını söyler. Kontrol bilerek küçüktür: sınıfın nerede olduğunu beş dakikada okumak içindir, puanlanmaz (`references/ortak/maarif/cerceve.md` 8. bölüm: süreç içi değerlendirme). MEB mevzuatındaki kısa süreli sınavın karşılığıdır: birkaç soru, anında geri bildirim, not yok (MEV-40, `references/ortak/maarif/meb-olcme-mevzuati.md`). İlkokulda "sınav" sözcüğü kullanılmaz ve çoktan seçmeli madde yazılmaz; kontrol bir gözlem etkinliği olarak verilir (MEV-41).

**Önyargısız dil her yerde:** dosyalarda ve sohbette `references/ortak/uslup/onyargisiz-dil.md`. "Paydayı anlamakta zayıf" değil, "paydayı her parçanın büyüklüğü yerine parça sayısı olarak okuyor".

Öğretmeni bilgilendirme `references/ortak/uslup/ilerleme-ve-kapanis.md` kurallarıyla: "Programdaki bileşeni ve bu bileşende sık görülen hataları alıp kontrolü ve cevapları okuma kılavuzunu hazırlayacağım." Adım adları, dosya adları ve denetimler görünmez.

## Adım 0 — Yönlendirme (sessiz)

**Ders.** Matematik (sayılar, kesirler, oran, geometri, cebir, fonksiyon, veri ve olasılık, MAT kodları) → `references/dersler/matematik.md` dosyasını **şimdi** oku. Okumak zorunludur; maddeleri onsuz tasarlamak kritik hatadır ve bu turda o dosya skill talimatının kendisidir. Başka bir dersse bu belgeyi bir kenara bırak ve skill'i anmadan normal yardım et. Ders belirsizse Adım 1'de sor.

**Omurga.** `references/ortak/maarif/cerceve.md` ve `references/ortak/maarif/tymm-erisim.md`.

## Adım 1 — Netleştirme (en fazla bir soru)

Yalnız maddeleri değiştirecekse: sınıf belli değilse ("kesirler" birkaç sınıfa yayılır) ya da konu iki çıktıya denk geliyorsa. Madde sayısı, biçim ya da zorluk hiç sorulmaz.

## Adım 2 — Programa dayandır

Tema sayfasından birebir: çıktı, bileşenler, İçerik Çerçevesi sınırları ve gösterimler; önceki sınıfın ön koşul çıktısı ve sonraki çıktı. Sayfa açılmazsa öğretmen kılavuzuna şu dipnot eklenir: "Çıktı, ön koşullar ve sık hatalar genel öğretim deneyimine dayanır; program sayfasından doğrulanamadı." Okunmamış bir kaynağa atıf yapılmaz, araştırma uydurulmaz.

## Adım 3 — Odak bileşeni seç ve onaylat

1. Çıktının **bütün** bileşenlerini gözden geçir.
2. **Ölçülmeye en uygun** olanı seç: öğrencilerin anlayışında gerçek bir ayrım noktası olan, 1–3 maddeyle yoklanabilen ve farklı anlayış düzeylerini birbirinden ayıran bileşen.
3. **Seçimi ve gerekçesini söyle, sonra dur ve sor:** bileşenin öğrenciden ne istediği tek bir sade cümleyle (öğretmen dilinde, bileşenin kendi sözcükleriyle değil; taşıdığı sınırı da anarak), neden bu bileşen tek satırla ve tek bir doğrudan soru. **Öğretmen cevap vermeden Adım 4'e geçilmez.**
4. Öğretmen başka bir bileşeni ya da birden fazlasını seçerse kapsam onun seçimidir; tek satırla yeniden söyle ve her maddeyi ona bağla.

Sonra bir iki cümleyle ne yapacağını söyle: "Bu bileşende sık görülen hataları çıkarıp kontrolü ve cevapları okuma kılavuzunu hazırlıyorum."

## Adım 4 — Kontrolü kur

Ders dosyasının kurulum bölümünü izle: zihinsel istem türü, hata → kök özelliği haritası, madde tasarımı, öğretmen notları.

**Veri kullanım sınırı:** Ders kitabı, yayınevi ve araştırma bilgisi madde tasarımını ve sonraki adım cümlelerini yalnız içeride besler. **Hiçbir dosyada ve hiçbir sohbet mesajında kitap, yayınevi ya da araştırma kaynağı adı geçmez.** Maddeler özgündür; alınan öğrenci metni, bağlam ya da öğretmen notu birebir kullanılmaz.

## Adım 5 — Çıktı

Adım 4'ün bittiği turda. Önce `references/cikti-bicimi.md` dosyasını oku. İki dosya: öğrenci kâğıdı (yalnız maddeler, seçenekler ya da cevap alanı, ad-tarih satırı) ve öğretmen kılavuzu. Slides artifact türü listeleniyorsa kontrol sunu olarak (her madde bir slayt), kılavuz ayrı belge; yoksa iki HTML ya da Docs belgesi.

## Adım 6 — Doğrulama

**Yalnız iki dosya da yazıldıktan sonra başlar.** `references/ortak/guvence/dogrulama-kapisi.md` dosyasını Adım 4 ya da 5 sırasında açma: o, yazılmış ürünün kapısıdır, kurulum rehberi değildir. Şimdi tamamını oku, iki dosyayı geri oku ve her maddede Kapı A, B ve C'yi çalıştır. Bulunanı düzelt ve dosyaları yeniden yaz. **İki kapıdan geçmemiş bir kontrolü teslim etmek kritik hatadır.**

## Adım 7 — Kapanış

Kontrolün öğretmenin işini görüp görmediğini sor; bu kontrolden çıkan en fazla iki somut değişiklik öner: başka bir zihinsel istem düzeyi, aynı bileşen için ikinci bir madde ya da açık uçlu bir sürüm. "Değişiklik isterseniz söyleyin" yazılmaz. Öğretmen birini seçerse yap, iki dosyayı yeniden yaz ve yeniden sor.

**Sade dil:** Biçimler, dosya adları, şablonlar, üretim yolu ya da doğrulamanın neyi değiştirdiği anlatılmaz: "Kontrol ve cevapları okuma kılavuzu hazır."

## Denetim listesi

- [ ] Odak bileşeni önce öğretmene onaylatıldı; her madde ona bağlı
- [ ] 1–3 madde, fazlası yok
- [ ] Zihinsel istem etiketi çıktıya uygun; biçim istem tablosuna uyuyor; sayılar sınıf aralığında ve bileşenin sınırında
- [ ] Ön koşul ile sınıf düzeyi yönlendirmeleri önceki ve sonraki çıktı haritasına dayanıyor
- [ ] Bir çeldirici ön koşul eksiğini, biri sınıf düzeyindeki karışıklığı gösteriyor; iki satır aynı yere yönlendirmiyor; her sonraki adım bir alt beceri, temsil ya da görev türü adlandırıyor
- [ ] Öğrenci cümleleri kademe sınırında (`references/ortak/uslup/turkce-yazim.md`)
- [ ] Her şeklin metin açıklaması iki dosyada da var; madde metni ve seçenek sırası iki dosyada aynı
- [ ] Öğrenci dosyasında yalnız maddeler, seçenekler ya da cevap alanı ve ad-tarih satırı; kaynak adı yok
