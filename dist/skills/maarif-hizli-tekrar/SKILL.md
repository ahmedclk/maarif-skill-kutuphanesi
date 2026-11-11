---
name: maarif-hizli-tekrar
description: Ders başında 5 dakikalık hızlı soru-cevap turu ve haftanın akılda kalıcı sloganını hazırlar; soruları aralıklı tekrar kuralıyla geçen haftadan ve daha önceki haftalardan karışık seçer, doğru-yanlış, boşluk tamamla, hatayı bul ve hızlı hesap gibi kısa biçimler kullanır; her sloganı matematiksel doğruluk, sınır ve karşı örnek denetiminden geçirir ve ardına bir neden sorusu ekler. Tetikleyiciler - ders başı tekrar, hızlı soru cevap, ısınma soruları, haftanın sloganı, akılda kalıcı kural, flaş kart, aralıklı tekrar, geçen haftaları da tekrar ettir, sınıfla hızlı yarışma. Haftalık kavrama ölçümü ve ödev kararı için değil (maarif-kavrama-testi), ders sonu çıkış kartı için değil (maarif-anlama-kontrolu), konu özeti slaytı için değil (maarif-konu-ozeti), Instagram gönderisi için değil (dnamathos-instagram-karusel). Konu özeti istendiğinde ayrıca yüklenmez; maarif-konu-ozeti ısınma turunu ve sloganı varsayılan olarak kendisi üretir.
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: TYMM sayfaları için web erişimi; Python 3 (tekrar seçimi).
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: TYMM süreç bileşenleri ve içerik çerçevesi; MEB kısa süreli sınav (notsuz)
  dersler: matematik (tam); diğerleri şablonla
  kanit: taslak
---

# Maarif hızlı tekrar

Amaç: Öğrencinin sevdiği hızlı soru-cevabı, öğrenmeyi en çok güçlendiren biçimde kurmak: **hatırlama** (cevabı bakmadan üretmek), **aralıklı tekrar** (geçen hafta ve daha öncesi) ve **karışık sıra** (konular art arda değil, karışık). Slogan bu turun sonunda gelir ve bir kuralı hatırlatır; anlamanın yerine geçmez. Tur notsuzdur (MEV-40, `references/ortak/maarif/meb-olcme-mevzuati.md`).

Dil: `references/ortak/uslup/turkce-yazim.md`; öğrenci sesi sıcak ve kısa, argo ve abartı yok.

## Adım 0 — Yönlendirme (sessiz)

1. `references/ortak/maarif/cerceve.md`, `references/ortak/maarif/tymm-erisim.md`, `references/ortak/maarif/meb-olcme-mevzuati.md`.
2. Ders dosyası: matematik → `references/dersler/matematik.md` (şimdi oku). Yoksa `references/ortak/dersler/_sablon.md`.
3. `references/ortak/haftalik/hizli-tekrar-bicimleri.md` ve `references/ortak/haftalik/slogan-olcutu.md` dosyalarını oku.
4. Aynı oturumda `kavrama_gecmisi.json` (maarif-kavrama-testi) ya da bir ders takvimi varsa onu kullan.

## Adım 1 — Netleştirme (en fazla bir soru)

Bu hafta hangi konu işlendiyse onu bilmen yeter; belli değilse yalnız onu sor. Varsayılanlar: 8 soru, 5 dakika, birebir ders (grup dersinde "yarışma" biçimi önerilir).

## Adım 2 — Programa dayandır

Turdaki her soru bir bileşene bağlıdır; bileşen ve sınırlar tema sayfasından alınır. Slogan da İçerik Çerçevesindeki terim ve gösterimle yazılır; programın değinmediği bir kavram (ör. 6. sınıfta EBOB ve EKOK) sloganda geçmez.

## Adım 3 — Soruları seç

- `kavrama_gecmisi.json` varsa: `python3 scripts/tekrar_sec.py --hafta <bu hafta> --gecmis kavrama_gecmisi.json [--ogrenci "<takma ad>"] --soru 8`. Betik, takılan bileşenleri ve 1, 2, 4, 8 hafta önce işlenenleri seçer.
- Yoksa işlenen konuları `konular.json` olarak yaz (bileşen → işlendiği hafta) ve `--konular konular.json` ile çalıştır. O da yoksa: 4 soru geçen haftadan, 3 soru 2–4 hafta önceden, 1 soru daha eskiden.
- Sırayı karıştır: aynı konudan iki soru art arda gelmez.

## Adım 4 — Soruları yaz

`hizli-tekrar-bicimleri.md` dosyasındaki biçimlerle. Kurallar: her soru en çok 20 saniyede cevaplanır (zihinden ya da tek satır); en az iki farklı biçim; en az bir "hatayı bul" (kavram yanılgısını yüzeye çıkarır); cevaplar kodla doğrulanır; her sorunun tek cevabı vardır.

## Adım 5 — Haftanın sloganı

`slogan-olcutu.md` dosyasındaki beş denetimi uygula. Her slogan şu dördüyle teslim edilir: slogan · neyi hatırlattığı (tam kural, bir cümle) · sınırı ya da karşı örneği · "Neden?" sorusu ve kısa cevabı. Slogan hafta boyunca aynı kalır; konu özetindeki Kaydet kartıyla aynı kuralı söyler. Geçmiş sloganlar `slogan_bankasi.json` dosyasında birikir; turun son sorusu çoğu zaman eski bir sloganı tamamlatmaktır.

## Adım 6 — Çıktı

`references/ortak/haftalik/hizli-tekrar-cikti-bicimi.md`:

1. **Tur kartları:** her soru bir ekran (16:9), büyük yazı; sunumda tek tek açılır. Cevap bir sonraki ekranda. DNAMATHOS tasarımı istenirse ve `dnamathos-pdf-tasarimi` yüklüyse onun tasarımıyla.
2. **Öğretmen listesi:** tek sayfa; soru · cevap · bileşen · yaygın yanlış cevap ve ona söylenecek tek cümle.
3. **Slogan kartı** ve `slogan_bankasi.json` güncellemesi.
4. İstenirse karusel ya da kısa video için malzeme (soru, cevap, slogan); üretimi ilgili skill yapar.

## Adım 7 — Doğrulama

1. Her cevap kodla ya da elle yeniden çözüldü; her soru 20 saniyelik sınırda.
2. Slogan beş denetimden geçti; karşı örnek gerçekten sınandı (kodla ya da örnek sayılarla).
3. Turda aynı konudan art arda iki soru yok; en az iki biçim var.
4. `python3 scripts/tymm_kod_denetle.py <öğretmen listesi> --veri references/veri` 0 hata.

## Adım 8 — Kapanış

En fazla iki somut seçenek: "Bu turu Instagram için kendini dene karuseline çevireyim mi?" (dnamathos-instagram-karusel) ya da "Haftanın sloganı için 30 saniyelik video hazırlayayım mı?" (maarif-anlatim-videosu).

## Denetim listesi

- [ ] 8 soru (ya da istenen sayı); geçen hafta ve önceki haftalar karışık
- [ ] Her soru ≤ 20 saniye; en az iki biçim ve bir "hatayı bul"
- [ ] Slogan doğru, sınırı belli, karşı örnekle sınandı, neden sorusu var
- [ ] Program sınırı ve gösterimi korunmuş
- [ ] Tur notsuz; öğretmen listesi yanlış cevaba tek cümlelik dönüt veriyor
