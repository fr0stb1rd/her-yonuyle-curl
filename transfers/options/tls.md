# TLS seçenekleri

Bunu yazarken, libcurl'ün SSL ve TLS'yi nasıl yapacağını kontrol etmek için ayrılmış curl_easy_setopt için **kırktan** az olmayan farklı seçenek vardır.

TLS kullanılarak yapılan transferler güvenli varsayılanları kullanır ancak curl birçok farklı senaryoda ve kurulumda kullanıldığından, bu davranışları değiştirmek isteyeceğiniz durumlara düşme ihtimaliniz vardır.

## Protokol sürümü

`CURLOPT_SSLVERSION` ve `CURLOPT_PROXY_SSLVERSION` ile sizin için kabul edilebilir SSL veya TLS protokol aralığını belirtebilirsiniz. Geleneksel olarak SSL ve TLS protokol sürümleri zamanla kusurlu ve kullanıma uygunsuz bulundu ve curl'ün kendisi zamanla varsayılan alt sürümünü yükseltse bile, yalnızca en son ve en güvenli protokol sürümlerini kullanmayı tercih etmek isteyebilirsiniz.

Bu seçenekler en düşük kabul edilebilir sürümü ve isteğe bağlı olarak maksimumu alır. Sunucu bu koşulla bir bağlantı kuramazsa, transfer başarısız olur.

Örnek:

    curl_easy_setopt(easy, CURLOPT_SSLVERSION, CURL_SSLVERSION_TLSv1_2);

## Protokol ayrıntıları ve davranış

`CURLOPT_SSL_CIPHER_LIST` ve `CURLOPT_PROXY_SSL_CIPHER_LIST` ayarlayarak hangi şifrelerin kullanılacağını seçebilirsiniz.

`CURLOPT_SSL_FALSESTART` ile SSL "False Start"ı etkinleştirmeyi isteyebilirsiniz ve `CURLOPT_SSL_OPTIONS` kullanarak ince ayar yapılacak birkaç başka davranış değişikliği vardır.

## Doğrulama

TLS kullanan bir istemcinin, konuştuğu sunucunun doğru ve güvenilir sunucu olduğunu doğrulaması gerekir. Bu, sunucunun sertifikasının curl'ün genel anahtarına sahip olduğu bir Sertifika Otoritesi (CA) tarafından imzalandığını ve sertifikanın sunucunun adını içerdiğini doğrulayarak yapılır. Bu kontrollerden herhangi birinin başarısız olması, transferin başarısız olmasına neden olur.

Geliştirme amaçları ve deneme için, curl bir uygulamanın sunucu veya bir HTTPS proxy için bu kontrollerden birini veya her ikisini de kapatmasına izin verir.

- `CURLOPT_SSL_VERIFYPEER`, sertifikanın güvenilir bir CA tarafından imzalandığı kontrolünü yönetir.

- `CURLOPT_SSL_VERIFYHOST`, sertifika içindeki adın kontrolünü yönetir.

- `CURLOPT_PROXY_SSL_VERIFYPEER`, `CURLOPT_SSL_VERIFYPEER`'ın proxy sürümüdür.

- `CURLOPT_PROXY_SSL_VERIFYHOST`, `CURLOPT_SSL_VERIFYHOST`'un proxy sürümüdür.

İsteğe bağlı olarak, `CURLOPT_PINNEDPUBLICKEY` veya `CURLOPT_PROXY_PINNEDPUBLICKEY` kullanarak curl'e sertifikanın genel anahtarını bilinen bir karmaya karşı doğrulamasını söyleyebilirsiniz. Burada da bir uyuşmazlık transferin başarısız olmasına neden olur.

## Kimlik Doğrulama

### TLS İstemci sertifikaları

TLS kullanırken ve sunucu istemciden sertifikaları kullanarak kimlik doğrulamasını istediğinde, genellikle `CURLOPT_SSLKEY` ve `CURLOPT_SSLCERT` kullanarak özel anahtarı ve ilgili istemci sertifikasını belirtirsiniz. Anahtarın şifresinin de genellikle `CURLOPT_SSLKEYPASSWD` ile ayarlanması gerekir.

Yine, HTTPS proxy'lerine bağlantılar için aynı seçenek seti ayrı olarak mevcuttur: `CURLOPT_PROXY_SSLKEY`, `CURLOPT_PROXY_SSLCERT` vb.

### TLS yetkilendirmesi

TLS bağlantıları Güvenli Uzak Şifreler (Secure Remote Passwords) adı verilen (nadiren kullanılan) bir özellik sunar. Bunu kullanarak, bir ad ve şifre kullanarak sunucu için bağlantıyı doğrularsınız ve seçenekler `CURLOPT_TLSAUTH_USERNAME` ve `CURLOPT_TLSAUTH_PASSWORD` olarak adlandırılır.

## STARTTLS

Bağlantıyı TLS'ye yükseltmek için STARTTLS yöntemini kullanan protokoller (FTP, IMAP, POP3 ve SMTP) için, genellikle bir URL belirtirken curl'e protokolün TLS olmayan sürümünü kullanmasını söylersiniz ve ardından `CURLOPT_USE_SSL` seçeneğiyle curl'den TLS'yi etkinleştirmesini istersiniz.

Bu seçenek, TLS'ye yükseltemezse curl'ün devam etmesine izin veren bir istemciye izin verir, ancak bu, güvenli olmayan bir protokol kullandığınızı fark etmeden kullanabileceğiniz için önerilen bir yol değildir.

    /* bunun için SSL kullanımını zorunlu kıl, yoksa başarısız ol */
    curl_easy_setopt(curl, CURLOPT_USE_SSL, CURLUSESSL_ALL);
