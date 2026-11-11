---
name: dnamathos-instagram-karusel
description: DNAMATHOS Instagram sayfası için Maarif Modeli çıktısına bağlı matematik içeriği üretir; konu karuseli, Maarif eğilim ve sosyal-duygusal becerilerine dayanan rehberlik gönderisi ve gerçek hayat örneğinden oluşan üçlü ızgara satırını sınıf renk paletiyle tasarlar; 1080 × 1350 PNG slaytları, temas tablosunu, açıklama, etiket ve alternatif metni teslim eder. Tetikleyiciler - Instagram karuseli hazırla, DNAMATHOS gönderisi, LGS karuseli, ızgara satırı, rehberlik gönderisi, gerçek hayat matematiği gönderisi, kaydırmalı post. Ders slaytı ya da PDF için değil (maarif-konu-ozeti, dnamathos-pdf-tasarimi), video için değil (maarif-anlatim-videosu), sınav sorusu için değil (maarif-beceri-temelli-test).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: Python 3, Playwright (Chromium), KaTeX, PIL; Inter ve Lora yazı tipleri. Doğa fotoğrafı için telifsiz kaynaklara web erişimi.
metadata:
  surum: "2.0.0"
  yazar: DNAMATHOS
  marka: DNAMATHOS
  omurga: TYMM çıktısı (konu karuseli), temanın E ve SDB kodları (rehberlik gönderisi)
---

# DNAMATHOS Instagram karuseli

Amaç: Ortaokul (özellikle LGS'ye hazırlanan 8. sınıf) ve lise öğrencilerine bir matematik fikrini kaydırarak öğrenilen, kaydedilen ve paylaşılan bir karuselle anlatmak. Karusel ders notu değildir: bir merakla açılır, tek bir fikri adım adım kurar, bir ters köşe ya da sık yapılan hatayla akılda kalır ve kaydetmeye değer bir özetle biter.

Profilde her ızgara satırı bir konuya ayrılır: sağda konu karuseli, ortada Maarif Modeli kapsamında bir rehberlik gönderisi, solda konunun gerçek hayattaki örneği; satır o sınıfın renk paletindedir. Konu, hedef kitle (LGS, lise, veli), slayt sayısı ve ilgili öğrenme çıktısı her çalışmada kullanıcıdan alınır; yalnız konu verilirse kitle konudan çıkarılır ve ilk cümlede söylenir. Yalnız karusel istense de karusel satırın sağ karosu olarak tasarlanır.

## Adım 0 — Yönlendirme (sessiz)

`references/ortak/maarif/cerceve.md` ve `references/ortak/maarif/tymm-erisim.md`. Dil: `references/ortak/uslup/turkce-yazim.md`; İngilizce sosyal medya terimleri çevrilmez, karşılığı kullanılır (kanca, harekete çağrı, kaydırma).

## Adım 1 — Konu ve kaynak

- **Matematik doğruluğu:** her sayı, işlem ve sonuç kodla hesaplanır; karuselde yanlış bir işlem marka için en büyük risktir.
- **Program uyumu:** konu bir çıktıya bağlıysa (ör. MAT.8.1.2) tema sayfası açılır; terimler, gösterimler ve İçerik Çerçevesi sınırları oradan alınır. Sınır dışı gösterim ya da yöntem kullanılmaz.
- **LGS konuları:** soru `references/ortak/dersler/matematik/coktan-secmeli.md` dosyasındaki beceri temelli madde tanımına uyar; gerçek LGS sorusu kopyalanmaz, "LGS tarzı" denir.
- **Gerçek veri:** istatistik ya da bilimsel bilgi kaynağı açılıp doğrulanır; son slaytta ya da açıklamada belirtilir.

## Adım 2 — Tek fikir, kanca, akış ve metin

`references/kanca-akis-metin.md`: bir cümlelik vaat; kanca türleri ve kuralları; 7–10 slaytlık akış (kanca → soru → adımlar → ters köşe → özet kartı → kendini dene → kapanış); slayt başına tek fikir ve sözcük sınırları; tek ve somut harekete çağrı.

## Adım 3 — Görsel ve üretim

`references/gorsel-ve-uretim.md`: görsel anlatının taşıyıcısıdır; 1080 × 1350 px, sınıf paleti, yazı boyları, sabit öğeler, kart bileşenleri; HTML → Playwright PNG üretim hattı, JS taşma ve en küçük yazı denetimi, temas tablosu ve 3:4 kırpılmış kapak.

## Adım 4 — Satırın öteki gönderileri

`references/profil-izgarasi.md`: paylaşım sırası (karusel → rehberlik → gerçek hayat), rehberlik gönderisinin Maarif dayanağı (yalnız temada adı geçen E, SDB, D ve OB kodları ve beceri basamakları; kod gönderide değil açıklamada), doğa fotoğrafı zemini ve telif kuralları, gerçek hayat örneği, sınıf renk paleti ve satır tasarım kuralları.

Rehberlik gönderisi tanı, tedavi ya da psikolojik danışmanlık yerine geçmez; kaygı ve motivasyon konularında okul rehber öğretmenine başvurmayı öneren bir cümle bulunur (`references/ortak/guvence/kvkk-ve-telif.md`).

## Adım 5 — Denetim (üretimden önce ve sonra)

`references/denetim.md` tablosu. Mümkünse denetimi karuseli görmemiş ayrı bir ajana yaptır. Üretimden sonra taşma ve yazı boyu denetimi 0 sorun, temas tablosu ve telefon boyutundaki kopya gözle görüldü.

## Adım 6 — Teslim

`references/aciklama-etiket.md`: PNG slaytlar (sırasıyla), temas tablosu, `aciklama.txt` (ilk satır kanca, gövde, harekete çağrı, 3–5 Türkçe etiket, her slayt için alternatif metin, fotoğraf künyesi). Satır üretildiyse paylaşım sırası yazılır: "1) Konu karuseli → 2) Rehberlik → 3) Gerçek hayat". En fazla iki somut seçenek: "Aynı satır için anlatım videosu hazırlayayım mı?" (maarif-anlatim-videosu) ya da "Sıradaki konunun satırına geçeyim mi?"
