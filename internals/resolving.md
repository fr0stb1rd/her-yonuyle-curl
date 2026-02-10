# Ana bilgisayar adlarını çözümleme (Resolving hostnames)

 Yani `hostip.c` açıklandı

 `host*.c` kaynak dosyasını okurken akılda tutulması gereken ana derleme zamanı tanımları şunlardır:

## `CURLRES_IPV6`

 bu ana bilgisayarın `getaddrinfo()` ve ailesine sahip olduğu ve dolayısıyla bunu kullandığımız anlamına gelir. Ana bilgisayar IPv6'yı çözümleyemeyebilir, ancak bunu gerçekten hesaba katmamız gerekmez. IPv6 özellikli olmayan ana bilgisayarlarda `CURLRES_IPV4` tanımlıdır.

## `CURLRES_ARES`

 libcurl asenkron ad çözümlemeleri için c-ares kullanacak şekilde oluşturulmuşsa tanımlanır. Bu Windows veya \*nix olabilir.

## `CURLRES_THREADED`

 libcurl asenkron ad çözümlemeleri için iş parçacığı (threading) kullanacak şekilde oluşturulmuşsa tanımlanır. Ad çözümlemesi yeni bir iş parçacığında yapılır ve desteklenen asenkron API, ares derlemeleriyle aynıdır. Bu (yerel) Windows altında varsayılandır.

 Önceki ikisinden herhangi biri tanımlanmışsa, `CURLRES_ASYNCH` de tanımlanır. libcurl asenkron bir çözümleyici kullanacak şekilde oluşturulmamışsa, `CURLRES_SYNCH` tanımlanır.

## `host*.c` kaynakları

 `host*.c` kaynak dosyaları şu şekilde bölünmüştür:

 - `hostip.c`      - yöntemden bağımsız çözümleyici işlevleri ve yardımcı işlevler
 - `hostasyn.c`    - asenkron ad çözümlemeleri için işlevler
 - `hostsyn.c`     - senkron ad çözümlemeleri için işlevler
 - `asyn-ares.c`   - c-ares kullanan asenkron ad çözümlemeleri için işlevler
 - `asyn-thread.c` - iş parçacığı kullanan asenkron ad çözümlemeleri için işlevler
 - `hostip4.c`     - IPv4'e özgü işlevler
 - `hostip6.c`     - IPv6'ya özgü işlevler

 `hostip.h`, tüm bunlar için tek birleşik başlık dosyasıdır. `config*.h` ve `curl_setup.h` tanımlarına dayanarak `CURLRES_*` tanımlarını tanımlar.
