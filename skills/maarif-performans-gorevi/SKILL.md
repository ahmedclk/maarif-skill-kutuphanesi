---
name: maarif-performans-gorevi
description: Maarif Modeli çıktılarına bağlı performans görevi ya da proje görevi hazırlar; yazılıda ölçülemeyen süreç bileşenlerini (veri toplama, araştırma planı, ürün oluşturma, sunum) gerçek bir bağlamda öğrenci görev kâğıdına, süreç takvimine ve bileşen satırlı dereceli puanlama anahtarına dönüştürür; eğilim, SDB ve değerleri puansız gözlem formunda izler. Tetikleyiciler - performans görevi hazırla, proje ödevi, dereceli puanlama anahtarı, rubrik, ürün dosyası değerlendirme ölçütü, veri toplama projesi, öz ve akran değerlendirme formu. Yazılı sınav için değil (maarif-ortak-yazili), çoktan seçmeli test için değil (maarif-beceri-temelli-test), 1–3 maddelik anlama kontrolü için değil (maarif-anlama-kontrolu), ders planı için değil (maarif-ders-plani).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: TYMM sayfaları için web erişimi. Belge için Docs artifact türü ya da docx skill'i.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: TYMM Öğrenme Kanıtları (performans görevi) ve süreç odaklı değerlendirme
  dersler: matematik (tam); diğerleri şablonla
---

# Maarif performans görevi

Amaç: Yazılının ölçemediği bileşenleri (MAB4.2 veri toplama planı ve veri toplama, uzun süreli araştırma, model ya da ürün oluşturma, sunum) gerçek bir bağlamda ölçen, öğrencinin baştan neye göre değerlendirileceğini bildiği bir görev. Maarif Modeli'nde bu görev süreç odaklı değerlendirmenin parçasıdır: ürün kadar süreç de izlenir.

Dil ve üslup: `references/ortak/uslup/turkce-yazim.md`, `references/ortak/uslup/onyargisiz-dil.md`. Öğrenci verisi: `references/ortak/guvence/kvkk-ve-telif.md`.

## Adım 0 — Yönlendirme (sessiz)

1. `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`.
2. Ders dosyası: matematik → `references/dersler/matematik.md` (şimdi oku). Yoksa `references/ortak/dersler/_sablon.md`.
3. `references/ortak/maarif/meb-olcme-mevzuati.md`: puanlama aracı ölçme aracına uygun seçilir (MEV-02, MEV-51); ilkokulda görev, notlu sınav gibi sunulmaz ve gelişim derecelendirme ölçeği ya da kontrol listesiyle izlenir (MEV-41); BEP'li öğrenci için ölçütler BEP hedefine göre uyarlanır (MEV-04).

## Adım 1 — Netleştirme (en fazla bir soru)

Çıktı ya da tema belli değilse sor. Varsayılanlar: bireysel görev, 2 hafta, ürün + kısa sunum, 100 puan.

## Adım 2 — Programa dayandır

Tema sayfasının Öğrenme Kanıtları bölümünde performans görevi önerisi varsa oradan başla. Çıktı kartındaki "performansa bırakılır" bileşenleri görevin çekirdeğidir; yazılıda ölçülen bileşenler göreve yalnız destek olarak girer. Temanın E, SDB, D ve OB kodlarından bu görevin doğal olarak taşıdıkları seçilir (en çok üç).

## Adım 3 — Görevi tasarla

Yapı `references/gorev-yapisi.md` dosyasındadır. Değişmez kurallar:

- **Gerçek bağlam ve gerçek kitle:** okulun kantini, mahallenin su tüketimi, sınıfın kitap okuma süresi; ürün birine bir şey söyler (rapor, afiş, öneri mektubu).
- **Ürün ve süreç:** görev bir ürün ve en az iki ara teslim içerir (plan, ham veri, taslak). Ara teslim, sürecin gözlendiği yerdir.
- **Öğrencinin kararı:** görev, öğrencinin kendi sorusunu, yöntemini ya da temsilini seçeceği en az bir karar noktası taşır.
- **Erişilebilirlik:** malzeme okulda ya da evde bulunur; ücret, internet ya da veli emeği gerektirmez. Kişisel veri toplanmaz; anketlerde ad sorulmaz.

## Adım 4 — Dereceli puanlama anahtarı

`references/dereceli-puanlama.md` dosyasını oku. Her satır bir süreç bileşenidir (harfiyle); dört düzey (Başlangıç · Gelişmekte · Yeterli · İleri) gözlenebilir davranışla yazılır; düzeyler arasındaki fark nitelikle anlatılır, "biraz", "çok" gibi niceliklerle değil. E, SDB ve D satırları ayrı bir **puansız gözlem formu**na gider. Öz değerlendirme ve akran değerlendirme formu anahtarın sade dildeki kısa hâlidir.

## Adım 5 — Çıktı

Dört belge: öğrenci görev kâğıdı (bağlam, görev, ürün, takvim, değerlendirme ölçütlerinin öğrenci dilindeki özeti), öğretmen dereceli puanlama anahtarı, puansız gözlem formu, öz ve akran değerlendirme formu. Docs artifact türü listeleniyorsa Docs belgeleri; yoksa docx skill'i.

## Adım 6 — Doğrulama (belgeler yazıldıktan sonra)

- Anahtarın her satırı bir bileşene bağlı; görevin her ara tesliminde en az bir satır gözlenebiliyor.
- Düzey tanımları birbirinden gözlenebilir bir davranışla ayrılıyor (aynı tanım iki düzeyde yok).
- Puanlar toplamı 100; puansız kodlar puana girmemiş.
- Görev kâğıdı, öğrencinin anahtarı görmeden neye göre değerlendirileceğini anlamasına yetiyor.
- `python3 scripts/tymm_kod_denetle.py <anahtar> --veri references/veri` 0 hata.

## Adım 7 — Kapanış

En fazla iki somut seçenek: "Görevi iki kişilik gruplar için uyarlayayım mı?" ya da "Ara teslimler için kısa geri bildirim cümle bankası hazırlayayım mı?"

## Denetim listesi

- [ ] Görev, yazılıda ölçülemeyen bileşenleri çekirdeğe aldı
- [ ] Gerçek bağlam, gerçek kitle, en az iki ara teslim, bir öğrenci kararı
- [ ] Anahtar satırları bileşen harfli; düzeyler nitelikle ayrılıyor
- [ ] E, SDB, D yalnız gözlem formunda ve puansız
- [ ] Kişisel veri ve ücret gerektirmiyor
