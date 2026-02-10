# Kimlik Doğrulama

Her HTTP isteği kimlik doğrulamalı hale getirilebilir. Bir sunucu veya vekil sunucu, kullanıcının bir URL'ye erişmek veya bir eylemi gerçekleştirmek için doğru kimlik bilgilerine sahip olduğuna dair kanıt sağlamasını isterse, müşteriye isteğe izin verilmesi için doğru bir HTTP kimlik doğrulama başlığı sağlaması gerektiğini bildiren bir HTTP yanıt kodu gönderebilir.

Kimlik doğrulaması gerektiren bir sunucu, 401 yanıt kodunu ve sunucunun desteklediği tüm kimlik doğrulama yöntemlerini listeleyen ilişkili bir `WWW-Authenticate:` başlığını geri gönderir.

Kimlik doğrulaması gerektiren bir HTTP vekil sunucusu, 407 yanıt kodunu ve vekil sunucunun desteklediği tüm kimlik doğrulama yöntemlerini listeleyen ilişkili bir `Proxy-Authenticate:` başlığını geri gönderir.

Bugünün web sitelerinin çoğunun oturum açma vb. için HTTP kimlik doğrulaması gerektirmediğini, bunun yerine kullanıcılardan web sayfalarında oturum açmalarını istediğini ve ardından tarayıcının kullanıcı ve şifre vb. ile bir POST yayınladığını ve ardından oturum için çerezleri koruduğunu belirtmekte fayda var.

curl'e kimlik doğrulamalı bir HTTP isteği yapmasını söylemek için, kullanıcı adı ve şifre (iki nokta üst üste ile ayrılmış) sağlamak üzere `-u, --user` seçeneğini kullanırsınız. Şöyle:

    curl --user daniel:secret http://example.com/

Bu, curl'ün varsayılan *Basic* HTTP kimlik doğrulama yöntemini kullanmasını sağlar. Evet, gerçekten Basic (Temel) olarak adlandırılır ve gerçekten temeldir. Temel yöntemi açıkça istemek için `--basic` kullanın.

Basic kimlik doğrulama yöntemi, kullanıcı adını ve şifreyi ağ üzerinden açık metin olarak (base64 kodlu) gönderir ve HTTP aktarımı için bundan kaçınılmalıdır.

Tek bir (belirtilen veya ima edilen) kimlik doğrulama yöntemini kullanarak bir HTTP transferi yapmayı isterken, curl kimlik doğrulama başlığını kablodaki ilk isteğe zaten ekler.

curl'ün önce kimlik doğrulamasının gerçekten gerekli olup olmadığını *test etmesini* tercih ederseniz, curl'den bunu bulmasını ve ardından `--anyauth` ile bildiği en güvenli yöntemi otomatik olarak kullanmasını isteyebilirsiniz. Bu, curl'ün isteği kimlik doğrulaması olmadan denemesini ve gerekirse kimlik doğrulamasına geçmesini sağlar:

    curl --anyauth --user daniel:secret http://example.com/

ve aynı kavram, kimlik doğrulama gerektirebilecek HTTP işlemleri için de çalışır:

    curl --proxy-anyauth --proxy-user daniel:secret http://example.com/ \
         --proxy http://proxy.example.com:80/

curl tipik olarak (nasıl oluşturulduğuna bağlı olarak biraz değişebilir) Digest, Negotiate ve NTLM dahil olmak üzere diğer birçok kimlik doğrulama yöntemini de konuşur. Bu yöntemleri de özellikle isteyebilirsiniz:

    curl --digest --user daniel:secret http://example.com/
    curl --negotiate --user daniel:secret http://example.com/
    curl --ntlm --user daniel:secret http://example.com/

## AWS sigv4

Defacto kimlik doğrulama standardı *AWS sigv4*, diğer HTTP kimlik doğrulama mekanizmalarından biraz farklıdır ve bu nedenle onu farklı kullanırsınız.

Bu seçenek, işlem için bir veya daha fazla veri alanı sağladığınız ek bir dize argümanı alır, iki nokta üst üste ile ayrılmış: *sağlayıcı 1*, *sağlayıcı 2*, *bölge* ve *hizmet*.

- *sağlayıcı* (provider), giden kimlik doğrulama başlıkları oluşturulurken algoritma tarafından kullanılan dizelerdir.

- *bölge* (region), bölge adı uç noktadan atlandığında bir kaynak koleksiyonunun coğrafi alanını (bölge kodu) işaret eden bir addır.

- *hizmet* (service), hizmet adı uç noktadan atlandığında bir bulut (hizmet kodu) tarafından sağlanan bir işlevi işaret eden bir dizedir.

Sadece *sağlayıcı 1*'in sağlanması zorunludur. Diğerleri aksi takdirde URL'de kullanılan ana bilgisayar adından çıkarılır.

Örnek:

    curl --aws-sigv4 "aws:amz:us-east-2:es" --user "key:secret" \
        https://example.com
