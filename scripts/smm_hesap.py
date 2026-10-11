#!/usr/bin/env python3
"""Avukatlar için serbest meslek kazancı hesap aracı (yalnız standart kütüphane).

Alt komutlar:
  makbuz      e-SMM tutarları: brütten, netten, tahsil edilecekten veya KDV dahil
              vekalet ücretinden (iç yüzde) hesap; GV stopajı, KDV, KDV tevkifatı.
  vergi       Gelir vergisi tarifesi (GVK 103) ile hesaplanan vergi.
  gecici      Kümülatif geçici vergi (dönem bazında hasılat/gider/stopaj).
  yillik      Yıllık beyan simülasyonu (indirim sınırları, %5 uyum indirimi, mahsup).
  esmm-ozet   e-SMM XML arşivini (klasör veya .zip) okuyup ay/çeyrek özeti ve
              tutarlılık uyarıları üretir; --csv ile satır dökümü yazar.
  parametre   Yıla ait parametreleri gösterir.
  test        GİB Rehberi (Yayın No 590, Şubat 2026) örnekleriyle öz-sınama.

Tutarlar TL'dir. Parametreler PARAMS sözlüğündedir; her yıl başında ve tutar
kullanmadan önce references/parametreler.md ile karşılaştırın.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
import zipfile
from collections import defaultdict
from decimal import ROUND_HALF_UP, Decimal
from xml.etree import ElementTree as ET

D = Decimal
INF = D("1e18")


def r2(x) -> Decimal:
    return D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP)


def tl(x) -> str:
    """1234567.8 -> '1.234.567,80'"""
    q = r2(x)
    s = f"{abs(q):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("-" if q < 0 else "") + s


# ---------------------------------------------------------------------------
# Parametreler. "dogrulandi" alanı kaynağı söyler; None olan değerleri kullanmadan
# önce teyit edin. Kaynaklar references/parametreler.md'de.
# ---------------------------------------------------------------------------
PARAMS = {
    2025: {
        "tarife": [(158000, "0.15"), (330000, "0.20"), (800000, "0.27"), (4300000, "0.35"), (None, "0.40")],
        "tarife_ucret": [(158000, "0.15"), (330000, "0.20"), (1200000, "0.27"), (4300000, "0.35"), (None, "0.40")],
        "telif_istisna_siniri": 4300000,      # GVK 18 — tarifenin 4. dilim tutarı
        "arizi_smk_istisna": 280000,          # GVK 82
        "genc_girisimci_istisna": 330000,     # GVK mük. 20 — 2. dilim tutarı
        "uyum_indirimi_azami": 12000000,      # GVK mük. 121 — 1/1/2026dan itibaren verilen beyannameler (2025 kazancı) için
        "asgari_ucret_yillik_brut": "312066", # Rehber Örnek 2
        "engellilik_aylik": {1: 9900, 2: 5700, 3: 2400},  # 1. derece Rehber Örnek 4; 2-3. derece 2025 GVGT
        "mesken_istisnasi": 47000,            # Rehber Örnek 1
        "nakden_iade_siniri": 340000,
        "kdv_tevkifat_siniri": 9900,          # KDV dahil, işlem/dosya bazında; KDV GUT I/C-2.1.3.4.1 = VUK 232 sınırı (VUK GT 577)
        "dogrulandi": "GİB Rehberi Yayın 590 (2025 tarifesi ve tutarları)",
    },
    2026: {
        "tarife": [(190000, "0.15"), (400000, "0.20"), (1000000, "0.27"), (5300000, "0.35"), (None, "0.40")],
        "tarife_ucret": [(190000, "0.15"), (400000, "0.20"), (1500000, "0.27"), (5300000, "0.35"), (None, "0.40")],
        "telif_istisna_siniri": 5300000,
        "arizi_smk_istisna": 350000,
        "genc_girisimci_istisna": 400000,
        "uyum_indirimi_azami": 12000000,      # 2027'de verilecek beyanname için yeniden değerlenecek — teyit edin
        "asgari_ucret_yillik_brut": "396360", # 33.030 x 12 (AÜTK 2025/1, RG 26/12/2025-33119)
        "engellilik_aylik": {1: 12000, 2: 7000, 3: 3000},  # 332 Seri No.lu GVGT md.3/(2)-d
        "nakden_iade_siniri": 426000,
        "kdv_tevkifat_siniri": 12000,         # VUK GT 588 (RG 31/12/2025-33124 5.Mük.) VUK 232 sınırı
        "mesken_istisnasi": 58000,
        "dogrulandi": "332 Seri No.lu GVGT (RG 31/12/2025-33124 5.Mük.) tarife ve tutarlar; VUK GT 588 (VUK 232 = 12.000); Rehber 590",
    },
}

GV_STOPAJ_SMK = D("0.20")    # GVK 94/2-b (2009/14592 BKK)
GV_STOPAJ_TELIF = D("0.17")  # GVK 94/2-a — GVK 18 kapsamı
GECICI_VERGI_ORANI = D("0.15")
UYUM_INDIRIM_ORANI = D("0.05")


def params(yil: int) -> dict:
    if yil not in PARAMS:
        sys.exit(f"{yil} yılı için parametre yok. PARAMS sözlüğüne ekleyin (kaynak: GVGT / VUK GT).")
    return PARAMS[yil]


def need(p: dict, key: str, yil: int):
    v = p.get(key)
    if v is None:
        sys.exit(f"{yil} için '{key}' parametresi teyit edilmemiş. references/parametreler.md'ye bakın, "
                 f"değeri PARAMS'a girin veya komut satırından verin.")
    return v


# ---------------------------------------------------------------------------
# Gelir vergisi tarifesi
# ---------------------------------------------------------------------------
def gelir_vergisi(matrah, yil: int, ucret: bool = False) -> Decimal:
    p = params(yil)
    dilimler = p["tarife_ucret" if ucret else "tarife"]
    m = D(matrah)
    if m <= 0:
        return D(0)
    vergi, alt = D(0), D(0)
    for ust, oran in dilimler:
        ust_d = INF if ust is None else D(ust)
        if m > alt:
            vergi += (min(m, ust_d) - alt) * D(oran)
        alt = ust_d
        if m <= ust_d:
            break
    return r2(vergi)


def tarife_tablosu(yil: int, ucret: bool = False) -> list[str]:
    p = params(yil)
    dilimler = p["tarife_ucret" if ucret else "tarife"]
    satirlar, alt = [], D(0)
    for ust, oran in dilimler:
        if ust is None:
            satirlar.append(f"  {tl(alt)} TL'den fazlasının {tl(alt)} TL'si için {tl(gelir_vergisi(alt, yil, ucret))} TL, fazlası %{D(oran)*100:.0f}")
        else:
            sabit = gelir_vergisi(alt, yil, ucret)
            if alt == 0:
                satirlar.append(f"  {tl(ust)} TL'ye kadar %{D(oran)*100:.0f}")
            else:
                satirlar.append(f"  {tl(ust)} TL'nin {tl(alt)} TL'si için {tl(sabit)} TL, fazlası %{D(oran)*100:.0f}")
            alt = D(ust)
    return satirlar


# ---------------------------------------------------------------------------
# Makbuz (e-SMM) hesabı
# ---------------------------------------------------------------------------
def makbuz(brut=None, net=None, tahsil=None, kdv_dahil=None, stopaj_orani=GV_STOPAJ_SMK,
           kdv_orani=D("0.20"), kdv_tevkifat=D(0)) -> dict:
    """Tek kalem e-SMM hesabı.

    brut      : KDV hariç brüt ücret
    net       : stopaj sonrası net ücret (KDV hariç)
    tahsil    : müşteriden fiilen tahsil edilecek tutar (net + KDV - tevkif edilen KDV)
    kdv_dahil : KDV dahil kabul edilen tutar (ör. "KDV hariç" ibaresi olmayan mahkeme
                kararıyla hükmedilen vekalet ücreti — 311 Seri No.lu GVGT md.25/5): iç yüzde.
    """
    s, k, t = D(stopaj_orani), D(kdv_orani), D(kdv_tevkifat)
    if brut is not None:
        b = D(brut)
    elif net is not None:
        b = D(net) / (1 - s)
    elif tahsil is not None:
        b = D(tahsil) / (1 - s + k * (1 - t))
    elif kdv_dahil is not None:
        b = D(kdv_dahil) / (1 + k)
    else:
        raise ValueError("brut, net, tahsil veya kdv_dahil verin")
    b = r2(b)
    stopaj = r2(b * s)
    kdv = r2(b * k)
    tevkif_kdv = r2(kdv * t)
    return {
        "brut": b, "stopaj": stopaj, "net_ucret": b - stopaj, "kdv": kdv,
        "kdv_tevkifat": tevkif_kdv, "tahsil_edilen_kdv": kdv - tevkif_kdv,
        "tahsil_edilecek": b - stopaj + kdv - tevkif_kdv, "kdv_dahil_toplam": b + kdv,
    }


def oran_coz(s: str) -> Decimal:
    s = s.strip().replace(",", ".").replace("%", "")
    if "/" in s:
        a, b = s.split("/")
        return D(a) / D(b)
    v = D(s)
    return v / 100 if v > 1 else v


# ---------------------------------------------------------------------------
# Geçici vergi (kümülatif) — Rehber 9 ve 16.2.1
# ---------------------------------------------------------------------------
def gecici_vergi(donemler: list[dict]) -> list[dict]:
    """donemler: [{'hasilat':..,'gider':..,'stopaj':..}, ...] (dönem içi tutarlar, Q1..Q4)."""
    cum_h = cum_g = cum_s = D(0)
    odenen_top = D(0)
    out = []
    for i, d in enumerate(donemler, 1):
        cum_h += D(d.get("hasilat", 0))
        cum_g += D(d.get("gider", 0))
        cum_s += D(d.get("stopaj", 0))
        matrah = max(D(0), cum_h - cum_g)
        hesaplanan = r2(matrah * GECICI_VERGI_ORANI)
        odenecek = max(D(0), hesaplanan - cum_s - odenen_top)
        odenecek = r2(odenecek)
        odenen_top += odenecek
        out.append({"donem": i, "kumulatif_matrah": matrah, "hesaplanan": hesaplanan,
                    "kumulatif_stopaj": cum_s, "onceki_odenen": odenen_top - odenecek,
                    "odenecek": odenecek, "devreden_stopaj": max(D(0), cum_s - hesaplanan)})
    return out


# ---------------------------------------------------------------------------
# Yıllık beyan simülasyonu
# ---------------------------------------------------------------------------
def yillik(a: dict, yil: int) -> dict:
    p = params(yil)
    hasilat = D(a.get("hasilat", 0))
    gider = D(a.get("gider", 0))
    bagkur = D(a.get("bagkur", 0))
    smk = hasilat - gider - bagkur                       # beyan edilecek serbest meslek kazancı
    diger_gelir = D(a.get("diger_gelir", 0))             # ör. safi GMSİ, menkul sermaye iradı
    beyan_edilen = smk + diger_gelir                     # indirim sınırlarının bazı (Rehber 10.2)

    notlar, ind = [], {}
    base = max(D(0), beyan_edilen)
    if a.get("egitim_saglik"):
        sinir = r2(base * D("0.10"))
        ind["egitim_saglik"] = min(D(a["egitim_saglik"]), sinir)
        if D(a["egitim_saglik"]) > sinir:
            notlar.append(f"Eğitim/sağlık harcaması beyan edilen gelirin %10'u ({tl(sinir)}) ile sınırlandı (GVK 89/1-2).")
    if a.get("sigorta_primi"):
        aub = p.get("asgari_ucret_yillik_brut") or a.get("asgari_ucret_yillik_brut")
        if aub is None:
            sys.exit(f"{yil} asgari ücret yıllık brüt tutarı teyitsiz: --asgari-ucret-yillik ile verin.")
        sinir = min(r2(base * D("0.15")), D(aub))
        ind["sigorta_primi"] = min(D(a["sigorta_primi"]), sinir)
        if D(a["sigorta_primi"]) > sinir:
            notlar.append(f"Şahıs sigorta primi %15 ve yıllık brüt asgari ücret sınırıyla ({tl(sinir)}) sınırlandı (GVK 89/1-1).")
    if a.get("bagis_sinirli"):
        sinir = r2(base * D(str(a.get("bagis_orani", "0.05"))))
        ind["bagis_sinirli"] = min(D(a["bagis_sinirli"]), sinir)
    if a.get("bagis_tam"):
        ind["bagis_tam"] = D(a["bagis_tam"])
    if a.get("engellilik_derece"):
        aylik = (p.get("engellilik_aylik") or {}).get(int(a["engellilik_derece"])) or a.get("engellilik_aylik")
        if aylik is None:
            sys.exit(f"{yil} engellilik indirimi tutarı teyitsiz: --engellilik-aylik ile verin.")
        ind["engellilik"] = D(aylik) * int(a.get("engellilik_ay", 12))
    if a.get("diger_indirim"):
        ind["diger_indirim"] = D(a["diger_indirim"])
    zarar = D(a.get("gecmis_yil_zarari", 0))
    matrah = max(D(0), beyan_edilen - sum(ind.values(), D(0)) - zarar)
    hesaplanan = gelir_vergisi(matrah, yil)

    uyum = D(0)
    if a.get("uyum_indirimi"):
        payda = max(smk, D(0)) + max(diger_gelir, D(0))
        oran = (max(smk, D(0)) / payda) if payda > 0 else D(0)
        uyum = min(r2(hesaplanan * oran * UYUM_INDIRIM_ORANI), D(p["uyum_indirimi_azami"]))
        notlar.append(f"%5 indirim: hesaplanan vergi × mesleki kazanç payı ({oran:.4%}) × %5. "
                      "Rehber Örnek C oranı 4 haneye yuvarlar; sonuç birkaç TL farklı olabilir.")

    gecici = D(a.get("gecici_vergi", 0))
    tevkifat = D(a.get("tevkifat", 0))
    mahsup = gecici + tevkifat
    odenmesi_gereken = hesaplanan - mahsup
    sonuc = odenmesi_gereken - uyum
    devreden_indirim = D(0)
    if odenmesi_gereken <= 0:
        devreden_indirim = uyum
        sonuc = odenmesi_gereken
    elif sonuc < 0:
        devreden_indirim = -sonuc
        sonuc = D(0)
    if devreden_indirim > 0:
        notlar.append(f"Uyum indiriminin {tl(devreden_indirim)} TL'si ödenecek vergiden mahsup edilemedi; "
                      "beyan süresini izleyen 1 yıl içinde diğer beyana dayalı vergilerden mahsup edilebilir, iade edilmez.")
    iade = -sonuc if sonuc < 0 else D(0)
    if iade > 0:
        notlar.append("Mahsup edilemeyen tutar: geçici vergi kısmı yıl sonuna kadar talep halinde (beyannamede gösterilirse talep sayılır), "
                      f"tevkifat kısmı 1A dilekçesiyle iade/mahsup. Nakden iadede {yil} sınırı: {tl(p['nakden_iade_siniri'])} TL (aşan kısım inceleme/YMM).")
    return {
        "serbest_meslek_kazanci": smk, "diger_gelir": diger_gelir, "beyan_edilen_gelir": beyan_edilen,
        "indirimler": ind, "gecmis_yil_zarari": zarar, "matrah": matrah, "hesaplanan_vergi": hesaplanan,
        "uyum_indirimi": uyum, "mahsup_gecici": gecici, "mahsup_tevkifat": tevkifat,
        "odenecek": max(sonuc, D(0)), "iade_mahsup_alacagi": iade,
        "taksit": r2(max(sonuc, D(0)) / 2), "notlar": notlar,
    }


# ---------------------------------------------------------------------------
# e-SMM XML arşivi
# ---------------------------------------------------------------------------
NS = {"e": "http://earsiv.efatura.gov.tr"}
KOD = {"0015": "kdv", "0003": "stopaj", "9015": "kdv_tevkifat"}
KAMU_IPUCU = re.compile(r"BAŞSAVCILI|SAVCILI|MAHKEME|BAKANLI|BELEDİYE|VALİLİ|KAYMAKAM|MÜDÜRLÜĞÜ|BAŞKANLI|"
                        r"ÜNİVERSİTE|BAROSU|BARO BAŞKAN|HASTANE|SGK|SOSYAL GÜVENLİK|DÖNER SERMAYE|GENEL MÜDÜRLÜ|İL ÖZEL İDARE",
                        re.I)


def _t(el, path):
    x = el.find(path, NS)
    return x.text.strip() if x is not None and x.text else ""


def esmm_oku(kaynak: str) -> list[dict]:
    dosyalar = []
    if os.path.isdir(kaynak):
        for ad in sorted(os.listdir(kaynak)):
            if ad.lower().endswith(".xml"):
                with open(os.path.join(kaynak, ad), "rb") as f:
                    dosyalar.append((ad, f.read()))
    elif zipfile.is_zipfile(kaynak):
        with zipfile.ZipFile(kaynak) as z:
            for ad in sorted(z.namelist()):
                if ad.lower().endswith(".xml") and not ad.startswith("__MACOSX"):
                    dosyalar.append((ad, z.read(ad)))
    else:
        with open(kaynak, "rb") as f:
            dosyalar.append((os.path.basename(kaynak), f.read()))
    satirlar = []
    for ad, veri in dosyalar:
        try:
            kok = ET.fromstring(veri)
        except ET.ParseError as e:
            print(f"UYARI: {ad} okunamadı: {e}", file=sys.stderr)
            continue
        for m in kok.findall(".//e:serbestMeslekMakbuz", NS):
            v = {"kdv": D(0), "stopaj": D(0), "kdv_tevkifat": D(0)}
            oranlar = {}
            for vg in m.findall("./e:vergiBilgisi/e:vergi", NS):
                k = KOD.get(_t(vg, "e:vergiKodu"))
                if k:
                    v[k] += D(_t(vg, "e:vergiTutari") or "0")
            for vg in m.findall("./e:malHizmetBilgisi/e:malHizmet/e:vergiBilgisi/e:vergi", NS):
                k = KOD.get(_t(vg, "e:vergiKodu"))
                o = _t(vg, "e:vergiOrani")
                if k and o:
                    oranlar[k] = o
            tuzel = m.find("./e:aliciBilgileri/e:tuzelKisi", NS)
            gercek = m.find("./e:aliciBilgileri/e:gercekKisi", NS)
            if tuzel is not None:
                alici, kimlik, tur = _t(tuzel, "e:unvan"), _t(tuzel, "e:vkn"), "tuzel"
            elif gercek is not None:
                alici, kimlik, tur = _t(gercek, "e:adiSoyadi"), _t(gercek, "e:tckn") or _t(gercek, "e:vkn"), "gercek"
            else:
                alici, kimlik, tur = "", "", "?"
            ulke = _t(m, "./e:aliciBilgileri/e:adres/e:ulke")
            kalemler = [_t(x, "e:ad") for x in m.findall("./e:malHizmetBilgisi/e:malHizmet", NS)]
            brut = D(_t(m, "e:toplamTutar") or "0")
            satirlar.append({
                "dosya": ad, "makbuz_no": _t(m, "e:makbuzNo"), "tarih": _t(m, "e:belgeTarihi"),
                "alici": alici, "alici_kimlik": kimlik, "alici_tur": tur,
                "kamu_ipucu": bool(KAMU_IPUCU.search(alici or "")), "ulke": ulke,
                "kalemler": " | ".join(kalemler), "brut": brut, "kdv": v["kdv"], "stopaj": v["stopaj"],
                "kdv_tevkifat": v["kdv_tevkifat"], "tahsil": D(_t(m, "e:odenecekTutar") or "0"),
                "kdv_orani": oranlar.get("kdv", ""), "stopaj_orani": oranlar.get("stopaj", ""),
            })
    satirlar.sort(key=lambda s: (s["tarih"], s["makbuz_no"]))
    return satirlar


def kdv_tevkifat_siniri(tarih: str):
    """KDV GUT I/C-2.1.3.4.1 kısmi tevkifat sınırı (KDV dahil, işlem bazında)."""
    if tarih < "2021-07-01":
        return D(1000)
    if tarih < "2024-03-01":
        return D(2000)                     # KDV GUT Seri 36
    yil = int(tarih[:4])                   # Seri 50: işlem yılının VUK 232 fatura sınırı
    if yil == 2024:
        return D(6900)
    v = PARAMS.get(yil, {}).get("kdv_tevkifat_siniri")
    return D(v) if v is not None else None


def esmm_uyarilar(s: dict) -> list[str]:
    u = []
    beklenen = s["brut"] - s["stopaj"] + s["kdv"] - s["kdv_tevkifat"]
    if abs(beklenen - s["tahsil"]) > D("0.05"):
        u.append(f"tahsil tutarı tutmuyor (beklenen {tl(beklenen)})")
    if s["alici_tur"] == "tuzel" and s["stopaj"] == 0:
        u.append("tüzel kişi alıcı ama GV stopajı yok — alıcı GVK 94 sorumlusuysa %20 kesinti gerekir")
    if s["alici_tur"] == "gercek" and s["stopaj"] > 0:
        u.append("gerçek kişi alıcıda stopaj var — alıcı tacir/serbest meslek erbabı değilse stopaj yapılmaz")
    if re.search(r"BARO", s["alici"] or "", re.I) and s["kdv_orani"] and D(s["kdv_orani"]) != 10:
        u.append("baro alıcı: adli yardım hizmetinde KDV %10 (2007/13033 BKK (II) 32; özelge 38775) — kontrol edin")
    if (re.search(r"ÇOCUK|COCUK|BOŞANMA|BOSANMA|AİLE|AILE|NAFAKA|VELAYET|TÜKETİCİ|TUKETICI|VESAYET|ADLİ YARDIM|ADLI YARDIM",
                  s["kalemler"] or "", re.I) and s["kdv_orani"] and D(s["kdv_orani"]) != 10):
        u.append("aile/tüketici/çocuk mahkemesi, vesayet veya adli yardım işi: KDV %10 olabilir "
                 "(2007/13033 BKK (II) 32; özelge 32149, 38775) — kontrol edin")
    if s["kamu_ipucu"] and s["tarih"]:
        sinir = kdv_tevkifat_siniri(s["tarih"])
        kdv_dahil = s["brut"] + s["kdv"]
        if sinir is None:
            u.append(f"kamu alıcı: KDV tevkifatı sınırı {s['tarih'][:4]} için tanımsız — KDV dahil {tl(kdv_dahil)} TL'yi VUK 232 sınırıyla karşılaştırın")
        elif kdv_dahil > sinir and s["kdv_tevkifat"] == 0:
            u.append(f"kamu alıcı ve KDV dahil {tl(kdv_dahil)} > {tl(sinir)}: 5/10 KDV tevkifatı beklenirdi (KDV GUT I/C-2.1.3.2.13) "
                     "— makbuz birden fazla dosyayı kapsıyorsa sınır dosya bazında uygulanır (özelge 30159)")
        elif kdv_dahil <= sinir and s["kdv_tevkifat"] > 0:
            u.append(f"kamu alıcı ama KDV dahil {tl(kdv_dahil)} ≤ {tl(sinir)}: tevkifat sınır altında uygulanmamalıydı")
        elif kdv_dahil > sinir and s["kdv_tevkifat"] > 0:
            u.append(f"bilgi: 5/10 KDV tevkifatı uygulanmış (KDV dahil {tl(kdv_dahil)} > {tl(sinir)}); makbuz birden fazla "
                     "dosyayı kapsıyorsa her dosyanın ayrı ayrı sınırı aşıp aşmadığını kontrol edin (özelge 30159)")
    if s["ulke"] and s["ulke"].upper() not in ("TÜRKİYE", "TURKIYE", "TR") and s["kdv"] > 0:
        u.append(f"alıcı adresi {s['ulke']}: hizmetten yurt dışında faydalanılıyorsa KDVK 11/1-a istisnası değerlendirilmeli (Türkiye'deki taşınmaz/dava için genelde KDV'li)")
    return u


def ceyrek(tarih: str) -> str:
    y, m = tarih[:4], int(tarih[5:7])
    return f"{y}-Ç{(m - 1) // 3 + 1}"


def esmm_ozet(kaynak: str, csv_yolu: str | None, yil: int | None) -> None:
    satirlar = esmm_oku(kaynak)
    if yil:
        satirlar = [s for s in satirlar if s["tarih"].startswith(str(yil))]
    if not satirlar:
        print("Makbuz bulunamadı.")
        return
    alanlar = ["brut", "kdv", "kdv_tevkifat", "stopaj", "tahsil"]

    def topla(anahtar):
        t = defaultdict(lambda: defaultdict(lambda: D(0)))
        n = defaultdict(int)
        for s in satirlar:
            k = anahtar(s)
            n[k] += 1
            for a in alanlar:
                t[k][a] += s[a]
        return t, n

    for baslik, fn in (("AYLIK", lambda s: s["tarih"][:7]), ("ÇEYREK (geçici vergi dönemi)", lambda s: ceyrek(s["tarih"]))):
        t, n = topla(fn)
        print(f"\n== {baslik} ==")
        print(f"{'dönem':<10}{'adet':>5}{'brüt':>15}{'KDV':>13}{'KDV tevk.':>12}{'beyan KDV*':>13}{'GV stopaj':>13}{'tahsil':>15}")
        for k in sorted(t):
            v = t[k]
            print(f"{k:<10}{n[k]:>5}{tl(v['brut']):>15}{tl(v['kdv']):>13}{tl(v['kdv_tevkifat']):>12}"
                  f"{tl(v['kdv'] - v['kdv_tevkifat']):>13}{tl(v['stopaj']):>13}{tl(v['tahsil']):>15}")
    print("* beyan KDV: KDV1'de ödenecek hale gelen kısım (hesaplanan − alıcının 2 No.lu KDV ile beyan edeceği tevkifat).")

    print("\n== UYARILAR ==")
    var = False
    for s in satirlar:
        for u in esmm_uyarilar(s):
            var = True
            print(f"{s['makbuz_no']} {s['tarih']} {s['alici'][:40]}: {u}")
    if not var:
        print("Uyarı yok.")
    if csv_yolu:
        with open(csv_yolu, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            basliklar = ["makbuz_no", "tarih", "alici", "alici_kimlik", "alici_tur", "ulke", "kalemler",
                         "brut", "kdv", "kdv_tevkifat", "stopaj", "tahsil", "uyarilar"]
            w.writerow(basliklar)
            for s in satirlar:
                w.writerow([s[b] if b not in alanlar else str(s[b]).replace(".", ",") for b in basliklar[:-1]]
                           + [" / ".join(esmm_uyarilar(s))])
        print(f"\nCSV yazıldı: {csv_yolu}")


# ---------------------------------------------------------------------------
# Öz-sınama: GİB Rehberi (Yayın 590) örnekleri
# ---------------------------------------------------------------------------
def test() -> int:
    hatalar = 0

    def esit(ad, bulunan, beklenen, tol=D("0.01")):
        nonlocal hatalar
        ok = abs(D(bulunan) - D(beklenen)) <= tol
        hatalar += 0 if ok else 1
        print(f"{'OK ' if ok else 'HATA'} {ad}: {tl(bulunan)} (beklenen {tl(beklenen)})")

    # 2025 tarifesi — Rehber s.21 ve örnekler
    esit("Tarife sabit 330.000", gelir_vergisi(330000, 2025), 58100)
    esit("Tarife sabit 800.000", gelir_vergisi(800000, 2025), 185000)
    esit("Tarife sabit 4.300.000", gelir_vergisi(4300000, 2025), 1410000)
    esit("Tarife ücret 1.200.000", gelir_vergisi(1200000, 2025, ucret=True), 293000)
    esit("Tarife ücret 4.300.000", gelir_vergisi(4300000, 2025, ucret=True), 1378000)
    # 2026 tarifesi — 332 Seri No.lu GVGT md.3/(3) sabit tutarları
    esit("2026 sabit 400.000", gelir_vergisi(400000, 2026), 70500)
    esit("2026 sabit 1.000.000", gelir_vergisi(1000000, 2026), 232500)
    esit("2026 sabit 5.300.000", gelir_vergisi(5300000, 2026), 1737500)
    esit("2026 ücret 1.500.000", gelir_vergisi(1500000, 2026, ucret=True), 367500)
    esit("2026 ücret 5.300.000", gelir_vergisi(5300000, 2026, ucret=True), 1697500)
    esit("Örnek C (avukat) hesaplanan", gelir_vergisi(8900000, 2025), 3250000)
    c = yillik({"hasilat": 8000000, "diger_gelir": 900000, "gecici_vergi": 1200000, "tevkifat": 1000000,
                "uyum_indirimi": True}, 2025)
    esit("Örnek C (avukat) %5 indirim", c["uyum_indirimi"], 146055, tol=D("15"))
    esit("Örnek C (avukat) ödenecek", c["odenecek"], 903945, tol=D("15"))
    d = yillik({"hasilat": 2850000, "diger_gelir": 748000}, 2025)
    esit("Örnek 1 (avukat, konut kirası)", d["hesaplanan_vergi"], 1164300)
    e = yillik({"hasilat": 3185000, "gider": 1098500, "bagkur": 270000, "sigorta_primi": 156000}, 2025)
    esit("Örnek 2 matrah", e["matrah"], 1660500)
    esit("Örnek 2 vergi", e["hesaplanan_vergi"], 486175)
    f = yillik({"hasilat": 2925000, "gider": 676000, "bagis_tam": 65000}, 2025)
    esit("Örnek 3 vergi", f["hesaplanan_vergi"], 669400)
    g = yillik({"hasilat": 3445000, "gider": 832000, "bagkur": 208000, "engellilik_derece": 1}, 2025)
    esit("Örnek 4 vergi", g["hesaplanan_vergi"], 705170)
    h = yillik({"hasilat": 4160000, "diger_gelir": 795600}, 2025)
    esit("Örnek 5 vergi", h["hesaplanan_vergi"], 1672240)
    i = yillik({"hasilat": 4927000, "gider": 611000, "egitim_saglik": 494000, "tevkifat": 837590}, 2025)
    esit("Örnek 6 eğitim/sağlık sınırı", i["indirimler"]["egitim_saglik"], 431600)
    esit("Örnek 6 ödenecek", i["odenecek"], 426950)
    k = yillik({"hasilat": 4875000, "gider": 678600, "bagkur": 143000, "bagis_tam": 26000,
                "tevkifat": 975000, "uyum_indirimi": True}, 2025)
    esit("Örnek 7 (avukat) hesaplanan", k["hesaplanan_vergi"], 1314590)
    esit("Örnek 7 (avukat) %5 indirim", k["uyum_indirimi"], D("65729.50"))
    esit("Örnek 7 (avukat) ödenecek", k["odenecek"], D("273860.50"))
    # Makbuz: UHAP CMK dökümü (KDV dahil 9.627 → KDV hariç 8.022,50, 5/10 KDV tevkifatı)
    m = makbuz(kdv_dahil=9627, kdv_tevkifat=D("0.5"))
    esit("CMK iç yüzde brüt", m["brut"], D("8022.50"))
    esit("CMK stopaj", m["stopaj"], D("1604.50"))
    esit("CMK KDV tevkifatı", m["kdv_tevkifat"], D("802.25"))
    esit("CMK ödenecek", m["tahsil_edilecek"], D("7220.25"))
    m2 = makbuz(tahsil=10000, stopaj_orani=0)
    esit("Gerçek kişi, 10.000 tahsil → brüt", m2["brut"], D("8333.33"))
    m3 = makbuz(net=8000)
    esit("Net 8.000 → brüt", m3["brut"], 10000)
    gv = gecici_vergi([{"hasilat": 100000, "stopaj": 20000}, {"hasilat": 100000, "stopaj": 5000}])
    esit("Geçici vergi Ç1 (stopaj > vergi)", gv[0]["odenecek"], 0)
    esit("Geçici vergi Ç2 (kümülatif)", gv[1]["odenecek"], 5000)
    print(f"\n{'Tüm testler geçti.' if not hatalar else f'{hatalar} test başarısız.'}")
    return 1 if hatalar else 0


# ---------------------------------------------------------------------------
def makbuz_yazdir(r: dict, so, ko, to) -> None:
    def oran(x):
        x = D(x) * 100
        return f"%{x.normalize():f}".replace(".", ",")
    tev = f" ({(D(to) * 10).normalize():f}/10)" if to else ""
    satirlar = [
        ("Brüt ücret (KDV hariç)", r["brut"], ""),
        (f"GV stopajı {oran(so)}", -r["stopaj"], "ödeyen keser, muhtasarla beyan eder"),
        ("Net ücret", r["net_ucret"], ""),
        (f"KDV {oran(ko)}", r["kdv"], ""),
        (f"KDV tevkifatı{tev}", -r["kdv_tevkifat"], "alıcı 2 No.lu KDV ile beyan eder" if to else ""),
        ("Tahsil edilecek", r["tahsil_edilecek"], ""),
    ]
    print("┌" + "─" * 52 + "┐")
    for i, (ad, tutar, not_) in enumerate(satirlar):
        if ad == "Net ücret" or ad == "Tahsil edilecek":
            print("├" + "─" * 52 + "┤")
        sayi = ("−" if tutar < 0 else "") + tl(abs(tutar))
        print(f"│ {ad:<31}{sayi:>19} │")
    print("└" + "─" * 52 + "┘")
    print(f"  KDV dahil makbuz toplamı: {tl(r['kdv_dahil_toplam'])} · KDV1'de beyan edilecek KDV: {tl(r['tahsil_edilen_kdv'])}")


def yazdir(d: dict) -> None:
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{k}:")
            for kk, vv in v.items():
                print(f"  {kk}: {tl(vv)}")
        elif isinstance(v, list):
            for n in v:
                print(f"NOT: {n}")
        elif isinstance(v, Decimal):
            print(f"{k}: {tl(v)}")
        else:
            print(f"{k}: {v}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="komut", required=True)

    m = sub.add_parser("makbuz", help="e-SMM tutarlarını hesapla")
    g = m.add_mutually_exclusive_group(required=True)
    g.add_argument("--brut", type=D)
    g.add_argument("--net", type=D)
    g.add_argument("--tahsil", type=D)
    g.add_argument("--kdv-dahil", type=D, help="KDV dahil tutar (iç yüzde), ör. 'KDV hariç' denmeyen vekalet ücreti")
    m.add_argument("--stopaj", default="20", help="GV stopaj oranı: 20 (varsayılan), 17 (telif), 0 (gerçek kişi/sorumlu değil)")
    m.add_argument("--kdv", default="20", help="KDV oranı (varsayılan 20; istisna için 0)")
    m.add_argument("--kdv-tevkifat", default="0", help="KDV tevkifat oranı, ör. 5/10")

    v = sub.add_parser("vergi", help="gelir vergisi tarifesi")
    v.add_argument("matrah", type=D)
    v.add_argument("--yil", type=int, default=2026)
    v.add_argument("--ucret", action="store_true")

    gv = sub.add_parser("gecici", help="kümülatif geçici vergi")
    gv.add_argument("--donem", action="append", required=True,
                    help="hasılat,gider,stopaj (dönem içi). Her çeyrek için bir kez verin; sıra Ç1..Ç4")

    y = sub.add_parser("yillik", help="yıllık beyan simülasyonu")
    y.add_argument("--yil", type=int, default=2025)
    for a in ("hasilat", "gider", "bagkur", "diger_gelir", "egitim_saglik", "sigorta_primi", "bagis_sinirli",
              "bagis_tam", "diger_indirim", "gecmis_yil_zarari", "gecici_vergi", "tevkifat",
              "asgari_ucret_yillik_brut", "engellilik_aylik"):
        y.add_argument("--" + a.replace("_", "-"), dest=a, type=D)
    y.add_argument("--engellilik-derece", type=int)
    y.add_argument("--uyum-indirimi", action="store_true")
    y.add_argument("--json", action="store_true")

    e = sub.add_parser("esmm-ozet", help="e-SMM XML arşivini özetle")
    e.add_argument("kaynak", help="XML klasörü, .zip veya tek .xml")
    e.add_argument("--yil", type=int)
    e.add_argument("--csv")

    p = sub.add_parser("parametre")
    p.add_argument("--yil", type=int, default=2026)

    sub.add_parser("test")
    a = ap.parse_args(argv)

    if a.komut == "makbuz":
        so, ko, to = oran_coz(a.stopaj), oran_coz(a.kdv), oran_coz(a.kdv_tevkifat)
        r = makbuz(brut=a.brut, net=a.net, tahsil=a.tahsil, kdv_dahil=a.kdv_dahil,
                   stopaj_orani=so, kdv_orani=ko, kdv_tevkifat=to)
        makbuz_yazdir(r, so, ko, to)
    elif a.komut == "vergi":
        print(f"{a.yil} {'ücret' if a.ucret else 'ücret dışı'} tarifesi:")
        print("\n".join(tarife_tablosu(a.yil, a.ucret)))
        print(f"Matrah {tl(a.matrah)} → hesaplanan gelir vergisi {tl(gelir_vergisi(a.matrah, a.yil, a.ucret))} TL")
    elif a.komut == "gecici":
        ds = []
        for s in a.donem:
            parca = [x.strip() for x in s.split(",")] + ["0", "0"]
            ds.append({"hasilat": parca[0] or 0, "gider": parca[1] or 0, "stopaj": parca[2] or 0})
        print(f"{'Dönem':<6}{'Küm. matrah':>15}{'Hesaplanan':>13}{'Küm. stopaj':>13}{'Önce ödenen':>13}{'ÖDENECEK':>12}")
        for r in gecici_vergi(ds):
            print(f"{'Ç' + str(r['donem']):<6}{tl(r['kumulatif_matrah']):>15}{tl(r['hesaplanan']):>13}"
                  f"{tl(r['kumulatif_stopaj']):>13}{tl(r['onceki_odenen']):>13}{tl(r['odenecek']):>12}")
        print("Oran %15; kesilen stopaj ve önceki dönemlerde ödenen geçici vergi mahsup edilir (Rehber s.28-29).")
    elif a.komut == "yillik":
        girdi = {k: v for k, v in vars(a).items() if v is not None and k not in ("komut", "yil", "json")}
        r = yillik(girdi, a.yil)
        if a.json:
            print(json.dumps(r, default=str, ensure_ascii=False, indent=1))
        else:
            yazdir(r)
    elif a.komut == "esmm-ozet":
        esmm_ozet(a.kaynak, a.csv, a.yil)
    elif a.komut == "parametre":
        print(json.dumps(params(a.yil), ensure_ascii=False, indent=1, default=str))
    elif a.komut == "test":
        return test()
    return 0


if __name__ == "__main__":
    sys.exit(main())
