# Karar kuralı ve hedefli ödev

## kavrama_sonuc.json

```json
{
  "hafta": 7, "sinif": 6, "cikti": ["MAT.6.1.4"],
  "sorular": {
    "S1": {"tur": "kume", "bilesenler": ["6.1.4-a", "6.1.4-b"]},
    "S2": {"tur": "kume", "bilesenler": ["6.1.4-c"]},
    "S3": {"tur": "aktarim", "bilesenler": ["6.1.4-a", "6.1.4-c"]},
    "S4": {"tur": "tekrar", "bilesenler": ["6.1.2-ç"], "islendi": 5}
  },
  "ogrenciler": {
    "Öğrenci A": {"S1": {"cevap": 1, "gerekce": 1, "emin": 1}, "S2": {"cevap": 1, "gerekce": 0, "emin": 1},
                  "S3": {"cevap": 0, "gerekce": 0, "emin": 1}, "S4": {"cevap": 1, "gerekce": 1, "emin": 0}}
  }
}
```

`islendi`: tekrar sorusunun bileşeninin ilk işlendiği hafta (aralıklı tekrar bunu kullanır; yazılmazsa testin haftası alınır). `cevap` ve `gerekce`: 1 doğru, 0 yanlış ya da boş (gerekçe yarımsa 0,5). `emin`: 1 eminim, 0 emin değilim. Gerçek ad yazılmaz.

## Bileşen kararı

Bir bileşenin puanı, onu yoklayan soruların ortalamasıdır; soru puanı = (cevap + gerekçe) ÷ 2.

| Puan | Karar |
| --- | --- |
| ≥ 0,85 | **Geçti** |
| 0,5 – 0,85 | **Kısa telafi** |
| < 0,5 | **Yeniden ele al** |

Ek kurallar:
- Bir sorunun cevabı yanlış ve güveni "emin" ise o bileşen en az **yeniden ele al** olur (yerleşmiş yanılgı).
- Cevap doğru, gerekçe 0 ise bileşen en çok **kısa telafi** olur (doğru cevap, eksik akıl yürütme).
- Bir bileşen **ancak iki ayrı haftada** geçti alırsa "kalıcı" sayılır ve tekrar listesinden çıkar (ustalık: farklı biçimde iki doğru).

## Hedefli ödev

| Karar | Ödev |
| --- | --- |
| Geçti | Yok |
| Kısa telafi | 2 soru: biri testteki biçimde, biri farklı biçimde |
| Yeniden ele al | Telafi kartı (≤ 60 sözcük) + 3 soru; sonraki derste ilk 5 dakika |

Haftalık üst sınır 6 soru. **Konu yeniden:** Haftanın bileşenlerinin yarısında ya da fazlasında puan 0,5'in altındaysa sorun ödevle çözülmez; konu sonraki derste 10–15 dakika yeniden işlenir ve ödev 3 soruyla sınırlanır (önce en temel bileşen). Aşılırsa sıra: (1) emin ama yanlış, (2) yeniden ele al, (3) kısa telafi. Kalanlar bir sonraki haftanın tekrar sorusuna aktarılır.

## kavrama_gecmisi.json

Betik her hafta öğrenci → bileşen → {işlendiği hafta, [hafta, karar] kayıtları} ekler. `maarif-hizli-tekrar` aynı dosyayı ders başı tekrar turunu seçmek için okur.
