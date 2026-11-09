# Avukatlık Asgari Ücret Tarifesi 2025–2026 ve vergisel sonuçları

**Kaynak:** Türkiye Barolar Birliği, *Avukatlık Asgari Ücret Tarifesi*, Resmî Gazete 04/11/2025, sayı 33067 (Tebliğ; ekleri Film 7–10). Tarife **yayımı tarihinde yürürlüğe girer** (md.24). Madde metni `kaynak/aaut-2025-metin.txt`. Hesap: `scripts/aaut_hesap.py`.

**Değişiklikler:**
- **RG 08/01/2026-33131:** md.10/2 yürürlükten kaldırıldı. Manevi tazminatın kısmi reddinde davalı lehine ücret artık davacı lehine ücretle sınırlı değil.
- **RG 28/03/2026-33207:** md.14/5 yeniden düzenlendi. Sulh ceza hâkimliği başvurularında (tekzip, içerik çıkarma, İPC itirazı) ücret yalnız **kabul** veya itiraz üzerine kararın **kaldırılması** halinde hükmedilir; ret halinde hükmedilmez.
- 12/10/2026 itibarıyla yeni tarife yayımlanmadı (RG fihristi kontrol edildi). Son üç tarife 21/09/2023, 03/10/2024 ve 04/11/2025'te yayımlandı; yeni tarife için RG'yi izleyin.

> Ücret takdirinde **hukuki yardımın tamamlandığı veya hükmün verildiği tarihte** yürürlükteki tarife uygulanır (md.21). Bozma veya kaldırma sonrası verilen kararlarda da bu kural geçerlidir: hükmün verildiği tarihteki tarife esas alınır (md.2/3). Yeni tarife (son yıllarda Eylül–Kasım arasında) yayımlanınca bu dosyayı ve `aaut_hesap.py` içindeki `TARIFELER` sözlüğünü güncelleyin. Önceki tarifelerin künyesi: aşağıda "Önceki tarifeler".
>
> - md.21'in lafzı karşı tarafa yükletilen ücretle sınırlı değildir. md.1/1 tarifeyi tüm hukuki yardımlarda ücretin tayin ve takdirine uygular; md.1/2 akdi ücretin asgarisini de bu tarifeye bağlar.
> - ⚖️ **KDV matrahının alt sınırında hangi tarihteki tarife?** GİB görüşü: matrah tarifedeki ücretten düşük olamaz (KDVK 27/5; özelge 23601); hangi tarihteki tarifenin esas alınacağı düzenlenmemiştir. Bir görüş, md.21'e ve KDV'nin doğduğu ana (hizmetin tamamlanması) dayanarak hukuki yardımın tamamlandığı tarihteki tarifeyi esas alır. Bu tarife genellikle daha yüksek olduğundan vergi riski açısından ihtiyatlı olan budur (çıkarım). TBB eğitimindeki görüş ise sözleşme veya işe başlama tarihindeki tarifeyi esas alır. Ayrıntı: `uygulama-notlari.md` §3, `kdv.md` §9.

