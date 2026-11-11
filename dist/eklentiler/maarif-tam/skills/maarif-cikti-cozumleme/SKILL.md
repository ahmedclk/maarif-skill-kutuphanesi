---
name: maarif-cikti-cozumleme
description: Bir dersin, sınıfın, temanın ya da tek bir öğrenme çıktısının Maarif Modeli programını TYMM sayfasından okuyup çözümler; çıktı metnini, süreç bileşenlerini, beceri basamaklarını, içerik çerçevesi sınırlarını, temada geçen eğilim, SDB, değer ve okuryazarlık kodlarını tek bir çıktı kartında toplar. Netleştirici soru sormadan önce yükle. Tetikleyiciler - kazanımları çıkar, bu temanın öğrenme çıktıları neler, MAT.6.1.3 bileşenleri, programda bu konunun sınırı ne, ders kitabındaki konu hangi çıktıya denk geliyor. Diğer Maarif skill'lerinin ilk adımıdır ve onlara çıktı kartını verir. Ders planı için değil (maarif-ders-plani), haftalık takvim için değil (maarif-ders-takvimi), soru ya da sınav üretmek için değil (maarif-ortak-yazili, maarif-beceri-temelli-test).
license: Lisans kararı bekliyor; bkz. depo kökündeki LISANS.md
compatibility: TYMM sayfalarını okumak için web erişimi (WebFetch) gerekir; erişim yoksa öğretmenin verdiği metinle çalışır.
metadata:
  surum: "1.0.0"
  yazar: DNAMATHOS
  omurga: Türkiye Yüzyılı Maarif Modeli, TYMM öğretim programları
  dersler: matematik (tam); diğer dersler references/dersler/_sablon.md ile eklenir
  kanit: 6. ve 9. sınıf matematik temalarında kullanıldı (2026)
---

# Maarif çıktı çözümleme

Amaç: Öğretmenin ve öteki skill'lerin üzerine kuracağı tek ve doğru bir **çıktı kartı** hazırlamak. Kart, programın söylediğini birebir aktarır, söylemediğini uydurmaz ve her bileşenin hangi beceri basamağına dayandığını gösterir. Bütün kütüphane bu kartın doğruluğuna yaslanır.

"Öğretmen", konuştuğun kullanıcıdır. Öğretmene giden her metin `references/ortak/uslup/onyargisiz-dil.md` ve `references/ortak/uslup/turkce-yazim.md` kurallarına uyar; çalışırken ve kapanışta `references/ortak/uslup/ilerleme-ve-kapanis.md` uygulanır.

## Adım 0 — Yönlendirme (sessiz)

1. **Omurga:** `references/ortak/maarif/cerceve.md` ve `references/ortak/maarif/tymm-erisim.md` dosyalarını şimdi oku. Kod adlarını ve sayfa başlıklarını yalnız buradan al.
2. **Ders:** Dersi istekten çıkar ve `references/dersler/<ders>.md` dosyasını oku (matematik → `references/dersler/matematik.md`). Bu dosyayı okumadan çözümleme yapmak kritik hatadır. Ders dosyası yoksa `references/ortak/dersler/_sablon.md` başlıklarını izleyerek doğrudan tema sayfasıyla çalış ve kartın sonuna "Bu ders için ayrıntılı ders dosyası henüz yok; çözümleme program sayfasına dayanır." notunu ekle.
3. **Veri:** `references/veri/tymm/` altında o sınıfın dosyası varsa kodları ve bileşen harflerini ilk bakış için oradan al; birebir metni yine sayfadan oku.

## Adım 1 — Netleştirme (en fazla bir soru)

Yalnız cevabı kartı değiştiriyorsa sor: sınıf belli değilse ya da konu iki temaya denk geliyorsa. Ders kitabı sayfaları verildiyse tema numarasını kitaptan değil siteden eşle; fark varsa kartta belirt, soru sorma.

## Adım 2 — Programı oku

`tymm-erisim.md` yolunu izle: ders sayfası → sınıf sayfası → tema sayfası. Ünite kimliğini tahmin etme. Sayfadan şunları al: başlık kod listeleri, Öğrenme Çıktıları ve Süreç Bileşenleri (birebir), İçerik Çerçevesi (Genellemeler, Anahtar Kavramlar, Sembol ve Gösterimler), Öğrenme Kanıtları, Öğrenme-Öğretme Yaşantıları (Temel Kabuller, Ön Değerlendirme Süreci, Köprü Kurma, çıktı başına uygulamalar ve sınırlamalar), Farklılaştırma. Boş başlığı ("-") boş olarak yaz.

