# Çıktı kartı: alanlar ve biçim

Kart tek kaynaktır: öğretmen tablosu ve `cikti.json` aynı alanlardan üretilir; biri değişirse öteki de değişir.

## cikti.json

```json
{
  "ders": "Matematik",
  "sinif": 6,
  "tema": {"no": 1, "ad": "Sayılar ve Nicelikler (1)", "sayfa": "https://tymm.meb.gov.tr/ortaokul-matematik-dersi/unite/456", "ders_saati": "…"},
  "dogrulama": {"tarih": "2026-11-11", "kaynak": "tema sayfası | program PDF'i | öğretmenin metni"},
  "tema_kodlari": {
    "alan_becerileri": ["MAB1"], "kavramsal_beceriler": ["KB2.4", "KB2.10", "KB2.14"],
    "egilimler": ["E1.1"], "sdb": ["SDB2.1"], "degerler": ["D14"], "okuryazarlik": ["OB4"],
    "disiplinler_arasi": [], "beceriler_arasi": ["MAB3"]
  },
  "ciktilar": [
    {
      "kod": "MAT.6.1.1",
      "metin": "… (birebir)",
      "beceri": ["MAB1", "KB2.10"],
      "bilesenler": [
        {"harf": "a", "birebir": "…", "kisa_ad": "Çarpan ve katlara yönelik varsayımda bulunma",
         "basamak": "KB2.10.SB1", "esleme": "yorum", "olcme": "yazılı | süreç | performans", "gerekce": "…"}
      ],
      "sinirlar": ["… ile sınırlandırılır (birebir)"],
      "genellemeler": ["…"], "anahtar_kavramlar": ["…"], "sembol_gosterim": ["…"],
      "ogrenme_kanitlari": ["…"],
      "uygulamalar": {"ozet": "…", "programlar_arasi": [{"kod": "SDB2.1", "davranis": "birbirlerini dinlemeleri"}]},
      "farklilastirma": {"zenginlestirme": "…", "destekleme": "…"},
      "kitap": [{"bolum": "Etkinlik 2", "sayfa": 91, "bilesenler": ["a", "b"]}]
    }
  ],
  "temel_kabuller": "…", "on_degerlendirme": "…", "kopru_kurma": "…",
  "notlar": ["Kitabın 3. teması sitede 1. Tema'nın ikinci sayfasıdır."]
}
```

Kurallar: `birebir` alanları sayfadan kelimesi kelimesine; `kisa_ad` öğretmen tablosu ve soru etiketi için programın fiil öbeğinden kısaltılır. Bilinmeyen alan boş bırakılır, doldurulmaz.

## Öğretmen tablosu (sohbet ya da belge)

1. Başlık: "MAT.6.1 · Sayılar ve Nicelikler (1) · 6. sınıf matematik"
2. Tema kod listeleri tek satırda.
3. Her çıktı için tablo: harf · bileşen (birebir) · basamak · ölçme · not.
4. "Sınırlar" kutusu (birebir alıntılar).
5. "Programlar arası bileşenler derste nerede?" tablosu: kod · uygulamadaki davranış.
6. Varsa kitap eşlemesi.
7. En altta tek satır doğrulama notu (tarih ve kaynak).