## Vergi açısından en önemli üç nokta
1. **Tarifede KDV hükmü yoktur.** Mahkeme kararında "KDV hariç" yazmıyorsa, hükmedilen vekalet ücreti **KDV dahil** kabul edilir. Bu durumda:
   - KDV iç yüzdeyle ayrılır: 45.000 / 1,20 = 37.500 TL brüt, 7.500 TL KDV.
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
| 10 | Manevi tazminatta hüküm altına alınan miktar üzerinden üçüncü kısma göre hesaplanır. Tamamen redde maktu ücret uygulanır. Maddi tazminatla birlikte açılırsa ayrı kalem olarak hükmedilir. ~~10/2: kısmi redde davalı lehine ücret davacı lehine ücreti geçemez~~ (RG 08/01/2026 ile **mülga**). |
| 11 | **İcra:** takip sonuçlanıncaya kadar tüm işlemleri kapsar ve üçüncü kısma göre hesaplanır. **56.250 TL'ye kadar** takiplerde icra dairesi maktu ücreti (9.000 TL) uygulanır, ancak asıl alacağı geçemez. Aciz belgesi takibi sonuçlandırır ve tam ücret ödenir. İcra mahkemesinde duruşma olursa ayrıca ücret hükmedilir; istihkakta üçüncü kısım uygulanır. **Borçlu ödeme süresinde öderse ücretin ¾'ü** takdir edilir; bu maktu ücrette ve tahliye takibinde de geçerlidir. Borçlu vekilliğinde akdi ücret yoksa maktu ücret uygulanır. |
| 12 | Tüketici hakem heyeti kararına itirazda kararın iptali halinde tüketici aleyhine üçüncü kısma göre ücret hükmedilir; kabul veya red miktarını geçemez. Heyete sunulmayan belge nedeniyle iptalde ücret yoktur. |
| 13 | Konusu para olan işler: **maktu ücretin altında kalmamak kaydıyla** üçüncü kısma göre hesaplanır, ancak kabul veya red miktarını geçemez. Maddi tazminatın kısmi reddinde davalı lehine ücret davacı lehine ücreti geçemez. Tamamen redde maktu ücret uygulanır. |
| 14 | **Ceza:** mahkumiyet veya HAGB halinde katılan vekili lehine maktu ücret sanığa yükletilir. **CMK ile görevlendirilen vekil varsa kovuşturma için ödenen ücret mahsup edilir.** Beraatte sanık lehine Hazine aleyhine maktu ücret hükmedilir; **CMK müdafii varsa Hazineden alınan ücret mahsup edilir.** Yalnız para cezasında ücret para cezasını geçemez. CMK 141 tazminat davalarında üçüncü kısım uygulanır (sınırlar sıra 9 ile 13 arası). Sulh ceza hâkimliği başvurularında **kabul** veya kaldırma halinde ikinci kısım birinci bölüm 1. sıra uygulanır; ret halinde ücret hükmedilmez (md.14/5, RG 28/03/2026 değişikliği). |
| 15 | Danıştay, idare ve vergi mahkemelerinde ilk savunma süresi bitmeden anlaşmazlık sona ererse ücretin yarısı, aksi halde tamamı hükmedilir. Görevli merciye gönderme veya dilekçe reddinde ücret yoktur. |
| 16 | **Arabuluculuk ve uzlaşma:** tarife tutarları akdi ücretin asgarisidir. Av.K. 35/A uzlaşmasında mahkeme maktu ücretinin **¼ fazlası** uygulanır. Dava şartı arabuluculukta: anlaşma halinde konusu para olan işlerde üçüncü kısım ücretin **¼ fazlası**; 50.000 TL'ye kadar işlerde 8.000 TL'nin ¼ fazlası (10.000 TL), asıl alacağı geçemez. Konusu para olmayan işlerde maktu ücretin ¼ fazlası. Anlaşmazlık halinde **8.000 TL**, asıl alacağı geçemez. Aynı vekille dava açılırsa bu tutar mahsup edilir. |
| 17 | Tahkimde tarife uygulanır. Sigorta Tahkim Komisyonunda asliye maktu ücretinin altında kalmamak kaydıyla üçüncü kısım uygulanır; talebi reddedilen aleyhine ücretin 1/5'i. Spor Tahkim Kurulunda idare mahkemesi ücreti uygulanır. |
| 18 | İş takibi ücreti, işin sonuçlanmasına kadarki tüm işlemleri kapsar. |
| 19 | Dava takipçileri için tarifenin 1/4'ü uygulanır. |
| 20 | Tarifede yazılı olmayan işlerde benzer işe göre ücret belirlenir. |
| 22 | **Seri davalar:** ilk 10 dosyada tam ücret, 11–50. dosyalarda %50, 51–100. dosyalarda %40, 100'ü aşan dosyalarda %25. Duruşmalı işlerde aynı gün ve aynı mahkemede yapılması şarttır. |
| 23 | Kötü niyetli taraf, karşı tarafın akdi vekalet ücretinin tamamını veya bir kısmını ödemeye mahkûm edilebilir. |

## Ücret tabloları (Ekler, Film 7–10)

