# Meta

`curl_ws_recv()` ve `curl_ws_meta()` işlevlerinin ikisi de, gelen WebSocket verileri hakkında bilgi sağlayan bir `curl_ws_frame` yapısına bir işaretçi döndürür. Bu durumda bir WebSocket "çerçevesi", bir WebSocket parçasının bir bölümüdür. Bütün bir parça *olabilir*, ancak yalnızca bir parçası da olabilir. `curl_ws_frame`, size ayrıntıları anlatmak için çerçeve hakkında bilgi içerir.

    struct curl_ws_frame {
      int age;              /* sıfır */
      int flags;            /* CURLWS_* tanımlarına bakın */
      curl_off_t offset;    /* bu verinin çerçeve içindeki ofseti */
      curl_off_t bytesleft; /* yükün kalan bekleyen bayt sayısı */
    };

## `age`

Bu sadece bu yapının yaşını tanımlayan bir sayıdır. Şimdi her zaman 0'dır, ancak gelecekte artabilir ve o zaman yapı büyüyebilir.

## `flags`

`flags` alanı, veri ayrıntılarını tanımlayan bir bit maskesidir.

### `CURLWS_TEXT`

Tampon metin verisi içerir. Bunun WebSocket için bir fark yarattığını ancak libcurl'ün içeriğin herhangi bir doğrulamasını yapmadığını veya gerçekte geçerli UTF-8 içeriği aldığınıza dair önlemler almadığını unutmayın.

### `CURLWS_BINARY`

Bu ikili veridir.

### `CURLWS_FINAL`

Bu mesajın son parçasıdır, bu ayarlanmamışsa, aynı mesajın bir parçası olarak başka bir parçanın geldiği anlamına gelir.

### `CURLWS_CLOSE`

Bu transfer artık kapatıldı.

### `CURLWS_PING`

Bu, bir pong yanıtı bekleyen gelen bir ping mesajıdır.

## `offset`

İletilen veriler yalnızca daha büyük bir parçanın bir bölümü olduğunda, bu, bu parçanın ait olduğu daha büyük parça içindeki bayt sayısı cinsinden ofseti tanımlar.

## `bytesleft`

Bu çerçeveden sonra, bu parçayı tamamlamak için kalan bekleyen yük baytlarının sayısı.

Bir WebSocket parçasının maksimum boyutu 63 bittir.
