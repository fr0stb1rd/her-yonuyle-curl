# Ayrıntılı (Verbose)

curl komutunuz beklediğiniz şeyi yürütmez veya döndürmezse, ilk içgüdüsel tepkiniz her zaman daha fazla bilgi almak için komutu `-v / --verbose` seçeneğiyle çalıştırmak olmalıdır.

Ayrıntılı mod etkinleştirildiğinde, curl daha konuşkan hale gelir ve yaptıklarının çoğunu açıklar ve gösterir. Bilgilendirme testleri ekler ve bunlara '\*' öneki koyar. Örneğin, basit bir HTTP örneği denerken (indirilen verileri 'saved' adlı dosyaya kaydederek) curl'ün ne söyleyebileceğini görelim:

    $ curl -v http://example.com -o saved
    * Rebuilt URL to: http://example.com/

Tamam, yani curl'ü eksik gördüğü bir URL ile çağırdık, bu yüzden bize yardımcı oluyor ve devam etmeden önce sonuna bir eğik çizgi ekliyor.

    *   Trying 93.184.216.34...

Bu bize curl'ün şimdi bu IP adresine bağlanmaya çalıştığını söyler. Bu, 'example.com' adının bir veya daha fazla adrese çözümlendiği ve bunun curl'ün bağlanmaya çalıştığı ilk (ve muhtemelen tek) adres olduğu anlamına gelir.

    * Connected to example.com (93.184.216.34) port 80 (#0)

Çalıştı. curl siteye bağlandı ve burada adın IP adresiyle nasıl eşleştiğini ve hangi portta bağlandığını açıklıyor. '(#0)' kısmı, curl'ün bu bağlantıya verdiği dahili numaradır. Aynı komut satırında birden fazla URL denerseniz, daha fazla bağlantı kullandığını veya bağlantıları yeniden kullandığını görebilirsiniz, bu nedenle bağlantı sayacı curl'ün yapması gerektiğine karar verdiği şeye bağlı olarak artabilir veya artmayabilir.

HTTP yerine `HTTPS://` URL'si kullanırsak, curl'ün sunucunun sertifikasını doğrulamak için CA sertifikalarını nasıl kullandığını ve sunucunun sertifikasından bazı ayrıntıları vb. açıklayan bir sürü satır da vardır. Hangi şifrelerin seçildiği ve daha fazla TLS ayrıntısı dahil.

curl'ün iç yapısından verilen ek bilgilere ek olarak, `-v` ayrıntılı modu ayrıca curl'ün gönderdiği ve aldığı tüm başlıkları göstermesini sağlar. Başlıkları olmayan protokoller için (FTP, SMTP, POP3 vb. gibi), komutları ve yanıtları başlık olarak kabul edebiliriz ve bunlar da `-v` ile gösterilir.

Daha sonra yukarıdaki komuttan görülen çıktıya devam edersek (ancak gerçek HTML yanıtını görmezden gelirsek), curl şunları gösterir:

    > GET / HTTP/1.1
    > Host: example.com
    > User-Agent: curl/7.45.0
    > Accept: */*
    >

Bu, siteye yapılan tam HTTP isteğidir. Bu istek, varsayılan bir curl 7.45.0 kurulumunda nasıl göründüğüdür ve elbette farklı sürümler arasında biraz farklılık gösterebilir ve özellikle komut satırı seçenekleri eklerseniz değişir.

HTTP istek başlıklarının son satırı boş görünüyor ve öyledir. Başlıklar ile gövde arasındaki ayrımı belirtir ve bu istekte gönderilecek "gövde" yoktur.

Devam edersek ve her şeyin plana göre gittiğini varsayarsak, gönderilen istek sunucudan karşılık gelen bir yanıt alır ve bu HTTP yanıtı, yanıt gövdesinden önce bir dizi başlıkla başlar:

    < HTTP/1.1 200 OK
    < Accept-Ranges: bytes
    < Cache-Control: max-age=604800
    < Content-Type: text/html
    < Date: Sat, 19 Dec 2015 22:01:03 GMT
    < Etag: "359670651"
    < Expires: Sat, 26 Dec 2015 22:01:03 GMT
    < Last-Modified: Fri, 09 Aug 2013 23:54:35 GMT
    < Server: ECS (ewr/15BD)
    < Vary: Accept-Encoding
    < X-Cache: HIT
    < x-ec-custom-error: 1
    < Content-Length: 1270
    <

Bu size çoğunlukla anlamsız gelebilir, ancak bu, yanıt hakkında normal bir HTTP başlıkları (meta verileri) setidir. İlk satırın "200" olması, oradaki en önemli bilgi parçası olabilir ve "her şey yolunda" anlamına gelir.

Alınan başlıkların son satırı, görebileceğiniz gibi boştur ve bu, HTTP protokolü için başlıkların sonunu belirtmek üzere kullanılan işaretçidir.

Başlıklardan sonra asıl yanıt gövdesi, veri yükü gelir. Normal -v ayrıntılı modu bu verileri göstermez, yalnızca şunu görüntüler:

    { [1270 bytes data]

Bu 1270 baytın 'saved' dosyasında olması gerekir. Yanıtta tam dosya uzunluğunu içeren Content-Length: adında bir başlık olduğunu da görebilirsiniz (ancak yanıtlarda her zaman mevcut olmayabilir).

## HTTP/2 ve HTTP/3

HTTP protokolünün ikinci veya üçüncü sürümünü kullanarak dosya transferleri yaparken, curl **sıkıştırılmış** başlıklar gönderir ve alır. Giden ve gelen HTTP/2 ve HTTP/3 başlıklarını okunabilir ve anlaşılır bir şekilde görüntülemek için curl, sıkıştırılmamış sürümleri HTTP/1.1 ile göründükleri şekle benzer bir tarzda gösterir.

## Sessizlik (Silence)

Ayrıntılı modun tersi, elbette curl'ü daha sessiz yapmaktır. `-s` (veya `--silent`) seçeneğiyle curl'ün ilerleme göstergesini kapatmasını ve hatalar oluştuğunda herhangi bir hata mesajı vermemesini sağlarsınız. Dilsizleşir. Yine de istediğiniz indirilen verileri çıktılar.

Sessizlik etkinleştirildiğinde, `-S` veya `--show-error` ekleyerek hatalarda hata mesajını yine de çıktılamasını isteyebilirsiniz.

 * [İzleme seçenekleri](trace.md)
 * [Yazdır](writeout.md)
