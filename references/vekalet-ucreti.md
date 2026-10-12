# Vekalet ücreti: tevkifat, KDV ve belge düzeni

## Kapsam ve ilgili dosyalar
- **Kapsam:** Mahkeme veya icra dairesince karşı tarafa yükletilip avukata ödenen vekalet ücreti (ilam ve icra vekalet ücreti). Konular: %20 gelir vergisi stopajını kimin keseceği, e-SMM'nin kimin adına ve ne zaman düzenleneceği, KDV (dahil mi hariç mi, oran, 5/10 tevkifat), ücretli ve kurum avukatları, avukatlar arası paylaşım, CMK ve adli yardımla kesişen noktalar. Müvekkil ve borçlu açısından bilgiler ayrı başlıktadır (11. başlık).
- **İlgili dosyalar:** `parametreler.md` (tutar, oran, sınır ve cezalarda esas dosya), `uygulama-notlari.md` (⚖️ tartışmalı konular: §3, §4, §5, §14), `kdv.md` (KDV tevkifatı, %10 kapsamı, CMK), `aaut-2025-2026.md` (ücretin tarifeden hesabı), `rehber-590-avukat.md` (GİB Rehberi özeti), `ek-faaliyetler.md`, `smm-belge-duzeni.md`, `damga-harc.md`, `giderler.md`.
- **Hesap:** `scripts/aaut_hesap.py karsi-taraf --hukmedilen <tutar>`. Seçenekler: `--kdv 10`, `--kdv-haric`, `--odeyen-gercek-kisi`, `--kdv-tevkifat 5/10`.
- **Özelge tam metinleri:** Linkin sonundaki sayı GİB kimlik numarasıdır (ID). Tam metin `references/ozelgeler/<ID>.txt` dosyasındadır. Yerelde bulunmayanlar dosya sonundaki tabloda işaretlidir.

## Hızlı karar tablosu
"Ö-" kısaltması özelge ID'sidir; künyeler dosya sonundaki tablodadır. ⚖️ işaretli satırlarda GİB görüşü yazılmıştır; diğer görüş için `uygulama-notlari.md`'ye bakın. Tutarlar `parametreler.md` ile aynıdır.

