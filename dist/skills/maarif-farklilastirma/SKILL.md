---
name: maarif-farklilastirma
description: Öğretmenin getirdiği ya da adını verdiği var olan bir dersi, aynı öğrenme çıktısı ve aynı görev üzerinde Maarif Modeli'nin destekleme ve zenginleştirme yaklaşımıyla üç gruba uyarlar; bir öğretmen farklılaştırma planı ve üç öğrenci çalışma kâğıdı üretir, ortak içerik bir kez yazıldığı için gruplar birbirinden kopmaz. Netleştirici soru sormadan önce yükle. Tetikleyiciler - bu dersi farklılaştır, öğrencilerim farklı düzeylerde, destekleme ve zenginleştirme etkinliği, kaynaştırma öğrencisi için uyarla, hızlı bitirenler için ek görev, çalışma kâğıdını üç düzeyde hazırla. Sıfırdan yeni bir ders için değil, yeni ders farklılaştırılmış materyal istese bile (maarif-ders-plani); not verme, dereceli puanlama anahtarı ya da test için değil (maarif-performans-gorevi, maarif-beceri-temelli-test).
license: Apache-2.0. k12-teacher-skills (Copyright 2026 Anthropic, PBC; Copyright 2026 Learning Commons) k12-lesson-differentiation skill'inden uyarlanmıştır ve değiştirilmiştir. Ayrıntı - LICENSE ve NOTICE.
compatibility: TYMM sayfaları için web erişimi. Belge üretimi için Docs artifact türü ya da docx skill'i.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: TYMM tema sayfası Farklılaştırma (Zenginleştirme, Destekleme) ve süreç bileşenleri
  dersler: matematik (tam); diğerleri şablonla
  uyarlama: anthropics/k12-teacher-skills k12-lesson-differentiation (Apache-2.0)
---

# Maarif farklılaştırma

Amaç: Aynı çıktıyı, aynı bağlamı ve aynı zor durumu üç grubun da çalışması; gruplar arasındaki fark **destek ve zihinsel yükte** olsun, konuda, metin türünde ya da "öğrenme stilinde" değil. Maarif dilinde: destekleme, temel ve zenginleştirme.

| Grup (öğretmen planında) | Öğrenci kâğıdında | İlke |
| --- | --- | --- |
| Destekleme | A kâğıdı | Aynı görev; ön koşul bileşeni adıyla anılır ve basamaklı destekle kurulur; en zor durum düşürülmez, desteklenir |
| Temel | B kâğıdı | Görev dersin yazıldığı hâliyle |
| Zenginleştirme | C kâğıdı | Aynı görev uzatılır: genelleme, gerekçe, sonraki çıktıya köprü; ek iş değil derin iş |

Öğrenci kâğıdında düzey adı yazılmaz (`references/ortak/uslup/onyargisiz-dil.md`). Öğrenci verisi takma adla işlenir (`references/ortak/guvence/kvkk-ve-telif.md`). Kaynaştırma ya da bütünleştirme yoluyla eğitim gören öğrencide ölçme ve değerlendirmenin temeli BEP'tir (MEV-04, `references/ortak/maarif/meb-olcme-mevzuati.md`): skill BEP yazmaz ve tanı istemez; öğretmen bir BEP hedefi verirse o öğrencinin kâğıdı ve çıkış kartı o hedefe göre uyarlanır.

## Adım 0 — Yönlendirme (sessiz)

1. `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`.
2. Ders dosyası: matematik → `references/dersler/matematik.md` (şimdi oku; okumadan farklılaştırmak kritik hatadır). Ders dosyası yoksa `references/ortak/dersler/_sablon.md` ile çalış ve planın sonuna not ekle.

## Adım 1 — Dersi al ve netleştir (en fazla bir soru)

Ders yoksa yalnız onu iste (plan, kitap sayfası ya da önceki skill'in ürünü). Öğretmen grupların neye ihtiyaç duyduğunu söylediyse ("kesirleri modelle göremeyen 6 öğrenci") bunu kullan; söylemediyse sorma, programın Farklılaştırma önerisiyle başla.

## Adım 2 — Programa dayandır

Tema sayfasından: çıktı ve bileşenler, Farklılaştırma (Zenginleştirme, Destekleme) birebir, ön koşul çıktı (önceki sınıf) ve sonraki çıktı. Destekleme grubunun ön koşul bileşeni ve zenginleştirme grubunun ileri çıktısı **kod ya da tam adla** planda yazılır; "biraz ön bilgi" gibi belirsiz ifade geçmez.

## Adım 3 — Üç grubu kur

1. **En zor durumu belirle** (ders dosyasındaki listeden) ve üç grubun her birinde bulunduğunu doğrula: destekleme grubunda desteklenmiş, temel grubunda yalın, zenginleştirmede uzatılmış.
2. **Ortak içerik bir kez:** bağlam, sayılar, görsel ve çıkış kartı `farklilastirma.json` içinde `ortak` altında bir kez yazılır; gruplar onu çeker (`references/farklilastirma-json.md`).
3. **Destek düşünceyi taşır, cevabı vermez:** tek olası sözcüklü boşluk, gömülü cevap, hiçbir karar gerektirmeyen adım listesi, anahtar sözcük kısa yolu ("toplam varsa topla") kullanılmaz. Her grupta en az bir soru, desteğin çözmediği bir öğrenci kararı ister.
4. **Zenginleştirme ek iş değildir:** daha çok soru değil; genelleme, karşı örnek, iki yöntemi karşılaştırma ya da sonraki çıktıya köprü.
5. **Programlar arası bileşenler:** Grupların ortak tartışmasında temanın SDB ya da E kodu bir davranışla geçer (ör. SDB2.1 İletişim: A ve C grubundan birer öğrenci çözümünü birbirine anlatır).

## Adım 4 — Çıktı (tek tur)

Bir öğretmen planı (grupların amacı, ön koşul ve ileri çıktı, en zor durumun her gruptaki hâli, gruplama ölçütü, ortak tartışma) ve üç öğrenci kâğıdı. Docs artifact türü listeleniyorsa Docs belgeleri; yoksa docx skill'i. Revizyonda önce `farklilastirma.json` düzeltilir, sonra bütün belgeler taranır.

## Adım 5 — Doğrulama (belgeler yazıldıktan sonra)

`references/ortak/guvence/dogrulama-kapisi.md` dosyasını şimdi oku ve her kâğıda uygula. Ek olarak:

- Üç kâğıtta çıktı kodu aynı; en zor durum üçünde de var (metinde arayarak say).
- Hiçbir destek cevabı vermiyor; her kâğıtta desteğin çözmediği en az bir karar var.
- Ortak sayı ve bağlam üç kâğıtta birebir aynı.
- `python3 scripts/tymm_kod_denetle.py <plan> --veri references/veri` 0 hata.

## Adım 6 — Kapanış

Paketin işini görüp görmediğini sor; en fazla iki somut seçenek: "Destekleme grubu için somut model kartı ekleyeyim mi?" ya da "Zenginleştirme kâğıdına sonraki çıktıya köprü kuran bir problem koyayım mı?"

## Denetim listesi

- [ ] Aynı çıktı, aynı bağlam, aynı en zor durum üç grupta
- [ ] Ön koşul ve ileri çıktı adıyla yazılı
- [ ] Destek cevap vermiyor; zenginleştirme derinleştiriyor
- [ ] Öğrenci kâğıdında düzey adı yok
- [ ] Doğrulama kapısı geçti; kod denetimi 0 hata
