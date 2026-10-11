#!/usr/bin/env python3
"""Avukatlık Asgari Ücret Tarifesi (AAÜT) hesabı ve vergisel karşılığı.

Tarife: Türkiye Barolar Birliği, RG 04/11/2025, sayı 33067 (yayımı tarihinde yürürlükte,
md.24); değişiklikler RG 08/01/2026-33131 (md.10/2 mülga) ve RG 28/03/2026-33207 (md.14/5). Hükmün verildiği / hukuki yardımın tamamlandığı tarihteki tarife uygulanır (md.21).
Yeni tarife yayımlanınca TARIFELER sözlüğüne yeni anahtar ekleyin.

Alt komutlar:
  nispi        Üçüncü kısım nispi ücret (dilimli).
  maktu        İkinci kısım ikinci bölüm maktu ücret listesi / tek kalem.
  karsi-taraf  Karşı tarafa yükletilecek ücret (md.11, 13, 16 kuralları) + vergi/makbuz.
  test         Öz-sınama.

Vergi: Kararda "KDV hariç" ibaresi yoksa hükmedilen vekalet ücreti KDV dahil kabul edilir;
KDV iç yüzdeyle ayrılır, GV stopajı KDV hariç tutar üzerinden hesaplanır (311 Seri No.lu
GVGT md.25/5; GİB özelgesi 17/10/2022-245464). Stopajı ödeyen GVK 94 sorumlusu yapar;
gerçek kişi borçlu kesinti yapmaz. Makbuz borçlu (davayı kaybeden) adına düzenlenir.
"""
from __future__ import annotations

import argparse
import os
import sys
from decimal import Decimal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from smm_hesap import D, makbuz, oran_coz, r2, tl  # noqa: E402

TARIFELER = {
    "2025-11-04": {
        "kunye": "AAÜT, RG 04/11/2025-33067 (değ. RG 08/01/2026-33131, RG 28/03/2026-33207)",
        # Üçüncü kısım: (dilim genişliği, oran); son dilim sınırsız
        "nispi": [(600000, "0.16"), (600000, "0.15"), (1200000, "0.14"), (1200000, "0.13"),
                  (1800000, "0.11"), (2400000, "0.08"), (3000000, "0.05"), (3600000, "0.03"),
                  (4200000, "0.02"), (None, "0.01")],
        "icra_maktu_esik": 56250,          # md.11/1
        "arabuluculuk_maktu_esik": 50000,  # md.16/2-a
        # İkinci kısım ikinci bölüm (konusu para olmayan / maktu) — sıra no ile
        "maktu": {
            "icra-dairesi": (1, 9000), "icra-mahkemesi": (2, 11000), "icra-mahkemesi-durusmali": (3, 18000),
            "tahliye-icra": (4, 20000), "icra-ceza": (5, 15000), "cocuk-teslimi": (6, 16000),
            "sorusturma": (7, 11000), "sulh-hukuk": (8, 30000), "sulh-ceza": (9, 18000),
            "asliye": (10, 45000), "tuketici": (11, 22500), "fsmh": (12, 55000), "agir-ceza": (13, 65000),
            "cocuk": (14, 45000), "cocuk-agir-ceza": (15, 65000), "askerlik-disiplin": (16, 27000),
            "idare-durusmasiz": ("17a", 30000), "idare-durusmali": ("17b", 40000),
            "bam-ilk-derece": ("18a", 35000), "bam-istinaf-tek-durusma": ("18b", 22000),
            "bam-istinaf-cok-durusma": ("18c", 42000), "sayistay-durusmasiz": ("19a", 34000),
            "sayistay-durusmali": ("19b", 65000), "yargitay-ilk-derece": (20, 65000),
            "danistay-ilk-durusmasiz": ("21a", 40000), "danistay-ilk-durusmali": ("21b", 65000),
            "temyiz-durusmasi": (22, 40000), "uyusmazlik": (23, 40000), "aym-yuce-divan": ("24a", 120000),
            "aym-bireysel-durusmasiz": ("24b", 40000), "aym-bireysel-durusmali": ("24b", 80000),
            "aym-diger": ("24c", 90000),
        },
        # Birinci kısım ve ikinci kısım birinci bölüm — bilgi amaçlı
        "diger": {
            "Büroda sözlü danışma (ilk saat / sonraki her saat)": "4.000 / 1.800",
            "Çağrı üzerine gidilen yerde sözlü danışma (ilk saat / sonraki)": "7.000 / 3.500",
            "Yazılı danışma (ilk saat / sonraki)": "7.000 / 3.500",
            "Dilekçe, ihbarname, ihtarname, protesto": "6.000",
            "Kira sözleşmesi ve benzeri": "8.000",
            "Tüzük, yönetmelik, miras sözleşmesi, vasiyetname, vakıf senedi": "32.000",
            "Şirket ana sözleşmesi, devir/birleşme vb. ticari sözleşmeler": "21.000",
            "Arabuluculuk anlaşmazlıkla sonuçlanırsa taraf vekili (md.16/2-c)": "8.000",
            "İş takibi: belgelendirme, tahsil, örnek çıkarma": "6.000",
            "İş takibi: hakkın doğumu/tespiti/tescili/nakli/sona ermesi": "12.000",
            "İş takibi: ipotek tesis/fek vb. sürekli sözleşmeli bankalar için her işlem": "3.000",
            "Tüzel kişi tacir kuruluş, ruhsat, imtiyaz, devir, vatandaşlık işleri": "60.000",
            "Vergi komisyonlarında takip": "24.000",
            "Uluslararası yargı yerleri (duruşmasız / duruşmalı)": "110.000 / 200.000",
            "Tüketici hakem heyetleri (6502 s.K. 70/1 saklı; asıl alacağı geçemez)": "7.000",
            "Yapı kooperatifi sözleşmeli avukat aylık (Av.K. 35)": "27.000",
            "Anonim şirket sözleşmeli avukat aylık (Av.K. 35)": "45.000",
            "Özel/tüzel kişi ve kamu kurumu sözleşmeli avukat aylık": "33.000",
            "İhtiyati haciz/tedbir, delil tespiti vb. (duruşmasız / duruşmalı)": "10.000 / 12.500",
            "Ortaklığın giderilmesi satış memurluğu işleri": "18.000",
            "Ortaklığın giderilmesi ve taksim davaları": "40.000",
            "Vergi mahkemelerinde dava (duruşmasız / duruşmalı) — ikinci kısım birinci bölüm 4": "30.000 / 40.000",
            "Tüketici mahkemelerinde kredi taksit/faiz uyarlama davaları": "20.000",
        },
    },
}
VARSAYILAN = "2025-11-04"


