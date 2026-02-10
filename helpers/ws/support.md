# Destek (Support)

libcurl kurulumunuzun WebSocket'i destekleyip desteklemediğini anlamak için [`curl_version_info()`](../../libcurl/api.md) çağırabilir ve döndürülen yapıdaki `->protocols` alanlarını kontrol edebilirsiniz. Mevcut olması için `ws` ve muhtemelen `wss` içermelidir.

WebSocket, 8.11.0 sürümünden beri varsayılan olarak desteklenmektedir.
