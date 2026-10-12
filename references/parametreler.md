# Parametreler: tutarlar, oranlar, sınırlar ve tarihler (2025 / 2026)

Son kontrol: **12/10/2026**. Tutarlar, oranlar ve tarihler aynı gün tarihli doğrulama paketiyle tek tek karşılaştırıldı.
- 2026 tutarlarının çoğu 31/12/2025 tarihli Resmî Gazete'nin 5. mükerrer sayısındaki (33124) tebliğlere dayanır:
  - 332 Seri No.lu GVGT
  - 588 Sıra No.lu VUK GT
  - 71 Seri No.lu DVK GT
- 2025 VUK tutarları 577 Sıra No.lu VUK GT'dedir (RG 30/12/2024-32768, 2. Mük.).
- 2025 yeniden değerleme oranı %25,49'dur (VUK GT 585, RG 27/11/2025-33090). Harç ve damga vergisinin maktu tutarları CBK 10783 (30/12/2025) ile %18,95 artırıldı. 12/10/2026'ya kadar bu tutarları değiştiren bir ara düzenleme yayımlanmadı.
- "Gelir yılı" ile beyan yılını karıştırma. 2026 kazancı Mart 2027'de beyan edilir.
- GİB'in 26/09/2026 tarihli yayın kataloğunda Şubat 2026 tarihli Serbest Meslek Kazancı Rehberi'nin (Yayın 590) yeni sürümü yok. 2026 değişiklikleri ayrı yayınlarda: 603 (işe yeni başlayan serbest meslek erbabı), 610 (tecil), 611–612 (uzlaşma), 613 (varlık barışı), 615 (cezalarda indirim), 616 (yurt dışı kazanç istisnası).
- **2027 tutarları henüz yayımlanmadı.** Bekleyenler:
  - Mart 2027'de verilecek beyannamenin damga vergisi
  - Mük. 121 azami indirim tutarı (01/01/2027'den itibaren verilecek beyannameler)
  - 2027 nakden iade hadleri
  - 2027 GVK, VUK ve DVK tutarları; 2027'de KDV tevkifat sınırı 2027 VUK 232 sınırı olacak
  - 2027 asgari ücreti ve Bağ-Kur sınırları

  Dayanak 2026 yeniden değerleme oranıdır (Kasım 2026'da ilan edilir) ve Aralık sonu tebliğleridir. 2026 tarifesi 2026 kazancına uygulanmaya devam eder.
- **"(teyit edilmedi)"** yazan değer 12/10/2026 doğrulamasında birincil kaynaktan teyit edilemedi. Kullanmadan önce doğrula.

> Bu tablodaki bir değer `scripts/smm_hesap.py` içindeki `PARAMS` sözlüğünden farklıysa betiği düzelt. Her Ocak ayında yeni tebliğlerle güncelle.

## Gelir vergisi tarifesi (GVK 103)
| | 2025 (Rehber s.21) | 2026 (332 Seri No.lu GVGT md.3/3) |
|---|---|---|
| %15 | 158.000 TL'ye kadar | 190.000 TL'ye kadar |
| %20 | 330.000 TL'ye kadar; sabit 23.700 TL | 400.000 TL'ye kadar; sabit 28.500 TL |
| %27 | 800.000 TL'ye kadar; sabit 58.100 TL (ücrette 1.200.000) | 1.000.000 TL'ye kadar; sabit 70.500 TL (ücrette 1.500.000) |
| %35 | 4.300.000 TL'ye kadar; sabit 185.000 TL (ücrette 293.000) | 5.300.000 TL'ye kadar; sabit 232.500 TL (ücrette 367.500) |
| %40 | Fazlası; sabit 1.410.000 TL (ücrette 1.378.000) | Fazlası; sabit 1.737.500 TL (ücrette 1.697.500) |

Serbest meslek kazancına **ücret dışı** tarife uygulanır. 12/10/2026'ya kadar GVK 103'ü değiştiren kanun çıkmadı; 7582, 7587, 7590 ve 7594 sayılı Kanunlar bu maddeye dokunmuyor.

## Kazanç, istisna ve indirimler
| Kalem | 2025 | 2026 | Dayanak |
|---|---|---|---|
| Telif istisnası üst sınırı (GVK 18). Aşılırsa tamamı beyan edilir ve ödeyen tevkifat yapmaz | 4.300.000 | 5.300.000 | Rehber s.13; 4. dilim |
| Arızi serbest meslek kazancı istisnası (GVK 82) | 280.000 | 350.000 | 332 md.3/2-ı; Rehber s.11 |
| Genç girişimci istisnası (GVK **mük. 20**; mük. 20/A basit usul istisnasıdır, karıştırma). Şartlar: ilk kez mükellefiyet, başlangıçta 29 yaşın doldurulmamış olması, 3 vergilendirme dönemi. Kazanç olmasa da beyanname verilir. GVK 94 tevkifatını etkilemez | 330.000 | 400.000 | 2. dilim; Rehber s.13–14 |
| Mesken kira istisnası (GVK 21). **Serbest meslek kazancı beyan edenler yararlanamaz.** Gayrisafi gelirleri toplamı ücret tarifesinin 3. dilimini (2025: 1.200.000; 2026: 1.500.000) aşanlar da yararlanamaz | 47.000 | 58.000 | 332 md.3/2-b; Rehber Örnek 1 |
| Beyanname verme sınırı (GVK 86/1-c; 2. dilim). GİB, serbest meslek kazancını da toplama katar: serbest meslek kazancı ile brüt iş yeri kirası toplamı sınırı aşarsa kira da beyana girer. Bu nedenle avukatın tevkifatlı kira geliri pratikte beyana girer. Tek işverenden alınan tevkifatlı ücret ise 86/1-b sınırına kadar girmez; "zaten beyanname veriyorum, her gelir girer" genellemesi yanlıştır | 330.000 | 400.000 | Rehber Örnek 5; 332 md.3/3 |
| Tevkifatlı ücretin beyan dışı kalma sınırı (GVK 86/1-b; 4. dilim). Birden fazla işverenden ücret alınıyorsa iki şart birlikte aranır: ikinci ve sonraki işverenlerden alınanlar 2. dilimi, birinci işveren dahil tüm ücretler 4. dilimi aşmamalı. Biri bozulursa tüm ücretler beyan edilir (bilirkişilik ücreti alan avukat için önemli) | 4.300.000 | 5.300.000 | GVK 86/1-b (7194 md.15); 332 md.3/3 |
| Tevkifata ve istisnaya konu olmayan MSİ+GMSİ beyan sınırı (GVK 86/1-d) | — | 22.000 | 332 md.3/2-i |
| Engellilik indirimi, aylık (1. / 2. / 3. derece). Serbest meslek erbabı yıllık uygular (GVK 89/1-3). Bakmakla yükümlü olunan engelli kişi için de geçerlidir | 9.900 / 5.700 / 2.400 | 12.000 / 7.000 / 3.000; yıllık 144.000 / 84.000 / 36.000 | 332 md.3/2-d; 2025: 329 Seri No.lu GVGT (RG 30/12/2024-32768, 2. Mük.) ve Rehber Örnek 4 (9.900 × 12 = 118.800) |
| Yıllık brüt asgari ücret (şahıs sigortası primi indirim sınırı; %15 ile birlikte) | 312.066 (Rehber Örnek 2) | 396.360 (günlük 1.101; aylık 33.030 × 12). 2026'da ara zam yapılmadı | AÜTK Karar 2025/1, RG 26/12/2025-33119 |
| %5 uyum indirimi azami tutarı | 12.000.000 (01/01/2026'dan itibaren verilen beyannameler, yani 2025 kazancı) | Mart 2027 beyanı için Aralık 2026 sonunda yeniden belirlenecek; henüz yayımlanmadı | 332 md.3/4 |
| Eğitim ve sağlık harcaması | Beyan edilen gelirin %10'u | Aynı | GVK 89/1-2 |
| Bağış (genel) | %5 (kalkınmada öncelikli yörelerde %10) | Aynı | GVK 89/1-4 |
| Yurt dışına verilen hizmet indirimi (GVK 89/1-13) | %80 (1/1/2023–31/12/2025 kazançları; 7491 md.10) | **%100** (CBK 11257, RG 30/04/2026-33239; 1/1/2026'dan itibaren başlayan dönemler). Bedesten'deki konsolide metin CB kararını işlemediği için hâlâ %80 gösterir | **Avukatlık ve hukuki danışmanlık kanundaki kapalı listede yok**; yararlanılamaz. Bu sonuç kapalı listeden çıkarılmıştır; doğrudan avukatlığa ilişkin özelge yoktur. GİB, sayılan alanlardaki danışmanlığı da kapsam dışı sayıyor. 89/1-15, 7338 md.5 ile mülgadır |

### Asgari ücret istisnası (2026; GVK 23/1-18, DVK (2) sayılı tablo IV-34)
Yalnız **ücret** sayılan ödemelere uygulanır: mahkeme bilirkişiliği, CMK uzlaştırmacılığı, kayyımlık, meslek kuruluşu huzur hakkı vb. (bkz. `ek-faaliyetler.md` §1, §6, §10). Serbest meslek kazancına uygulanmaz.
- Aylık brüt asgari ücret 33.030 TL. İşçi payları: SGK %14 (MYÖ %9 + GSS %5; 5510 md.81/a ve f) ve işsizlik %1 (4447 md.49). Gelir vergisi matrahı 33.030 × 0,85 = 28.075,50 TL.
- **Gelir vergisi istisnası, aylık (hesap; 2026 tarifesi):** Ocak–Haziran 4.211,33 TL; Temmuz 4.537,75 TL (asgari ücretin kümülatif matrahı bu ayda 190.000 TL'lik ilk dilimi aşar); Ağustos–Aralık 5.615,10 TL.
- Ödenecek vergi, ücretin tamamı üzerinden hesaplanan vergiden o ayın istisna tutarı düşülerek bulunur. İstisna, o ay asgari ücret üzerinden hesaplanan vergiyi aşamaz. Birden fazla işverenden ücret alınıyorsa yalnız en yüksek ücrete uygulanır (GVK 23/1-18).
- **Damga vergisi istisnası, aylık:** brüt asgari ücrete isabet eden kısım; 33.030 × binde 7,59 = 250,70 TL (7349 s.K. md.4; özelge 22482).
- Zorunlu yol ve masraf ödemeleri dahil aylık toplama bir kez uygulanır (`ek-faaliyetler.md` §6).

## Binek otomobil (GVK 68/1-4, 68/1-5)
| | 2025 | 2026 |
|---|---|---|
| Amortismana esas ilk iktisap bedeli (ÖTV ve KDV hariç) | 1.100.000 | 1.380.000 |
| ÖTV ve KDV maliyete eklenmişse veya ikinci el | 2.100.000 | 2.600.000 |
| Kiralık binek araç, aylık kira | 37.000 | 46.000 |
| Gider yazılabilecek ÖTV+KDV | 990.000 | 1.200.000 |
| Diğer binek araç giderleri | %70 | %70 |

Amortisman sınırında aracın **alındığı tarihteki** tutar uygulanır. Kaynak: 332 md.3/2-e ve 2-ğ; Rehber s.9–10. Binek otomobil alışındaki KDV indirilemez (KDVK 30/b).

## Stopaj (tevkifat), KDV ve geçici vergi oranları
| Kalem | Oran | Dayanak |
|---|---|---|
| Avukatlık ücreti, karşı taraf vekalet ücreti (GVK 94/2-b) | %20 (kanuni oran %25; Cumhurbaşkanı değiştirmeye yetkili) | 2009/14592 BKK. 2024–2026'da BKK'yı değiştiren kararlar (9284, 9286, 9707, 11344) bu oranı değiştirmedi. CBK 11344 (18/05/2026; RG 19/05/2026-33258) yalnız eki Kararın 1/1-(3) bendine nükleer santral inşaat ve onarım istihkakları için %1 alt bendi ekledi (01/06/2026'dan itibaren). Karşı taraf vekalet ücretinde tevkifatı GVK 94/1'de sayılan ödeyici yapar. Ölçüt gerçek kişi olmak değil, 94/1'de sayılmaktır: ticari veya mesleki faaliyeti olmayan ya da ödemeyi bu faaliyetiyle ilgisiz (kişisel) bir dava için yapan gerçek kişi borçlu tevkifat yapmaz; gerçek gelirini beyan eden tacir veya serbest meslek erbabı işiyle ilgili ödemede yapar (311 GVGT md.25/3; özelge 23620). Ücret haciz, mal satışı, kefil veya istinaf ve temyiz teminatından tahsil edilirse de tevkifat yapılmaz; avukat borçlu adına stopajsız SMM düzenler ve brüt tutarı beyan eder (311 GVGT md.25/6; bkz. `vekalet-ucreti.md`). Kararda "KDV hariç" yazmıyorsa ücret KDV dahildir ve tevkifat KDV hariç tutar üzerinden yapılır |
| Telif (GVK 94/2-a, GVK 18 kapsamı) | %17 | Aynı |
| İş yeri kirası (GVK 94/5-a; avukat kiracıysa ödeme sırasında keser) | %20 (2009/14592 BKK; GİB Kira Geliri Rehberi Yayın 593, Şubat 2026, s.18 aynı oranı verir. BKK metni ayrıca açılmadı) | Ev-ofiste kira gider yazılıyorsa tamamından kesilir (128 Seri No.lu GVGT; Kırşehir Def. 12/12/2022 özelgesi). Bkz. `giderler.md` |
| Mevduat ve menkul kıymet stopajı (GVK geçici 67) | 2026'da CBK 11107 (RG 27/03/2026), 11444 (RG 20/06/2026-33286) ve 11734 (RG 05/09/2026-33361) ile değişti. Güncel oranlar teyit edilmedi | Serbest meslek tevkifatını etkilemez. Avukatın faiz geliri varsa ayrıca kontrol et |
| KDV genel oranı | %20 (10/07/2023'ten itibaren; öncesi %18) | CBK 7346 (RG 07/07/2023-32241) |
| KDV indirimli oran: adli yardım; aile, tüketici ve çocuk mahkemesi davaları ve işleri; vesayet; dava şartı iş arabuluculuğu; bunlara bağlı kanun yolları ve ilamlı icra | **%10** (10/07/2023'ten itibaren). Öncesinde %8: aile, tüketici, çocuk, vesayet, dava şartı iş arabuluculuğu ve bunlara bağlı kanun yolları ile ilamlı icra için 02/10/2019'dan (CBK 1594), adli yardım ve adli müzaharet için 01/12/2021'den (CBK 4862, RG 26/11/2021-31671) 09/07/2023'e kadar (özelge 32149) | 2007/13033 BKK (II) 32; özelge 38775 (02/07/2025). Çocuk mahkemesinin görevine giren CMK işleri, soruşturma dahil, %10'dur. Diğer CMK ödemelerinde %20 lafzi yorumdur; oranı açıkça söyleyen özelge yok (teyit edilmedi). Bkz. `kdv.md` |
| KDV tevkifatı: I/C-2.1.3.2.13 listesindeki alıcılara (5018 cetvellerindeki idareler, kendi kuruluş kanunu veya CBK'si olan kamu kurumları, döner sermayeli kuruluşlar, baro gibi meslek kuruluşları, banka, sigorta, reasürans ve emeklilik şirketleri, emekli ve yardım sandıkları, kalkınma ajansları; 01/03/2024'ten itibaren KİT) yargı mercileri önündeki ve icra hizmetleri | **5/10** (I/C-2.1.3.2.13). 5018 idareleri için 2021'den önce de vardı: önce 117 Seri No.lu KDV GT 3.2.13 (özelge 30576, 21/02/2013), sonra KDV GUT (özelge 30288, 12/08/2020). Baro, banka, sigorta gibi alıcılar Seri 35 ile 01/03/2021'den, KİT'ler Seri 50 ile 01/03/2024'ten itibaren listede. Tarihçe: `kdv.md` | Karşı taraf vekalet ücreti belgelerinde de uygulanır. **Belediyenin kendisi listede yok:** belediyeye verilen hizmette (karşı taraf vekalet ücreti dahil) 5/10 yoktur; belediye GVK 94 sorumlusu olduğundan %20 stopajı yine keser (özelge 30252). Belediye birlikleri ve büyükşehir su ve kanalizasyon idareleri belirlenmiş alıcıdır; ancak 5/10 için I/C-2.1.3.2.13 listesinde olmaları gerekir. Kendi kuruluş kanunu olmayan su idaresinde dava ve icrada tevkifat yok (özelge 30251; İSKİ gibi kendi kanunu olanda var, 23533). Yargı mercileri önündeki hizmet 9/10 danışmanlık kapsamında değildir (I/C-2.1.3.2.2.2; özelge 23509) |
| KDV tevkifatı: hukuki danışmanlık, I/C-2.1.3.1/b'deki belirlenmiş alıcılara | **9/10** (I/C-2.1.3.2.2) | Avukatlık ve danışmanlık ayrı ücretlendirilmemişse toplam bedel üzerinden. Belirlenmiş alıcı olmayan özel şirkete ve belediyenin kendisine verilen danışmanlıkta tevkifat yok (özelge 30252) |
| Geçici vergi | %15 (tarifenin ilk dilim oranı). Dönem içinde tevkif edilen gelir vergisi hesaplanan geçici vergiden mahsup edilir. Tahakkuk edip ödenmemiş geçici vergi yıllık beyannamede mahsup edilemez | GVK mük. 120; Rehber s.14 |
| Vergiye uyum indirimi | Hesaplanan verginin mesleki kazanca isabet eden kısmının %5'i. Şartlar: indirim yılı ve önceki iki yılın beyannameleri süresinde verilmiş olmalı. Bu dönemde kesinleşmiş tarhiyat bulunmamalı (indirim sınırının %1'ine kadar olan hariç). Tahakkuklar ödenmiş olmalı ve 1.000 TL'yi aşan vadesi geçmiş borç bulunmamalı. İndirim yılı ve önceki 4 yılda VUK 359 fiili olmamalı | GVK mük. 121; Rehber s.15–16 |

## KDV kısmi tevkifat sınırı (I/C-2.1.3.4.1; KDV dahil, işlem bazında)
- **2014 – 30/06/2021:** 1.000 TL (KDV GUT'un ilk hâli)
- **01/07/2021 – 29/02/2024:** 2.000 TL (Seri 36 md.3, RG 03/06/2021-31500)
- **01/03/2024'ten itibaren:** işlem yılının **VUK 232 fatura sınırı** (Seri 50 md.3, RG 10/02/2024-32456)
  - 2024: 6.900 TL (VUK GT 556)
  - **2025: 9.900 TL** (VUK GT 577)
  - **2026: 12.000 TL** (VUK GT 588). Bazı kopyalarda geçen 12.900 TL yanlıştır.
- Bütünlük arz eden iş bölünemez. Aynı davanın ilam ve icra vekalet ücretleri sınır hesabında toplanır.
- Başsavcılığa kesilen arabuluculuk makbuzlarında GİB sınırı **dosya bazında** uygulamıştır (özelge 30159, Konya VDB 07/11/2023).
- "İşlemin yapıldığı yıl" ifadesinin hizmet yılını mı makbuz yılını mı kastettiği belirsizdir; GİB görüşü bulunamadı.

## Damga vergisi (beyanname başına, 01/01/2026'dan itibaren; DVK GT 71)
| Beyanname | 2026 |
|---|---|
| Yıllık gelir vergisi beyannamesi | 1.189,50 TL |
| KDV beyannamesi | 791,00 TL |
| Muhtasar beyanname | 791,00 TL |
| Geçici vergi beyannamesi ("diğer beyannameler" grubu; bu gruplama uygulama bilgisidir) | 791,00 TL |
| Muhtasar ve prim hizmet beyannamesi | 939,70 TL |

- Tutarlar 2025'e göre %18,95 artırıldı. 2026'da başka bir DVK genel tebliği çıkmadı.
- **Mart 2027'de verilecek 2026 yıllık beyannamesinde 2027 tutarları uygulanacak.** Bu tutarlar henüz yayımlanmadı.
- DVK md.14'teki kâğıt başına üst sınır 2026 için 29.115.961,10 TL'dir.

## Veraset ve intikal vergisi (2026; 57 Seri No.lu VİVK GT, RG 31/12/2025-33124, 5. Mük.)
- **İvazsız intikal istisnası (VİVK 4/d): 66.935 TL.** Bağış ve TBB munzam emeklilik yardımı gibi ivazsız iktisaplarda uygulanır (`diger.md` §1). Yarışma, çekiliş ve şans oyunu ikramiyelerinde (4/e) de 66.935 TL.
- Veraset yoluyla intikalde füruğ ve eşten her birinin miras hissesi için (4/b) 2.907.136 TL; füruğ yoksa eşe 5.817.845 TL.
- **Tarife (VİVK 16; 2026 dilimleri):** ilk 3.000.000 TL; sonraki 7.000.000 TL; sonraki 15.000.000 TL; sonraki 30.000.000 TL; 55.000.000 TL'yi aşan kısım. Oranlar veraset için %1 / 3 / 5 / 7 / 10, ivazsız intikal için %10 / 15 / 20 / 25 / 30. Ana, baba, eş ve çocuktan ivazsız intikalde ivazsız oranların yarısı uygulanır. Dilim tutarları VİVK 16'nın konsolide metninden alındı (57 Seri No.lu Tebliğin ek tablosu).

## Cezalar ve hadler (2026; VUK GT 588)
2025 tutarları yalnız belirtilen satırlarda verilmiştir (VUK GT 577).

| Kalem | 2026 |
|---|---|
| **e-SMM vermeme, almama, gerçek meblağdan farklı düzenleme, e-belge yerine kâğıt düzenleme veya hiç düzenlenmemiş sayılma (VUK 353/1)** | Her belge için meblağın veya farkın %10'u. Asgari ceza takvim yılı içindeki tespit sırasına göre artar: 1. tespitte 17.000; 2. tespitte 35.000; 3. tespitte 53.000; 4. tespitte 70.000; 5. tespitte 87.000; 6. ve sonraki tespitlerde 170.000 TL. Belge nevi başına yıllık üst sınır 17.000.000 TL. **2025 (VUK GT 577):** 14.000 / 28.000 / 43.000 / 57.000 / 70.000 / 140.000 TL; yıllık üst sınır 14.000.000 TL |
| VUK 353/1'deki 7524 s.K. kuralları (28/7/2024) | Aynı nevi birden çok belge tek tespitte bulunursa her belgeye ayrı ceza kesilir ama cetvelde bir tespit sayılır. Alıcı, idare öğrenmeden belgenin düzenlenmesi gereken süreyi izleyen 5 iş günü içinde bildirirse alıcıya ceza kesilmez, düzenleyene **3 kat** uygulanır. VUK dışı belge düzenlenirse ceza 2 kat, alıcı bildirirse 6 kat olur |
| Mükellef olmayan müvekkilin SMM almaması (VUK 353/3) | Belge başına 8.700 TL, yıllık en fazla 87.000 TL. Belgenin düzenlenmediğini 5 iş günü içinde bildirirse ceza kesilmez |
| Diğer belgeler (VUK 353/2; SMM için uygulanmaz) | Belge başına 17.000 TL; tespit başına 1.700.000, yıllık 17.000.000 TL. Bedesten'deki konsolide metnin parantezlerinde eski tutarlar (14.000 / 1.400.000 / 14.000.000) görünür; 588 listesini esas al |
| Tevsik zorunluluğuna uymama (VUK mük. 355) | İşlem tutarının %10'u; serbest meslek erbabı için asgari 35.000 TL (asgarinin mükellef sınıfına göre belirlenmesi GİB uygulamasıdır; mükellef olmayan ödeyici için 8.700 TL); yıllık üst sınır 35.000.000 TL. Ödeme yapan taraf aykırılığı 5 iş günü içinde kendiliğinden bildirirse ona ceza kesilmez |
| Tahsilatın başkalarının adı veya hesabı kullanılarak yapılması (VUK mük. 355, 7524 md.13 ile eklenen fıkra) | Her işlem için işlem tutarının %10'u. Mük. 355 tutarından (serbest meslek erbabı: 35.000 TL) az olamaz. Hizmeti yapan avukata ve adına veya hesabına ödeme yapılan kişiye ayrı ayrı kesilir. Yıllık üst sınır 35.000.000 TL |
| Kartla, karekodla veya e-cüzdanla yapılan tahsilatın kendi adına kayıtlı olmayan POS veya ödeme sistemiyle yapılması (VUK mük. 355, 7524 md.13 ile eklenen ayrı fıkra; 5464 s.K.'nın izin verdiği haller hariç) | Her işlem için mük. 355 cezasının **3 katı**: serbest meslek erbabı için 35.000 × 3 = 105.000 TL (hesap). Tahsilatı yapan avukata ve cihazı kullandırana ayrı ayrı kesilir. Yıllık üst sınır 35.000.000 TL. Tek fiil birden çok mük. 355 cezasını gerektiriyorsa yalnız en ağırı kesilir. Büroda ortak POS kullanan avukatlar için önemli |
| Tevsik haddi (459 Sıra No.lu VUK GT; 575 ile 30/11/2024'ten itibaren, öncesi 7.000 TL) | **30.000 TL** (2025 ve 2026; 575'ten sonra değişiklik yok). Aynı gün aynı kişiyle yapılan işlemler toplanır. Ücret taksitle tahsil edilse bile sözleşmenin toplam tutarı esas alınır |
| İş yeri ve konut kirası tevsiki | Tutar sınırı yok: kiraya veren ve kiracı, kira tahsilat ve ödemelerini banka veya PTT belgesiyle tevsik eder. Mahkeme ve icra yoluyla ya da ayni yapılan ödemeler kapsam dışıdır. Uymamanın cezası mük. 355'tir (yukarıda). Dayanak: 328 Seri No.lu GVGT md.2 (RG 17/10/2024-32695; 268 Seri No.lu GVGT'yi kaldırdı, konuttaki 500 TL sınırı da kalktı); Rehber 590 md.7, s.11; GİB Yayın 534 |
| I. ve II. derece usulsüzlük (serbest meslek erbabı) | 17.000 / 8.700 TL |
| Mük. 355/1: bilgi vermeme ve 86, 148, 149, 150, mük. 242, 256, 257 zorunluluklarına uymama (serbest meslek erbabı) | 35.000 TL |
| e-tebligat zorunluluğuna uymama (VUK 107/A; ceza mük. 355'e göre) | 12.000 TL |
| Doğrudan gider yazılabilecek demirbaş (VUK 313) | 12.000 TL (2025: 9.900) |
| VUK 232 fatura sınırı | 12.000 TL (2025: 9.900) |
| Uzlaşmaya konu usulsüzlük ve özel usulsüzlük cezası eşiği | 40.000 TL'nin üzeri (VUK GT 588 listesi; VUK GT 592 md.4/3, RG 28/03/2026-33207). Kapsamın tespitinde ihbarnamenin tebliğ tarihindeki tutar esas alınır. 40.000 TL ve altındaki cezalarda VUK 376 indirimi %50 artırımlı uygulanır |
| VUK 343 en az ceza haddi | Damga vergisinde 150 TL, diğer vergilerde 300 TL |

## İade (252 Seri No.lu GVGT)
| | 2025 | 2026 |
|---|---|---|
| Tevkifat nakden iadesi: inceleme raporu ve teminat aranmayan sınır (1A dilekçesi) | 340.000 | 426.000 |
| YMM tam tasdik raporuyla iade üst sınırı. Aşan kısım yalnız vergi inceleme raporuyla iade edilir; teminat verilirse inceleme beklenmeden iade yapılır | 3.400.000 | 4.266.000 |
| Tevkifatın diğer vergi borçlarına mahsuben iadesi | Tutar sınırı yok; inceleme raporu ve teminat aranmaz (1A dilekçesi; Rehber s.24–25) | Aynı |
| Geçici vergi iadesi | Tutar sınırı, teminat ve inceleme raporu yok. Yıllık beyannamenin ilgili tablosuna yazılması talep sayılır. Yazılmamışsa o yılın sonuna kadar 1B dilekçesi verilir (429 Sıra No.lu VUK GT) | Aynı. 2026 dönemleri için son gün 31/12/2027 olarak yorumlanır (orta güven) |

- Mahsup için kesintinin beyannameye dahil edilen gelire ait olması gerekir. Stopaj önce o dönemin geçici vergisinden, sonra yıllık beyannamede hesaplanan vergiden düşülür.
- Tutarlar Rehber s.26–27'den doğrulandı. 2025 hadlerinin %25,49 ile artırılıp 1.000 TL altı kesirlerin atılmasıyla bulundukları hesapla tutarlı. Hadleri yeniden değerleme oranına bağlayan 252 Seri No.lu GVGT bölümü ve GİB'in 20/01/2026 tarihli duyurusu açılamadı (teyit edilmedi).

## SGK 4/1-b (Bağ-Kur) 2026
- **Prime esas kazanç:**
  - Alt sınır günlük 1.101 TL, aylık 33.030 TL.
  - Üst sınır alt sınırın **9 katıdır** (5510 md.82; 7566 s.K. md.24 ile 7,5 kattan çıkarıldı, yürürlük 01/01/2026): günlük 9.909 TL, aylık 297.270 TL.
- **Prim oranı:** %35,75 (MYÖ %21, kısa vadeli sigorta %2,25, GSS %12,5). MYÖ oranı 7566 s.K. md.23 ile %20'den %21'e çıktı. Primini süresinde ödeyen ve borcu olmayana MYÖ priminin 5 puanı Hazinece karşılanır ve oran %30,75'e düşer (5510 md.81/1-j; isteğe bağlı sigortalı ve muhtar hariç). 7590 s.K. md.15 ayrı bir Devlet katkısı fıkrasını kaldırdı; 5 puan indirimi yürürlükte. SGK'nın 2026 oran tablosu birincil metinden görülmedi (orta güven).
  - Alt sınırda aylık 11.808,23 TL, indirimle 10.156,73 TL.
  - Üst sınırda aylık 106.274,03 TL, indirimle 91.410,53 TL.
- Bağ-Kur primi GİB'e göre gider değildir: yıllık beyannamede beyan edilen serbest meslek kazancından ayrı satırda indirilir. Kazanç primi karşılamazsa kalan kısım diğer gelirlerden düşülmez, zarar doğurmaz ve sonraki yıla devretmez. Geçici vergide kümülatif olarak düşülebilir (özelge 23610; 110 Seri No.lu GVGT). Rehber Örnek 7 "gider" ifadesini kullandığı için nitelendirme ⚖️ tartışmalıdır; GİB'in indirim yöntemini esas al (`uygulama-notlari.md` §8).
- Yalnız fiilen ödenen prim indirilir (5510 md.88). Hazinece karşılanan 5 puan indirilemez (5510 md.81/1-j). Bkz. `giderler.md`.

## Takvim
| Yükümlülük | Süre |
|---|---|
| Yıllık gelir vergisi beyanı | 1–31 Mart (2025 kazancı için 31/03/2026, bu süre uzatılmadı; 2026 kazancı için 31/03/2027) |
| Yıllık gelir vergisi ödemesi | 1. taksit 31 Mart (damga vergisiyle birlikte), 2. taksit 31 Temmuz. Hafta sonuna veya resmî tatile denk gelirse izleyen ilk iş günü (VUK 18/4). 2026 kazancı: 1. taksit 31/03/2027 Çarşamba; 2. taksit 31/07/2027 Cumartesi olduğundan **02/08/2027 Pazartesi** |
| Geçici vergi (beyan ve ödeme) | 17 Mayıs (2026'da Pazar olduğundan 18 Mayıs'a kaydı; VUK 18/4 hesabı, ayrı GİB duyurusu görülmedi), 17 Ağustos, **17/11/2026 Salı** (Ocak–Eylül dönemi; kayma yok), 17/02/2027 Çarşamba (4. dönem; kayma yok). 4. dönem 7566 s.K. md.2 ile 1/1/2025'ten itibaren başlayan dönemlerde yeniden verilir; 2025/IV'ün son günü 17/02/2026 idi. 2026 dönemleri için genel süre uzatımı bulunamadı |
| KDV beyannamesi (aylık) | İzleyen ayın 28'i (beyan ve ödeme). KDVK 41/1'in konsolide metni hâlâ "yirmidördüncü günü" der; 28'i idari düzenlemedir ve dayanağının künyesi teyit edilmedi. Süre sonu VUK-199/2026-5'teki tarihlerle tutarlı. Son gün hafta sonuna veya resmî tatile denk gelirse izleyen ilk iş günü (VUK 18/4). 2026'nın kalan dönemleri (hesap): Eylül → **28/10/2026 Çarşamba**; Ekim → 28/11/2026 Cumartesi olduğundan **30/11/2026 Pazartesi**; Kasım → **28/12/2026 Pazartesi**; Aralık → **28/01/2027 Perşembe**. 28 Ekim'de saat 13.00'ten sonrası Cumhuriyet Bayramı tatilidir (2429 s.K. md.1). Yarım günlük tatilin süreyi VUK 18/4 uyarınca kaydırıp kaydırmadığına dair GİB görüşü bulunamadı; uzatma duyurusu yoksa beyanı 28/10 öğleden önce ver |
| Muhtasar / MUHSGK (kira stopajı, personel) | İzleyen ayın 26'sı. Doğrudan teyit edilmedi; VUK-199/2026-5'teki süre sonlarıyla tutarlı. Son gün hafta sonuna veya resmî tatile denk gelirse izleyen ilk iş günü (VUK 18/4). 2026'nın kalan dönemleri (hesap): Eylül → 26/10/2026 Pazartesi; Ekim → 26/11/2026 Perşembe; Kasım → 26/12/2026 Cumartesi olduğundan **28/12/2026 Pazartesi**; Aralık → 26/01/2027 Salı |
| İşe başlama bildirimi | 10 gün (Rehber 19.1.1) |
| Defter-Beyan başvurusu | İşe başlama bildirimini izleyen 7. iş günü |
| e-SMM'ye geçiş | İşe başlanan ayı izleyen 3. ayın sonu (509 Sıra No.lu VUK GT IV.4.5) |
| Adres veya iş değişikliği ve işi bırakma bildirimi | 1 ay |
| Gider pusulası | 7 gün |
| Belge saklama | İzleyen yıldan itibaren 5 yıl |
| Tevkifat fazlası iadesi | Bildirim veya tebliğden itibaren 1 yıl (GVK 121/2) |
| Geçici vergi iadesi (beyannamede gösterilmemişse) | Beyannamenin verildiği yılın sonu (1B dilekçesi) |
| Uyum indirimi devri | Beyannamenin verilmesi gereken tarihi izleyen 1 tam yıl; bu sürede mahsup edilemeyen kısım iade edilmez |

> Kanun metinleriyle uygulama arasında farklar var:
> - GVK 92'nin konsolide metni yıllık beyan için "25 Mart" diyor; Rehber ve uygulama 31 Mart.
> - GVK mük. 120/3 geçici vergi beyanı için "14'ü", ödeme için "17'si" diyor; uygulamada beyan da 17'sinde yapılıyor.
> - İki uygulamanın da dayanak düzenlemesinin künyesi bulunamadı (teyit edilmedi). Tarihleri GİB'in "Beyanname Verme ve Ödeme Süreleri" belgesine (Ocak 2026) bağla.
>
> Son günü her yıl GİB duyurusu ve sirkülerlerinden teyit et. Uzatmalar VUK sirküleriyle yapılır:
> - **VUK-199/2026-5 (15/05/2026):** 26/05/2026'da biten muhtasar ve prim hizmet, konaklama vergisi ve damga vergisi beyannameleri 03/06/2026'ya; 01/06/2026'da biten KDV beyannameleri 05/06/2026'ya uzatıldı. Bunlar Nisan 2026 dönemine aittir.
> - **VUK-197/2026-3 (16/02/2026):** Yalnız deprem bölgesindeki mükelleflerin 2025/IV geçici vergi süresini 09/03/2026'ya uzattı.

## 2026'da yapılan ve avukatı etkileyen değişiklikler (Rehber'de yer almıyor)
- **e-tebligat:** 7587 s.K. md.9 (RG 01/07/2026-33297, yayımı tarihinde yürürlükte) ile VUK 107/A yeniden yazıldı.
  - Mesleki kazancı nedeniyle gerçek usulde vergilendirilen serbest meslek erbabı e-tebligatı kanun gereği kullanmak zorunda. Engellilik oranı %90 ve üzeri olanlar için zorunluluk yok.
  - Tebliğ, iletiyi izleyen **5. günün sonunda** yapılmış sayılır. Dava ve uzlaşma süreleri buna göre başlar.
  - Önceden sisteme dahil olanlar yeni başvuru yapmadan devam eder (geçici 38).
  - Sistemden çıkış iki yolla olur: mükellefiyetin sona erdiği tarihi izleyen 5. takvim yılı sonundan itibaren talep (başka zorunluluk sebebi yoksa) veya 65 yaşını doldurmuş olarak talep.
  - Uymama cezası mük. 355'e göre 12.000 TL'dir (2026).
  - Aynı Kanunun 10. maddesi mük. 257/1-(8)'deki "iki katına" ibaresini "beş katına" çevirdi; kapsamı teyit edilmedi.
- **Tecil:** 7582 s.K. md.1 (RG 04/06/2026-33270) ile 6183 md.48 kapsamında azami süre 36 aydan 72 aya çıktı.
  - Kanundaki teminatsız tecil sınırı 50.000 TL'den 1.000.000 TL'ye yükseldi. CBK 11414 (RG 13/06/2026-33279) bu sınırı 10.000.000 TL olarak uygular. Sınır, tahsil dairesi itibarıyla tecil edilen borçların toplamına bakar; aşan kısmın yarısı kadar teminat istenir.
  - Olağan tecil faizi 16/06/2026'dan itibaren yıllık %39'dur.
  - Düşük faizli yapılandırma (Tahsilat GT Seri B Sıra 20, RG 16/06/2026-33282; faiz %29) için başvuru süresi 31/08/2026'da sona erdi. Serbest meslek kazanç defteri tutan avukat 48 taksit grubundadır. Başvuranların taksitleri ve ihlal kuralları sürüyor.
- **Varlık barışı (KVK geçici 19; 7582 md.10):** Bildirim 31/07/2027'ye kadar yapılır.
  - Vergi %5'tir; vade ve tutma taahhüdüne göre %0–4'e iner. 01/01–31/07/2027 arasındaki bildirimlerde oran yarım puan artar.
  - Türkiye'de olup kanuni defterlerde yer almayan varlıklar defter tutan mükellefler için kapsamdadır. Mükellefiyeti olmayanlar, defter tutmayanlar ve mükellefiyetiyle ilişkilendirmeden yararlanmak isteyen gelir vergisi mükellefleri de Türkiye'de olup bankada veya aracı kurumda bulunmayan para, altın, döviz ve menkul kıymetleri bildirebilir. Şart: varlıkları bildirim tarihinde banka veya aracı kurumdaki hesaba yatırıp belgelemek (Seri No 1 Genel Tebliğ, RG 04/07/2026-33300).
  - Serbest meslek erbabı bildirilen kıymetleri defterinde ayrıca gösterir.
- **Yurt dışı kazanç istisnası (GVK mük. 20/D; 7582 md.4):** Kural 01/01/2026'dan itibaren Türkiye'de yerleşmiş sayılanların yurt dışı kazançlarına 20 yıl uygulanır. Türkiye'de verilen hizmetten doğan serbest meslek kazancı istisna dışıdır (GVGT 333 Örnek 10; avukata kıyasen). Dolayısıyla Türkiye'de verilen avukatlık hizmetinin kazancına uygulanmaz.
- **Yurt dışına verilen hizmet indirimi:** CBK 11257 (RG 30/04/2026) oranı %100'e çıkardı. Avukatlık kapsam dışıdır; bkz. yukarıdaki tablo.
- **Stopaj:** CBK 11344 (RG 19/05/2026) yalnız nükleer santral istihkaklarına %1 oran ekledi. Serbest meslek oranları (%20 / %17) değişmedi.
- **Cezalarda uzlaşma:** VUK GT 592 (RG 28/03/2026-33207) yetkili komisyonları belirledi; eşik 40.000 TL.
- **AAÜT değişiklikleri:** RG 08/01/2026-33131 ve 28/03/2026-33207. Bkz. `aaut-2025-2026.md`.
- **CMK Ücret Tarifesi 2026:** RG 08/01/2026-33131 (2025 tarifesi: RG 01/02/2025-32800). Hukuki yardımın yapıldığı tarihteki tarife uygulanır. Bkz. `ek-faaliyetler.md`.
- **Arabuluculuk ve Bilirkişilik Asgari Ücret Tarifeleri 2026:** RG 26/12/2025-33119, yürürlük 01/01/2026. Arabuluculukta anlaşma halinde ücret 9.000 TL'den az olamaz; ticari uyuşmazlık ve ortaklığın giderilmesinde alt sınır 13.000 TL'dir. Saatlik tutarlar tebliğ ekindeki tablodadır. Bkz. `ek-faaliyetler.md`.
- **7589 s.K. (yargı paketi, RG 31/07/2026-33326):**
  - HMK 362/3-b: BAM'ın istinafı kabul ederek yeniden esas hakkında verdiği karar temyiz sınırının altındaysa ve yalnız vekalet ücreti veya yargılama giderine ilişkinse temyiz edilemez.
  - İYUK 46/2-f: 46/1 kapsamı dışındaki davalarda BİM'in kaldırma üzerine yeniden verdiği kararlardan yalnız vekalet ücreti ve yargılama giderine ilişkin olanlar temyiz edilemez. Yürürlükten sonra verilen BİM kararlarına uygulanır.
  - İdare ve vergi mahkemelerinde tek hakim sınırı 486.000 TL oldu (2576 md.7). Yürürlükten sonra açılan davalara uygulanır.
  - Kanuni faiz TCMB kısa vadeli reeskont oranının %80'i oldu.
  - Vergi kanunlarını değiştiren hüküm yok.
- **Diğer 2026 kanunları:** 7573–7595 arasında serbest meslek kazancını doğrudan etkileyen başka vergi hükmü yok. 7577, GVK 41/1-12'yi (şans oyunu reklam giderleri) ve KDVK 17/4-ğ'yi ekledi.
- **Değişmeyenler:**
  - %20 serbest meslek stopajı.
  - GVK 94/3. AYM, E.2024/94, K.2025/179 (10/09/2025; RG 23/12/2025-33116) ile iptal talebini reddetti.
  - 311 GVGT md.25-26.
  - e-SMM (509 Sıra No.lu VUK GT). 589 Sıra No.lu VUK GT yalnız e-Arşiv faturayı ilgilendiriyor.
  - %5 uyum indirimi şartları.
  - GVK 69 hasılat tespiti (326 Seri No.lu GVGT).
