#!/usr/bin/env python3
"""KATALOG.md ve katalog.json üretir (skill adı, açıklama, paketler, dersler, lisans, sözcük sayısı)."""
import os, sys, json, glob
import yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ortak import KOK, skill_klasorleri, on_bilgi

paket = {}
for p in sorted(glob.glob(os.path.join(KOK, "paketler", "*.yaml"))):
    pk = yaml.safe_load(open(p, encoding="utf-8"))
    for s in pk["skills"]:
        paket.setdefault(s, []).append(pk["ad"])
kayit = []
for k in skill_klasorleri():
    fm, govde = on_bilgi(os.path.join(k, "SKILL.md"))
    md = fm.get("metadata", {})
    kayit.append({"ad": fm["name"], "yol": os.path.relpath(k, KOK), "aciklama": fm["description"],
                  "surum": md.get("surum"), "dersler": md.get("dersler", ""), "onceki_ad": md.get("onceki_ad", ""),
                  "lisans": "Apache-2.0 (uyarlama)" if "Apache" in str(fm.get("license")) else "karar bekliyor",
                  "paketler": paket.get(fm["name"], []), "sozcuk": len(govde.split())})
json.dump(kayit, open(os.path.join(KOK, "katalog.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
s = ["# Katalog", "", "Bu dosya `araclar/katalog.py` ile üretilir; elle düzenlenmez.", "",
     "| Skill | Ne yapar (kısaca) | Paketler | Lisans | Sözcük |", "| --- | --- | --- | --- | --- |"]
for r in kayit:
    kisa = r["aciklama"].split(";")[0].split(". ")[0]
    s.append(f"| `{r['ad']}` | {kisa} | {', '.join(r['paketler'])} | {r['lisans']} | {r['sozcuk']} |")
s += ["", "## Tam açıklamalar", ""]
for r in kayit:
    s += [f"### {r['ad']}", "", r["aciklama"], "", f"Yol: `{r['yol']}` · Sürüm: {r['surum']}" + (f" · Önceki ad: {r['onceki_ad']}" if r["onceki_ad"] else ""), ""]
open(os.path.join(KOK, "KATALOG.md"), "w", encoding="utf-8").write("\n".join(s))
print(f"{len(kayit)} skill kataloglandı.")
