# libcurl nasıl bağlanır (How libcurl connects)

libcurl bir İnternet transferi yapmak üzereyken, önce ana bilgisayar için bir dizi IP adresi almak üzere ana bilgisayar adını *çözer*. Bir ana bilgisayar adının, libcurl'ün ona bağlanabilmesi için en az bir adrese sahip olması gerekir.

Bir ana bilgisayar adı hem IPv4 adreslerine hem de IPv6 adreslerine sahip olabilir ve her ikisinden oluşan bir kümeye sahip olabilirler.

Ana bilgisayar yalnızca tek bir IP ailesine ait adresler döndürürse, libcurl her adres üzerinde yinelenir ve bağlanmayı dener. Bir IP için bağlanma girişimi başarısız olursa, libcurl tüm liste tükenene kadar bir sonraki girişi denemeye devam eder.

Bir uygulama, `CURLOPT_IPRESOLVE` ayarlayarak libcurl'ün hangi IP sürümlerini kullanacağını sınırlayabilir.

## Happy Eyeballs

Bir ana bilgisayar için hem IPv4 hem de IPv6 adreslerini aldığında, libcurl önce bir IPv6 adresine bağlanmayı dener ve kısa bir gecikmeden sonra ilk IPv4 adresine bağlanmayı dener - aynı anda ve paralel olarak. Girişimlerden biri başarılı olduğunda, diğerleri atılır. Her iki aileyi aynı anda kullanarak bağlanmaya çalışma yöntemine **Happy Eyeballs** denir ve İnternet istemcileri için yaygın olarak kabul edilen en iyi uygulamadır.

Bir uygulama, Happy Eyeball prosedüründe ikinci aile bağlanma girişiminin başlayacağı gecikmeyi `CURLOPT_HAPPY_EYEBALLS_TIMEOUT_MS` kullanarak ayarlayabilir.

## Zaman aşımı ve yarıya indirme

Bağlantı aşamasının izin verilen maksimum bir süresi vardır (`CURLOPT_CONNECTTIMEOUT_MS` ile ayarlanır), varsayılan olarak 300 saniyedir. Bu süre içinde hiçbir bağlantı başarılı olmazsa tüm bağlanma prosedürü başarısız sayılır.

libcurl'ün bağlanmayı deneyecek birden fazla adresi kaldığında ve 600 milisaniyeden fazla süresi kaldığında, bu girişim için kalan sürenin en fazla yarısına izin verir. Bu, tek bir kara delik (sink-hole) adresinin libcurl'ün tüm zaman aşımı süresini o kötü giriş üzerinde harcamasını önlemek içindir.

Örneğin: zaman aşımının bitmesine 1000 milisaniye kaldıysa ve bağlanmayı deneyecek iki IP adresi kaldıysa, libcurl bir sonraki girişimde yalnızca 500 milisaniyeye izin verir.

Bunun yerine zaman aşımının bitmesine yalnızca 600 milisaniye kaldıysa ve bağlanmayı deneyecek iki IP adresi kaldıysa, libcurl başarılı olması için çok kısa olmaması adına bir sonraki girişimde kalan tüm zaman aşımı süresine izin verir. Zaman aşımı yarıya indirme yaklaşımı yalnızca 600 milisaniyeden fazla süre kaldığı sürece yapılır.

## HTTP/3

libcurl'den HTTP/3 kullanmasını isteyen uygulamalar için, başka bir Happy Eyeballs katmanı ekler. HTTP/3, QUIC üzerinde çalışır ve QUIC, TCP'den farklı bir taşıma protokolüdür ve bazen engellenen veya aksi takdirde TCP kadar iyi çalışmayan bir mekanizmadır. Bunun getirdiği sorunları düzeltmek amacıyla libcurl, yukarıda açıklanan farklı IP sürümü bağlantılarına ek olarak normal TCP bağlantılarıyla *paralel olarak* QUIC bağlantıları gerçekleştirir.

libcurl bir ana bilgisayar için hem IPv4 hem de IPv6 adreslerini aldığında ve ana bilgisayarla HTTP/3 yapmak istediğinde, şöyle ilerler:

1. Bir IPv6 QUIC bağlanma girişimi başlat, IPv6 adresleri üzerinde yinele
2. Kısa bir gecikmeden sonra, bir IPv4 QUIC bağlanma girişimi başlat, IPv4 adresleri üzerinde yinele
3. Kısa bir gecikmeden sonra, bir IPv6 TCP bağlanma girişimi başlat, IPv6 adresleri üzerinde yinele
4. Kısa bir gecikmeden sonra, bir IPv4 TCP bağlanma girişimi başlat, IPv4 adresleri üzerinde yinele

Bir bağlanma girişimi başarılı olduğunda, diğerlerinin tümü hemen atılır.

HTTP/3 happy eyeballing, libcurl'den `CURL_HTTP_VERSION_3` kullanması istendiğinde yapılır ancak `CURL_HTTP_VERSION_3ONLY` olarak ayarlandığında yapılmaz.
