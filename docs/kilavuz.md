# Maarif Skill Kütüphanesi: öğretmen kullanım kılavuzu

> Bu dosya `docs/kilavuz.yaml` dosyasından `araclar/kilavuz_uret.py` ile üretilir; elle düzenlenmez.

Claude ile ders planı, ortak yazılı, anlama kontrolü, performans görevi ve hata analizi hazırlarken her ürün bir öğrenme çıktısına ve süreç bileşenine bağlanır; çıktılar TYMM sayfasından doğrulanır, sorular MEB ölçme ve değerlendirme mevzuatına uyar.

## Dört ilke

- **Önce program.** Her skill çıktıyı, bileşenleri ve içerik çerçevesi sınırlarını TYMM sayfasından alır; bellekten yazmaz, kod uydurmaz.
- **MEB kurallarına uyum.** Okul yazılısı açık uçludur, 100 puan üzerindendir, bir ders saatine sığar; kısa süreli sınav notsuzdur; ilkokulda sınav yapılmaz.
- **Doğrulanmış ürün.** Sorular yazıldıktan sonra tek doğru cevap, çeldirici, kod, puan ve cevap sızıntısı betiklerle denetlenir.
- **Son söz öğretmenin.** Skill hazırlar, öğretmen onaylar. Ürünün sınıfa uygunluğunu her zaman siz kontrol edersiniz.

## Kurulum

1. **Hazır istem:** istemler klasöründeki istemi kopyalayın, köşeli parantezleri doldurun ve Claude'a yapıştırın. Kurulum gerekmez.
2. **Skill yükleme:** dist/zip klasöründeki skill dosyasını Claude ayarlarındaki skill bölümünden yükleyin ve açın. Claude isteğinize uyan skill'i kendisi seçer.
3. **Paket:** Claude Code kullanıyorsanız depoyu eklenti pazar yeri olarak ekleyin ve bir paketi kurun (ör. maarif-ogretmen-temel).

## Hangi iş için hangi skill?

### Planlama

