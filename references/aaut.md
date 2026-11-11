# Avukatlık Asgari Ücret Tarifesi (AAÜT) ve vergisel sonuçları

Son kontrol: 09/11/2026 (RG fihristi 01/09/2026–09/11/2026 tarandı; tablolar RG ekinden okundu).

## Hangi tarife uygulanır
| Hüküm / hukuki yardımın tamamlandığı tarih | Tarife | Betik anahtarı | Madde metni |
|---|---|---|---|
| **03/11/2026 ve sonrası** | AAÜT, RG 03/11/2026, sayı 33419 | `2026-11-03` (öntanımlı) | `kaynak/aaut-2026-metin.txt` |
| 04/11/2025 – 02/11/2026 | AAÜT, RG 04/11/2025, sayı 33067 (değ. RG 08/01/2026-33131 ve RG 28/03/2026-33207) | `2025-11-04` | `kaynak/aaut-2025-metin.txt` |
| 03/11/2025 ve öncesi | Bkz. "Önceki tarifeler" | yok | yok |

- Her tarife **yayımı tarihinde yürürlüğe girer** (md.24). Hesap: `scripts/aaut_hesap.py`. Tarihi verince tarife kendiliğinden seçilir: `python3 scripts/aaut_hesap.py --hukum-tarihi 15.10.2026 karsi-taraf 250000`.
- Aşağıdaki tablolarda **2026** sütunu 03/11/2026 tarifesini, **2025** sütunu 04/11/2025 tarifesini gösterir.
- 2026 tarifesinin tabloları RG ekindeki PDF'ten okundu. İç tutarlılık denetimi tutuyor (dilim genişlikleri toplamı 24.800.000; 78.125 × %16 = 12.500 icra maktu ücreti; 62.500 × %16 = 10.000 arabuluculuk maktu ücreti). Başlıca tutarlar (asliye 62.000, ağır ceza 86.000, sulh hukuk 40.000, tüketici 30.000, icra mahkemesi duruşmalı 23.000, icra dairesi 12.500, sözleşmeli avukat 43.000, icra eşiği 78.125) yayım günü çıkan haber ve duyurularla da uyuşuyor; 08/11/2026'da 2026 tablolarındaki 96 tutar RG ekinin taranmış dört sayfasıyla tek tek karşılaştırıldı, hata çıkmadı; 04–08/11/2026 RG sayılarında (33420–33424, mükerrer yok) AAÜT'ye düzeltme veya değişiklik yok. Kritik işte yine RG ekine bak.

**2026 tarifesinin 2025 tarifesine göre madde değişiklikleri** (iki madde metni karşılaştırıldı):
- **Tutarlar:** bütün maktu ücretler ve nispi dilimler yükseldi (asliye 45.000 → 62.000; ilk dilim 600.000 → 800.000). md.11/1 icra eşiği 56.250 → **78.125 TL**; md.16/2-a arabuluculuk eşiği 50.000 → **62.500 TL**.
- **md.10:** 2025 tarifesinde 08/01/2026'da yürürlükten kaldırılan 10/2 (kısmi redde davalı lehine ücret sınırı) yeni tarifeye alınmadı; fıkralar yeniden numaralandı (tamamen red artık 10/2, birlikte açılan dava 10/3). md.13/1'deki atıf buna göre "10 uncu maddenin ikinci fıkrası" oldu.
- **md.11/1 ve 11/6:** icra dairesi maktu ücretinin üst sınırı "asıl alacak" yerine **"takipte kesinleşen miktar"**.
- **md.14/5:** 28/03/2026 değişikliğiyle gelen metin korundu (yalnız kabul veya kaldırma halinde ücret).
- **md.18/3 (yeni):** vesayet makamının talebiyle baronun bildirdiği avukatlar arasından vasi, kayyım veya yasal danışman olarak görevlendirilenlere, istemleri halinde TMK 457 uyarınca **her yıl için** ücret hükmedilir; bu ücret birinci kısım ikinci bölüm 2/a'daki ücretten (15.000 TL) az olamaz. Görev süresi uzatılırsa uzatma kararı tarihindeki tarife uygulanır. Vergi yönü için `ek-faaliyetler.md` (kayyımlık).

