# Parametreler: tutarlar, oranlar, sınırlar ve tarihler (2025 / 2026)

Son kontrol: **12/10/2026**.
- 2026 tutarlarının çoğu 31/12/2025 tarihli Resmî Gazete'nin 5. mükerrer sayısındaki (33124) tebliğlere dayanır:
  - 332 Seri No.lu GVGT
  - 588 Sıra No.lu VUK GT
  - 71 Seri No.lu DVK GT
- 2025 yeniden değerleme oranı %25,49'dur (VUK GT 585). Harç ve damga vergisinin maktu tutarları CBK 10783 ile %18,95 artırıldı.
- "Gelir yılı" ile beyan yılını karıştırma. 2026 kazancı Mart 2027'de beyan edilir.

> Bu tablodaki bir değer `scripts/smm_hesap.py` içindeki `PARAMS` sözlüğünden farklıysa betiği düzelt. Her Ocak ayında yeni tebliğlerle güncelle.

## Gelir vergisi tarifesi (GVK 103)
| | 2025 (Rehber s.21) | 2026 (332 Seri No.lu GVGT md.3/3) |
|---|---|---|
| %15 | 158.000 TL'ye kadar | 190.000 TL'ye kadar |
| %20 | 330.000 TL'ye kadar; sabit 23.700 TL | 400.000 TL'ye kadar; sabit 28.500 TL |
| %27 | 800.000 TL'ye kadar; sabit 58.100 TL (ücrette 1.200.000) | 1.000.000 TL'ye kadar; sabit 70.500 TL (ücrette 1.500.000) |
| %35 | 4.300.000 TL'ye kadar; sabit 185.000 TL (ücrette 293.000) | 5.300.000 TL'ye kadar; sabit 232.500 TL (ücrette 367.500) |
| %40 | Fazlası; sabit 1.410.000 TL (ücrette 1.378.000) | Fazlası; sabit 1.737.500 TL (ücrette 1.697.500) |

Serbest meslek kazancına **ücret dışı** tarife uygulanır.