| # | Soru | Kısa cevap | Dayanak |
|---|---|---|---|
| 1 | %20 stopajı kim keser? | **Ödeyen.** Borçlu doğrudan avukata öderse veya icraya yatırırsa borçlu keser. Borçlu müvekkile öderse müvekkil, avukata öderken keser. Ödeyen GVK 94 sorumlusu değilse (ör. ticari veya mesleki faaliyeti olmayan gerçek kişi) kesinti yapılmaz. | GVK 94/3; 311 GVGT 25/2-3; Ö-23524 |
| 2 | e-SMM kimin adına? | Doğrudan veya icra yoluyla ödemede **borçlu (davayı kaybeden)** adına. İcraya nüsha verilmez. Borçlu müvekkile ödediyse **ödeyen müvekkil** adına. Bordrolu avukat e-SMM düzenlemez; işveren bordro düzenler. | 311 GVGT 26/2-6; Ö-23524, Ö-23511 |
| 3 | Kararda "KDV hariç" yazmıyor. KDV'yi üstüne ekler miyim? | **Hayır.** Ücret KDV dahildir. KDV iç yüzdeyle ayrılır: %20'lik işte tutar / 1,20, %10'luk işte tutar / 1,10. Stopaj KDV hariç tutar üzerinden hesaplanır. | 311 GVGT 25/5; KDV GUT I/B-4 |
| 4 | Hangi KDV oranı? | Genel oran **%20**. Şu işlerde **%10**: aile, tüketici ve çocuk mahkemesi işleri, vesayet, adli yardım, iş uyuşmazlığında dava şartı arabuluculuk, bunların kanun yolları ve ilamlı icrası. ⚖️ İlamsız takipteki tedbir nafakasında GİB %20 görüşündedir (`uygulama-notlari.md` §4). | 2007/13033 BKK (II) 32; Ö-38775, Ö-32149 |
| 5 | Borçlu stopaj kesmedi. Ne yaparım? | Ücreti **brüt** beyan et. Mahsup edecek stopaj yoktur. Borçlu sorumluysa vergi onun adına tarh edilir. ⚖️ Kesilmeyen stopajın makbuzda gösterilip gösterilmeyeceği tartışmalıdır (`uygulama-notlari.md` §14 #5a). | 311 GVGT 25/3; Ö-23524, Ö-23511 |
| 6 | Ücret haciz, mal satışı, kefil veya tehir-i icra teminatından tahsil edildi | Stopaj **yok**. e-SMM borçlu adına ve stopajsız düzenlenir, tutar brüt beyan edilir. | 311 GVGT 25/6; Ö-23544, Ö-23519, Ö-24441, Ö-23536 |
| 7 | Borçlu banka, kamu idaresi, KİT, baro vb. ise KDV tevkifatı var mı? | ⚖️ **GİB: var.** KDV dahil bedel 2026'da **12.000 TL**'yi (2025: 9.900 TL) aşarsa **5/10** tevkifat uygulanır. Aynı davanın ilam ve icra vekalet ücretleri sınır hesabında toplanır. Tevkif edilen KDV'yi borçlu beyan eder. | KDV GUT I/C-2.1.3.2.13, 2.1.3.4.1; Ö-30232, Ö-30226, Ö-38680; `uygulama-notlari.md` §14 #17 |
| 8 | Borçlu icraya net tutarı yatırdı. Dosya kapanır mı, farkı isteyebilir miyim? | Stopajın eksik yatırılması dosyanın kapanmasına **engel değildir**. Farkın borçludan istenemeyeceği bu kuralın sonucudur (çıkarım). e-SMM brüt tutar üzerinden düzenlenir ve stopaj gösterilir. | Ö-23524, Ö-23533 |
| 9 | e-SMM'yi ne zaman düzenlerim? | Tahsilatta. Özelgeler bu anı icra dairesinin avukata ödeme (reddiyat) yaptığı an olarak alır. GVK 67 ise avukat adına icraya yatırılan parayı, avukat bundan haberdar olunca tahsil edilmiş sayar. ⚖️ Yatırma ile reddiyat farklı yıllara düşüyorsa dönemi bilinçli seç (`uygulama-notlari.md` §5). | GVK 67; Ö-20674, Ö-23519 |
| 10 | e-SMM'yi düzenlemez veya geç düzenlersem? | VUK 353/1: belge tutarının %10'u. 2026'da asgari ceza ilk tespitte **17.000 TL**'dir. Ödeyen süreyi izleyen 5 iş günü içinde bildirirse ona ceza kesilmez, avukata **üç kat** uygulanır. Stopaj makbuz olmasa da kesilir. | VUK 353/1 (7524 s.K.); VUK GT 588; Ö-23531 |

## Güncel çerçeve (Ekim 2026)
- **GVK 94/3 (7194 s.K. md.16 ile eklenen fıkra):**
  - 07.12.2019'da yürürlüğe girdi. İİK ve Avukatlık Kanunu uyarınca karşı tarafa yükletilen vekalet ücretinde (icra ve iflas müdürlüklerine yatırılanlar dahil) tevkifatı **ödeyen** yapar. İcra müdürlüğü tevkifat sorumlusu değildir.
  - AYM iptal talebini reddetti (E.2024/94, K.2025/179, 10.09.2025). AYM bilgi bankasındaki yayın tarihi 23.12.2025'tir; RG sayısı ayrıca doğrulanmadı.
  - Kural GİB Rehberi'nde de yer alır (Yayın 590, Şubat 2026, s.11; `rehber-590-avukat.md` §5).
  - GVK 94'ün son fıkralarına göre tüccar ve serbest meslek erbabının tevkifat yükümlülüğü ticari ve mesleki işleriyle ilgili ödemelerle sınırlıdır.
  - [Kanun: GVK md.94 (Ek fıkra: 5/12/2019-7194/16) — https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=193&MevzuatTur=1&MevzuatTertip=4] [AYM: E.2024/94, K.2025/179 — https://kararlarbilgibankasi.anayasa.gov.tr/kbb/pages/search/NormDenetimi?id=a2JiOjZkYWYxYWI2LTkyMTAtYTAxMC0xMTllLTUzYmEwNWNhZmVjZA&type=NormDenetimi] [Özelge (yürürlük tarihi): 07.07.2023, E-62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519]
- **Oran:** Stopaj oranı %20'dir (GVK 94/1-2-b; 2009/14592 BKK). 2026'da değişmedi; CBK 11344 (RG 19.05.2026/33258) yalnız nükleer santral istihkakları için %1'lik bir alt bent ekledi. %17'lik oran GVK 18 kapsamındaki telif işlerine aittir, vekalet ücretine uygulanmaz (`parametreler.md`).
- **311 Seri No.lu GVGT (RG 27.05.2020/31137):** md.25 tevkifatı, md.26 belge düzenini düzenler. 2020 sonrasındaki bütün özelgeler bu iki maddeye dayanır. Şubat–Ekim 2026 arasında bu maddeleri değiştiren bir tebliğ tespit edilmedi; 2026 tarihli 333, 334 ve 335 Seri No.lu GVGT'ler 311'e dokunmuyor. [Tebliğ: https://www.resmigazete.gov.tr/eskiler/2020/05/20200527-10.htm]
- **Avukatlık Kanunu md.164 (son fıkra):** Kararla tarifeye dayanılarak karşı tarafa yüklenen vekalet ücreti avukata aittir. İş sahibinin borcu nedeniyle takas ve mahsup edilemez, haczedilemez. 01.02–12.10.2026 arasında Av.K. 164, 168 ve 35/A'da değişiklik tespit edilmedi. İİK'da 7589 s.K. ile yalnız md.114 değişti; vekalet ücreti ve tevkifat hükümleri aynı kaldı (orta güven). [Kanun: 1136 s.K. md.164 — https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=1136&MevzuatTur=1&MevzuatTertip=5]
- **KDV GUT:**
  - Avukatlık ücretleri I/B-4'te düzenlenir. Seri 52 ile 31.10.2024'ten itibaren I/B-4'teki belge düzeni 311 GVGT md.26 ile aynı hale getirildi. Eski "makbuzu davayı kazanan müvekkil adına düzenle" yaklaşımı artık uygulanmaz.
  - Belirlenmiş alıcılara verilen hizmetlerde 5/10 tevkifat I/C-2.1.3.2.13'tedir.
  - I/C-2.1.3.2.2.2'ye göre yargı mercileri nezdindeki ve icra hizmetleri 9/10'luk danışmanlık tevkifatının dışında kalır.
  - Tevkifat sınırı I/C-2.1.3.4.1'dedir.
  - KDV GUT Seri 56 (RG 31.12.2025) yalnız III/B-3'teki 2026 tutarını ekledi; avukatlık tevkifatıyla ilgisi yok.
- **e-SMM:** Zorunludur (509 Sıra No.lu VUK GT). Kâğıt makbuz dönemine ait "nüsha" açıklamaları artık uygulanmaz. 589 Sıra No.lu VUK GT yalnız e-Arşiv zorunluluğunu basit usul ve işletme esası mükellefleri için erteledi; e-SMM'ye etkisi yok.
- **Ceza rejimi:** VUK 353/1, 7524 s.K. ile 02.08.2024'ten itibaren değişti (ayrıntı 4. başlıkta, tutarlar `parametreler.md`'de).
- **Usul notu (vergi dışı; 7589 s.K., RG 31.07.2026/33326, 31.07.2026'dan itibaren):**
  - Bölge adliye mahkemesinin yeniden esas hakkında verdiği karar temyiz sınırının altındaysa ve yalnız yargılama gideri veya vekalet ücretine ilişkinse temyiz edilemez (HMK 362/3-b).
  - Yalnız vekalet ücreti ve yargılama giderine ilişkin bölge idare mahkemesi kararları temyiz edilemez (İYUK 46/2-f). Bu değişiklik yürürlükten sonra verilen kararlara uygulanır.
  - Kanunda vergi hükmü yok.
  - [Kanun: 7589 s.K. md.4-6, 10, 19-20, 25 ve geçici md.1 — https://www.resmigazete.gov.tr/eskiler/2026/07/20260731-1.htm]
- **Özelgelerin bağlayıcılığı:**
  - Özelgeler VUK 413'e dayanır ve yalnız talep edeni bağlar. Özelgeye uygun işlem yapan talep sahibine ceza kesilmez, gecikme faizi hesaplanmaz.
  - Aşağıdaki kurallar özelgelerdeki ortak eğilimin özetidir.
  - 7194 s.K. ve 311 GVGT öncesine ait özelgeler 311 GVGT md.25-26 ile çatışıyorsa esas alınmaz (12. başlık).
  - Olayınız farklıysa ya da görüşler çelişiyorsa kendi adınıza özelge isteyin.

## Omurga özelge: Bursa VDB, 17.10.2022 (ID 23524)
- **Künye:**
  - Bursa Vergi Dairesi Başkanlığı, 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464.
  - Konu: avukatlara ödenen vekalet ücretlerinin vergilendirilmesi ve belge düzeni. Talep eden bir avukattır.
  - GİB sisteminde GVK (193) altında kayıtlıdır: https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524. Kullanıcının paylaştığı `/kanun/434/ozelge/23524` bağlantısı da aynı metne gider.
  - Yerel metin: `references/ozelgeler/23524.txt`.
- **İlgili mevzuat:** GVK md.65, 94/1-2-b, 94/3; VUK md.236, 413; 311 Seri No.lu GVGT md.25-26.
- **Olay:** Avukat, müvekkilleri adına işverenlere karşı açtığı davalarda karşı taraftan mahkeme kararıyla vekalet ücreti tahsil ediyor. Davayı kaybeden taraf tevkifat yükümlüsü olduğu halde tevkifat yapmıyor. Tevkifatın nasıl yapılacağı soruluyor.
- **Değerlendirme (özet):**
  - Avukata ödenen vekalet ücreti serbest meslek kazancıdır (GVK 65) ve %20 tevkifata tabidir (GVK 94/1-2-b).
  - Tevkifatı kimin yapacağını 311 GVGT 25/2 belirler:
    - (a) Borçlu doğrudan avukata öderse borçlu.
    - (b) Borçlu avukata ödenmek üzere icra ve iflas müdürlüğüne yatırırsa borçlu.
    - (c) Borçlu alacaklıya (davayı kazanana) öderse alacaklı, avukata öderken.
  - GVK 94/1'de sayılmayanların ödemesinden tevkifat yapılmaz (25/3). Ücretli avukatın işverenine yapılan ödemeden de tevkifat yapılmaz; işveren avukata öderken ücret hükümlerine göre keser (25/4).
  - Kararda "KDV hariç" ifadesi yoksa ücret KDV dahil kabul edilir. KDV iç yüzdeyle hesaplanıp makbuzda gösterilir; stopaj KDV hariç tutar üzerinden yapılır (25/5).
  - Doğrudan veya icra yoluyla ödemede SMM borçlu adına düzenlenir; icra müdürlüğüne nüsha verilmez (26/2-3).
  - İcraya yatırılan ücretten tevkifat yapılması GVK 94'ün amir hükmüdür. %20'lik tevkifat tutarının eksik yatırılması icra dosyasının kapanmasına engel değildir; Adalet Bakanlığı bunu teşkilatına duyurmuştur. Duyurunun tarih ve sayısı özelgede yoktur.
- **Sonuç:**
  - Doğrudan veya icra yoluyla ödenen ücret için avukat borçlu adına SMM düzenler ve tevkifat tutarını makbuzda gösterir.
  - Sorumlu tevkifat yapmazsa onun adına VUK hükümlerine göre tarhiyat yapılır. Avukat ücreti brüt olarak kazancına katar; mahsup edeceği tutar olmaz.
- Aynı görüş 31.07.2024 tarihli İstanbul VDB özelgesinde (ID 23511) aynen tekrarlanmıştır.
- [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524] [Özelge: 31.07.2024, E-62030549-120-1020639 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511]

## 1. Özet tablo: tevkifatı kim yapar, e-SMM kimin adına düzenlenir
Ayrıntı ve kaynaklar aşağıdaki maddelerdedir.

| Ödeme şekli | %20 GV tevkifatı | e-SMM kimin adına | Dayanak |
|---|---|---|---|
| Borçlu (GVK 94 sorumlusu) doğrudan avukata öder | Borçlu, ödeme anında | Borçlu (davayı kaybeden) | 311 GVGT 25/2-a, 26/2; Ö-23524 |
| Borçlu, avukata ödenmek üzere icraya yatırır | Borçlu, yatırma anında; icraya net tutarı yatırır | Borçlu; icraya nüsha verilmez | 25/2-b, 26/3; Ö-23524, Ö-23511 |
| Borçlu icraya yatırır, para icradan müvekkilin veya kurumun hesabına geçer, o da avukata aktarır | Borçlu keser. Borçlu kestiyse aktaran yeniden kesmez. Kesmediyse (ör. tevkifat yükümlüsü olmayan borçlu) aktaran şirket keser | Borçlu (2024 görüşü) | Ö-23151, Ö-23530 |
| Borçlu, icraya uğramadan doğrudan müvekkile (davayı kazanana) öder | Borçlu kesmez. Müvekkil GVK 94 sorumlusuysa avukata öderken keser | Ödeyen müvekkil. Müvekkil mükellefse 7 gün içinde borçlu adına fatura vb. belge düzenler. Bu belgede KDV hesaplanmayacağı GUT I/B-4'ten çıkarılır (açık soru, 13. başlık) | 25/2-c, 26/4-5; Ö-23533, Ö-23531 |
| Borçlu GVK 94'te sayılmıyor (ticari veya mesleki faaliyeti olmayan gerçek kişi) | Tevkifat yok; avukat brüt tutarı beyan eder | Borçlu | 25/3; Ö-23625, Ö-23617 |
| Haciz: mal satışı; banka hesabına, maaşa veya kıdem tazminatına haciz; kefilden tahsil | Tevkifat yok; avukat brüt tutarı beyan eder | Borçlu | 25/6; Ö-23544, Ö-23519, Ö-24441 |
| Tehir-i icra teminatından ödeme | Tevkifat yok (teminat yatırılırken de yok) | Borçlu | 25/6; Ö-23536 |
| Üçüncü kişi, borçlu adına icraya yatırır | Borçlu, yatırma tarihinde | Borçlu | Ö-23511 |
| Avukat, alacaklının ücretli (bordrolu) çalışanı | Borçlu bilgilendirilirse kesmez; işveren ücret olarak keser | e-SMM düzenlenmez; ücret bordrosu düzenlenir | 25/4, 26/6; Ö-24440, Ö-23533 |

## 2. Gelir vergisi tevkifatı: oran, matrah ve uygulama
- **Oran ve matrah:**
  - Oran %20'dir (2009/14592 BKK; 2026'da değişmedi).
  - Kararda "KDV hariç" ibaresi yoksa ücret KDV dahil sayılır. Önce KDV iç yüzdeyle ayrılır, %20 tevkifat kalan KDV hariç tutar üzerinden hesaplanır (311 GVGT 25/5).
  - %10 oranlı işlerde böleni 1,10 almak bu kurallardan türetilen bir sonuçtur; metinde açıkça geçmez.
  - [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524] [Özelge: 09.02.2011, B.07.1.GİB.4.06.16.01-2010-GVK-65-12-70 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23658]
- **Eksik yatırma:**
  - Borçlu icraya tevkifat düşülmüş net tutarı yatırır. Tutarın %20'lik tevkifat kadar eksik yatırılması icra dosyasının kapanmasına engel değildir; Adalet Bakanlığı bunu teşkilatına duyurmuştur.
  - 311 GVGT'deki örnek de aynıdır: belediye, vekalet ücretini avukata ödenmek üzere icraya yatırırken %20 tevkifatı yapıp muhtasarla öder ve icraya kalan tutarı yatırır. Avukat belediye adına SMM düzenler.
  - "Avukat stopaj farkını borçludan isteyemez" sonucu özelgelerde yazmaz; bu kuraldan çıkarılır.
  - [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524] [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533] [Özelge: 24.08.2011, B.07.1.GİB.4.34.16.01-GVK 94-1399 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23639] [Tebliğ: 311 GVGT md.25-26 örneği — https://www.resmigazete.gov.tr/eskiler/2020/05/20200527-10.htm]
- **Belirsizlik:**
  - Borçlu, icraya yatırdığı paranın avukata mı alacaklıya mı ödeneceğini bilmiyorsa tevkifat yapar. Avukatın alacaklının ücretli çalışanı olduğu borçluya bildirilirse borçlu tevkifat yapmayabilir.
  - Tebliğin 25/4. fıkrası yalnız ilk kuralı (ücretli avukatın işverenine ödemede tevkifat yapılmaz) içerir. "Bilinmiyorsa kes" ve "bildirilirse kesmeyebilir" cümleleri özelgeden gelir.
  - Yersiz kesilen vergi için alacaklı kurum "bağlı bulunan vergi dairesi müdürlüğüne" düzeltme talebinde bulunarak iade isteyebilir. Özelgeler hangi dairenin kastedildiğini açık söylemez. Stopaj borçlunun dairesine ödendiğinden başvurulacak daireyi teyit edin.
  - [Özelge: 19.03.2021, 38418978-120[94-20/27-İ]-101240 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/24440] [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533]
- **Sorumlu tevkifat yapmazsa:**
  - Sorumlu adına tarhiyat yapılır. Avukat ücreti brüt olarak kazancına katar; mahsup edebileceği bir stopaj olmaz.
  - Stopajı kesilmemiş ücrette stopaj mahsup edilmez. Kayıtlarda görünmeyen stopaj, iade ve mahsup kontrolünde uyuşmazlık çıkarır (`uygulama-notlari.md` §14 #5).
  - ⚖️ **Makbuzda gösterim:** GİB özelgeleri makbuzun fiili kesintiye göre düzenlenmesini öngörür. Haciz hallerinde "tevkifatsız SMM" denir ve 2011 tarihli özelge makbuzun borçlunun kesinti yapıp yapmadığı bilgisine göre düzenleneceğini söyler. 23524'teki "makbuzda tevkifat tutarını da gösterin" ifadesi tevkifatın yapıldığı olağan durum içindir. Uygulamada iki yol vardır; ayrıntı için `uygulama-notlari.md` §14 #5a. Hangisi seçilirse seçilsin, açıklamaya "GVK 94/3 uyarınca yapılması gereken tevkifat borçluca yapılmamıştır" yaz ve stopajı mahsup etme.
  - [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524] [Özelge: 31.07.2024, E-62030549-120-1020639 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511] [Özelge: 19.08.2011, B.07.1.GİB.4.34.16.01-GVK 94-1349 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23641]
- **Borçlu net ödeyip kestiği stopajı beyan etmediyse (açık soru):**
  - 23524 ve 23511 yalnız hiç kesinti yapılmayan durumu cevaplar.
  - Rehbere göre nakden iadede kesintinin sorumlu adına tahakkuk ettiğini gösteren belge aranır. 2026'da 426.000 TL'ye kadar bilgiler YBS'den görülebiliyorsa bu belge istenmez (Yayın 590 s.26; `rehber-590-avukat.md` §16).
  - İcra dosyasındaki net ödeme kaydını ve e-SMM'yi sakla, gerekirse vergi dairesine bildir. Bu senaryoya ilişkin özelge bulunamadı.
- **Stopajın ödenip ödenmediği:** Ücret icradan reddiyat makbuzuyla, tevkifat düşülerek ödendiyse avukat, kesilen verginin sorumluca vergi dairesine ödenip ödenmediğini takip etmek zorunda değildir. Ödenmemesinden de sorumlu tutulmaz. Özelge 2011 tarihlidir, ancak ilke güncel kuralla uyumludur. [Özelge: 17.11.2011, B.07.1.GİB.4.34.16.01-GVK 94-2032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23625]
- **Tevkifat yükümlüsü olmayan borçlu:**
  - GVK 94'te sayılmayan borçlunun ödemesinden tevkifat yapılmaz. Avukat tutarı geçici vergi dönemlerinde ve yıllık beyannamede beyan eder. e-SMM yine borçlu adına düzenlenir (26/2-3).
  - Dikkat: GVK 94'ün son fıkralarına göre gerçek kişi tacir ve serbest meslek erbabının tevkifat yükümlülüğü ticari veya mesleki işleriyle ilgili ödemelerle sınırlıdır. İşle ilgisiz bir davada bu kişilerin tevkifat yapmaması savunulabilir; bu ayrıma doğrudan değinen bir özelge bulunamadı. Tersinden, borç ticari veya mesleki işiyle ilgiliyse gerçek kişi tacir de tevkifat yapar.
  - Aynı ölçüt müvekkil üzerinden ödemede de geçerlidir: "müvekkil gerçek kişiyse stopaj yok" kuralı ancak müvekkil GVK 94 kapsamı dışındaysa doğrudur.
  - [Özelge: 17.11.2011, B.07.1.GİB.4.34.16.01-GVK 94-2032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23625] [Özelge: 20.04.2012, B.07.1.GİB.4.38.15.01-GV-20-485-57 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617] [Tebliğ: 311 GVGT 25/3]
- **e-SMM sorunları tevkifatı etkilemez:**
  - e-SMM'nin hiç düzenlenmemesi, hatalı ya da geç düzenlenmesi veya avukatın düzenlemekten kaçınması tevkifatı değiştirmez.
  - Ödeyen, karşı taraf vekalet ücreti stopajını muhtasar beyannamede (bugün muhtasar ve prim hizmet beyannamesi) makbuz bilgisi girmeden beyan edebilir.
  - Ödeyen, makbuz düzenlemeyen avukatı vergi dairesine bildirebilir; avukata VUK ceza hükümleri uygulanır (4. başlık).
  - [Özelge: 17.06.2022, E-62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Özelge: 06.06.2022, 27523430-200.03.01[2950368442]-35929 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/20674] [Özelge: 07.07.2023, E-62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519]
- **Ödeyen açısından dönem:**
  - Stopaj, ödemenin nakden veya hesaben yapıldığı (icraya yatırıldığı) ayın muhtasarıyla beyan edilir.
  - 2012 tarihli özelgeye göre makbuz da ödemenin yapıldığı tarihte düzenlenmeli ve stopaj makbuzda gösterilmelidir. İdarenin iç onay süreci için makbuzun önceden istenmesi bu tarihi değiştirmez.
  - Özelgedeki "ertesi ayın 23'ü" süresi eskimiştir. Bugün beyan ve ödeme ertesi ayın 26'sına kadar yapılır (`parametreler.md`).
  - [Özelge: 13.09.2012, B.07.1.GİB.4.34.16.01-120[98-2012/254]-2776 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/24499] [Özelge: 31.07.2024, E-62030549-120-1020639 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511]
- **Net ücret anlaşması (brüte iblağ):** Kesilmesi gereken vergiyi ödeyen üstlenirse vergi, fiilen ödenen tutar ile üstlenilen verginin toplamı üzerinden hesaplanır (GVK 96). [Özelge: 16.11.2017, B.07.1.GİB.4.07.17.02-105[Mük.257.VUK.ÖZ.14.39]-188100 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23504]
- **İstisnalar stopajı etkilemez:** Genç girişimci istisnasından (GVK mük. 20; 2026'da 400.000 TL, 2025'te 330.000 TL) yararlanan avukattan da borçlu %20 stopaj keser. Kesilen stopajın mahsup ve iadesi için `uygulama-notlari.md` §9 ve §12 ile `parametreler.md`'ye bakın.

## 3. İcra yoluyla tahsilde özel durumlar
- **Haciz yoluyla tahsil:**
  - Ücret, borçlunun malları satılarak ya da üçüncü kişilerdeki hak ve alacakları haczedilerek tahsil edilirse borçlu tevkifat yapmaz.
  - Banka hesabına haciz ihbarnamesiyle yapılan tahsil ve işverenin kıdem tazminatından kesip icraya aktarması da bu kapsamdadır.
  - Avukat borçlu adına tevkifatsız e-SMM düzenler ve tutarı geçici vergi ve yıllık beyannamede beyan eder (311 GVGT 25/6).
  - [Özelge: 26.10.2020, 27575268-105[236-2020-472]-E.280399 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23544] [Özelge: 07.07.2023, E-62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519] [Özelge: 30.12.2020, 84098128-120.04.06[94-2020/6]-E.389388 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/24441]
- **Üçüncü kişinin borçlu adına ödemesi:**
  - Haciz durumundan ayrıdır. Üçüncü kişiler ücreti borçlu şirket adına icraya yatırırsa tevkifatı yatırma tarihinde borçlu yapar ve e-SMM borçlu adına düzenlenir.
  - Ölçüt şudur: ödeme borçlu adına (lehine) mi yapılmıştır, yoksa para cebri icra veya kefil yoluyla mı tahsil edilmiştir?
  - Kanunen masrafları üstlenen şirket (ör. kamulaştırmada lisans sahibi) icraya yatırırsa, 2013 tarihli özelgeye göre tevkifatı bu şirket yapar ve e-SMM onun adına düzenlenir.
  - [Özelge: 31.07.2024, E-62030549-120-1020639 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511] [Özelge: 26.10.2020, 27575268-105[236-2020-472]-E.280399 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23544] [Özelge: 11.03.2013, 62030549-120[94-2012/280]-374 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/22455]
- **Tehir-i icra:**
  - Vekalet ücreti dahil borç için teminat yatırılırken nakden veya hesaben ödeme olmadığından tevkifat yapılmaz.
  - İstinaf veya temyiz reddedilir ve ücret teminattan avukata ödenirse yine tevkifat yapılmaz; avukat borçlu adına e-SMM düzenleyip tutarı brüt beyan eder.
  - Karar kesinleştikten sonra borçlu ücreti dosyaya ayrıca yatırırsa tevkifat yapar.
  - [Özelge: 12.03.2021, 64597866-120-4566 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23536]
- **Para icradan müvekkil veya kurum hesabına geçerse (avukatın ahzu kabz yetkisi yoksa):**
  - Tevkifat yükümlüsü yine borçludur; paranın icradan kim tarafından çekildiği önemli değildir.
  - Borçlu tevkifat yaptıysa aktaran şirket avukata öderken yeniden kesmez. Yapmadıysa (ör. tevkifat yükümlüsü olmayan borçlu) aktaran şirket %20 keser.
  - e-SMM borçlu adına düzenlenir.
  - Açık nokta: tevkifatı aktaran şirket yaptığında e-SMM'nin kimin adına düzenleneceği özelgelerde açıkça yanıtlanmamıştır.
  - [Özelge: 17.01.2024, E-13649056-125[2020-ÖZE-06]-5526 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23151] [Özelge: 02.09.2022, 62030549-120[94-2019/473]-978373 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23530] [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533]
- **Kurumun ücretten sözleşmeyle pay alması (SGK'da %70 / %30 örneği):**
  - Hizmet akdi olmadan vekalet akdiyle çalışan avukat serbest meslek erbabıdır.
  - Borçlu, icraya yatırdığı ücretin tamamından tevkifat yapar ve avukat bu ödeme için makbuz düzenler.
  - Kurumun avukata aktardığı pay vekalet ücreti ödemesi sayılmaz ve yeniden tevkifata tabi değildir.
  - Kurumda kalan pay, kurumdan alınacak belgeyle GVK 68/1'e göre gider yazılabilir. Özel sözleşmeler vergi dairesini bağlamaz (VUK 8).
  - [Özelge: 30.09.2013, B.07.1.GİB.4.06.16.01-120[94-13/14]-1083 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23260]
- **Ücretin bir kısmının sözleşmeyle müvekkile bırakılması (protokollü banka örneği):**
  - Avukat, hükmedilecek ücretin yarısını bankaya bırakmayı sözleşmeyle kabul etmiş olsa da ücretin tamamı avukatın hasılatıdır. SMM tutarın tamamı üzerinden ödeyen adına düzenlenir.
  - Bankaya bırakılan kısım, bankanın VUK'a göre düzenleyeceği geçerli belgeyle GVK 68/1 uyarınca gider yazılabilir. VUK 8/3 uyarınca özel sözleşmeler vergi dairesini bağlamaz.
  - Özelge 2011 tarihlidir; dayanak hükümler değişmedi.
  - [Özelge: 09.02.2011, B.07.1.GİB.4.06.16.01-2010-GVK-65-9-67 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23660]

## 4. Belge düzeni (e-SMM)
- **Doğrudan veya icra yoluyla ödeme:** e-SMM borçlu (davayı kaybeden) adına düzenlenir. Tevkifat ve KDV makbuzda gösterilir. Makbuzun bir nüshasının icra dairesine verilmesi gerekmez (311 GVGT 26/3). e-SMM'nin alıcı alanına müvekkil değil borçlu yazılır. [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524] [Özelge: 31.07.2024, E-62030549-120-1020639 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511] [Özelge: 06.06.2022, 27523430-200.03.01[2950368442]-35929 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/20674]
- **Müvekkil üzerinden ödeme:**
  - Borçlu ücreti müvekkile öderse avukat e-SMM'yi ödemeyi yapan müvekkil adına düzenler.
  - Müvekkil gelir veya kurumlar vergisi mükellefiyse, aldığı ücret için 7 gün içinde borçlu adına fatura vb. belge düzenler (müvekkile bilgi: 11. başlık).
  - Avukat müvekkilin ücretli çalışanıysa ödeme ücret bordrosuyla yapılır (311 GVGT 26/4-6).
  - [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533] [Özelge: 17.06.2022, E-62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Özelge: 07.07.2023, E-62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519] [Özelge: 16.11.2017, B.07.1.GİB.4.07.17.02-105[Mük.257.VUK.ÖZ.14.39]-188100 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23504]
- **KDV GUT ile 311 GVGT arasındaki eski fark:** KDV GUT I/B-4'ün eski metni (2016 tarihli özelgede aktarılan hali) avukatın davayı kazanana SMM düzenleyeceğini söylüyordu. Seri 52 ile bu kısım 311 GVGT 26 ile uyumlu hale getirildi. Belge düzeninde her durumda daha yeni ve özel olan 311 GVGT 26 esas alınır. [Özelge: 07.01.2016, B.07.1.GİB.4.34.16.01-120[65-2014/483]-1238 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23585]
- **Zaman:**
  - e-SMM, tahsilat anında ve tahsil edilen tutar üzerinden düzenlenir. Tahsil günü düzenle; sonraki günlere bırakmak, aynı ay içinde de olsa VUK 353 riski taşır (⚖️ `uygulama-notlari.md` §5).
  - Özelgeler icra yoluyla ödemede bu anı, icra dairesinin avukata ödeme (reddiyat) yaptığı an olarak alır.
  - GVK 67 ise serbest meslek erbabı adına icra dairesine yatırılan parayı, avukatın bundan haberdar olması (ıttıla) kaydıyla tahsil hükmünde sayar. GİB Rehberi de bu kuralı tekrarlar (`rehber-590-avukat.md` §2). 2023 tarihli özelge bu hükmü aktarmış, ancak sonuçta ayrıca uygulamamıştır.
  - ⚖️ Yatırma ile reddiyat farklı yıllara düşüyorsa iki ölçüt farklı sonuç verebilir. Dönemi bilinçli belirleyin ve gerekirse özelge isteyin. TBB eğitimindeki "UYAP'ta görünce tahsil sayılır" yaklaşımı için `uygulama-notlari.md` §5.
  - [Özelge: 09.06.2022, E-64597866-130-9597 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30226] [Özelge: 06.06.2022, 27523430-200.03.01[2950368442]-35929 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/20674] [Özelge: 17.06.2022, E-62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Özelge: 07.07.2023, E-62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519]
- **Aynı borçludan birden çok dosya veya kalem:**
  - Aynı anda yapılan tahsilat için her hizmete (ör. ilam ve icra vekalet ücreti) ayrı e-SMM düzenlenebilir. Hizmetleri dosya numarasıyla ayrı ayrı gösteren tek bir e-SMM de olur.
  - Aynı işlem veya hizmet için aynı anda yapılan tahsilata birden fazla makbuz düzenlenemez.
  - [Özelge: 09.06.2022, E-64597866-130-9597 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30226] [Özelge: 20.04.2012, B.07.1.GİB.4.38.15.01-GV-20-485-57 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617]
- **Farklı borçlular:** Her borçlu adına ayrı e-SMM düzenlenir. Kurum, icradan aldığı ücretleri avukata toplu aktarsa da bu değişmez. Kurumun sözleşmeye dayanarak kendisinin ödediği ücret ise karşı taraf vekalet ücreti değildir; bunun için kurum adına toplu makbuz düzenlenebilir. [Özelge: 01.06.2011, B.07.1.GİB.4.06.18.02-32236-8007-328 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26380] [Özelge: 17.01.2024, E-13649056-125[2020-ÖZE-06]-5526 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23151]
- **Müvekkilden ücret alınmıyorsa:** Müvekkile e-SMM düzenlenmez (ör. sendika üyesi işçiler). Karşı taraftan alınan ücret için ödeyen adına makbuz düzenlenir. [Özelge: 09.11.2017, B.07.1.GİB.4.07.16.01-120.04[GVK.ÖZ.2016.34]-181943 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23217]
- **Yargılama giderleri:** Müvekkile iade edilmek üzere tahsil edilen yargılama giderleri kazanç sayılmaz (GVK 67). Bunlardan tevkifat yapılmaz ve e-SMM düzenlenmez. Gider avukatta kalırsa kazanca eklenir ve müvekkil adına e-SMM düzenlenir. [Özelge: 29.08.2022, 48816587-120[2019]-60836 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23697]
- **Beraat vekalet ücreti:**
  - Hazine aleyhine hükmedilen ücret, kararda "sanığa verilmesine" denmiş olsa da avukatın serbest meslek kazancıdır ve tutarın tamamı için e-SMM düzenlenir. Özelge 2012 tarihlidir.
  - Ödeyen kamu idaresi (uygulamada Cumhuriyet başsavcılığı; `uygulama-notlari.md` §5) %20 tevkifat yapar.
  - Belge 5018 sayılı Kanunun cetvelindeki bir idare adına düzenlendiğinden, KDV dahil bedel sınırı aşarsa 5/10 KDV tevkifatı da gündeme gelir; 2022 tarihli özelgedeki kamu borçlu mantığı burada da uygulanır.
  - [Özelge: 06.12.2012, 53445970-105-[236-2012-27-15]-128 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/26366] [Özelge: 06.06.2022, E-36062021-130[09-2021/ÖZE-40]-50290 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232]
- **Damga vergisi:** Kamu kurumunun mahkeme kararıyla karşı taraf avukatına ödediği vekalet ücreti mal veya hizmet alımı değildir. DVK (1) sayılı tablo IV/1-a uygulanmaz, damga vergisi kesilmez. Kesildiyse düzeltme veya iade istenebilir (`uygulama-notlari.md` §14 #16; `damga-harc.md`). CMK ödemelerindeki damga vergisi tartışmalıdır (10. başlık). [Özelge: 08.04.2022, 97895701-155[2021/251]-389396 — https://gib.gov.tr/mevzuat/kanun/438/ozelge/34278]
- **Ceza (VUK 353/1; 7524 s.K. ile 02.08.2024'ten itibaren):**
  - e-SMM'yi düzenlememek veya geç düzenlemek özel usulsüzlük cezası gerektirir. Ceza belge tutarının %10'udur.
  - Asgari tutar bir takvim yılındaki ilk tespitte kanundaki tutardır; sonraki tespitlerde VUK'a bağlı 2 sayılı cetveldeki artan tutarlardır. 2026 tutarları: ilk tespit 17.000 TL; sonrakiler 35.000 / 53.000 / 70.000 / 87.000 / 170.000 TL; yıllık üst sınır 17.000.000 TL (VUK GT 588; `parametreler.md`).
  - Belgeyi almak zorunda olan ödeyen, durumu idare öğrenmeden önce ve belgenin düzenlenmesi gereken süreyi izleyen 5 iş günü içinde vergi dairesine bildirirse kendisine ceza kesilmez. Makbuzu düzenlemeyen avukata ise ceza üç kat uygulanır.
  - Özelgelerdeki eski tutarlar (380 TL vb.) geçersizdir. Özelgeler de ödeyenin makbuz düzenlemeyen avukatı bildirmesini ister.
  - Alıcı VUK 232'de sayılmayan biri (ör. tacir olmayan gerçek kişi borçlu veya müvekkil) ise VUK 353/3 uygulanır (11. başlık).
  - [Özelge: 07.07.2023, E-62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519] [Özelge: 17.06.2022, E-62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Kanun: VUK md.353 (7524 s.K. ile değişik); VUK GT 588 (RG 31.12.2025/33124 5. Mük.)]

## 5. KDV: dahil mi hariç mi, oran ve KDV tevkifatı
- **KDV'ye tabiiyet:**
  - Serbest avukatın karşı taraftan aldığı vekalet ücreti serbest meslek faaliyeti olarak KDV'ye tabidir. Avukat, hükmolunan ücret üzerinden KDV hesaplar.
  - KDVK 27/5'e göre meslek kuruluşunca belirlenmiş tarife varsa hizmet bedeli tarifedeki ücretten düşük olamaz. Özelgeler bu hükmü, avukatın karşı taraftan tahsil ettikleri dahil bütün gelirlerinin KDV'ye tabi olduğu sonucuyla birlikte anar (KDV matrahının alt sınırı için `uygulama-notlari.md` §3).
  - [Özelge: 06.06.2022, 27523430-200.03.01[2950368442]-35929 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/20674] [Özelge: 13.11.2017, B.07.1.GİB.4.06.18.02-105[236-2015-369]-447207 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23505] [Özelge: 24.11.2011, B.07.1.GİB.4.22.15.01-2010/KDV-13-2-30 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/29609] [Özelge: 28.12.2018, 11395140-105[VUK-1-20846]-1194369 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26372] [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985]
- **KDV dahil kabulü:** Kararda "KDV hariç" ifadesi yoksa ücret KDV dahil kabul edilir; KDV iç yüzdeyle hesaplanıp e-SMM'de gösterilir (KDV GUT I/B-4; 311 GVGT 25/5). Kararda "KDV hariç" yazıyorsa KDV hükmedilen tutarın üzerine eklenir. [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524] [Özelge: 01.12.2020, 27523430-130[1-2019/324]-E.51656 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/24709]
- **Oran:**
  - Genel oran 10.07.2023'ten itibaren %20'dir (öncesinde %18); iç yüzde 20/120'dir.
  - %10 indirimli oran, 2007/13033 BKK (II) sayılı listenin 32. sırasına dayanır ve şu işlerde uygulanır: adli yardım ve adli müzaharet; aile, tüketici ve çocuk mahkemelerinin görev alanı; vesayet; bunlara bağlı kanun yolları; iş uyuşmazlığında dava şartı arabuluculuk ve bunlara bağlı ilamlı icra. İç yüzde 10/110'dur.
  - Oranın tarihçesi kaleme göre değişir:
    - Mahkeme, vesayet, kanun yolu, arabuluculuk ve ilamlı icra kalemleri: 02.10.2019'dan itibaren %8 (1594 sayılı CBK), öncesinde %18.
    - Adli yardım ve adli müzaharet: 01.12.2021'den itibaren %8 (4862 sayılı CBK), öncesinde %18.
    - Bütün kalemler 10.07.2023'ten itibaren %10'dur (7346 sayılı CBK, RG 07.07.2023/32241).
  - Çocuk mahkemesinin görev alanındaki işlerde soruşturma evresindeki avukatlık hizmeti de indirimli orana girer.
  - Adli yardımlı davanın ilamlı icrasında takdir edilen icra vekalet ücreti de %10'dur.
  - ⚖️ Sınır durumlar (tüketici hakem heyeti, ilamsız takipteki tedbir nafakası, özel vekil sıfatıyla adli yardım): GİB görüşü %20'dir; karşı görüş için `uygulama-notlari.md` §4 ve `kdv.md` §8.
  - [Özelge: 02.07.2025, E-84974990-130[KDV-2/İ/28-2025/75]-365183 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/38775] [Özelge: 16.02.2022, E-62902401-130[2020-701-75]-22832 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/32149]
- **5/10 KDV tevkifatı:**
  - Borçlu KDV GUT I/C-2.1.3.2.13'te sayılan belirlenmiş alıcılardansa, onun adına düzenlenen karşı taraf vekalet ücreti makbuzunda 5/10 KDV tevkifatı uygulanır.
  - Güncel metne göre bu alıcılar şunlardır: 5018 sayılı Kanun cetvellerindeki idareler, kanun veya CBK ile kurulan kamu kurumları, kamu iktisadi teşebbüsleri (KİT'ler; Seri 50 ile 01.03.2024'ten itibaren eklendi), döner sermayeli kuruluşlar, kamu kurumu niteliğindeki meslek kuruluşları (baro dahil), bankalar, sigorta, reasürans ve emeklilik şirketleri, emekli ve yardım sandıkları ile kalkınma ajansları.
  - "Kanunla veya CBK ile kurulan" ifadesi, kendine özgü kuruluş kanunu veya kararnamesi olan kurumları kapsar. Genel bir kanuna dayanılarak kurulan kurum (ör. özel kuruluş kanunu bulunmayan bir su ve kanalizasyon idaresi) listede değildir ve tevkifat yapmaz. Liste dışındaki alıcıya (ör. özel şirket) kesilen makbuzda KDV tevkifatı yoktur.
  - Avukat, hizmeti kamuya değil müvekkiline verdiğini ileri sürmüştü; 2022 tarihli özelge buna rağmen tevkifat uygulanacağını belirtmiştir. Uygulama 01.03.2021'den beri geçerlidir.
  - Dava ve icra hizmetleri 9/10'luk danışmanlık tevkifatının kapsamında değildir (I/C-2.1.3.2.2.2). Hukuki danışmanlıkta belirlenmiş alıcılar 9/10 uygular (I/C-2.1.3.2.2); avukatlık ve danışmanlık aynı sözleşmede ayrı ücretlendirilmemişse toplam bedel üzerinden tevkifat yapılır. Ayrıntı `kdv.md`.
  - ⚖️ "Vekalet ücreti yargılama gideridir, KDV tevkifatı yapılmaz" görüşü GİB'in yerleşik özelgeleriyle çelişir. GİB görüşü: uygulanır (`uygulama-notlari.md` §14 #17).
  - [Özelge: 06.06.2022, E-36062021-130[09-2021/ÖZE-40]-50290 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232] [Özelge: 05.05.2025, E-84974990-130[KDV-2/İ/9-2025/26]-245593 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/38680] [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533] [Özelge: 11.11.2021, 20811645-130[21-415-30]-72187 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30251]
- **Tevkifat sınırı:**
  - Sınır KDV dahil bedele ve işlem bazında uygulanır. Bedel sınırı aşarsa tevkifat tutarın tamamı üzerinden yapılır. Bütünlük arz eden bedel parçalara bölünemez.
  - Aynı davaya ait ilam ve icra vekalet ücretleri sınır hesabında toplanır.
  - Birbiriyle bağlantısız ayrı dosyalarda sınır, ödeme toplu yapılsa da dosya bazında uygulanır. Bu görüş arabuluculuk makbuzları için verilmiştir.
  - Güncel tebliğ metni sınırı "işlemin yapıldığı yıl"ın VUK 232 fatura sınırı olarak tanımlar. Bu ifadenin hizmet yılını mı, tahsilat ve makbuz yılını mı kastettiği belirsizdir.
  - [Özelge: 09.06.2022, E-64597866-130-9597 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30226] [Özelge: 07.11.2023, E-37009108-130[467770]-182439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30159] [Özelge: 19.11.2025, E-93996897-130-211856 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/38780]

  | Dönem | Sınır (KDV dahil) | Dayanak |
  |---|---|---|
  | 30.06.2021'e kadar | 1.000 TL | KDV GUT ilk hali |
  | 01.07.2021 – 29.02.2024 | 2.000 TL | Seri 36 (RG 03.06.2021/31500); Karabük Def. 25.09.2024 özelgesi (ID 30151) |
  | 2024 (01.03.2024'ten itibaren) | 6.900 TL (VUK 232 fatura sınırı) | Seri 50 (RG 10.02.2024/32456); VUK GT 556 |
  | 2025 | 9.900 TL | VUK GT 577 (RG 30.12.2024/32768 2. Mük.); özelge 15.08.2025, E-64597866-130-1025186 (ID 38981) |
  | 2026 | 12.000 TL | VUK GT 588 (RG 31.12.2025/33124 5. Mük.) |

  01.03.2024'ten itibaren sınır, işlemin yapıldığı yılın VUK 232 fatura sınırıdır (`parametreler.md`).
- **Beyan:** Tevkif edilen KDV'yi alıcı (borçlu) 2 No.lu KDV beyannamesiyle beyan eder. Avukat yalnız tevkif edilmeyen kısmı 1 No.lu beyannamede beyan eder (genel KDV tevkifatı mekanizması; ayrıntı `kdv.md`). [Özelge: 06.06.2022, E-36062021-130[09-2021/ÖZE-40]-50290 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232]
- **Ücretin davayı kazanana ödenmesi:**
  - Hükmolunan ücretin davayı kazanana ödenmesi KDV'nin konusuna girmez. Bu kural 1985'ten beri 15 Seri No.lu KDV GT'nin (J) bölümünde yer alıyordu ve KDV GUT I/B-4'e aynen aktarıldı.
  - Kazananın ücreti ücretli avukatına aktarması da KDV'ye tabi değildir.
  - Serbest avukata geçen kısım KDV'ye tabidir ve avukat e-SMM'yi davayı kazanan adına düzenler.
  - 2003–2014 tarihli özelgelerdeki aksi görüşler için 12. başlığa bakın.
  - [Özelge: 01.12.2020, 27523430-130[1-2019/324]-E.51656 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/24709] [Özelge: 19.02.2016, 90792880-155.01.05.02[2013/2512]-6991 — https://gib.gov.tr/mevzuat/kanun/438/ozelge/23471] [Özelge: 02.01.2012, B.07.1.GİB.4.20.15.01-40-MUK-2011-45-3 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/29584]
- **Sözleşmeli ama ücretli olmayan avukat:** Hizmet akdiyle değil vekalet akdiyle (hizmet satın alma olarak) çalışan avukatın vekalet ücreti KDV'ye tabidir. 2015 tarihli özelgedeki "ücret karşılığı hizmet verilen müvekkilin davasından doğan ücret KDV'ye tabi değildir" ifadesi yalnız gerçek ücret (hizmet akdi) ilişkisi için okunmalıdır. [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533] [Özelge: 30.09.2013, B.07.1.GİB.4.06.16.01-120[94-13/14]-1083 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23260] [Özelge: 27.07.2015, B.07.1.GİB.4.06.16.01-120[94-15/11]-786 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/37779]

## 6. Ücretli, kurum ve sözleşmeli avukatlar; sendika
- **Hizmet akdiyle çalışan avukat:** İşvereni aracılığıyla ödenen vekalet ücreti ücrettir (GVK 61, 94, 103-104). İşveren bordro düzenler; avukat e-SMM düzenlemez ve KDV hesaplanmaz. Alacaklı şirket aldığı ücreti kurum kazancına dahil eder. Büroda bordrolu avukat çalıştıran serbest avukat için de bu ayrım önemlidir. [Özelge: 01.12.2020, 27523430-130[1-2019/324]-E.51656 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/24709] [Özelge: 17.01.2024, E-13649056-125[2020-ÖZE-06]-5526 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23151] [Özelge: 19.03.2021, 38418978-120[94-20/27-İ]-101240 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/24440]
- **Alacaklı kuruma ödeme:** Tam mükellef alacaklı kuruma yapılan vekalet ücreti ödemesinden kurumlar vergisi kesintisi yapılmaz (ayrıntı 11. başlık).
- **657 sayılı Kanuna tabi kamu avukatı:**
  - Borçlu, kuruma öderken tevkifat yapmaz.
  - Kurum avukata, hukuk müşavirine veya hukuk birimi amirine öderken bu ücreti kurumdan alınan diğer ücretlerle birleştirir ve kümülatif matrah üzerinden keser.
  - Dikkat: 2020 tarihli özelgenin sonuç cümlesinde "vergi tevkifatı yapılmaması gerekmemektedir" diye bir yazım hatası (çift olumsuz) vardır. Sonuç 311 GVGT 25/4 ve 24440 ile birlikte "borçlu kesmez" şeklinde okunmalıdır.
  - Hazine avukatlarına kayyımlık hesabından yapılan ödemeyi 2010 tarihli özelge ikinci işverenden alınan ücret saymıştır; bu özelgedeki beyan sınırları değişmiştir.
  - [Özelge: 14.12.2020, 62030549-120[94-2020/121]-E.928424 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23175] [Özelge: 19.03.2021, 38418978-120[94-20/27-İ]-101240 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/24440] [Özelge: 27.04.2010, B.07.1.GİB.4.35.16.01-176200-14 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23416]
- **Belediyede kısmi zamanlı sözleşmeli avukat (5393 md.49):** Tevzi Yönetmeliğine göre ödenen %70'lik pay ücrettir. Ödemede GV ve damga vergisi kesilir, avukat e-SMM düzenlemez. 2022'den bu yana ücretin asgari ücrete isabet eden kısmı GV ve DV'den istisnadır. [Özelge: 25.08.2011, B.07.1.GİB.4.48.15.01-GVK-49-85 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23340]
- **Sendika avukatı:**
  - Sendikanın ücretli avukatı sendika adına davalarda çalışırsa, sendikanın borçludan tahsil edip avukata ödediği ücret maaş niteliğindedir. Sendika bordro düzenler, KDV hesaplanmaz. Ödemeye ilişkin kâğıtlar DVK (1) sayılı tablo IV/1-b'ye göre damga vergisine tabidir.
  - Aynı avukat sendika üyelerinin davalarına vekalet ederse faaliyeti serbest meslektir. Avukat ödeyen adına KDV'li e-SMM düzenler. Ödeyen GVK 94 sorumlusuysa %20 keser.
  - [Özelge: 19.02.2016, 90792880-155.01.05.02[2013/2512]-6991 — https://gib.gov.tr/mevzuat/kanun/438/ozelge/23471]
- **Kararda adı geçen avukat bir büronun sigortalı çalışanıysa:**
  - Bu avukat kendi adına makbuz düzenleyemez.
  - 2016 tarihli özelgeye göre işveren serbest avukat e-SMM düzenler ve ödeyen %20 tevkifat yapar. CMK Ücret Yönetmeliği md.11/4 de sigortalı müdafinin işveren avukatın makbuzunu kullanacağını öngörür; bu hüküm aynı yaklaşımı destekler.
  - Dikkat: 311 GVGT 25/4'e göre ücretli avukatın işverenine yapılan ödemeden tevkifat yapılmaz. Daha yeni ve genel düzenleme olan tebliğ esas alınırsa ödeyen kesmez, işveren ücret olarak keser. İşveren serbest avukat olduğunda bu hükmün uygulanıp uygulanmayacağı açık değildir; özelge alınması önerilir (12. başlık).
  - [Özelge: 26.05.2016, B.07.1.GİB.4.35.16.01-120.04.06[94-2016/2]-296 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23579] [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985]

## 7. Avukatlar arası paylaşım ve akdi ücretin dava veya icra yoluyla tahsili
- **Yetki belgesiyle takip:**
  - Kararla hükmedilen ücret, davayı bizzat takip eden avukata aittir. Aksi ispatlanmadıkça bu kişi kararda vekil olarak adı geçen avukattır ve e-SMM'yi o düzenler.
  - Yetki belgesiyle çalışan avukat, asıl avukattan tevkil sözleşmesine göre aldığı pay için asıl avukat adına makbuz düzenler. Paylaşım oranı vergi mevzuatının konusu değildir.
  - Özelge 2014 tarihlidir ve bu konudaki tek özelgedir.
  - [Özelge: 10.04.2014, 38418978-120[65-13/9]-361 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23597]
- **Başka bir serbest avukata iş verme veya ücret payı ödeme:**
  - Ödeyen avukat GVK 94/1-2-b uyarınca %20 stopaj yapar ve muhtasarla beyan eder.
  - İşi alan avukat, ödeyen avukat adına KDV'li SMM düzenler.
  - Tevkil ücreti müvekkile yansıtılıyorsa makbuz müvekkile düzenlenir (`uygulama-notlari.md` §5).
  - [Özelge: 28.12.2018, 11395140-105[VUK-1-20846]-1194369 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26372]
- **Ortak iş:** Ücret paylaşılıyorsa her avukat kendi payı için ayrı makbuz düzenler. Biri tutarın tamamına makbuz kesip vergisini düşerek dağıtamaz (`uygulama-notlari.md` §5).
- **Akdi ücret alacağının dava veya icra yoluyla eski müvekkilden tahsili:**
  - Ücret sözleşmesine dayanan alacak, mahkeme ilamı üzerine müvekkil şirketçe icraya yatırılırsa, alacak aslı ve vekalet ücreti serbest meslek kazancıdır. Ödeyen şirket ödeme sırasında ikisi üzerinden %20 tevkifat yapar.
  - Kanuni faiz menkul sermaye iradıdır (GVK 75/6). Faizden tevkifat yapılmaz.
  - İcra takip masrafı, mahkeme masrafları ve icra tahsil harcı serbest meslek kazancına dahil edilmez (GVK 67).
  - Kararda "KDV hariç" yoksa ücret KDV dahil kabul edilir; KDV iç yüzdeyle bulunup SMM'de gösterilir.
  - Serbest meslek kazancı niteliğindeki kısım için SMM düzenlenir.
  - Özelge 2016 tarihlidir.
  - [Özelge: 07.01.2016, B.07.1.GİB.4.34.16.01-120[65-2014/483]-1238 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23585]

## 8. Bozma kararı üzerine iade ve düzeltme
- **Gelir vergisi:** Tahsil edilip e-SMM ile beyan edilen ücret bozma kararı üzerine iade edilirse, iade geçerli belgelerle ispatlanmak şartıyla tutar serbest meslek kazancından gider olarak düşülebilir. [Özelge: 23.08.2011, B.07.1.GİB.4.35.16.01-176200-406 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23702]
- **KDV:** İade edilen kısımda KDV'ye konu hizmet kalmaz. Avukat, değişikliğin olduğu dönemde KDVK 35'e göre beyannamede ve defterde düzeltme yapar. İadeyi alan 5018 kapsamındaki belediye fatura düzenleyemiyorsa, Merkezi Yönetim Harcama Belgeleri Yönetmeliğine göre düzenlediği belge tevsik edici sayılır. [Özelge: 18.02.2016, 50426076-130[1-2014/20-1182]-40 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/29150] [Özelge: 23.08.2011, B.07.1.GİB.4.35.16.01-176200-406 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23702]
- **Açık nokta:** Borçlunun kestiği %20 stopajın iade halinde nasıl düzeltileceği bu özelgelerde ele alınmamıştır; somut olayda vergi dairesine danışın. [Özelge: 18.02.2016, 50426076-130[1-2014/20-1182]-40 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/29150]

## 9. Hesap örnekleri (2026; `aaut_hesap.py karsi-taraf` ile aynı sonuç)
Tutarlar TL'dir.

| | Örnek A | Örnek B | Örnek C | Örnek D |
|---|---|---|---|---|
| Karardaki ücret | 30.000 | 30.000 | 22.000 | 30.000, kararda "KDV hariç" yazıyor |
| Borçlu | Özel şirket | Banka (belirlenmiş alıcı) | Özel şirket (tüketici davasında davalı) | Özel şirket |
| KDV oranı | %20 | %20 | %10 (tüketici mahkemesi) | %20 |
| e-SMM brüt (KDV hariç) | 25.000 | 25.000 | 20.000 | 30.000 |
| KDV | 5.000 | 5.000 | 2.000 | 6.000 |
| GV stopajı (%20) | 5.000 | 5.000 | 4.000 | 6.000 |
| KDV tevkifatı (5/10) | Yok | 2.500 | Yok | Yok |
| Borçlunun icraya yatıracağı | 25.000 | 22.500 | 18.000 | 30.000 |
| Komut (`--hukmedilen` ile) | `--hukmedilen 30000` | `--hukmedilen 30000 --kdv-tevkifat 5/10` | `--hukmedilen 22000 --kdv 10` | `--hukmedilen 30000 --kdv-haric` |

- **Örnek A:** Avukat 5.000 KDV beyan eder, 5.000 stopajı mahsup eder. e-SMM borçlu adına düzenlenir. [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524]
- **Örnek B:** KDV dahil 30.000, 2026 sınırı olan 12.000'i aştığı için 5/10 KDV tevkifatı uygulanır. Banka 2.500 KDV'yi 2 No.lu beyannameyle beyan eder; avukat kalan 2.500'ü beyan eder. [Özelge: 06.06.2022, E-36062021-130[09-2021/ÖZE-40]-50290 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232]
- **Örnek C:** KDV %10 oranından iç yüzdeyle (10/110) ayrılır. Aile mahkemesi dosyalarında borçlu genellikle GVK 94 sorumlusu olmayan gerçek kişidir. Bu durumda stopaj yapılmaz, borçlu 22.000'in tamamını yatırır ve avukat brüt tutarı beyan eder (311 GVGT 25/3; komut: `--hukmedilen 22000 --kdv 10 --odeyen-gercek-kisi`). [Özelge: 02.07.2025, E-84974990-130[KDV-2/İ/28-2025/75]-365183 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/38775] [Özelge: 17.11.2011, B.07.1.GİB.4.34.16.01-GVK 94-2032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23625]
- **Örnek D:** KDV ücretin üzerine eklenir, %20 stopaj KDV hariç 30.000 üzerinden hesaplanır (311 GVGT 25/5). [Özelge: 17.02.2012, B.07.1.GİB.4.06.16.01-120[94-11/10]-215 — https://gib.gov.tr/mevzuat/kanun/435/ozelge/24634] [Özelge: 09.02.2011, B.07.1.GİB.4.06.16.01-2010-GVK-65-12-70 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23658] [Özelge: 12.09.2011, B.07.1.GİB.4.34.17.01-KDV.1-1579 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23627]

## 10. İlgili: CMK, adli yardım ve dosya bazlı sınır (ayrıntı `kdv.md`, `ek-faaliyetler.md`)
- **5/10 KDV tevkifatı:**
  - Cumhuriyet başsavcılıkları (Adalet Bakanlığı; 5018 (I) sayılı cetvel) ve barolar (kamu kurumu niteliğindeki meslek kuruluşu) belirlenmiş alıcıdır.
  - CMK görevi ve adli yardım için bunlar adına düzenlenen makbuzda KDV dahil bedel o yılın sınırını (2026: 12.000 TL; 2025: 9.900 TL) aşarsa 5/10 tevkifat uygulanır.
  - Yargı mercileri nezdindeki hizmet 9/10 danışmanlık kapsamına girmez; "diğer hizmetler" kapsamında 5/10 uygulanır (I/C-2.1.3.2.2.2, I/C-2.1.3.2.13).
  - Özelgedeki 1.000 TL sınırı 2021 tarihlidir ve eskimiştir.
  - e-SMM'deki tevkifat kodu muhtemelen 616'dır ("diğer hizmetler") (teyit edilmedi).
  - [Özelge: 02.06.2021, E-66523654-130[ÖZG-7-2021]-29773 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273]
- **Stopaj ve makbuz:**
  - Başsavcılık GVK 94 sorumlusudur ve %20 stopaj yapar.
  - CMK ödemeleri ve zorunlu yol giderleri serbest meslek kazancıdır, GVK 94'e göre tevkifata ve KDV'ye tabidir.
  - Makbuz CMK görevinde başsavcılık, adli yardımda baro adına düzenlenir (baro adına makbuzun dayanağı 30273'tür).
  - Sigortalı çalışan müdafi, işveren avukatın makbuzunu kullanır (Yönetmelik md.11/4). Gelir, büro sahibinin serbest meslek kazancı olarak stopaja ve KDV'ye tabidir.
  - [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985] [Özelge: 02.06.2021, E-66523654-130[ÖZG-7-2021]-29773 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273]
- **Ücretli dönemden kalan alacak:**
  - Avukat, ücretli çalıştığı dönemde baro görevlendirmesi (CMK veya adli yardım) nedeniyle hak ettiği ücreti işten ayrıldıktan sonra tahsil ederse, bu ödeme arızi serbest meslek kazancıdır. Makbuz düzenleme zorunluluğu yoktur, ödeyen %20 tevkifat yapar.
  - Arızi serbest meslek kazancında 2026'da 350.000 TL'ye (2025: 280.000 TL) kadar istisna vardır. Haddin altındaki kısımdan kesilen vergi nihai vergidir (GVK 82; Rehber s.11; `parametreler.md`).
  - [Özelge: 20.04.2020, 84098128-120[65-2019/5]-134497 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23551]
- **Mükellefiyet kapatıldıktan sonra tahsil edilen baro görevi ücreti:**
  - Serbest meslek mükellefiyetini kapatan avukatın, mükellef olduğu döneme ait baro görevlerinden sonradan tahsil ettiği tutar GVK 82/1-5 kapsamında arızi kazançtır.
  - Bu bent için istisna yoktur (istisna yalnız (1)-(4) numaralı bentlerin toplamına uygulanır).
  - SMM gerekmez, ödeyen %20 tevkifat yapar.
  - [Özelge: 20.05.2022, E-50426076-120[65-2021/20-822]-66280 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23169]
- **Sigortalı çalışırken sürekli CMK görevi alan avukat:** 2011 tarihli özelgeye göre baronun sürekli görevlendirmesi faaliyetin mutad yapıldığını gösterir; avukat mükellefiyet açmalı ve SMM düzenlemelidir. Güncel Yönetmelik md.11/4 ise sigortalı müdafinin işveren avukatın makbuzunu kullanmasını öngörür (12. başlık). Av.K. 11-12'deki çalışma yasakları ayrıca değerlendirilmelidir. [Özelge: 09.06.2011, B.07.1.GİB.4.38.15.02-VUK-21-197-50 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23655]
- **"Masraf" satırı:**
  - Zorunlu yol gideri, CMK Ücret Yönetmeliği md.4/1-e'deki "ücret" tanımına girer. Bu nedenle stopaja ve KDV'ye tabidir ve tevkifat sınırı hesabında işin bedeline eklenir.
  - Aynı tanım müdafi veya vekilin ödediği temyiz, istinaf ve itiraz harçlarını da kapsar. Ancak harç iadesi md.11/6 uyarınca kesintisiz ödenir ve kazanç sayılmaz (GVK 67/2). e-SMM'de tarife ücreti ve yol gideri, harç iadesinden ayrı tutulmalıdır.
  - Yönetmeliğin md.11/3 ve 4/1-b'deki "büro" (birden fazla barolu illerdeki adli yardım bürosu) ibareleri Danıştay 8. Dairesinin 24.12.2025 tarihli, E.2025/1380, K.2025/10316 sayılı kararıyla iptal edilmiştir (araştırma notu; Yönetmelik metni: mevzuat.gov.tr MevzuatNo=11156).
  - [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985]
- **Dosya bazlı sınır:**
  - Birbiriyle bağlantısız dosyalara ait makbuzlarda sınır, başsavcılık ödemeyi toplu yapsa da her dosya için ayrı uygulanır. Aynı dosyada birden fazla şüpheli veya sanık için yapılan ödemelerin bütünlük arz edip etmediği somut olaya göre değerlendirilir.
  - Örnek (2025): Toplu ödeme dökümü 3 soruşturma ücreti (3 × 3.209) ve 3 yol gideri (3 × 200) içeriyor, toplam 10.227 TL. Tek işlem sayılırsa 9.900 TL sınırı aşılır ve 5/10 tevkifat uygulanır. Ücretler bağlantısız ayrı dosyalara aitse her biri yaklaşık 3.409 TL'dir ve dosya bazlı yaklaşıma göre tevkifat gerekmez. Aynı dosyada birden fazla şüpheliye aitse tevkifat savunulabilir. e-SMM, ödeyenin yaptığı kesintiyle aynı olmalıdır.
  - [Özelge: 07.11.2023, E-37009108-130[467770]-182439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30159]
- **İndirimli KDV:** Adli yardım kapsamındaki avukatlık hizmetinde KDV %10'dur. Çocuk mahkemelerinin görev alanındaki işlerde, örneğin suça sürüklenen çocuk müdafiliğinde, soruşturma evresi dahil KDV %10'dur (özelgenin verildiği 2022'de %8 idi). Çocuk mahkemesinin görev alanı dışındaki CMK işlerinde genel oran %20 uygulanır; bu lafzi bir yorumdur ve oranı doğrudan belirten özelge bulunamadı (`kdv.md` §8a). [Özelge: 16.02.2022, E-62902401-130[2020-701-75]-22832 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/32149] [Özelge: 02.07.2025, E-84974990-130[KDV-2/İ/28-2025/75]-365183 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/38775]
- **Damga vergisi (⚖️):** GİB'in 2009 görüşüne göre başsavcılığın CMK ödemesi hizmet alımıdır ve DVK (1) sayılı tablo IV/1-a kapsamında damga vergisine tabidir; harcırah niteliğindeki yol gideri tabi değildir. "Bu kesinti de haksızdır" görüşü tartışmalıdır; güncel durum doğrulanmadı (`uygulama-notlari.md` §14 #16a). [Özelge: 27.08.2009, B.07.1.GİB.0.02.62/6210-35 — https://gib.gov.tr/mevzuat/kanun/438/ozelge/35082]
- **CMK tarifeleri:** 2025 CMK Ücret Tarifesi RG 01.02.2025/32800'de, 2026 tarifesi RG 08.01.2026/33131'de yayımlandı. Hukuki yardımın yapıldığı tarihteki tarife uygulanır (Yönetmelik md.10/11). Aynı evrede bir kişi için aynı avukata birden fazla ücret ödenmez (md.10/3).

## 11. Müvekkile bilgi (müvekkil veya borçlu açısından)
Bu başlıktaki bilgiler avukatın kendi vergisine değil, müvekkile veya karşı tarafa verilecek bilgiye ilişkindir.
- **Davayı kazanan müvekkilin borçluya düzenleyeceği belge:**
  - Borçlu ücreti müvekkile öderse, gelir veya kurumlar vergisi mükellefi müvekkil borçlu adına 7 gün içinde fatura vb. belge düzenler (311 GVGT 26/4).
  - KDV GUT I/B-4 bu ödemenin KDV'nin konusuna girmediğini söyler. Faturanın KDV'siz (konu dışı) düzenleneceği buradan çıkarılır; bunu açıkça söyleyen özelge bulunamadı (açık soru).
  - Müvekkil GVK 94 sorumlusuysa ücreti avukata öderken %20 keser (25/2-c).
  - [Özelge: 17.06.2022, E-62030549-120[94-2020/1307]-687704 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531] [Özelge: 01.12.2020, 27523430-130[1-2019/324]-E.51656 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/24709]
- **Alacaklı kuruma ödeme:** Tam mükellef alacaklı kuruma yapılan vekalet ücreti ödemesinden kurumlar vergisi kesintisi yapılmaz (KVK 15 kapsamında değildir). Özelge 2012 tarihlidir; 311 GVGT 25/4 ile uyumludur. [Özelge: 20.02.2012, B.07.1.GİB.4.06.16.01-120[94-11/13]-218 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23318]
- **Makbuz almayan alıcının cezası:**
  - Alıcı VUK 232'de sayılan bir mükellefse (şirket, kurum vb.) VUK 353/1 uygulanır. Belgeyi alamadığını süreyi izleyen 5 iş günü içinde bildirirse kendisine ceza kesilmez (4. başlık).
  - VUK 232/1-5 dışındaki kişiler (ör. tacir olmayan gerçek kişi) SMM almazsa 2026'da her belge için 8.700 TL, yılda en çok 87.000 TL ceza kesilir. Kişi 5 iş günü içinde bildirirse ceza kesilmez (VUK 353/3; `parametreler.md`).
- **Ticari kazançta indirim:** Mahkeme kararıyla ödenen karşı taraf vekalet ücreti, harç, faiz ve icra masrafları, işle ilgili olmak şartıyla GVK 40/3'e göre gider yazılabilir. 2010 tarihli özelgede bu giderler Yargıtay kararının verildiği yılın kazancından indirilmiştir. [Özelge: 06.09.2011, B.07.1.GİB.4.16.16.01-KV-11-4-197 — https://gib.gov.tr/mevzuat/kanun/435/ozelge/22703] [Özelge: 05.01.2012, B.07.1.GİB.4.06.16.01-2009-GVK-40-26 — https://gib.gov.tr/mevzuat/kanun/435/ozelge/21543] [Özelge: 20.09.2010, B.07.1.GİB.4.34.16.01-KVK 8-356 — https://gib.gov.tr/mevzuat/kanun/435/ozelge/28172]
- **Kusurdan doğan yükümlülük:** Bir şirket, çevre kirliliği nedeniyle tahakkuk ettirilen kirlilik yükü bedeli için uzlaşmış; uzlaşma sonucu bedel, faiz ve ilam vekalet ücreti ödemişti. Bu ödemeler, kurumun kusurundan kaynaklandığı gerekçesiyle KVK 11/1-g uyarınca gider kabul edilmemiş, KDV'si de indirilememiştir. KVK 11/1-g'nin lafzı "suçlardan doğan" tazminatlardır; kural her kusur halinde değil, benzer olaylarda dikkate alınmalıdır. [Özelge: 17.02.2023, 64597866-125[11/g]-3310 — https://gib.gov.tr/mevzuat/kanun/435/ozelge/22484]
- **Kira geliri:** Kiraya verilen konutun satın alınmasına ilişkin sözleşme davasını kaybeden mükellefin ödediği yargılama gideri ve karşı taraf vekalet ücreti, gerçek gider usulünde kira gelirinden indirilemez (GVK 74'te sayılmamıştır). Kiracıyla ilgili davalar bu özelgenin kapsamında değildir. [Özelge: 08.08.2022, 84098128-120[74-2021/3]-410874 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/37741]
- **İşle ilgisiz dava:** Ticari kazançla ilgisi olmayan bir dava için ödenen vekalet ücreti ticari kazançtan indirilemez. Özelgedeki dava, mükellefin kendi aylığından kesilen SGDP'nin iptali içindir; özelge ücretin kime ödendiğini belirtmez. [Özelge: 02.01.2012, B.07.1.GİB.4.41.15.01-GVK-2011/18-3 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/22037]

## 12. Değişen ve çelişen görüşler (dikkat listesi)
- **Genel kural:** 7194 s.K. ve 311 GVGT öncesine ait özelgeler (ör. 13.11.2017 tarihli 23505; 375 Sıra No.lu VUK GT dönemindeki "bir nüshayı icra memuruna ver" kuralı) bugünkü düzenle çelişebilir. 311 GVGT md.25-26 ile çatıştıklarında esas alınmaz.
- **Ücret davayı kazanana ödenirse tevkifatı kim yapar? Artık uygulanmaz.** 7194 s.K. öncesindeki özelgeler bu durumda da tevkifatı davayı kaybedene yüklüyordu. 07.12.2019'da yürürlüğe giren GVK 94 fıkrası ve 27.05.2020 tarihli 311 GVGT 25/2-c'ye göre tevkifatı, davayı kazanan avukata öderken yapar. e-SMM de onun adına düzenlenir (26/5). [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533] [Özelge: 27.07.2015, B.07.1.GİB.4.06.16.01-120[94-15/11]-786 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/37779] [Özelge: 13.11.2017, B.07.1.GİB.4.06.18.02-105[236-2015-369]-447207 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23505]
- **Müvekkile toplu ödenen tutar içindeki vekalet ücreti: Artık uygulanmaz.** 2015 tarihli özelge, müvekkile ödenen toplam tutar içindeki vekalet ücretinde tevkifatı borçluya yüklemiş ve makbuzun borçlu adına düzenlenmesini istemişti. Güncel kural 311 GVGT 25/2-c ve 26/5'tir. [Özelge: 30.01.2015, 38418978-120[18-14/17]-92 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/21112]
- **Makbuz nüshasının icra memuruna verilmesi: Artık uygulanmaz.** 356 ve 375 Sıra No.lu VUK GT dönemindeki özelgeler makbuzun bir nüshasının ödemeyi yapan icra memuruna verilmesini istiyordu. 311 GVGT 26/3 bu gereği kaldırdı; e-SMM ile zaten anlamını yitirdi. Borçlu adına düzenleme kuralı sürüyor. [Özelge: 17.10.2022, E-95462982-105[VUK.ÖZLG-20-109]-245464 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524] [Özelge: 10.02.2016, B.07.1.GİB.4.34.19.02-105[236-2015/VUK-1-18922]-11024 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/23657] [Özelge: 14.03.2017, 11395140-105[236-2015/VUK-1-19116]-72536 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/29720]
- **Davayı kazanan mükellefe ödenen ücrette KDV: Eski görüş terk edildi.**
  - 2003–2014 tarihli özelgeler, davayı kazanan mükellefin karşı taraftan aldığı ücret için KDV'li belge düzenleyeceğini söylüyordu.
  - Bu görüş yayımlandığı dönemde de tebliğle çelişiyordu: 15 Seri No.lu KDV GT'nin (J) bölümü 1985'ten beri bu ödemeyi KDV'nin konusu dışında sayıyordu. KDV GUT I/B-4 (01.05.2014'ten itibaren) ve 2020 tarihli özelge de aynı yöndedir.
  - 37976 sayılı özelge GUT'un yürürlüğe girmesinden sonra verildiği halde eski görüşü tekrarlamıştır.
  - 311 GVGT 26/4'teki "fatura ve benzeri belge" zorunluluğu belgeyle sınırlıdır; KDV hesaplanmasını gerektirmez.
  - [Özelge: 01.12.2020, 27523430-130[1-2019/324]-E.51656 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/24709] [Özelge: 22.05.2014, 45404237-130[I-13-170]-161 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/37976] [Özelge: 19.09.2003, B.07.0.GEL.0.53/5320-252-38427 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23682] [Özelge: 02.01.2012, B.07.1.GİB.4.20.15.01-40-MUK-2011-45-3 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/29584]
- **Aynı yönde eski özelgeler:** 2011–2012 tarihli 23627, 26028 ve 24634 sayılı özelgeler de davayı kazanana ödenen ücrette KDV hesaplanacağını söylüyordu; bu görüş de terk edilmiştir. Bu özelgeler oran belirtmez. Tarihlerindeki genel oran %18 idi; 10.07.2023'ten itibaren %20'dir. [Özelge: 12.09.2011, B.07.1.GİB.4.34.17.01-KDV.1-1579 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/23627] [Özelge: 05.09.2011, B.07.1.GİB.4.34.19.02-019.01-1456 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26028] [Özelge: 17.02.2012, B.07.1.GİB.4.06.16.01-120[94-11/10]-215 — https://gib.gov.tr/mevzuat/kanun/435/ozelge/24634]
- **KDV tevkifatı ve sınırı: Değişti.** Karşı taraf vekalet ücretinde 5/10 KDV tevkifatı 01.03.2021'den beri vardır. 2021–2023 tarihli özelgelerdeki 1.000 TL ve 2.000 TL'lik sınırlar artık geçerli değildir. 2026'da sınır VUK 232 fatura sınırı olan 12.000 TL'dir (2025: 9.900 TL). [Özelge: 21.03.2022, 62030549-120[94-2019/1718]-313032 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533] [Özelge: 09.06.2022, E-64597866-130-9597 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30226] [Özelge: 02.06.2021, E-66523654-130[ÖZG-7-2021]-29773 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273]
- **KDV tevkifatına "yargılama gideri" itirazı: Tartışmalı (⚖️), GİB: uygulanır.** Bkz. 5. başlık ve `uygulama-notlari.md` §14 #17.
- **37779 sayılı özelge: Kısmen eskimiş, KDV ifadesi yanlış okunmaya açık.** "Sözleşme gereği ücret karşılığı hizmet verdiğiniz müvekkil" ifadesi, vekalet sözleşmesiyle çalışan serbest avukatı KDV dışında bırakmaz. Bu özelge KDV yönünden dayanak gösterilmemelidir. Tevkifat görüşü de 7194 öncesine aittir. [Özelge: 27.07.2015, B.07.1.GİB.4.06.16.01-120[94-15/11]-786 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/37779]
- **Ücretli avukatın işvereni serbest avukatsa: Tartışmalı.** 2016 tarihli özelge ödeyenin %20 tevkifat yapacağını söyler; CMK Ücret Yönetmeliği md.11/4 de işveren makbuzunu öngörür. 311 GVGT 25/4 ise ücretli avukatın işverenine yapılan ödemede tevkifat yapılmayacağını öngörür. Daha yeni olan tebliğ esas alınırsa ödeyen kesmez, işveren ücret olarak keser. [Özelge: 26.05.2016, B.07.1.GİB.4.35.16.01-120.04.06[94-2016/2]-296 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23579] [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985]
- **Sigortalı avukatın sürekli CMK görevi: Farklı yaklaşımlar.** 2011 tarihli özelge avukatın kendi mükellefiyetini açmasını ister; Yönetmelik md.11/4 ve 2014 tarihli özelge işveren avukatın makbuzunu öngörür. [Özelge: 09.06.2011, B.07.1.GİB.4.38.15.02-VUK-21-197-50 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23655] [Özelge: 26.05.2014, 39044742-130-1439 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985]
- **Kurum aracılığıyla aktarılan icra vekalet ücretinde e-SMM: Kısmen açık.** 2011 ve 2024 tarihli özelgeler e-SMM'nin borçlu adına düzenleneceğini söyler. 311 GVGT 26/5 (alacaklı adına makbuz) yalnız borçlunun icraya uğramadan doğrudan alacaklıya ödediği durumu kapsar. Borçlu tevkifat yapmamış ve aktaran kurum kesmişse makbuzun kimin adına düzenleneceği açık değildir. [Özelge: 17.01.2024, E-13649056-125[2020-ÖZE-06]-5526 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23151] [Özelge: 01.06.2011, B.07.1.GİB.4.06.18.02-32236-8007-328 — https://gib.gov.tr/mevzuat/kanun/434/ozelge/26380]
- **Belgeye göre makbuz düzenleme (2011):** Eski özelgede avukatın makbuzu, borçlunun kesinti yapıp yapmadığı bilgisine göre düzenleyeceği belirtilmişti. Sonuç bugün de geçerlidir, ancak güncel dayanak 311 GVGT'dir. Kesilmeyen stopajın makbuzda gösterilmesi tartışmalıdır (⚖️ 2. başlık; `uygulama-notlari.md` §14 #5a). [Özelge: 19.08.2011, B.07.1.GİB.4.34.16.01-GVK 94-1349 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23641]
- **Ödeme anı: Gerilim (⚖️).** Özelgeler e-SMM anını icra dairesinin avukata ödediği an olarak alır. GVK 67 ise avukat adına icraya yatırılan parayı, avukatın bundan haberdar olmasıyla tahsil edilmiş sayar (4. başlık; `uygulama-notlari.md` §5). [Özelge: 06.06.2022, 27523430-200.03.01[2950368442]-35929 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/20674] [Özelge: 07.07.2023, E-62030549-120[94-2021/516]-718872 — https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519]
- **CMK müdafilik ücretinde KDV tevkifatı yok (2013): Artık uygulanmaz.** Bu görüş 117 Seri No.lu KDV GT dönemine aittir. 01.03.2021'den beri I/C-2.1.3.2.13 uyarınca 5/10 tevkifat uygulanır (10. başlık). [Özelge: 22.10.2013, 88409335-130[9-ÖZELGE-2013-1-3]-26 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30484] [Özelge: 02.06.2021, E-66523654-130[ÖZG-7-2021]-29773 — https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273]
- **Eski tutar ve dönemler:** Eski özelgelerdeki "altışar aylık" geçici vergi, 23'ü muhtasar süresi, 380 TL ceza ve 1.000 / 2.000 TL KDV tevkifat sınırı gibi tutar ve süreler güncel değildir. Güncel değerler `parametreler.md`'dedir.

## 13. Açık sorular (doğrudan dayanak bulunamadı)
- İcra veznesine yatan paradan haberdar olma (ıttıla) anının nasıl tespit edileceğine ilişkin özelge veya düzenleme bulunamadı; GVK 67 yalnız "ıttıla hasıl etmeleri kaydıyla" der.
- Borçlu net ödeyip kestiği stopajı beyan etmemişse avukatın durumu (2. başlık).
- Tevkifatı aktaran şirket yaptığında e-SMM'nin kimin adına düzenleneceği (3. başlık).
- Davayı kazanan müvekkilin borçluya düzenleyeceği faturanın KDV'siz olup olmadığı (11. başlık).
- İşveren serbest avukat olduğunda 311 GVGT 25/4'ün uygulanıp uygulanmayacağı (6. başlık).
- Bozma üzerine iadede borçlunun kestiği stopajın düzeltilmesi (8. başlık) ve yersiz kesintinin iadesinde başvurulacak vergi dairesi (2. başlık).
- KDV tevkifat sınırındaki "işlemin yapıldığı yıl" ifadesinin hizmet yılını mı, makbuz yılını mı kastettiği (5. başlık).
- e-SMM iptal ve itiraz usulü (509 Sıra No.lu VUK GT V.5.4 ayrıntıyı ebelge.gib.gov.tr teknik kılavuzlarına bırakır; kılavuz incelenmedi) ve KDV tevkifatının e-SMM satırlarında gösterimi (GUT birincil metninden okunmadı).
- Adli yardımda baronun gelir vergisi tevkifatı: Baro KDV GUT'ta açıkça belirlenmiş alıcıdır, ancak GVK 94/1'deki tevkifat sorumluları listesinde adıyla yer almaz. 23551, ücretli dönemde hak edilen zorunlu müdafilik ve adli yardım ödemelerinden %20 tevkifat yapılacağını söyler; baronun kendisine yönelik doğrudan özelge bulunamadı. Baro ödeme dökümünü kontrol et; kesinti yoksa brüt tutarı beyan et.

## Bu dosyada kullanılan özelgeler
"Yerel" sütunu, tam metnin `references/ozelgeler/<ID>.txt` olarak bulunup bulunmadığını gösterir.

| Tarih | Sayı | Konu | ID | Yerel | Link |
|---|---|---|---|---|---|
| 19.11.2025 | E-93996897-130-211856 | KDV tevkifat sınırının güncel tebliğ metni (VUK 232 fatura sınırı) | 38780 | yok | https://gib.gov.tr/mevzuat/kanun/436/ozelge/38780 |
| 15.08.2025 | E-64597866-130-1025186 | 2025 tevkifat sınırı 9.900 TL (VUK GT 577) | 38981 | yok | https://gib.gov.tr/mevzuat/kanun/436/ozelge/38981 |
| 02.07.2025 | E-84974990-130[KDV-2/İ/28-2025/75]-365183 | Adli yardımlı davanın ilamlı icrasında icra vekalet ücretine %10 KDV | 38775 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/38775 |
| 05.05.2025 | E-84974990-130[KDV-2/İ/9-2025/26]-245593 | 5/10 tevkifatta belirlenmiş alıcıların güncel listesi (KİT dahil) | 38680 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/38680 |
| 25.09.2024 | E-35831311-010.01-23750 | 01.03.2024 öncesi tevkifat sınırı 2.000 TL | 30151 | yok | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30151 |
| 31.07.2024 | E-62030549-120-1020639 | Üçüncü kişinin borçlu adına icraya yatırması; tevkifatı borçlu yapar, SMM borçlu adına | 23511 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23511 |
| 17.01.2024 | E-13649056-125[2020-ÖZE-06]-5526 | İcradan şirket hesabına geçip avukata aktarılan ücrette tevkifat ve SMM | 23151 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23151 |
| 07.11.2023 | E-37009108-130[467770]-182439 | Başsavcılığın toplu ödemesinde KDV tevkifat sınırının dosya bazında uygulanması | 30159 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30159 |
| 07.07.2023 | E-62030549-120[94-2021/516]-718872 | Kayyım atanan şirketin hesabından haczen ödemede tevkifat yokluğu ve SMM | 23519 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23519 |
| 17.02.2023 | 64597866-125[11/g]-3310 | Kirlilik yükü uzlaşmasında ilam vekalet ücreti gider yazılamaz, KDV'si indirilemez | 22484 | var | https://gib.gov.tr/mevzuat/kanun/435/ozelge/22484 |
| 17.10.2022 | E-95462982-105[VUK.ÖZLG-20-109]-245464 | Omurga: borçlunun tevkifatı, SMM borçlu adına, tevkifat yapılmazsa brüt beyan | 23524 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23524 |
| 02.09.2022 | 62030549-120[94-2019/473]-978373 | Alacaklı şirket aracılığıyla aktarımda mükerrer tevkifat yapılmaması | 23530 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23530 |
| 29.08.2022 | 48816587-120[2019]-60836 | Döner sermaye ödemesinde tevkifat ve SMM; yargılama giderleri | 23697 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23697 |
| 08.08.2022 | 84098128-120[74-2021/3]-410874 | Konut alım sözleşmesi davasındaki vekalet ücretinin kira gelirinden indirilememesi | 37741 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/37741 |
| 17.06.2022 | E-62030549-120[94-2020/1307]-687704 | e-SMM gelmese de tevkifat; muhtasarda makbuz bilgisiz beyan; ceza; müvekkilin 7 günlük faturası | 23531 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23531 |
| 09.06.2022 | E-64597866-130-9597 | İlam ve icra vekalet ücretinin KDV tevkifatı sınırında birlikte değerlendirilmesi; tek veya çok makbuz | 30226 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30226 |
| 06.06.2022 | 27523430-200.03.01[2950368442]-35929 | Avukatın SMM düzenlemekten kaçınması; KDV ve tevkifat | 20674 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/20674 |
| 06.06.2022 | E-36062021-130[09-2021/ÖZE-40]-50290 | Kamu borçlu adına karşı taraf vekalet ücreti makbuzunda 5/10 KDV tevkifatı | 30232 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30232 |
| 20.05.2022 | E-50426076-120[65-2021/20-822]-66280 | Mükellefiyet kapatıldıktan sonra tahsil edilen baro görevi ücreti: GVK 82/1-5 arızi kazanç, istisna yok | 23169 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23169 |
| 08.04.2022 | 97895701-155[2021/251]-389396 | Kamu kurumunun ödediği karşı taraf vekalet ücretinden damga vergisi kesilmez | 34278 | var | https://gib.gov.tr/mevzuat/kanun/438/ozelge/34278 |
| 21.03.2022 | 62030549-120[94-2019/1718]-313032 | Kurum aleyhine ve lehine vekalet ücreti; ücretli avukat; KDV tevkifatı | 23533 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23533 |
| 16.02.2022 | E-62902401-130[2020-701-75]-22832 | 32. sıra KDV oranının tarihçesi; çocuk mahkemesi işlerinde soruşturma dahil indirimli oran | 32149 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/32149 |
| 11.11.2021 | 20811645-130[21-415-30]-72187 | Özel kuruluş kanunu olmayan kurum belirlenmiş alıcı değil; KDV tevkifatı yok | 30251 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30251 |
| 02.06.2021 | E-66523654-130[ÖZG-7-2021]-29773 | Adli yardım (baro) ve CMK (savcılık) ödemelerinde 5/10 KDV tevkifatı | 30273 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30273 |
| 19.03.2021 | 38418978-120[94-20/27-İ]-101240 | İcraya yatırılan ücrette kadrolu avukat; yersiz kesintinin iadesi | 24440 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/24440 |
| 12.03.2021 | 64597866-120-4566 | Tehir-i icra teminatı ve sonradan yatırılan ücrette tevkifat | 23536 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23536 |
| 30.12.2020 | 84098128-120.04.06[94-2020/6]-E.389388 | Kıdem tazminatından kesilip icraya aktarılan ücrette tevkifat yokluğu | 24441 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/24441 |
| 14.12.2020 | 62030549-120[94-2020/121]-E.928424 | 657'ye tabi kurum avukatı; borçlu kesmez (metinde yazım hatası), kümülatif matrah | 23175 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23175 |
| 01.12.2020 | 27523430-130[1-2019/324]-E.51656 | Kazanan şirkete ödeme KDV konusu dışı; ücretli avukata aktarım | 24709 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/24709 |
| 26.10.2020 | 27575268-105[236-2020-472]-E.280399 | Mal satışı veya alacak haczi yoluyla tahsil; tevkifatsız SMM | 23544 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23544 |
| 20.04.2020 | 84098128-120[65-2019/5]-134497 | Ücretli dönemde hak edilen baro görev ücreti: arızi kazanç, %20 tevkifat | 23551 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23551 |
| 28.12.2018 | 11395140-105[VUK-1-20846]-1194369 | Avukatın başka bir avukata iş vermesi: %20 stopaj, KDV'li SMM; KDVK 27/5 | 26372 | var | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26372 |
| 16.11.2017 | B.07.1.GİB.4.07.17.02-105[Mük.257.VUK.ÖZ.14.39]-188100 | SMM kurum, borçlu veya davayı kazanan adına; GVK 96 brüte iblağ | 23504 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23504 |
| 13.11.2017 | B.07.1.GİB.4.06.18.02-105[236-2015-369]-447207 | İcraya yatırılan ücrette KDV ve SMM (7194 öncesi tevkifat görüşü) | 23505 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23505 |
| 09.11.2017 | B.07.1.GİB.4.07.16.01-120.04[GVK.ÖZ.2016.34]-181943 | Sendikaya vekalet akdiyle hizmet; ücret alınmayan üyeye SMM yok | 23217 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23217 |
| 14.03.2017 | 11395140-105[236-2015/VUK-1-19116]-72536 | Hükmolunan ücrette KDV ve SMM adresatı (375 VUK GT dönemi) | 29720 | var | https://gib.gov.tr/mevzuat/kanun/434/ozelge/29720 |
| 26.05.2016 | B.07.1.GİB.4.35.16.01-120.04.06[94-2016/2]-296 | Kararda adı geçen avukat büroda ücretli; işveren avukat SMM (tartışmalı) | 23579 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23579 |
| 19.02.2016 | 90792880-155.01.05.02[2013/2512]-6991 | Sendika avukatı: ücret veya serbest meslek; KDV ve damga vergisi | 23471 | var | https://gib.gov.tr/mevzuat/kanun/438/ozelge/23471 |
| 18.02.2016 | 50426076-130[1-2014/20-1182]-40 | Bozma üzerine iade edilen ücrette KDV düzeltmesi | 29150 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/29150 |
| 10.02.2016 | B.07.1.GİB.4.34.19.02-105[236-2015/VUK-1-18922]-11024 | İcradan ödenen ücrette SMM borçlu adına (nüsha açıklaması eski) | 23657 | var | https://gib.gov.tr/mevzuat/kanun/434/ozelge/23657 |
| 07.01.2016 | B.07.1.GİB.4.34.16.01-120[65-2014/483]-1238 | Akdi ücret alacağının ilam ve icra yoluyla tahsili; KDV GUT I/B-4'ün eski metni | 23585 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23585 |
| 27.07.2015 | B.07.1.GİB.4.06.16.01-120[94-15/11]-786 | Eski tevkifat görüşü; yanlış okunmaya açık KDV ifadesi | 37779 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/37779 |
| 30.01.2015 | 38418978-120[18-14/17]-92 | Telif tazminatı içindeki vekalet ücreti (eski tevkifat görüşü) | 21112 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/21112 |
| 26.05.2014 | 39044742-130-1439 | CMK ödemeleri ve zorunlu yol gideri serbest meslek kazancı; sigortalı müdafi işveren makbuzu | 31985 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/31985 |
| 22.05.2014 | 45404237-130[I-13-170]-161 | Kazanan şirkete ödemede KDV (eski görüş, GUT sonrası); ücretli avukata aktarım | 37976 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/37976 |
| 10.04.2014 | 38418978-120[65-13/9]-361 | Yetki belgesiyle takipte ücretin hak sahibi; tevkil payına makbuz | 23597 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23597 |
| 22.10.2013 | 88409335-130[9-ÖZELGE-2013-1-3]-26 | CMK müdafilik ücretinde KDV tevkifatı yok (117 Seri dönemi; geçersiz) | 30484 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/30484 |
| 30.09.2013 | B.07.1.GİB.4.06.16.01-120[94-13/14]-1083 | SGK sözleşmeli avukat: tamamından tevkifat, mükerrer tevkifat yok, %30 gider | 23260 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23260 |
| 11.03.2013 | 62030549-120[94-2012/280]-374 | Kamulaştırmada masrafı üstlenen şirketin icraya ödemesi; gider | 22455 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/22455 |
| 06.12.2012 | 53445970-105-[236-2012-27-15]-128 | Beraat eden sanık lehine hazineden ödenen ücret avukatın kazancı | 26366 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/26366 |
| 13.09.2012 | B.07.1.GİB.4.34.16.01-120[98-2012/254]-2776 | Kamu idaresinin ödemesinde SMM tarihi ve tevkifat dönemi | 24499 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/24499 |
| 20.04.2012 | B.07.1.GİB.4.38.15.01-GV-20-485-57 | Tevkifatsız icraya yatırma; çok dosyaya tek SMM | 23617 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23617 |
| 20.02.2012 | B.07.1.GİB.4.06.16.01-120[94-11/13]-218 | Alacaklı kuruma ödemede KV kesintisi yok | 23318 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23318 |
| 17.02.2012 | B.07.1.GİB.4.06.16.01-120[94-11/10]-215 | İcraya yatırılan ücrette tevkifat, SMM, KDV hariç matrah (eski KDV görüşü) | 24634 | var | https://gib.gov.tr/mevzuat/kanun/435/ozelge/24634 |
| 05.01.2012 | B.07.1.GİB.4.06.16.01-2009-GVK-40-26 | Mahkeme kararıyla ödenen vekalet ücretinin gider yazılması | 21543 | var | https://gib.gov.tr/mevzuat/kanun/435/ozelge/21543 |
| 02.01.2012 | B.07.1.GİB.4.20.15.01-40-MUK-2011-45-3 | 15 Seri KDV GT (J): kazanana ödeme KDV dışı; KDV dahil karinesi | 29584 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/29584 |
| 02.01.2012 | B.07.1.GİB.4.41.15.01-GVK-2011/18-3 | İşle ilgisiz (SGDP) dava için ödenen ücret gider yazılamaz | 22037 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/22037 |
| 24.11.2011 | B.07.1.GİB.4.22.15.01-2010/KDV-13-2-30 | Karşı taraftan alınan ücret KDV'ye tabi | 29609 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/29609 |
| 17.11.2011 | B.07.1.GİB.4.34.16.01-GVK 94-2032 | Reddiyatla ödenen ücrette avukatın stopaj takibi sorumluluğu yok | 23625 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23625 |
| 12.09.2011 | B.07.1.GİB.4.34.17.01-KDV.1-1579 | KDV dahil ve hariç; icra yoluyla ödeme (2011; eski KDV görüşü) | 23627 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23627 |
| 06.09.2011 | B.07.1.GİB.4.16.16.01-KV-11-4-197 | Ödenen karşı taraf vekalet ücretinin GVK 40/3 ile gider yazılması | 22703 | var | https://gib.gov.tr/mevzuat/kanun/435/ozelge/22703 |
| 05.09.2011 | B.07.1.GİB.4.34.19.02-019.01-1456 | İcra yoluyla tahsil edilen hizmet bedeli ve vekalet ücretinde KDV | 26028 | var | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26028 |
| 25.08.2011 | B.07.1.GİB.4.48.15.01-GVK-49-85 | Belediyede kısmi zamanlı sözleşmeli avukatın payı ücrettir | 23340 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23340 |
| 24.08.2011 | B.07.1.GİB.4.34.16.01-GVK 94-1399 | Borçlu tevkifat düşülmüş tutarı icraya yatırır | 23639 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23639 |
| 23.08.2011 | B.07.1.GİB.4.35.16.01-176200-406 | Bozma üzerine iade edilen ücretin gider yazılması | 23702 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23702 |
| 19.08.2011 | B.07.1.GİB.4.34.16.01-GVK 94-1349 | İcra yoluyla ödemede SMM'nin kesinti bilgisine göre düzenlenmesi | 23641 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23641 |
| 09.06.2011 | B.07.1.GİB.4.38.15.02-VUK-21-197-50 | Sigortalı avukatın sürekli CMK görevi: mükellefiyet ve SMM | 23655 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23655 |
| 01.06.2011 | B.07.1.GİB.4.06.18.02-32236-8007-328 | Topluca aktarılan ücrette her borçlu adına ayrı SMM | 26380 | var | https://gib.gov.tr/mevzuat/kanun/434/ozelge/26380 |
| 09.02.2011 | B.07.1.GİB.4.06.16.01-2010-GVK-65-9-67 | Ücretin yarısının sözleşmeyle bankaya bırakılması: tamamı hasılat, bırakılan pay belgeyle gider | 23660 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23660 |
| 09.02.2011 | B.07.1.GİB.4.06.16.01-2010-GVK-65-12-70 | Vergi dairesinin ödediği ücrette KDV iç yüzde ve stopaj matrahı | 23658 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23658 |
| 20.09.2010 | B.07.1.GİB.4.34.16.01-KVK 8-356 | Yargıtay kararına bağlı vekalet ücretinin gider dönemi | 28172 | var | https://gib.gov.tr/mevzuat/kanun/435/ozelge/28172 |
| 27.04.2010 | B.07.1.GİB.4.35.16.01-176200-14 | Kayyımlık hesabından hazine avukatlarına ödenen ücret | 23416 | var | https://gib.gov.tr/mevzuat/kanun/433/ozelge/23416 |
| 27.08.2009 | B.07.1.GİB.0.02.62/6210-35 | CMK ödemesinde damga vergisi (tartışmalı) | 35082 | var | https://gib.gov.tr/mevzuat/kanun/438/ozelge/35082 |
| 19.09.2003 | B.07.0.GEL.0.53/5320-252-38427 | GEGM görüşü: tevkifat, KDV, SMM (eski KDV görüşü) | 23682 | var | https://gib.gov.tr/mevzuat/kanun/436/ozelge/23682 |
