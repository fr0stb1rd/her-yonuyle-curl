# curl olarak kopyala

Bir kullanıcının tarayıcısıyla yapmayı başardığı bir işlemi yeniden oluşturmak için curl kullanmak, yaygın bir istektir ve insanların yardım istediği bir alandır.

Tıpkı tarayıcının alacağı gibi bir kaynağı almak için bir curl komut satırını nasıl güzel ve kolay bir şekilde alırsınız? Chrome, Firefox, Edge ve Safari'nin tümü bu özelliğe sahiptir.

## Firefox'tan

Siteyi Firefox'un ağ araçlarıyla gösterirsiniz. Daha sonra HTTP trafiğini gördüğünüzde "Web Geliştirici->Ağ" (Web Developer->Network) aracında tekrarlamak istediğiniz belirli isteğe sağ tıklarsınız ve beliren menüde "cURL olarak Kopyala"yı (Copy as cURL) seçersiniz. Aşağıdaki ekran görüntüsünün gösterdiği gibi. İşlem daha sonra panonuza bir curl komut satırı oluşturur ve ardından bunu favori kabuk pencerenize yapıştırabilirsiniz. Bu özellik tüm Firefox kurulumlarında varsayılan olarak mevcuttur.

![copy as curl with Firefox](firefox-copy-as-curl.png)

## Chrome ve Edge'den

Chrome veya Edge'de Diğer araçlar->Geliştirici modu'nu (More tools->Developer mode) açtığınızda ve Ağ (Network) sekmesini seçtiğinizde, sitenin kaynaklarını almak için kullanılan HTTP trafiğini görürsünüz. İlgilendiğiniz belirli kaynağın satırında fareyle sağ tıklarsınız ve "cURL olarak Kopyala"yı (Copy as cURL) seçersiniz ve panonuzda sizin için bir komut satırı oluşturur. Transferi yapan bir curl komut satırı elde etmek için bunu bir kabuğa yapıştırın. Bu özellik tüm Chrome ve Chromium kurulumlarında varsayılan olarak mevcuttur. _(Not: Windows'taki Chromium tarayıcıları, Chromium'daki bir [hata](https://bugs.chromium.org/p/chromium/issues/detail?id=1242803) nedeniyle yanlış alıntılanmış hatalı bir komut satırı oluşturabilir)._

![copy as curl with Chrome](chrome-copy-as-curl.png)

## Safari'den

Safari'de, **tercihler->İleri Düzey**'e (preferences->Advanced) gidip etkinleştirene kadar "geliştirme" (development) menüsü görünmez. Bunu yaptıktan sonra, o geliştirme menüsünde **Web denetçisini göster**'i (Show web inspector) seçebilir ve Firefox ve Chrome'un geliştirme araçlarına benzer yeni bir konsolun açıldığını görebilirsiniz.

Ağ sekmesini seçin, web sayfasını yeniden yükleyin ve ardından curl ile almak istediğiniz belirli kaynaklara sağ tıklayabilirsiniz, sanki Safari ile yapmışsınız gibi..

![copy as curl with Safari](safari-copy-as-curl.png)

## Firefox'ta, geliştirici araçlarını (devtools) kullanmadan

Bu daha sık yapmak istediğiniz bir şeyse, sadece komut satırını kopyalamak için geliştirici araçlarını açmayı biraz zahmetli ve kullanışsız bulabilirsiniz. O zaman [cliget](https://addons.mozilla.org/en-US/firefox/addon/cliget/) sizin için mükemmel bir eklentidir çünkü sağ tıklama menüsünde size yeni bir seçenek sunar, böylece Firefox'ta bir resme sağ tıkladığımdaki bu örnek gibi gerçekten hızlı bir şekilde oluşturulmuş hızlı bir komut satırı elde edebilirsiniz:

![cliget with Firefox](firefox-cliget.png)

## Mükemmel değil

Bu yöntemlerin tümü, HTTP transferlerini yeniden üretmeniz için size bir komut satırı verir. Genellikle sorunlarınız için mükemmel çözüm değildirler. Neden? Çoğunlukla bu araçlar kopyaladığınız *aynı* isteği tam olarak yeniden çalıştırmak için yazılmıştır, oysa siz genellikle aynı mantığı yeniden çalıştırmak istersiniz ancak aynı çerezlerin ve dosya içeriklerinin vb. tam bir kopyasını göndermek istemezsiniz.

Bu araçlar, istekte göndermek için size statik ve sabit çerez içeriğine sahip komut satırları verir, çünkü tarayıcının isteklerinde gönderilen çerezlerin içeriği budur. Büyük olasılıkla komut satırını, sunucunun size önceki bir yanıtta söylediği çerezdeki içerik ne olursa olsun dinamik olarak uyum sağlayacak şekilde yeniden yazmak istersiniz. Vb.

Curl olarak kopyala işlevi ayrıca genellikle `-F` kullanma konusunda da kötüdür ve bunun yerine mime ayırıcı dizeleri vb. içeren el yapımı `--data-binary` çözümleri sunarlar.
