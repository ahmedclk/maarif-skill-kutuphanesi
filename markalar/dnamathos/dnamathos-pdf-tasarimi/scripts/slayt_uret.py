#!/usr/bin/env python3
"""DNAMATHOS 16:9 slayt PDF'i üretir.

Kullanım:
  python3 slayt_uret.py govde.html cikti.pdf [--katex node_modules/katex/dist] [--css assets/dnamathos-slayt.css]
            [--goruntu klasor] [--baslik "Başlık"]

govde.html: yalnız <section class="slide" id="..."> öğelerinden oluşan gövde. Betik bunu CSS ve KaTeX ile
sarar, taşma denetimini (assets/tasma-denetimi.js) çalıştırır, 297 × 167 mm PDF ve isteğe bağlı her slaytın
PNG görüntüsünü üretir. Taşma bulunursa listeler ve 1 ile çıkar (PDF yine yazılır).
"""
import argparse, json, os, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("govde"); ap.add_argument("pdf")
    ap.add_argument("--katex", default="node_modules/katex/dist")
    ap.add_argument("--css", default=os.path.join(KOK, "assets", "dnamathos-slayt.css"))
    ap.add_argument("--goruntu"); ap.add_argument("--baslik", default="DNAMATHOS")
    a = ap.parse_args()
    kat = os.path.abspath(a.katex)
    if not os.path.exists(os.path.join(kat, "katex.min.js")):
        sys.exit(f"KaTeX bulunamadı: {kat} (npm install katex)")
    css = open(a.css, encoding="utf-8").read()
    js = open(os.path.join(KOK, "assets", "tasma-denetimi.js"), encoding="utf-8").read().split("\n", 1)[1]
    govde = open(a.govde, encoding="utf-8").read()
    html = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{a.baslik}</title>'
            f'<link rel="stylesheet" href="file://{kat}/katex.min.css"><style>{css}</style>'
            f'<script src="file://{kat}/katex.min.js"></script><script src="file://{kat}/contrib/auto-render.min.js"></script>'
            f'</head><body>{govde}</body></html>')
    hp = os.path.splitext(os.path.abspath(a.pdf))[0] + ".html"
    open(hp, "w", encoding="utf-8").write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": 1123, "height": 632})
        pg.goto("file://" + hp); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
        res = pg.evaluate(js)
        pg.emulate_media(media="print")
        pg.pdf(path=a.pdf, width="297mm", height="167mm", print_background=True, prefer_css_page_size=True)
        ids = []
        for el in pg.query_selector_all(".slide"):
            ids.append(el.get_attribute("id"))
            if a.goruntu:
                os.makedirs(a.goruntu, exist_ok=True)
                el.screenshot(path=os.path.join(a.goruntu, f"{len(ids):03d}_{ids[-1]}.png"))
        br.close()
    json.dump(ids, open(os.path.splitext(a.pdf)[0] + "_sira.json", "w"))
    sorun = res.get("problems", []) if isinstance(res, dict) else res
    print(f"{len(ids)} slayt · taşma: {len(sorun)}")
    for s in sorun:
        print("TAŞMA ", s)
    sys.exit(1 if sorun else 0)


if __name__ == "__main__":
    main()
