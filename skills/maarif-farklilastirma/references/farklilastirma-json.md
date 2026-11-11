# farklilastirma.json

```json
{
  "ortak": {
    "cikti": {"kod": "MAT.6.1.5", "bilesenler": ["a", "b"]},
    "on_kosul": {"kod": "MAT.5.x.x", "ad": "…"}, "ileri": {"kod": "MAT.6.1.6", "ad": "…"},
    "baglam": "…", "gorsel": {"tur": "yüzlük model", "aciklama": "…"},
    "en_zor_durum": "0,6 ile 0,60'ın eşitliği (sıfır eklemenin değeri değiştirmediği)",
    "cikis_karti": {"ogrenci": "…", "gruplar": {"Tamam": "…", "Neredeyse": "…", "Yeniden ele alınmalı": "…"}}
  },
  "gruplar": {
    "destekleme": {"kagit": "A", "destekler": ["model kartı", "örnek çözümün ilk satırı"], "sorular": ["s1", "s2", "s3"]},
    "temel": {"kagit": "B", "sorular": ["s1", "s2", "s3", "s4"]},
    "zenginlestirme": {"kagit": "C", "uzatma": "genelleme ve karşı örnek", "sorular": ["s2", "s4", "s5"]}
  },
  "sorular": {"s1": {"ogrenci": "…", "durum": "temel durum"}, "s4": {"ogrenci": "…", "durum": "en zor durum"}}
}
```

Bir soru birden çok grupta kullanılıyorsa metni bir kez yazılır; grup yalnız desteği ya da uzatmayı ekler.
