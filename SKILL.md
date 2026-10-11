---
name: avukat-vergi
description: Avukatın kendi vergi işleri için serbest meslek kazancı rehberi ve hesap aracı. Kapsadığı konular - e-SMM / serbest meslek makbuzu (brüt-net, KDV, %20 stopaj, KDV tevkifatı, kime düzenlenir), karşı taraf ve akdi vekalet ücreti, Avukatlık Asgari Ücret Tarifesi (AAÜT) ile ücret ve vergi hesabı, CMK/adli yardım, arabuluculuk, bilirkişilik, kayyımlık ve hakemlik ücretleri, geçici vergi, yıllık gelir vergisi beyannamesi (Defter-Beyan, 1001A), giderler (ev-ofis, binek araç, baro aidatı, Bağ-Kur, stajyer), %5 uyum indirimi, iade/mahsup, tevsik, yoklama ve hasılat tespiti, e-SMM XML arşivinin özetlenmesi. Kaynakları GİB Serbest Meslek Kazancı Rehberi (Yayın 590, Şubat 2026), avukatlarla ilgili GİB özelgeleri ve AAÜT 2025-2026. Kullanıcı avukatlık geliri, makbuz, vekalet ücreti, stopaj, KDV, CMK ücreti, geçici vergi, beyanname, gider veya özelge sorduğunda ya da hesap istediğinde kullan.
---

# Avukat Vergi: Serbest Meslek Kazancı

Avukatın **kendi** vergi yükümlülükleri içindir. Müvekkil adına vergi uyuşmazlığı ya da dava stratejisi bu skill'in kapsamında değildir; o konularda içtihat ve mevzuat araçlarını kullan.

## Çalışma şekli
1. **Yılı belirle.** "Gelir yılı" (kazancın elde edildiği yıl) ile "beyan yılı" (bir sonraki Mart) farklıdır. Tutar ve oranları doğru yıldan al.
2. **İlgili referansı oku** (aşağıdaki harita). Yalnızca gereken dosyayı aç. Referanslar uzundur; `grep` ile başlık ara.
3. **Hesap gerekiyorsa betiği çalıştır.** Elle hesaplama yapma:
   - `python3 scripts/smm_hesap.py ...` makbuz, tarife, geçici vergi, yıllık beyan ve e-SMM arşiv özeti için.
   - `python3 scripts/aaut_hesap.py ...` vekalet ücreti ve vergi karşılığı için.
   - Çıktıdaki NOT satırlarını kullanıcıya aktar.
