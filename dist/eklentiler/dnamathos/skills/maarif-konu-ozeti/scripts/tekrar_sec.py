#!/usr/bin/env python3
"""Aralıklı tekrar: ders başı turunda hangi bileşenlerin sorulacağını seçer.

Girdi: kavrama_gecmisi.json (kavrama_karari.py yazar) ya da işlenen konular listesi.
Kural (haftalık ders düzeni): bir bileşen işlendiği haftadan 1, 2, 4 ve 8 hafta sonra tekrar edilir.
Son kararı "Kısa telafi" ya da "Yeniden ele al" olan bileşen aralığa bakılmaksızın bu hafta sorulur;
iki ayrı haftada "Geçti" almış (kalıcı) bileşen yalnız 8 haftalık tekrarda sorulur.

Kullanım:
  python3 tekrar_sec.py --hafta 9 --gecmis kavrama_gecmisi.json [--ogrenci "Öğrenci A"] [--soru 8]
  python3 tekrar_sec.py --hafta 9 --konular konular.json [--soru 8]    # konular.json: {"6.1.4-a": 7, "6.1.2-ç": 5, ...}
Çıktı: seçilen bileşenler ve tur dağılımı (geçen hafta / 2–4 hafta / daha eski).
"""
import argparse, json

ARALIK = (1, 2, 4, 8)
ap = argparse.ArgumentParser()
ap.add_argument("--hafta", type=int, required=True)
ap.add_argument("--gecmis"); ap.add_argument("--konular"); ap.add_argument("--ogrenci")
ap.add_argument("--soru", type=int, default=8)
a = ap.parse_args()

aday = {}  # bileşen -> (öncelik, ilk hafta, son karar)
if a.gecmis:
    g = json.load(open(a.gecmis, encoding="utf-8"))
    ogrenciler = [a.ogrenci] if a.ogrenci else list(g)
    for o in ogrenciler:
        for b, e in g[o].items():
            kayit = e["kayit"]
            ilk, son = e["islendi"], kayit[-1][1]
            kalici = sum(1 for x in kayit if x[1] == "Geçti") >= 2
            fark = a.hafta - ilk
            if son != "Geçti":
                p = 3 if son == "Yeniden ele al" else 2
            elif kalici:
                p = 1 if fark == 8 else 0
            else:
                p = 1 if fark in ARALIK else 0
            if p:
                aday[b] = max(aday.get(b, (0, ilk, son)), (p, ilk, son))
elif a.konular:
    for b, ilk in json.load(open(a.konular, encoding="utf-8")).items():
        if a.hafta - ilk in ARALIK:
            aday[b] = (1, ilk, "—")
secilen = sorted(aday.items(), key=lambda x: (-x[1][0], -x[1][1]))[: a.soru]
kova = {"geçen hafta": 0, "2–4 hafta önce": 0, "daha eski": 0}
for b, (p, ilk, son) in secilen:
    f = a.hafta - ilk
    kova["geçen hafta" if f <= 1 else "2–4 hafta önce" if f <= 4 else "daha eski"] += 1
    print(f"{b:10} işlendi: {ilk}. hafta ({f} hafta önce) · son karar: {son} · öncelik {p}")
print("Dağılım:", ", ".join(f"{k} {v}" for k, v in kova.items()))
if len(secilen) < a.soru:
    print(f"Not: {a.soru - len(secilen)} soru boş; geçen haftanın bileşenlerinden tamamla.")
