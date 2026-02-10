# Tarayıcım başka bir şey gösteriyor

Yaygın bir kullanım durumu, URL'yi tarayıcının adres çubuğuna yapıştırdığınızda tarayıcınızda alabileceğiniz bir URL'yi almak için curl kullanmaktır.

Girdi olarak bir URL alan bir tarayıcı, curl'den o kadar çok şey ve o kadar farklı şekillerde yapar ki, curl'ün terminal çıktısında gösterdiği şey muhtemelen tarayıcı pencerenizde gördüğünüz şeyle hiç aynı değildir.

## İstemci farklılıkları

Curl yalnızca tam olarak almasını istediğiniz şeyi alır ve sunucunun teslim ettiği gerçek içeriği —veriyi— asla ayrıştırmaz. Bir tarayıcı veri alır ve aldığı içeriğin türüne bağlı olarak farklı ayrıştırıcıları etkinleştirir. Örneğin, veri HTML ise, bir web sayfasını görüntülemek ve muhtemelen resimler, JavaScript ve CSS dosyaları gibi diğer alt kaynakları indirmek için ayrıştırır. curl HTML indirdiğinde, bir tarayıcı tarafından ayrıştırıldığında bir sürü daha fazla indirmeyi tetikleyecek olsa bile, yalnızca o tek HTML kaynağını alır. curl'ün alt kaynakları da indirmesini istiyorsanız, bu URL'leri curl'e iletmeniz ve tıpkı diğer URL'ler gibi onları almasını istemeniz gerekir.

İstemciler ayrıca isteklerini nasıl gönderdikleri konusunda da farklılık gösterir ve bir kaynak isteğinin bazı yönleri, örneğin biçim tercihlerini, sıkıştırılmış veri istemeyi veya sadece sunucuya hangi önceki sayfadan "geldiğimizi" söylemeyi içerir. curl'ün istekleri, tarayıcınızın isteklerini gönderme şeklinden biraz veya çok farklıdır.

## Sunucu farklılıkları

İsteği alan ve verileri teslim eden sunucu genellikle, kendisiyle iletişim kurduğunu düşündüğü istemci türüne bağlı olarak belirli şekillerde davranacak şekilde ayarlanmıştır. Bazen bu, istemci için en iyi içeriği sunmaya çalışmak kadar masumdur, bazen bazı içerikleri bazı istemciler için gizlemek veya hatta belirli tarayıcılardaki bilinen sorunların etrafından dolaşmaya çalışmaktır. Ayrıca elbette HTTP kimlik doğrulamasına veya çerezlere veya istemcinin önceden doğrulanmış IP adresi aralığından olmasına dayanabilecek çeşitli oturum açma sistemleri de vardır.

Bazen curl kullanarak bir sunucudan bir tarayıcıyla aldığınız yanıtın aynısını almak gerçekten zor bir işe dönüşür. Kullanıcılar daha sonra tipik olarak tarayıcı oturumlarını tarayıcının ağ araçlarıyla kaydeder ve ardından bu kaydı curl'ün `--trace-ascii` seçeneğinden gelen kaydedilmiş verilerle karşılaştırır ve sunucu her ikisine de aynı yanıtı verene kadar curl'ün isteklerini (genellikle `-H / --header` ile) değiştirmeye devam eder.

Bu tür bir çalışma hem zaman alıcı hem de sıkıcı olabilir. Bunu her zaman sunucu sahiplerinden veya yöneticilerinden izin alarak yapmalısınız.

## Aradaki aracıların oynamaları

Aracılar (Intermediaries), açık veya örtük vekil sunuculardır (proxies). Bazı ortamlar sizi bir tane kullanmaya zorlar veya çeşitli nedenlerle bir tane kullanmayı seçebilirsiniz, ancak ağ trafiğinizi sessizce engelleyen ve ne isterseniz isteyin sizin adınıza vekil sunuculuk yapan şeffaf olanlar da vardır.

Vekil sunucular, trafiği sonlandıran ve ardından uzak sunucuya karşı sizin adınıza hareket eden "aracı adamlardır". Bu, her türlü açık filtrelemeyi ve sizi belirli içeriklerden "kurtarmayı" ve hatta uzak sunucuyu ona göndermeye çalıştığınız verilerden "korumayı" getirebilir, ancak daha da fazlası, protokolün nasıl çalıştığına ve yapılacak doğru şeylerin neler olduğuna dair başka bir yazılımın görüşünü getirir.

Müdahale eden aracılar genellikle birçok baş ağrısının ve gizemin, hatta içeriğin düpedüz kötü niyetli modifikasyonlarının nedenidir.

İndirdiğiniz veya yüklediğiniz içeriğin gerçekten uzak sunucunun size gönderdiği veriler olduğunu ve değerli baytlarınızın amaçlanan hedefe kelimesi kelimesine ulaştığını doğrulamak için HTTPS veya diğer yolları kullanmanızı şiddetle tavsiye ederiz.
