#!/usr/bin/env python3
"""Kütüphane denetimi: Anthropic skill rehberi kuralları ve kütüphane kuralları.

Kullanım: python3 araclar/denetle.py [--dagitim]   (--dagitim: dist/skills altındaki paketlenmiş skill'leri denetler)
Çıkış kodu: hata varsa 1.
"""
import os, re, sys, glob, argparse
import yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import KOK, IZINLI, skill_klasorleri, on_bilgi, atiflar, goreli_md_atiflari

ap = argparse.ArgumentParser()
ap.add_argument("--dagitim", action="store_true")
a = ap.parse_args()

hata, uyari = [], []
H = lambda s, m: hata.append(f"{s}: {m}")
U = lambda s, m: uyari.append(f"{s}: {m}")

klasorler = (sorted(os.path.dirname(p) for p in glob.glob(os.path.join(KOK, "dist", "skills", "*", "SKILL.md")))
             if a.dagitim else skill_klasorleri())
adlar = {os.path.basename(k) for k in klasorler}
SUPHELI = re.compile(r"(ignore (all|previous)|önceki talimat|system prompt|sistem istemi|<\s*script|curl |http://)", re.I)

for k in klasorler:
    ad = os.path.basename(k)
    # 1. Klasör ve dosya adları
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", ad):
        H(ad, "klasör adı kebab-case ve ASCII değil")
    if "claude" in ad or "anthropic" in ad:
        H(ad, "adda 'claude' ya da 'anthropic' geçiyor")
    dosyalar = os.listdir(k)
    if "SKILL.md" not in dosyalar:
        H(ad, "SKILL.md yok (ad birebir SKILL.md olmalı)")
        continue
    for f in dosyalar:
        if f.lower() in ("readme.md", "readme"):
            H(ad, "skill klasöründe README bulunamaz")
        if f.lower() == "skill.md" and f != "SKILL.md":
            H(ad, f"dosya adı {f}; SKILL.md olmalı")
    # 2. Üst bilgi
    fm, govde = on_bilgi(os.path.join(k, "SKILL.md"))
    if fm is None:
        H(ad, "YAML üst bilgisi (--- ... ---) yok"); continue
    fazla = set(fm) - IZINLI
    if fazla:
        H(ad, f"izin verilmeyen üst bilgi alanı: {sorted(fazla)}")
    if fm.get("name") != ad:
        H(ad, f"name '{fm.get('name')}' klasör adıyla aynı değil")
    d = fm.get("description") or ""
    if not d:
        H(ad, "description boş")
    if len(d) > 1024:
        H(ad, f"description {len(d)} karakter (en çok 1024)")
    if "<" in d or ">" in d:
        H(ad, "description içinde < ya da > var")
    if "için değil" not in d and "için kullanma" not in d:
        U(ad, "description olumsuz tetikleyici (… için değil) içermiyor")
    if "Tetikleyiciler" not in d and "kullan" not in d:
        U(ad, "description ne zaman kullanılacağını söylemiyor")
    for anilan in re.findall(r"\((?:[a-z0-9-]+(?:, )?)+\)", d):
        for s in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)+", anilan):
            if s not in adlar and s not in ("docx", "pptx", "xlsx", "pdf"):
                H(ad, f"description kardeş skill '{s}' adını anıyor ama böyle bir skill yok")
    c = fm.get("compatibility")
    if c is not None and not (1 <= len(str(c)) <= 500):
        H(ad, "compatibility 1–500 karakter olmalı")
    if fm.get("metadata") is not None and not isinstance(fm["metadata"], dict):
        H(ad, "metadata bir eşleme olmalı")
    if SUPHELI.search(d) or SUPHELI.search(yaml.safe_dump(fm, allow_unicode=True)):
        H(ad, "üst bilgide şüpheli talimat ya da bağlantı (enjeksiyon denetimi)")
    # 3. Boyut
    sozcuk = len(govde.split())
    if sozcuk > 5000:
        H(ad, f"SKILL.md {sozcuk} sözcük (en çok 5000)")
    elif sozcuk > 3000:
        U(ad, f"SKILL.md {sozcuk} sözcük; ayrıntıyı references/ altına taşımayı düşün")
    # 4. Lisans
    lic = str(fm.get("license", ""))
    if "Apache" in lic and not {"LICENSE", "NOTICE"} <= set(dosyalar):
        H(ad, "Apache-2.0 uyarlaması ama LICENSE ya da NOTICE yok")
    # 5. Atıflar
    tum = govde
    for yol in glob.glob(os.path.join(k, "references", "**", "*.md"), recursive=True):
        tum += "\n" + open(yol, encoding="utf-8").read()
    refs, betikler = atiflar(tum)
    for r in sorted(refs):
        yerel = os.path.join(k, r)
        if os.path.exists(yerel.rstrip("/")):
            continue
        if not a.dagitim and r.startswith("references/ortak/") and os.path.exists(os.path.join(KOK, "ortak", r[len("references/ortak/"):])):
            continue
        if not a.dagitim and r.startswith("references/veri") and os.path.isdir(os.path.join(KOK, "veri")):
            continue
        H(ad, f"atıf bulunamadı: {r}")
    for b in sorted(betikler):
        if os.path.exists(os.path.join(k, b)):
            continue
        if not a.dagitim and os.path.exists(os.path.join(KOK, "ortak", "betikler", os.path.basename(b))):
            continue
        H(ad, f"betik bulunamadı: {b}")
    if "references/dersler/" in govde and not os.path.exists(os.path.join(k, "references", "dersler", "matematik.md")):
        H(ad, "ders dosyasına yönlendiriyor ama references/dersler/matematik.md yok")
    # 6. Testler (yalnız kaynak depoda)
    if not a.dagitim:
        tp = os.path.join(KOK, "testler", "tetikleme", f"{ad}.yaml")
        if not os.path.exists(tp):
            H(ad, "tetikleme testi yok (testler/tetikleme/<ad>.yaml)")
        else:
            t = yaml.safe_load(open(tp, encoding="utf-8"))
            if len(t.get("tetiklemeli", [])) < 10:
                H(ad, "tetikleme testinde 10'dan az 'tetiklemeli' istem")
            if len(t.get("tetiklememeli", [])) < 5:
                H(ad, "tetikleme testinde 5'ten az 'tetiklememeli' istem")
            for i in t.get("tetiklememeli", []):
                if i.get("dogru_skill") and i["dogru_skill"] not in adlar | {"yok"}:
                    H(ad, f"test '{i['dogru_skill']}' adında olmayan bir skill'e yönlendiriyor")
        if not os.path.exists(os.path.join(KOK, "istemler", f"{ad}.md")):
            U(ad, "hazır istem dosyası yok (istemler/<ad>.md)")

