# HTTP temelleri

HTTP, temellerini öğrenmesi kolay bir protokoldür. Bir istemci bir sunucuya bağlanır — ve inisiyatifi alan her zaman istemcidir — bir istek gönderir ve bir yanıt alır. Hem istek hem de yanıt, başlıklar (headers) ve bir gövdeden (body) oluşur. Her iki yönde de çok az veya çok fazla bilgi gidebilir.

Bir istemci tarafından gönderilen bir HTTP isteği, bir istek satırı (request line), ardından başlıklar ve isteğe bağlı olarak bir gövde ile başlar. En yaygın HTTP isteği muhtemelen sunucudan belirli bir kaynağı (resource) döndürmesini isteyen ve bir gövde içermeyen GET isteğidir.

Bir istemci 'example.com'a bağlandığında ve '/' kaynağını istediğinde, istek gövdesi olmayan bir GET gönderir:

    GET / HTTP/1.1
    User-agent: curl/2000
    Host: example.com

…sunucu, yanıt başlıkları ve bir yanıt gövdesi ('hello') ile aşağıdaki gibi bir yanıt verebilir. Yanıttaki ilk satır ayrıca yanıt kodunu ve sunucunun desteklediği belirli sürümü de içerir:

    HTTP/1.1 200 OK
    Server: example-server/1.1
    Content-Length: 5
    Content-Type: plain/text

    hello

İstemci bunun yerine küçük bir istek gövdesi ('hello') içeren bir istek gönderirse, şuna benzeyebilir:

    POST / HTTP/1.1
    Host: example.com
    User-agent: curl/2000
    Content-Length: 5

    hello

Bir şeyler ters gitmediği sürece bir sunucu her zaman bir HTTP isteğine yanıt verir.

## URL'in bir isteğe dönüştürülmesi

Bir HTTP istemcisine üzerinde işlem yapması için bir URL verildiğinde, bu URL daha sonra kullanılır, parçalarına ayrılır ve bu parçalar sunucuya giden istekte çeşitli yerlerde kullanılır. Örnek bir URL alalım:

    https://www.example.com/path/to/file

 - **https**, curl'ün 443 numaralı uzak porta TLS kullandığı anlamına gelir (URL'de belirtilmediğinde varsayılan port numarası budur).

 - **www.example.com**, curl'ün bağlanmak için bir veya daha fazla IP adresine çözümlediği ana bilgisayar adıdır (hostname). Bu ana bilgisayar adı, HTTP isteğindeki `Host:` başlığında da kullanılır.

 - **/path/to/file**, HTTP isteğinde sunucuya curl'ün hangi belgeyi/kaynakları almak istediğini söylemek için kullanılır.