**2025 tarifesinin yürürlükteyken gördüğü değişiklikler** (04/11/2025 – 02/11/2026 arası hükümler için):
- **RG 08/01/2026-33131 (Tebliğler sıra 19):** md.10/2 yürürlükten kaldırıldı (yayımı tarihinde yürürlükte). Manevi tazminatın kısmi reddinde davalı lehine ücret artık davacı lehine ücretle sınırlı değil. md.21 gereği 07/01/2026'ya kadar verilen hükümlerde sınır uygulanır, 08/01/2026'dan itibaren uygulanmaz.
- **RG 28/03/2026-33207:** md.14/5 yeniden düzenlendi. Sulh ceza hâkimliği başvurularında (tekzip, içerik çıkarma, İPC itirazı) ücret yalnız **kabul** veya itiraz üzerine kararın **kaldırılması** halinde hükmedilir. Eski metindeki "reddi" ibaresi çıkarıldı; ret halinde ücret hükmedilmeyeceği bu çıkarmadan anlaşılır (metinde ayrıca yazmaz). md.21 gereği 27/03/2026'ya kadar verilen ret kararlarında eski metin uygulanır.

> Ücret takdirinde **hukuki yardımın tamamlandığı veya hükmün verildiği tarihte** yürürlükteki tarife uygulanır (md.21). Bozma veya kaldırma sonrası verilen kararlarda da bu kural geçerlidir: hükmün verildiği tarihteki tarife esas alınır (md.2/3). Yeni tarife (son yıllarda Eylül–Kasım arasında) yayımlanınca bu dosyaya yeni sütun, `aaut_hesap.py` içindeki `TARIFELER` sözlüğüne yeni anahtar ekleyin ve `kaynak/` altına madde metnini koyun. Önceki tarifelerin künyesi: aşağıda "Önceki tarifeler".
>
> - md.21'in lafzı karşı tarafa yükletilen ücretle sınırlı değildir. md.1/1 tarifeyi tüm hukuki yardımlarda ücretin tayin ve takdirine uygular; md.1/2 akdi ücretin asgarisini de bu tarifeye bağlar.
> - ⚖️ **KDV matrahının alt sınırında hangi tarihteki tarife?** GİB görüşü: matrah tarifedeki ücretten düşük olamaz (KDVK 27/5; özelge 23601); hangi tarihteki tarifenin esas alınacağı düzenlenmemiştir. Bir görüş, md.21'e ve KDV'nin doğduğu ana (hizmetin tamamlanması) dayanarak hukuki yardımın tamamlandığı tarihteki tarifeyi esas alır. Bu tarife genellikle daha yüksek olduğundan vergi riski açısından ihtiyatlı olan budur (çıkarım). TBB eğitimindeki görüş ise sözleşme veya işe başlama tarihindeki tarifeyi esas alır. Ayrıntı: `uygulama-notlari.md` §3, `kdv.md` §9.

## Vergi açısından en önemli üç nokta
1. **Tarifede KDV hükmü yoktur.** Mahkeme kararında "KDV hariç" yazmıyorsa, hükmedilen vekalet ücreti **KDV dahil** kabul edilir. Bu durumda:
   - KDV iç yüzdeyle ayrılır. Örnek (2025 tarifesinin asliye maktu ücreti): 45.000 / 1,20 = 37.500 TL brüt, 7.500 TL KDV.
   - GV stopajı **KDV hariç** tutar üzerinden hesaplanır (311 Seri No.lu GVGT md.25/5).
   - **KDV oranı işin türüne göre değişir:**
     - Genel oran %20'dir.
     - 2007/13033 BKK eki (II) sayılı liste 32. sırada sayılan işlerde oran **%10**'dur: adli yardım; aile, tüketici ve çocuk mahkemelerindeki davalar; vesayet işleri; iş uyuşmazlıklarında dava şartı arabuluculuk; bunlara ilişkin ilamların icrası.
     - %10'luk işlerde iç yüzde hesabında **1,10**'a bölünür (`--kdv 10`). Örnek: aile mahkemesinde 33.000 / 1,10 = 30.000 TL brüt.
     - Kapsam ayrıntısı için `kdv.md` dosyasına bakın.
2. Karşı tarafa yükletilen ücret **avukata aittir** (Av.K. 164/5) ve serbest meslek kazancıdır.
   - **Tevkifatı ödeyen yapar.** Ölçüt, ödeyenin GVK 94/1'de sayılıp sayılmadığıdır; gerçek kişi olması tek başına belirleyici değildir.
     - Şirket, kamu idaresi (belediye dahil) vb. stopaj yapar.
     - Ticari veya mesleki faaliyeti olmayan gerçek kişi (ör. ücretli, emekli) stopaj yapmaz.
     - Gerçek gelirini beyan eden tacir veya serbest meslek erbabı gerçek kişi, ödeme ticari veya mesleki işiyle ilgiliyse stopaj yapar; işle ilgisiz kişisel davada yapmaz (GVK 94: "... ticari, mesleki ve zirai işleriyle ilgili ödemelerine münhasırdır"; 311 GVGT md.25/3; özelge 23620).
   - **e-SMM borçlu (davayı kaybeden) adına** düzenlenir. Ücret icra müdürlüğüne yatırıldığında da makbuz borçlu adına kesilir ve icra müdürlüğüne nüsha verilmez.
   - Ayrıntı için `vekalet-ucreti.md` dosyasına bakın.
