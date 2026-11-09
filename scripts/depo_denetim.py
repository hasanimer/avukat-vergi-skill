#!/usr/bin/env python3
"""Depo tutarlılık denetimi (yalnız standart kütüphane). CI her push'ta çalıştırır.

Kullanım:
  python3 scripts/depo_denetim.py            # denetle; hata varsa çıkış kodu 1
  python3 scripts/depo_denetim.py --duzelt   # README'deki örnek çıktıları betiklerin gerçek çıktısıyla yenile

Denetlenenler:
  1. SKILL.md ön bilgisi (name, description <= 1024 karakter).
  2. Markdown dosyalarında geçen dosya yolları (`references/...`, `scripts/...`, `kdv.md` gibi) var mı.
  3. Bölüm atıfları: `dosya.md` §N için N numaralı başlık, `§14 #k` için o bölümdeki tablo satırı var mı.
  4. Özelgeler: atıf yapılan `ozelgeler/<ID>.txt` var mı; dizin.json, .txt sayısı, DIZIN.md ve
     SKILL.md / README'de yazan sayı aynı mı.
  5. Betiklerdeki tutarlar (PARAMS, TARIFELER) referans dosyalarında geçiyor mu.
  6. README'deki `$ python3 scripts/...` örnek çıktıları betiklerin gerçek çıktısıyla uyuşuyor mu.
  7. "Son kontrol" tarihi 120 günden eskiyse uyarı (hata değil).
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import shlex
import subprocess
import sys

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.join(KOK, "scripts"))
from aaut_hesap import TARIFELER  # noqa: E402
from smm_hesap import KDV_TEVKIFAT_SINIRI_ONCEKI, PARAMS  # noqa: E402

hatalar: list[str] = []
uyarilar: list[str] = []


def oku(yol: str) -> str:
    with open(os.path.join(KOK, yol), encoding="utf-8") as f:
        return f.read()


def md_dosyalari() -> list[str]:
    ref = sorted(os.path.relpath(p, KOK) for p in glob.glob(os.path.join(KOK, "references", "*.md")))
    return ["SKILL.md", "README.md"] + [p for p in ref if ".local." not in p]


def sayi(x) -> str:
    """1234567 -> '1.234.567'"""
    return f"{int(x):,}".replace(",", ".")


# --- 1 ---------------------------------------------------------------------
def on_bilgi() -> None:
    t = oku("SKILL.md")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if not m:
        hatalar.append("SKILL.md: ön bilgi (--- ... ---) yok")
        return
    fm = m.group(1)
    if not re.search(r"^name:\s*avukat-vergi\s*$", fm, re.M):
        hatalar.append("SKILL.md: name alanı 'avukat-vergi' değil")
    d = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not d:
        hatalar.append("SKILL.md: description alanı yok")
    elif len(d.group(1)) > 1024:
        hatalar.append(f"SKILL.md: description {len(d.group(1))} karakter (sınır 1024)")


# --- 2 ---------------------------------------------------------------------
YOL_RE = re.compile(r"`((?:references/|scripts/|examples/|kaynak/|ozelgeler/)?[A-Za-z0-9_./-]+\.(?:md|py|txt|json|yml))`")
BAGLANTI_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")


def yol_var(dosya: str, hedef: str) -> bool:
    adaylar = [hedef, os.path.join(os.path.dirname(dosya), hedef), os.path.join("references", hedef),
               os.path.join("references", "ozelgeler", hedef), os.path.join("scripts", hedef)]
    return any(os.path.exists(os.path.join(KOK, a)) for a in adaylar)


def yollar() -> None:
    for dosya in md_dosyalari():
        t = oku(dosya)
        hedefler = set(YOL_RE.findall(t)) | {h.split("#")[0] for h in BAGLANTI_RE.findall(t)}
        for h in sorted(hedefler):
            if not h or ".local." in h or "<" in h or "*" in h or h.startswith("/tmp/"):
                continue
            if not yol_var(dosya, h):
                hatalar.append(f"{dosya}: var olmayan dosyaya atıf: {h}")


# --- 3 ---------------------------------------------------------------------
BOLUM_RE = re.compile(r"`?((?:references/)?[a-z0-9-]+\.md)`?,? §(\d+)((?:,? ?#\d+[a-z]?)*)")


def bolumler(dosya: str) -> dict[str, str]:
    """{'14': bölüm metni} — '## 14. Başlık' biçimindeki numaralı başlıklar."""
    t = oku(dosya)
    parcalar = re.split(r"^#{2,3} (\d+)\. .*$", t, flags=re.M)
    return {parcalar[i]: parcalar[i + 1] for i in range(1, len(parcalar) - 1, 2)}


def bolum_atiflari() -> None:
    onbellek: dict[str, dict[str, str]] = {}
    for dosya in md_dosyalari():
        for hedef, no, satirlar in BOLUM_RE.findall(oku(dosya)):
            yol = hedef if hedef.startswith("references/") else os.path.join("references", hedef)
            if not os.path.exists(os.path.join(KOK, yol)):
                continue    # 2. denetim bildirir
            b = onbellek.setdefault(yol, bolumler(yol))
            if no not in b:
                hatalar.append(f"{dosya}: {hedef} §{no} yok (numaralı başlıklar: {', '.join(b) or 'yok'})")
                continue
            for k in re.findall(r"#(\d+[a-z]?)", satirlar):
                if not re.search(rf"^\| {re.escape(k)} \|", b[no], re.M):
                    hatalar.append(f"{dosya}: {hedef} §{no} #{k} yok (o bölümün tablosunda '| {k} |' satırı bulunamadı)")
        # bölüm numarası gibi görünen ama eski biçimde yazılmış atıflar
        for m in re.finditer(r"§\d+(?:/|, )\d{1,2}[a-z]?\b(?!\d)", oku(dosya)):
            hatalar.append(f"{dosya}: belirsiz bölüm atfı '{m.group(0)}' — tablo satırı için '§N #k' yazın")


# --- 4 ---------------------------------------------------------------------
def ozelgeler() -> None:
    dizin = json.loads(oku("references/ozelgeler/dizin.json"))
    idler = {str(x["id"]) for x in dizin}
    txt = {os.path.basename(p)[:-4] for p in glob.glob(os.path.join(KOK, "references", "ozelgeler", "*.txt"))}
    if len(idler) != len(dizin):
        hatalar.append("dizin.json: yinelenen özelge ID'si var")
    for i in sorted(idler - txt):
        hatalar.append(f"dizin.json: {i} dizinde var, {i}.txt yok")
    for i in sorted(txt - idler):
        hatalar.append(f"ozelgeler/{i}.txt var, dizin.json'da kaydı yok")
    n = len(dizin)
    md = oku("references/ozelgeler/DIZIN.md")
    toplam = 0
    for m in re.finditer(r"^## (\S+) \((\d+)\)\n(.*?)(?=^## |\Z)", md, re.M | re.S):
        satir = len(re.findall(r"^\| \d{4}-\d{2}-\d{2} \|", m.group(3), re.M))
        toplam += satir
        if satir != int(m.group(2)):
            hatalar.append(f"DIZIN.md: '{m.group(1)}' başlığında {m.group(2)} yazıyor, tabloda {satir} satır var")
    toplam += len(re.findall(r"^\| \d{4}-\d{2}-\d{2} \|", md.split("## sınıflandırılmadı")[1], re.M)) if "## sınıflandırılmadı" in md else 0
    if toplam != n:
        hatalar.append(f"DIZIN.md: tablolarda {toplam} özelge var, dizin.json'da {n}")
    for dosya, kalip in (("SKILL.md", r"(\d+) özelge,"), ("README.md", r"(\d+)'\w+ tam metniyle"),
                         ("README.md", r"(\d+) GİB özelgesinin tam metni")):
        m = re.search(kalip, oku(dosya))
        if not m:
            hatalar.append(f"{dosya}: özelge sayısı ifadesi bulunamadı ({kalip})")
        elif int(m.group(1)) != n:
            hatalar.append(f"{dosya}: özelge sayısı {m.group(1)} yazıyor, arşivde {n} var")
    for dosya in md_dosyalari():
        for i in set(re.findall(r"ozelgeler/(\d+)\.txt", oku(dosya))):
            if i not in txt:
                hatalar.append(f"{dosya}: ozelgeler/{i}.txt yok")


# --- 5 ---------------------------------------------------------------------
def tutarlar() -> None:
    p_md = oku("references/parametreler.md")
    for yil, p in PARAMS.items():
        aranan = {f"{yil} tarife dilimi": [u for u, _ in p["tarife"] if u] + [u for u, _ in p["tarife_ucret"] if u]}
        for k in ("telif_istisna_siniri", "arizi_smk_istisna", "genc_girisimci_istisna", "mesken_istisnasi",
                  "nakden_iade_siniri", "ymm_iade_siniri", "kdv_tevkifat_siniri", "uyum_indirimi_azami"):
            if p.get(k) is not None:
                aranan[f"{yil} {k}"] = [p[k]]
        for ad, degerler in aranan.items():
            for d in degerler:
                if sayi(d) not in p_md:
                    hatalar.append(f"smm_hesap.py PARAMS[{ad}] = {sayi(d)} parametreler.md'de geçmiyor")
    for yil, d in KDV_TEVKIFAT_SINIRI_ONCEKI.items():
        if sayi(d) not in p_md:
            hatalar.append(f"smm_hesap.py KDV_TEVKIFAT_SINIRI_ONCEKI[{yil}] = {sayi(d)} parametreler.md'de geçmiyor")

    a_md = oku("references/aaut.md")
    anahtarlar = sorted(TARIFELER)          # eski → yeni; aaut.md sütunları yeni → eski
    for tarih, t in TARIFELER.items():
        gun = f"{tarih[8:10]}/{tarih[5:7]}/{tarih[:4]}"
        if gun not in a_md or f"`{tarih}`" not in a_md:
            hatalar.append(f"aaut.md: {tarih} tarifesinin tarihi ({gun}) veya betik anahtarı geçmiyor")
        for k in ("icra_maktu_esik", "arabuluculuk_maktu_esik", "arabuluculuk_anlasmazlik"):
            if sayi(t[k]) not in a_md:
                hatalar.append(f"aaut_hesap.py TARIFELER[{tarih}][{k}] = {sayi(t[k])} aaut.md'de geçmiyor")
        for g, _ in t["nispi"]:
            if g and sayi(g) not in a_md:
                hatalar.append(f"aaut_hesap.py TARIFELER[{tarih}] nispi dilim {sayi(g)} aaut.md'de geçmiyor")
    for anahtar in TARIFELER[anahtarlar[-1]]["maktu"]:
        beklenen = " | ".join(sayi(TARIFELER[k]["maktu"][anahtar][1]) for k in reversed(anahtarlar))
        if not re.search(rf"\| {re.escape(anahtar)} \| {re.escape(beklenen)} \|", a_md):
            hatalar.append(f"aaut.md: maktu tablosunda '{anahtar}' satırı betikle uyuşmuyor (beklenen: {beklenen})")


# --- 6 ---------------------------------------------------------------------
BLOK_RE = re.compile(r"```console\n\$ (python3 scripts/[^\n]+)\n(.*?)```", re.S)


def calistir(komut: str) -> str:
    r = subprocess.run(["python3", "-B"] + shlex.split(komut)[1:], cwd=KOK, capture_output=True, text=True, timeout=120)
    return (r.stdout + r.stderr).rstrip("\n")


def readme(duzelt: bool) -> None:
    t = oku("README.md")

    def yenile(m):
        return f"```console\n$ {m.group(1)}\n{calistir(m.group(1))}\n```"

    if duzelt:
        yeni = BLOK_RE.sub(yenile, t)
        if yeni != t:
            with open(os.path.join(KOK, "README.md"), "w", encoding="utf-8") as f:
                f.write(yeni)
            print("README.md örnek çıktıları yenilendi.")
        return
    for komut, govde in BLOK_RE.findall(t):
        gercek = [s.rstrip() for s in calistir(komut).split("\n")]
        konum = 0
        for satir in (s.rstrip() for s in govde.split("\n")):
            if not satir:
                continue
            try:
                konum = gercek.index(satir, konum) + 1
            except ValueError:
                hatalar.append(f"README.md: '$ {komut}' örneğindeki satır betiğin çıktısında yok: {satir[:90]}"
                               " (yenilemek için: python3 scripts/depo_denetim.py --duzelt)")
                break


# --- 7 ---------------------------------------------------------------------
def guncellik(bugun: datetime.date, esik: int = 120) -> None:
    for dosya in md_dosyalari():
        m = re.search(r"Son kontrol\W{0,6}(\d{2})[./](\d{2})[./](\d{4})", oku(dosya))
        if m:
            tarih = datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
            gun = (bugun - tarih).days
            if gun > esik:
                uyarilar.append(f"{dosya}: son kontrol {tarih:%d.%m.%Y} ({gun} gün önce)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--duzelt", action="store_true", help="README örnek çıktılarını gerçek çıktıyla yenile")
    a = ap.parse_args()
    if a.duzelt:
        readme(True)
    for denetim in (on_bilgi, yollar, bolum_atiflari, ozelgeler, tutarlar):
        denetim()
    readme(False)
    guncellik(datetime.date.today())
    for u in uyarilar:
        print(f"UYARI {u}")
    for h in hatalar:
        print(f"HATA  {h}")
    print(f"\n{len(hatalar)} hata, {len(uyarilar)} uyarı." if hatalar or uyarilar else "Depo denetimi temiz.")
    return 1 if hatalar else 0


if __name__ == "__main__":
    sys.exit(main())