def nispi(deger, tarife=VARSAYILAN) -> Decimal:
    kalan, toplam = D(deger), D(0)
    for genislik, oran in TARIFELER[tarife]["nispi"]:
        if kalan <= 0:
            break
        dilim = kalan if genislik is None else min(kalan, D(genislik))
        toplam += dilim * D(oran)
        kalan -= dilim
    return r2(toplam)


def karsi_taraf(deger=None, mahkeme="asliye", tur="dava", odeme_suresinde=False, tarife=VARSAYILAN,
                asil_alacak=None) -> dict:
    """tur: dava | icra | arabuluculuk-anlasma | maddi-tazminat-red | para-disi"""
    t = TARIFELER[tarife]
    notlar = []
    maktu = D(t["maktu"][mahkeme][1]) if mahkeme in t["maktu"] else None
    if tur == "para-disi":
        ucret = maktu
        notlar.append(f"Konusu para olmayan iş: {mahkeme} maktu ücreti (ikinci kısım ikinci bölüm).")
    elif tur == "maddi-tazminat-red":
        ucret = maktu
        notlar.append("Maddi tazminat davasının tamamen reddi: maktu ücret (md.13/4).")
    elif tur == "icra":
        mk = D(t["maktu"]["icra-dairesi"][1])
        if D(deger) <= D(t["icra_maktu_esik"]):
            ucret = min(mk, D(asil_alacak if asil_alacak is not None else deger))
            notlar.append(f"Takip miktarı ≤ {tl(t['icra_maktu_esik'])}: icra dairesi maktu ücreti, asıl alacağı geçemez (md.11/1).")
        else:
            ucret = nispi(deger, tarife)
            notlar.append("Takip miktarı eşik üstü: üçüncü kısım nispi ücret (md.11/1).")
        if odeme_suresinde:
            ucret = r2(ucret * D("0.75"))
            notlar.append("Borçlu ödeme süresinde ödedi: ücretin 3/4'ü (md.11/4).")
    elif tur == "arabuluculuk-anlasma":
        if D(deger) <= D(t["arabuluculuk_maktu_esik"]):
            ucret = r2(D(8000) * D("1.25"))
            notlar.append("≤ 50.000 TL: birinci kısım 1/6 maktu (8.000) + 1/4 fazlası (md.16/2-a).")
        else:
            ucret = r2(nispi(deger, tarife) * D("1.25"))
            notlar.append("Üçüncü kısım nispi + 1/4 fazlası (md.16/2-a). Bu, akdi ücretin asgarisidir.")
        ucret = min(ucret, D(asil_alacak if asil_alacak is not None else deger))
        notlar.append("Ücret asıl alacağı geçemez.")
    else:  # dava, konusu para
        n = nispi(deger, tarife)
        ucret = max(n, maktu) if maktu is not None else n
        if maktu is not None and maktu > n:
            notlar.append(f"Nispi ücret ({tl(n)}) maktu ücretin ({tl(maktu)}) altında: maktu uygulanır (md.13/1).")
        if ucret > D(deger):
            ucret = D(deger)
            notlar.append("Ücret kabul/red edilen miktarı geçemez (md.13/2).")
    notlar.append("Mahkeme tarifedeki miktarın 3 katına kadar hükmedebilir (md.3/1); bu asgari tutardır.")
    return {"ucret": ucret, "notlar": notlar}


