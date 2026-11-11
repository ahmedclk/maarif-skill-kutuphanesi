---
name: maarif-ders-plani
description: Bir öğrenme çıktısı için sıfırdan Maarif Modeli'ne uygun ders planı hazırlar; ön değerlendirme ve köprü kurmadan öğrenme-öğretme uygulamalarına, tartışmaya ve çıkış kartına uzanan akışı, öğrenci çalışma kâğıdını ve öğretmen gözlem formunu tek pakette verir. Netleştirici soru sormadan önce yükle. Tetikleyiciler - ders planı hazırla, yarın 6. sınıfa OBEB anlatacağım, bu çıktı için 40 dakikalık ders, günlük plan, etkinlik planı, mini ders. Yeni bir ders farklılaştırılmış materyal de istiyorsa yine tek istektir ve bu skill üretir. Var olan bir dersi uyarlamak için değil (maarif-farklilastirma), derse hazırlanmak için değil (maarif-derse-hazirlik), haftalara dağıtım için değil (maarif-ders-takvimi), slayt özeti için değil (maarif-konu-ozeti), sınav ya da test için değil (maarif-ortak-yazili, maarif-beceri-temelli-test).
license: Apache-2.0. k12-teacher-skills (Copyright 2026 Anthropic, PBC; Copyright 2026 Learning Commons) k12-lesson-plan-creation skill'inden uyarlanmıştır ve değiştirilmiştir. Ayrıntı - LICENSE ve NOTICE.
compatibility: TYMM sayfaları için web erişimi. Belge üretimi için Docs artifact türü ya da docx skill'i.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: Türkiye Yüzyılı Maarif Modeli, tema sayfasındaki Öğrenme-Öğretme Yaşantıları
  dersler: matematik (tam); diğerleri şablonla
  uyarlama: anthropics/k12-teacher-skills k12-lesson-plan-creation (Apache-2.0)
---

# Maarif ders planı

Amaç: Öğretmenin sınıfa götürebileceği, programın Öğrenme-Öğretme Yaşantılarını izleyen bir ders paketi: **ders planı + öğrenci çalışma kâğıdı + gözlem formu**, tek turda ve birbiriyle tutarlı. Her etkinlik bir süreç bileşenine hizmet eder; her bileşen en az bir öğrenci işiyle karşılanır.

Öğretmene giden metin `references/ortak/uslup/onyargisiz-dil.md`, `references/ortak/uslup/turkce-yazim.md` ve `references/ortak/uslup/ilerleme-ve-kapanis.md` kurallarına uyar. Anlatım dili `references/ortak/uslup/ogretmen-uslubu.md` dosyasındadır.

## Adım 0 — Yönlendirme (sessiz)

1. **Omurga:** `references/ortak/maarif/cerceve.md` ve `references/ortak/maarif/tymm-erisim.md` dosyalarını oku.
2. **Ders:** Dersi belirle ve `references/dersler/<ders>.md` dosyasını şimdi oku (matematik → `references/dersler/matematik.md`). Ders dosyasını okumadan plan yazmak kritik hatadır; bu turda ders dosyası skill talimatının parçasıdır. Ders dosyası yoksa `references/ortak/dersler/_sablon.md` başlıklarıyla çalış ve planın sonuna "Bu ders için ayrıntılı ders dosyası henüz yok." notunu ekle.
3. Aynı oturumda bir `cikti.json` (maarif-cikti-cozumleme) ya da takvim satırı (maarif-ders-takvimi) varsa onu kullan.

## Adım 1 — Netleştirme ve taslak teklifi (tek tur)

Ders dosyasındaki önceliğe göre en fazla bir soru sor (çoğunlukla sınıf ya da çıktı). Soruyla birlikte, aynı turda, şu teklif sorulur (soru sayısına girmez):

- "Sınıfa hazır tam paketi mi (ders planı, çalışma kâğıdı, gözlem formu) hazırlayayım, yoksa önce sohbette kısa bir taslak mı görmek istersiniz?" Seçenekler: **Tam paketi hazırla** · **Önce kısa taslak**.

Varsayılan tam pakettir. Varsayılanlar sessizce uygulanır: 40 dakika, sınıf mevcudu 30, ders kitabı yöntemi.

## Adım 2 — Programa dayandır

Tema sayfasından birebir al: çıktı ve bileşenler, İçerik Çerçevesi ve sınırlar, Temel Kabuller, Ön Değerlendirme Süreci, Köprü Kurma, o çıktının Öğrenme-Öğretme Uygulamaları, Farklılaştırma (Zenginleştirme, Destekleme), Öğrenme Kanıtları ve temanın E, SDB, D, OB kodları. Sayfa açılmazsa `tymm-erisim.md` "Bağlantı yoksa" kuralı uygulanır; plana not düşülür, atıf uydurulmaz. Bulguları sohbette özetleme; doğrudan Adım 3'e geç.

## Adım 3 — Dersi kur

Akış ve bölüm yapısı ders dosyasındadır. Bütün derslerde değişmeyen iskelet:

