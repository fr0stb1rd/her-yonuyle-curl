# HTTP sürümleri

Diğer herhangi bir İnternet protokolü gibi, HTTP protokolü de yıllar içinde gelişmeye devam etti ve şu anda dünyaya dağılmış ve zaman içinde değişen başarı seviyeleriyle farklı sürümleri konuşan istemciler ve sunucular var. curl'ün URL'lerinizle çalışmasını sağlamak için curl, bir isteğin ve transferin hangi HTTP sürümünü kullanması gerektiğini belirtmeniz için yollar sunar. curl, en yaygın, isterseniz en mantıklı varsayılan değerleri ilk önce kullanmaya çalışacak şekilde tasarlanmıştır ancak bazen bu yeterli olmaz ve o zaman curl'e ne yapması gerektiği konusunda talimat vermeniz gerekebilir.

curl, HTTP sunucuları için varsayılan olarak HTTP/1.1'i kullanır ancak HTTPS'e bağlanırsanız ve yerleşik HTTP/2 yeteneklerine sahip bir curl'ünüz varsa, otomatik olarak HTTP/2'yi müzakere etmeye çalışır veya müzakere başarısız olursa 1.1'e geri döner. HTTP/2 yetenekli olmayan curl'ler varsayılan olarak HTTPS üzerinden 1.1 alır.

| Seçenek                             | Açıklama    |
|-------------------------------------|-------------|
| --http1.0                           | HTTP/1.0
| --http1.1                           | HTTP/1.1
| --http2                             | HTTP/2
| --http2-prior-knowledge             | HTTP/2
| --http3                             | HTTP/3

* [HTTP/0.9](http09.md)
* [HTTP/2](http2.md)
* [HTTP/3](http3.md)
