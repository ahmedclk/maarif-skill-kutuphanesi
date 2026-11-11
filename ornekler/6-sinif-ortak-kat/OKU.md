# Örnek: 6. sınıf ortak kat ve ortak bölen (MAT.6.1.4)

`maarif-kavrama-testi` ve `maarif-hizli-tekrar` skill'lerinin bir haftalık döngüde ürettiği dosyalar. Bütün cevaplar `uret.py` içinde kodla hesaplanır ve denetlenir.

**Program sınırı:** Tema sayfasındaki Öğrenme-Öğretme Uygulamalarına göre bu çıktıda EBOB ve EKOK kavramlarına değinilmez; ortak böleni yalnız 1 olan sayıların aralarında asal olma durumu tartışılır. Sorular bu sınırın içindedir.

| Dosya | Ne |
| --- | --- |
| `DNAMATHOS_6_Ders8_OrtakKat.pdf` | **Tam ders (DNAMATHOS 2.0 tasarımı), 25 slayt:** kapak, ısınma turu (6 soru ve cevapları), konu 1 ve soru 1, konu 2 ve soru 2, Kaydet kartı, kavrama testi (4 soru), ödev kartı. Üreten betik: `ders_uret.py` |
| `kavrama_testi_ogrenci.pdf` | 8. hafta sonu, 4 soru, 12 dakika, notsuz. 2 küme sorusu, 1 aktarım sorusu, 1 tekrar sorusu; her soruda cevap, gerekçe ve güven kutusu |
| `kavrama_testi_ogretmen.pdf` | Doğru cevaplar, kabul edilen ve edilmeyen gerekçeler, sık hatalı cevaplar, hedefli soru bankası, karar kuralı |
| `kavrama_sonuc.json` | Üç örnek öğrencinin (takma ad) sonuçları |
| `karar_ciktisi.txt` | `kavrama_karari.py` çıktısı: A ödevsiz, B'ye 6 hedefli soru, C için konu yeniden işlenir ve ödev 3 soru |
| `kavrama_gecmisi.json` | Aralıklı tekrar için bileşen geçmişi |
| `tekrar_secimi_ogrenci_B.txt` | 9. hafta ders başı turu için `tekrar_sec.py` seçimi |
| `hizli_tekrar_kartlari.pdf` | 9. hafta ders başı: 8 soru (geçen hafta 4, 2–4 hafta önce 3, 8 hafta önce 1), cevap ekranları ve haftanın sloganı |
| `hizli_tekrar_ogretmen.pdf` | Soru, cevap, bileşen, yanlış cevaba tek cümle; slogan denetimi ve reddedilen slogan önerileri |

Yeniden üretmek: `python3 ornekler/6-sinif-ortak-kat/ders_uret.py` (ders PDF'i) ve `python3 ornekler/6-sinif-ortak-kat/uret.py` (A4 kâğıtlar, ayrı tur kartları)
