# İçerik Kodlaması (Content Encoding)

## İçerik kodlamaları hakkında

 HTTP/1.1, bir istemcinin sunucunun yanıtını kodlamasını talep edebileceğini belirtir. Bu genellikle, yaygın olarak bulunan sıkıştırma tekniklerinden oluşan bir setten bir (veya daha fazla) kodlama kullanarak bir yanıtı sıkıştırmak için kullanılır. Bu şemalar `deflate` (zlib algoritması), `gzip`, `br` (brotli) ve `compress`'i içerir. Bir istemci, istek belgesine bir `Accept-Encoding` başlığı ekleyerek sunucunun bir kodlama gerçekleştirmesini talep eder. Başlığın değeri tanınan belirteçlerden `deflate`, ... biri olmalıdır (yeni şemaları/belirteçleri kaydetmenin bir yolu vardır, spesifikasyonun bkz. 3.5. bölümü). Bir sunucu, istemcinin kodlama isteğini yerine getirebilir (MAY). Bir yanıt kodlandığında, sunucu yanıta bir `Content-Encoding` başlığı ekler. `Content-Encoding` başlığının değeri, verileri kodlamak için hangi kodlamaların kullanıldığını, uygulandıkları sıraya göre belirtir.

 Bir istemcinin farklı şemalara öncelikler eklemesi de mümkündür, böylece sunucu hangisini tercih ettiğini bilir. `Accept-Encoding` başlığı hakkında daha fazla bilgi için RFC 2616'nın 14.3. bölümüne bakın. `Content-Encoding` başlığı hakkında daha fazla bilgi için [RFC 7231'in 3.1.2.2. bölümüne](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.2.2) bakın.

## Desteklenen içerik kodlamaları

 `deflate`, `gzip`, `zstd` ve `br` içerik kodlamaları libcurl tarafından desteklenir. Hem normal hem de parçalı (chunked) transferler iyi çalışır. `deflate` ve `gzip` kodlamaları için zlib kütüphanesi gereklidir, `br` kodlaması için brotli kod çözme kütüphanesi ve çok şaşırtıcı olmayan bir şekilde libzstd `zstd` yapar.

## libcurl arayüzü

 libcurl'den içerik kodlaması kullanarak bir istek yapmasını istemek için şunu kullanın:

     curl_easy_setopt(curl, CURLOPT_ACCEPT_ENCODING, string);

 burada string, `Accept-Encoding` başlığının amaçlanan değeridir.

 libcurl birden fazla kodlamayı destekler ancak yalnızca `deflate`, `gzip`, `zstd` ve/veya `br` içerik kodlamalarını kullanan yanıtları nasıl işleyeceğini anlar, bu nedenle `CURLOPT_ACCEPT_ENCODING` için çalışan tek değerler (hiçbir şey yapmayan `identity` dışında) `deflate`, `gzip`, `zstd` ve `br`'dir. Bir yanıt `compress` veya yöntemleri kullanılarak kodlanmışsa, libcurl yanıtın çözülemediğini belirten bir hata döndürür. `<string>` NULL ise hiçbir `Accept-Encoding` başlığı oluşturulmaz. `<string>` sıfır uzunluklu bir dizeyse, desteklenen tüm kodlamaları içeren bir `Accept-Encoding` başlığı oluşturulur.

 İçeriğin otomatik olarak kodunun çözülmesi için `CURLOPT_ACCEPT_ENCODING` herhangi bir NULL olmayan değere ayarlanmalıdır. Ayarlanmamışsa ve sunucu yine de kodlanmış içerik gönderirse (istenmemiş olmasına rağmen), veriler ham biçiminde döndürülür ve `Content-Encoding` türü kontrol edilmez.

## curl arayüzü

 Sunuculardan yanıtları curl tarafından desteklenen herhangi bir formatı kullanarak sıkıştırmalarını istemesi için curl ile `--compressed` seçeneğini kullanın.
