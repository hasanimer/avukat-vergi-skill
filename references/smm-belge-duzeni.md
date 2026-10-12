# e-SMM ve belge düzeni: akdi ücret, masraflar, tahsil zamanı

**Kapsam:** Avukatın kendi e-SMM düzeni. Akdi ücrette makbuzun zamanı, alıcısı ve tutarı; stopaj ve KDV tevkifatının makbuzda gösterimi; masraf ve gider avansı; avukatlar arası iş ve tevkil; ücret iadesi; ceza, tevsik, stopaj mahsubu ve yoklama. Kaynaklar GİB özelgeleri (yalnız talep edeni bağlar, VUK 413), kanun ve tebliğ metinleridir. Son kontrol: 12.10.2026.
**İlgili dosyalar:** `parametreler.md` (tüm tutarlar; esas alınır) · `vekalet-ucreti.md` (karşı taraf vekalet ücreti) · `kdv.md` (oran, tevkifat, CMK) · `uygulama-notlari.md` (⚖️ tartışmalı konular, KDV'nin doğması, sık hatalar) · `rehber-590-avukat.md` (GİB Rehberi özeti) · `ek-faaliyetler.md` (CMK, arabuluculuk) · `giderler.md` · `aaut-2025-2026.md` · `mukellefiyet-istisna.md` · `damga-harc.md`.
**Özelge tam metinleri:** `ozelgeler/<ID>.txt` (skill kökünden `references/ozelgeler/<ID>.txt`). Dosyanın sonundaki tabloda hangi metnin yerelde bulunduğu yazılıdır.

## Hızlı karar tablosu

| # | Soru | Kısa cevap | Dayanak |
|---|---|---|---|
| 1 | e-SMM'yi ne zaman keserim? | Ücreti tahsil ettiğin anda ve tahsil ettiğin tutar kadar. Her taksit ve avans için ayrı makbuz gerekir. Tahsilden önce kesme (CMK ve adli yardım istisnadır). Faturadaki 7 günlük süre SMM'de yoktur. | VUK 236; GVK 67; 23649, 23519, 23289 · §2 |
| 2 | İcra dairesine veya bankaya adıma yatan para ne zaman tahsil sayılır? | Haberdar olduğun (ıttıla) anda. Alacağın temliki ve takası da tahsil hükmündedir. | GVK 67 (tahsil hükmü fıkrası); Rehber s.7 · §2 |
| 3 | Akdi ücreti başkası ödüyor, makbuz kime? | Hizmeti alan müvekkile; ödeyenin adı açıklamaya yazılabilir. Temlikte de asıl borçlu müvekkildir. Karşı taraf vekalet ücreti borçluya, CMK ücreti Başsavcılığa, adli yardım ücreti baroya kesilir. | VUK 237; 26368, 25506; 311 GVGT md.26; 30273 · §3 |
| 4 | Stopaj kesilir mi? | Ödeyen GVK 94/1'de sayılıyorsa (şirket, kamu idaresi, dernek, vakıf, serbest meslek erbabı, defter tutan tacir vb.) avans dahil %20. GVK 94/1'de sayılmayan gerçek kişiden veya tacirin kişisel davasından alınan ücrette stopaj yoktur; ücret brüt beyan edilir. | GVK 94/1-2-b; 2009/14592 BKK; 23620 · §3 |
| 5 | KDV tevkifatı ne zaman uygulanır? | Alıcı tebliğdeki listedeyse ve KDV dahil bedel 12.000 TL'yi (2026; 2025'te 9.900 TL) aşarsa. Danışmanlıkta 9/10 ve geniş liste; dava ve icra hizmetinde 5/10 ve dar "diğer hizmetler" listesi. Bedel bölünemez. | KDV GUT I/C-2.1.3.2.2, 2.1.3.2.13, 2.1.3.4.1 · §9 |
| 6 | Harç, icra, tebligat ve bilirkişi avansı için makbuz keser miyim? | Aynen harcanıp yansıtılıyorsa hayır: makbuz yok, KDV yok, gider de yok. Harcanmayan bakiye hasılattır. Masrafa eklenen bedel ile yol ve konaklama karşılığı hasılattır: e-SMM, stopaj ve KDV gerekir. | GVK 67/2, 67/4; 21255, 23601, 23644 · §5 |
| 7 | Ücreti tahsil edemedim | Gelir vergisinde makbuz yok, hasılat yok. KDV ise hizmetin tamamlanmasıyla (kesinleşme) doğar; tahsilata bağlı değildir. | 23601, 26026, 23649; KDVK 10 · §2; `uygulama-notlari.md` §3 |
| 8 | Aldığım ücreti iade ettim | Sözleşme şartına dayanan ve belgelenen iade, stopaj dahil tutar üzerinden GVK 68'e göre gider yazılır. Beyan edilmiş KDV, GİB'e göre düzeltilemez (⚖️ tartışmalı). İstisna: bozma kararıyla iade edilen karşı taraf vekalet ücretinde KDVK 35 düzeltmesi yapılır. | 23649; 23574; 29150 · §7 |
| 9 | Makbuzu hiç kesmezsem veya geç kesersem ne olur? | Belge başına tutarın %10'u özel usulsüzlük cezası; 2026'da ilk tespitte en az 17.000 TL. Alıcı 5 iş günü içinde bildirirse senin cezan 3 kat olur. | VUK 353/1 (7524 s.K.); VUK GT 588 · §10 |
| 10 | Ücreti nakit alabilir miyim? | 30.000 TL'yi aşan tahsilat banka, ödeme kuruluşu veya PTT üzerinden yapılmalıdır. Taksitli ödemede sözleşmenin toplam tutarına bakılır. Gerçek kişi müvekkil de buna tabidir. | VUK mük. 257; 459, 572 ve 575 Sıra No.lu VUK GT · §11 |

## Okuma notu
- Bu dosya, avukatın müvekkille yaptığı sözleşmeye dayanan (akdi) ücrete ve genel belge düzenine ilişkin GİB özelgelerini uygulanabilir kurallara çevirir.
- Özelgeler VUK 413 uyarınca yalnız talep edeni ve onun anlattığı somut olayı bağlar. Burada GİB'in yerleşik görüşünü göstermek için kullanılırlar; benzer bir olayda bağlayıcı sayılmamalıdır.
- 2020 öncesi özelgelerde geçen "serbest meslek makbuzu" bugün e-SMM'dir.
- Bu özelgelerdeki %18 KDV oranı 10.07.2023'ten itibaren %20, %8 oranı ise %10'dur. Özelgelerdeki eski tutarların güncel karşılığı `parametreler.md` dosyasındadır.
- KDV GUT bölüm numaraları, VUK 353 metni ve GVK 67'nin fıkra yapısı 12.10.2026'da birincil kaynaktan kontrol edildi.
- Tartışmalı konularda önce GİB görüşü verilir; diğer görüş "⚖️ tartışmalı" diye işaretlenir ve `uygulama-notlari.md` dosyasına atıf yapılır.
- Diğer konular için: karşı taraf vekalet ücretinin stopaj ayrıntısı `vekalet-ucreti.md`, KDV oranı ve tevkifat ayrıntısı `kdv.md`, gider indirimi `giderler.md`, yıllık tutarlar `parametreler.md`.

## Güncel çerçeve (Ekim 2026)

| Konu | Kural | Dayanak |
|---|---|---|
| Belge | Her mesleki tahsilat için e-SMM düzenlenir. 01.02.2020'de faaliyette olanlar için 01.06.2020'den, sonra işe başlayanlar için başladıkları ayı izleyen 3. ayın sonundan itibaren zorunludur. 01.02–12.10.2026 arasında 509 Sıra No.lu Tebliğde e-SMM'yi etkileyen değişiklik yapılmadı. | VUK 236; 509 Sıra No.lu VUK GT (RG 19.10.2019, 30923) IV.4.4–IV.4.5; Rehber s.7–8 |
| GV stopajı | GVK 94/1'de sayılan müvekkil, avans ödemeler dahil %20 keser. Oran 2025 ve 2026'da %20'dir; CBK 11344 (RG 19.05.2026) bu oranı değiştirmedi. Telif kazancında oran %17'dir (GVK 94/2-a). GVK 94/1'de sayılmayan gerçek kişiden yapılan tahsilatta stopaj yoktur. Tacir veya serbest meslek erbabı müvekkilin ticari ya da mesleki faaliyetiyle ilgisi olmayan kişisel davası için yaptığı ödemede de stopaj yoktur. | GVK 94/1-2-b; 2009/14592 BKK; özelge 23620; Rehber s.10–11 |
| KDV | Genel oran 10.07.2023'ten itibaren %20, öncesinde %18. %10 oranı (öncesinde %8) şu avukatlık hizmetlerine uygulanır: aile, tüketici ve çocuk mahkemelerinin görev alanındaki dava ve işler; vesayet işleri; bunların kanun yolları; iş uyuşmazlıklarında dava şartı arabuluculuk; bunlara bağlı ilamlı icra takipleri (02.10.2019'dan). Adli yardım ve adli müzaharet kapsamındaki hizmetler de bu orana tabidir (01.12.2021'den). Ayrıntı `kdv.md`; ⚖️ tartışmalı sınırlar `uygulama-notlari.md` §4. | KDVK 28; 2007/13033 BKK (II) sayılı liste 32. sıra; CBK 1594 (02.10.2019'dan), CBK 4862 (RG 26.11.2021, 31671), CBK 7346 (RG 07.07.2023, 32241); özelgeler 38775, 32149 |
| KDV tevkifatı oranı | Hukuki danışmanlık belirlenmiş alıcıya verilirse 9/10 tevkifat uygulanır. Yargı mercileri önündeki hizmetler ile yargı kararlarının sonuçlarıyla ilgili hizmetler (icra vb.) 01.03.2021'den itibaren "diğer hizmetler" alıcılarına verildiğinde 5/10 tevkifata tabidir. Avukatlık ve danışmanlık aynı sözleşmede ayrı ücretlendirilmemişse toplam bedel üzerinden 9/10 uygulanır. | KDV GUT I/C-2.1.3.2.2.1–2.1.3.2.2.2, I/C-2.1.3.2.13; Seri 35, 38, 50 |
| KDV tevkifatı sınırı (KDV dahil, işlem veya dosya bazında) | 30.06.2021'e kadar 1.000 TL; 01.07.2021–29.02.2024 arası 2.000 TL; 01.03.2024'ten itibaren işlemin yapıldığı yılın VUK 232 fatura sınırı (2024: 6.900 TL, **2025: 9.900 TL, 2026: 12.000 TL**). Sınır aşılırsa tevkifat tutarın tamamına uygulanır. Tevkifattan kaçınmak için bedel bölünemez. | KDV GUT I/C-2.1.3.4.1; Seri 36 ve 50 (RG 10.02.2024, 32456); VUK GT 556, 577, 588; özelgeler 30151, 38981 |
| Defter | Serbest meslek kazanç defteri tutulur ve Defter-Beyan Sistemi zorunludur. Defter ve belgeler 5 yıl saklanır. | VUK 210, 253; GVK 67/5; GİB Rehberi Yayın 590 (Şubat 2026) s. 30–31 |
| Tevsik | 30.000 TL'yi aşan tahsilat ve ödemeler banka, ödeme kuruluşu veya PTT üzerinden yapılır ve bu kurumların belgeleriyle tevsik edilir. Mükellef olmayan gerçek kişi müvekkillerle yapılan işlemler de buna dahildir. Taksitli tahsilatta sözleşmenin toplam tutarı esas alınır. Bu kural e-SMM yükümlülüğünü kaldırmaz. Ayrıntı §11. | VUK mük. 257; 459, 572 ve 575 Sıra No.lu VUK GT; GİB Rehberi Yayın 590 s. 34 |
| Ceza | e-SMM hiç düzenlenmezse, gerçek tutardan farklı düzenlenirse veya kâğıt olarak düzenlenirse belge başına tutarın %10'u kadar özel usulsüzlük cezası kesilir. 2026'da ilk tespitte asgari ceza 17.000 TL, yıllık üst sınır 17.000.000 TL'dir. | VUK 353/1 (7524 sayılı Kanunla değişik); VUK GT 588 |
| Stopaj mahsubu ve iade | Kesilen stopaj önce geçici vergiden, sonra yıllık beyanda hesaplanan vergiden mahsup edilir. Kalanı mahsuben (sınırsız) veya nakden iade edilir; nakden iadede raporsuz ve teminatsız sınır 2025 için 340.000 TL, 2026 için 426.000 TL'dir. Ayrıntı §11. | GVK 94, 121; 252 Seri No.lu GVGT; Rehber s.24–29 |
| Yoklama | 01.01.2025'ten itibaren yoklamayla tespit edilen hasılat ile beyan edilen gayrisafi hasılat arasındaki fark %20'yi aşarsa mükellef izaha davet edilir. Ayrıntı §11. | GVK 69 (7524 s.K.); 326 Seri No.lu GVGT |

> 2026 değişiklik kontrolü: Bedesten'deki konsolide GVK 67 ve 94 metinlerinde (kayıt 01.07.2026) 2026'ya ait değişiklik notu yok. 31.12.2025 tarihli KDV GUT Seri 56 yalnız III/B-3'teki 2026 tutarını (164.000 TL) ekler; avukatlık tevkifatıyla ilgisi yoktur. KDVK'yı değiştiren 7577 sayılı Kanunun kapsamı incelenmedi; KDVK 27 bundan etkilenmemiştir. [Kaynak: araştırma notu, 12.10.2026; CBK 11344, RG 19.05.2026, 33258]

## 1. e-SMM: zorunluluk, içerik, imza, ÖKC ve POS

- **e-SMM zorunlu, e-Fatura değil.**
  - Avukat mesleki faaliyetine ilişkin her tahsilat için e-SMM düzenler.
  - e-SMM yeni bir belge türü değildir; kâğıt SMM ile aynı hukuki niteliktedir (509 Sıra No.lu VUK GT IV.4.1). Bu yüzden VUK 236–237 ve 311 Seri No.lu GVGT'deki bütün SMM kuralları e-SMM için de geçerlidir.
  - Serbest meslek faaliyeti nedeniyle e-Fatura uygulamasına geçme zorunluluğu yoktur.
  - Avukata kesilen faturalar satıcının durumuna göre e-Arşiv veya kâğıt olur.

  [Özelge: 27.06.2025, E-11395140-105[VUK-3-4253]-798105 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/38672] [Özelge: 20.11.2020, 11395140-105[VUK-1-22499]-864517 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26369]
