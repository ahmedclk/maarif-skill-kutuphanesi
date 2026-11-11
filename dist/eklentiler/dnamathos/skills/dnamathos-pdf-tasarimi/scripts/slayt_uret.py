#!/usr/bin/env python3
"""DNAMATHOS 16:9 slayt PDF'i üretir.

Kullanım:
  python3 slayt_uret.py govde.html cikti.pdf [--katex node_modules/katex/dist] [--css assets/dnamathos-slayt.css]
            [--goruntu klasor] [--baslik "Başlık"]

govde.html: yalnız <section class="s ..." id="..."> öğelerinden oluşan gövde (scripts/dna.py ile kurulur). Betik bunu CSS ve KaTeX ile
sarar, taşma denetimini (assets/tasma-denetimi.js) çalıştırır, 297 × 167 mm PDF ve isteğe bağlı her slaytın
PNG görüntüsünü üretir. Taşma bulunursa listeler ve 1 ile çıkar (PDF yine yazılır).
"""
import argparse, json, os, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def font_css():
    """assets/fontlar içindeki woff2 dosyalarından @font-face kuralları. 'Govde' ailesi: harfler Atkinson
    Hyperlegible Next, rakamlar Inter (Atkinson'ın çizgili sıfırı saat ve ondalıkta yadırganır)."""
    fd = os.path.join(KOK, "assets", "fontlar")
    url = lambda f: "url('file://" + os.path.join(fd, f) + "') format('woff2')"
    k = []
    def yuz(aile, dosya_aile, agirlik, stil="normal", aralik=None):
        for alt in ("latin", "latin-ext"):
            f = f"{dosya_aile}-{alt}-{agirlik}-{stil}.woff2"
            if os.path.exists(os.path.join(fd, f)):
                k.append(f"@font-face{{font-family:'{aile}';font-weight:{agirlik};font-style:{stil};src:{url(f)}" + (f";unicode-range:{aralik}" if aralik else "") + "}")
    for w, st in (("600", "normal"), ("800", "normal"), ("600", "italic"), ("800", "italic")):
        yuz("Fraunces", "fraunces", w, st)
    for w, st in (("400", "normal"), ("700", "normal"), ("400", "italic")):
        yuz("Govde", "atkinson-hyperlegible-next", w, st)
        yuz("Atkinson Hyperlegible Next", "atkinson-hyperlegible-next", w, st)
    for w in ("400", "700"):
        k.append(f"@font-face{{font-family:'Govde';font-weight:{w};src:{url(f'inter-latin-{w}-normal.woff2')};unicode-range:U+0030-0039}}")
    for w in ("600", "700"):
        yuz("Caveat", "caveat", w)
    for w in ("500", "600"):
        yuz("IBM Plex Mono", "ibm-plex-mono", w)
    return "".join(k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("govde"); ap.add_argument("pdf")
    ap.add_argument("--katex", default="node_modules/katex/dist")
    ap.add_argument("--css", default=os.path.join(KOK, "assets", "dnamathos.css"))
    ap.add_argument("--goruntu"); ap.add_argument("--baslik", default="DNAMATHOS")
    a = ap.parse_args()
    kat = os.path.abspath(a.katex)
    if not os.path.exists(os.path.join(kat, "katex.min.js")):
        sys.exit(f"KaTeX bulunamadı: {kat} (npm install katex)")
    css = open(a.css, encoding="utf-8").read().replace("/*{{FONTLAR}}*/", font_css())
    js = "\n".join(l for l in open(os.path.join(KOK, "assets", "tasma-denetimi.js"), encoding="utf-8").read().splitlines() if not l.startswith("//"))
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
        for el in pg.query_selector_all(".s, .slide"):
            ids.append(el.get_attribute("id"))
            if a.goruntu:
                os.makedirs(a.goruntu, exist_ok=True)
                el.screenshot(path=os.path.join(a.goruntu, f"{len(ids):03d}_{ids[-1]}.png"))
        br.close()
    json.dump(ids, open(os.path.splitext(a.pdf)[0] + "_sira.json", "w"))
    sorun = res.get("problems", []) if isinstance(res, dict) else res
    print(f"{len(ids)} slayt · sorun: {len(sorun)} · en küçük gövde yazısı: {res.get('enkucuk') if isinstance(res, dict) else '?'} px")
    for s in sorun:
        print("SORUN ", s)
    sys.exit(1 if sorun else 0)


if __name__ == "__main__":
    main()
