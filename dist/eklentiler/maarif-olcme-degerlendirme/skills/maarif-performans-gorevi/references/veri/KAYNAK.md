# Veri katmanı: kaynak ve doğrulama

`veri/tymm/` program verisini makinece okunur biçimde tutar. Skill'ler bu veriyi **ilk bakış ve denetim** için kullanır; birebir çıktı metni ve sınırlar her çalışmada TYMM tema sayfasından alınır (`ortak/maarif/tymm-erisim.md`).

| Dosya | İçerik | Doğrulama |
| --- | --- | --- |
| `tymm/kodlar.yaml` | KB, E, SDB, D, OB, MAB kodları ve adları | TYMM beceri sayfaları, 11.11.2026, birebir |
| `tymm/matematik/6.yaml` | 6. sınıf çıktıları (6.1.1–6.1.8, 6.6.1), bileşen harfleri, kısa adlar, basamaklar; 1. Tema kod listeleri | Kısmi: 6.1.1 bileşenleri ve 1. Tema kod listeleri birebir; öteki adlar kısaltılmış |
| `tymm/matematik/9.yaml` | 9. sınıf 9.2.1–9.4.1 çıktıları ve bileşen harfleri | Özet: kodlar ve harfler eşlendi, metinler kısaltılmış |

Kurallar:
- Yeni bir sınıf ya da ders eklenirken her dosyanın `dogrulama` alanı doldurulur: tarih, durum (birebir · kısmi · özet) ve not.
- `birebir` alanına yalnız sayfadan kelimesi kelimesine alınmış metin yazılır.
- Program güncellenirse önce bu dosyalar, sonra `ortak/maarif/cerceve.md` güncellenir; `araclar/denetle.py` ikisinin tutarlılığını sınar.
