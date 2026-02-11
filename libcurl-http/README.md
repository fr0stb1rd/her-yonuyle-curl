# libcurl HTTP

HTTP, libcurl kullanıcıları tarafından açık ara en yaygın kullanılan protokoldür ve libcurl, bu tür transferleri değiştirmek için sayısız yol sunar. HTTP protokolünün nasıl çalıştığına dair bazı temel bilgiler için [HTTP protokolü temelleri](../protocols/http.md) bölümüne bakın.

## HTTPS

HTTPS yapmak genellikle HTTP ile aynı şekilde yapılır çünkü ekstra güvenlik katmanı ve sunucu doğrulaması vb. varsayılan olarak otomatik ve şeffaf bir şekilde yapılır. URL'de sadece `https://` şemasını kullanın.

HTTPS, üstünde TLS olan HTTP'dir. Ayrıca [TLS transfer seçenekleri](../transfers/options/tls.md) bölümüne bakın.

## HTTP vekil sunucusu (proxy)

[libcurl ile Vekil Sunucular kullanma](../transfers/conn/proxies.md) bölümüne bakın

## Bölümler

  * [HTTP yanıtları](responses.md)
  * [HTTP istekleri](requests.md)
  * [HTTP sürümleri](versions.md)
  * [HTTP aralıkları](ranges.md)
  * [HTTP kimlik doğrulaması](auth.md)
  * [libcurl ile çerezler](cookies.md)
  * [İndirme](download.md)
  * [Yükleme](upload.md)
  * [Çoğullama (Multiplexing)](multiplexing.md)
  * [HSTS](hsts.md)
  * [alt-svc](alt-svc.md)
