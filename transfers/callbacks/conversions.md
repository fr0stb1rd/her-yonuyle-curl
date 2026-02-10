# Ağ veri dönüşümü

libcurl sürüm 7.82.0'a kadar, bu geri çağırımlar ASCII olmayan platformlarda işlerin yürümesi için sağlanıyordu. **Bu geri çağırımlar için destek o zamandan beri kaldırıldı.**

Aşağıdaki belgeler bir süre burada tutulacak ve nasıl çalıştıklarını açıklayacaktır. Gelecek bir tarihte bu kitaptan kaldırılacaktır.

## Ağa ve ağdan dönüştürme geri çağırımları

ASCII olmayan platformlar için `CURLOPT_CONV_FROM_NETWORK_FUNCTION` sağlanır. Bu işlev ağ kodlamasından **(from)** ana bilgisayar kodlamasına **(to)** dönüştürmelidir.

`CURLOPT_CONV_TO_NETWORK_FUNCTION`, **ana bilgisayar** kodlamasından ağ kodlamasına **(to)** dönüştürmelidir. Komutlar veya ASCII verileri ağ üzerinden gönderildiğinde kullanılır.

## UTF-8'den dönüştürme geri çağırımı

`CURLOPT_CONV_FROM_UTF8_FUNCTION`, UTF-8 kodlamasından ana bilgisayar kodlamasına dönüştürmelidir. Yalnızca SSL işlemleri için gereklidir.
