# Kavram (Concept)

Bir libcurl uygulaması, aşağıdaki iki farklı yaklaşımdan birini kullanarak WebSocket yapabilir.

## 1. Geri çağırım yaklaşımı (The callback approach)

Gelen verileri almak için normal [yazma geri çağırımını](../../transfers/callbacks/write.md) kullanmaya ve bu verilere geri çağırımın içinde veya dışında `curl_ws_send` ile yanıt vermeye karar verebilir. Böylece tüm oturumu sunucudan gelen bir indirme biçimi olarak ele alır.

Yazma geri çağırımı içinde, bir uygulama gelen WebSocket verileri hakkında bilgi almak için `curl_ws_meta()` çağırabilir.

## 2. Yalnızca bağlantı yaklaşımı (The connect-only approach)

Bunu yapmanın diğer yolu, yazma geri çağırımını kullanmak uygun değilse, `CURLOPT_CONNECT_ONLY` seçeneğini `2L` değerine ayarlamak ve libcurl'ün yalnızca sunucuya bağlantıyı kuran, WebSocket yükseltmesini yapan ve ardından tamamlanmış sayılan bir transfer yapmasına izin vermektir. O *yalnızca bağlantı* transferinden sonra, uygulama bağlantı üzerinden WebSocket verilerini almak ve göndermek için `curl_ws_recv()` ve `curl_ws_send()` kullanabilir.

## Yükselt ya da öl (Upgrade or die)

Bir `ws://` veya `wss://` URL'si ile transfer yapmak, libcurl'ün WebSocket protokolüne başarılı bir yükseltme yaptığı veya bir hata döndürüldüğü anlamına gelir. Örneğin normal bir HTTP transferinde iyi kabul edilen bir HTTP 200 yanıt kodu, bu nedenle bir WebSocket transferi istendiğinde bir hata olarak kabul edilir.

## Otomatik `PONG`

[Ham mod](options.md) kullanılmıyorsa, libcurl gelen `PING` çerçeveleri için uygun `PONG` yanıtıyla otomatik olarak yanıt verir ve bunları API'de göstermez.
