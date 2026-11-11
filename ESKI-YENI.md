# Eski skill adları → yeni düzen

| Eski skill | Yeni skill(ler) | Ne değişti |
| --- | --- | --- |
| `maarif-matematik-icerik` (5625 sözcük; 5000 sınırını aşıyordu) | `maarif-ortak-yazili`, `maarif-beceri-temelli-test`, `dnamathos-pdf-tasarimi` ve `ortak/` | Tek skill üçe ve ortak başvurulara bölündü. TYMM erişimi → `ortak/maarif/tymm-erisim.md`; beceri eşlemesi, soru dili, görsel ölçütü, cevap anahtarı, güçlük, robotiklik → `ortak/dersler/matematik/`; öğretmen üslubu → `ortak/uslup/`; PDF ile çalışma → `ortak/guvence/`; tasarım dili ve üretim hattı → `dnamathos-pdf-tasarimi`. Metin korunarak taşındı. |
| `maarif-konu-ozeti` | `maarif-konu-ozeti` (2.0) + `dnamathos-pdf-tasarimi` | Ad korundu. SKILL.md adımlara indirildi (3022 → ~800 sözcük); bölümler `references/` altına taşındı; tasarım ve üretim marka skill'ine ayrıldı; sızıntı ve kod denetimi betiğe bağlandı. |
| `benzer-soru-uretimi` | `maarif-benzer-soru` | Kaynak sorunun çıktı ve bileşenle eşlenmesi, içerik çerçevesi sınırı ve doğrulama kapısı eklendi; açıklamaya olumsuz tetikleyiciler eklendi. |
| `ogrenci-hata-analizi` | `maarif-hata-analizi` | Hatalar bileşene bağlandı; önyargısız dil, KVKK ve sınıf düzeyi rapor eklendi. |
| `matematik-anlatim-videosu` | `maarif-anlatim-videosu` | Kurallar `references/` altına bölündü; çıktıya bağlama adımı eklendi. |
| `dnamathos-instagram-karusel` (3233 sözcük) | `dnamathos-instagram-karusel` (2.0) | Ad korundu. SKILL.md adımlara indirildi; bölümler `references/` altına; LGS tarzı madde tanımı ortak dosyaya bağlandı. |
| `unbearable-senaryo` | — | Maarif kütüphanesinin konusu dışında; kütüphaneye alınmadı, kendi hesabınızda olduğu gibi kalabilir. |

Yeni eklenenler: `maarif-cikti-cozumleme`, `maarif-ders-takvimi`, `maarif-ders-plani`, `maarif-derse-hazirlik`, `maarif-farklilastirma`, `maarif-anlama-kontrolu`, `maarif-performans-gorevi`.

**Geçiş önerisi:** Yeni skill'leri yüklemeden önce eski `maarif-matematik-icerik`, `benzer-soru-uretimi`, `ogrenci-hata-analizi` ve `matematik-anlatim-videosu` skill'lerini kapatın; aynı işi yapan iki skill açık kalırsa Claude hangisini seçeceğini şaşırabilir.
