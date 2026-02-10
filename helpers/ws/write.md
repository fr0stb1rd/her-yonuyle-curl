# Yaz (Write)

Bir uygulama WebSocket verilerini iki farklı şekilde alabilir, ancak verileri bağlantı üzerinden göndermesi için tek bir yol vardır: `curl_ws_send()` işlevi.

## `curl_ws_send()`

    CURLcode curl_ws_send(CURL *curl, const void *buffer, size_t buflen,
                          size_t *sent, curl_off_t fragsize,
                          unsigned int sendflags);

`curl` - transfer handle'ı

`buffer` - gönderilecek çerçeve verilerine işaretçi

`buflen` - `buffer` içindeki verilerin (bayt cinsinden) uzunluğu

`fragsize` - daha büyük bir parçanın yalnızca bir kısmı gönderilirken kullanılan tüm parçanın toplam boyutu.

`sent` - gönderilen bayt sayısı

`flags` - verileri tanımlayan bit maskesi. Aşağıdaki bit açıklamalarına bakın.

## Tam parça vs kısmi (Full fragment vs partial)

Tam bir WebSocket parçası göndermek için `fragsize`'ı sıfıra ayarlayın ve diğer tüm argümanlar için veri sağlayın.

Bir parçayı daha küçük parçalar halinde göndermek için: ilk kısmı `fragsize` *toplam* parça boyutuna ayarlanmış olarak gönderin. Göndermeden önce tüm parçanın boyutunu bilmeniz ve sağlamanız **gerekir**. Sonraki `curl_ws_send()` çağrılarında, parçanın sonraki parçalarını `fragsize` sıfır olarak ayarlanmış ancak `flags` argümanında `CURLWS_OFFSET` biti ayarlanmış olarak gönderirsiniz. Bütün parçayı oluşturan tüm parçalar gönderilene kadar tekrarlayın.

## Bayraklar (Flags)

### `CURLWS_TEXT`

Tampon metin verisi içerir. Bunun WebSocket için bir fark yarattığını ancak libcurl'ün içeriğin herhangi bir doğrulamasını yapmadığını veya gerçekte geçerli UTF-8 içeriği gönderdiğinize dair herhangi bir önlem almadığını unutmayın.

### `CURLWS_BINARY`

Bu ikili veridir.

### `CURLWS_CONT`

Bu mesajın son parçası değildir, bu da aynı mesajın bir parçası olarak bu bitin ayarlanmadığı başka bir parçanın geldiği anlamına gelir.

### `CURLWS_CLOSE`

Bu transferi kapatın.

### `CURLWS_PING`

Bu bir ping olarak.

### `CURLWS_PONG`

Bu bir pong olarak.

### `CURLWS_OFFSET`

Sağlanan veriler yalnızca kısmi bir parçadır ve sonraki bir `curl_ws_send()` çağrısında daha fazla veri gelmektedir. Bir parçanın yalnızca bir kısmını bu şekilde gönderirken, `fragsize` ilk çağrıda toplam beklenen çerçeve boyutuyla sağlanmalı ve sonraki çağrılarda sıfır olmalıdır.

`CURLWS_OFFSET` ayarlandığında, bu önceki bir gönderimin devamı olduğundan ve parçaları tanımlayan bitler o zaman ayarlandığından başka hiçbir bayrak biti ayarlanmamalıdır.
