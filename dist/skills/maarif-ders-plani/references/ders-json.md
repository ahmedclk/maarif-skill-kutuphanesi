# ders.json: ortak kaynak

Uyarlama: k12-teacher-skills lesson-json dosyası (Apache-2.0). Bu dosya her belgenin **ne** taşıdığını belirler; sayfa görünümünü belirlemez.

```json
{
  "ortak": {
    "ders": "Matematik", "sinif": 6, "sure_dk": 40,
    "cikti": {"kod": "MAT.6.1.4", "metin": "… (birebir, planda yalnız bir kez)", "bilesenler": {"a": "…", "b": "…"}},
    "tema_kodlari": {"egilimler": ["E3.7"], "sdb": ["SDB2.1"], "degerler": [], "okuryazarlik": ["OB4"]},
    "on_bilgi": "MAT.5.x.x kodu ve bir cümle: öğrenci şimdiden ne yapabiliyor",
    "buyuk_fikir": "tek cümle",
    "ogrenci_hedefi": "Bu derste … yapabileceksin.",
    "kavramlar": [{"terim": "ortak kat", "tanim": "…"}],
    "yanilgilar": [{"ne_yapar": "4 ile 6'nın ortak katı olarak 10 yazar", "neden": "toplamayı kat sanıyor", "ogretmen_hamlesi": "…"}],
    "on_degerlendirme": {"ogrenci": "…", "ogretmen": "beklenen cevaplar"},
    "kopru": {"ogrenci": "…", "ogretmen": "…"},
    "gorev": {"ogrenci": "… (ikinci tekil kişi)", "ogretmen": "başlatma ve yürütme notu"},
    "s1": {"ogrenci": "…", "ogretmen": "durum: temel durum · bileşen a", "uyaran": "tablo | sayı doğrusu | şekil"},
    "s2": {"ogrenci": "…", "ogretmen": "durum: en zor durum · bileşen c"},
    "gozlem_olcutleri": [{"gorulen": "öğrencinin yaptığı", "neden_onemli": "…", "ne_yapilir": "…"}],
    "programlar_arasi": [{"kod": "SDB2.1", "davranis": "arkadaşının çözümünü dinleyip kendi sözleriyle aktarır"}],
    "cikis_karti": {"ogrenci": "…", "ogretmen": "toplama notu · durum: en zor durum",
                    "gruplar": {"Tamam": "…", "Neredeyse": "…", "Yeniden ele alınmalı": "…"}},
    "farklilastirma": {"zenginlestirme": "…", "destekleme": "…"}
  },
  "belgeler": [
    {"id": "ders_plani", "bolumler": ["Bir bakışta", "Hedef", "Kavramlar ve olası zorluklar", "Ders akışı", "Bileşen kapsaması", "Farklılaştırma", "Uyarlarsanız"]},
    {"id": "calisma_kagidi", "bolumler": ["Başlayalım", "Deneyelim", "Çıkış kartı"]},
    {"id": "gozlem_formu", "bolumler": ["Nasıl kullanılır", "Gözlenecekler", "Programlar arası bileşenler (puansız)", "Çıkış kartı gruplaması"]}
  ]
}
```

Kurallar:
- Ortak içerik yalnız `ortak` altında yazılır; belgeler onu çeker. Bir soru iki belgede farklı yazılamaz.
- Çıktı metni birebir ve planda tek bir alıntı kutusunda; başka her yerde kod ve kısa ad.
- "Bir bakışta" bölümü evreleri dakikalarıyla tek satırda verir: "Ön değerlendirme 4 → Köprü 4 → Keşfet 14 → Tartış 10 → Genelle 4 → Çıkış 4".
- "Uyarlarsanız" son bölümdür: dersin dayandığı iki üç parça (ad öbeği olarak) ve kısa gerekçe; dersin merkezî temsili ve neden seçildiği.
- Gözlem formunda 8 satırlık boş tablo: Öğrenci (takma ad) · Görülen strateji · Sonraki adım.
