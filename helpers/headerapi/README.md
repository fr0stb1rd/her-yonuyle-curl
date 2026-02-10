# Başlıklar (Headers) API

libcurl, alınan tüm HTTP başlıkları üzerinde yineleme yapmak ve belirli olanlardan içerik çıkarmak için bir API sunar.

Başlık içeriğini döndürürken libcurl, baştaki ve sondaki boşlukları kırpar ancak içeriği başka hiçbir şekilde değiştirmez veya modifiye etmez.

Bu API resmi hale getirildi ve libcurl 7.84.0'dan itibaren gerçek anlamda sağlandı.

## Başlık kökenleri (Header origins)

HTTP başlıkları, bir transfer sırasında sunucudan birkaç farklı *kökenden* gönderilen anahtar değer çiftleridir. libcurl tüm başlıkları toplar ve uygulamalar için bunlara kolay erişim sağlar.

HTTP başlıkları şu şekillerde gelebilir:

1. **CURLH_HEADER** - normal yanıt içeriğinden önce.
2. **CURLH_TRAILER** - yanıt içeriğinden *sonra* gelen alanlar
3. **CURLH_CONNECT** - asıl sunucu isteğinden önce yapılmış olabilecek proxy `CONNECT` isteğindeki yanıt başlıkları
4. **CURLH_1XX** - aşağıdaki >= 2xx yanıt kodundan önce gelmiş olabilecek olası 1xx HTTP yanıtlarındaki başlıklar.
5. **CURLH_PSEUDO** - iki nokta üst üste (`:`) ile başlayan HTTP/2 ve HTTP/3 seviyesi başlıklar

## İstek numarası

libcurl ile yapılan tek bir HTTP transferi bir dizi HTTP isteğinden oluşabilir ve başlık API işlevlerine verilen **request** argümanı, hangi belirli bireysel istekten başlıkları istediğinizi belirtmenize olanak tanır. 0 ilk istektir ve daha sonra sayı daha sonraki yönlendirmeler için veya çok durumlu kimlik doğrulama kullanıldığında artar. `-1` iletmek, kullanılan gerçek istek miktarından bağımsız olarak serideki son isteğe bir kısayoldur.

## Başlık katlama (Header folding)

HTTP/1 başlıkları, bir başlıktan sonra bir devam satırı olduğu ve satırı katlanmış hale getirdiği *katlama* (folding) adı verilen kullanımdan kaldırılmış bir formatı destekler.

Başlıklar API'si katlanmış başlıkları destekler ve bu tür içerikleri katlanmamış olarak döndürür - burada farklı parçalar tek bir boşluk karakteriyle ayrılır.

## Ne zaman

İki başlık API işlevi çağrısını, bir transfer sırasında herhangi bir zamanda, hem geri çağırımların içinden hem de dışından çağırmak tamamen mümkündür. Ancak, API'nin yalnızca çağrıldığı andaki başlıkların durumu hakkında bilgi döndürdüğünü, transfer hala devam ederken çağırırsanız bunun nihai durum olmayabileceğini unutmamak önemlidir.

 - [Başlık yapısı](struct.md)
 - [Bir başlık al](get.md)
 - [Başlıklar üzerinde yineleme](iterate.md)
