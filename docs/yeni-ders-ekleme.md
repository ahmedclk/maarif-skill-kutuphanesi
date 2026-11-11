# Yeni bir ders eklemek (ör. Fen Bilimleri)

1. **Programı oku:** dersin TYMM sayfasından sınıf ve tema kimliklerini bul; alan becerisi kod önekini `ortak/maarif/tymm-erisim.md` tablosundan al (Fen: FBAB).
2. **Veri:** `veri/tymm/<ders>/<sınıf>.yaml` dosyasını 6. sınıf matematik dosyası örneğiyle yaz; `dogrulama` alanını doldur. `ortak/betikler/tymm_kod_denetle.py` içindeki `DERS_ON` sözlüğüne dersin kod önekini ekle (ör. `"FEN": "fen-bilimleri"`).
3. **Ortak ders bilgisi:** `ortak/dersler/<ders>/` altında en az `beceri-eslemesi.md` (alan becerisi basamakları → bileşen fiilleri) ve gerekiyorsa soru dili dosyası.
4. **Skill ders dosyaları:** her skill için `skills/<skill>/references/dersler/<ders>.md` dosyasını `ortak/dersler/_sablon.md` ile yaz. Önce en çok kullanılacak üç skill (`maarif-cikti-cozumleme`, `maarif-ders-plani`, `maarif-anlama-kontrolu`).
5. **Skill gövdesi:** SKILL.md Adım 0'daki ders yönlendirmesine yeni dersi ekle (ör. "fen bilimleri → `references/dersler/fen-bilimleri.md`"). Açıklamada ders yalnız matematikle sınırlıysa ("Şu an matematik içindir") güncelle.
6. **Test:** tetikleme dosyalarına o derse ait en az üç istem ekle; işlev testini bir öğretmenle yap.
7. `python3 araclar/denetle.py && python3 araclar/paketle.py`.

Doğrulanmamış her bölüm "taslak" diye işaretlenir; öğretmen denemesinden geçmeden `kanit` alanı "denendi" yapılmaz.