## Kazanç, istisna ve indirimler
| Kalem | 2025 | 2026 | Dayanak |
|---|---|---|---|
| Telif istisnası üst sınırı (GVK 18; aşılırsa tamamı beyan edilir) | 4.300.000 | 5.300.000 | Rehber s.13; 4. dilim |
| Arızi serbest meslek kazancı istisnası (GVK 82) | 280.000 | 350.000 | 332 md.3/2-ı |
| Genç girişimci istisnası (GVK mük. 20) | 330.000 | 400.000 | 2. dilim |
| Mesken kira istisnası (GVK 21). **Serbest meslek kazancı beyan edenler yararlanamaz.** | 47.000 | 58.000 | 332 md.3/2-b; Rehber Örnek 1 |
| Beyanname verme sınırı (GVK 86/1-c; 2. dilim) | 330.000 | 400.000 | Rehber Örnek 5 |
| Tevkifata ve istisnaya konu olmayan MSİ+GMSİ beyan sınırı (GVK 86/1-d) | — | 22.000 | 332 md.3/2-i |
| Engellilik indirimi, aylık (1. / 2. / 3. derece) | 9.900 / 5.700 / 2.400 | 12.000 / 7.000 / 3.000 | 332 md.3/2-d (2025 için 1. derece Rehber Örnek 4) |
| Yıllık brüt asgari ücret (şahıs sigortası primi indirim sınırı; %15 ile birlikte) | 312.066 | 396.360 (33.030 × 12) | AÜTK kararı, RG 26/12/2025-33119 |
| %5 uyum indirimi azami tutarı | 12.000.000 (01/01/2026'dan itibaren verilen beyannameler, yani 2025 kazancı) | 2027 beyanı için yeniden belirlenecek | 332 md.3/4 |
| Eğitim ve sağlık harcaması | Beyan edilen gelirin %10'u | Aynı | GVK 89/1-2 |
| Bağış (genel) | %5 (kalkınmada öncelikli yörelerde %10) | Aynı | GVK 89/1-4 |
| Yurt dışına verilen hizmet indirimi (GVK 89/1-13) | %80 | **%100** (CBK 11257, RG 30/04/2026-33239; 1/1/2026'dan itibaren başlayan dönemler) | 7491 s.K. **Avukatlık ve hukuki danışmanlık kanundaki kapalı listede yok**; yararlanılamaz (89/1-15 mülgadır) |

## Binek otomobil (GVK 68/1-4, 68/1-5)
| | 2025 | 2026 |
|---|---|---|
| Amortismana esas ilk iktisap bedeli (ÖTV ve KDV hariç) | 1.100.000 | 1.380.000 |
| ÖTV ve KDV maliyete eklenmişse veya ikinci el | 2.100.000 | 2.600.000 |
| Kiralık binek araç, aylık kira | 37.000 | 46.000 |
| Gider yazılabilecek ÖTV+KDV | 990.000 | 1.200.000 |
| Diğer binek araç giderleri | %70 | %70 |

Amortisman sınırında aracın **alındığı tarihteki** tutar uygulanır.

## Stopaj (tevkifat), KDV ve geçici vergi oranları
| Kalem | Oran | Dayanak |
|---|---|---|
| Avukatlık ücreti, karşı taraf vekalet ücreti (GVK 94/2-b) | %20 | 2009/14592 BKK. CBK 11344 (RG 19/05/2026) bu oranı değiştirmedi |
| Telif (GVK 94/2-a, GVK 18 kapsamı) | %17 | Aynı |
| İş yeri kirası (GVK 94/5-a; avukat kiracıysa ödeme sırasında keser) | %20 | Teyit için `giderler.md` |
| KDV genel oranı | %20 (10/07/2023'ten itibaren; öncesi %18) | |
| KDV indirimli oran: adli yardım, aile, tüketici ve çocuk mahkemesi davaları, vesayet, dava şartı iş arabuluculuğu ve bunların ilamlı icrası | **%10** (10/07/2023'ten itibaren; 01/12/2021 – 09/07/2023 arasında %8) | 2007/13033 BKK (II) 32; CBK 4862; özelge 38775 (02/07/2025). Bkz. `kdv.md` |
| KDV tevkifatı: belirlenmiş alıcılara (kamu idaresi, baro, banka vb.) avukatlık hizmeti | **5/10** (I/C-2.1.3.2.13) | Yargı mercileri önündeki hizmet 9/10 danışmanlık kapsamında değildir (I/C-2.1.3.2.2.2) |
| Geçici vergi | %15 (tarifenin ilk dilim oranı) | GVK mük. 120 |
| Vergiye uyum indirimi | Hesaplanan verginin mesleki kazanca isabet eden kısmının %5'i | GVK mük. 121 |

## KDV kısmi tevkifat sınırı (I/C-2.1.3.4.1; KDV dahil, işlem bazında)
- **2014 – 30/06/2021:** 1.000 TL
- **01/07/2021 – 29/02/2024:** 2.000 TL (Seri 36)
- **01/03/2024'ten itibaren:** işlem yılının **VUK 232 fatura sınırı** (Seri 50)
  - 2024: 6.900 TL
  - **2025: 9.900 TL**
  - **2026: 12.000 TL** (VUK GT 588)
- Başsavcılığa kesilen arabuluculuk makbuzlarında GİB sınırı **dosya bazında** uygulamıştır (özelge 30159, 07/11/2023).

## Damga vergisi (beyanname başına, 01/01/2026'dan itibaren; DVK GT 71)
| Beyanname | 2026 |
|---|---|
| Yıllık gelir vergisi beyannamesi | 1.189,50 TL |
| KDV beyannamesi | 791,00 TL |
| Muhtasar beyanname | 791,00 TL |
| Geçici vergi beyannamesi ("diğer beyannameler" grubu) | 791,00 TL |
| Muhtasar ve prim hizmet beyannamesi | 939,70 TL |

## Cezalar ve hadler (2026; VUK GT 588)
| Kalem | 2026 |
|---|---|
| **e-SMM vermeme, almama veya eksik/yanlış tutarla düzenleme (VUK 353/1)** | Her belge için tutarın %10'u. Asgari ceza 1. tespitte 17.000; 2. tespitte 35.000; 3. tespitte 53.000; 4. tespitte 70.000; 5. tespitte 87.000; 6. ve sonraki tespitlerde 170.000 TL. Yıllık üst sınır 17.000.000 TL |
| Mükellef olmayan müvekkilin SMM almaması (VUK 353/3) | Belge başına 8.700 TL, yıllık en fazla 87.000 TL. Belgenin düzenlenmediğini 5 iş günü içinde bildirirse ceza kesilmez |
| Tevsik zorunluluğuna uymama (VUK mük. 355) | İşlem tutarının %10'u; serbest meslek erbabı için asgari 35.000 TL; yıllık üst sınır 35.000.000 TL |
| Tevsik haddi (459 Sıra No.lu VUK GT; 575 ile 30/11/2024'ten itibaren) | **30.000 TL**. Ücret taksitle tahsil edilse bile sözleşmenin toplam tutarı esas alınır |
| İş yeri kirası tevsiki | Tutar sınırı yok |
| I. ve II. derece usulsüzlük (serbest meslek erbabı) | 17.000 / 8.700 TL |
| Mük. 355/1: bilgi vermeme ve 257 vb. zorunluluklara uymama (serbest meslek erbabı) | 35.000 TL |
| e-tebligat zorunluluğuna uymama (VUK 107/A) | 12.000 TL |
| Doğrudan gider yazılabilecek demirbaş (VUK 313) | 12.000 TL |
| VUK 232 fatura sınırı | 12.000 TL |
| Uzlaşmaya konu usulsüzlük ve özel usulsüzlük cezası eşiği | 40.000 TL'nin üzeri (VUK GT 592) |

## İade (252 Seri No.lu GVGT)
| | 2025 | 2026 |
|---|---|---|
| Tevkifat nakden iadesi: inceleme ve teminatsız | 340.000 | 426.000 |
| YMM tam tasdik raporuyla | 3.400.000 | 4.266.000 |
| Geçici vergi iadesi | Tutar sınırı yok. Yıl sonuna kadar talep edilir (1B) | Aynı |

## SGK 4/1-b (Bağ-Kur) 2026
- **Prime esas kazanç:**
  - Alt sınır günlük 1.101 TL, aylık 33.030 TL.
  - Üst sınır alt sınırın **9 katıdır** (7566 s.K.): aylık 297.270 TL.
- **Prim oranı:** %35,75 (MYÖ %21, kısa vadeli sigorta %2,25, GSS %12,5). Süresinde ödeyene 5 puan indirim uygulanır ve oran %30,75'e düşer (teyit: orta güven).
  - Alt sınırda aylık yaklaşık 11.808 TL, indirimle 10.157 TL.
- Bağ-Kur primi serbest meslek kazancının tespitinde indirilir. Bkz. `giderler.md`.

## Takvim
| Yükümlülük | Süre |
|---|---|
| Yıllık gelir vergisi beyanı | 1–31 Mart (2025 kazancı için 31/03/2026; 2026 kazancı için 31/03/2027) |
| Yıllık gelir vergisi ödemesi | 1. taksit 31 Mart (damga vergisiyle birlikte), 2. taksit 31 Temmuz. Hafta sonuna denk gelirse ertesi iş günü (VUK 18) |
| Geçici vergi | 17 Mayıs (2026'da 18 Mayıs'a kaydı), 17 Ağustos, **17 Kasım 2026** (Ocak–Eylül dönemi), 17 Şubat 2027 (4. dönem, 7566 s.K.) |
| KDV beyannamesi (aylık) | İzleyen ayın 28'i (beyan ve ödeme) |
| Muhtasar / MUHSGK (kira stopajı, personel) | İzleyen ayın 26'sı |
| İşe başlama bildirimi | 10 gün |
| Defter-Beyan başvurusu | İşe başlama bildirimini izleyen 7. iş günü |
| e-SMM'ye geçiş | İşe başlanan ayı izleyen 3. ayın sonu |
| Adres veya iş değişikliği ve işi bırakma bildirimi | 1 ay |
| Gider pusulası | 7 gün |
| Belge saklama | İzleyen yıldan itibaren 5 yıl |
| Tevkifat fazlası iadesi | Bildirim veya tebliğden itibaren 1 yıl |
| Uyum indirimi devri | Beyan süresini izleyen 1 yıl |

> Kanun metinleriyle uygulama arasında farklar var:
> - GVK 92'nin konsolide metni yıllık beyan için "25 Mart" diyor; Rehber ve uygulama 31 Mart.
> - GVK mük. 120/3 geçici vergi beyanı için "14'ü", ödeme için "17'si" diyor; uygulamada beyan da 17'sinde yapılıyor.
>
> Son günü her yıl GİB duyurusu ve sirkülerlerinden teyit et. Uzatmalar VUK sirküleriyle yapılır (ör. VUK-199/2026-5, Nisan 2026 KDV ve muhtasar).

## 2026'da yapılan ve avukatı etkileyen değişiklikler (Rehber'de yer almıyor)
- **e-tebligat:** 7587 s.K. md.9 (RG 01/07/2026) ile VUK 107/A yeniden yazıldı. Gerçek usulde vergilendirilen serbest meslek erbabı e-tebligatı kanun gereği kullanmak zorunda. Tebliğ, iletiyi izleyen **5. günün sonunda** yapılmış sayılır. Dava ve uzlaşma süreleri buna göre başlar.
- **Tecil:** 7582 s.K. md.1 (RG 04/06/2026) ile 6183 md.48 kapsamında azami süre 72 aya çıktı. Teminatsız tecil sınırı CBK 11414 ile 10.000.000 TL. Düşük faizli tecil kampanyası (Tahsilat GT B-20) 31/08/2026'da sona erdi.
- **Varlık barışı (KVK geçici 19):** Başvuru 31/07/2027'ye kadar. Serbest meslek erbabı bildirilen kıymetleri defterinde gösterir.
- **Yurt dışı kazanç istisnası (GVK mük. 20/D):** Türkiye'de verilen avukatlık hizmetinin kazancına uygulanmaz.
- **Cezalarda uzlaşma:** VUK GT 592 (RG 28/03/2026) yetkili komisyonları belirledi; eşik 40.000 TL.
- **AAÜT değişiklikleri:** RG 08/01/2026 ve 28/03/2026. Bkz. `aaut-2025-2026.md`.
- **CMK Ücret Tarifesi 2026:** RG 08/01/2026-33131. Bkz. `ek-faaliyetler.md`.
- **7589 s.K. (yargı paketi, RG 31/07/2026):**
  - Yalnız vekalet ücreti veya yargılama giderine ilişkin BAM ve BİM kararları temyiz edilemiyor (HMK 362/3-b, İYUK 46).
  - İdare ve vergi mahkemelerinde tek hakim sınırı 486.000 TL oldu.
  - Vergi hükmü yok.
- **Değişmeyenler:** %20 serbest meslek stopajı, GVK 94/3 (AYM E.2024/94, K.2025/179 ile iptal talebi reddedildi), 311 GVGT md.25-26, e-SMM (509 Sıra No.lu VUK GT), %5 uyum indirimi şartları, GVK 69 hasılat tespiti.