3. **Akdi ücret tarifenin altında kararlaştırılamaz** (md.1/3; Av.K. 164/4). Tarifedeki tutarlar akdi ücretin asgarisidir.
   - Gelir vergisinde tahsil edilen tutar esas alınır (tahsil esası).
   - KDV matrahı ise tarifedeki ücretten düşük olamaz. Tarifenin altında ücret alınırsa ya da hiç alınmazsa KDV tarife tutarı üzerinden hesaplanır (KDVK 27/5; özelge 23601). Bkz. `kdv.md` §2, `uygulama-notlari.md` §3.
   - Peşin veya taksitli tahsilatta her tahsilat için ayrı e-SMM düzenlenir.
   - ⚖️ Akdi ücreti tarifeyle karşılaştırırken tarife tutarının KDV hariç mi dahil mi sayılacağını AAÜT ve Av.K. düzenlemez. GİB, tarife altı veya ücretsiz işte KDV'yi tarife tutarı **üzerinden** hesaplatır (23601); yani KDV yönünden tarife tutarı KDV hariç matrahtır. Yukarıdaki "KDV dahil" kabulü yalnız mahkemece hükmedilen veya icra yoluyla ödenen ücrete ilişkindir. Bkz. `uygulama-notlari.md` §3.

## Hesap kuralları (madde özeti)
Madde numaraları iki tarifede aynıdır; farklar satırda belirtilmiştir. Tutarlar "2026 / 2025" sırasıyla verilir.

