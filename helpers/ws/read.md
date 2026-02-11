# Oku (Read)

Bir uygulama, gelen WebSocket trafiğini şu iki yöntemden birini kullanarak alır ve okur:

## Yazma geri çağırımı (Write callback)

`CURLOPT_CONNECT_ONLY` seçeneği **ayarlanmadığında**, WebSocket verileri yazma geri çağırımına iletilir.

Varsayılan çerçeve modunda (ham modun aksine), libcurl veriler geldikçe WebSocket parçalarının bölümlerini geri çağırıma iletir. Uygulama daha sonra geri çağırıma iletilen belirli çerçeve hakkında bilgi almak için `curl_ws_meta()` çağırabilir.

libcurl, kablo üzerinden ne zaman ne geldiğine bağlı olarak tam parçaları veya kısmi olanları iletebilir. Her WebSocket parçası 63 bit boyutunda olabilir.

## `curl_ws_recv`

Yalnızca bağlantı seçeneği ayarlandıysa, transfer uzak ana bilgisayara WebSocket kurulduktan sonra sona erer ve o noktadan sonra uygulamanın WebSocket verilerini okumak için `curl_ws_recv()` ve göndermek için `curl_ws_send()` çağırması gerekir.

`curl_ws_recv` işlevi şu prototipe sahiptir:

    CURLcode curl_ws_recv(CURL *curl, void *buffer, size_t buflen,
                          size_t *recv, struct curl_ws_frame **meta);

`curl` - transferin handle'ı

`buffer` - WebSocket verilerini almak için bir tampona işaretçi

`buflen` - **buffer**'ın bayt cinsinden boyutu

`recv` - dönüşte **buffer**'da saklanan verilerin bayt cinsinden boyutu

`meta` - [alınan çerçeve hakkında bilgi](meta.md) içeren bir yapıya bir işaretçi alır.
