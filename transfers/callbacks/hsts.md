# HSTS

HSTS (HTTP Strict Transport Security) için libcurl, bir tahsisin kurallar için depolamayı uygulamasına izin vermek üzere iki geri çağırım sağlar. Geri çağırımlar daha sonra kalıcı bir depolamadan HSTS politikalarını okumak ve/veya yazmak üzere ayarlanır.

`CURLOPT_HSTSREADFUNCTION` ile uygulama, HSTS verilerinin libcurl'e okunduğu bir işlev sağlar. `CURLOPT_HSTSWRITEFUNCTION`, verileri yazmak için libcurl'ün çağırdığı karşılık gelen işlevdir.