### Birinci kısım, birinci bölüm: Dava ve takip dışındaki hukuki yardımlar
| Sıra | İş | Ücret (TL) |
|---|---|---|
| 1 | Büroda sözlü danışma, ilk saat / sonraki her saat | 4.000 / 1.800 |
| 2 | Çağrı üzerine gidilen yerde sözlü danışma, ilk saat / sonraki her saat | 7.000 / 3.500 |
| 3 | Yazılı danışma, ilk saat / sonraki her saat | 7.000 / 3.500 |
| 4 | Her türlü dilekçe, ihbarname, ihtarname, protesto | 6.000 |
| 5a | Kira sözleşmesi ve benzeri | 8.000 |
| 5b | Tüzük, yönetmelik, miras sözleşmesi, vasiyetname, vakıf senedi vb. | 32.000 |
| 5c | Şirket ana sözleşmesi, devir ve birleşme vb. ticari sözleşmeler | 21.000 |
| 6 | Arabuluculuk anlaşmazlıkla sonuçlanırsa taraf vekili | 8.000 |

### Birinci kısım, ikinci bölüm: İş takibi
| Sıra | İş | Ücret (TL) |
|---|---|---|
| 1 | Belgelendirme, ödeme aşamasındaki paranın tahsili, belge örneği çıkarma vb. | 6.000 |
| 2a | Hakkın doğumu, tespiti, tescili, nakli, değiştirilmesi, sona erdirilmesi veya korunması | 12.000 |
| 2b | İpotek tesis ve fekki vb. işlemler (sürekli sözleşmeli banka ve finans kuruluşları için, her işlem) | 3.000 |
| 3 | Tüzel kişi tacir kuruluş sözleşmesi, ruhsat, imtiyaz, devir, vatandaşlık işleri | 60.000 |
| 4 | Vergi komisyonlarında takip edilen işler | 24.000 |
| 5a | Uluslararası yargı yerleri, duruşmasız | 110.000 |
| 5b | Uluslararası yargı yerleri, duruşmalı | 200.000 |
| 5c | Konusu para olan işler | Üçüncü kısım |
| 6 | İl ve ilçe tüketici hakem heyetleri, hal hakem heyetleri (6502 s.K. 70/1 saklı; üçüncü kısma göre hesaplanır, maktu ücretin altındaysa asıl alacağı geçmemek kaydıyla) | 7.000 |

### Birinci kısım, üçüncü ve dördüncü bölüm: Sözleşmeli avukat aylık ücreti
| İş | Aylık (TL) |
|---|---|
| Yapı kooperatifleri (Av.K. 35 zorunlu sözleşmeli avukat) | 27.000 |
| Anonim şirketler (Av.K. 35 zorunlu sözleşmeli avukat) | 45.000 |
| Özel kişi ve tüzel kişilerin sözleşmeli avukatları | 33.000 |
| Kamu kurum ve kuruluşlarının sözleşmeli avukatları | 33.000 |

Takip edilen işlerin tarifeye göre ücreti yıllık ücreti aşarsa, aradaki fark avukata ayrıca ödenir.

> Vergi notu: Bu "sözleşmeli avukat" ücreti, avukat bağımsız çalışıyorsa serbest meslek kazancıdır (e-SMM düzenlenir, ödeyen %20 stopaj yapar). Avukat bordrolu ve işverene bağlıysa ücret geliridir. Bkz. `mukellefiyet-istisna.md`.

### İkinci kısım, birinci bölüm: Konusu para olsa da maktu ücrete bağlı işler
| Sıra | İş | Ücret (TL) |
|---|---|---|
| 1a | Görülmekte olan dava içinde olmayan ihtiyati haciz, ihtiyati tedbir, delil tespiti, icranın geri bırakılması, ödeme ve tevdi yeri belirlenmesi; duruşmasız | 10.000 |
| 1b | Aynı işler, duruşmalı | 12.500 |
| 2 | Ortaklığın giderilmesi için satış memurluğu işleri | 18.000 |
| 3 | Ortaklığın giderilmesi ve taksim davaları | 40.000 |
| 4a | Vergi mahkemelerinde dava ve işler, duruşmasız | 30.000 |
| 4b | Vergi mahkemelerinde dava ve işler, duruşmalı | 40.000 |
| 5 | Tüketici mahkemelerinde kredi taksiti veya faiz uyarlama davaları | 20.000 |

### İkinci kısım, ikinci bölüm: Konusu para olmayan işler (maktu ücretler)
`aaut_hesap.py maktu <anahtar>` komutu bu tablodaki anahtarlarla çalışır.