| Evre | Programdaki karşılığı | Süre (40 dk) |
| --- | --- | --- |
| Ön değerlendirme | Ön Değerlendirme Süreci, Temel Kabuller | 4 |
| Köprü kurma | Köprü Kurma | 4 |
| Keşfet | Öğrenme-Öğretme Uygulamaları (bileşen sırasıyla) | 14 |
| Tartış | Öğrenciler arası konuşma; E ve SDB davranışları burada | en az 10 |
| Genelle | Genelleme ya da önerme; Kaydet özeti | 4 |
| Çıkış kartı | Öğrenme Kanıtları | 4 |

Değişmez kurallar:

- **Bileşen kapsaması:** Her süreç bileşeni ya numaralı bir öğrenci işinde ya da çıkış kartında karşılanır; yalnız öğretmen notunda geçen bileşen karşılanmış sayılmaz. Hangi işin hangi bileşeni taşıdığı planda bir kez tablo olarak yazılır. Performansa bırakılan bileşen "bu derste değil" diye gösterilir.
- **Yapısal durumlar:** Çalışma kâğıdı, çıktının en kolay durumundan yapısal olarak en zor durumuna kadar uzanır (ders dosyasında listelenir); zor durum isteğe bağlı ek soruya bırakılmaz.
- **Çıkış kartı en zor durumdur:** Dersin birincil kavram yanılgısını taşıyan öğrenci çıkış kartını yanlış yapmalıdır; yapmıyorsa kart değiştirilir. Üç grup ölçütü yazılır: "Tamam", "Neredeyse", "Yeniden ele alınmalı"; her birinin cevapta neyi içerdiği açıkça.
- **Programlar arası bileşenler:** Yalnız tema listesindeki E, SDB, D, OB kodları, uygulamadaki davranışla birlikte ve puansız olarak gözlem formuna girer.
- **Farklılaştırma:** Programın Zenginleştirme ve Destekleme önerileri planın sonunda iki kısa kutuda; destek zihinsel zorluğu düşürmez (`maarif-farklilastirma` ilkeleri).
- **Telif:** Ders kitabı ve yayınevi metni model olarak kullanılır, birebir aktarılmaz (`references/ortak/guvence/kvkk-ve-telif.md`).

## Adım 4 — Taslak (yalnız istenirse)

Taslak Adım 2 ve 3 tamamlandıktan sonra sohbette verilir, onların yerine geçmez: bir satırda sınıf, konu ve çıktı kodu; en çok üç cümlelik özet; evre başına bir madde (ad, dakika, ne olur); öğrencinin yapacağı işler; dersin varsaydığı ön bilgi; çıkış kartı. Sonra düz metinle sorulur: "Değiştirmek istediğiniz bir yer var mı? Yoksa tam paketi hazırlayayım." Değişiklikler taslağa işlenir; paket onaydan sonra üretilir.

## Adım 5 — Paket (tek tur)

1. `references/cikti-kurallari.md` dosyasını oku (kısalık, tutarlılık, okuma düzeyi, cümle desteği).
2. `references/ders-json.md` dosyasını oku ve tek bir `ders.json` yaz. Bütün belgeler bu ortak kaynaktan üretilir; ortak içerik (görev, sorular, çıkış kartı, gözlem ölçütleri) bir kez yazılır.
3. Belgeleri üret: Docs artifact türü listeleniyorsa plan ve gözlem formu Docs belgesi, çalışma kâğıdı Docs belgesi ya da (DNAMATHOS markası isteniyorsa) `dnamathos-pdf-tasarimi` ile PDF; bu türler yoksa docx skill'i ile Word belgesi. Üretim tamamen başarısız olursa bunu söyle; sessizce sohbete dönme.
4. Revizyonda önce `ders.json` düzeltilir; sonra bütün belgeler taranır ve eski sayı, bağlam ya da ad kalmadığı doğrulanır.

## Adım 6 — Doğrulama (belgeler yazıldıktan sonra)

`references/ortak/guvence/dogrulama-kapisi.md` dosyasını ancak şimdi oku ve öğrenci çalışma kâğıdına uygula. Ayrıca:

- Her sorunun ve çıkış kartının cevabını çözerek doğrula; işlem sayısı çıktıya uygun.
- Bileşen kapsama tablosunu kodla say: eksik bileşen 0.
- `python3 scripts/tymm_kod_denetle.py <plan dosyası> --veri references/veri` 0 hata.
- Alt ajan varsa yalnız çalışma kâğıdını ona çözdür.

## Adım 7 — Kapanış

Tek bir kapanış mesajı: (1) derste sınıfta bulunan bir araç kâğıtla yerine konabiliyorsa (sayı kartları, onluk bloklar) kalın bir baskı teklifi; (2) üç belgenin işini görüp görmediği sorusu; (3) bu derse özgü en fazla iki somut seçenek (ör. "Destek gerektiren grup için ikinci bir çalışma kâğıdı hazırlayayım mı?", "Çıkış kartını LGS tarzı çoktan seçmeliye çevireyim mi?").

## Denetim listesi

- [ ] Ders dosyası okundu; program birebir alındı
- [ ] Altı evre; tartışma en az 10 dakika ve öğrenciden öğrenciye bir konuşma biçimi adıyla var
- [ ] Her bileşen numaralı bir işte; kapsama tablosu planda
- [ ] Çıkış kartı en zor durum; üç grup ölçütü açık
- [ ] E, SDB, D, OB yalnız tema listesinden ve puansız
- [ ] Öğrenci kâğıdında cevap yok; doğrulama kapısı geçti; kod denetimi 0 hata