| Skill | Ne yapar |
| --- | --- |
| [Programı çözümle](#maarif-cikti-cozumleme) · `maarif-cikti-cozumleme` | Bir temanın ya da çıktının programını tek bir çıktı kartında toplar. |
| [Ders takvimi](#maarif-ders-takvimi) · `maarif-ders-takvimi` | Sınava kalan haftalara göre çıktıları derslere dağıtır. |
| [Ders planı](#maarif-ders-plani) · `maarif-ders-plani` | Bir çıktı için ders planı, öğrenci çalışma kâğıdı ve gözlem formunu birlikte hazırlar. |
| [Derse hazırlık](#maarif-derse-hazirlik) · `maarif-derse-hazirlik` | Var olan bir derse sizinle birlikte hazırlanır ve kısa bir hazırlık notu bırakır. |
| [Farklılaştırma](#maarif-farklilastirma) · `maarif-farklilastirma` | Var olan bir dersi destekleme, temel ve zenginleştirme için üç gruba uyarlar. |

### Ölçme ve değerlendirme

| Skill | Ne yapar |
| --- | --- |
| [Anlama kontrolü](#maarif-anlama-kontrolu) · `maarif-anlama-kontrolu` | Tek bir bileşen için 1–3 maddelik notsuz kontrol ve cevapları okuma kılavuzu hazırlar. |
| [Kavrama testi](#maarif-kavrama-testi) · `maarif-kavrama-testi` | Haftanın konusunu 4–5 soruyla ölçer; ödevi yalnız takılan bileşenlere verir. |
| [Hızlı tekrar](#maarif-hizli-tekrar) · `maarif-hizli-tekrar` | Ders başı 5 dakikalık soru-cevap turu ve denetlenmiş haftanın sloganını hazırlar. |
| [Ortak yazılı](#maarif-ortak-yazili) · `maarif-ortak-yazili` | Seçilen senaryoya uyan açık uçlu yazılı kâğıtlarını ve cevap anahtarlarını hazırlar. |
| [Beceri temelli test](#maarif-beceri-temelli-test) · `maarif-beceri-temelli-test` | LGS ve TYT tarzı, bağlamlı ve görselli çoktan seçmeli test hazırlar. |
| [Performans görevi](#maarif-performans-gorevi) · `maarif-performans-gorevi` | Yazılıda ölçülemeyen bileşenler için görev, dereceli puanlama anahtarı ve formlar hazırlar. |
| [İkiz soru](#maarif-benzer-soru) · `maarif-benzer-soru` | Verdiğiniz soruların aynı bileşeni ölçen özgün ikizlerini yazar. |
| [Hata analizi](#maarif-hata-analizi) · `maarif-hata-analizi` | Yanlışları bileşene ve hata türüne göre ayırır, telafi planı ve tekrar takvimi hazırlar. |

### İçerik üretimi

| Skill | Ne yapar |
| --- | --- |
| [Konu özeti](#maarif-konu-ozeti) · `maarif-konu-ozeti` | Haftalık ders paketini hazırlar - ısınma turu, konu özeti slaytları, slogan, kavrama testi ve sonuca bağlı ödev. |
| [Anlatım videosu](#maarif-anlatim-videosu) · `maarif-anlatim-videosu` | Bir konu ya da soru için sahne planı, seslendirme metni ve Remotion kodu hazırlar. |
| [DNAMATHOS PDF](#dnamathos-pdf-tasarimi) · `dnamathos-pdf-tasarimi` | İçeriği DNAMATHOS'un 16:9 PDF tasarımına dönüştürür ve dosyayı denetler. |
| [Instagram karuseli](#dnamathos-instagram-karusel) · `dnamathos-instagram-karusel` | Konu karuseli, rehberlik ve gerçek hayat gönderisinden oluşan ızgara satırını hazırlar. |

## Skill'ler tek tek

### Programı çözümle
<a id="maarif-cikti-cozumleme"></a>`maarif-cikti-cozumleme`

Bir temanın ya da çıktının programını tek bir çıktı kartında toplar.

**Ne zaman kullanılır?**

- Yeni bir temaya başlarken
- Ders kitabındaki konunun hangi çıktıya denk geldiğini öğrenmek için
- Öteki skill'lerden önce ilk adım olarak

**Siz verin:**

- Sınıf ve ders
- Tema adı ya da çıktı kodu
- İsterseniz ders kitabı sayfaları

**Siz alırsınız:**

- Birebir çıktı metni ve süreç bileşenleri
- Her bileşenin beceri basamağı ve yazılıda ölçülüp ölçülmediği
- İçerik çerçevesi sınırları
- Temadaki eğilim
- SDB
- değer ve okuryazarlık kodları

**Örnek istem:**

```
6. sınıf matematik 1. temanın öğrenme çıktılarını çıkar; bileşenleri beceri basamaklarıyla eşle ve sınırları yaz.
```

**Kontrol edin:** Kitap ile site arasında tema numarası farkı varsa kartın altındaki nota bakın.

**Uyduğu MEB kuralları:**

- MEV-01: Başarı, programdaki çıktılara dayanan ve dersin yapısına uygun ölçmelerle belirlenir. Ölçme şekli çıktının özelliğine göre seçilir; bütün çıktılar planlı bir izlemeyle ölçülür.

**Sonra:** [Ders takvimi](#maarif-ders-takvimi)

### Ders takvimi
<a id="maarif-ders-takvimi"></a>`maarif-ders-takvimi`

Sınava kalan haftalara göre çıktıları derslere dağıtır.

**Ne zaman kullanılır?**

- Dönem başında ya da yazılıdan birkaç hafta önce
- Özel ders ya da koçluk planında

**Siz verin:**

- Kalan hafta ve haftalık ders sayısı
- Okul zümresinin seçtiği senaryo tablosu
- İsterseniz kaynak kitabın içindekiler sayfası

**Siz alırsınız:**

- Haftalık takvim tablosu
- Her derste çıktı kodu ve bileşenler
- Kitap sayfası ve ödev sayfaları
- Kapsama özeti

**Örnek istem:**

```
2. yazılıya 8 hafta var, haftada bir ders yapıyorum. Ekteki senaryoya göre konuları dağıt; son ders tekrar olsun.
```

**Kontrol edin:** Ödev sayfalarının içindekiler sayfasıyla aynı olduğunu bir kez gözle kontrol edin.

**Uyduğu MEB kuralları:**

- MEV-14: Okul sınavları konu soru dağılım tablosuna göre hazırlanır. Tabloyu il sınıf/alan zümreleri senaryolu olarak hazırlar; okul zümresi senaryoyu seçer; soru sayısı seçilen senaryoya uyar. Ülke geneli sınavın tablosunu Genel Müdürlük hazırlar ve örnek tablolar yayımlar.
- MEV-15: Bir dönemde her dersten iki yazılı yapılır (haftada 6 saat ve üstü derslerde il zümresi kararıyla üçüncü).

**Sonra:** [Konu özeti](#maarif-konu-ozeti)

### Ders planı
<a id="maarif-ders-plani"></a>`maarif-ders-plani`

Bir çıktı için ders planı, öğrenci çalışma kâğıdı ve gözlem formunu birlikte hazırlar.

**Ne zaman kullanılır?**

- Yeni bir dersi sıfırdan planlarken
- Mini ders ya da etkinlik planı için

**Siz verin:**

- Sınıf
- Çıktı kodu ya da konu
- İsterseniz süre ve sınıf mevcudu

**Siz alırsınız:**

- Ön değerlendirme, köprü kurma, keşfet, tartış, genelle ve çıkış kartından oluşan akış
- Bileşen kapsama tablosu
- Çalışma kâğıdı ve gözlem formu

**Örnek istem:**

```
Yarın 6. sınıfa ortak katları anlatacağım; 40 dakikalık ders planı, çalışma kâğıdı ve gözlem formu hazırla.
```

**Kontrol edin:** Çıkış kartının dersin en zor durumunu yokladığını ve üç grup ölçütünü okuyun.

**Uyduğu MEB kuralları:**

- MEV-03: Değerlendirme süreç odaklıdır: öğrencinin başlangıç ve son düzeyi karşılaştırılır, gelişim aralıklarla izlenir, öğrenciye ve veliye geri bildirim verilir. Ölçme yalnız not vermek değil, geri bildirim vermektir.

**Sonra:** [Derse hazırlık](#maarif-derse-hazirlik)

### Derse hazırlık
<a id="maarif-derse-hazirlik"></a>`maarif-derse-hazirlik`

Var olan bir derse sizinle birlikte hazırlanır ve kısa bir hazırlık notu bırakır.

**Ne zaman kullanılır?**

- Dersten bir gün önce
- İlk kez anlatacağınız bir etkinlikte

**Siz verin:**

- Ders planı ya da kitap sayfası

**Siz alırsınız:**

- Kilit görev üzerine birlikte düşünme
- Neredeyse doğru öğrenci cevapları
- 200–300 sözcüklük hazırlık notu

**Örnek istem:**

```
Ekteki planla yarınki derse hazırlanmama yardım et; kilit görevi önce ben çözeyim.
```

**Kontrol edin:** Hazırlık notunu dersin bölümlerine göre okuyun; değişmesi gereken yeri söyleyin.

**Sonra:** [Anlama kontrolü](#maarif-anlama-kontrolu)

### Farklılaştırma
<a id="maarif-farklilastirma"></a>`maarif-farklilastirma`

Var olan bir dersi destekleme, temel ve zenginleştirme için üç gruba uyarlar.

**Ne zaman kullanılır?**

- Ön değerlendirmeden sonra
- Sınıfta farklı hazırbulunuşluk varken
- BEP hedefi olan öğrenci için

**Siz verin:**

- Ders planı ya da çalışma kâğıdı
- İsterseniz gözlediğiniz durum ya da BEP hedefi

**Siz alırsınız:**

- Öğretmen farklılaştırma planı
- A B C çalışma kâğıtları
- Her grupta aynı çıktı ve aynı zor durum

**Örnek istem:**

```
Ekteki dersi farklılaştır; kesirleri modelle göremeyen öğrenciler için destek ekle.
```

**Kontrol edin:** Öğrenci kâğıtlarında düzey adı yazmadığını kontrol edin.

**Uyduğu MEB kuralları:**

- MEV-04: Kaynaştırma ya da bütünleştirme yoluyla eğitim gören öğrencilerde ölçme ve değerlendirmenin temeli BEP'tir; ölçme araçları BEP'e göre hazırlanır, gerekirse farklı soru tipleri kullanılır.

**Sonra:** [Anlama kontrolü](#maarif-anlama-kontrolu)

### Anlama kontrolü
<a id="maarif-anlama-kontrolu"></a>`maarif-anlama-kontrolu`

Tek bir bileşen için 1–3 maddelik notsuz kontrol ve cevapları okuma kılavuzu hazırlar.

**Ne zaman kullanılır?**

- Ders sonunda çıkış kartı olarak
- Yeni konuya geçmeden ön değerlendirme olarak
- Kısa süreli sınav yerine

**Siz verin:**

- Sınıf
- Konu ya da çıktı kodu

**Siz alırsınız:**

- Öğrenci kâğıdı
- Her cevabın neyi gösterdiği
- Sonraki öğretim adımı

**Örnek istem:**

```
6. sınıf ondalık gösterim için ders sonu çıkış kartı hazırla; cevapları okuma kılavuzu da olsun.
```

**Kontrol edin:** Skill odak bileşeni önce size sorar; onayladığınız bileşenin doğru olduğundan emin olun.

**Uyduğu MEB kuralları:**

- MEV-40: Ortaokul ve lisede ünite, tema ya da konu sonunda veya kritik çıktılar için kısa süreli sınav yapılabilir: birkaç soru, kısa süre, anında geri bildirim. Not ya da puanla değerlendirilmez; farklı soru türleri kullanılabilir; değerlendirme değil, pekiştirme etkinliğidir.
- MEV-41: İlkokulda kısa süreli, hazırbulunuşluk, deneme ve tarama sınavı dâhil hiçbir adla sınav yapılmaz; süreç odaklı değerlendirme araçlarında çoktan seçmeli soru kullanılmaz. Gelişim değerlendirme formu, kontrol listesi ve dereceleme ölçeğiyle izlenir; araçlar öğrenci gelişim dosyasında tutulur.

**Sonra:** [Hata analizi](#maarif-hata-analizi)

### Kavrama testi
<a id="maarif-kavrama-testi"></a>`maarif-kavrama-testi`

Haftanın konusunu 4–5 soruyla ölçer; ödevi yalnız takılan bileşenlere verir.

**Ne zaman kullanılır?**

- Haftalık konu bittikten sonra
- Ödevi azaltmak istediğinizde
- Koçlukta haftalık izlemede

**Siz verin:**

- Haftanın konusu ya da çıktısı
- Sonuç geldiğinde öğrencilerin cevapları

**Siz alırsınız:**

- Cevap ve gerekçe isteyen 4–5 soruluk kâğıt
- Öğretmen anahtarı ve karar tablosu
- Öğrenci başına geçti / kısa telafi / yeniden ele al kararı
- En çok 6 soruluk hedefli ödev

**Örnek istem:**

```
6. sınıfta bu hafta ortak kat ve ortak böleni bitirdik; en az soruyla kavrama testi hazırla.
```

**Kontrol edin:** Öğrenci sonuçlarını takma adla girin; karar ve ödev betikle hesaplanır.

**Uyduğu MEB kuralları:**

- MEV-40: Ortaokul ve lisede ünite, tema ya da konu sonunda veya kritik çıktılar için kısa süreli sınav yapılabilir: birkaç soru, kısa süre, anında geri bildirim. Not ya da puanla değerlendirilmez; farklı soru türleri kullanılabilir; değerlendirme değil, pekiştirme etkinliğidir.
- MEV-41: İlkokulda kısa süreli, hazırbulunuşluk, deneme ve tarama sınavı dâhil hiçbir adla sınav yapılmaz; süreç odaklı değerlendirme araçlarında çoktan seçmeli soru kullanılmaz. Gelişim değerlendirme formu, kontrol listesi ve dereceleme ölçeğiyle izlenir; araçlar öğrenci gelişim dosyasında tutulur.

**Sonra:** [Hızlı tekrar](#maarif-hizli-tekrar)

### Hızlı tekrar
<a id="maarif-hizli-tekrar"></a>`maarif-hizli-tekrar`

Ders başı 5 dakikalık soru-cevap turu ve denetlenmiş haftanın sloganını hazırlar.

**Ne zaman kullanılır?**

- Her dersin ilk 5 dakikasında
- Önceki haftaları unutturmamak için
- Grup dersinde kısa yarışma olarak

**Siz verin:**

- Bu hafta işlenen konu
- İsterseniz kavrama testi geçmişi

**Siz alırsınız:**

- 8 soruluk karışık tur (geçen hafta ve öncesi)
- Cevap ekranları ve öğretmen listesi
- Karşı örnekle sınanmış slogan ve neden sorusu

**Örnek istem:**

```
Geçen hafta ortak katı işledik; ders başı için hızlı tekrar turu ve haftanın sloganını hazırla.
```

**Kontrol edin:** Sloganın sınırını ve karşı örneğini okuyun; slogan kuralın yerine geçmez, onu hatırlatır.

**Uyduğu MEB kuralları:**

- MEV-40: Ortaokul ve lisede ünite, tema ya da konu sonunda veya kritik çıktılar için kısa süreli sınav yapılabilir: birkaç soru, kısa süre, anında geri bildirim. Not ya da puanla değerlendirilmez; farklı soru türleri kullanılabilir; değerlendirme değil, pekiştirme etkinliğidir.

**Sonra:** [Kavrama testi](#maarif-kavrama-testi)

### Ortak yazılı
<a id="maarif-ortak-yazili"></a>`maarif-ortak-yazili`

Seçilen senaryoya uyan açık uçlu yazılı kâğıtlarını ve cevap anahtarlarını hazırlar.

**Ne zaman kullanılır?**

- Okul geneli ortak yazılıdan önce
- Yazılı provası için

**Siz verin:**

- Okul zümresinin seçtiği senaryo tablosu
- Sınıf ve dönem

**Siz alırsınız:**

- Kâğıt seti ve kapsama planı
- Adım puanlı cevap anahtarı ve öğretmen notları
- Kapsama tablosu

**Örnek istem:**

```
Ekteki senaryoya göre 9. sınıf 1. dönem 2. yazılı kâğıtlarını ve cevap anahtarlarını hazırla.
```

**Kontrol edin:** Kâğıtların bir ders saatine sığdığını ve cevap alanlarının yeterli olduğunu kontrol edin.

**Uyduğu MEB kuralları:**

- MEV-10: Okul sınavları, cevabını öğrencinin oluşturduğu ve farklı bilişsel düzeydeki çıktıları ölçen maddelerden oluşan yazılı yoklamadır. Açık uçlu soru esastır.
- MEV-11: Çıktının özelliğine ve bilişsel düzeyine göre kısa cevaplı soru da kullanılabilir; ama yalnız kısa cevaplı sorulardan oluşan yazılı yapılamaz.
- MEV-12: Okul yazılısında cevabı yalnız işaretlemeye dayanan maddeler (çoktan seçmeli, gerekçesiz doğru-yanlış, gerekçesiz eşleştirme) kullanılmaz, çünkü cevabı öğrenci oluşturmaz. Doğru-yanlış ya da eşleştirme ancak öğrenci kararının gerekçesini yazıyorsa açık uçlu madde sayılır (MEB örnek yazılılarındaki "doğru ya da yanlış olma nedenleri" gibi). Yabancı dilde, eşleştirme olmayacak biçimde verilenler arasından seçilen boşluk doldurma kullanılabilir.
- MEV-13: Soru, ölçtüğü çıktının bilişsel düzeyindedir: çözümleme ya da değerlendirme düzeyindeki bir çıktı, aynı düzeyde soru gerektirir.
- MEV-14: Okul sınavları konu soru dağılım tablosuna göre hazırlanır. Tabloyu il sınıf/alan zümreleri senaryolu olarak hazırlar; okul zümresi senaryoyu seçer; soru sayısı seçilen senaryoya uyar. Ülke geneli sınavın tablosunu Genel Müdürlük hazırlar ve örnek tablolar yayımlar.
- MEV-16: Yazılı sınavın süresi, zorunlu hâller dışında bir ders saatini geçemez. Kâğıt bu süreye sığacak uzunluktadır.
- MEV-17: Sınav kâğıdında öğrencinin cevabı için yeterli alan bırakılır.
- MEV-19: Sınavlar 100 tam puan üzerinden değerlendirilir; yanlış cevaplar doğru cevapları etkilemez (götürü yoktur).
- MEV-30: Puanlanan cevap kâğıtları öğrencilere gösterilir; kâğıtta eksik ya da yanlış öğrenmelere yönelik öğretmen notları bulunur.

**Sonra:** [Hata analizi](#maarif-hata-analizi)

### Beceri temelli test
<a id="maarif-beceri-temelli-test"></a>`maarif-beceri-temelli-test`

LGS ve TYT tarzı, bağlamlı ve görselli çoktan seçmeli test hazırlar.

**Ne zaman kullanılır?**

- LGS ya da TYT hazırlığında
- Tarama testi olarak

**Siz verin:**

- Sınıf
- Konu ya da çıktılar
- Soru sayısı

**Siz alırsınız:**

- Test kâğıdı
- Çeldirici açıklamalı cevap anahtarı
- Güçlük dağılımı

**Örnek istem:**

```
8. sınıf üslü ifadeler için 15 soruluk LGS tarzı tarama testi hazırla.
```

**Kontrol edin:** Bu test okul yazılısı yerine kullanılmaz; okul yazılısı için ortak yazılı skill'ini kullanın.

**Uyduğu MEB kuralları:**

- MEV-12: Okul yazılısında cevabı yalnız işaretlemeye dayanan maddeler (çoktan seçmeli, gerekçesiz doğru-yanlış, gerekçesiz eşleştirme) kullanılmaz, çünkü cevabı öğrenci oluşturmaz. Doğru-yanlış ya da eşleştirme ancak öğrenci kararının gerekçesini yazıyorsa açık uçlu madde sayılır (MEB örnek yazılılarındaki "doğru ya da yanlış olma nedenleri" gibi). Yabancı dilde, eşleştirme olmayacak biçimde verilenler arasından seçilen boşluk doldurma kullanılabilir.
- MEV-40: Ortaokul ve lisede ünite, tema ya da konu sonunda veya kritik çıktılar için kısa süreli sınav yapılabilir: birkaç soru, kısa süre, anında geri bildirim. Not ya da puanla değerlendirilmez; farklı soru türleri kullanılabilir; değerlendirme değil, pekiştirme etkinliğidir.
- MEV-41: İlkokulda kısa süreli, hazırbulunuşluk, deneme ve tarama sınavı dâhil hiçbir adla sınav yapılmaz; süreç odaklı değerlendirme araçlarında çoktan seçmeli soru kullanılmaz. Gelişim değerlendirme formu, kontrol listesi ve dereceleme ölçeğiyle izlenir; araçlar öğrenci gelişim dosyasında tutulur.

**Sonra:** [Hata analizi](#maarif-hata-analizi)

### Performans görevi
<a id="maarif-performans-gorevi"></a>`maarif-performans-gorevi`

Yazılıda ölçülemeyen bileşenler için görev, dereceli puanlama anahtarı ve formlar hazırlar.

**Ne zaman kullanılır?**

- Veri toplama ya da araştırma gerektiren çıktılarda
- Proje ödevi için

**Siz verin:**

- Sınıf
- Çıktı ya da tema
- İsterseniz süre ve bireysel ya da grup

**Siz alırsınız:**

- Öğrenci görev kâğıdı
- Dereceli puanlama anahtarı
- Puansız gözlem formu
- Öz ve akran değerlendirme formu

**Örnek istem:**

```
6. sınıf olasılık çıktısı için iki haftalık bir deney görevi ve dereceli puanlama anahtarı hazırla.
```

**Kontrol edin:** Görevin ücret, internet ya da veli emeği gerektirmediğini kontrol edin.

**Uyduğu MEB kuralları:**

- MEV-02: Ölçme araçları geçerli, güvenilir ve kullanışlı olur. Araca göre cevap anahtarı, puanlama anahtarı, derecelendirme ölçeği ya da kontrol listesi kullanılır.
- MEV-51: Uzun süreli ürün ve süreç değerlendirmesinde araca uygun puanlama aracı kullanılır: dereceli puanlama anahtarı, derecelendirme ölçeği ya da kontrol listesi (MEV-02). Kitapçıkta performans görevi ve projeye ayrı madde yoktur; o yılın Bakanlık duyurusu esas alınır.

**Sonra:** [Hata analizi](#maarif-hata-analizi)

### İkiz soru
<a id="maarif-benzer-soru"></a>`maarif-benzer-soru`

Verdiğiniz soruların aynı bileşeni ölçen özgün ikizlerini yazar.

**Ne zaman kullanılır?**

- Öğrencinin yanlış yaptığı sorular için
- Paralel kâğıt ya da ek alıştırma için

**Siz verin:**

- Kaynak sorular (PDF ya da fotoğraf)
- Kaç ikiz istediğiniz

**Siz alırsınız:**

- İkiz sorular
- Cevap anahtarı
- Adım adım çözümler

**Örnek istem:**

```
Ekteki 5 sorunun her biri için aynı bileşeni ölçen birer ikiz soru ve çözüm yaz.
```

**Kontrol edin:** İkizler okul yazılısında kullanılacaksa bunu belirtin; çoktan seçmeliler açık uçluya çevrilir.

**Uyduğu MEB kuralları:**

- MEV-12: Okul yazılısında cevabı yalnız işaretlemeye dayanan maddeler (çoktan seçmeli, gerekçesiz doğru-yanlış, gerekçesiz eşleştirme) kullanılmaz, çünkü cevabı öğrenci oluşturmaz. Doğru-yanlış ya da eşleştirme ancak öğrenci kararının gerekçesini yazıyorsa açık uçlu madde sayılır (MEB örnek yazılılarındaki "doğru ya da yanlış olma nedenleri" gibi). Yabancı dilde, eşleştirme olmayacak biçimde verilenler arasından seçilen boşluk doldurma kullanılabilir.
- MEV-60: Merkezî ve ortak sınavlarda kullanılan soruları izinsiz çoğaltmak, yayımlamak ya da kullanmak yasaktır (5846 sayılı Fikir ve Sanat Eserleri Kanunu). Bu sorular model alınır; birebir kullanılmaz.

**Sonra:** [Hata analizi](#maarif-hata-analizi)

### Hata analizi
<a id="maarif-hata-analizi"></a>`maarif-hata-analizi`

Yanlışları bileşene ve hata türüne göre ayırır, telafi planı ve tekrar takvimi hazırlar.

**Ne zaman kullanılır?**

- Yazılı ya da deneme sonrasında
- Koçluk görüşmesinden önce

**Siz verin:**

- Yanlış yapılan sorular ve öğrenci cevapları
- İsterseniz çözüm kâğıdı fotoğrafı ya da sonuç tablosu

**Siz alırsınız:**

- Öğretmen raporu
- Öğrenci telafi çalışma sayfası
- Tekrar takvimi
- İsteğe bağlı veli özeti

**Örnek istem:**

```
Ekteki deneme sonucuna göre hata analizi yap; telafi planı ve kontrol soruları hazırla.
```

**Kontrol edin:** Raporda gerçek ad kullanılmaz; öğrencileri takma adla tanırsınız.

**Uyduğu MEB kuralları:**

- MEV-30: Puanlanan cevap kâğıtları öğrencilere gösterilir; kâğıtta eksik ya da yanlış öğrenmelere yönelik öğretmen notları bulunur.
- MEV-31: Her sınavdan sonra öğretmen cevapları analiz eder, hangi çıktıda eksik ya da yanlış öğrenme olduğunu belirler, öğrenciye bireysel geri bildirim verir ve gerekirse telafi yapar.
- MEV-32: Öğretmenin analizi kendi kullanımı içindir; okul idaresine ayrıca rapor verilerek evrak yükü oluşturulmaz.
- MEV-33: Ortak sınav sonuçlarından öğrenci toplu listesi, okullar ya da sınıflar arası karşılaştırmalı veri yayımlanmaz; öğrenci adlı reklam listesi yapılmaz.

**Sonra:** [İkiz soru](#maarif-benzer-soru)

### Konu özeti
<a id="maarif-konu-ozeti"></a>`maarif-konu-ozeti`

Haftalık ders paketini hazırlar - ısınma turu, konu özeti slaytları, slogan, kavrama testi ve sonuca bağlı ödev.

**Ne zaman kullanılır?**

- Haftalık özel derste
- Yazılıya kadar konu tekrarında

**Siz verin:**

- Ders kitabı
- İsterseniz takvim ve kaynak kitabın içindekiler sayfası

**Siz alırsınız:**

- Ders başı ısınma turu (aralıklı tekrar)
- Konu kartları ve yazılı tarzı sorular
- Haftanın sloganı
- 4 soruluk kavrama testi (slayt ve A4 kâğıt)
- Kavrama testine bağlı ödev kartı
- Öğretmen çözüm dosyası

**Örnek istem:**

```
Ekteki ders kitabına ve haftalık plana göre 9. sınıf ders anlatım sunumunu hazırla.
```

**Kontrol edin:** Yalnız özet istediğiniz hafta "yalnız özet" deyin; ısınma ve kavrama testi atlanır.

**Uyduğu MEB kuralları:**

- MEV-10: Okul sınavları, cevabını öğrencinin oluşturduğu ve farklı bilişsel düzeydeki çıktıları ölçen maddelerden oluşan yazılı yoklamadır. Açık uçlu soru esastır.
- MEV-13: Soru, ölçtüğü çıktının bilişsel düzeyindedir: çözümleme ya da değerlendirme düzeyindeki bir çıktı, aynı düzeyde soru gerektirir.

**Sonra:** [Anlama kontrolü](#maarif-anlama-kontrolu)

### Anlatım videosu
<a id="maarif-anlatim-videosu"></a>`maarif-anlatim-videosu`

Bir konu ya da soru için sahne planı, seslendirme metni ve Remotion kodu hazırlar.

**Ne zaman kullanılır?**

- Kısa ders videosu ya da soru çözümü için

**Siz verin:**

- Konu ya da soru
- Biçim (dikey ya da yatay)

**Siz alırsınız:**

- Sahne planı
- Seslendirme metni
- Remotion kodu ve son kare görüntüleri

**Örnek istem:**

```
Ortak kat için 45 saniyelik dikey anlatım videosu hazırla.
```

**Kontrol edin:** Seslendirmedeki sayıların ekrandakiyle aynı olduğunu dinleyerek kontrol edin.

**Sonra:** [Instagram karuseli](#dnamathos-instagram-karusel)

### DNAMATHOS PDF
<a id="dnamathos-pdf-tasarimi"></a>`dnamathos-pdf-tasarimi`

İçeriği DNAMATHOS'un 16:9 PDF tasarımına dönüştürür ve dosyayı denetler.

**Ne zaman kullanılır?**

- Konu özeti
- yazılı ya da test DNAMATHOS görünümünde istendiğinde

**Siz verin:**

- İçerik (öteki skill'lerin ürünü)

**Siz alırsınız:**

- PDF
- Taşma ve bağlantı denetimi
- Slayt görüntüleri

**Örnek istem:**

```
Bu içeriği DNAMATHOS 16:9 düzeninde PDF'e çevir ve bağlantıları denetle.
```

**Kontrol edin:** Birbirine bağlanan PDF'leri aynı klasörde tutun.

**Sonra:** [Instagram karuseli](#dnamathos-instagram-karusel)

### Instagram karuseli
<a id="dnamathos-instagram-karusel"></a>`dnamathos-instagram-karusel`

Konu karuseli, rehberlik ve gerçek hayat gönderisinden oluşan ızgara satırını hazırlar.

**Ne zaman kullanılır?**

- Haftalık sosyal medya içeriğinde

**Siz verin:**

- Sınıf ve konu
- İsterseniz çıktı kodu

**Siz alırsınız:**

- 1080 × 1350 PNG slaytlar
- Açıklama ve etiketler
- Paylaşım sırası

**Örnek istem:**

```
8. sınıf üslü ifadeler için konu karuseli, rehberlik ve gerçek hayat gönderilerinden oluşan satırı hazırla.
```

**Kontrol edin:** Paylaşırken sırayı izleyin - önce karusel, sonra rehberlik, en son gerçek hayat.

**Sonra:** [Anlatım videosu](#maarif-anlatim-videosu)

## İş akışları

### Yazılıya 8 hafta kala

1. `maarif-cikti-cozumleme` — senaryodaki çıktıların kartı ("Ekteki senaryodaki çıktıların kartını çıkar.")
2. `maarif-ders-takvimi` — 8 derslik takvim, son ders tekrar ve prova
3. `maarif-konu-ozeti` — her hafta o haftanın konu özeti ve ödev kartı
4. `maarif-anlama-kontrolu` — her dersin sonunda bir çıkış kartı
5. `maarif-ortak-yazili` — 7. hafta: senaryoya uyan prova kâğıtları
6. `maarif-hata-analizi` — prova sonuçlarına göre telafi planı
7. `maarif-benzer-soru` — en sık iki hata örüntüsü için ikiz soru seti

### Haftalık döngü (az ödev, kalıcı öğrenme)

1. `maarif-hizli-tekrar` — dersin ilk 5 dakikası: geçen hafta ve öncesinden karışık 6–8 soru, haftanın sloganı
2. `maarif-konu-ozeti` ya da `maarif-ders-plani` — haftanın konusu
3. `maarif-kavrama-testi` — konu bitince 4 soruluk notsuz test
4. Sonuçlar girilince (`kavrama_karari.py`) — öğrenci başına karar ve en çok 6 soruluk hedefli ödev
5. Sonraki hafta — takılan bileşenler ısınma turunun başına gelir

### Yeni bir temaya başlarken

1. `maarif-cikti-cozumleme` — tema kartı (temel kabuller, ön değerlendirme, köprü kurma)
2. `maarif-anlama-kontrolu` — ön değerlendirme kontrolü (ön koşul bileşeni)
3. `maarif-ders-plani` — ilk dersin paketi
4. `maarif-farklilastirma` — ön değerlendirme sonucuna göre üç grup
5. `maarif-derse-hazirlik` — dersten bir gün önce

### Dönem içi süreç değerlendirmesi

1. `maarif-performans-gorevi` — yazılı dışı bileşenler için görev ve dereceli anahtar
2. `maarif-anlama-kontrolu` — ara teslimlerde kısa kontroller
3. `maarif-hata-analizi` — sınıf düzeyi rapor ve destekleme grubu

### DNAMATHOS haftalık üretim

1. `maarif-konu-ozeti` + `dnamathos-pdf-tasarimi` — haftanın ders PDF'leri
2. `dnamathos-instagram-karusel` — aynı konunun ızgara satırı
3. `maarif-anlatim-videosu` — satırın konusu için Shorts

## MEB ölçme kuralları (özet)

Tam tablo ve dayanaklar: `ortak/maarif/meb-olcme-mevzuati.md`.

| Kod | Kural |
| --- | --- |
| MEV-01 | Başarı, programdaki çıktılara dayanan ve dersin yapısına uygun ölçmelerle belirlenir. Ölçme şekli çıktının özelliğine göre seçilir; bütün çıktılar planlı bir izlemeyle ölçülür. |
| MEV-02 | Ölçme araçları geçerli, güvenilir ve kullanışlı olur. Araca göre **cevap anahtarı, puanlama anahtarı, derecelendirme ölçeği ya da kontrol listesi** kullanılır. |
| MEV-03 | Değerlendirme süreç odaklıdır: öğrencinin başlangıç ve son düzeyi karşılaştırılır, gelişim aralıklarla izlenir, öğrenciye ve veliye geri bildirim verilir. Ölçme yalnız not vermek değil, geri bildirim vermektir. |
| MEV-04 | Kaynaştırma ya da bütünleştirme yoluyla eğitim gören öğrencilerde ölçme ve değerlendirmenin temeli **BEP**'tir; ölçme araçları BEP'e göre hazırlanır, gerekirse farklı soru tipleri kullanılır. |
| MEV-05 | Sınav ve ölçme işleri güvenirlik, gizlilik ve tarafsızlık ilkeleriyle yürütülür. |
| MEV-10 | Okul sınavları, cevabını **öğrencinin oluşturduğu** ve farklı bilişsel düzeydeki çıktıları ölçen maddelerden oluşan yazılı yoklamadır. **Açık uçlu soru esastır.** |
| MEV-11 | Çıktının özelliğine ve bilişsel düzeyine göre **kısa cevaplı** soru da kullanılabilir; ama **yalnız kısa cevaplı sorulardan oluşan yazılı yapılamaz.** |
| MEV-12 | Okul yazılısında cevabı **yalnız işaretlemeye** dayanan maddeler (çoktan seçmeli, gerekçesiz doğru-yanlış, gerekçesiz eşleştirme) kullanılmaz, çünkü cevabı öğrenci oluşturmaz. Doğru-yanlış ya da eşleştirme ancak öğrenci kararının **gerekçesini yazıyorsa** açık uçlu madde sayılır (MEB örnek yazılılarındaki "doğru ya da yanlış olma nedenleri" gibi). Yabancı dilde, eşleştirme olmayacak biçimde verilenler arasından seçilen boşluk doldurma kullanılabilir. |
| MEV-13 | Soru, ölçtüğü çıktının **bilişsel düzeyindedir**: çözümleme ya da değerlendirme düzeyindeki bir çıktı, aynı düzeyde soru gerektirir. |
| MEV-14 | Okul sınavları **konu soru dağılım tablosuna** göre hazırlanır. Tabloyu il sınıf/alan zümreleri senaryolu olarak hazırlar; okul zümresi senaryoyu seçer; **soru sayısı seçilen senaryoya uyar.** Ülke geneli sınavın tablosunu Genel Müdürlük hazırlar ve örnek tablolar yayımlar. |
| MEV-15 | Bir dönemde her dersten **iki yazılı** yapılır (haftada 6 saat ve üstü derslerde il zümresi kararıyla üçüncü). |
| MEV-16 | Yazılı sınavın süresi, zorunlu hâller dışında **bir ders saatini geçemez.** Kâğıt bu süreye sığacak uzunluktadır. |
| MEV-17 | Sınav kâğıdında **öğrencinin cevabı için yeterli alan** bırakılır. |
| MEV-18 | Sınav kâğıdında **kazanım (çıktı) ifadesine yer verilmesi gerekmez.** |
| MEV-19 | Sınavlar **100 tam puan** üzerinden değerlendirilir; **yanlış cevaplar doğru cevapları etkilemez** (götürü yoktur). |
| MEV-20 | İptal edilen soru değerlendirme dışı kalır; kalan soruların puanları yeniden belirlenir. |
| MEV-21 | Okul geneli sınavın sorularını ve cevaplarını eğitim kurumu sınıf/alan zümresi hazırlar; puanlamayı zümre yapar. Ülke, il ve ilçe geneli sınavların soruları ilgili kurumlarca hazırlanır. |
| MEV-22 | Türkçe ve yabancı dilde sınav yazılı ve uygulamalı iki aşamadır: yazılı %50, dinleme %25, konuşma %25 (Türk dili ve edebiyatında %70, %15, %15). |
| MEV-30 | Puanlanan cevap kâğıtları öğrencilere gösterilir; kâğıtta eksik ya da yanlış öğrenmelere yönelik **öğretmen notları** bulunur. |
| MEV-31 | Her sınavdan sonra öğretmen cevapları analiz eder, hangi çıktıda eksik ya da yanlış öğrenme olduğunu belirler, öğrenciye **bireysel geri bildirim** verir ve gerekirse **telafi** yapar. |
| MEV-32 | Öğretmenin analizi kendi kullanımı içindir; okul idaresine ayrıca rapor verilerek evrak yükü oluşturulmaz. |
| MEV-33 | Ortak sınav sonuçlarından **öğrenci toplu listesi, okullar ya da sınıflar arası karşılaştırmalı veri** yayımlanmaz; öğrenci adlı reklam listesi yapılmaz. |
| MEV-34 | Analizler şube ve sınıf bazında yapılır; eksiklik görülen öğrenciler için zümre iyileştirici önlem alır. |
| MEV-40 | Ortaokul ve lisede ünite, tema ya da konu sonunda veya kritik çıktılar için **kısa süreli sınav** yapılabilir: birkaç soru, kısa süre, anında geri bildirim. **Not ya da puanla değerlendirilmez**; farklı soru türleri kullanılabilir; değerlendirme değil, pekiştirme etkinliğidir. |
| MEV-41 | **İlkokulda** kısa süreli, hazırbulunuşluk, deneme ve tarama sınavı dâhil **hiçbir adla sınav yapılmaz**; süreç odaklı değerlendirme araçlarında **çoktan seçmeli soru kullanılmaz**. Gelişim değerlendirme formu, kontrol listesi ve dereceleme ölçeğiyle izlenir; araçlar öğrenci gelişim dosyasında tutulur. |
| MEV-50 | Uygulamalı sınavların biçimi, sayısı ve süresi zümrece belirlenir; bütün şubelerde aynı çıktı ve becerilerden yapılır. |
| MEV-51 | Uzun süreli ürün ve süreç değerlendirmesinde araca uygun puanlama aracı kullanılır: dereceli puanlama anahtarı, derecelendirme ölçeği ya da kontrol listesi (MEV-02). Kitapçıkta performans görevi ve projeye ayrı madde yoktur; o yılın Bakanlık duyurusu esas alınır. |
| MEV-60 | Merkezî ve ortak sınavlarda kullanılan soruları izinsiz çoğaltmak, yayımlamak ya da kullanmak yasaktır (5846 sayılı Fikir ve Sanat Eserleri Kanunu). Bu sorular model alınır; birebir kullanılmaz. |

## Sık sorulanlar

**Skill'ler başka derslerde çalışır mı?**

Bütün skill'ler Maarif omurgasıyla çalışır; ayrıntılı ders dosyası şu an matematik için hazır. Başka derslerde skill programı doğrudan tema sayfasından okur ve bunu ürünün sonunda belirtir.

**TYMM sayfası açılmazsa ne olur?**

Skill, verdiğiniz çıktı metniyle çalışır ve ürüne "program sayfasından doğrulanamadı" notunu ekler. Kod ya da kaynak uydurmaz.

**Çoktan seçmeli test yazılı yerine kullanılabilir mi?**

Hayır. MEB mevzuatına göre okul yazılıları açık uçludur ve cevabı öğrenci oluşturur. Çoktan seçmeli test LGS hazırlığı, tarama ya da notsuz kısa süreli sınav içindir.

**Haftalık ödevi nasıl azaltırım?**

Konu bitince kavrama testi yapın. Bileşeni geçen öğrenciye o konudan ödev verilmez; takılan öğrenciye yalnız takıldığı bileşen için 2–3 hedefli soru verilir. Haftalık üst sınır 6 sorudur.

**Öğrenci adlarını vermeli miyim?**

Gerek yok. Skill'ler öğrencileri takma adla işler; sınıflar ya da öğrenciler arası sıralama üretmez.

**Ürünü doğrudan sınıfa götürebilir miyim?**

Ürünler denetlenmiş olarak gelir, ama son kontrol sizindir. Sorunu bulduğunuz yeri söylerseniz skill yalnız o kısmı düzeltir.