| Md. | Kural |
|---|---|
| 1 | Tarife, Av.K. ile birlikte uygulanır. Akdi ücret yoksa veya geçersizse mahkeme tarifenin altında ücrete hükmedemez. Tarifenin altında vekalet ücreti kararlaştırılamaz. |
| 2 | Ücret, kesin hükme kadarki bütün işleri kapsar. İcra takibi ile Yargıtay, Danıştay ve Sayıştay'daki temyiz ve istinaf duruşmaları ayrıca ücrete tabidir. |
| 3 | Karşı tarafa yükletilecek ücret tarifedeki miktardan az, **3 katından çok** olamaz. Ret sebebi ortak olan davalılara tek ücret, ayrı olanlara her sebep için ayrı ücret hükmedilir. |
| 4 | Birden çok avukat olsa bile karşı tarafa tek ücret yükletilir. |
| 5 | Dava veya takibi kabul eden avukat ücretin **tamamına** hak kazanır. Kısmi ve belirsiz alacak davalarında belirlenmiş dava değeri esas alınır. |
| 6 | Konusuz kalma, feragat, kabul veya sulh: ön inceleme tutanağından önce **yarısı**, sonra **tamamı**. Bu kural, yargı mercilerince hesaplanan akdi ücrette uygulanmaz. |
| 7 | Nakil, açılmamış sayılma, görevsizlik veya yetkisizlik: ön incelemeden önce yarısı, sonra tamamı (ikinci kısım ikinci bölüm tutarlarını aşamaz). Dava şartı yokluğu veya husumet nedeniyle red: üçüncü kısma göre hesaplanır, ikinci kısım ikinci bölüm sınırı geçerlidir. Gönderme kararlarında ücret yoktur. |
| 8 | Karşılık dava, birleştirme veya ayırmada her dava için ayrı ücret. İradi taraf değişikliğinde çıkarılan taraf lehine maktu ücret. |
| 9 | Tahliye davasında 1 yıllık kira, kira tespitinde 1 yıllık fark, nafakada 1 yıllık nafaka üzerinden üçüncü kısma göre hesaplanır; mahkeme maktu ücretinden az olamaz. Reddedilen nafaka için ücret yoktur. |
| 10 | Manevi tazminatta hüküm altına alınan miktar üzerinden üçüncü kısma göre hesaplanır. Tamamen redde maktu ücret uygulanır. Maddi tazminatla birlikte açılırsa ayrı kalem olarak hükmedilir. Kısmi redde davalı lehine ücreti davacı lehine ücretle sınırlayan fıkra 2026 tarifesinde yoktur; 2025 tarifesinde 07/01/2026'ya kadar verilen hükümlerde vardı (eski 10/2, RG 08/01/2026 ile mülga). |
| 11 | **İcra:** takip sonuçlanıncaya kadar tüm işlemleri kapsar ve üçüncü kısma göre hesaplanır. **78.125 TL'ye kadar** (2025 tarifesinde 56.250 TL) takiplerde icra dairesi maktu ücreti (12.500 / 9.000 TL) uygulanır; bu ücret 2026 tarifesinde **takipte kesinleşen miktarı**, 2025 tarifesinde asıl alacağı geçemez (kısmi itirazda kesinleşen miktar takip miktarından düşük olabilir; hesapta `--kesinlesen`). ⚖️ Sınır maktu ücretin altındaysa ve borçlu süresinde öderse, sınırın ¾ indiriminden önce mi sonra mı uygulanacağı metinde açık değildir; araç önce sınırlar sonra ¾ uygular (düşük sonuç) ve öbür sonucu not olarak verir. Bu sırayı karara bağlayan Yargıtay veya BAM kararı Legaluga/Bedesten taramasında bulunamadı (08/11/2026). Aciz belgesi takibi sonuçlandırır ve tam ücret ödenir. İcra mahkemesinde duruşma olursa ayrıca ücret hükmedilir; istihkakta üçüncü kısım uygulanır. **Borçlu ödeme süresinde öderse ücretin ¾'ü** takdir edilir; bu maktu ücrette ve tahliye takibinde de geçerlidir. **¾ için dosya borcunun tamamı (asıl alacak, faiz, masraf ve vekâlet ücreti) süresinde ödenmeli;** yalnız asıl alacağın ödenmesi yetmez (Yargıtay 12. HD 19.03.2013, E.2013/2131, K.2013/10220; İstanbul BAM 12. HD 07.07.2020, E.2018/2608, K.2020/667). İcra dairesindeki ücrete md.3/1'deki 3 kata kadar artırma uygulanmaz; o hüküm yargı yerlerinin hükmettiği ücret içindir. Borçlu vekilliğinde akdi ücret yoksa maktu ücret uygulanır (aynı üst sınırla). |
| 12 | Tüketici hakem heyeti kararına itirazda kararın iptali halinde tüketici aleyhine üçüncü kısma göre ücret hükmedilir; kabul veya red miktarını geçemez. Heyete sunulmayan belge nedeniyle iptalde ücret yoktur. |
| 13 | Konusu para olan işler: **maktu ücretin altında kalmamak kaydıyla** üçüncü kısma göre hesaplanır, ancak kabul veya red miktarını geçemez. Maddi tazminatın kısmi reddinde davalı lehine ücret davacı lehine ücreti geçemez. Tamamen redde maktu ücret uygulanır. |
| 14 | **Ceza:** mahkumiyet veya HAGB halinde katılan vekili lehine maktu ücret sanığa yükletilir. **CMK ile görevlendirilen vekil varsa kovuşturma için ödenen ücret mahsup edilir.** Beraatte sanık lehine Hazine aleyhine maktu ücret hükmedilir; **CMK müdafii varsa Hazineden alınan ücret mahsup edilir.** Yalnız para cezasında ücret para cezasını geçemez. CMK 141 tazminat davalarında üçüncü kısım uygulanır (sınırlar sıra 9 ile 13 arası). Sulh ceza hâkimliği başvurularında **kabul** veya kaldırma halinde ikinci kısım birinci bölüm 1. sıra uygulanır; ret halinde ücret hükmedilmez (md.14/5; 2025 tarifesinde 28/03/2026'dan itibaren). İdari para cezası bu maktu ücretin altındaysa ceza tutarı kadar ücret hükmedilir. |
| 15 | Danıştay, idare ve vergi mahkemelerinde ilk savunma süresi bitmeden anlaşmazlık sona ererse ücretin yarısı, aksi halde tamamı hükmedilir. Görevli merciye gönderme veya dilekçe reddinde ücret yoktur. |
| 16 | **Arabuluculuk ve uzlaşma:** tarife tutarları akdi ücretin asgarisidir. Av.K. 35/A uzlaşmasında mahkeme maktu ücretinin **¼ fazlası** uygulanır. Dava şartı arabuluculukta: anlaşma halinde konusu para olan işlerde üçüncü kısım ücretin **¼ fazlası**; 62.500 TL'ye kadar (2025: 50.000 TL) işlerde 10.000 TL'nin (2025: 8.000 TL) ¼ fazlası, yani 12.500 TL (2025: 10.000 TL), asıl alacağı geçemez. Konusu para olmayan işlerde maktu ücretin ¼ fazlası. Anlaşmazlık halinde **10.000 TL** (2025: 8.000 TL), asıl alacağı geçemez. Aynı vekille dava açılırsa bu tutar mahsup edilir. |
| 17 | Tahkimde tarife uygulanır. Sigorta Tahkim Komisyonunda asliye maktu ücretinin altında kalmamak kaydıyla üçüncü kısım uygulanır; talebi reddedilen aleyhine ücretin 1/5'i. Spor Tahkim Kurulunda idare mahkemesi ücreti uygulanır. |
| 18 | İş takibi ücreti, işin sonuçlanmasına kadarki tüm işlemleri kapsar. **2026 tarifesiyle eklenen 18/3:** baronun bildirdiği avukatlardan vasi, kayyım veya yasal danışman olarak görevlendirilene istemi halinde her yıl için ücret hükmedilir (TMK 457); birinci kısım ikinci bölüm 2/a ücretinden (15.000 TL) az olamaz. |
| 19 | Dava takipçileri için tarifenin 1/4'ü uygulanır. |
| 20 | Tarifede yazılı olmayan işlerde benzer işe göre ücret belirlenir. |
| 22 | **Seri davalar:** ilk 10 dosyada tam ücret, 11–50. dosyalarda %50, 51–100. dosyalarda %40, 100'ü aşan dosyalarda %25. Duruşmalı işlerde aynı gün ve aynı mahkemede yapılması şarttır. |
| 23 | Kötü niyetli taraf, karşı tarafın akdi vekalet ücretinin tamamını veya bir kısmını ödemeye mahkûm edilebilir. |

## Ücret tabloları (RG ekleri)
Tutarlar TL'dir. **2026** = RG 03/11/2026-33419; **2025** = RG 04/11/2025-33067.

### Birinci kısım, birinci bölüm: Dava ve takip dışındaki hukuki yardımlar
| Sıra | İş | 2026 | 2025 |
|---|---|---|---|
| 1 | Büroda sözlü danışma, ilk saat / sonraki her saat | 5.500 / 2.400 | 4.000 / 1.800 |
| 2 | Çağrı üzerine gidilen yerde sözlü danışma, ilk saat / sonraki her saat | 9.000 / 4.500 | 7.000 / 3.500 |
| 3 | Yazılı danışma, ilk saat / sonraki her saat | 9.000 / 4.500 | 7.000 / 3.500 |
| 4 | Her türlü dilekçe, ihbarname, ihtarname, protesto | 7.500 | 6.000 |
| 5a | Kira sözleşmesi ve benzeri | 10.000 | 8.000 |
| 5b | Tüzük, yönetmelik, miras sözleşmesi, vasiyetname, vakıf senedi vb. | 40.000 | 32.000 |
| 5c | Şirket ana sözleşmesi, devir ve birleşme vb. ticari sözleşmeler | 27.000 | 21.000 |
| 6 | Arabuluculuk anlaşmazlıkla sonuçlanırsa taraf vekili | 10.000 | 8.000 |

### Birinci kısım, ikinci bölüm: İş takibi
| Sıra | İş | 2026 | 2025 |
|---|---|---|---|
| 1 | Belgelendirme, ödeme aşamasındaki paranın tahsili, belge örneği çıkarma vb. | 7.500 | 6.000 |
| 2a | Hakkın doğumu, tespiti, tescili, nakli, değiştirilmesi, sona erdirilmesi veya korunması | 15.000 | 12.000 |
| 2b | İpotek tesis ve fekki vb. işlemler (sürekli sözleşmeli banka ve finans kuruluşları için, her işlem) | 4.000 | 3.000 |
| 3 | Tüzel kişi tacir kuruluş sözleşmesi, ruhsat, imtiyaz, devir, vatandaşlık işleri | 78.000 | 60.000 |
| 4 | Vergi komisyonlarında takip edilen işler | 30.000 | 24.000 |
| 5a | Uluslararası yargı yerleri, duruşmasız | 140.000 | 110.000 |
| 5b | Uluslararası yargı yerleri, duruşmalı | 250.000 | 200.000 |
| 5c | Konusu para olan işler | Üçüncü kısım | Üçüncü kısım |
| 6 | İl ve ilçe tüketici hakem heyetleri, hal hakem heyetleri (6502 s.K. 70/1 saklı; üçüncü kısma göre hesaplanır, maktu ücretin altındaysa asıl alacağı geçmemek kaydıyla) | 9.000 | 7.000 |

### Birinci kısım, üçüncü ve dördüncü bölüm: Sözleşmeli avukat aylık ücreti
| İş | 2026 | 2025 |
|---|---|---|
| Yapı kooperatifleri (Av.K. 35 zorunlu sözleşmeli avukat) | 35.000 | 27.000 |
| Anonim şirketler (Av.K. 35 zorunlu sözleşmeli avukat) | 58.000 | 45.000 |
| Özel kişi ve tüzel kişilerin sözleşmeli avukatları | 43.000 | 33.000 |
| Kamu kurum ve kuruluşlarının sözleşmeli avukatları | 43.000 | 33.000 |

Takip edilen işlerin tarifeye göre ücreti yıllık ücreti aşarsa, aradaki fark avukata ayrıca ödenir.

> Vergi notu: Bu "sözleşmeli avukat" ücreti, avukat bağımsız çalışıyorsa serbest meslek kazancıdır (e-SMM düzenlenir, ödeyen %20 stopaj yapar). Avukat bordrolu ve işverene bağlıysa ücret geliridir. Bkz. `mukellefiyet-istisna.md`.

### İkinci kısım, birinci bölüm: Konusu para olsa da maktu ücrete bağlı işler
| Sıra | İş | 2026 | 2025 |
|---|---|---|---|
| 1a | Görülmekte olan dava içinde olmayan ihtiyati haciz, ihtiyati tedbir, delil tespiti, icranın geri bırakılması, ödeme ve tevdi yeri belirlenmesi; duruşmasız | 13.000 | 10.000 |
| 1b | Aynı işler, duruşmalı | 16.000 | 12.500 |
| 2 | Ortaklığın giderilmesi için satış memurluğu işleri | 25.000 | 18.000 |
| 3 | Ortaklığın giderilmesi ve taksim davaları | 52.000 | 40.000 |
| 4a | Vergi mahkemelerinde dava ve işler, duruşmasız | 40.000 | 30.000 |
| 4b | Vergi mahkemelerinde dava ve işler, duruşmalı | 52.000 | 40.000 |
| 5 | Tüketici mahkemelerinde kredi taksiti veya faiz uyarlama davaları | 26.000 | 20.000 |

### İkinci kısım, ikinci bölüm: Konusu para olmayan işler (maktu ücretler)
`aaut_hesap.py maktu <anahtar>` komutu bu tablodaki anahtarlarla çalışır (2025 tutarı için `--tarife 2025-11-04`).

| Sıra | Yargı yeri / iş | Anahtar | 2026 | 2025 |
|---|---|---|---|---|
| 1 | İcra dairelerinde takip | icra-dairesi | 12.500 | 9.000 |
| 2 | İcra mahkemelerinde iş | icra-mahkemesi | 15.000 | 11.000 |
| 3 | İcra mahkemelerinde dava ve duruşmalı iş | icra-mahkemesi-durusmali | 23.000 | 18.000 |
| 4 | Tahliyeye ilişkin icra takibi | tahliye-icra | 26.000 | 20.000 |
| 5 | İcra mahkemelerinde ceza işi | icra-ceza | 20.000 | 15.000 |
| 6 | Çocuk teslimi ve kişisel ilişki kararlarının yerine getirilmesi | cocuk-teslimi | 21.000 | 16.000 |
| 7 | **Ceza soruşturma evresi** | sorusturma | 15.000 | 11.000 |
| 8 | Sulh hukuk mahkemesi | sulh-hukuk | 40.000 | 30.000 |
| 9 | Sulh ceza ve infaz hâkimlikleri | sulh-ceza | 23.000 | 18.000 |
| 10 | **Asliye mahkemeleri** | asliye | 62.000 | 45.000 |
| 11 | Tüketici mahkemeleri | tuketici | 30.000 | 22.500 |
| 12 | Fikri ve sınai haklar mahkemeleri | fsmh | 70.000 | 55.000 |
| 13 | **Ağır ceza mahkemeleri** | agir-ceza | 86.000 | 65.000 |
| 14 | Çocuk mahkemeleri | cocuk | 62.000 | 45.000 |
| 15 | Çocuk ağır ceza mahkemeleri | cocuk-agir-ceza | 86.000 | 65.000 |
| 16 | Askerlik Kanunu disiplin kurulları | askerlik-disiplin | 34.000 | 27.000 |
| 17a | İdare ve vergi mahkemeleri, duruşmasız | idare-durusmasiz | 40.000 | 30.000 |
| 17b | İdare ve vergi mahkemeleri, duruşmalı | idare-durusmali | 52.000 | 40.000 |
| 18a | BAM ve BİM, ilk derece | bam-ilk-derece | 45.000 | 35.000 |
| 18b | BAM ve BİM, istinafta tek duruşma | bam-istinaf-tek-durusma | 28.000 | 22.000 |
| 18c | BAM ve BİM, istinafta birden fazla duruşma veya keşif | bam-istinaf-cok-durusma | 55.000 | 42.000 |
| 19a | Sayıştay hesap yargılaması, duruşmasız | sayistay-durusmasiz | 44.000 | 34.000 |
| 19b | Sayıştay hesap yargılaması, duruşmalı | sayistay-durusmali | 84.000 | 65.000 |
| 20 | Yargıtay, ilk derece | yargitay-ilk-derece | 85.000 | 65.000 |
| 21a | Danıştay ilk derece, duruşmasız | danistay-ilk-durusmasiz | 50.000 | 40.000 |
| 21b | Danıştay ilk derece, duruşmalı | danistay-ilk-durusmali | 80.000 | 65.000 |
| 22 | Yargıtay, Danıştay, Sayıştay temyiz duruşması | temyiz-durusmasi | 50.000 | 40.000 |
| 23 | Uyuşmazlık Mahkemesi | uyusmazlik | 50.000 | 40.000 |
| 24a | AYM Yüce Divan | aym-yuce-divan | 150.000 | 120.000 |
| 24b | AYM bireysel başvuru, duruşmasız | aym-bireysel-durusmasiz | 55.000 | 40.000 |
| 24b | AYM bireysel başvuru, duruşmalı | aym-bireysel-durusmali | 100.000 | 80.000 |
| 24c | AYM diğer dava ve işler | aym-diger | 115.000 | 90.000 |

- **Aile, iş ve ticaret mahkemeleri:** Tabloda ayrı sıraları yoktur. Bu mahkemeler asliye derecesindedir: aile mahkemesi (4787 s.K. md.2), iş mahkemesi (7036 s.K. md.2/1), asliye ticaret mahkemesi (TTK md.5). Bu nedenle sıra 10 (asliye: 62.000 TL; 2025 tarifesinde 45.000 TL) uygulanır.
  - Tüketici (sıra 11), fikri ve sınai haklar (sıra 12) ve çocuk mahkemelerinin (sıra 14) kendi sıraları vardır; onlarda kendi tutarları uygulanır.
  - Güven: çıkarım. Tarifede açık hüküm yoktur; sonuç mahkemelerin kuruluş kanunlarına dayanır.
  - Aile mahkemesi işlerinde KDV oranı %10'dur (yukarıda "Vergi açısından en önemli üç nokta", 1. madde).

### Üçüncü kısım: Konusu para olan işlerde nispi ücret (dilimli)
| Dilim | Oran | 2026 dilim genişliği | 2025 dilim genişliği |
|---|---|---|---|
| 1 | %16 | İlk 800.000 TL | İlk 600.000 TL |
| 2 | %15 | Sonraki 800.000 TL | Sonraki 600.000 TL |
| 3 | %14 | Sonraki 1.600.000 TL | Sonraki 1.200.000 TL |
| 4 | %13 | Sonraki 1.600.000 TL | Sonraki 1.200.000 TL |
| 5 | %11 | Sonraki 2.400.000 TL | Sonraki 1.800.000 TL |
| 6 | %8 | Sonraki 3.200.000 TL | Sonraki 2.400.000 TL |
| 7 | %5 | Sonraki 4.000.000 TL | Sonraki 3.000.000 TL |
| 8 | %3 | Sonraki 4.800.000 TL | Sonraki 3.600.000 TL |
| 9 | %2 | Sonraki 5.600.000 TL | Sonraki 4.200.000 TL |
| 10 | %1 | 24.800.000 TL'den yukarısı | 18.600.000 TL'den yukarısı |

- Kümülatif değerler (2026): 800.000 TL → 128.000 TL; 1.600.000 TL → 248.000 TL; 24.800.000 TL → 1.656.000 TL.
- Kümülatif değerler (2025): 600.000 TL → 96.000 TL; 1.200.000 TL → 186.000 TL; 18.600.000 TL → 1.242.000 TL.
- Örnekler (2026 tarifesi):
  - 250.000 TL'lik asliye davası: nispi ücret 40.000 TL, maktu alt sınır 62.000 TL olduğundan **62.000 TL** hükmedilir. Nispi ücret 387.500 TL'lik dava değerinde maktu ücrete eşitlenir.
  - 100.000 TL'lik icra takibi: nispi ücret 16.000 TL. Borçlu süresinde öderse ¾'ü olan **12.000 TL** takdir edilir.
  - 70.000 TL'lik icra takibi (78.125 TL eşiğinin altında): icra dairesi maktu ücreti **12.500 TL**.
- Aynı örnekler 2025 tarifesinde: 250.000 TL'lik asliye davasında 45.000 TL (maktu); 100.000 TL'lik icra takibinde süresinde ödemeyle 12.000 TL.

## Önceki tarifeler (md.21 için)
Hukuki yardımın tamamlandığı veya hükmün verildiği tarihte yürürlükteki tarife uygulanır (md.21). Tarifelerin hepsi yayımı tarihinde yürürlüğe girer (her birinin md.24'ü).

| Tarife | Uygulandığı dönem | Not |
|---|---|---|
| AAÜT, RG 21/09/2023-32316 | 21/09/2023 – 02/10/2024 | md.14/5, RG 03/10/2024-32681 ile değişti. Tabloları bu dosyada yok |
| AAÜT, RG 03/10/2024-32681 | 03/10/2024 – 03/11/2025 | Tabloları bu dosyada yok |
| AAÜT, RG 04/11/2025-33067 | 04/11/2025 – 02/11/2026 | Bu dosyadaki "2025" sütunu |
| AAÜT, RG 03/11/2026-33419 | 03/11/2026'dan beri | Bu dosyadaki "2026" sütunu |

- 2023 ve 2024 tarifelerinin ücret tabloları (ekleri) bu dosyada **yoktur** ve `aaut_hesap.py` bu tarihler için hesap yapmaz (`--hukum-tarihi` 04/11/2025'ten önceyse hata verir).
- O tarihli iş için tutarı RG ekinden kontrol edin; bu dosyadaki tutarları kullanmayın.
- [Kaynak: resmigazete.gov.tr, 21/09/2023-32316, 03/10/2024-32681, 04/11/2025-33067 ve 03/11/2026-33419 sayıları; RG fihristi 01/10/2025–09/11/2026]

## Vergiye çeviri örnekleri (`aaut_hesap.py karsi-taraf`)
Örnek tutar 2026 tarifesinin asliye maktu ücretidir (62.000 TL). Başka tutar için `--hukmedilen <tutar>` kullanın.

| Durum | e-SMM brüt | KDV | Stopaj | Avukata ödenecek | Makbuz kime |
|---|---|---|---|---|---|
| 62.000 TL hükmedildi, kararda "KDV hariç" yok, ödeyen **şirket** | 51.666,67 | 10.333,33 | 10.333,33 | 51.666,67 | Davayı kaybeden şirket |
| Aynısı, ödeyen **GVK 94/1'de sayılmayan gerçek kişi** (ticari veya mesleki faaliyeti yok ya da dava bu faaliyetle ilgisiz) | 51.666,67 | 10.333,33 | 0 | 62.000 | Davayı kaybeden kişi |
| Kararda "62.000 TL + KDV" yazıyor, ödeyen şirket | 62.000 | 12.400 | 12.400 | 62.000 | Davayı kaybeden şirket |
| Ödeyen **5018 cetvellerindeki kamu idaresi** (ör. bakanlık; KDV GUT I/C-2.1.3.2.13 listesinde), KDV dahil tutar tevkifat sınırını aşıyor | 51.666,67 | 10.333,33 | 10.333,33 | 46.500 (5/10 KDV tevkifatı 5.166,67) | Kamu idaresi. Bkz. `kdv.md` §4 |
| Ödeyen **belediye** (belirlenmiş alıcı değil) | 51.666,67 | 10.333,33 | 10.333,33 | 51.666,67 (KDV tevkifatı yok) | Belediye. Belediye GVK 94 sorumlusudur, %20 stopajı keser. Büyükşehir su ve kanalizasyon idaresi ile belediye birlikleri belirlenmiş alıcıdır (I/C-2.1.3.1/b), ama dava ve icrada 5/10 yalnız I/C-2.1.3.2.13 listesinde de yer alana uygulanır: kendi kuruluş kanunu olan su idaresinde (İSKİ; özelge 23533) uygulanır, olmayanında uygulanmaz (özelge 30251); belediye birlikleri o listede adıyla sayılmaz (teyit edilmedi). Bkz. `kdv.md` §4 (özelgeler 30252, 30257) |

> CMK görevlendirmesinde (md.14/1 ve 14/4) hükmedilen maktu ücretten CMK kapsamında ödenen ücret mahsup edilir. CMK ücretinin kendisi Cumhuriyet Başsavcılığı adına e-SMM ile belgelenir; bkz. `ek-faaliyetler.md` ve `kdv.md`.
