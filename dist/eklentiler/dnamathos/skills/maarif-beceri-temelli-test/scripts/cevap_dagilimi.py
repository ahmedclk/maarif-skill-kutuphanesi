#!/usr/bin/env python3
"""Çoktan seçmeli cevap anahtarının dengesini denetler.

Kullanım: python3 cevap_dagilimi.py ABDCBADC... [--secenek 4]
Kurallar: her seçenek beklenen sayının ±%50'si içinde; aynı harf art arda en fazla 3 kez.
"""
import sys, argparse
from collections import Counter

ap = argparse.ArgumentParser()
ap.add_argument("anahtar")
ap.add_argument("--secenek", type=int, default=4)
a = ap.parse_args()
harf = "ABCDE"[: a.secenek]
k = a.anahtar.upper().replace(",", "").replace(" ", "")
bad = [c for c in k if c not in harf]
if bad:
    sys.exit(f"Geçersiz harf: {''.join(bad)}")
say = Counter(k)
bek = len(k) / a.secenek
ihlal = [f"{h}: {say[h]} kez (beklenen ≈ {bek:.1f})" for h in harf if abs(say[h] - bek) > max(1, bek * 0.5)]
seri, en = 1, 1
for i in range(1, len(k)):
    seri = seri + 1 if k[i] == k[i - 1] else 1
    en = max(en, seri)
if en > 3:
    ihlal.append(f"aynı harf art arda {en} kez")
print("Dağılım:", ", ".join(f"{h}={say[h]}" for h in harf))
for i in ihlal:
    print("İHLAL ", i)
sys.exit(1 if ihlal else 0)
