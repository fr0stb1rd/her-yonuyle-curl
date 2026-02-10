# Aralıklar (Ranges)

İstemci uzak bir kaynağın yalnızca ilk 200 baytını veya ortasında bir yerde 300 baytını isterse ne olur? HTTP protokolü, bir istemcinin yalnızca belirli bir veri aralığını istemesine izin verir. İstemci sunucudan bir başlangıç ofseti ve bir bitiş ofseti ile belirli aralığı ister. Hatta şeyleri birleştirebilir ve aynı istekte yan yana bir dizi parça listeleyerek birkaç aralık isteyebilir. Bir sunucu böyle bir isteği yanıtlamak için birden fazla bağımsız parça geri gönderdiğinde, bunları mime sınır dizeleriyle ayrılmış olarak alırsınız ve bunu buna göre ele almak kullanıcı uygulamasına kalmıştır. curl böyle bir yanıtı daha fazla ayırmaz.

Ancak, bir bayt aralığı yalnızca sunucuya yapılan bir istektir. İsteğe saygı duymak zorunda değildir ve sunucunun içeriği istendiğinde anında otomatik olarak oluşturduğu durumlar gibi birçok durumda, bunu yapmayı reddeder ve bunun yerine yine de tam içeriği yanıtlar.

`CURLOPT_RANGE` ile libcurl'ün bir aralık istemesini sağlayabilirsiniz. Bir şeyin ilk 200 baytını istiyorsanız:

    curl_easy_setopt(curl, CURLOPT_RANGE, "0-199");

Veya 200. indisten başlayan dosyadaki her şeyi:

    curl_easy_setopt(curl, CURLOPT_RANGE, "200-");

0. indisten 200 bayt *ve* 1000. indisten 200 bayt alın:

    curl_easy_setopt(curl, CURLOPT_RANGE, "0-199,1000-199");
