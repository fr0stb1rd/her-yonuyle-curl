# curl kullanıcıları

![yirmi milyar kurulum](20-billion.jpg)

Dünyada yirmi milyardan fazla curl kurulumu olduğunu tahmin ediyoruz. Söylemesi iyi bir söz ama gerçekte, elbette elimizde bu kadar kesin bir sayı yok. Sadece gözlemlere ve eğilimlere dayanarak tahmin ediyor ve varsayımda bulunuyoruz. Ayrıca bu, tam olarak neyi "bir kurulum" olarak kabul ettiğimize de bağlıdır. Hadi biraz açalım.

## Açık Kaynak

Projenin Açık Kaynak olması ve özgürce lisanslanması, hemen hemen herkesin curl'ü kaynak formatında veya ikili (binary) bir formda yerleşik olarak yeniden dağıtabileceği anlamına gelir.

## İndirmeleri sayma

curl komut satırı aracı ve libcurl kütüphanesi, çoğu işletim sistemi için curl web sitesi aracılığıyla indirilebilir, birçoğuna üçüncü taraf yükleyiciler aracılığıyla sağlanır ve hatta daha fazla işletim sistemiyle varsayılan olarak yüklü gelir. Bu, curl web sitesinden yapılan indirmeleri saymayı bir ölçüm aracı olarak tamamen uygunsuz hale getirir.

## Kullanıcıları bulma

Yani, indirmeleri sayamıyoruz ve herkes onu yeniden dağıtabilir; ve kimse bize curl kullandığını söylemek zorunda değil. Sayıları nasıl belirleyebiliriz? Kullanıcıları nasıl bulabiliriz? Cevap, makul bir doğruluk seviyesiyle gerçekten yapamayacağımızdır.

Bunun yerine tanık raporlarına, ikincil kanıtlara (circumstantial evidence), İnternet'teki bulgulara, curl'den bahseden ara sıra görülen "hakkında kutusu" veya lisans sözleşmesine ya da yazarların yardım isteyip kullanımlarından bahsetmelerine güveniyoruz.

curl lisansı, kullanıcıların bunu bir yerde, örneğin belgelerde tekrarlamaları gerektiğini söyler, ancak çoğu durumda bunu bulmamız kolay değildir ve küçük lisans gereksinimine uymamaya karar verirlerse bu konuda yapabileceğimiz bir şey de yoktur.

## Komut satırı aracı kullanıcıları

Komut satırı aracı curl, dünya çapındaki programcılar tarafından kabuk (shell) ve toplu iş (batch) komut dosyalarında (scripts), sunucularda hata ayıklamak ve bir şeyleri test etmek için yaygın olarak kullanılır. Her gün milyonlarca kişi tarafından kullanıldığına şüphe yok.

## Gömülü kütüphane

libcurl, projemizin gerçekten büyük bir kullanıcı hacmine ulaşmasını sağlayan şeydir. İstemci taraflı dosya transfer yeteneklerini uygulamanıza hızlı ve kolay bir şekilde dahil etme yeteneği birçok kullanıcı için arzu edilir ve ardından libcurl'ün mükemmel taşınabilirliği de yardımcı olur: Çok çeşitli platformlarda aşağı yukarı aynı uygulamayı yazabilir ve transferler için libcurl'ü kullanmaya devam edebilirsiniz.

libcurl'ün C ile yazılmış olması ve hiç veya çok az sayıda zorunlu bağımlılığa sahip olması, gömülü sistemlerde kullanılmasına da yardımcı olur.

libcurl; akıllı telefon işletim sistemlerinde, araç bilgi-eğlence sistemlerinde, televizyon setlerinde, set üstü kutularda (set-top boxes), Blu-Ray oynatıcılar ve üst düzey alıcılar gibi ses ve video ekipmanlarında popüler olarak kullanılır. Genellikle ev yönlendiricilerinde ve yazıcılarda kullanılır.

Çok sayıda en çok satan oyun da, Windows ve oyun konsollarında libcurl kullanıyor.

![hepsi curl çalıştıran farklı cihazlar, araçlar, uygulamalar ve hizmetler](curl-runs-in-all-your-devices.jpg)

## Web sitesi arka uçlarında (backends)

PHP için libcurl bağlayıcısı (binding), libcurl'ün gerçekten tutulması ve yaygın olarak kullanılması için ilk bağlayıcılardan biriydi, hatta belki de ilkiydi. Hızla PHP kullanıcılarının veri transfer etmesi için varsayılan bir yol olarak benimsendi. PHP artık on yılı aşkın bir süredir bu konumda ve İnternet'te oldukça popüler bir teknoloji olduğu ortaya çıktı (son rakamlar İnternet'teki tüm sitelerin yaklaşık dörtte birinin PHP kullandığını gösteriyor).

Gerçekten yüksek talep gören birkaç site PHP kullanıyor ve arka uçta libcurl kullanıyor. Facebook ve Yahoo bu tür iki sitedir.

## Ünlü kullanıcılar

Hiçbir şey kullanıcıları bize hizmetlerinde veya ürünlerinde curl veya libcurl kullandıklarını söylemeye zorlamaz. Genellikle bunu tesadüfen, diyalogları, belgeleri ve lisans sözleşmelerini okuyarak öğreniriz. Elbette bazı şirketler de bize açıkça söyler.

Web sitemizde, projenin ürünlerini "ticari ortamlarda" kullanan kullanıcıların şirket ve ürün adlarını toplardık. Bunu çoğunlukla diğer büyük markalara hava atmak için yaptık; eğer bu diğer adamlar bize bağlı ürünler geliştirebiliyorsa, belki siz de yapabilirsiniz?

Şirketler listesi yüzlerce isim içeriyor, ancak daha büyük veya daha iyi bilinen markalardan bazılarını çıkarırsak, işte elbette sadece küçük bir seçim olan oldukça iyi bir liste:

Adobe, Altera, AOL, Apple, AT&T, BBC, Blackberry, BMW, Bosch, Broadcom, Chevrolet, Cisco, Comcast, Facebook, Google, Hitachi, Honeywell, HP, Huawei, HTC, IBM, Intel, LG, Mazda, Mercedes-Benz, Microsoft, Motorola, NASA, Netflix, Nintendo, Oracle, Panasonic, Philips, Pioneer, RBS, Samsung, SanDisk, SAP, SAS Institute, SEB, Sharp, Siemens, Sony, Spotify, Sun, Swisscom, Tomtom, Toshiba, VMware, Xilinx, Yahoo, Yamaha.

## curl kullanan ünlü yüksek hacimli uygulamalar

Google Youtube uygulaması, Google Photos uygulaması, Spotify, Instagram, Skype (Android'de), iOS ile birlikte gelir, Grand Theft Auto V, Fortnite.
