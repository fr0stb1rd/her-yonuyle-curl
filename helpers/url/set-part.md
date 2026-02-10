# URL parçalarını ayarla (Set URL parts)

API, uygulamanın `CURLU` handle içinde tutulan bir URL'nin bireysel parçalarını, tam bir URL'yi ayrıştırdıktan sonra veya böyle bir ayrıştırma yerine ayarlamasına olanak tanır.

    rc = curl_url_set(urlp, CURLUPART_HOST, "www.example.com", 0);
    rc = curl_url_set(urlp, CURLUPART_SCHEME, "https", 0);
    rc = curl_url_set(urlp, CURLUPART_USER, "john", 0);
    rc = curl_url_set(urlp, CURLUPART_PASSWORD, "doe", 0);
    rc = curl_url_set(urlp, CURLUPART_PORT, "443", 0);
    rc = curl_url_set(urlp, CURLUPART_PATH, "/index.html", 0);
    rc = curl_url_set(urlp, CURLUPART_QUERY, "name=john", 0);
    rc = curl_url_set(urlp, CURLUPART_FRAGMENT, "anchor", 0);
    rc = curl_url_set(urlp, CURLUPART_ZONEID, "25", 0);

API her zaman üçüncü argümanda null ile sonlandırılmış bir `char *` dizesi veya alanı temizlemek için NULL bekler. Port numarasının da bu şekilde bir dize olarak sağlandığını unutmayın.

Kullanıcı dördüncü argümanda `CURLU_URLENCODE` bayrağıyla istemedikçe, ayarlanan parçalar URL kodlamasına tabi tutulmaz.

## Parçaları güncelle

Bireysel bir parçayı ayarlayarak, örneğin önce tam bir URL ayarlayabilir, ardından o URL'nin tek bir bileşenini güncelleyebilir ve ardından o URL'nin güncellenmiş sürümünü çıkarabilirsiniz.

Örneğin, şöyle bir URL'miz olduğunu varsayalım

    const char *url="http://joe:7Hbz@example.com:8080/images?id=5445#footer";

ve o URL'deki ana bilgisayarı bunun yerine `example.net` olacak şekilde değiştirmek istiyoruz, bu şöyle yapılabilir:

    CURLU *h = curl_url();
    rc = curl_url_set(h, CURLUPART_URL, url, 0);

Sonra ana bilgisayar adı parçasını değiştirin:

    rc = curl_url_set(h, CURLUPART_HOST, "example.net", 0);

ve bu artık şu URL'yi tutar:

    http://joe:7Hbz@example.net:8080/images?id=5445#footer

Daha sonra devam edip yol parçasını `/foo` olarak şöyle değiştirirseniz:

    rc = curl_url_set(h, CURLUPART_PATH, "/foo", 0);

ve URL handle artık şu URL'yi tutar:

    http://joe:7Hbz@example.net:8080/foo?id=5445#footer

vb...