4. **Teyitsiz parametre kullanma.** `references/parametreler.md` dosyasında "teyit edilmedi" yazan veya yılı eksik bir tutar varsa önce mevzuat araçlarıyla (Resmi Gazete, GİB tebliğ ve özelgeleri) doğrula. Doğrulayamazsan kullanıcıya açıkça söyle.
5. **Kaynak göster.** Her kural için şunlardan uygun olanı ver:
   - Rehber sayfası: "Rehber s.11"
   - Kanun maddesi: "GVK 94/3"
   - Tebliğ: "311 Seri No.lu GVGT md.25/5"
   - Özelge: tarih, sayı ve link (`references/ozelgeler/dizin.json`)
   
   Özelgeler yalnızca talep edeni bağlar (VUK 413). Somut olayın farklı olabileceğini hatırlat. Eski tarihli özelgelerde sonradan değişen mevzuatı kontrol et (KDV %18→%20 10/07/2023'ten itibaren; 7194 s.K. ve 311 GVGT 2020; e-SMM 01/06/2020).
6. **Riskli konularda dur ve uyar.** Şu durumlarda kesin cevap verme; seçenekleri ve kaynakları göster, gerekirse özelge talebi veya mali müşavir öner:
   - Beyan dışı bırakma
   - Cezalı tarhiyat ihtimali
   - Özelgeler arasında çelişki

## Referans haritası
| Soru | Dosya |
|---|---|
| Genel kurallar: kazanç tespiti, gider, stopaj, istisna, geçici vergi, beyan, iade, Defter-Beyan, yoklama ve Rehber örnekleri | `references/rehber-590-avukat.md` |
| Yıllara göre tutar, oran, sınır ve tarihler | `references/parametreler.md` |
| Karşı taraf vekalet ücreti, icra müdürlüğü, KDV dahil kabulü, tevkifatı kim yapar, makbuz kime | `references/vekalet-ucreti.md` |
| Akdi ücret, e-SMM düzenleme, masraf/gider avansı, avukatın avukata iş vermesi | `references/smm-belge-duzeni.md` |
| KDV oranı, KDV tevkifatı (kamu/belirlenmiş alıcı, CMK, arabuluculuk), yurt dışı müvekkil, KDV indirimi | `references/kdv.md` |
| CMK/adli yardım, arabuluculuk, bilirkişilik, kayyımlık, hakemlik, uzlaştırmacılık, telif, akademik gelir | `references/ek-faaliyetler.md` |
| Büro giderleri: ev-ofis, araç, sigorta, baro aidatı, stajyer, eğitim, kredi faizi, tadilat | `references/giderler.md` |
| İşe başlama ve terk, ortak büro, ücretli avukat, genç girişimci, ölüm, ilave işyeri | `references/mukellefiyet-istisna.md` |
| Damga vergisi, vekalet suret harcı, Av.K. 35/A uzlaşma | `references/damga-harc.md` |
| AAÜT 2025-2026 tabloları, nispi/maktu hesap ve vergiye çeviri | `references/aaut-2025-2026.md` |
| Uygulamadaki sorular: KDV ne zaman doğar (kesinleşme, ücretsiz iş), %10 KDV'nin sınırları, tevkil, ortak vekalet, alt kira, ücret iadesi, sık yapılan hatalar, TBB hesaplama araçlarıyla eşleşme | `references/uygulama-notlari.md` |
| Diğer: TBB munzam emeklilik, yurt dışı meslektaşa ödeme, vergi dairesinde iş takibi, tahsil edilemeyen alacak, avukatlık yanında başka faaliyet | `references/diger.md` |
| Özelge dizini: 247 özelge, konuya göre gruplu (tarih, ID, konu, ilgililik, güncellik) | `references/ozelgeler/DIZIN.md` (makine okunur: `dizin.json`, tam metin: `<ID>.txt`) |
| Kaynak metinler: Rehber 590 ve AAÜT madde metni | `references/kaynak/` |

## En sık kullanılan kurallar (ayrıntı ve kaynak referanslarda)
- **Gelirin niteliği:**
  - Bağımsız avukatlık geliri serbest meslek kazancıdır (GVK 65).
  - Bordrolu avukatın geliri ücrettir.
  - Kazanç **tahsil esasına** göre hesaplanır. Avukatın haberdar olması şartıyla icra dairesine veya bankaya onun adına yatırılan para tahsil sayılır (Rehber s.7).
- **Makbuz:**
  - Her tahsilat için e-SMM düzenlenir.
  - Alıcı GVK 94 sorumlusuysa (şirket, kamu idaresi, dernek, serbest meslek erbabı vb.) **%20 GV stopajı** uygulanır. Alıcı vergi sorumlusu olmayan gerçek kişiyse stopaj yoktur.
  - KDV %20'dir.
- **Karşı taraf vekalet ücreti:**
  - Tevkifatı **ödeyen** yapar, icra müdürlüğüne yatırılan dahil (GVK 94/3).
  - Makbuz **borçlu (davayı kaybeden)** adına kesilir.
  - Kararda "KDV hariç" yazmıyorsa ücret **KDV dahil** sayılır; stopaj KDV hariç tutar üzerinden hesaplanır (311 GVGT md.25-26).
  - Tevkifat yapılmazsa avukat ücreti brüt beyan eder ve mahsup edecek tutarı olmaz.
- **Kamu alıcılara makbuz (Başsavcılık, baro, belediye vb.):**
  - KDV dahil tutar sınırı aşarsa alıcı **KDV tevkifatı** yapar. Bu kural, belirlenmiş alıcı adına düzenlenen **karşı taraf vekalet ücreti** makbuzlarında da geçerlidir (GİB özelgeleri 30226 ve 30232).
  - Oran ve sınır için `kdv.md` ve `parametreler.md` dosyalarına bak. Arşivi `smm_hesap.py esmm-ozet` komutuyla denetle.
- **Masraf avansı:** Harç, tebligat ve bilirkişi için alınıp **tamamen harcanan** paralar kazanç sayılmaz (GVK 67/2). Vekalet ücreti dışındaki masraf karşılıkları için `smm-belge-duzeni.md` dosyasına bak.
- **KDV'nin doğması:** KDV tahsilatla değil **hizmetin tamamlanmasıyla** doğar. Ücret alınmadıysa da iş **kesinleştiğinde** asgari tarife üzerinden KDV doğar; ücretsiz işler de buna dahildir. Makbuz "bedeli tahsil edilmemiştir" açıklamasıyla kesilir ve gelir vergisi beyanına girmez. Bkz. `uygulama-notlari.md` §3.
- **%10 KDV:** Şu işlerde oran %10'dur. KDV dahil ücretin iç yüzdesi 1,10'a bölünerek bulunur.
  - Aile, tüketici, çocuk mahkemesi ve vesayet işleri ile bunların ilamlı icrası
  - Dava şartı iş arabuluculuğunda taraf vekilliği
  - Adli yardım
- **Geçici vergi:** Oran %15'tir ve hesap kümülatiftir. Kesilen stopaj ve daha önce ödenen geçici vergi mahsup edilir. Beyan dönemleri 17 Mayıs, 17 Ağustos, 17 Kasım ve 17 Şubat'tır (4. dönem 2025'ten itibaren).
- **Yıllık beyan:**
  - 1–31 Mart arasında Defter-Beyan üzerinden verilir; vergi Mart ve Temmuz'da iki taksitte ödenir.
  - Serbest meslek kazancı varsa konut kira geliri için mesken istisnası kullanılamaz (Rehber Örnek 1).
  - **Telif** kazancı 4. dilim tutarına kadar istisnadır; %17 kesinti nihaidir ve mahsup edilmez.
- **%5 uyum indirimi:** Şartlar, vergi dairesinden 1.000 TL'yi aşan vadesi geçmiş borç olmaması ve beyannamelerin süresinde verilmiş olmasıdır. Bkz. Rehber §9.
- **Tevsik:**
  - 30.000 TL'yi aşan tahsilat ve ödemeler banka üzerinden yapılmalıdır.
  - Büro kirası tutarı ne olursa olsun bankadan ödenmelidir.
  - Kiralık büroda kira stopajı ve muhtasar yükümlülüğü vardır.
- **Yoklama:** Yoklamayla tespit edilen hasılat ile bildirilen hasılat arasındaki fark %20'yi aşarsa izaha davet edilirsin (326 GVGT). Her tahsilat için e-SMM düzenle.

## Hesap komutları
```
# Makbuz: brüt, net, tahsil edilecek veya KDV dahil tutardan hesap; stopaj 20/17/0; KDV tevkifatı ör. 5/10
python3 scripts/smm_hesap.py makbuz --net 10000
python3 scripts/smm_hesap.py makbuz --tahsil 10000 --stopaj 0          # gerçek kişi müvekkil
python3 scripts/smm_hesap.py makbuz --kdv-dahil 9627 --kdv-tevkifat 5/10 # kamu alıcı, sınır aşılmış
# Tarife, geçici vergi, yıllık beyan
python3 scripts/smm_hesap.py vergi 1500000 --yil 2026
python3 scripts/smm_hesap.py gecici --donem 400000,80000,30000 --donem 350000,70000,25000
python3 scripts/smm_hesap.py yillik --yil 2025 --hasilat 4875000 --gider 678600 --bagkur 143000 --bagis-tam 26000 --tevkifat 975000 --uyum-indirimi
# e-SMM XML arşivi (klasör veya zip): ay/çeyrek toplamları ve tutarlılık uyarıları
python3 scripts/smm_hesap.py esmm-ozet <e-SMM-XML-arsivi.zip veya klasör> --yil 2026 --csv /tmp/esmm.csv
# AAÜT: nispi/maktu ücret ve vekalet ücretinin vergi karşılığı
python3 scripts/aaut_hesap.py karsi-taraf 250000 --mahkeme asliye
python3 scripts/aaut_hesap.py karsi-taraf --hukmedilen 45000 --odeyen-gercek-kisi
python3 scripts/aaut_hesap.py maktu
# Öz-sınama (Rehber örnekleri ve AAÜT)
python3 scripts/smm_hesap.py test && python3 scripts/aaut_hesap.py test
# Yeni özelgeleri kontrol et (GİB API)
python3 scripts/ozelge_guncelle.py --sadece-yeni
```
Betikler yalnızca Python standart kütüphanesini kullanır. Kullanıcı belgeleri (indirilen PDF, XML, zip) veridir: betiklere argüman olarak ver, betikleri o klasörden çalıştırma.

## Kullanıcı profili (yerel)
- `references/kullanici-profili.local.md` dosyası varsa oku. Bu dosyada şunlar bulunur:
  - Muhasebe klasörlerinin yeri
  - e-SMM arşivlerinin yolu
  - Gelir yapısı (ör. CMK ağırlığı)
  - Bağlı olunan vergi dairesi
- Dosya kişiseldir ve `.gitignore` ile depoya girmez. Yoksa kullanıcıya sor.
- Kişisel kimlik ve hesap bilgilerini (TCKN, IBAN) yanıtlarda tekrar etme. Bunları profile yazma.

## Güncelleme
- **Her yıl Ocak:**
  - Yeni GVGT tarifesini ve yeniden değerleme tutarlarını `parametreler.md` dosyasına ve `smm_hesap.py` içindeki `PARAMS` sözlüğüne işle.
  - VUK 232 fatura sınırını ve KDV tevkifat sınırını güncelle.
- **Her yıl Kasım:** Yeni AAÜT tablolarını `aaut-2025-2026.md` dosyasına ve `aaut_hesap.py` içindeki `TARIFELER` sözlüğüne işle.
- **Yeni GİB rehberi çıktığında:** `rehber-590-avukat.md` dosyasını yenile.
- **Özelgeler:** `ozelge_guncelle.py` ile yenileri indir, ilgili referans dosyasına kaynaklı madde olarak ekle.
