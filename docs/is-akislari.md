# İş akışı tarifleri

Her tarif aynı sohbette sırayla çalıştırılır; bir skill'in ürünü sonrakinin girdisidir.

## Yazılıya 8 hafta kala

1. `maarif-cikti-cozumleme` — senaryodaki çıktıların kartı ("Ekteki senaryodaki çıktıların kartını çıkar.")
2. `maarif-ders-takvimi` — 8 derslik takvim, son ders tekrar ve prova
3. `maarif-konu-ozeti` — her hafta o haftanın konu özeti ve ödev kartı
4. `maarif-anlama-kontrolu` — her dersin sonunda bir çıkış kartı
5. `maarif-ortak-yazili` — 7. hafta: senaryoya uyan prova kâğıtları
6. `maarif-hata-analizi` — prova sonuçlarına göre telafi planı
7. `maarif-benzer-soru` — en sık iki hata örüntüsü için ikiz soru seti

## Haftalık döngü (az ödev, kalıcı öğrenme)

Konu özeti isterseniz bu döngünün tamamı tek istekle gelir; `maarif-konu-ozeti` ısınma turunu, sloganı ve kavrama testini varsayılan olarak üretir. Ders planıyla çalışıyorsanız parçaları ayrı isteyin:

1. `maarif-hizli-tekrar` — dersin ilk 5 dakikası: geçen hafta ve öncesinden karışık 6–8 soru, haftanın sloganı
2. `maarif-konu-ozeti` ya da `maarif-ders-plani` — haftanın konusu
3. `maarif-kavrama-testi` — konu bitince 4 soruluk notsuz test
4. Sonuçlar girilince (`kavrama_karari.py`) — öğrenci başına karar ve en çok 6 soruluk hedefli ödev
5. Sonraki hafta — takılan bileşenler ısınma turunun başına gelir

## Yeni bir temaya başlarken

1. `maarif-cikti-cozumleme` — tema kartı (temel kabuller, ön değerlendirme, köprü kurma)
2. `maarif-anlama-kontrolu` — ön değerlendirme kontrolü (ön koşul bileşeni)
3. `maarif-ders-plani` — ilk dersin paketi
4. `maarif-farklilastirma` — ön değerlendirme sonucuna göre üç grup
5. `maarif-derse-hazirlik` — dersten bir gün önce

## Dönem içi süreç değerlendirmesi

1. `maarif-performans-gorevi` — yazılı dışı bileşenler için görev ve dereceli anahtar
2. `maarif-anlama-kontrolu` — ara teslimlerde kısa kontroller
3. `maarif-hata-analizi` — sınıf düzeyi rapor ve destekleme grubu

## DNAMATHOS haftalık üretim

1. `maarif-konu-ozeti` + `dnamathos-pdf-tasarimi` — haftanın ders PDF'leri
2. `dnamathos-instagram-karusel` — aynı konunun ızgara satırı
3. `maarif-anlatim-videosu` — satırın konusu için Shorts
