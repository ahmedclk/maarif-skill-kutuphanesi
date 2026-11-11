#!/usr/bin/env python3
"""Öğrenci dosyasında cevap sızıntısı arar.

Kullanım: python3 sizinti_ara.py OGRENCI_DOSYASI cevaplar.json
cevaplar.json: ["36", "2/5", "0,4", "asal değildir", ...] — cevap anahtarındaki ayırt edici dizgeler.
Öğrenci dosyası .pdf, .html, .md ya da .txt olabilir. Bulunan her dizge, bağlamıyla yazdırılır.
Kısa sayısal dizgeler (1–2 karakter) yanlış alarm üretir; onları listeye koyma.
"""
import json, re, sys, unicodedata


def oku(yol):
    if yol.lower().endswith(".pdf"):
        from pypdf import PdfReader
        return "\n".join((p.extract_text() or "") for p in PdfReader(yol).pages)
    t = open(yol, encoding="utf-8", errors="replace").read()
    return re.sub(r"<[^>]+>", " ", t) if yol.lower().endswith((".html", ".htm")) else t


def norm(s):
    s = unicodedata.normalize("NFC", s).lower()
    return re.sub(r"\s+", " ", s)


metin = norm(oku(sys.argv[1]))
bulunan = 0
for c in json.load(open(sys.argv[2], encoding="utf-8")):
    n = norm(str(c))
    for m in re.finditer(re.escape(n), metin):
        bulunan += 1
        print(f"SIZINTI '{c}': …{metin[max(0, m.start() - 40): m.end() + 40]}…")
print(f"Sonuç: {bulunan} olası sızıntı")
sys.exit(1 if bulunan else 0)
