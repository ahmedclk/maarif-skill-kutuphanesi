---
name: maarif-benzer-soru
description: Öğretmenin verdiği sınavın, testin, yazılının ya da tek bir sorunun kurgusunu, ölçtüğü Maarif çıktısını ve süreç bileşenini, becerisini ve güçlüğünü koruyarak bağlamı ve sayıları değişmiş özgün ikiz sorular, cevap anahtarı ve öğrenciye hitap eden adım adım çözümler üretir. Netleştirici soru sormadan önce yükle. Tetikleyiciler - bu sorunun benzerini yaz, ikiz soru, aynı tarzda 5 soru daha, bu testin benzeri, bu yazılının paraleli, öğrencinin yanlış yaptığı soruların benzerleri, bu sayfadaki sorulardan yeni set. Senaryoya göre sıfırdan yazılı için değil (maarif-ortak-yazili), sıfırdan LGS tarzı test için değil (maarif-beceri-temelli-test), hata analizi ve telafi planı için değil (maarif-hata-analizi).
license: Apache-2.0. DeepTutor (HKUDS) soru üretim hattından uyarlanmıştır ve değiştirilmiştir. Ayrıntı - LICENSE ve NOTICE.
compatibility: Kaynak sorular PDF, fotoğraf, Word ya da metin olabilir. TYMM sayfaları için web erişimi; Python 3.
metadata:
  surum: "2.0.0"
  yazar: DNAMATHOS
  omurga: TYMM öğrenme çıktısı ve süreç bileşeni (ikiz soru aynı bileşeni ölçer)
  dersler: matematik (tam); diğerleri şablonla
  onceki_ad: benzer-soru-uretimi 1.x
  uyarlama: HKUDS/DeepTutor (Apache-2.0)
---

# Maarif benzer soru

Amaç: Verilen kaynak soruların kurgusunu, ölçtüğü bileşeni ve güçlüğünü koruyup bağlamı ve sayıları değiştirerek yeni ve özgün sorular yazmak. İkiz soru, kaynak soruyla **aynı çıktının aynı bileşenini** ölçer; yalnız yüzeyi değişir.

Dil: `references/ortak/uslup/turkce-yazim.md`. Telif: kaynak cümleler aynen kopyalanmaz (`references/ortak/guvence/kvkk-ve-telif.md`).

## Adım 0 — Yönlendirme (sessiz)

1. `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`.
2. Ders dosyası: matematik → `references/dersler/matematik.md` (şimdi oku). Yoksa `references/ortak/dersler/_sablon.md`.
3. Kaynak PDF ya da görüntüyse `references/ortak/guvence/pdf-ile-calisma.md` kurallarıyla oku; kesir, üs ve şekil değerlerini görüntüden doğrula.

## Adım 1 — Girdi

- Kaynak: PDF, fotoğraf, Word ya da metin. Yoksa yalnız onu iste.
- Adet: belirtilmemişse her kaynak soru için bir ikiz.
- Sınav türü: LGS, ortak yazılı, TYT/AYT ya da okul yazılısı; belirtilmemişse kaynağın biçiminden çıkar.
- Varsa öğrencinin daha önce yanlış yaptığı sorular.

## Adım 2 — Keşif: kaynağı çözümle ve programa bağla

Her kaynak soru için bir şablon çıkar: çıktı kodu ve bileşen harfi (TYMM'den eşlenir; kaynakta "kazanım" yazıyorsa güncel çıktıya çevrilir) · soru tipi (`references/soru-tipleri.md`) · güçlük (Z · Y · C) · bağlam türü · ölçülen beceri basamağı · çözüm adımı sayısı.

- Şekilli sorularda metinde açıkça tanımlanmayan bir ilişki şekilden varsayılmaz: "orta nokta gibi görünüyor" ya da "dik gibi duruyor" veri değildir.
- Kaynak soru İçerik Çerçevesi sınırını aşıyorsa (eski programdan kalma) ikiz sınır içinde yazılır ve bu teslimde söylenir.
- Öğrenci geçmişi verildiyse önce onu incele: hangi bileşende, hangi güçlükte, hangi soru tipinde yanlış yapılmış. Yeni sette bu noktalara ağırlık ver ve önceki soruların kökünü tekrar etme.

## Adım 3 — Plan

| No | Kaynak soru | Çıktı · bileşen | Tip | Güçlük | Değişecek öğeler |

İstenen adet kadar satır; iki satırın odağı aynı olmaz. Set 10 soru ve üstüyse ve öğretmen ortamdaysa planı gösterip onay iste; değilse plana göre devam et.

## Adım 4 — Yazım

- Kaynağın kurgusunu koru: aynı bileşen, aynı adım sayısı, aynı güçlük.
- Bağlamı, nesneleri ve sayıları değiştir; yalnız bir sayıyı değiştirmek yetmez, sonuç da kaynaktakinden farklı olmalı.
- Kök tek anlamlı ve tek doğru cevaplıdır. Matematik LaTeX ile: satır içinde `$...$`, ayrı satırda `$$...$$`.
- Çoktan seçmeli sorularda çeldirici kuralları ders dosyasının gösterdiği dosyadadır; her çeldirici adı konmuş bir hatanın bu kökün sayılarına uygulanmış sonucudur.
- MEB soru üslubu: yalın, kısa cümleler ve "Buna göre … kaçtır?" kalıbı.
- İkizler bir **okul yazılısında** kullanılacaksa `references/ortak/maarif/meb-olcme-mevzuati.md` geçerlidir: açık uçlu ya da kısa cevaplı (MEV-10, MEV-11); çoktan seçmeli kaynak soru açık uçluya çevrilir (MEV-12); madde bileşenin bilişsel düzeyindedir (MEV-13). Ortak sınav ve merkezî sınav soruları birebir kullanılmaz (MEV-60).

## Adım 5 — Çıktı

Üç parça: (1) öğrenci soru kâğıdı, (2) cevap anahtarı (çıktı · bileşen · güçlük), (3) öğrenciye hitap eden adım adım çözümler; her yanlış seçeneğin hangi hatadan doğduğu kısaca. Varsayılan biçim Markdown; PDF ya da tasarımlı çıktı istenirse marka skill'i (DNAMATHOS: `dnamathos-pdf-tasarimi`) ya da pdf skill'i.

## Adım 6 — Doğrulama (dosyalar yazıldıktan sonra)

`references/ortak/guvence/dogrulama-kapisi.md` dosyasını şimdi oku ve her soruya uygula. Ayrıca:

1. Soruyu baştan, bağımsız çöz; sayısal sonuçları kodla hesapla.
2. Sorunun şablondaki tipe, bileşene ve güçlüğe uyduğunu kontrol et.
3. Sette tekrar ya da birbirine çok benzeyen soru olmadığını kontrol et.
4. Çoktan seçmelide `python3 scripts/cevap_dagilimi.py <ANAHTAR>`; anahtarda `python3 scripts/tymm_kod_denetle.py <anahtar> --veri references/veri`.

Sorun bulursan yalnız hatalı kısmı düzelt; soruyu baştan yazma. İki kez düzeltilip hâlâ kalan soruyu değiştir.

## Adım 7 — Kapanış

En fazla iki somut seçenek: "Bu ikizleri tek bir çalışma kâğıdı PDF'i yapayım mı?" ya da "Aynı bileşen için bir güçlük düzeyi üstünde ikinci bir set çıkarayım mı?"