# 7. Ortak dosyalar arası göreli atıflar
if not a.dagitim:
    for yol in glob.glob(os.path.join(KOK, "ortak", "**", "*.md"), recursive=True):
        for r in goreli_md_atiflari(open(yol, encoding="utf-8").read()):
            hedef = os.path.normpath(os.path.join(os.path.dirname(yol), r))
            if not os.path.exists(hedef) and not r.startswith(("dersler/", "references/")):
                H(os.path.relpath(yol, KOK), f"göreli atıf bulunamadı: {r}")
    # 8. Veri ile çerçeve tutarlılığı
    kod = yaml.safe_load(open(os.path.join(KOK, "veri", "tymm", "kodlar.yaml"), encoding="utf-8"))["kodlar"]
    cerceve = open(os.path.join(KOK, "ortak", "maarif", "cerceve.md"), encoding="utf-8").read()
    for kd in kod:
        if not re.search(re.escape(kd) + r"\b", cerceve):
            H("veri/kodlar.yaml", f"{kd} çerçeve dosyasında geçmiyor")
    # 9. Kılavuz her skill'i kapsıyor
    kil = yaml.safe_load(open(os.path.join(KOK, "docs", "kilavuz.yaml"), encoding="utf-8"))
    for s in adlar - set(kil["skills"]):
        H("docs/kilavuz.yaml", f"{s} kılavuzda yok")
    for s, d in kil["skills"].items():
        if s not in adlar:
            H("docs/kilavuz.yaml", f"olmayan skill: {s}")
        for c in d.get("mevzuat", []):
            if c not in open(os.path.join(KOK, "ortak", "maarif", "meb-olcme-mevzuati.md"), encoding="utf-8").read():
                H("docs/kilavuz.yaml", f"{s}: {c} mevzuat dosyasında yok")
    # 10. Paketler
    for p in glob.glob(os.path.join(KOK, "paketler", "*.yaml")):
        pk = yaml.safe_load(open(p, encoding="utf-8"))
        for s in pk.get("skills", []):
            if s not in adlar:
                H(os.path.basename(p), f"pakette olmayan skill: {s}")

print(f"{len(klasorler)} skill denetlendi.")
for h in hata:
    print("HATA  ", h)
for u in uyari:
    print("UYARI ", u)
print(f"Sonuç: {len(hata)} hata, {len(uyari)} uyarı")
sys.exit(1 if hata else 0)