| Sıra | Yargı yeri / iş | Anahtar | Ücret (TL) |
|---|---|---|---|
| 1 | İcra dairelerinde takip | icra-dairesi | 9.000 |
| 2 | İcra mahkemelerinde iş | icra-mahkemesi | 11.000 |
| 3 | İcra mahkemelerinde dava ve duruşmalı iş | icra-mahkemesi-durusmali | 18.000 |
| 4 | Tahliyeye ilişkin icra takibi | tahliye-icra | 20.000 |
| 5 | İcra mahkemelerinde ceza işi | icra-ceza | 15.000 |
| 6 | Çocuk teslimi ve kişisel ilişki kararlarının yerine getirilmesi | cocuk-teslimi | 16.000 |
| 7 | **Ceza soruşturma evresi** | sorusturma | 11.000 |
| 8 | Sulh hukuk mahkemesi | sulh-hukuk | 30.000 |
| 9 | Sulh ceza ve infaz hâkimlikleri | sulh-ceza | 18.000 |
| 10 | **Asliye mahkemeleri** | asliye | 45.000 |
| 11 | Tüketici mahkemeleri | tuketici | 22.500 |
| 12 | Fikri ve sınai haklar mahkemeleri | fsmh | 55.000 |
| 13 | **Ağır ceza mahkemeleri** | agir-ceza | 65.000 |
| 14 | Çocuk mahkemeleri | cocuk | 45.000 |
| 15 | Çocuk ağır ceza mahkemeleri | cocuk-agir-ceza | 65.000 |
| 16 | Askerlik Kanunu disiplin kurulları | askerlik-disiplin | 27.000 |
| 17a | İdare ve vergi mahkemeleri, duruşmasız | idare-durusmasiz | 30.000 |
| 17b | İdare ve vergi mahkemeleri, duruşmalı | idare-durusmali | 40.000 |
| 18a | BAM ve BİM, ilk derece | bam-ilk-derece | 35.000 |
| 18b | BAM ve BİM, istinafta tek duruşma | bam-istinaf-tek-durusma | 22.000 |
| 18c | BAM ve BİM, istinafta birden fazla duruşma veya keşif | bam-istinaf-cok-durusma | 42.000 |
| 19a | Sayıştay hesap yargılaması, duruşmasız | sayistay-durusmasiz | 34.000 |
| 19b | Sayıştay hesap yargılaması, duruşmalı | sayistay-durusmali | 65.000 |
| 20 | Yargıtay, ilk derece | yargitay-ilk-derece | 65.000 |
| 21a | Danıştay ilk derece, duruşmasız | danistay-ilk-durusmasiz | 40.000 |
| 21b | Danıştay ilk derece, duruşmalı | danistay-ilk-durusmali | 65.000 |
| 22 | Yargıtay, Danıştay, Sayıştay temyiz duruşması | temyiz-durusmasi | 40.000 |
| 23 | Uyuşmazlık Mahkemesi | uyusmazlik | 40.000 |
| 24a | AYM Yüce Divan | aym-yuce-divan | 120.000 |
| 24b | AYM bireysel başvuru, duruşmasız | aym-bireysel-durusmasiz | 40.000 |
| 24b | AYM bireysel başvuru, duruşmalı | aym-bireysel-durusmali | 80.000 |
| 24c | AYM diğer dava ve işler | aym-diger | 90.000 |

- **Aile, iş ve ticaret mahkemeleri:** Tabloda ayrı sıraları yoktur. Bu mahkemeler asliye derecesindedir: aile mahkemesi (4787 s.K. md.2), iş mahkemesi (7036 s.K. md.2/1), asliye ticaret mahkemesi (TTK md.5). Bu nedenle sıra 10 (asliye, 45.000 TL) uygulanır.
  - Tüketici (sıra 11), fikri ve sınai haklar (sıra 12) ve çocuk mahkemelerinin (sıra 14) kendi sıraları vardır; onlarda kendi tutarları uygulanır.
  - Güven: çıkarım. Tarifede açık hüküm yoktur; sonuç mahkemelerin kuruluş kanunlarına dayanır.
  - Aile mahkemesi işlerinde KDV oranı %10'dur (yukarıda "Vergi açısından en önemli üç nokta", 1. madde).

### Üçüncü kısım: Konusu para olan işlerde nispi ücret (dilimli)
| Dilim | Oran |
|---|---|
| İlk 600.000 TL | %16 |
| Sonraki 600.000 TL | %15 |
| Sonraki 1.200.000 TL | %14 |
| Sonraki 1.200.000 TL | %13 |
| Sonraki 1.800.000 TL | %11 |
| Sonraki 2.400.000 TL | %8 |
| Sonraki 3.000.000 TL | %5 |
| Sonraki 3.600.000 TL | %3 |
| Sonraki 4.200.000 TL | %2 |
| 18.600.000 TL'den yukarısı | %1 |

