#!/usr/bin/env python3
"""TYMM kod denetimi: bir ürün dosyasındaki çıktı, bileşen ve beceri kodlarını program verisiyle sınar.

Kullanım:
  python3 tymm_kod_denetle.py URUN [URUN ...] [--veri references/veri] [--kati]

URUN: .html, .md, .txt, .json ya da .pdf. --veri klasörü kodlar.yaml ve <ders>/<sınıf>.yaml dosyalarını içerir.
Çıkış kodu: hata varsa 1. Uyarılar çıkış kodunu değiştirmez (--kati verilirse değiştirir).
"""
import argparse, glob, os, re, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML gerekli: pip install pyyaml")

DERS_ON = {"MAT": "matematik"}
CIKTI = re.compile(r"\b(MAT|TUR|FEN|SOS|ING)\.(\d{1,2})\.(\d{1,2})\.(\d{1,2})\b")
BILESEN = re.compile(r"\b(\d{1,2})\.(\d{1,2})\.(\d{1,2})-([a-zçğıöşü])\b")
BECERI = re.compile(r"\b(KB[123](?:\.\d{1,2}){0,2}|MAB\d(?:\.\d)?|SDB[123](?:\.\d)?|E[123](?:\.\d{1,2})?|OB\d(?:\.\d)?)(?:\.SB\d)?\b")


def metin_oku(yol):
    if yol.lower().endswith(".pdf"):
        from pypdf import PdfReader
        return "\n".join((p.extract_text() or "") for p in PdfReader(yol).pages)
    with open(yol, encoding="utf-8", errors="replace") as f:
        t = f.read()
    return re.sub(r"<[^>]+>", " ", t) if yol.lower().endswith((".html", ".htm")) else t


def veri_yukle(kok):
    kodlar = yaml.safe_load(open(os.path.join(kok, "tymm", "kodlar.yaml"), encoding="utf-8"))["kodlar"]
    siniflar = {}
    for y in glob.glob(os.path.join(kok, "tymm", "*", "*.yaml")):
        d = yaml.safe_load(open(y, encoding="utf-8"))
        siniflar[(os.path.basename(os.path.dirname(y)), int(d["sinif"]))] = d["ciktilar"]
    return kodlar, siniflar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urun", nargs="+")
    ap.add_argument("--veri", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "veri"))
    ap.add_argument("--kati", action="store_true")
    a = ap.parse_args()
    if not os.path.isdir(a.veri):
        alt = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "veri")
        a.veri = alt if os.path.isdir(alt) else a.veri
    kodlar, siniflar = veri_yukle(a.veri)
    hata, uyari = [], []
    for yol in a.urun:
        t = metin_oku(yol)
        gorulen = set()
        for m in CIKTI.finditer(t):
            on, s, tema, sira = m.groups()
            kod = m.group(0)
            gorulen.add(kod)
            ders = DERS_ON.get(on)
            veri = siniflar.get((ders, int(s))) if ders else None
            if veri is None:
                uyari.append(f"{kod}: {s}. sınıf için veri dosyası yok; tema sayfasından doğrula")
            elif kod not in veri:
                hata.append(f"{kod}: program verisinde yok")
        for m in BILESEN.finditer(t):
            s, tema, sira, harf = m.groups()
            kod = f"MAT.{s}.{tema}.{sira}"
            veri = siniflar.get(("matematik", int(s)))
            if veri and kod in veri and harf not in veri[kod]["bilesenler"]:
                hata.append(f"{s}.{tema}.{sira}-{harf}: bu çıktının böyle bir bileşeni yok")
        for m in BECERI.finditer(t):
            k = m.group(1)
            if k in kodlar:
                continue
            if re.fullmatch(r"KB2\.16\.\d", k):
                uyari.append(f"{k}: KB2.16 alt kodu; tema sayfasından doğrula")
            else:
                hata.append(f"{k}: TYMM kod listesinde yok")
        print(f"{yol}: {len(gorulen)} çıktı kodu tarandı")
    for h in sorted(set(hata)):
        print("HATA  ", h)
    for u in sorted(set(uyari)):
        print("UYARI ", u)
    print(f"Sonuç: {len(set(hata))} hata, {len(set(uyari))} uyarı")
    sys.exit(1 if hata or (a.kati and uyari) else 0)


if __name__ == "__main__":
    main()
