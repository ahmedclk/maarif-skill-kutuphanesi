# Remotion kuralları ve yerleşim sözleşmesi

## Remotion kuralları

- Her hareket kare numarasına bağlı olmalı: `useCurrentFrame()` ve `interpolate()` kullan. `interpolate` çağrılarına `{extrapolateLeft: "clamp", extrapolateRight: "clamp"}` ekle.
- CSS geçişi, CSS animasyonu, `setTimeout`, zamanlayıcılı `useEffect`, `Math.random()` ve `Date` kullanma.
- Sahneleri `<Sequence>` ile böl. Sahne içinde kare sayımı 0'dan başlar.

## Yerleşim sözleşmesi

- Her sahneyi yazmadan önce birbirine değmeyen kutular planla ve planı sahne bileşeninin üstüne yorum olarak yaz. Örnek: `// başlık 80,160-1000,320 | şekil 80,360-1000,1000 | metin 80,1040-1000,1480`
- Bir çizim tamamen kendi kutusunun içinde kalmalı. Şeklin ucu, tepesi ya da etiketi de çizime dahildir.
- Metin hiçbir çizginin ya da şeklin üstüne binmemeli. Etiketleri adlandırdıkları öğenin yanına kısa bir çizgiyle bağla. Etiketlerle diğer öğeler arasında en az 24 piksel boşluk bırak.
- Yeni bir adım eklemeden önce yerine geçtiği öğeyi ekrandan kaldır; ekranda öğe birikmesin.
- Zamanla öğe eklenen bir sahne, tamamen kurulmuş son hâlinde de çakışmasız olmalı.
- İşi bitirmeden önce her sahnenin son karesinin ekran görüntüsünü al ve çakışma olup olmadığını kontrol et.
