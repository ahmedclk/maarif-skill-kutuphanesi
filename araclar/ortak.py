"""Araçların ortak yardımcıları."""
import os, re, glob
import yaml

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IZINLI = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def skill_klasorleri(kok=KOK):
    """Kaynak depodaki bütün skill klasörleri: skills/* ve markalar/*/*."""
    yollar = sorted(glob.glob(os.path.join(kok, "skills", "*", "SKILL.md")) +
                    glob.glob(os.path.join(kok, "markalar", "*", "*", "SKILL.md")))
    return [os.path.dirname(y) for y in yollar]


def on_bilgi(skill_md):
    t = open(skill_md, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    if not m:
        return None, t
    return yaml.safe_load(m.group(1)), m.group(2)


def atiflar(metin):
    """Metindeki references/... ve scripts/... yollarını döndürür."""
    refs = set(re.findall(r"references/[\w./<>-]+?\.(?:md|yaml|json|csv)", metin))
    refs |= {r.rstrip("/") + "/" for r in re.findall(r"references/veri(?=[/\s`)])", metin)}
    betik = set(re.findall(r"scripts/[\w.-]+\.(?:py|js|sh)", metin))
    return {r for r in refs if "<" not in r}, betik


def goreli_md_atiflari(metin):
    """Bir ortak dosyanın içinde `x.md`, `../y/z.md` biçimindeki göreli atıflar."""
    return set(re.findall(r"`((?:\.\./)*[\w-]+(?:/[\w-]+)*\.md)`", metin))
