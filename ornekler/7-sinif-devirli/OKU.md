# Örnek: 7. sınıf ondalık gösterim (MAT.7.1.2) — kontrol çalışması

`maarif-konu-ozeti` skill'inin haftalık paketi, kütüphanenin son durumunu sınamak için yeni bir konuda baştan sona üretildi. Skill'ler depodan değil, `dist/zip` içindeki paketlerden kurulup çalıştırıldı.

**Program:** TYMM 7. sınıf 1. Tema (1) sayfası (11.11.2026). Çıktı: "Gerçek yaşam durumlarında rasyonel sayıların ondalık gösterimlerini yansıtabilme" (KB2.15). Bu çıktıda sınırlama cümlesi yoktur. Devir çizgisi programın Sembol ve Gösterimler listesinde geçmediği için öğrenci belgelerinde "…" kullanıldı.

**Varsayımlar:** Ders kitabı paylaşılmadı. Bu yüzden "Kitapta" satırları yalnız bölüm adını verir; ödev kartındaki kaynak kitap satırını öğretmen doldurur. Ders 70 dakikadır (2 × 35): ısınma 8 soru, 3 konu ve soru çifti. Önceki dersler 7.1.1'in bileşenleridir.

| Dosya | Ne |
| --- | --- |
| `DNAMATHOS_7_Ders6_Ondalik.pdf` | Ders, 31 slayt: kapak, ısınma (8 soru ve cevapları), 3 konu ve ardındaki sorular, Kaydet ve slogan, kavrama testi (4 soru), ödev |
| `DNAMATHOS_7_Ders6_Kavrama.pdf` | Yazdırılabilir kavrama testi kâğıdı (tek yaprak, ön ve arka) |
| `DNAMATHOS_7_Ders6_Ogretmen.pdf` | Ders planı, kart boşluklarının cevapları, adım puanlı çözümler, ısınma listesi, slogan, test anahtarı, hedefli soru bankası, kapsama tablosu |
| `kavrama_sonuc.json`, `karar_ciktisi.txt`, `kavrama_gecmisi.json` | Üç örnek öğrencinin sonucu ve `kavrama_karari.py` kararı: A ödevsiz, B'ye 6 hedefli soru, C için konu yeniden ve ödev 3 soru |
| `tekrar_secimi_ogrenci_B.txt` | 7. hafta ısınması için `tekrar_sec.py` seçimi |
| `cevaplar.json`, `slogan_bankasi.json` | Sızıntı denetimi dizgeleri; ders ders biriken sloganlar |

## Denetim sonuçları

| Denetim | Sonuç |
| --- | --- |
| Matematik (assert) | Bütün sayılar uzun bölme işleviyle hesaplandı ve doğrulandı |
| Taşma ve üst üste binme | 31 slayt, 0 sorun; en küçük gövde yazısı 17 px |
| Cevap sızıntısı | Ders PDF'i 0, kavrama kâğıdı 0 |
| Boşluk cevapları | Konu kartlarında görünmüyor (betikte assert) |
| TYMM kod denetimi | 0 hata, 0 uyarı |
| PDF bağlantıları | 120 bağlantı, 0 hatalı |
| Paket | Isınma 8 soru, 5 biçim, art arda aynı bileşen yok; kavrama testi 2 küme, 1 aktarım, 1 tekrar; slogan ≤ 8 sözcük |

## Bu çalışmanın bulduğu ve düzelttiği sorunlar

1. **Kapakta rozet başlığın üstüne biniyordu.** Alt başlık uzun olunca "DERS 06" rozeti soru işaretini örtüyordu ve taşma denetimi bunu görmüyordu. `dnamathos.css` içinde alt başlık rozetin altına indirildi. `tasma-denetimi.js` artık rozet ve tüyonun bir metnin üstüne binip binmediğine de bakıyor; eski CSS ile denendi ve sorunu yakaladı.
2. **Konu kartı boşluğun cevabını veriyordu.** Konu 1'deki tablonun başlığı ("Payı paydaya böl") karttaki boşluğu dolduruyordu. Sızıntı betiği yakaladı; başlık "Bölme işlemi yap" oldu. Betiğe, kart boşluklarının cevabını arayan bir denetim eklendi.
3. **Pakette 7. sınıf program verisi yoktu.** Kod denetimi yalnız uyarı verebiliyordu. `veri/tymm/matematik/7.yaml` sayfadan okunarak eklendi (MAT.7.1.1–7.1.4).
4. **Çözüm alanı başlangıcı.** Üç soruda çip satırı çözüm alanına biniyordu; denetim yakaladı, `coz_ust` değerleri büyütüldü.

Yeniden üretmek: `python3 ornekler/7-sinif-devirli/uret.py` (kurulu paketle sınamak için `--skill <dnamathos-pdf-tasarimi klasörü>`).