- **2025–2026 tebliğ değişiklikleri e-SMM'yi etkilemedi.**
  - 589 Sıra No.lu VUK GT (RG 31.12.2025, 33124 5. Mük.) yalnız 509 Sıra No.lu Tebliğ IV.2.4.3'teki e-Arşiv zorunluluğunu basit usul ve işletme esası mükellefleri için 01.01.2027'ye erteler.
  - 01.02–12.10.2026 arasında yayımlanan VUK genel tebliğleri de e-SMM'yi etkilemez: 591 (taksi mali cihazı), 592 (uzlaşma), 594 (531 değişikliği, teminat), 595 (538 değişikliği, e-ticaret ve ilan bildirimi).

  [Kaynak: 589 Sıra No.lu VUK GT; RG başlık araması 01.12.2025–12.10.2026: VUK GT 591 (RG 13.02.2026, 33167), 592 (RG 28.03.2026, 33207), 594 (RG 31.07.2026, 33326), 595 (RG 05.09.2026, 33361); güven orta]
- **Zorunlu içerik (VUK 237).**
  - Makbuzda şunlar bulunur: düzenleyenin adı veya unvanı, adresi, vergi dairesi ve numarası; müşterinin adı veya unvanı ve adresi; alınan paranın miktarı; paranın alındığı tarih.
  - Makbuz imzalanır ve seri-sıra numarasıyla teselsül ettirilir.
  - Ödemeyi müvekkilden başka biri yapıyorsa, zorunlu bilgilerin okunmasını engellemeden ödeyenin bilgileri de yazılabilir.
  - Açıklama alanına icra dosya numarası veya mahkeme esas numarası ile "karşı taraf vekalet ücreti" ya da "X tarafından ödenmiştir" gibi ifadeler yazılabilir.

  [Özelge: 27.06.2025, E-11395140-105[VUK-3-4253]-798105 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/38672] [Özelge: 12.10.2015, 11395140-105[236-2014/VUK-1-18834]-86114 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/25506] [Kaynak: VUK 237]
- **İmza ve teslim.**
  - e-SMM elektronik sertifikayla imzalanır.
  - Muhatap isterse ıslak imzalı kâğıt çıktısı verilir, istemezse elektronik ortamda iletilir. Örneğin icra dosyasında borçluya elektronik iletim yeterlidir; çıktı istenirse imzalı verilir.
  - Islak imza yerine notere tasdik ettirilmiş hazır imza kullanılabilir.
  - Düzenleyen e-SMM'yi elektronik ortamda saklar ve ibraz eder. Alıcı, teslim yöntemine göre kâğıt çıktıyı veya elektronik hâlini saklar.
  - Format ve raporlama süreleri ebelge.gib.gov.tr'deki teknik kılavuzlara bırakılmıştır (509 Sıra No.lu VUK GT V.5.4).

  [Özelge: 20.11.2020, 11395140-105[VUK-1-22499]-864517 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26369]
  - *Eski görüş:* 2017 tarihli özelge hazır imzayı, matbaada basılan kâğıt makbuz için kabul etmişti. Aynı özelgeye göre imzası basılan avukat ortaklıktan ayrılırsa bu makbuzlar artık kullanılamaz. Kâğıt makbuz kısmı e-SMM ile geçerliliğini yitirdi. Ayrılan ortağın hazır imzasının kullanılmaması ilkesine ise ihtiyaten uyulmalıdır. [Özelge: 07.08.2017, 11395140-105[VUK-1-20574]-237669 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26375]
