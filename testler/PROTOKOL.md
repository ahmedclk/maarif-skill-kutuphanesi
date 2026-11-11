# Test protokolü

Anthropic'in skill rehberindeki üç test düzeyi bu kütüphanede şöyle uygulanır.

## 1. Tetikleme testi (her sürümde)

`testler/tetikleme/<skill>.yaml` dosyasında en az 10 "tetiklemeli" ve 5 "tetiklememeli" Türkçe istem bulunur. Her istem temiz bir oturumda, kütüphanenin bütün skill'leri yüklüyken denenir:

- Tetiklemeli istemlerde doğru skill'in yüklenme oranı **en az %90** olmalı.
- Tetiklememeli istemlerde skill yüklenmemeli; `dogru_skill` alanındaki skill (ya da "yok") yüklenmeli.
- Kalan istem için önce `description` düzeltilir: eksik tetikleyici sözcük eklenir ya da olumsuz tetikleyici ("… için değil") netleştirilir. Talimat gövdesi tetiklemeyi düzeltmek için değiştirilmez.

Sonuç `testler/sonuclar/<tarih>-tetikleme.csv` dosyasına yazılır: istem · beklenen · yüklenen · geçti.

## 2. İşlev testi (yeni skill ve büyük değişiklikte)

Her skill için en az üç gerçek öğretmen isteği (biri matematik ortaokul, biri lise, biri eksik bilgili) çalıştırılır. Ürünler `testler/rubrikler/ortak.csv` ve skill türüne göre `olcme.csv` ya da `plan.csv` ile, `testler/yargic-istemi.md` kullanılarak ayrı bir modele değerlendirtilir. Geçme eşiği: P ve R kovalarında kalan ölçüt yok; O ve M kovalarında en çok bir.

Deterministik denetimler yargıçtan önce çalışır ve kalırsa yargıca gidilmez:

```
python3 araclar/denetle.py
python3 scripts/tymm_kod_denetle.py <ürün> --veri references/veri
python3 scripts/guclugu_hesapla.py maddeler.json            # yazılı
python3 scripts/cevap_dagilimi.py <ANAHTAR>                  # çoktan seçmeli
python3 scripts/sizinti_ara.py <öğrenci dosyası> cevaplar.json
python3 scripts/pdf_denetle.py <pdf> --sayfa N --sira <sira.json>   # DNAMATHOS PDF
```

## 3. Tutarlılık testi (sürüm öncesi)

Aynı istem 3–5 kez çalıştırılır. Beklenen: aynı çıktı kodları ve bileşen kapsaması, aynı kâğıt sayısı (yazılıda), aynı akış iskeleti. Sorular ve bağlamlar farklı olabilir; yapı farklı olmamalı.

## Öğretmen denemesi

Bir skill "kararlı" sayılmadan önce en az iki öğretmen gerçek sınıfında kullanır ve `KATKI.md` dosyasındaki kısa geri bildirim formunu doldurur.
