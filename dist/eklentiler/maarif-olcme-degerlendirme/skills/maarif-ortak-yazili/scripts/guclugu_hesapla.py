#!/usr/bin/env python3
"""Z · Y · C güçlük kuralı ve puan denetimi (ortak/dersler/matematik/guclugu-belirleme.md).

Girdi: JSON listesi. Her öğe bir alt maddedir:
  {"kagit": "K1", "soru": 1, "madde": "1.1", "Z": 2, "Y": "acik", "C": "H", "puan": 6}
  Y: "yonlendirilmis" | "acik"   C: "H" | "A" | "G"
  İsteğe bağlı: "tur": "acik" | "kisa" | "coktan" | "dy" | "eslestirme"   "sure_dk": tahmini çözüm süresi
Kullanım: python3 guclugu_hesapla.py maddeler.json [--kademe ortaokul|lise] [--yazili]
--yazili: MEB okul yazılısı kuralları da denetlenir (ortak/maarif/meb-olcme-mevzuati.md):
  MEV-10/11 yalnız kısa cevaplı kâğıt olamaz · MEV-12 çoktan seçmeli, gerekçesiz doğru-yanlış ve eşleştirme yok ·
  MEV-16 kâğıt başına tahmini süre ≤ 40 dakika · MEV-19 toplam 100.
Çıkış kodu: kural ihlali varsa 1.
"""
import json, sys, argparse
from collections import defaultdict


def guclugu(z, y, c):
    if c == "G" or (y == "acik" and z >= 2) or z >= 3:
        return "zor"
    if z == 1 and y == "yonlendirilmis" and c == "H":
        return "kolay"
    return "orta"


PAY = {"kolay": (15, 25), "orta": (45, 55), "zor": (25, 35)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dosya")
    ap.add_argument("--kademe", default="lise")
    ap.add_argument("--yazili", action="store_true")
    a = ap.parse_args()
    maddeler = json.load(open(a.dosya, encoding="utf-8"))
    ihlal = []
    kagit = defaultdict(lambda: defaultdict(int))
    soru = defaultdict(int)
    for m in maddeler:
        g = guclugu(int(m["Z"]), m["Y"], m["C"])
        if m.get("guclugu") and m["guclugu"] != g:
            ihlal.append(f"{m['kagit']} {m['madde']}: etiket '{m['guclugu']}', kural '{g}' diyor")
        m["guclugu"] = g
        kagit[m["kagit"]][g] += m["puan"]
        soru[(m["kagit"], m["soru"])] += m["puan"]
        print(f"{m['kagit']:>3} {m['madde']:>5}  Z={m['Z']} Y={m['Y'][:5]:5} C={m['C']}  {g:5} {m['puan']:>3} puan")
    for (k, s), p in soru.items():
        if not 10 <= p <= 20:
            ihlal.append(f"{k} soru {s}: toplam {p} puan (10–20 olmalı)")
    paylar = {}
    for k, d in kagit.items():
        top = sum(d.values())
        if top != 100:
            ihlal.append(f"{k}: toplam {top} puan (100 olmalı)")
        paylar[k] = {g: round(100 * d[g] / top) for g in PAY}
        for g, (lo, hi) in PAY.items():
            if not lo <= paylar[k][g] <= hi:
                ihlal.append(f"{k}: {g} payı %{paylar[k][g]} (%{lo}–{hi} olmalı)")
        print(f"{k}: " + ", ".join(f"{g} %{v}" for g, v in paylar[k].items()))
    if len(paylar) > 1:
        for g in PAY:
            v = [p[g] for p in paylar.values()]
            if max(v) - min(v) > 10:
                ihlal.append(f"{g} payı kâğıtlar arasında {max(v) - min(v)} puan farklı (≤ 10 olmalı)")
    if a.yazili:
        kagitlar = sorted({m["kagit"] for m in maddeler})
        for k in kagitlar:
            km = [m for m in maddeler if m["kagit"] == k]
            turler = [m.get("tur") for m in km]
            if None in turler:
                ihlal.append(f"{k}: bazı maddelerde 'tur' alanı yok (MEV-10 denetlenemez)")
            if turler and all(t == "kisa" for t in turler):
                ihlal.append(f"{k}: kâğıt yalnız kısa cevaplı maddelerden oluşuyor (MEV-11)")
            for m in km:
                if m.get("tur") in ("coktan", "dy", "eslestirme"):
                    ihlal.append(f"{k} {m['madde']}: '{m['tur']}' türü okul yazılısında kullanılmaz; gerekçeli biçime çevir (MEV-12)")
            sure = sum(float(m.get("sure_dk", 0)) for m in km)
            if any("sure_dk" in m for m in km):
                print(f"{k}: tahmini süre {sure:.0f} dk")
                if sure > 40:
                    ihlal.append(f"{k}: tahmini süre {sure:.0f} dk; bir ders saatini (40 dk) aşıyor (MEV-16)")
            else:
                ihlal.append(f"{k}: 'sure_dk' verilmedi (MEV-16 denetlenemez)")
    for i in ihlal:
        print("İHLAL ", i)
    print(f"Sonuç: {len(ihlal)} ihlal")
    sys.exit(1 if ihlal else 0)


if __name__ == "__main__":
    main()
