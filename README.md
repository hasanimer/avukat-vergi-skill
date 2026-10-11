<div align="center">

# Avukat Vergi Asistanı

**Makbuzdan beyannameye, kaynağıyla.**

Serbest çalışan avukatın kendi vergi işleri için Claude Code skill'i: e-SMM hesabı, vekalet ücreti, CMK ve adli yardım ücretleri, KDV tevkifatı, geçici vergi, yıllık beyan ve giderler. Her cevap GİB rehberine, özelgeye veya mevzuat maddesine dayanır.

[![Paket kontrolü](https://github.com/hasanimer/avukat-vergi-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/hasanimer/avukat-vergi-skill/actions/workflows/validate.yml)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square)
![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-D97757?style=flat-square)

</div>

---

| **GİB Rehberi 590** | **2026 parametreleri** | **AAÜT 2025–2026** |
| :---: | :---: | :---: |
| Serbest Meslek Kazancı Rehberi (Şubat 2026), avukat odaklı ve sayfa referanslı | 332 GVGT, 588 VUK GT, 71 DVK GT ile tarife, had ve cezalar | Nispi ve maktu ücret, vergi karşılığına çeviri |

## Ne yapar?

<table>
<tr>
<td width="50%" valign="top">

<h3>01 · Makbuz hesabı</h3>
Brütten, netten, tahsil edilecek tutardan veya KDV dahil vekalet ücretinden e-SMM tutarlarını çıkarır: %20 stopaj, KDV (%20 veya %10), belirlenmiş alıcılarda 5/10 KDV tevkifatı ve tarihe göre tevkifat sınırı.

</td>
<td width="50%" valign="top">

<h3>02 · e-SMM arşiv denetimi</h3>
GİB e-SMM XML arşivini (zip veya klasör) okur. Aylık ve çeyreklik toplamları çıkarır, şu tutarsızlıkları işaretler: kamu alıcıda eksik veya fazla KDV tevkifatı, gerçek kişide stopaj, yurt dışı alıcıda KDV.

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h3>03 · Vekalet ücreti</h3>
AAÜT'ye göre ücreti hesaplar (md. 11, 13, 16) ve vergiye çevirir: tevkifatı kim yapar, makbuz kime kesilir, "KDV hariç" denmemişse iç yüzde (311 Seri No.lu GVGT md. 25-26).

</td>
<td width="50%" valign="top">

<h3>04 · Geçici ve yıllık vergi</h3>
Kümülatif geçici vergiyi (stopaj mahsubuyla) ve yıllık beyanı hesaplar: indirim sınırları, %5 uyum indirimi, mahsup ve iade. Rehber örneklerinin tamamı kuruşu kuruşuna doğrulanır.

</td>
</tr>
</table>

## Hızlı başlangıç

**Gerekenler:** Claude Code ve Python 3.9+. Betikler yalnız standart kütüphaneyi kullanır.

```bash
git clone https://github.com/hasanimer/avukat-vergi-skill.git ~/.claude/skills/avukat-vergi
```

```bash
cd ~/.claude/skills/avukat-vergi && python3 scripts/smm_hesap.py test && python3 scripts/aaut_hesap.py test
```

İsteğe bağlı olarak kişisel ayarlarınızı (muhasebe klasörü, e-SMM arşiv yolu, vergi dairesi) `references/kullanici-profili.local.md` dosyasına yazın. Bu dosya `.gitignore` ile depo dışında kalır.

## Kullanım örnekleri

- "Başsavcılığa KDV dahil 14.000 TL'lik CMK makbuzu keseceğim, tutarlar ne olur?"
- "Asliye hukukta 250.000 TL'lik davada karşı taraf vekalet ücreti ne olur, borçlu şirket icraya yatırırsa makbuzu kime keserim?"
- "Boşanma davası için gerçek kişi müvekkilden 50.000 TL + KDV alacağım, makbuzu hesapla."
- "Bu e-SMM arşivini özetle ve hataları göster: `~/…/e-smm-xml-arsivi.zip`"
- "2026 üçüncü dönem geçici vergimi hesapla: hasılat …, gider …, stopaj …"
- "Ev-ofis kiramı ve aracımın giderlerini nasıl yazarım?"

## Komutlar

```text
scripts/smm_hesap.py makbuz      --brut | --net | --tahsil | --kdv-dahil  [--stopaj 20|17|0] [--kdv 20|10] [--kdv-tevkifat 5/10]
scripts/smm_hesap.py vergi       <matrah> --yil 2026
scripts/smm_hesap.py gecici      --donem hasılat,gider,stopaj  (çeyrek başına)
scripts/smm_hesap.py yillik      --yil 2025 --hasilat … --gider … --bagkur … --tevkifat … --uyum-indirimi
scripts/smm_hesap.py esmm-ozet   <arşiv.zip|klasör> [--yil 2026] [--csv çıktı.csv]
scripts/aaut_hesap.py karsi-taraf <değer> --mahkeme asliye | --hukmedilen 45000 [--kdv 10] [--odeyen-gercek-kisi]
scripts/aaut_hesap.py maktu | nispi <değer>
scripts/ozelge_guncelle.py       --sadece-yeni   (GİB'den yeni "avukat" özelgeleri)
```

## Kaynaklar

| Kaynak | Kapsam |
|---|---|
| GİB, *Serbest Meslek Kazancı Elde Eden Mükellefler İçin Vergi Rehberi*, Şubat 2026, Yayın No 590 | `references/rehber-590-avukat.md`, tam metin `references/kaynak/` |
| 332 Seri No.lu GVGT, 588 Sıra No.lu VUK GT, 71 Seri No.lu DVK GT (RG 31/12/2025-33124 5. Mük.) | `references/parametreler.md` |
| Avukatlık Asgari Ücret Tarifesi (RG 04/11/2025-33067; değişiklikler 08/01/2026 ve 28/03/2026) | `references/aaut-2025-2026.md` |
| KDV GUT I/C-2.1.3.2.13, I/C-2.1.3.4.1; Seri 36 ve 50; 2007/13033 BKK (II) 32 | `references/kdv.md` |
| 311 Seri No.lu GVGT md. 25-26; GVK 94/3; GİB özelgeleri | `references/vekalet-ucreti.md` |

**Güncellik:** 12/10/2026. Tutar ve oranlar yıllık değişir; `references/parametreler.md` dosyasındaki tarihlere bakın.

**Durum:** Avukatlık faaliyetine ilişkin 450'yi aşkın GİB özelgesinin konu bazlı sentezi ekleniyor (SMM, KDV, giderler, yan faaliyetler, mükellefiyet, damga vergisi).

## Uyarı

Bu skill bilgi amaçlıdır; mali müşavirlik veya hukuki görüş yerine geçmez. Özelgeler yalnızca talep eden mükellefi bağlar (VUK 413). Beyan ve ödeme öncesinde güncel tutarları ve GİB duyurularını kontrol edin.

## Lisans

Kod ve özgün metinler MIT lisanslıdır. GİB yayınları, Resmî Gazete metinleri ve özelgeler resmî belgelerdir; kaynak gösterilerek alıntılanmıştır.
