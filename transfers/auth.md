# Kimlik Doğrulama

libcurl ile transfer yapmak genellikle uygulamanın herhangi bir kimlik bilgisi sağlamadan bunu yapmasına olanak tanır. Buna belki de *anonim* olarak diyebilirsiniz.

FTP transferleri için libcurl, kuralın bize söylediği gibi varsayılan bir kullanıcı ve şifre kullanırken, SFTP ve SCP gibi diğer bazı protokollerde transfer büyük olasılıkla başarısız olur. Kimlik doğrulama, bazı transferler için sadece zorunludur.

libcurl için kimlik doğrulama, kimlik bilgileri (kullanıcı + şifre) ve bazı durumlarda ek bir yöntem anlamına gelir: uygulamanın hangi kimlik doğrulama yöntemini kullanacağını seçmesine izin vermek. Her protokolün genellikle kendi setleri vardır.

Kimlik doğrulama yöntemine ve iletimin belki de kimlik doğrulamalı bir güvenlik katmanı (TLS, QUIC veya SSH gibi) kullanmıyor olmasına bağlı olarak, hassas bilgilerin ağ üzerinden sızma riski vardır. Bu riskten kaçınmanın en kolay yolu, kimlik doğrulaması olmayan protokollerle asla kimlik doğrulama kullanmamaktır.

Bazı protokoller veya yöntemler için kimlik doğrulama bağlantı başına yapılırken, diğerleri için transfer başına yapılır. libcurl bunu takip eder ve bağlantıların doğru şekilde yeniden kullanıldığından emin olur. Yani bazen farklı kimlik bilgileri kullanılarak yapılan transferler için bağlantıları yeniden kullanamaz ancak bazen kullanabilir.

## Kullanıcı adı

Kullanıcı adını `CURLOPT_USERNAME` ile düz, null ile sonlandırılmış bir C dizesi olarak ayarlayın.

`CURLOPT_USERPWD` adlı eski seçeneğin kullanılmasından kaçınılması daha iyidir, bunun basit nedeni kullanıcı adı ve şifreyi aynı dizede, iki nokta üst üste ile ayrılmış olarak istemesidir; bu da ad veya şifre iki nokta üst üste içeriyorsa kolayca sorunlara neden olur. Bunun asla olmayacağını garanti etmek zor olabilir.

## Şifre

Kullanılacak şifreyi `CURLOPT_PASSWORD` ile düz, null ile sonlandırılmış bir C dizesi olarak ayarlayın.

## Yöntem

Yöntem seçimi protokole bağlıdır. HTTP özellikleri için [HTTP Kimlik Doğrulaması (HTTP Authentication)](../libcurl-http/auth.md) bölümüne bakın.

# `.netrc`

Unix sistemleri, kullanıcıların uzak FTP sunucuları için kullanıcı adı ve şifrelerini saklamaları için uzun zamandır bir yol sunmaktadır. ftp istemcileri bunu on yıllardır desteklemiş ve bu sayede kullanıcıların her seferinde kimlik bilgilerini manuel olarak girmek zorunda kalmadan bilinen sunuculara hızlı bir şekilde giriş yapmalarına izin verilmiştir. `.netrc` dosyası genellikle bir kullanıcının ev dizininde saklanır.

libcurl, `CURLOPT_NETRC` seçeneğiyle isterseniz `.netrc` dosyasından kimlik bilgilerini almayı destekler.

Bu seçeneğin üç farklı ayarı vardır ve `CURL_NETRC_IGNORED` varsayılandır:

`CURL_NETRC_OPTIONAL` olarak ayarlamak, *.netrc* dosyasının kullanımının isteğe bağlı olduğu ve URL'de sağlanan kullanıcı bilgilerinin tercih edileceği anlamına gelir. Dosya, şifreyi bulmak için ana bilgisayar ve kullanıcı adı için taranır.

`CURL_NETRC_REQUIRED` ise *.netrc* dosyasının kullanımının gerekli olduğu ve URL'de bulunan herhangi bir kimlik bilgisinin yok sayılacağı anlamına gelir.
