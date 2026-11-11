#!/usr/bin/env python3
"""Kaynak depodan dağıtılabilir skill'ler üretir.

Her skill için dist/skills/<ad>/ klasörü kurulur:
  - skill klasörü olduğu gibi kopyalanır;
  - skill'in andığı references/ortak/... dosyaları ortak/ altından (ve onların andığı göreli dosyalar) kopyalanır;
  - references/veri/ anılıyorsa veri/ klasörü references/veri/ olarak kopyalanır;
  - scripts/<betik> anılıp skill'de yoksa ortak/betikler/ altından kopyalanır.
Sonra dist/zip/<ad>.zip (claude.ai'ye yüklenecek biçim) ve paketler/*.yaml için
dist/eklentiler/<paket>/ (Claude Code eklentisi) ile .claude-plugin/marketplace.json üretilir.

Kullanım: python3 araclar/paketle.py
"""
import os, re, sys, json, glob, shutil, zipfile
import yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import KOK, skill_klasorleri, on_bilgi, atiflar, goreli_md_atiflari

DIST = os.path.join(KOK, "dist")
shutil.rmtree(DIST, ignore_errors=True)
os.makedirs(os.path.join(DIST, "skills")); os.makedirs(os.path.join(DIST, "zip"))


def ortak_kopyala(goreli, hedef_kok, gorulen):
    """ortak/<goreli> dosyasını hedef_kok/references/ortak/<goreli> olarak kopyalar; içindeki göreli atıfları izler."""
    if goreli in gorulen:
        return
    gorulen.add(goreli)
    kaynak = os.path.join(KOK, "ortak", goreli)
    if not os.path.exists(kaynak):
        raise SystemExit(f"ortak dosya yok: {goreli}")
    hedef = os.path.join(hedef_kok, "references", "ortak", goreli)
    os.makedirs(os.path.dirname(hedef), exist_ok=True)
    shutil.copy2(kaynak, hedef)
    metin = open(kaynak, encoding="utf-8").read()
    for r in goreli_md_atiflari(metin):
        alt = os.path.normpath(os.path.join(os.path.dirname(goreli), r))
        if os.path.exists(os.path.join(KOK, "ortak", alt)):
            ortak_kopyala(alt, hedef_kok, gorulen)
    for r in atiflar(metin)[0]:
        if r.startswith("references/ortak/"):
            ortak_kopyala(r[len("references/ortak/"):], hedef_kok, gorulen)
    for b in atiflar(metin)[1]:
        betik_kopyala(b, hedef_kok)


def betik_kopyala(b, hedef_kok):
    hedef = os.path.join(hedef_kok, b)
    if os.path.exists(hedef):
        return
    kaynak = os.path.join(KOK, "ortak", "betikler", os.path.basename(b))
    if os.path.exists(kaynak):
        os.makedirs(os.path.dirname(hedef), exist_ok=True)
        shutil.copy2(kaynak, hedef)


ozet = []
for k in skill_klasorleri():
    ad = os.path.basename(k)
    hedef = os.path.join(DIST, "skills", ad)
    shutil.copytree(k, hedef)
    metin = "".join(open(p, encoding="utf-8").read() for p in glob.glob(os.path.join(hedef, "**", "*.md"), recursive=True))
    refs, betikler = atiflar(metin)
    gorulen = set()
    for r in sorted(refs):
        if r.startswith("references/ortak/"):
            ortak_kopyala(r[len("references/ortak/"):], hedef, gorulen)
    if any(r.startswith("references/veri") for r in refs):
        shutil.copytree(os.path.join(KOK, "veri"), os.path.join(hedef, "references", "veri"), dirs_exist_ok=True)
    for b in betikler:
        betik_kopyala(b, hedef)
    z = os.path.join(DIST, "zip", f"{ad}.zip")
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(glob.glob(os.path.join(hedef, "**", "*"), recursive=True)):
            if os.path.isfile(p) and "__pycache__" not in p:
                zf.write(p, os.path.relpath(p, os.path.join(DIST, "skills")))
    dosya = sum(len(f) for _, _, f in os.walk(hedef))
    ozet.append((ad, dosya, len(gorulen)))

# Eklentiler (Claude Code) ve pazar yeri
pazar = {"name": "maarif-skill-kutuphanesi", "owner": {"name": "DNAMATHOS"},
         "metadata": {"description": "Türkiye Yüzyılı Maarif Modeli'ne dayalı öğretmen skill'leri."}, "plugins": []}
for p in sorted(glob.glob(os.path.join(KOK, "paketler", "*.yaml"))):
    pk = yaml.safe_load(open(p, encoding="utf-8"))
    ek = os.path.join(DIST, "eklentiler", pk["ad"])
    os.makedirs(os.path.join(ek, ".claude-plugin"))
    for s in pk["skills"]:
        shutil.copytree(os.path.join(DIST, "skills", s), os.path.join(ek, "skills", s))
    json.dump({"name": pk["ad"], "version": pk["surum"], "description": pk["aciklama"], "author": {"name": "DNAMATHOS"}},
              open(os.path.join(ek, ".claude-plugin", "plugin.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    pazar["plugins"].append({"name": pk["ad"], "displayName": pk["gorunen_ad"], "description": pk["aciklama"],
                             "version": pk["surum"], "category": "education", "source": f"./dist/eklentiler/{pk['ad']}"})
os.makedirs(os.path.join(KOK, ".claude-plugin"), exist_ok=True)
json.dump(pazar, open(os.path.join(KOK, ".claude-plugin", "marketplace.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

for ad, n, o in ozet:
    print(f"{ad:32} {n:3} dosya · {o:2} ortak başvuru")
print(f"{len(ozet)} skill paketlendi → dist/skills, dist/zip, dist/eklentiler")
