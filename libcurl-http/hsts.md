# HSTS

HSTS, HTTP Strict-Transport-Security'nin kısaltmasıdır. Bir sunucunun bir istemciye, istemcinin gelecekte belirli bir süre boyunca o siteyle HTTPS kullanmayı tercih etmesi gerektiğini söylemesi için tanımlanmış bir yoldur.

HSTS'yi libcurl ile şöyle kullanırsınız.

## Bellek içi önbellek

libcurl, HSTS ana bilgisayarları için birincil olarak bir bellek içi önbelleğe (cache) sahiptir, böylece önbellekte bulunan bir ana bilgisayar adına yapılan sonraki salt HTTP istekleri dahili olarak HTTPS sürümüne "yönlendirilir". Bu özelliğin etkinleştirildiğini varsayarsak.

## Bir handle için HSTS'yi etkinleştir

HSTS, `curl_easy_setopt()` ile `CURLOPT_HSTS_CTRL` seçeneği kullanılarak doğru bit maskesi ayarlanarak etkinleştirilir. Bit maskesinde kullanılabilecek iki ayrı bayrak vardır ancak `CURLHSTS_ENABLE` birincil olanıdır. Bu ayarlanırsa, bu easy handle artık HSTS desteğine sahip olur.

Bu seçenek için mevcut olan ikinci bayrak `CURLHSTS_READONLYFILE`'dır; bu ayarlanırsa, libcurl'e HSTS önbelleği olarak kullanması için belirttiğiniz dosya adının yalnızca okunacağını ve hiçbir şeyin geri yazılmayacağını söyler.

## Bir HSTS önbellek dosyası ayarla

HSTS önbelleğini diskte kalıcı hale getirmek istiyorsanız, `CURLOPT_HSTS` seçeneğiyle bir dosya adı ayarlayın. libcurl bir transferin başlangıcında bu dosyadan okur ve easy handle kapatıldığında (salt okunur ayarlanmadıkça) ona yazar.
