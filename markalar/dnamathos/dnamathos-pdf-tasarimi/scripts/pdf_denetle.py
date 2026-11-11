#!/usr/bin/env python3
"""Üretilmiş PDF'i denetler: sayfa sayısı, iç bağlantı hedefleri, dosyalar arası bağlantılar, üst veri.

Kullanım: python3 pdf_denetle.py dosya.pdf [--sayfa N] [--sira cikti_sira.json] [--baslik "..."]
--sira: slayt_uret.py'nin yazdığı slayt kimliği listesi; her kimliğin doğru sayfada olduğu ve her slayta
en az bir bağlantıyla ulaşıldığı (kapak hariç) denetlenir.
Çıkış kodu: hatalı bağlantı ya da sayfa sayısı uyuşmazlığı varsa 1.
"""
import argparse, os, sys
from pypdf import PdfReader, PdfWriter

ap = argparse.ArgumentParser()
ap.add_argument("pdf"); ap.add_argument("--sayfa", type=int); ap.add_argument("--baslik"); ap.add_argument("--sira")
a = ap.parse_args()
r = PdfReader(a.pdf)
n = len(r.pages)
adlar = set((r.named_destinations or {}).keys())
toplam = hatali = 0
sayfa_no = {str(k).lstrip("/"): r.get_destination_page_number(v) for k, v in (r.named_destinations or {}).items()}
ulasilan = set()
for i, pg in enumerate(r.pages, 1):
    for an in pg.get("/Annots") or []:
        o = an.get_object()
        if o.get("/Subtype") != "/Link":
            continue
        toplam += 1
        act = o.get("/A")
        act = act.get_object() if act else None
        dest = o.get("/Dest")
        if act is not None and act.get("/S") == "/GoToR":
            f = act.get("/F")
            f = f.get_object() if hasattr(f, "get_object") else f
            f = f.get("/F") if isinstance(f, dict) else f
            if not os.path.exists(os.path.join(os.path.dirname(a.pdf), str(f))):
                hatali += 1; print(f"s.{i}: dosyalar arası hedef yok → {f}")
        elif act is not None and act.get("/S") == "/URI":
            uri = str(act.get("/URI"))
            if "invalid" in uri:
                hatali += 1; print(f"s.{i}: dönüştürülmemiş bağlantı → {uri}")
        else:
            d = dest if dest is not None else (act.get("/D") if act is not None else None)
            if d is None:
                hatali += 1; print(f"s.{i}: hedefsiz bağlantı")
            elif isinstance(d, str) or hasattr(d, "startswith"):
                if str(d) not in adlar:
                    hatali += 1; print(f"s.{i}: adlandırılmış hedef yok → {d}")
                else:
                    ulasilan.add(sayfa_no.get(str(d).lstrip("/")))
print(f"Sayfa: {n} · bağlantı: {toplam} · hatalı: {hatali}")
ok = hatali == 0
if a.sira:
    import json
    sira = json.load(open(a.sira))
    yanlis = [k for k in sira if sayfa_no.get(k) != sira.index(k)]
    ulasilamayan = [sira[i] for i in range(1, len(sira)) if i not in ulasilan]
    print(f"Yanlış sayfadaki hedef: {yanlis or 'yok'} · ulaşılamayan slayt: {ulasilamayan or 'yok'}")
    ok = ok and not yanlis and not ulasilamayan
if a.sayfa and a.sayfa != n:
    ok = False; print(f"Sayfa sayısı {n}, beklenen {a.sayfa}")
if a.baslik:
    w = PdfWriter(clone_from=r); w.add_metadata({"/Title": a.baslik, "/Author": "DNAMATHOS"}); w.write(a.pdf)
    print("Üst veri yazıldı.")
sys.exit(0 if ok else 1)