Sayfa açılmazsa `tymm-erisim.md` "Bağlantı yoksa" kuralını uygula.

## Adım 3 — Çözümle

Her çıktı için:

1. **Bileşen → basamak eşlemesi:** Her bileşenin fiiline bakarak becerinin süreç basamağını yaz (matematikte `references/ortak/dersler/matematik/beceri-eslemesi.md`). Eşleme senin yorumundur; kartta "eşleme: yorum" diye işaretlenir.
2. **Ölçülebilirlik:** Her bileşeni "yazılıda ölçülür", "süreç içinde gözlenir" ya da "performans görevine bırakılır" diye sınıfla ve bir gerekçe yaz (ders dosyasındaki kural).
3. **Sınırlar:** İçerik Çerçevesi ve uygulamalardaki "…'e girilmez", "… ile sınırlandırılır" ifadelerini ayrı bir "Sınırlar" listesine birebir aktar.
3a. **Uygulamadaki işlemler ve terimler:** Öğrenme-Öğretme Uygulamalarında öğrenciden istenen ama bileşen listesinde adı geçmeyen işlemleri (ör. 6.1.5'te yuvarlama) "uygulama_islemleri" alanına, İçerik Çerçevesi terimlerini (ör. 6.6.1'de "Deneysel Olasılık") "icerik_terimleri" alanına birebir yaz. Gerçek ortak sınav bu işlemlerden de soru sordu.
4. **Programlar arası bileşenler:** Tema başlığındaki E, SDB, D, OB kodlarından her birinin uygulamalarda hangi davranışın arkasında geçtiğini yaz ("birbirlerini dinlemeleri (SDB2.1)"). Uygulamada geçmeyen kodu "yalnız listede" diye işaretle. Bunlar puanlanmaz (`cerceve.md` 8. bölüm).
5. **Kitap eşlemesi (varsa):** Ders kitabı ya da kaynak kitap verildiyse kitap bölümü → çıktı ve bileşen eşlemesi; basılı sayfa numarasıyla.

## Adım 4 — Çıktı kartı

Biçim ve alanlar `references/cikti-karti.md` dosyasındadır; önce onu oku. Kart iki biçimde teslim edilir:

- **Öğretmen için:** okunur tablo (sohbette ya da belge olarak; öğretmen saklayacaksa Docs türünden belge).
- **Öteki skill'ler için:** `cikti.json` (aynı alanlar). Aynı oturumda `maarif-ders-plani`, `maarif-ortak-yazili` gibi bir skill çalışacaksa bu dosyayı kullanır ve programı yeniden okumaz.

## Adım 5 — Doğrulama

Kart yazıldıktan sonra:

- `python3 scripts/tymm_kod_denetle.py cikti.json --veri references/veri` çalıştır; hata 0 olmalı. Uyarıları tema sayfasından tek tek doğrula.
- Birebir alanlarındaki her cümleyi sayfadaki metinle karşılaştır (WebFetch'e tek çıktıyı ayrı istekle sor). Kısaltılmış metin "birebir" alanında kalamaz.
- Kartta, sayfada olmayan bir sınır ya da kod yok.

## Adım 6 — Kapanış

Kartı bir satırla sun ("6. sınıf 1. Tema'nın dört çıktısı ve bileşenleri hazır."). Kitap ile site arasındaki farkı bir satırla söyle. En fazla iki somut seçenek sun; ör. "Bu kartla bir haftalık takvim çıkarayım mı?" (maarif-ders-takvimi) ya da "İlk çıktı için ders planı hazırlayayım mı?" (maarif-ders-plani).

## Denetim listesi

- [ ] Ders dosyası ve omurga dosyaları okundu
- [ ] Çıktı metni ve bileşenler sayfadan birebir; kısaltma yalnız "kısa ad" alanında
- [ ] Her bileşene basamak ve ölçülebilirlik yazıldı; eşleme "yorum" diye işaretli
- [ ] Sınırlar birebir ve ayrı listede
- [ ] E, SDB, D, OB yalnız tema listesinden; uygulamadaki davranışla eşlendi
- [ ] Kod denetimi 0 hata
- [ ] Bağlantı yoksa not eklendi, uydurma atıf yok