- **ÖKC ve POS.**
  - Avukatın ÖKC kullanma zorunluluğu yoktur ve ÖKC fişi SMM yerine geçmez. Avukatların ÖKC muafiyeti 2001/1 Seri No.lu İç Genelge'ye dayanır.
  - YN ÖKC'den e-SMM bilgi fişi verilse bile e-SMM ayrıca düzenlenip elektronik ortamda saklanır.
  - POS fişinin SMM sayılması 379 Sıra No.lu VUK GT ile yalnız hekimlere (diş hekimi ve veteriner hekim dahil) tanınmıştır.
  - POS ile tahsilat yapan avukat, ücrete isabet eden kısım için e-SMM düzenler.

  [Özelge: 20.11.2020, 11395140-105[VUK-1-22499]-864517 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26369] [Özelge: 05.10.2018, 36486581-120[38404182718]-E.38199 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26374] [Özelge: 30.09.2013 (izahat), 12436462-195.01[171]-95500 — https://gib.gov.tr/mevzuat/kanun/443/ozelge/38226]
  - *Dikkat:* 2014 tarihli veteriner özelgesindeki "POS fişleri SMM sayılır" ifadesi 379 Sıra No.lu VUK GT kapsamındaki hekimlere özgüdür ve avukatlara hiçbir zaman uygulanmamıştır. e-SMM döneminde hekimler için de EFT-POS özellikli YN ÖKC'den verilen e-SMM bilgi fişi düzeni geçerlidir (509 Sıra No.lu VUK GT V.5.4). [Özelge: 17.07.2014, 65771276-105[MÜK257-2013/9]-15 — https://gib.gov.tr/mevzuat/kanun/443/ozelge/26384]
- **Defter.** Serbest meslek kazanç defterinin hasılat tarafına ücretin alındığı tarih, tutarı ve kimden alındığı yazılır (VUK 210). Defter-Beyan Sistemi zorunludur; e-SMM, hasılat ve gider kayıtları bu sistemde tutulabilir. [Özelge: 05.10.2018, 36486581-120[38404182718]-E.38199 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26374] [Özelge: 23.08.2013, 11395140-019.01-1319 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/22146] [Kaynak: VUK 210; GVK 67/5; GİB Rehberi Yayın 590, s. 30–31]

## 2. Ne zaman düzenlenir? Tahsil esası

- **Tahsil esası (GVK 67/1).** Serbest meslek kazancı, dönem içinde tahsil edilen para, ayın ve para ile temsil edilebilen menfaatlerden aynı dönemde yapılan giderlerin düşülmesiyle bulunur. Hasılat, makbuzun tarihine göre değil, tahsilatın veya tahsil hükmündeki olayın tarihine göre döneme yazılır. [Kaynak: GVK 67/1; GİB Rehberi Yayın 590 s. 6–7]
- **Kural.**
  - e-SMM, ücretin tahsil edildiği anda ve tahsil edilen tutar kadar düzenlenir.
  - Kısım kısım tahsilde her tahsilat için ayrı makbuz düzenlenir. Sözleşme bedelinin tamamı için peşin makbuz düzenlenmez; her peşinat ve taksit ayrı makbuza konu olur.
  - Bu kural ilamla hükmedilen ve icra yoluyla tahsil edilen ücretler için de geçerlidir.
  - Stopaj da tahsil edilen tutar üzerinden yapılır; GVK 94 avans olarak yapılan ödemeleri de kapsar.
  - Faturadaki 7 günlük düzenleme süresi (VUK 231/5) SMM için öngörülmemiştir; esas olan tahsil anıdır.

  [Özelge: 07.07.2023, 62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519] [Özelge: 17.06.2022, 62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Özelge: 17.02.2021, 27575268-105[236-2018-593]-58403 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26368] [Özelge: 29.03.2017, 11395140-105[VUK-1-19829]-87103 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/23649]
  - ⚖️ *Tartışmalı (zamanlama):* İdare makbuzun tahsilatın yapıldığı gün düzenlenmesini bekler ve sonraki günlere bırakılan makbuz için VUK 353 cezası kesebilir. Eğitimciye göre kanundaki "düzenlenmemiş sayılma" hali yalnız fatura ve gider pusulası içindir. GİB görüşüne uy: makbuzu tahsilat günü düzenle. Bkz. `uygulama-notlari.md` §5.
- **Tahsil edilmeyen ücret.** Tahsil edilmeyen ücret için SMM düzenlenmez ve hasılat yazılmaz. [Özelge: 11.10.2013, 49327596-120[65.GVK.2013.29]-259 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23601] [Özelge: 16.09.2011, B.07.1.GİB.4.06.18.02-32229--8126-740 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26026]
- **Tahsil hükmündeki haller (GVK 67).** Şu durumlar tahsil sayılır ve bu anlarda e-SMM düzenlenmelidir:
  - avukatın haberdar olması (ıttıla) şartıyla adına icra dairesine, bankaya, kamu müessesesine, notere veya postaya para yatırılması;
  - ücret alacağının başkasına temliki (temlikin ivazlı olup olmadığına bakılmaz, ivazın tahsili aranmaz);
  - ücret alacağının müvekkile olan borçla takası.

  Ittıla anının (UYAP bildirimi, reddiyat vb.) nasıl tespit edileceğine ilişkin bir özelge bulunamadı. Uygulamacı görüşüne göre para, avukatın UYAP'ta gördüğü gün tahsil edilmiş sayılır ve reddiyat beklenmez; ihtiyatlı yol budur (`uygulama-notlari.md` §5). [Özelge: 12.10.2015, 11395140-105[236-2014/VUK-1-18834]-86114 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/25506] [Kaynak: GVK 67 (tahsil hükmü fıkrası); GİB Rehberi Yayın 590 s. 7]
- **Tahsilden önce düzenlenen makbuzun riski.**
  - 23289'da GİB, tevkifat sorumlusu müvekkilin makbuz tutarının tamamı üzerinden %20 stopaj yapmasını istemiştir. Gerekçesi GVK 96'daki "hesaben ödeme" kavramıdır: ödeyeni borçlu gösteren her kayıt ödeme sayılır.
  - Vekalet ilişkisi sonradan biter ve alınmayan kısım için iade belgesi düzenlenirse, o kısma ait stopaj yersiz ödenmiş vergi sayılmaz. Bu stopaj 252 Seri No.lu GVGT çerçevesinde yıllık beyanname üzerinden mahsup edilebilir.
  - Özelge, avukatın tahsil etmediği kısmın hasılat sayılıp sayılmayacağını ele almaz.
  - Makbuz kesilip KDV beyan edildikten sonra ücret tahsil edilemezse KDV düzeltilemez (23574).
  - Pratik sonuç: e-SMM'yi tahsilden önce düzenlemeyin.
  - İstisna: CMK ve adli yardımda makbuz, Yönetmelik md. 11 gereği ödemeden önce verilir (§3 CMK; `uygulama-notlari.md` §5). Bu durumda kazanç, paranın hesaba geçtiği yılın kazancıdır ve stopaj o yılın beyannamesinde mahsup edilir (23700).

  [Özelge: 29.08.2012, B.07.1.GİB.4.34.19.02-019.01-2703 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23289] [Özelge: 21.02.2012, B.07.1.GİB.4.35.17.01-35-02-208 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23574] [Özelge: 11.03.2013, 97677631-041-2-7 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23700]
- **KDV'nin zamanı tahsilden bağımsızdır.**
  - Sözleşmede aksi yoksa KDV'de vergiyi doğuran olay hükmün kesinleştiği tarihte gerçekleşir.
  - Ayrı ücrete tabi işlerde olay hizmetin verildiği dönemde gerçekleşir.
  - Makbuz düzenlenmesi gerektiği hâlde düzenlenmediyse, düzenlenmesi gereken tarih esas alınır.
  - Makbuz hizmetten önce düzenlendiyse (peşin ücret, avans) olay, belgedeki tutarla sınırlı olarak belge tarihinde gerçekleşir ve KDV o dönemde beyan edilir (KDVK 10/b).
  - Beyan edilen KDV, ücret sonradan tahsil edilemese ya da iade edilse de düzeltilemez (bozma kararıyla iade istisnası için §7).
  - Müvekkil banka takip dosyalarını varlık şirketine temlik eder ve avukatın dosyayla ilişiği kesilirse, bankaya verilen hizmet temlik tarihinde tamamlanmış sayılır. KDV bu tarihte, AAÜT'ün altında olmamak üzere hizmet bedeli üzerinden hesaplanıp beyan edilir. Vekalet ücreti alacağı için e-SMM ve stopaj ise tahsil tarihinde ve tahsil edilen tutarın tamamı üzerinden yapılır. Tek ve 2012 tarihli özelgedir. [Özelge: 10.08.2012, B.07.1.GİB.4.35.16.01-176200-743 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23614]
  - Tahsilatsız kesinleşen iş ve ücretsiz iş için uygulamadaki "bedeli tahsil edilmemiştir" makbuzu: `uygulama-notlari.md` §3.

  [Özelge: 29.03.2017, 11395140-105[VUK-1-19829]-87103 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/23649] [Özelge: 21.02.2012, B.07.1.GİB.4.35.17.01-35-02-208 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23574] [Kaynak: KDVK 10/a-b-c, 27/5]
- **Faaliyet terk edildikten sonraki tahsilat.**
  - Mükellefiyet döneminde verilen hizmetin bedeli terkten sonra tahsil edilirse GVK 82/1-5 kapsamında arızi kazançtır.
  - Bu bent için istisna yoktur. GVK 82'deki arızi kazanç istisnası (2026: 350.000 TL, 2025: 280.000 TL; özelgede geçen tutar 43.000 TL) bu kazanca uygulanmaz.
  - Mükellefiyet kapandığından SMM düzenlenemez. Ödeyen tevkifat sorumlusuysa %20 stopaj yapar.
  - Ücretli avukatlıktan ayrıldıktan sonra tahsil edilen baro görev ücretleri (zorunlu müdafilik, adli yardım) de arızi serbest meslek kazancı sayılmıştır: SMM zorunluluğu yoktur, %20 stopaj yapılır. Bu özelge 82/1-5'i anar, ancak istisnanın uygulanıp uygulanmayacağını tartışmaz.
  - Her iki özelge, 221 Seri No.lu GVGT'ye dayanarak arızi serbest meslek faaliyetinde KDV, geçici vergi, defter ve makbuz yükümlülüğü bulunmadığını aktarır.
  - *Gerilim:* KDV'de vergiyi doğuran olay hizmetin verildiği, yani mükellefiyetin sürdüğü dönemde doğmuş olabilir (23649). Özelgeler bu noktayı tartışmaz.

  [Özelge: 20.05.2022, E-50426076-120[65-2021/20-822]-66280 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23169] [Özelge: 20.04.2020, 84098128-120[65-2019/5]-134497 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23551] [Kaynak: GVK 82; tutarlar `parametreler.md`]

## 3. Kime düzenlenir?

- **Genel ilke: hizmeti alan.** e-SMM, ödemeyi kim yaparsa yapsın, hizmeti alan müvekkil adına düzenlenir. Örneğin ödemeyi yurt dışındaki merkez yapsa da hizmet Türkiye şubesine verildiyse makbuz şube adına düzenlenir ve %20 stopajı şube yapar. [Özelge: 17.02.2021, 27575268-105[236-2018-593]-58403 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26368] [Özelge: 29.03.2017, 11395140-105[VUK-1-19829]-87103 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/23649]
- **Stopaj yapan müvekkiller (GVK 94/1).**
  - Avukata ödedikleri ücretten avans dahil %20 keserler: kamu idare ve müesseseleri, iktisadi kamu müesseseleri, sair kurumlar, ticaret şirketleri, iş ortaklıkları, dernek ve vakıflar ile bunların iktisadi işletmeleri, kooperatifler, gerçek gelirini beyan eden ticaret ve serbest meslek erbabı, bilanço veya zirai işletme hesabı esasına göre çiftçiler.
  - Stopaj e-SMM'de gösterilir.
  - Genç girişimci istisnası (GVK mük. 20; 2026: 400.000 TL, 2025: 330.000 TL) stopajı ortadan kaldırmaz; ödeyen kesmeye devam eder (Rehber s.14; `uygulama-notlari.md` §9).

  [Kaynak: GVK 94/1-2-b; 2009/14592 BKK; GİB Rehberi Yayın 590 s. 10–11, 14]
- **Alacağın temliki.** Ücret alacağını temlik alan üçüncü kişi ödese bile e-SMM asıl borçlu olan müvekkil adına düzenlenir ve stopajı müvekkil yapar. Temlik, müvekkilin vergisel sorumluluğunu sona erdirmez. Ödeyenin bilgisi makbuza ek olarak yazılabilir. Tek ve 2015 tarihli bir özelgedir. [Özelge: 12.10.2015, 11395140-105[236-2014/VUK-1-18834]-86114 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/25506]
- **Akdi ücretin icra dosyasından düşülerek alınması.**
  - Sözleşme gereği, müvekkil adına icra dosyasından tahsil edilen paradan kesilen ücret akdi ücrettir. 7194 sayılı Kanunla eklenen GVK 94/3 kapsamındaki karşı taraf vekalet ücreti değildir.
  - e-SMM, mahsubun yapıldığı anda davayı kazanan müvekkil adına düzenlenir.
  - Müvekkil gayri faal veya re'sen terk ettirilmişse ve ortaklarına ulaşılamıyorsa stopaj yapılamaz. Bu durumda brüt hasılat, tahsil dönemine ait yıllık beyannameye dahil edilir.

  [Özelge: 03.11.2016, 62030549-120[94-2015/286]-193057 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23575]
- **Karşı taraf vekalet ücreti (özet; ayrıntı `vekalet-ucreti.md`).**
  - Kararla karşı tarafa yükletilen vekalet ücreti avukata aittir; iş sahibinin borcu nedeniyle takas ve mahsup edilemez, haczedilemez (Av.K. 164). Bu yüzden müvekkilin değil, avukatın hasılatıdır.
  - Borçlu ücreti doğrudan veya icra müdürlüğü aracılığıyla öderse e-SMM borçlu (davayı kaybeden) adına düzenlenir ve stopaj makbuzda gösterilir. İcra müdürlüğüne nüsha verilmez.
  - Ücret borçlu adına üçüncü kişilerce icra dairesine yatırılsa da tevkifat sorumlusu borçludur.
  - Ücret önce davayı kazanan müvekkile ödenir, müvekkil de avukata öderse stopajı müvekkil yapar ve e-SMM müvekkil adına düzenlenir. Müvekkilin borçluya düzenleyeceği fatura için §12.
  - Ücretli çalışan avukatın işverenine yapılan vekalet ücreti ödemesinden tevkifat yapılmaz; işveren avukata öderken ücret hükümlerine göre keser ve ödeme bordroyla belgelenir (311 Seri No.lu GVGT md. 25/2-c, 25/4, 26/4–26/6). 2016 tarihli 23579 bu düzenlemeden önce verilmiştir; çeliştiği yerde 311 Seri No.lu GVGT'yi esas alın.
  - Borçlu GVK 94/1'de sayılmıyorsa stopaj yapılmaz; avukat ücreti brüt olarak beyan eder (311 Seri No.lu GVGT md. 25/3).
  - Haciz, kefil ya da teminat yoluyla tahsilde borçlu stopaj yapmaz. e-SMM yine borçlu adına düzenlenir ve ücret brüt olarak beyan edilir.
  - Sorumlu stopaj yapmazsa sorumlu adına tarhiyat yapılır. Avukat brüt tutarı kazancına katar ve mahsup edeceği vergi olmaz. ⚖️ Kesilmeyen stopajın makbuzda gösterilip gösterilmeyeceği tartışmalıdır; hangisi seçilirse seçilsin stopajı mahsup etme (`uygulama-notlari.md` §14, 5a).
  - Borçlu belirlenmiş alıcıysa ve KDV dahil tutar sınırı aşıyorsa KDV tevkifatı uygulanır; aynı davanın ilam ve icra vekalet ücretleri sınır hesabında toplanır. ⚖️ "Yargılama gideridir, tevkifat yapılmaz" görüşü GİB özelgeleriyle çelişir (`kdv.md` §9; `uygulama-notlari.md` §14, 17).

  [Özelge: 31.07.2024, E-62030549-120-1020639 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511] [Özelge: 07.07.2023, 62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519] [Özelge: 29.08.2022, 48816587-120[2019]-60836 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23697] [Özelge: 20.04.2012, B.07.1.GİB.4.38.15.01-GV-20-485-57 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617] [Özelge: 26.05.2016, B.07.1.GİB.4.35.16.01-120.04.06[94-2016/2]-296 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23579] [Özelge: 06.06.2022, 36062021-130[09-2021/ÖZE-40]-50290 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232] [Özelge: 09.06.2022, 64597866-130-9597 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30226] [Kaynak: Av.K. 164; 311 Seri No.lu GVGT md. 25–26]
  - *Eskimiş:* 2012 tarihli özelge, 375 Sıra No.lu VUK GT'ye dayanarak makbuzun bir nüshasının ödemeyi yapan icra memuruna verileceğini söylüyordu. 311 Seri No.lu GVGT md. 26/3 (RG 27.05.2020) ile buna gerek kalmadı. [Özelge: 20.04.2012, B.07.1.GİB.4.38.15.01-GV-20-485-57 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617]
- **Ücretin bir kısmının sözleşmeyle müvekkile bırakılması (ör. protokollü banka).**
  - Hükmedilen ücretin tamamı avukatın hasılatıdır ve e-SMM tamamı üzerinden ödeyen adına düzenlenir.
  - Bırakılan kısım ancak müvekkilin VUK'a uygun olarak düzenlediği bir belgeyle GVK 68/1 uyarınca gider yazılabilir.
  - Vergi sorumluluğuna ilişkin özel sözleşmeler idareyi bağlamaz (VUK 8/3).
  - Özelge eskidir ancak dayandığı hükümler değişmedi.

  [Özelge: 09.02.2011, B.07.1.GİB.4.06.16.01-2010-GVK-65-9-67 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23660]
- **Tevkifat sorumlusu olmayan müvekkil.**
  - GVK 94/1'de sayılmayan gerçek kişi müvekkilden yapılan tahsilatta stopaj yapılmaz.
  - Müvekkil tacir veya serbest meslek erbabı olsa bile, ticari ya da mesleki faaliyetiyle ilgisi olmayan kişisel davası için yaptığı ödemede de stopaj yapılmaz. Somut olay, emekli maaşından kesilen SGDP'nin iadesi davasıdır. Dayanak, GVK 94'teki tevkifatın ticari, mesleki ve zirai işlerle ilgili ödemelere münhasır olduğu hükmüdür.
  - Her iki durumda da e-SMM KDV hesaplanarak müvekkil adına düzenlenir ve ücret brüt olarak beyan edilir.
  - Teknoloji geliştirme bölgesindeki şirketler gibi kazanç istisnasından yararlananlar ise avukata yaptıkları ödemeden genel hükümlere göre %20 stopaj keser.

  [Özelge: 28.02.2012, B.07.1.GİB.4.41.15.01-GVK-2011/24-49 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23620] [Özelge: 20.04.2012, B.07.1.GİB.4.38.15.01-GV-20-485-57 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617] [Özelge: 01.03.2012, B.07.1.GİB.4.34.16.01-KVK 6-809 — https://gib.gov.tr/mevzuat/kanun/435/ozelge/27919]
- **Aynı borçludan birden çok dosya için toplu ödeme.**
  - Dosya numarasına göre tutarlar ayrı gösterilerek tek e-SMM düzenlenebilir (23617).
  - Birbirinden bağımsız dosyalarda KDV tevkifatı sınırı her dosya için ayrı uygulanmıştır, ödeme toplu yapılsa bile. 30159'un olayında her dosya için ayrı makbuz düzenlenmişti.
  - Bütünlük arz eden tek bir işin bedeli ise bölünemez (KDV GUT I/C-2.1.3.4.1).
  - Birden çok dosya tek makbuzda gösterildiğinde sınırın dosya başına mı yoksa makbuz toplamına mı uygulanacağına ilişkin özelge bulunamadı. Bkz. §9.

  [Özelge: 07.11.2023, E-37009108-130[467770]-182439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30159] [Özelge: 20.04.2012, B.07.1.GİB.4.38.15.01-GV-20-485-57 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617]
- **CMK ve adli yardım.**
  - **Kime düzenlenir:**
    - CMK ücreti için e-SMM, ödemeyi yapan Cumhuriyet Başsavcılığı adına düzenlenir. Adli yardım ücreti için makbuz baro adına düzenlenir.
    - Makbuz baroya verilir. Başsavcılık, ödeme emri belgesiyle makbuzu düzenleyenin banka hesabına öder (Yönetmelik md. 11/3, 11/5).
    - Yönetmelik md. 11/3 ve 4/1-b'deki "büro" (birden fazla barolu illerdeki adli yardım bürosu) ibareleri Danıştay 8. Dairesinin 24.12.2025 tarihli, E.2025/1380, K.2025/10316 sayılı kararıyla iptal edilmiştir.
  - **Stopaj:**
    - CMK ödemeleri serbest meslek kazancıdır ve %20 stopaja tabidir. Baro görevlerinden doğan ödemelerde de %20 stopaj öngörülmüştür (23551, 23169).
    - Baro, GVK 94/1'deki tevkifat sorumluları arasında adıyla sayılmaz ve bu konuda doğrudan özelge bulunamadı. Baro ödeme dökümünü kontrol et; kesinti yoksa brüt tutarı beyan et ve mahsup etme (teyit edilmedi).
  - **Yıl:** Makbuz Başsavcılığa bir yıl düzenlenip ödeme hesaba ertesi yıl geçtiyse kazanç ve stopaj mahsubu, paranın hesaba geçtiği yıla aittir (23700).
  - **KDV tevkifatı:**
    - Başsavcılık 5018 sayılı Kanuna ekli (I) sayılı cetveldeki Adalet Bakanlığına bağlıdır. Baro ise kamu kurumu niteliğinde meslek kuruluşudur. İkisi de "diğer hizmetler" alıcısıdır.
    - KDV dahil bedel işlemin yapıldığı yılın sınırını aşarsa (2026: 12.000 TL, 2025: 9.900 TL) 5/10 tevkifat uygulanır. Zorunlu yol gideri bu bedele eklenir.
    - 2013 tarihli özelgedeki "CMK ücretinde tevkifat yok" görüşü 01.03.2021'den itibaren geçersizdir (30484).
  - **Tevkif edilen KDV'nin beyanı:** Baro tevkif ettiği KDV'yi 2 No.lu beyannameyle beyan eder. Genel bütçeli idareler ise 2 No.lu beyanname vermez (KDV GUT I/C-2.1.3.4.3.1). Bu yüzden genel bütçe ödeneğinden ödeme yapan Başsavcılık için 2 No.lu beyanname söz konusu değildir. Avukat açısından sonuç değişmez: işlemi 1 No.lu beyannamede gösterir.
  - **Ücretli çalışan avukat:**
    - CMK tahsilatı yanında çalıştığı avukatın veya büronun e-SMM'siyle yapılır (Yönetmelik md. 11/4).
    - Ödemenin çalışana bırakılması, büro sahibi yönünden serbest meslek kazancı niteliğini değiştirmez. Çalışan yönünden ödeme ücrettir.
    - Şirkette sigortalı çalışan ama baro tarafından sürekli CMK görevi alan avukat için GİB'e göre faaliyet mutattır: mükellefiyet açılmalı ve SMM düzenlenmelidir (23655). Av.K. 11–12'deki çalışma yasaklarını ayrıca değerlendir.
  - **KDV oranı:** Adli yardım işlerinde ve çocuk mahkemesinin görev alanındaki CMK işlerinde (soruşturma evresi dahil) %10, diğer CMK işlerinde %20'dir. Diğer CMK işlerindeki %20 lafzi bir yorumdur; oranı doğrudan belirten özelge bulunamadı (`kdv.md` §1, §5 ve §9).
  - **Makbuzda ayrıştırma:** Tarife ücreti ve zorunlu yol gideri "ücret"tir; stopaja ve KDV'ye tabidir. Avukatın ödediği temyiz, istinaf ve itiraz harçlarının iadesi ise kesintisiz ödenir (Yönetmelik md. 11/6). Bu kalemleri e-SMM'de ayrı göster (§5).
  - **Tarife:**
    - Hukuki yardımın yapıldığı tarihte yürürlükte olan tarife uygulanır (Yönetmelik md. 10/11). 2025 CMK Ücret Tarifesi RG 01.02.2025/32800'de, 2026 tarifesi RG 08.01.2026/33131'de yayımlandı.
    - Aynı soruşturma veya kovuşturma evresinde bir kişi için aynı avukata birden fazla ücret ödenmez (md. 10/3). Aralarında menfaat çatışması olmayan birden fazla kişi için ise her biri adına ayrı ücret ödenir (md. 10/4).
  - ⚖️ CMK ödemelerinden damga vergisi kesilmesi tartışmalıdır (`uygulama-notlari.md` §14, 16a; `damga-harc.md`).

  [Özelge: 02.07.2025, E-84974990-130[KDV-2/İ/28-2025/75]-365183 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/38775] [Özelge: 16.02.2022, E-62902401-130[2020-701-75]-22832 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/32149] [Özelge: 02.06.2021, E-66523654-130[ÖZG-7-2021]-29773 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273] [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985] [Özelge: 22.10.2013, 88409335-130[9-ÖZELGE-2013-1-3]-26 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30484] [Özelge: 11.03.2013, 97677631-041-2-7 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23700] [Özelge: 09.06.2011, B.07.1.GİB.4.38.15.02-VUK-21-197-50 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23655] [Kaynak: CMK Ücret Yönetmeliği (mevzuat.gov.tr MevzuatNo=11156) md. 4/1-e, 10/3, 10/4, 10/11, 11/3–11/8; Danıştay 8. D., 24.12.2025, E.2025/1380, K.2025/10316; KDV GUT I/C-2.1.3.2.13, I/C-2.1.3.4.1, I/C-2.1.3.4.3.1; doğrulanmış araştırma notu, 12.10.2026]

## 4. Avukatın avukata iş vermesi ve tevkil

- **Belge ve stopaj.** İşi alan avukat, işi veren avukat adına KDV'li e-SMM düzenler. İşi veren avukat GVK 94'te sayılan serbest meslek erbabı olduğundan ödemeden %20 stopaj keser ve muhtasar beyannameyle beyan eder. Aynı kural başka bir serbest avukata vekalet ücreti payı ödenmesinde de geçerlidir. [Özelge: 28.12.2018, 11395140-105[VUK-1-20846]-1194369 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26372]
- **Hasılat ve gider.**
  - İşi veren avukatın müvekkilden (somut olayda bankadan) tahsil ettiği bedelin tamamı hasılattır.
  - Diğer avukata ödenen bedel, onun düzenlediği e-SMM'ye dayanılarak gider yazılır.
  - İki hizmet ayrı ayrı KDV'ye ve stopaja tabidir. Alınan e-SMM'deki KDV'nin indirimi genel hükümlere tabidir (`kdv.md`).

  [Özelge: 08.09.2014, 39044742-130-2170 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/29253]
  - *Güncelleme:* 2014 tarihli özelge KDV tevkifatına hiç değinmez; tevkifat olmadığını da söylemez. Bugün bankaya verilen avukatlık hizmetinde hizmetin niteliğine bakılır:
    - Hukuki danışmanlıksa 9/10 tevkifat uygulanır (KDV GUT I/C-2.1.3.2.2). Danışmanlık 117 Seri No.lu Tebliğ döneminde de belirlenmiş alıcılara karşı tevkifata tabiydi.
    - Yargı mercileri önündeki veya icra hizmetiyse 01.03.2021'den itibaren 5/10 tevkifat uygulanır (KDV GUT I/C-2.1.3.2.13).
    - Her iki durumda da KDV dahil bedelin sınırı aşması gerekir.

    Özelgedeki iş, bankanın ipotek işlemlerinin yürütülmesidir; bu iş yargı mercii önünde verilmez. Bu tür işlerin danışmanlık mı yoksa "diğer hizmet" mi sayılacağına ilişkin özelge bulunamadı. [Özelge: 02.06.2021, E-66523654-130[ÖZG-7-2021]-29773 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273] [Özelge: 22.10.2013, 88409335-130[9-ÖZELGE-2013-1-3]-26 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30484]
- **Tevkil (yetki belgesi).**
  - Kararla hükmedilen vekalet ücretinin hak sahibi, aksi ispatlanmadıkça kararda vekil olarak adı geçen avukattır ve e-SMM'yi o düzenler.
  - Tevkil sözleşmesi gereği yetki belgeli avukata yapılan ödeme için yetki belgeli avukat ayrıca e-SMM düzenler.
  - Ücretin avukatlar arasında hangi oranda paylaşılacağı vergi konusu sayılmamıştır.
  - Ortak ve tevkilli dosyalarda her avukat kendi payı için ayrı makbuz düzenler; biri tamamına makbuz kesip vergisini düşerek dağıtamaz. Tevkil ücreti müvekkile yansıtılıyorsa makbuz müvekkil adına düzenlenir (`uygulama-notlari.md` §5 tablosu).
  - Tek ve 2014 tarihli özelgedir.

  [Özelge: 10.04.2014, 38418978-120[65-13/9]-361 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23597]

## 5. Masraflar: gider avansı, icra ve tebligat masrafı, yol gideri, yargılama gideri

GVK 67'deki temel ayrım (fıkra numaraları 12.10.2026'da konsolide metinden kontrol edildi):
- **2. fıkra:** Müvekkilden mesleki faaliyetle ilgili alınan gider karşılıkları kazanca eklenir.
- **4. fıkra:** Vergi, resim, harç, keşif, şahitlik, bilirkişilik ve ekspertiz gibi işlere harcanmak üzere alınan ve tamamen bu işlere harcanan paralar kazanç sayılmaz.

- **Müvekkil adına icra dairesine yatırılan takip masrafları.**
  - Bunlar bedel eklenmeden müvekkile aynen yansıtılırsa kazanç sayılmaz; e-SMM düzenlenmez ve KDV hesaplanmaz.
  - Masraf sözleşme gereği borçludan tahsil edilemeyip avukatın üzerinde kalsa bile gider yazılamaz.
  - Masrafın üstüne komisyon gibi bir bedel alınırsa, o bedel için e-SMM düzenlenir ve genel oranda (2026'da %20) KDV hesaplanır.
  - Harç, tebligat, bilirkişi ve keşif avansları için masraf dökümünü ve dekontları dosya bazında sakla. Tebligat masrafı özelgede ayrıca anılmaz; "...gibi" ifadesine dayanan bir kıyastır.

  [Özelge: 04.06.2015, 11395140-105[236-2012/VUK-1-...]-58433 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/21255] [Kaynak: GVK 67/4; GİB Rehberi Yayın 590 s. 7]
- **Harcanmayan bakiye.** Gider avansının harcanmayan kısmı hasılattır. Bakiyenin müvekkile iade edilmesi hâlinde hasılat sayılmayacağı özelgelerde açıkça yazmaz; bu, yargılama giderlerindeki iade mantığına uyan bir yorumdur. İadeyi bankadan yapın ve dekontunu saklayın. [Özelge: 04.06.2015, 11395140-105[236-2012/VUK-1-...]-58433 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/21255] [Özelge: 11.10.2013, 49327596-120[65.GVK.2013.29]-259 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23601]
- **Yol, konaklama ve benzeri gider karşılıkları.**
  - Bunlar 67/4'teki istisnaya girmez; 67/2 uyarınca hasılattır. Tahsil edildiğinde e-SMM düzenlenir; tahsil edilmeyen tutar için düzenlenmez.
  - Ödeyen tevkifat sorumlusuysa %20 stopaj yapılır. "Yansıtma" adıyla stopajsız belge düzenlenemez.
  - Akdi işlerdeki yol giderinin KDV'sini özelgeler tartışmaz. KDVK 24/b gider karşılıklarını matraha kattığından KDV hesaplanır.
  - Yolun ve otelin faturası avukat adına alınırsa önce e-SMM düzenlenir, sonra fatura gider yazılır (`uygulama-notlari.md` §8).
  - CMK'daki zorunlu yol gideri "ücret" tanımına girer (Yönetmelik md. 4/1-e). Kazanç sayılır, stopaja ve KDV'ye tabidir (31985) ve KDV tevkifatı sınırı hesabında işin bedeline eklenir.

  [Özelge: 11.10.2013, 49327596-120[65.GVK.2013.29]-259 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23601] [Özelge: 22.07.2011, B.07.4.DEF.0.03.10.00-193-845-26 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23644] [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985] [Kaynak: GVK 67/2; KDVK 24/b; CMK Ücret Yönetmeliği md. 4/1-e]
- **Tebligat ve posta masrafı.**
  - PTT'nin icra dairesi adına düzenlediği tebligat faturası avukatın kazancından indirilemez; indirim için faturanın avukat adına düzenlenmesi gerekir.
  - Hizmeti alan icra dairesi olduğundan faturanın onun adına düzenlenmesi VUK'a aykırı değildir.
  - Bu masraf müvekkilden aynen alınıyorsa zaten kazanç dışıdır.
  - Masrafı sözleşmeye göre avukat üstleniyorsa, gider yazabilmek için belgeyi kendi adına almalıdır.

  [Özelge: 12.09.2019, 27575268-105[229-2017-164]-302638 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23555]
- **Vekaletname pulu.** TBB'nin bastırdığı ve vekaletnameye yapıştırılması zorunlu pulun bedelini avukat karşılıyorsa GVK 68/9 kapsamında gider yazılır. Bedeli müvekkil karşılıyorsa gider yazılamaz; aynen yansıtılan bedel de kazanç sayılmaz. [Özelge: 07.03.2017, B.07.1.GİB.4.35.16.01-120.04.01[68-2016/3]-7601 (metinde: 84098128-120.04.01[68-2016/3]-7601) — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23723]
- **UYAP Avukat Portal ödemeleri.** Avukat, masrafları aynen yansıttığını ispatlamak için portal çıktılarını, icra hesabına yapılan havale ve EFT dekontlarını ve POS sliplerini dosya bazında saklamalıdır. Bu belgelerin müvekkilin kayıtlarında kullanılması için §12. [Özelge: 21.04.2014, 64597866-105[229-2014]-57 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/25620]
- **Yargılama giderleri.**
  - Davayı kaybedenin ödemesine hükmedilen ve müvekkile iade edilmek üzere avukatın tahsil ettiği yargılama giderleri GVK 67/4 uyarınca kazanç sayılmaz. Bunlar için e-SMM düzenlenmez ve ödeyen stopaj yapmaz.
  - Giderler müvekkile iade edilmeyip avukatta kalırsa kazanç sayılır ve müvekkil adına e-SMM düzenlenir.
  - İcradan tek kalemde gelen tahsilatta, makbuza tabi vekalet ücreti ile müvekkile aktarılacak yargılama giderini ayrıştır.

  [Özelge: 29.08.2022, 48816587-120[2019]-60836 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23697]
- **Avukatın kendi alacak davasındaki masraflar.** İcra takip masrafı, mahkeme masrafı ve icra tahsil harcı serbest meslek kazancına dahil edilmez. İcra müdürlüğünün kestiği harç ve damga vergisi gibi kesintiler de gider yazılamaz. [Özelge: 07.01.2016, 62030549-120[65-2014/483]-1238 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23585] [Özelge: 16.09.2011, B.07.1.GİB.4.06.18.02-32229--8126-740 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26026]
- **CMK'da avukatın ödediği harçlar.** Temyiz, istinaf ve itiraz harçları "ücret" tanımında sayılır, ancak avukata kesinti yapılmadan ödenir ve kazanç sayılmaz. Maddi dayanak GVK 67/4'tür; Yönetmelik ise GVK 67'nin "ikinci fıkrasına" atıf yapar. [Kaynak: CMK Ücret Yönetmeliği md. 4/1-e ve 11/6; GVK 67/4; doğrulanmış araştırma notu, 12.10.2026]

## 6. POS ile ve müvekkil adına yapılan tahsilatlar

- **Yalnız ücret kısmı için makbuz.**
  - Avukat kendi POS cihazıyla icra borçlusundan tahsilat yaparsa yalnız avukatlık ücretine isabet eden kısım hasılattır.
  - e-SMM yalnız bu kısım için ve KDV ayrıca gösterilerek düzenlenir.
  - Müvekkile ait asıl alacak, faiz ve masraflar için e-SMM düzenlenmez.
  - POS kullanımı için ayrıca komisyon alınırsa onun için de e-SMM düzenlenir.

  [Özelge: 26.08.2011, B.07.1.GİB.4.07.16.01-GVK.2010.162-266 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23637] [Özelge: 30.05.2011, B.07.1.GİB.4.20.15.02-VUK-2011/2-114 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26381]
- **Başkasının POS'u veya hesabı.** 7524 sayılı Kanunla VUK mük. 355'e, tahsilatın başkasının adı, hesabı veya POS'u kullanılarak yapılmasına ilişkin ayrı bir ceza eklendi. Cezanın oranı ve tutarı doğrulama kayıtlarında çelişkilidir (teyit edilmedi; `parametreler.md`). Büroda ortak POS veya başka avukatın hesabı kullanılıyorsa tahsilatı kendi POS'una ya da hesabına geçir; e-SMM'yi de kendi adına düzenle. [Kaynak: VUK mük. 355 (7524 s.K.); `parametreler.md` cezalar tablosu]
- **KDV beyannamesi.** Matrah olarak yalnız ücret kısmı yazılır; POS tahsilat toplamı kredi kartı tahsilatı satırında gösterilir. Özelgedeki satır numaraları eskimiştir; güncel beyanname formuna bakın. [Özelge: 26.08.2011, B.07.1.GİB.4.07.16.01-GVK.2010.162-266 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23637]
- **Müvekkile aktarılan paralar (emanet).**
  - Müvekkil adına tahsil edilip müvekkile aktarılan asıl alacak avukatın hasılatı değildir. Avukatın hasılatı yalnız kendisine kalan vekalet ücreti ve kazanca dahil gider karşılıklarıdır.
  - Aktarım dekontlarını dosya bazında saklayın.
  - Emanet paraları ayrı bir hesapta ve dosya bazında izlemek, hasılatla karışmalarını önler ve GVK 69 yoklamasında ya da banka hareketi incelemesinde izah güçlüğünü azaltır.
  - Bu paraların 459 Sıra No.lu VUK GT'deki tevsik kapsamına girip girmediğine ve emanet hesap uygulamasına ilişkin özelge veya tebliğ açıklaması bulunamadı. Bu konudaki sonuçlar çıkarımdır (güven düşük).

  [Özelge: 26.08.2011, B.07.1.GİB.4.07.16.01-GVK.2010.162-266 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23637] [Özelge: 29.08.2022, 48816587-120[2019]-60836 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23697] [Kaynak: GVK 65, 67/1, 67/4]

## 7. Avukatın kendi ücret alacağı: dava, icra, iade

- **Azilden sonra ilamlı icrayla tahsil.**
  - Eski müvekkil şirketin icra dosyasına yatırdığı alacak aslı (akdi ücret) ve vekalet ücreti serbest meslek kazancıdır. Şirket ödeme sırasında ikisinden de %20 stopaj yapar; avukat bu kısım için eski müvekkil adına e-SMM düzenler.
  - Kanuni faiz GVK 75/2-6 uyarınca menkul sermaye iradıdır. Stopaja tabi değildir ve e-SMM'ye girmez.
  - Masraflar kazanca dahil edilmez.
  - Kararda "KDV hariç" ibaresi yoksa ücret KDV dahil sayılır ve KDV iç yüzde yöntemiyle hesaplanır.
  - Tek ve 2016 tarihli özelgedir.

  [Özelge: 07.01.2016, 62030549-120[65-2014/483]-1238 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23585]
- **İcra inkar tazminatı ve yasal faiz.**
  - Bunlar menkul sermaye iradıdır; KDV'nin konusuna girmez ve stopaja tabi değildir. Tahsil edildikleri yılın geliri sayılır.
  - Tevkifata ve istisnaya tabi olmayan menkul ve gayrimenkul sermaye iratlarının toplamı GVK 86/1-d'deki haddi (2026: 22.000 TL) aşmıyorsa beyana dahil edilmez.
  - Bu had bir istisna değildir; aşılırsa tutarın tamamı beyan edilir.

  [Özelge: 16.09.2011, B.07.1.GİB.4.06.18.02-32229--8126-740 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26026] [Kaynak: GİB Menkul Sermaye İradı Rehberi Yayın 584 (Şubat 2026) s. 7–9]
  - *Çelişki:* Aynı özelgenin VUK bölümü, tazminat ve faiz için borçlu adına SMM düzenleneceğini söyler; bu, özelgenin kendi GV ve KDV değerlendirmesiyle çelişir. Daha yeni olan 23585, SMM'yi yalnız serbest meslek kazancı niteliğindeki kısımla sınırlar. 23585'i esas alın; tutar büyükse kendi olayınız için özelge isteyin.
- **KDV dahil kararlaştırılan ücret.** Ücret sözleşmede KDV dahil belirlenmişse KDV iç yüzde yöntemiyle ayrılır ve stopaj KDV hariç tutardan hesaplanır.
  - Örnek (türetilmiş; 2026, %20 KDV, alıcı belirlenmiş alıcı değil): KDV dahil 12.000 TL ücret → KDV hariç 10.000 TL, KDV 2.000 TL, stopaj 2.000 TL; avukata ödenen 10.000 TL.
  - %10'luk işlerde iç yüzde 1,10 ile hesaplanır (`kdv.md` §1–2).
  - Avukat ile müvekkil arasında işçi-işveren ilişkisi varsa ödeme ücrettir; e-SMM yerine bordro düzenlenir.

  [Özelge: 11.11.2011, B.07.1.GİB.4.06.16.01-120[94-11/12]-987 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23630]
- **Net ücret anlaşması (vergiyi müvekkil üstleniyor).** Kesilmesi gereken vergiyi ödeyen üstlenirse stopaj, fiilen ödenen tutar ile üstlenilen verginin toplamı üzerinden hesaplanır (brüte iblağ). e-SMM brüt tutar üzerinden düzenlenir. Hesap için `smm_hesap.py makbuz --net`. [Kaynak: GVK 96] [Özelge: 16.11.2017, B.07.1.GİB.4.07.17.02-105[Mük.257.VUK.ÖZ.14.39]-188100 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23504 (GVK 96 metnini aktarır)]
- **Başarıya bağlı ücretin iadesi.**
  - Akdi ücrette en çok %25'lik başarı yüzdesi kararlaştırılabilir (Av.K. 164/2).
  - Davayı kazanma şartıyla alınan ücret için tahsil anında e-SMM düzenlenir ve stopaj yapılır.
  - Dava kaybedilip ücret stopaj dahil toplam tutar olarak iade edilir ve iade belgelenirse, önceden gelir yazılan tutar GVK 68 uyarınca gider yazılabilir.
  - Beyan edilmiş KDV ise düzeltilemez; iade riski KDV açısından avukatta kalır. Sözleşmeyi buna göre kur.

  [Özelge: 29.03.2017, 11395140-105[VUK-1-19829]-87103 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/23649] [Kaynak: Av.K. 164/2]
  - *Çelişki:* 2012 tarihli İzmir özelgesi, tahsil edilip "değişik nedenlerle" iade edilen paranın gider yazılamayacağını söylemiştir. Daha yeni ve olaya daha uygun görüş 23649'dur. Bu görüşe dayanmak için iade şartı sözleşmede yazılı olmalı ve iade bankadan yapılmalıdır. [Özelge: 21.02.2012, B.07.1.GİB.4.35.17.01-35-02-208 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23574]
  - ⚖️ *Tartışmalı (iadede KDV):* GİB'in iki özelgesi de (23649, 23574) hizmet ifa edildikten sonra iade edilen ücrette KDV'nin düzeltilemeyeceğini söyler; gerekçe hizmetin iadesinin fiilen mümkün olmamasıdır. TBB eğitimindeki uygulama görüşüne göre ise iade tutarındaki KDV iç yüzdeyle hesaplanıp indirilecek KDV olarak alınabilir (`uygulama-notlari.md` §5). KDVK 35'teki "işlemden vazgeçilmesi" hükmüne dayanan bu görüş GİB'e karşı risklidir. Tutar büyükse kendi olayın için özelge iste.
  - *Bozma kararıyla iade ayrıdır:* Tahsil edilen karşı taraf vekalet ücreti Yargıtay bozma kararı üzerine kısmen iade edilirse, iade edilen kısımda KDV'ye konu hizmet kalmaz. Avukat değişikliğin olduğu dönemde defterde ve beyannamede KDVK 35'e göre düzeltme yapar; iade, belgelenmek şartıyla gelir vergisinde gider yazılır. İadeyi alan 5018 kapsamındaki kurum fatura düzenleyemiyorsa Merkezi Yönetim Harcama Belgeleri Yönetmeliğine göre düzenlediği belge tevsik edici sayılır. Ayrıntı `vekalet-ucreti.md` §8. [Özelge: 18.02.2016, 50426076-130[1-2014/20-1182]-40 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/29150] [Özelge: 23.08.2011, B.07.1.GİB.4.35.16.01-176200-406 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23702]
- **Sözleşme sona erince ödenen tazminat.**
  - Bağımsız avukatlık veya müşavirlik sözleşmesi gereği görevden ayrılırken ödenen kıdem benzeri tazminat da serbest meslek kazancıdır ve tahsil edildiği yılda beyan edilir.
  - Somut olayda 31.01.2018 tarihli kâğıt SMM düzenlenmiş, %20 stopaj ve o tarihte geçerli %18 KDV uygulanmıştır.
  - Vergileri sözleşme gereği şirket üstlenmiştir. Bu durumda stopaj GVK 96 uyarınca brüte iblağ edilerek hesaplanır.
  - Özelge yalnız tazminatın niteliği ve beyan yılı hakkında hüküm kurar.

  [Özelge: 19.11.2019, 62030549-120[67-2019/293]-E.996093 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23202]

## 8. Tutar, kamu sözleşmeleri ve demirbaş satışı

- **Tarife altı veya ücretsiz hizmet.**
  - Avukatlık Asgari Ücret Tarifesinin altında ücret kararlaştırılamaz (Av.K. 164/4).
  - Meslek teşekkülünün tarifesi varsa KDV matrahı tarifenin altında olamaz (KDVK 27/5). Bu yüzden KDV, Avukatlık Asgari Ücret Tarifesindeki tutar üzerinden hesaplanır; hiç ücret alınmayan işler de buna dahildir.
  - Özelgedeki soru, Av.K. 164/4 kapsamında mesleki dayanışma gereği ücretsiz takip edilen işleri de içeriyordu.
  - Ücretsiz işte KDV'nin hangi belgeyle beyan edileceği özelgede açık değildir. Uygulamada iş kesinleşince "bedeli tahsil edilmemiştir" açıklamalı makbuz düzenlenir ya da KDV doğrudan beyan edilir (`uygulama-notlari.md` §3).
  - Ücretsiz işe ilişkin tek özelge 2013 tarihli 23601'dir. Tarife alt sınırını 2012 tarihli 23614 de uygular (dosyaları varlık şirketine temlik edilen banka avukatı; §2).

  [Özelge: 11.10.2013, 49327596-120[65.GVK.2013.29]-259 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23601] [Özelge: 10.08.2012, B.07.1.GİB.4.35.16.01-176200-743 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23614] [Kaynak: KDVK 27/5; Av.K. 164/4]
  - ⚖️ *Tartışmalı:* KDV matrahı için hangi tarihteki tarifenin esas alınacağı (sözleşme tarihi mi, kesinleşme tarihi mi) GİB tarafından açıkça düzenlenmemiştir. AAÜT md. 21, karşı tarafa yükletilecek ücret için hukuki yardımın tamamlandığı veya hükmün verildiği tarihi esas alır. Sürekli şirket vekilliğinde tarife farkının KDV'si de tartışmalıdır. Bkz. `uygulama-notlari.md` §3 ve §5; `aaut-2025-2026.md`.
- **Belediyeye sözleşmeli avukatlık.**
  - e-SMM, belediyenin fiilen ödediği tutar üzerinden düzenlenir. Somut olayda tarifedeki 850 TL yerine ödenen 717,94 TL esas alınmıştır.
  - Sözleşme avukatlık ortaklığıyla yapılmış ve hizmeti ortaklık yürütüyorsa gelir serbest meslek kazancıdır ve %20 stopaja tabidir.
  - Sözleşme bir ortakla yapılmış ve iş ücret unsurlarını taşıyorsa gelir ücret sayılır.

  [Özelge: 06.03.2012, B.07.1.GİB.4.20.15.01-30-MUK-2011-230-195 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26378] [Özelge: 24.10.2011, B.07.1.GİB.4.20.15.01-30-MUK-2010-39-353 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23622]
  - *Gerilim:* Bu iki özelge KDVK 27/5'i anar ama KDV matrahını ayrıca tartışmaz. Gelir vergisinde tahsil edilen tutar esastır; KDV matrahı ise tarifenin altına inemez (23601). Bu nedenle KDV matrahının tarifenin altında kalıp kalmadığını ayrıca kontrol edin. Her iki özelge de somut olaya özgüdür.
- **Envantere kayıtlı aracın satışı.**
  - e-SMM, alış-satış farkı üzerinden değil, tahsil edilen satış bedelinin tamamı üzerinden ve tahsil anında düzenlenir.
  - VUK 328'e göre hesaplanan müspet fark kazanca eklenir (GVK 67/3).
  - KDV satış bedeli üzerinden hesaplanır.
  - Makbuzun düşük tutarla düzenlenmesi VUK 353/1 cezası gerektirir.
  - Binek otomobil teslimlerine özgü KDV hükümlerini `kdv.md`'den ayrıca kontrol edin.

  [Özelge: 07.01.2020, 57062627-010.01-357 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/25805]

## 9. KDV tevkifatının e-SMM'de gösterilmesi

- **Hukuki danışmanlık: 9/10.**
  - Belirlenmiş alıcılara (KDV GUT I/C-2.1.3.1/b) verilen hukuki danışmanlık ve müşavirlik hizmetinde 9/10 KDV tevkifatı uygulanır (I/C-2.1.3.2.2.1–2.1.3.2.2.2).
  - Belirlenmiş alıcılar dışındakilere verilen hizmette tevkifat uygulanmaz. Örneğin listede olmayan bir özel şirkete verilen danışmanlıkta 9/10 tevkifat yoktur.
  - Bu alıcı listesi geniştir. Kamu idareleri, bankalar ve sigorta şirketlerinin yanında sendikalar, vakıf üniversiteleri, organize sanayi bölgeleri, payları BİST'te işlem gören şirketler ve yarıdan fazla hissesi kamuya ait şirketler de listededir.
  - Avukatlık ve danışmanlık hizmetleri aynı sözleşmede yer alıyor ve ayrı ayrı ücretlendirilmiyorsa toplam sözleşme bedeli üzerinden 9/10 tevkifat uygulanır.
  - 23562 bu kuralı uygular, ancak olayı avukatlıkla ilgili değildir (3D görselleştirme hizmeti).

  [Kaynak: KDV GUT I/C-2.1.3.1/b, I/C-2.1.3.2.2.2] [Özelge: 26.01.2018, 62030549-120[94-2017/106]-93119 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23562]
- **Yargısal ve icra hizmetleri: 5/10.**
  - Avukatların hukuki ihtilaflarla ilgili olarak yargı mercileri önünde verdikleri hizmetler danışmanlık tevkifatının (9/10) kapsamı dışındadır. Yargı kararlarının sonuçlarıyla ilgili, vekâlet akdi çerçevesinde verilen hizmetler (icra vb.) de bu kapsamın dışındadır (I/C-2.1.3.2.2.2, 38 Seri No.lu Tebliğle değişik).
  - 01.03.2021'den itibaren bu hizmetler "diğer hizmetler" alıcılarına verildiğinde 5/10 tevkifata tabidir (I/C-2.1.3.2.13). Bu alıcılar: 5018 sayılı Kanuna ekli cetvellerdeki idareler; kanunla veya CBK ile kurulan kamu kurum ve kuruluşları; KİT'ler (50 Seri No.lu Tebliğle eklendi); döner sermayeli kuruluşlar; barolar dahil kamu kurumu niteliğindeki meslek kuruluşları; bankalar; sigorta, reasürans ve emeklilik şirketleri; emekli ve yardım sandıkları; kalkınma ajansları.
  - Bu liste 9/10 listesinden dardır. Örneğin payları BİST'te işlem gören bir sanayi şirketine verilen dava hizmetinde tevkifat yoktur.
  - Sınır KDV dahil bedele ve işlem bazında bakılarak uygulanır. Başsavcılık arabuluculuk ücretlerini toplu ödese bile sınır, birbirinden bağımsız dosyalar için dosya bazında uygulanmıştır.
  - Sınırın "işlemin yapıldığı yılın VUK 232 fatura sınırı" olarak belirlenmesi RG 10.02.2024, 32456'da yayımlanan Seri 50 değişikliğiyle getirilmiştir ve 01.03.2024'ten itibaren uygulanır (30151). 2025 sınırının 9.900 TL olduğu (VUK GT 577) GİB özelgesinde de aktarılmıştır (38981). 2026 sınırı 12.000 TL'dir (VUK GT 588).
  - Tevkif edilen KDV'yi alıcı 2 No.lu beyannameyle beyan eder. Genel bütçeli idareler (ör. Cumhuriyet Başsavcılığı) bunun dışındadır; ödeme genel bütçe dışı bir kaynaktan yapılırsa onlar da 2 No.lu beyanname verir (I/C-2.1.3.4.3.1).
  - Avukat işlemi 1 No.lu beyannamenin kısmi tevkifat tablosunda gösterir ve yalnız tevkif edilmeyen KDV'yi öder.
  - e-SMM'deki tevkifat kodu muhtemelen 616 ("diğer hizmetler") olmalıdır; teyit edilmedi.

  [Özelge: 07.11.2023, E-37009108-130[467770]-182439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30159] [Özelge: 02.06.2021, E-66523654-130[ÖZG-7-2021]-29773 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273] [Özelge: 25.09.2024, E-35831311-010.01-23750 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30151] [Özelge: 15.08.2025, E-64597866-130-1025186 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/38981] [Kaynak: KDV GUT I/C-2.1.3.2.2.2, I/C-2.1.3.2.13, I/C-2.1.3.4.1, I/C-2.1.3.4.3.1; Seri 35, 36, 38, 50]
- **Belgede gösterim.**
  - Makbuzda şu tutarlar ayrı ayrı gösterilir: işlem bedeli, hesaplanan KDV, tevkifat oranı, alıcının tevkif edeceği KDV, tevkifat dahil toplam tutar ve tevkifat hariç toplam tutar.
  - Borçlanılan tutar olarak rakam ve yazıyla tevkifattan sonra kalan tutar yazılır.
  - Tevkifatlı ve tevkifatsız işlemler tek belgede gösterilebilir. Bu durumda sınır, yalnız tevkifatlı işlemin KDV dahil bedeline uygulanır.
  - Gelir vergisi stopajı da makbuzda ayrıca gösterilir.

  [Kaynak: KDV GUT I/C-2.1.3.4.2] [Özelge: 23.08.2013, 11395140-019.01-1319 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/22146]
  - *Dayanağın güncel hâli:* 22146, 2014'te yürürlükten kalkan 117 Seri No.lu KDV Genel Tebliği'ne (3.4.2) ve %18 orana dayanır. Aynı gösterim kuralı bugün KDV GUT I/C-2.1.3.4.2'de yer alır; metin 12.10.2026'da kontrol edildi.
  - **Hesap örneği (türetilmiş; hiçbir özelgede bu rakamlarla geçmez).** 2026'da borçlu bir bankadır; kararda "KDV hariç" yazmayan 30.000 TL karşı taraf vekalet ücreti 12.000 TL sınırını aşar.
    - KDV hariç ücret 25.000 TL, KDV 5.000 TL.
    - GV stopajı (%20) 5.000 TL.
    - KDV tevkifatı (5/10) 2.500 TL.
    - Avukata ödenecek tutar: 25.000 − 5.000 + 5.000 − 2.500 = 22.500 TL.
    - Avukat 2.500 TL KDV beyan eder ve 5.000 TL stopajı mahsup eder.
    - Hesap: `smm_hesap.py makbuz --kdv-dahil 30000 --kdv-tevkifat 5/10`.

    [Kaynak: 311 Seri No.lu GVGT md. 25/5 (KDV dahil kabulü, iç yüzde, KDV hariç tutardan stopaj); KDV GUT I/C-2.1.3.2.13, I/C-2.1.3.4.1; VUK GT 588] [Özelge: 17.10.2022, 95462982-105[VUK.ÖZLG-20-109]-245464 — https://www.gib.gov.tr/mevzuat/kanun/434/ozelge/23524 (stopajın makbuzda gösterilmesi)] [Özelge: 06.06.2022, 36062021-130[09-2021/ÖZE-40]-50290 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232 (makbuzda 5/10)]

## 10. Belge düzenine uymamanın sonuçları

- **Özel usulsüzlük cezası (VUK 353/1).**
  - e-SMM'nin verilmemesi, alınmaması, hiç düzenlenmemesi, gerçek tutardan farklı düzenlenmesi veya e-belge yerine kâğıt olarak düzenlenmesi hâlinde belge başına tutarın veya farkın %10'u kadar özel usulsüzlük cezası kesilir. Kâğıt düzenleme yalnız Bakanlığın belirlediği zorunlu hallerde mümkündür.
  - Takvim yılı içindeki tespit sırasına göre asgari cezalar (2026):
    - 1. tespit: 17.000 TL
    - 2. tespit: 35.000 TL
    - 3. tespit: 53.000 TL
    - 4. tespit: 70.000 TL
    - 5. tespit: 87.000 TL
    - 6. ve sonraki tespitler: 170.000 TL
  - Bir takvim yılında her belge türü için ceza toplamı 17.000.000 TL'yi geçemez.
  - Asgari tutarlar VUK'a bağlı 2 sayılı cetveldedir ve her yıl yeniden değerlenir. 2025 tutarları (VUK GT 577): 14.000 / 28.000 / 43.000 / 57.000 / 70.000 / 140.000 TL; yıllık üst sınır 14.000.000 TL (`parametreler.md`).
  - Tek tespitte birden çok belge bulunursa her belge için ayrı ceza kesilir, ancak bu, cetvelde tek tespit sayılır.
  - e-SMM yerine VUK kapsamında olmayan bir belge düzenlenirse düzenleyene ceza 2 kat uygulanır.
  - Özelgelerde aktarılan eski tutarlar (ör. 23531'de yıllık üst sınır 120.000 TL, 2021 için 180.000 TL) güncel değildir.

  [Özelge: 07.01.2020, 57062627-010.01-357 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/25805] [Özelge: 17.06.2022, 62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Kaynak: VUK 353/1 (7524 sayılı Kanunla değişik; konsolide metin); VUK GT 588 eki liste (RG 31.12.2025, 33124 5. Mük.); VUK GT 577 (RG 30.12.2024, 32768 2. Mük.); cetvel tutarları `parametreler.md`]
- **Ödeyenin ihbarı.**
  - Ödeme yapan, e-SMM düzenlemeyen veya geç düzenleyen avukatı vergi dairesine bildirebilir; idare cezai işlem uygular (23519, 23531).
  - 7524 sayılı Kanunla getirilen kurala göre, belgeyi alması gereken kişi idarenin bilgisine girmeden önce, belgenin düzenlenmesi gereken süreyi izleyen 5 iş günü içinde bildirirse kendisine ceza kesilmez. Bu durumda düzenleyene ceza 3 kat uygulanır.
  - Belge yerine VUK dışı bir belge verildiği bildirilirse düzenleyene ceza 6 kat uygulanır.
  - Pratik sonuç: kurumsal müvekkile e-SMM'yi tahsilat günü ilet. Bekleyen her makbuz, alıcının ihbarıyla 3 kat ceza riski taşır.

  [Özelge: 07.07.2023, 62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519] [Özelge: 17.06.2022, 62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Kaynak: VUK 353/1]
- **Tacir olmayan gerçek kişi müvekkil (VUK 353/3).** Makbuz almayan müvekkile uygulanan ceza için §12. Avukatın kendi cezası bundan bağımsızdır. [Kaynak: VUK 353/3 (7524 sayılı Kanunla değişik)]
- **Tevsik zorunluluğuna uymama (VUK mük. 355).** İşlem tutarının %10'u kadar ceza kesilir; 2026'da serbest meslek erbabı için asgari 35.000 TL, yıllık üst sınır 35.000.000 TL'dir. Ceza avukata ve ödeyene ayrı ayrı kesilir (§11). Ödeme yapan taraf aykırılığı 5 iş günü içinde kendiliğinden bildirirse ona ceza kesilmez; bu durumda risk yalnız avukatta kalır. [Kaynak: VUK mük. 355 (7524 sayılı Kanunla değişik); `parametreler.md`]
- **Cezaların tebliği.** Ceza ihbarnameleri e-tebligatla gelir. Gerçek usulde vergilendirilen serbest meslek erbabı e-tebligatı kullanmak zorundadır. Tebliğ, iletiyi izleyen 5. günün sonunda yapılmış sayılır; dava ve uzlaşma süreleri buna göre başlar. Uzlaşma eşiği için `parametreler.md`. [Kaynak: VUK 107/A (7587 s.K. md. 9, RG 01.07.2026, 33297)]

## 11. Tevsik, stopaj mahsubu ve yoklama

- **Tevsik (30.000 TL).**
  - Serbest meslek erbabı 30.000 TL'yi aşan tahsilat ve ödemelerini banka, ödeme kuruluşu veya PTT aracılığıyla yapmak ve bunların belgeleriyle tevsik etmek zorundadır. Had 575 Sıra No.lu Tebliğle 30.11.2024'ten itibaren 7.000 TL'den 30.000 TL'ye çıktı.
  - Hizmet bedeli kısım kısım tahsil edildiğinde sözleşmenin toplam tutarı esas alınır. Tebliğdeki avukat örneğinde 160.000 TL'lik yıllık danışmanlık 15.000 TL'lik taksitlerle ödense de her taksit bankadan geçmelidir.
  - Aynı gün aynı kişiyle yapılan işlemler toplanır.
  - Uyulmazsa avukata ve ödeyene ayrı ayrı özel usulsüzlük cezası kesilir (VUK mük. 355).
  - 18.10.2024'ten itibaren mükellef olmayanlarla yapılan işlemler de kapsamdadır (572 Sıra No.lu Tebliğ). Avukatın gerçek kişi müvekkilden 30.000 TL'yi aşan tahsilatı da aracı kurum üzerinden yapılmalıdır. Mükellef olmayanların kendi aralarındaki işlemler kapsam dışıdır.
  - Ödemenin avukatın hesabına banka şubesinden açıklamalı olarak yatırılması uygun tevsiktir. Nakit alıp sonra kendi hesabına yatırmak uygun değildir.
  - Türkiye mukimi olmayanlarla yapılan işlemler belirli şartlarla kapsam dışıdır.
  - Aracı kurum kullanılması e-SMM düzenleme zorunluluğunu ortadan kaldırmaz.
  - Büyük tutarlı ücretleri elden tahsil etme. Büro kirası ise tutar sınırı olmaksızın banka veya PTT belgesiyle ödenir (Rehber Yayın 590 s.11; birincil tebliğ metninden teyit edilmedi; `giderler.md`, `parametreler.md`).

  [Kaynak: VUK mük. 257, mük. 355; 459 Sıra No.lu VUK GT (RG 24.12.2015, 29572) bölüm 3/d, 4.1, 4.1.1, 4.1.2, 4.2/h; 572 Sıra No.lu VUK GT (RG 18.10.2024, 32696) md. 1–4; 575 Sıra No.lu VUK GT (RG 30.11.2024, 32738) md. 1–4; GİB Rehberi Yayın 590 s. 34–35]
- **Stopajın mahsubu ve e-SMM mutabakatı.**
  - Kesilen stopaj önce ilgili dönemin hesaplanan geçici vergisinden, sonra yıllık beyannamede hesaplanan vergiden mahsup edilir. Mahsup için kesintinin beyannameye dahil edilen gelire ait olması gerekir.
  - Kalan kısım için iki yol vardır:
    - Diğer vergi borçlarına mahsup: tutar sınırı, inceleme raporu ve teminat aranmaz.
    - Nakden iade: inceleme raporu ve teminat aranmayan sınır 2025 için 340.000 TL, 2026 için 426.000 TL'dir. Aşan kısım için YMM tam tasdik raporu 2025'te 3.400.000 TL'ye, 2026'da 4.266.000 TL'ye kadar yeterlidir. Bunun üzerindeki kısım vergi inceleme raporuna göre ya da teminat karşılığında iade edilir.
  - e-SMM'lerdeki stopaj tutarlarını ödeyenlerin muhtasar beyanlarıyla mutabık tut. Stopaj yapılmayan tahsilatları mahsup listesine yazma.
  - Borçlu net ödeme yapıp kestiği stopajı beyan etmemişse ne olacağına ilişkin özelge bulunamadı. Rehbere göre nakden iadede verginin sorumlu adına tahakkuk ettiğini gösteren belge aranır. Bu durumda icra dosyasındaki net ödeme kaydını ve e-SMM'yi sakla, durumu vergi dairesine bildir (öneri; özelgeye dayanmaz).
  - Genel bütçeli idarelerin kestiği stopajın vergi dairesi ekranında görünmemesi sorunu için `uygulama-notlari.md` §12.

  [Kaynak: GVK 94, 121; 252 Seri No.lu GVGT; GİB Rehberi Yayın 590 (Şubat 2026) s. 24–29 (16.1.1, 16.1.3, 16.2.1); tutarlar `parametreler.md`]
- **Yoklama ve günlük hasılat tespiti (GVK 69).**
  - 01.01.2025'ten itibaren serbest meslek erbabında VUK 127 kapsamında ayda en az 3, yılda en az 12 yoklama yapılabilir.
  - Yoklamada tespit edilen günlük hasılat ortalamasından aylık ve yıllık hasılat hesaplanır. Bu tutar ile serbest meslek kazanç bildirimindeki gayrisafi hasılat arasındaki fark %20'den fazlaysa mükellef VUK 370 kapsamında izaha davet edilir.
  - 326 Seri No.lu GVGT md. 7'deki ayrıntılar:
    - Yoklama yapılacak mükellefler risk analizi ve beyan-harcama uyumsuzluğu gibi ölçütlerle seçilir.
    - Bir ayda üçten az yoklama yapılmışsa o ay ortalamaya katılmaz.
    - Fiilen çalışılan gün ve ay sayısı ile hafta sonu ve tatiller dikkate alınır.
    - Birden fazla mesleki faaliyet (ör. ayrı faaliyet kodlarıyla avukatlık ve arabuluculuk) ve birden fazla iş yeri ayrı ayrı kıyaslanır.
    - Düzeltme beyanları ve inceleme sonuçları kıyasta dikkate alınır.
  - Pratik sonuç: büroda alınan danışma ücreti ve avans için de e-SMM düzenle. Yoklama günlerinde makbuzsuz kalan tahsilat, yıl sonu bildirimiyle karşılaştırmada risk doğurur.
  - 12.10.2026 itibarıyla serbest meslek erbabı için asgari kazanç veya asgari matrah düzenlemesi kanunlaşmadı. Asgari kurumlar vergisi (KVK 32/C) yalnız kurumlar için geçerlidir. Bu alandaki tek mekanizma GVK 69'dur (güven orta).
  - GVK 113'teki hasılat esaslı kazanç tespiti avukatlara uygulanmaz. Bu usul şehir içi yolcu taşımacılığı içindir ve 7587 s.K. md. 5 ile taksi işletmecilerine de açılmıştır. KDVK 38'deki hasılat esaslı KDV de yalnız Cumhurbaşkanınca belirlenen sektörlere uygulanır (718 sayılı CBK: belediye ruhsatlı otobüsle toplu taşıma). Bu usulleri GVK 69 yoklamasıyla karıştırma.

  [Kaynak: GVK 69 (7524 s.K. md. 3, RG 02.08.2024, 32620; yürürlük 01.01.2025); 326 Seri No.lu GVGT (RG 27.09.2024, 32675) md. 6–7; VUK 127, 370; GİB Rehberi Yayın 590 §18 (s. 31–32); GVK 113; KDVK 38; 7587 s.K. md. 5 (RG 01.07.2026, 33297); 718 sayılı CBK (RG 07.02.2019, 30679); KVK 32/C] [Özelge: 14.08.2020, 62030549-120[37-2019/1371]-E.596266 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/24729 (GVK 113 kapsamı)]

## 12. Müvekkile bilgi

Bu bölüm avukatın kendi vergisine değil, müvekkilin yükümlülüklerine ilişkindir. Müvekkili bilgilendirirken kullan; müvekkil adına vergi danışmanlığı bu skill'in kapsamı dışındadır.

- **Stopajı kesen müvekkil.** GVK 94/1'de sayılan müvekkil kestiği %20 stopajı muhtasar beyannameyle beyan eder. Avukatın mahsubu bu beyana bağlıdır (§11). [Kaynak: GVK 94, 98]
- **KDV tevkifatı yapan alıcı.** Belirlenmiş alıcı, tevkif ettiği KDV'yi 2 No.lu beyannameyle beyan eder. Genel bütçeli idareler genel bütçe ödeneğinden yaptıkları ödemelerde bunun dışındadır. [Kaynak: KDV GUT I/C-2.1.3.4.3.1]
- **Davayı kazanan müvekkilin borçluya faturası.**
  - Karşı taraf vekalet ücreti önce davayı kazanan GV/KV mükellefi müvekkile ödenirse müvekkil, borçlu adına 7 gün içinde fatura düzenler.
  - Müvekkil bu ücreti kendi ücretli çalışanı olan avukata öderse ödeme bordroyla belgelenir.
  - Bu faturanın KDV'siz (KDV'nin konusu dışında) düzenleneceği KDV GUT I/B-4'ten çıkarılabilir, ancak bunu açıkça söyleyen özelge bulunamadı (teyit edilmedi).

  [Özelge: 17.06.2022, 62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Kaynak: 311 Seri No.lu GVGT md. 26/4–26/6; KDV GUT I/B-4]
- **Ödeyen kurumun kaydı ve bildirimi.** Ödeme yapan kurum e-SMM'yi VUK 219'a uygun olarak kayıtlarına geçirir. Makbuz düzenlenmezse veya eksik düzenlenirse avukatın bağlı olduğu vergi dairesine bilgi vermesi gerekir (23531).
- **Ücretin bir kısmının müvekkile bırakılması.** Bırakılan kısım için müvekkil (ör. banka) VUK'a uygun bir belge düzenlemelidir; aksi hâlde avukat bu kısmı gider yazamaz (§3, 23660).
- **Temlik.** Ücret alacağı temlik edilse de stopaj ve makbuz alma yükümlülüğü asıl borçlu müvekkilde kalır (§3, 25506).
- **UYAP Avukat Portal belgeleri.** Portal çıktıları, icra hesabına yapılan havale ve EFT dekontları ve POS slipleri ilgili mevzuata göre ödemeyi kanıtlıyorsa müvekkilin vergi kayıtlarında da tevsik belgesi olarak kullanılabilir. [Özelge: 21.04.2014, 64597866-105[229-2014]-57 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/25620]
- **Tevsik.** Gerçek kişi müvekkil de 30.000 TL'yi aşan ödemeyi banka üzerinden yapmak zorundadır; aksi hâlde müvekkile de ayrıca ceza kesilir. Aykırılığı 5 iş günü içinde kendiliğinden bildiren ödeyene ceza kesilmez (`parametreler.md`). Ücret sözleşmesine "ödemeler avukatın banka hesabına yapılır" maddesi konulması önerilir. [Kaynak: 572 ve 575 Sıra No.lu VUK GT; VUK mük. 355]
- **Makbuz almamanın cezası.**
  - VUK 232/1'in 1–5. bentleri dışında kalan kişiler (ör. tacir olmayan gerçek kişi müvekkil) SMM almazsa 2026'da belge başına 8.700 TL, yılda en çok 87.000 TL ceza kesilir. Kişi, makbuzun düzenlenmediğini 5 iş günü içinde bildirirse ceza kesilmez (VUK 353/3).
  - Kurumsal müvekkil de süresinde bildirirse VUK 353/1 cezasından kurtulur; bu durumda avukatın cezası 3 kat olur (§10).

  [Kaynak: VUK 353/1, 353/3 (7524 sayılı Kanunla değişik); VUK GT 588 eki liste]

## Çelişkiler, eskimiş görüşler ve açık sorular

1. **Kâğıt makbuz ve matbu imza** (26375, 2017): 01.06.2020'den itibaren e-SMM zorunludur. Hazır imza artık e-SMM'nin kâğıt çıktısında kullanılabilir (509 Sıra No.lu VUK GT V.5.4; 26369).
2. **"POS fişi SMM yerine geçer"** (26384, 2014): Bu kural yalnız hekimler içindir ve avukatlara hiç uygulanmamıştır; avukat e-SMM düzenler (26374, 26369).
3. **"Bir nüsha icra memuruna verilir"** (23617 ve 23614, 2012; 23504 ve 23505, 2017; 375 Sıra No.lu VUK GT): 311 Seri No.lu GVGT md. 26/3 (27.05.2020) ile buna gerek kalmamıştır (23511, 2024).
4. **7194 sayılı Kanun ve 311 Seri No.lu GVGT öncesi özelgeler** (ör. 23504, 23505, 23579): Karşı taraf vekalet ücretinde belge düzeni ve tevkifat sorumlusu konusunda bugünkü düzenle çelişebilir. 311 Seri No.lu GVGT md. 25–26 ile çatıştığında bu özelgeleri esas almayın.
5. **Ücretli avukatın vekalet ücreti** (23579, 2016): Özelgeye göre işveren avukat SMM düzenler ve ödeyen %20 keser. 311 Seri No.lu GVGT md. 25/4 ve 26/6'ya göre ise ödeyen tevkifat yapmaz; işveren avukata ücret olarak öder ve keser. Tebliği esas alın.
6. **Bankaya verilen hizmette tevkifat** (29253, 2014): Özelge tevkifata hiç değinmez; "tevkifat yok" demez. Bugün danışmanlık niteliğindeki hizmette 9/10, yargısal veya icra hizmetinde 01.03.2021'den itibaren 5/10 uygulanır (30273; KDV GUT I/C-2.1.3.2.2.2 ve I/C-2.1.3.2.13).
7. **117 Seri No.lu Tebliğ, %18 oran ve 1.000/2.000 TL sınır** (22146, 30484, 30273, 30159, 23202): Bugün KDV GUT, %20 oran ve VUK 232 fatura sınırı (2026: 12.000 TL, 2025: 9.900 TL) geçerlidir.
8. **Tahsil edilip iade edilen ücretin gider yazılması:** 23574 (2012) gider yazılamayacağını, 23649 (2017) ise sözleşme şartıyla yapılan ve belgelenen iadenin gider yazılabileceğini söyler. Yeni görüşü tercih edin.
9. ⚖️ **İade edilen ücretin KDV'si:** GİB (23649, 23574) KDV'nin düzeltilemeyeceğini söyler. `uygulama-notlari.md` §5'teki uygulama görüşüne göre iade tutarındaki KDV indirilebilir. GİB görüşü önceliklidir; diğer görüş tartışmalıdır (§7). Bozma kararıyla iade edilen karşı taraf vekalet ücreti çelişki değil olay farkıdır: orada KDVK 35 düzeltmesi yapılır (29150, 23702; `kdv.md` §10).
10. **İcra inkar tazminatı ve faiz için SMM:** 26026'nın VUK bölümü SMM düzenleneceğini söyler; 23585 ise SMM'yi yalnız serbest meslek kazancı kısmıyla sınırlar. 23585'i tercih edin.
11. **Fiilen ödenen tutardan SMM** (23622, 26378) ile **KDV matrahının tarifenin altına inemeyeceği kuralı** (23601, KDVK 27/5) arasında gerilim vardır.
12. **KDV beyannamesi satır numaraları** (23637) eskimiştir.
13. **"CMK ücretinde KDV tevkifatı yok"** (30484, 2013): 117 Seri No.lu Tebliğ dönemine aittir. 01.03.2021'den itibaren Başsavcılığa ve baroya verilen hizmette, sınır aşılırsa 5/10 tevkifat uygulanır (30273; KDV GUT I/C-2.1.3.2.13).
14. **"Başsavcılık tevkif ettiği KDV'yi 2 No.lu beyannameyle beyan eder"** (araştırma notu): KDV GUT I/C-2.1.3.4.3.1'e göre genel bütçeli idareler 2 No.lu beyanname vermez. Başsavcılık bu kapsamdadır, baro değildir. Avukat açısından sonuç değişmez.
15. **Geçici vergi dönemi** (31985, 2014): Özelgede aktarılan mük. 120 metnindeki "altışar aylık" ifadesi güncel değildir. Geçici vergi üçer aylık dönemler için %15 oranında hesaplanır; 7566 s.K. ile 2025'ten itibaren 4. dönem beyannamesi de verilir (`parametreler.md`).
16. **Harç ve masraf avansının dayanağı:** Kazanç sayılmama kuralı GVK 67'nin **4.** fıkrasındadır; 2. fıkra gider karşılıklarının kazanca eklenmesine ilişkindir. CMK Ücret Yönetmeliği md. 11/6 ise "ikinci fıkra"ya atıf yapar.
17. **Açık sorular:**
    - Ittıla anının tespiti.
    - e-SMM iptal ve düzeltme usulü: 509 Sıra No.lu Tebliğ bu konuyu teknik kılavuzlara bırakmıştır ve konuya ilişkin özelge bulunamadı. Uygulamadaki iptal ve yeniden düzenleme pratiği için `uygulama-notlari.md` §5.
    - Müvekkile iade edilen avans bakiyesinin vergisel durumu.
    - Emanet paraların tevsiki.
    - KDV tevkifatı sınırındaki "işlemin yapıldığı yıl" ifadesinin hizmet yılını mı, makbuz yılını mı kastettiği.
    - Birden çok dosya tek e-SMM'de gösterildiğinde sınırın dosya başına mı, makbuz toplamına mı uygulanacağı.
    - Bankanın ipotek ve benzeri yargı dışı işlerinde verilen avukatlık hizmetinin danışmanlık (9/10) mı, "diğer hizmet" (5/10) mi sayılacağı.
    - Terk sonrası tahsil edilen ücrette KDV'nin hangi dönemde ve kim tarafından beyan edileceği.
    - Ücretli avukatlıktan ayrıldıktan sonra tahsil edilen baro ücretlerine (23551) GVK 82'deki istisnanın uygulanıp uygulanmayacağı.
    - Baronun adli yardım ödemelerinde GV tevkifatı sorumluluğu (baro GVK 94/1'de adıyla sayılmaz).
    - Borçlunun net ödeme yapıp stopajı beyan etmediği durumda avukatın mahsup hakkı.
    - Davayı kazanan müvekkilin borçluya düzenleyeceği faturada KDV.
    - Ücretsiz işte KDV'nin hangi belgeyle beyan edileceği.
    - e-SMM tevkifat kodu (muhtemelen 616).

## Bu bölümde kullanılan özelgeler

Yerel tam metin yolu `ozelgeler/<ID>.txt` biçimindedir (skill kökünden `references/ozelgeler/<ID>.txt`). "Yok" yazanların metni yerelde bulunmaz; linkten okuyun.

| Tarih | Sayı | Konu | Link | Yerel metin |
|---|---|---|---|---|
| 15.08.2025 | E-64597866-130-1025186 | 2025 VUK 232 sınırının (9.900 TL) aktarımı; olay avukat dışı (şifre ve kod satışı) | https://gib.gov.tr/mevzuat/kanun/436/ozelge/38981 | yok |
| 02.07.2025 | E-84974990-130[KDV-2/İ/28-2025/75]-365183 | Adli yardım kararının icrasında vekalet ücretinde KDV %10; 2007/13033 BKK (II) 32. sıranın kapsamı | https://gib.gov.tr/mevzuat/kanun/436/ozelge/38775 | `ozelgeler/38775.txt` |
| 27.06.2025 | E-11395140-105[VUK-3-4253]-798105 | e-SMM düzenleyen serbest meslek erbabına e-Fatura zorunluluğu yok; e-SMM'nin niteliği | https://gib.gov.tr/mevzuat/kanun/434/ozelge/38672 | yok |
| 25.09.2024 | E-35831311-010.01-23750 | KDV GUT I/C-2.1.3.4.1'in 01.03.2024 sonrası metni; olay avukat dışı (demir-çelik) | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30151 | yok |
| 31.07.2024 | E-62030549-120-1020639 | Karşı taraf vekalet ücreti üçüncü kişilerce icraya yatırılınca borçlunun stopajı ve borçlu adına SMM | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511 | `ozelgeler/23511.txt` |
| 07.11.2023 | E-37009108-130[467770]-182439 | Bağımsız arabuluculuk dosyalarında KDV tevkifatı sınırının dosya bazında uygulanması | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30159 | `ozelgeler/30159.txt` |
| 07.07.2023 | 62030549-120[94-2021/516]-718872 | Haczen ödemede stopaj yok, SMM tahsil anında borçlu adına | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519 | `ozelgeler/23519.txt` |
| 17.10.2022 | 95462982-105[VUK.ÖZLG-20-109]-245464 | Stopaj yapılmayan vekalet ücreti; stopajın makbuzda gösterilmesi | https://www.gib.gov.tr/mevzuat/kanun/434/ozelge/23524 | `ozelgeler/23524.txt` |
| 29.08.2022 | 48816587-120[2019]-60836 | Vekalet ücreti belge düzeni; yargılama giderleri kazanç sayılmaz | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23697 | `ozelgeler/23697.txt` |
| 17.06.2022 | 62030549-120[94-2020/1307]-687704 | İlam vekalet ücretinde tahsil anında borçlu adına SMM; kazanan mükellef 7 gün içinde fatura; ihbar | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531 | `ozelgeler/23531.txt` |
| 09.06.2022 | 64597866-130-9597 | İlam ve icra vekalet ücretinde KDV tevkifatı; sınır hesabında toplama | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30226 | `ozelgeler/30226.txt` |
| 06.06.2022 | 36062021-130[09-2021/ÖZE-40]-50290 | Karşı taraf kamu idaresiyse vekalet ücretinde 5/10 KDV tevkifatı | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232 | `ozelgeler/30232.txt` |
| 20.05.2022 | E-50426076-120[65-2021/20-822]-66280 | Terk sonrası tahsilat arızi kazanç, SMM düzenlenmez | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23169 | `ozelgeler/23169.txt` |
| 16.02.2022 | E-62902401-130[2020-701-75]-22832 | Çocuk mahkemesi CMK işlerinde (soruşturma dahil) KDV oranı | https://gib.gov.tr/mevzuat/kanun/436/ozelge/32149 | `ozelgeler/32149.txt` |
| 02.06.2021 | E-66523654-130[ÖZG-7-2021]-29773 | CMK (Başsavcılık) ve adli yardımda (baro) 5/10 KDV tevkifatı | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273 | `ozelgeler/30273.txt` |
| 17.02.2021 | 27575268-105[236-2018-593]-58403 | Hizmeti alan Türkiye şubesi adına SMM | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26368 | `ozelgeler/26368.txt` |
| 20.11.2020 | 11395140-105[VUK-1-22499]-864517 | e-SMM zorunluluğu, ÖKC fişi, hazır imza, bilgi fişi (sağlık danışmanı) | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26369 | `ozelgeler/26369.txt` |
| 14.08.2020 | 62030549-120[37-2019/1371]-E.596266 | GVK 113 hasılat esaslı kazanç tespitinin kapsamı (avukat dışı) | https://gib.gov.tr/mevzuat/kanun/433/ozelge/24729 | yok |
| 20.04.2020 | 84098128-120[65-2019/5]-134497 | Ücretli avukatlıktan ayrılınca baro işi alacağı: arızi kazanç | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23551 | `ozelgeler/23551.txt` |
| 07.01.2020 | 57062627-010.01-357 | Envanterdeki aracın satışında SMM tutarı ve VUK 353/1 | https://gib.gov.tr/mevzuat/kanun/434/ozelge/25805 | `ozelgeler/25805.txt` |
| 19.11.2019 | 62030549-120[67-2019/293]-E.996093 | Sözleşme sonu tazminatı serbest meslek kazancı (2018, kâğıt SMM) | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23202 | `ozelgeler/23202.txt` |
| 12.09.2019 | 27575268-105[229-2017-164]-302638 | İcra dairesi adına kesilen PTT tebligat faturası gider yazılamaz | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23555 | `ozelgeler/23555.txt` |
| 28.12.2018 | 11395140-105[VUK-1-20846]-1194369 | Avukatın avukata iş vermesi: SMM, stopaj, KDV | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26372 | `ozelgeler/26372.txt` |
| 05.10.2018 | 36486581-120[38404182718]-E.38199 | Serbest meslek defteri, POS, ÖKC muafiyeti (fizyoterapist) | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26374 | `ozelgeler/26374.txt` |
| 26.01.2018 | 62030549-120[94-2017/106]-93119 | Belirlenmiş alıcıya danışmanlık niteliğindeki hizmette 9/10 (3D görselleştirme; avukat dışı) | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23562 | `ozelgeler/23562.txt` |
| 16.11.2017 | B.07.1.GİB.4.07.17.02-105[Mük.257.VUK.ÖZ.14.39]-188100 | İlam vekalet ücretinde SMM kime; GVK 96 (brüte iblağ) metni; 375 Sıra No.lu VUK GT (eskimiş kısım) | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23504 | `ozelgeler/23504.txt` |
| 13.11.2017 | B.07.1.GİB.4.06.18.02-105[236-2015-369]-447207 | 7194 öncesi vekalet ücreti belge düzeni (eskimiş kısım) | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23505 | `ozelgeler/23505.txt` |
| 07.08.2017 | 11395140-105[VUK-1-20574]-237669 | SMM'de matbu (hazır) imza | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26375 | `ozelgeler/26375.txt` |
| 29.03.2017 | 11395140-105[VUK-1-19829]-87103 | Başarıya bağlı ücret: tahsil anında SMM, iade, KDV | https://gib.gov.tr/mevzuat/kanun/434/ozelge/23649 | `ozelgeler/23649.txt` |
| 07.03.2017 | B.07.1.GİB.4.35.16.01-120.04.01[68-2016/3]-7601 (metinde: 84098128-120.04.01[68-2016/3]-7601) | Vekaletname pulu bedelinin gider yazılması | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23723 | `ozelgeler/23723.txt` |
| 03.11.2016 | 62030549-120[94-2015/286]-193057 | İcra dosyasından kesilen akdi ücret; gayri faal müvekkil | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23575 | `ozelgeler/23575.txt` |
| 26.05.2016 | B.07.1.GİB.4.35.16.01-120.04.06[94-2016/2]-296 | Ücretli avukat adına hükmedilen vekalet ücreti (311 öncesi; eskimiş) | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23579 | `ozelgeler/23579.txt` |
| 18.02.2016 | 50426076-130[1-2014/20-1182]-40 | Bozma kararıyla belediyeye iade edilen vekalet ücretinde KDVK 35 düzeltmesi ve tevsik | https://gib.gov.tr/mevzuat/kanun/436/ozelge/29150 | `ozelgeler/29150.txt` |
| 07.01.2016 | 62030549-120[65-2014/483]-1238 | Avukatın kendi ücret alacağının icrayla tahsili | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23585 | `ozelgeler/23585.txt` |
| 12.10.2015 | 11395140-105[236-2014/VUK-1-18834]-86114 | Alacağın temlikinde SMM asıl borçlu adına | https://gib.gov.tr/mevzuat/kanun/434/ozelge/25506 | `ozelgeler/25506.txt` |
| 04.06.2015 | 11395140-105[236-2012/VUK-1-...]-58433 | İcra takip masraflarının yansıtılması: SMM ve KDV yok | https://gib.gov.tr/mevzuat/kanun/434/ozelge/21255 | `ozelgeler/21255.txt` |
| 08.09.2014 | 39044742-130-2170 | Bankadan alınan işin (ipotek işlemleri) başka avukatlara yaptırılması; tevkifata değinmez | https://gib.gov.tr/mevzuat/kanun/436/ozelge/29253 | `ozelgeler/29253.txt` |
| 17.07.2014 | 65771276-105[MÜK257-2013/9]-15 | Veteriner: POS fişi (avukata uygulanmaz) | https://gib.gov.tr/mevzuat/kanun/443/ozelge/26384 | yok |
| 26.05.2014 | 39044742-130-1439 | Ücretli avukatın CMK görevi: büronun SMM'si; yol gideri KDV'ye tabi | https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985 | `ozelgeler/31985.txt` |
| 21.04.2014 | 64597866-105[229-2014]-57 | UYAP Avukat Portal ödemelerinin tevsiki | https://gib.gov.tr/mevzuat/kanun/434/ozelge/25620 | `ozelgeler/25620.txt` |
| 10.04.2014 | 38418978-120[65-13/9]-361 | Yetki belgesi (tevkil) ile tahsil edilen vekalet ücreti | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23597 | `ozelgeler/23597.txt` |
| 22.10.2013 | 88409335-130[9-ÖZELGE-2013-1-3]-26 | CMK müdafilik ücretinde KDV tevkifatı yok (117 Seri dönemi; eskimiş) | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30484 | `ozelgeler/30484.txt` |
| 11.10.2013 | 49327596-120[65.GVK.2013.29]-259 | Yol ve konaklama masrafları; tarife altı ücrette KDV | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23601 | `ozelgeler/23601.txt` |
| 30.09.2013 | 12436462-195.01[171]-95500 | Serbest meslek erbabında YN ÖKC zorunluluğu yok (izahat; SMMM) | https://gib.gov.tr/mevzuat/kanun/443/ozelge/38226 | `ozelgeler/38226.txt` |
| 23.08.2013 | 11395140-019.01-1319 | Tevkifatlı SMM'de tutarların gösterimi (117 Seri No.lu Tebliğ dönemi; harita mühendisi) | https://gib.gov.tr/mevzuat/kanun/434/ozelge/22146 | `ozelgeler/22146.txt` |
| 11.03.2013 | 97677631-041-2-7 | Başsavcılığa makbuz bir yıl, ödeme ertesi yıl: kazanç hesaba geçtiği yılın | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23700 | yok |
| 29.08.2012 | B.07.1.GİB.4.34.19.02-019.01-2703 | Tahsil edilmeyen kısmın SMM'si ve stopajı | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23289 | `ozelgeler/23289.txt` |
| 10.08.2012 | B.07.1.GİB.4.35.16.01-176200-743 | Dosyaların varlık şirketine temlikinde KDV'nin doğması (tarife alt sınırı); vekalet ücretinde tahsil anında SMM ve stopaj; 375 Sıra No.lu VUK GT (eskimiş kısım) | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23614 | `ozelgeler/23614.txt` |
| 20.04.2012 | B.07.1.GİB.4.38.15.01-GV-20-485-57 | İcra yoluyla vekalet ücreti, toplu ödemede tek SMM | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617 | `ozelgeler/23617.txt` |
| 06.03.2012 | B.07.1.GİB.4.20.15.01-30-MUK-2011-230-195 | Belediyeye kısmi zamanlı hizmette SMM tutarı | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26378 | `ozelgeler/26378.txt` |
| 01.03.2012 | B.07.1.GİB.4.34.16.01-KVK 6-809 | Teknopark firmasının avukata ödemesinde genel hükümlere göre stopaj | https://gib.gov.tr/mevzuat/kanun/435/ozelge/27919 | yok |
| 28.02.2012 | B.07.1.GİB.4.41.15.01-GVK-2011/24-49 | Tacir/serbest meslek erbabı müvekkilin kişisel davasında stopaj yok | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23620 | yok |
| 21.02.2012 | B.07.1.GİB.4.35.17.01-35-02-208 | Tahsil edilemeyen veya iade edilen ücrette GV ve KDV | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23574 | `ozelgeler/23574.txt` |
| 11.11.2011 | B.07.1.GİB.4.06.16.01-120[94-11/12]-987 | KDV dahil ücrette iç yüzde ve stopaj matrahı | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23630 | `ozelgeler/23630.txt` |
| 24.10.2011 | B.07.1.GİB.4.20.15.01-30-MUK-2010-39-353 | Belediye sözleşmesinde fiilen ödenen tutardan SMM | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23622 | `ozelgeler/23622.txt` |
| 16.09.2011 | B.07.1.GİB.4.06.18.02-32229--8126-740 | İcra inkar tazminatı ve faiz: MSİ, KDV dışı | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26026 | `ozelgeler/26026.txt` |
| 26.08.2011 | B.07.1.GİB.4.07.16.01-GVK.2010.162-266 | POS ile tahsilatta yalnız ücret kısmı için SMM | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23637 | `ozelgeler/23637.txt` |
| 23.08.2011 | B.07.1.GİB.4.35.16.01-176200-406 | Bozma kararıyla iade edilen vekalet ücretinin gider yazılması; 5018 kapsamındaki kurumun belgesi | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23702 | `ozelgeler/23702.txt` |
| 22.07.2011 | B.07.4.DEF.0.03.10.00-193-845-26 | Yol gideri karşılığı hasılattır, stopajlı SMM | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23644 | `ozelgeler/23644.txt` |
| 09.06.2011 | B.07.1.GİB.4.38.15.02-VUK-21-197-50 | Sigortalı avukatın sürekli CMK görevi: mükellefiyet ve SMM gerekir | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23655 | `ozelgeler/23655.txt` |
| 30.05.2011 | B.07.1.GİB.4.20.15.02-VUK-2011/2-114 | POS tahsilatında SMM kapsamı | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26381 | `ozelgeler/26381.txt` |
| 09.02.2011 | B.07.1.GİB.4.06.16.01-2010-GVK-65-9-67 | Vekalet ücretinin yarısının müvekkile bırakılması | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23660 | `ozelgeler/23660.txt` |