- Kümülatif değerler:
  - 600.000 TL → 96.000 TL
  - 1.200.000 TL → 186.000 TL
  - 18.600.000 TL → 1.242.000 TL
- Örnekler:
  - 250.000 TL'lik asliye davası: nispi ücret 40.000 TL, maktu alt sınır 45.000 TL olduğundan **45.000 TL** hükmedilir.
  - 100.000 TL'lik icra takibi: nispi ücret 16.000 TL. Borçlu süresinde öderse ¾'ü olan **12.000 TL** takdir edilir.

## Önceki tarifeler (md.21 için)
04/11/2025'ten önce tamamlanan hukuki yardımda veya verilen hükümde o tarihte yürürlükteki tarife uygulanır (md.21). Üç tarife de yayımı tarihinde yürürlüğe girer (her birinin md.24'ü).

| Tarife | Uygulandığı dönem | Not |
|---|---|---|
| AAÜT, RG 21/09/2023-32316 | 21/09/2023 – 02/10/2024 | md.14/5, RG 03/10/2024-32681 ile değişti |
| AAÜT, RG 03/10/2024-32681 | 03/10/2024 – 03/11/2025 | |
| AAÜT, RG 04/11/2025-33067 | 04/11/2025'ten beri | Bu dosyanın tabloları |

- Önceki iki tarifenin ücret tabloları (ekleri) bu dosyada **yoktur**. Ekler RG'de ayrı PDF olarak yayımlanır ve birincil metinden okunamadı. `aaut_hesap.py` de yalnız 2025 tarifesiyle hesap yapar.
- Eski tarihli iş için tutarı RG ekinden kontrol edin; bu dosyadaki 2025 tutarlarını kullanmayın.
- [Kaynak: resmigazete.gov.tr, 21/09/2023-32316 ve 03/10/2024-32681 sayıları (md.21 ve md.24 metinleri okundu); RG fihristi 01/10/2025–12/10/2026]

## Vergiye çeviri örnekleri (`aaut_hesap.py karsi-taraf`)
| Durum | e-SMM brüt | KDV | Stopaj | Avukata ödenecek | Makbuz kime |
|---|---|---|---|---|---|
| 45.000 TL hükmedildi, kararda "KDV hariç" yok, ödeyen **şirket** | 37.500 | 7.500 | 7.500 | 37.500 | Davayı kaybeden şirket |
| Aynısı, ödeyen **GVK 94/1'de sayılmayan gerçek kişi** (ticari veya mesleki faaliyeti yok ya da dava bu faaliyetle ilgisiz) | 37.500 | 7.500 | 0 | 45.000 | Davayı kaybeden kişi |
| Kararda "45.000 TL + KDV" yazıyor, ödeyen şirket | 45.000 | 9.000 | 9.000 | 45.000 | Davayı kaybeden şirket |
| Ödeyen **5018 cetvellerindeki kamu idaresi** (ör. bakanlık; KDV GUT I/C-2.1.3.2.13 listesinde), KDV dahil tutar tevkifat sınırını aşıyor | 37.500 | 7.500 | 7.500 | 33.750 (5/10 KDV tevkifatı 3.750) | Kamu idaresi. Bkz. `kdv.md` §4 |
| Ödeyen **belediye** (belirlenmiş alıcı değil) | 37.500 | 7.500 | 7.500 | 37.500 (KDV tevkifatı yok) | Belediye. Belediye GVK 94 sorumlusudur, %20 stopajı keser. Büyükşehir belediyesinin su ve kanalizasyon idaresi ile belediyelerin kurduğu birlikler ise listededir; onlarda bir üstteki satırdaki gibi 5/10 uygulanır. Bkz. `kdv.md` §4 (özelgeler 30252, 30257) |

> CMK görevlendirmesinde (md.14/1 ve 14/4) hükmedilen maktu ücretten CMK kapsamında ödenen ücret mahsup edilir. CMK ücretinin kendisi Cumhuriyet Başsavcılığı adına e-SMM ile belgelenir; bkz. `ek-faaliyetler.md` ve `kdv.md`.
