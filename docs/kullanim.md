# Kullanım

## Düzey 1 — Hazır istem (kurulum yok)

`istemler/<skill>.md` dosyasındaki istemi kopyalayın, köşeli parantezleri doldurun ve Claude'a yapıştırın. Skill yüklü değilse istemin başına dosyadaki tek cümlelik Maarif notunu ekleyin. Bu düzey denemek ve öğretmen eğitimi için uygundur; doğrulama betikleri çalışmaz.

## Düzey 2 — Skill yükleme (claude.ai ve masaüstü uygulaması)

1. `dist/zip/` klasöründen ihtiyaç duyduğunuz skill'lerin zip dosyalarını alın. Her zip kendi içinde eksiksizdir (ortak başvurular, veri ve betikler içindedir).
2. Claude ayarlarında skill bölümünden zip'i yükleyin ve açın.
3. Aynı işi yapan eski skill'leri kapatın (`ESKI-YENI.md`).
4. Normal bir istekle başlayın: "6. sınıf 1. tema için ders planı hazırla." Claude açıklamaya uyan skill'i kendisi seçer.

Öneri: Önce `maarif-cikti-cozumleme` ile başlayın; ürettiği çıktı kartını öteki skill'ler aynı sohbette doğrudan kullanır.

## Düzey 3 — Paket (Claude Code eklentisi)

Depo bir eklenti pazar yeridir (`.claude-plugin/marketplace.json`). Claude Code'da depoyu pazar yeri olarak ekleyip bir paketi kurun:

| Paket | İçerik |
| --- | --- |
| `maarif-ogretmen-temel` | Program okuma, takvim, ders planı, derse hazırlık, farklılaştırma, anlama kontrolü |
| `maarif-olcme-degerlendirme` | Anlama kontrolü, ortak yazılı, beceri temelli test, performans görevi, ikiz soru, hata analizi |
| `maarif-icerik-uretimi` | Konu özeti, anlatım videosu, ikiz soru |
| `dnamathos` | DNAMATHOS PDF ve Instagram skill'leri ile konu özeti ve yazılı |
| `maarif-tam` | Hepsi |

## Okulda yaygınlaştırma

- **Zümre:** Bir zümre öğretmeni `maarif-ogretmen-temel` paketini kurar ve haftalık zümre toplantısında bir iş akışını (`docs/is-akislari.md`) birlikte dener.
- **Geri bildirim:** Her denemeden sonra `KATKI.md` formu doldurulur; sorunlar ilgili skill'in ders dosyasına ya da tetikleme testine dönüşür.
- **Sınır:** Skill'ler öğretmenin yerine karar vermez; ürünün programa uygunluğunu son olarak öğretmen onaylar.