def vergi_karsiligi(ucret, kdv_haric=False, stopaj_sorumlusu=True, kdv_tevkifat="0", kdv="20") -> dict:
    s = D("0.20") if stopaj_sorumlusu else D(0)
    k = oran_coz(kdv)
    if kdv_haric:
        return makbuz(brut=ucret, stopaj_orani=s, kdv_orani=k, kdv_tevkifat=oran_coz(kdv_tevkifat))
    return makbuz(kdv_dahil=ucret, stopaj_orani=s, kdv_orani=k, kdv_tevkifat=oran_coz(kdv_tevkifat))


def test() -> int:
    hata = 0

    def esit(ad, a, b):
        nonlocal hata
        ok = abs(D(a) - D(b)) <= D("0.01")
        hata += 0 if ok else 1
        print(f"{'OK ' if ok else 'HATA'} {ad}: {tl(a)} (beklenen {tl(b)})")

    esit("Nispi 600.000", nispi(600000), 96000)
    esit("Nispi 1.000.000", nispi(1000000), 96000 + 60000)
    esit("Nispi 18.600.000", nispi(18600000), 96000 + 90000 + 168000 + 156000 + 198000 + 192000 + 150000 + 108000 + 84000)
    esit("Nispi 20.000.000", nispi(20000000), nispi(18600000) + 14000)
    esit("Asliye 100.000 → maktu 45.000", karsi_taraf(100000, "asliye")["ucret"], 45000)
    esit("Asliye 30.000 → asıl alacak sınırı", karsi_taraf(30000, "asliye")["ucret"], 30000)
    esit("İcra 50.000 → maktu 9.000", karsi_taraf(50000, tur="icra")["ucret"], 9000)
    esit("İcra 100.000 süresinde ödeme", karsi_taraf(100000, tur="icra", odeme_suresinde=True)["ucret"], 12000)
    esit("Arabuluculuk 40.000 anlaşma", karsi_taraf(40000, tur="arabuluculuk-anlasma")["ucret"], 10000)
    v10 = vergi_karsiligi(33000, kdv="10")
    esit("Aile mahkemesi 33.000 KDV dahil %10 → brüt", v10["brut"], 30000)
    v = vergi_karsiligi(45000)
    esit("45.000 KDV dahil → brüt", v["brut"], 37500)
    esit("45.000 KDV dahil → stopaj", v["stopaj"], 7500)
    esit("45.000 KDV dahil → avukata ödenecek", v["tahsil_edilecek"], 37500)
    print("Tüm testler geçti." if not hata else f"{hata} test başarısız.")
    return 1 if hata else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tarife", default=VARSAYILAN, choices=sorted(TARIFELER))
    sub = ap.add_subparsers(dest="komut", required=True)
    n = sub.add_parser("nispi")
    n.add_argument("deger", type=D)
    m = sub.add_parser("maktu")
    m.add_argument("mahkeme", nargs="?")
    k = sub.add_parser("karsi-taraf")
    k.add_argument("deger", type=D, nargs="?", default=D(0), help="dava/takip değeri (kabul/red edilen miktar)")
    k.add_argument("--mahkeme", default="asliye")
    k.add_argument("--tur", default="dava", choices=["dava", "icra", "arabuluculuk-anlasma", "maddi-tazminat-red", "para-disi"])
    k.add_argument("--odeme-suresinde", action="store_true")
    k.add_argument("--asil-alacak", type=D)
    k.add_argument("--hukmedilen", type=D, help="Kararda yazan ücret (verilirse tarife hesabı atlanır)")
    k.add_argument("--kdv-haric", action="store_true", help="Kararda 'KDV hariç' ibaresi varsa")
    k.add_argument("--odeyen-gercek-kisi", action="store_true", help="Ödeyen GVK 94 sorumlusu değil (stopaj yok)")
    k.add_argument("--kdv-tevkifat", default="0", help="Ödeyen belirlenmiş alıcıysa ve sınır aşılıyorsa ör. 5/10")
    k.add_argument("--kdv", default="20", help="KDV oranı: 20 (genel) veya 10 (adli yardım, aile/tüketici/çocuk mahkemesi, "
                   "vesayet, iş uyuşmazlığında dava şartı arabuluculuk ve bunların ilamlı icrası — 2007/13033 BKK (II) 32)")
    sub.add_parser("test")
    a = ap.parse_args(argv)
    t = TARIFELER[a.tarife]
    if a.komut == "nispi":
        print(f"{t['kunye']} üçüncü kısım: {tl(a.deger)} → {tl(nispi(a.deger, a.tarife))} TL")
    elif a.komut == "maktu":
        if a.mahkeme:
            sira, u = t["maktu"][a.mahkeme]
            print(f"{a.mahkeme} (ikinci kısım ikinci bölüm sıra {sira}): {tl(u)} TL")
        else:
            for k_, (sira, u) in t["maktu"].items():
                print(f"{k_:<28} sıra {str(sira):<4} {tl(u):>12} TL")
            print("\nDiğer kalemler:")
            for k_, u in t["diger"].items():
                print(f"  {k_}: {u} TL")
    elif a.komut == "karsi-taraf":
        if a.hukmedilen is not None:
            ucret, notlar = a.hukmedilen, ["Kararda hükmedilen tutar esas alındı."]
        else:
            r = karsi_taraf(a.deger, a.mahkeme, a.tur, a.odeme_suresinde, a.tarife, a.asil_alacak)
            ucret, notlar = r["ucret"], r["notlar"]
        print(f"Vekalet ücreti: {tl(ucret)} TL ({'KDV hariç' if a.kdv_haric else 'KDV dahil kabul — 311 GVGT md.25/5'})")
        if a.kdv == "20":
            print("  (İş adli yardım, aile/tüketici/çocuk mahkemesi, vesayet veya iş uyuşmazlığında dava şartı "
                  "arabuluculuk kapsamındaysa KDV %10'dur: --kdv 10)")
        v = vergi_karsiligi(ucret, a.kdv_haric, not a.odeyen_gercek_kisi, a.kdv_tevkifat, a.kdv)
        print(f"  e-SMM brüt (KDV hariç): {tl(v['brut'])}\n  KDV %{oran_coz(a.kdv) * 100:.0f}: {tl(v['kdv'])}\n  GV stopajı: {tl(v['stopaj'])}"
              f"\n  KDV tevkifatı: {tl(v['kdv_tevkifat'])}\n  Avukata ödenecek: {tl(v['tahsil_edilecek'])}")
        print("  Makbuz: borçlu (davayı kaybeden) adına; icra müdürlüğüne nüsha gerekmez (311 GVGT md.26).")
        print("  (Borçlu ücreti müvekkile ödediyse, makbuz ödemeyi yapan müvekkil adına kesilir (md.26/5); "
              "teminat, haciz veya kefil yoluyla tahsilde tevkifat yapılmaz (md.25/6).)")
        for n_ in notlar:
            print(f"NOT: {n_}")
    elif a.komut == "test":
        return test()
    return 0


if __name__ == "__main__":
    sys.exit(main())
