# TLS arka uçları (backends)

curl derlendiğinde, belirli bir TLS kütüphanesini kullanması söylenir. O TLS kütüphanesi, curl'e kablo üzerinden TLS konuşma yetkileri sağlayan motordur. Bunlara genellikle farklı "arka uçlar" (backends) deriz çünkü bunlar curl makinesine takılabilen farklı parçalar olarak görülebilir. curl bu arka uçlardan birini veya birkaçını kullanabilecek şekilde derlenebilir.

Bazen özellikler ve davranışlar, curl farklı TLS arka uçlarıyla derlendiğinde biraz farklılık gösterir ancak geliştiriciler bu farklılıkları mümkün olduğunca küçük ve fark edilemez hale getirmek için çok çalışırlar.

[curl --version](../../cmdline/curlver.md) ile curl sürüm bilgilerini göstermek, çıktının ilk satırında TLS kütüphanesini ve sürümünü içerir.

## Çoklu TLS arka uçları

curl *birden fazla* TLS arka ucuyla derlendiğinde, her başlatıldığında hangisini kullanacağı söylenebilir. Bir tanesi istenmedikçe her zaman varsayılan olarak belirli bir tanesini kullanacak şekilde derlenir.

Birden fazla arka uca sahip bir curl için `curl --version`'ı çağırırsanız, son satırda bir özellik olarak `MultiSSL`'den bahseder. İlk satır, varsayılan olmayanları parantez içinde olmak üzere desteklenen tüm TLS arka uçlarını içerir.

Kullanılacak belirli bir tanesini ayarlamak için `CURL_SSL_BACKEND` ortam değişkenini adına ayarlayın.
