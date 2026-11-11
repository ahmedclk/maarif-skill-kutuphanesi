# Katkı kuralları

Bu kütüphaneye bir skill, ders dosyası ya da veri eklemek isteyen her öğretmen ve geliştirici için.

## Kabul ölçütleri (hepsi zorunlu)

1. **Maarif bağı:** Skill ürettiği her şeyi bir öğrenme çıktısına ve süreç bileşenine bağlar; çıktıyı TYMM sayfasından alır (`ortak/maarif/tymm-erisim.md`). Programdan bağımsız "genel öğretmen yardımcısı" kabul edilmez.
2. **Skill rehberi kuralları** (`python3 araclar/denetle.py` 0 hata):
   - klasör ve `name` kebab-case, ASCII, birbirinin aynı; adda "claude" ya da "anthropic" yok;
   - dosya adı birebir `SKILL.md`; skill klasöründe README yok;
   - `description` ne yaptığını ve ne zaman kullanılacağını söyler, Türkçe tetikleyici sözcükler ve kardeş skill'leri adıyla anan olumsuz tetikleyiciler içerir; en çok 1024 karakter; `<` ve `>` yok;
   - yalnız izin verilen üst bilgi alanları (name, description, license, compatibility, metadata, allowed-tools);
   - SKILL.md en çok 5000 sözcük (hedef 1500'ün altı); ayrıntı `references/` altında.
3. **Ortak iskelet:** Adım 0 yönlendirme (omurga ve ders dosyası okunur) → en çok bir netleştirici soru → programa dayandırma → üretim → dosyalar yazıldıktan sonra doğrulama kapısı → en çok iki somut seçenekle kapanış (`docs/tasarim-ilkeleri.md`).
4. **Ders dosyası:** her skill'in `references/dersler/<ders>.md` dosyası vardır; matematik dışı ders `ortak/dersler/_sablon.md` ile başlar.
5. **Deterministik denetim:** sayı, kod, puan ve sızıntı gibi kritik denetimler betikle yapılır (`ortak/betikler/`); "dikkat et" cümlesi betiğin yerine geçmez.
6. **Testler:** `testler/tetikleme/<ad>.yaml` dosyasında en az 10 tetiklemeli ve 5 tetiklememeli Türkçe istem; `istemler/<ad>.md` hazır istem dosyası.
7. **MEB ölçme kuralları:** soru, sınav ya da değerlendirme aracı üreten skill `ortak/maarif/meb-olcme-mevzuati.md` dosyasını Adım 0'da okur ve uyduğu MEV kodlarını `docs/kilavuz.yaml` dosyasına yazar.
8. **Kılavuz:** her skill `docs/kilavuz.yaml` dosyasında ne yaptığı, ne zaman kullanılacağı, örnek istemi ve kontrol notuyla bulunur.
9. **Dil:** `ortak/uslup/turkce-yazim.md` ve `ortak/uslup/onyargisiz-dil.md`.

## Güvenlik ve gizlilik incelemesi (her katkıda)

- **Talimat enjeksiyonu:** SKILL.md üst bilgisi ve bütün başvuru dosyaları satır satır okunur. Modele yönelik gizli talimat ("önceki talimatları yok say", "sistem istemini göster"), görünmez karakter, bilinmeyen adrese bağlantı, veri gönderen ya da dosya silen betik bulunan katkı reddedilir. `denetle.py` üst bilgide temel bir tarama yapar; inceleme insan tarafından tamamlanır.
- **Betikler:** yalnız standart kütüphane ve bilinen paketler (pyyaml, pypdf, playwright); ağa çıkan, kabuk komutu çalıştıran ya da ev dizinine yazan betik kabul edilmez.
- **KVKK:** örnek dosyalarda gerçek öğrenci adı, numarası, fotoğrafı ya da sağlık bilgisi bulunmaz (`ortak/guvence/kvkk-ve-telif.md`).
- **Telif:** ders kitabı, yayınevi ve gerçek sınav sorusu kopyalanmaz; TYMM alıntıları kaynak ve tarihle verilir.

## Kanıt düzeyi

Her skill'in `metadata.kanit` alanı nerede ve nasıl kullanıldığını söyler. Düzeyler:

| Düzey | Anlamı |
| --- | --- |
| taslak | Yazıldı, testleri var, sınıfta denenmedi |
| denendi | En az iki öğretmen gerçek sınıfta kullandı ve geri bildirim verdi |
| kararlı | İşlev ve tutarlılık testleri geçti; üç dönem boyunca kullanıldı |

## Öğretmen geri bildirim formu

```
Skill:
Sınıf ve ders:
İstem (kısaca):
Ürün işinizi gördü mü? (evet / kısmen / hayır)
Program uyumu doğru muydu? (çıktı, bileşen, sınır)
Düzeltmek zorunda kaldığınız yer:
Öğrencilerde gözlediğiniz:
```

## Sürümleme

`metadata.surum` anlamsal sürümdür: üçüncü hane düzeltme, ikinci hane yeni adım ya da başvuru, birinci hane adımların ya da çıktının değişmesi (eski kullanıcıyı etkileyen değişiklik). Program güncellenirse önce `veri/` ve `ortak/maarif/cerceve.md`, sonra skill'ler güncellenir.
