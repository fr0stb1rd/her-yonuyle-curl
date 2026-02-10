# curl easy seçenekleri

O transferin nasıl yapılacağını kontrol etmek için easy handle'da seçenekler ayarlarsınız veya bazı durumlarda aslında seçenekleri ayarlayabilir ve transfer devam ederken transferin davranışını değiştirebilirsiniz. Seçenekleri `curl_easy_setopt()` ile ayarlarsınız ve handle'ı, ayarlamak istediğiniz seçeneği ve seçeneğin argümanını sağlarsınız. Tüm seçenekler tam olarak bir argüman alır ve `curl_easy_setopt()` çağrılarına her zaman tam olarak üç parametre iletmelisiniz.

`curl_easy_setopt()` çağrısı birkaç yüz farklı seçeneği kabul ettiğinden ve çeşitli seçenekler çeşitli farklı türde argümanları kabul ettiğinden, ayrıntıları okumak ve tam olarak o seçeneğin desteklediği ve beklediği argüman türünü sağlamak önemlidir. Yanlış türü iletmek, beklenmedik yan etkilere veya anlaşılması zor aksaklıklara yol açabilir.

Belki de her transferin ihtiyaç duyduğu en önemli seçenek URL'dir. libcurl hangi URL ile ilgili olduğunu bilmeden bir transfer gerçekleştiremez, bu yüzden ona söylemelisiniz. Tüm seçenekler `CURLOPT_` ve ardından açıklayıcı adla - tümü büyük harfler kullanılarak - ön eklendiğinden, URL seçeneği adı `CURLOPT_URL`'dir. `http://example.com` HTTP içeriğini almak için URL'yi ayarlayan örnek bir satır şöyle görünebilir:

    CURLcode ret = curl_easy_setopt(easy, CURLOPT_URL, "http://example.com");

Tekrar: bu sadece handle'daki seçeneği ayarlar. Gerçek transferi veya herhangi bir şeyi yapmaz. Sadece libcurl'e verilen dizeyi kopyalamasını söyler ve eğer bu çalışırsa OK döndürür.

Hiçbir şeyin yanlış gitmediğini görmek için dönüş kodunu kontrol etmek elbette iyi bir formdur.

## Seçenekleri al

`curl_easy_setopt()` ile daha önce ayarlanmış değerleri çıkarmanın bir yolu yoktur. Daha önce ayarladığınız bilgileri tekrar çıkarabilmeniz gerekiyorsa, bu verileri uygulamanızda kendinizin takip etmesini öneririz.

* [Sayısal seçenekleri ayarla](num.md)
* [Dize (string) seçeneklerini ayarla](strings.md)
* [TLS seçenekleri](tls.md)
* [Tüm seçenekler](all.md)
* [Seçenek bilgisini al](info.md)
