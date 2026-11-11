---
name: maarif-anlatim-videosu
description: Bir öğrenme çıktısına bağlı konu ya da soru için Remotion ile kısa anlatım videosu hazırlar; sahne planı, ElevenLabs'e yapıştırılmaya hazır Türkçe seslendirme metni, kare numarasına bağlı ve çakışmasız yerleşimli Remotion kodu üretir, her sahnenin son karesini render edip denetler. Tetikleyiciler - bu konu için anlatım videosu, animasyonlu çözüm, Shorts ya da Reels ders videosu, soru çözüm videosu, Remotion ile video, seslendirme metni. Kısa video senaryosu ya da eğlence içeriği için değil; Instagram görsel karuseli için değil (dnamathos-instagram-karusel); slayt sunumu için değil (maarif-konu-ozeti).
license: Apache-2.0. DeepTutor (HKUDS) video ders istemlerinden uyarlanmıştır ve değiştirilmiştir. Ayrıntı - LICENSE ve NOTICE.
compatibility: Node.js ve Remotion; render için Chromium. Seslendirme için ElevenLabs (isteğe bağlı).
metadata:
  surum: "2.0.0"
  yazar: DNAMATHOS
  omurga: TYMM öğrenme çıktısı; İçerik Çerçevesi gösterimleri
  dersler: matematik
  onceki_ad: matematik-anlatim-videosu 1.x
  uyarlama: HKUDS/DeepTutor (Apache-2.0)
---

# Maarif anlatım videosu (Remotion)

Amaç süslü bir tanıtım filmi değil, kalıcı bir öğrenmedir: video önce ana fikri ya da soruyu verir, sonra akıl yürütmeyi adım adım kurar; seslendirme ekranda görüneni anlatır. Anlatım Sokratiktir (`references/ortak/uslup/ogretmen-uslubu.md`): izleyiciye bir an durup düşünmesi için soru sorulur.

## Adım 0 — Yönlendirme (sessiz)

1. Konu bir çıktıya bağlıysa `references/ortak/maarif/tymm-erisim.md` ile çıktıyı, terimleri, Sembol ve Gösterimleri ve sınırları al; videoda sınır dışı gösterim ya da yöntem kullanılmaz.
2. Ders dosyası: matematik → `references/dersler/matematik.md`.
3. Biçim ve seslendirme: `references/bicim-ve-seslendirme.md`; kod: `references/remotion-ve-yerlesim.md`; görünüm: `references/gorsel-dil.md`. Üçünü de kod yazmadan önce oku.

## Adım 1 — Netleştirme (en fazla bir soru)

Biçim belirtilmemişse sor (Shorts 9:16 ya da yatay ders 16:9). Öğretmen ortamda değilse Shorts seç.

## Adım 2 — Sahne planı

Varsayılan akış: giriş ve soru · gelişme 1 · gelişme 2 · ana sonuç · kısa tekrar · sabit kapanış karesi. Her sahnede bir şey çizilir (grafik, sayı doğrusu, şekil, tablo). Sahnenin yerleşim kutuları sahne bileşeninin üstüne yorum olarak yazılır.

## Adım 3 — Seslendirme metni

Sahne numarasıyla, ElevenLabs'e yapıştırılmaya hazır; sayılar ve formüller okunduğu gibi ("x kare artı iki x"). Sahne süresi metnin okunma süresinden hesaplanır.

## Adım 4 — Remotion kodu

Sahne bileşenleri ve `Composition` tanımı. Her hareket kare numarasına bağlı; CSS geçişi, zamanlayıcı, `Math.random()` ve `Date` yok.

## Adım 5 — Doğrulama

1. Matematiksel doğruluk: her sayı ve sonuç kodla hesaplandı; emin olunmayan sayı videoya konmaz.
2. Kodu derle; her sahnenin son karesini render et ve ekran görüntüsüyle çakışma, taşma ve güvenli alan denetimi yap (yerleşim sözleşmesi).
3. Ekran metni ve seslendirme `references/ortak/uslup/turkce-yazim.md` kurallarına uyuyor.

## Adım 6 — Çıktı sırası ve kapanış

1. Kısa özet: başlık, 2–4 cümlelik içerik özeti, sahne listesi, bağlı çıktı kodu.
2. Seslendirme metni.
3. Remotion kodu.
4. Doğrulama sonucu (tek satır) ve son kare temas tablosu.

En fazla iki somut seçenek: "Aynı konu için 16:9 ders sürümünü çıkarayım mı?" ya da "Videonun sonundaki soruyu karusel olarak hazırlayayım mı?" (dnamathos-instagram-karusel).
