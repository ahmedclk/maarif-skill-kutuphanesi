#!/usr/bin/env python3
"""Kavrama testi sonuçlarından öğrenci ve bileşen başına karar ve hedefli ödev sayısı üretir.

Kurallar: ortak/haftalik/kavrama-karar-kurali.md (dağıtımda references/ortak/haftalik/)
Kullanım: python3 kavrama_karari.py kavrama_sonuc.json [--gecmis kavrama_gecmisi.json] [--ust 6]
Çıktı: karar tablosu (ekrana) ve kavrama_karar.json; --gecmis verilirse geçmiş dosyası güncellenir.
"""
import argparse, json, os
from collections import defaultdict

SIRA = {"Geçti": 0, "Kısa telafi": 1, "Yeniden ele al": 2}
ODEV = {"Geçti": 0, "Kısa telafi": 2, "Yeniden ele al": 3}

ap = argparse.ArgumentParser()
ap.add_argument("sonuc"); ap.add_argument("--gecmis"); ap.add_argument("--ust", type=int, default=6)
a = ap.parse_args()
d = json.load(open(a.sonuc, encoding="utf-8"))
gecmis = json.load(open(a.gecmis, encoding="utf-8")) if a.gecmis and os.path.exists(a.gecmis) else {}
cikti = {"hafta": d["hafta"], "ogrenciler": {}}

for ogr, cevaplar in d["ogrenciler"].items():
    puanlar, bayrak = defaultdict(list), defaultdict(set)
    for sid, s in d["sorular"].items():
        c = cevaplar.get(sid, {"cevap": 0, "gerekce": 0, "emin": 0})
        p = (float(c["cevap"]) + float(c["gerekce"])) / 2
        for b in s["bilesenler"]:
            puanlar[b].append(p)
            if not c["cevap"] and c.get("emin"):
                bayrak[b].add("emin-yanlis")
            if c["cevap"] and not c["gerekce"]:
                bayrak[b].add("gerekcesiz")
    kararlar = {}
    for b, ps in puanlar.items():
        ort = sum(ps) / len(ps)
        k = "Geçti" if ort >= 0.85 else "Kısa telafi" if ort >= 0.5 else "Yeniden ele al"
        if "emin-yanlis" in bayrak[b]:
            k = "Yeniden ele al"
        elif "gerekcesiz" in bayrak[b] and k == "Geçti":
            k = "Kısa telafi"
        kararlar[b] = {"puan": round(ort, 2), "karar": k, "isaret": sorted(bayrak[b])}
    # Ödev: öncelik emin-yanlış > yeniden > kısa telafi; üst sınır
    sirali = sorted(kararlar.items(), key=lambda x: (-("emin-yanlis" in x[1]["isaret"]), -SIRA[x[1]["karar"]], x[0]))
    # Haftanın bileşenlerinin yarısı ya da fazlası "Yeniden ele al" ise ödev çözüm değildir: konu derste yeniden işlenir.
    hafta_b = [b for s in d["sorular"].values() if s.get("tur") != "tekrar" for b in s["bilesenler"]]
    hafta_b = sorted(set(hafta_b))
    yeniden = [b for b in hafta_b if b in kararlar and kararlar[b]["puan"] < 0.5]
    konu_yeniden = bool(hafta_b) and len(yeniden) * 2 >= len(hafta_b)
    kalan, odev, ertelenen = (3 if konu_yeniden else a.ust), {}, []
    for b, k in sirali:
        n = ODEV[k["karar"]]
        if not n:
            continue
        if n <= kalan:
            odev[b] = n; kalan -= n
        else:
            ertelenen.append(b)
    # Geçmiş ve kalıcılık
    g = gecmis.setdefault(ogr, {})
    islendi = {b: s.get("islendi", d["hafta"]) for s in d["sorular"].values() for b in s["bilesenler"]}
    for b, k in kararlar.items():
        e = g.setdefault(b, {"islendi": islendi[b], "kayit": []})
        e["islendi"] = min(e["islendi"], islendi[b])
        kayit = [x for x in e["kayit"] if x[0] != d["hafta"]] + [[d["hafta"], k["karar"]]]
        e["kayit"] = kayit
        k["kalici"] = sum(1 for x in kayit if x[1] == "Geçti") >= 2
    cikti["ogrenciler"][ogr] = {"bilesenler": kararlar, "odev": odev, "odev_toplam": sum(odev.values()), "ertelenen": ertelenen,
                                "konu_yeniden": konu_yeniden}
    print(f"\n{ogr}")
    for b, k in sorted(kararlar.items()):
        isaret = (" · " + ", ".join(k["isaret"])) if k["isaret"] else ""
        print(f"  {b:10} {k['puan']:.2f}  {k['karar']:15} ödev {odev.get(b, 0)}{isaret}{' · kalıcı' if k['kalici'] else ''}")
    print(f"  Toplam ödev: {sum(odev.values())} soru" + (f" · sonraki haftaya: {', '.join(ertelenen)}" if ertelenen else ""))
    if konu_yeniden:
        print("  KONU YENİDEN: haftanın bileşenlerinin yarısında ya da fazlasında puan 0,5'in altında. Sonraki derste 10–15 dakika yeniden işleyin; ödev 3 soruyla sınırlı.")

json.dump(cikti, open(os.path.splitext(a.sonuc)[0].replace("_sonuc", "") + "_karar.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
if a.gecmis:
    json.dump(gecmis, open(a.gecmis, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
