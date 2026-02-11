# curl ne yapar?

cURL bir projedir ve birincil amacı ile odak noktası İnternet transferi ile ilgili Açık Kaynak ürünleri yapmaktır:

- curl, komut satırı aracı

- libcurl, C API'sine sahip transfer kütüphanesi

- trurl, URL ayrıştırıcı ve manipülasyon aracı

- wcurl, basit indirme aracı

İstemci taraflı (client-side) İnternet protokolü transferleriyle ilgili her şey curl'ün işi sayılabilir. Bununla ilgili olmayan şeylerden kaçınılmalı ve diğer projelere ve ürünlere bırakılmalıdır.

curl ve libcurl'ün transfer edilen gerçek verileri işlemekten kaçınmaya çalıştığını da göz önünde bulundurmak önemli olabilir. Örneğin, HTML veya HTTP üzerinden transfer edilmesi popüler olan diğer içerikler hakkında hiçbir bilgisi yoktur, ancak bu tür verilerin HTTP üzerinden nasıl transfer edileceği hakkında her şeyi bilir.

curl ürünleri, İnternet bağlantılı bir dünyada binlerce veya milyonlarca komut dosyasını ve uygulamayı çalıştırmak için sıkça kullanılmakla kalmaz, aynı zamanda sunucu testleri, protokol kurcalamaları ve yeni şeyler denemek için de yaygın olarak kullanılır.

## curl, komut satırı aracı

curl'ü komut satırından çalıştırmak doğaldı ve Daniel, verileri varsayılan olarak stdout'a (standart çıktı), terminale göndermekten başka bir şey düşünmedi. Standart Unix felsefesinin "her şey bir boru (pipe) hattıdır" mantrası Daniel'in inandığı bir şeydi. curl, 'cat' veya diğer Unix araçlarından biri gibidir; ne yapmak istiyorsanız diğer araçlarla zincirlemeyi kolaylaştırmak için verileri stdout'a gönderir. Bu aynı zamanda, bir dosyadan okumaya veya bir dosyaya yazmaya izin veren neredeyse tüm curl seçeneklerinin, bunu stdout'a veya stdin'den (standart girdi) yapmayı seçme yeteneğine de sahip olmasının nedenidir.

Komut satırı araçlarının çalışma şekline ilişkin Unix tarzını takiben, curl'ün komut satırında birden fazla URL'i desteklemesi gerekip gerekmediği konusunda da hiçbir zaman bir soru işareti olmadı.

Komut satırı aracı, komut dosyalarından (scripts) veya diğer otomatik yollardan mükemmel şekilde çalışacak şekilde tasarlanmıştır. Yalnızca metin girişi ve metin çıkışı dışında başka bir GUI veya UI (Kullanıcı Arayüzü) özelliği yoktur.

## libcurl, kütüphane

Komut satırı aracı önce gelse de, ağ motoru sökülüp 2000 yılında bir kütüphaneye dönüştürüldü ve bugün hala sahip olduğumuz kavramlar Ağustos 2000'de libcurl 7.1 ile tanıtıldı. O zamandan beri, komut satırı aracı, tüm ağır işi yapan kütüphanenin etrafında bir araç oluşturan ince bir mantık katmanı olmuştur.

libcurl, yazılımlarına istemci taraflı dosya transfer yetenekleri eklemek isteyen herkes için, herhangi bir platformda, herhangi bir mimaride ve herhangi bir amaçla kullanılabilir olacak şekilde tasarlanmış ve amaçlanmıştır. libcurl ayrıca bunun bir engel haline gelmesini önlemek için son derece özgürce lisanslanmıştır.

libcurl, geleneksel ve muhafazakar C ile yazılmıştır. Diğer dillerin tercih edildiği durumlarda, insanlar onlar için libcurl [bağlayıcıları (bindings)](../bindings/) oluşturmuştur.

Kütüphane, İnternet transferlerinin gerekli olduğu her türlü hayal edilebilir gömülü cihazda (embedded device) kullanılır: araç bilgi-eğlence sistemleri, televizyonlar, Blu-Ray oynatıcılar, set üstü kutular (set-top boxes), yazıcılar, yönlendiriciler, oyun sistemleri vb.

## trurl, bir URL aracı

URL'leri yönetmek, ayrıştırmak ve işlemek zordur. Sadece URL'lerin yetersiz standartlaştırılmış olması ve farklı ayrıştırıcıların aynı URL'i farklı şekilde ayrıştırması nedeniyle değil, aynı zamanda sözdizimlerinin doğru anlaşılmasının zor olması nedeniyle.

trurl, kullanıcıların komut dosyalarında ve komut satırlarında URL'leri ayrıştırmasına, oluşturmasına ve değiştirmesine yardımcı olan bir komut satırı aracıdır. trurl kullanarak, komut dosyaları URL standartlarının inceliklerini çözmek zorunda kalmadan URL'lerden ayrıntıları güvenli bir şekilde çıkarabilir, URL'leri güncelleyebilir veya URL'ler oluşturabilir.

trurl'ü curl ile birlikte kullanmanın bir başka nedeni de, trurl'ün libcurl kullanılarak oluşturulmuş olmasıdır, yani her iki araç da aynı URL ayrıştırıcısını kullanır ve bu nedenle URL'leri tam olarak aynı şekilde anlar ve işler. Bu önemlidir çünkü aynı URL üzerinde karışık URL ayrıştırıcıları kullanmak güvenlik açıklarının yaygın bir nedenidir.

## wcurl, bir URL indirici

Uzun yıllardır, insanların curl'ü URL indirmek için kullanmanın zor olduğunu, çünkü curl'e sadece bunu yaptırmak için (tek bir URL veya iki URL'i yerel bir dosyaya indirmek) gereken tam komut satırı seçeneklerini asla hatırlayamadıklarını söyledikleri ve bildirdikleri görülmüştür. İnsanlar, bu kullanım durumu için alternatif komut satırı araçlarını kullanmaya devam etmelerinin birincil nedeni olarak bunu gösterirlerdi.

wcurl, kullanıcının herhangi bir parametreyi hatırlamasına gerek kalmadan URL'leri basitçe indiren komut satırı aracıdır.
