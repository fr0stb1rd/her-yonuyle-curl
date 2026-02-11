# CURLOPT\_CURLU

Uygulamalara kolaylık olması açısından, `CURLOPT_URL`'ye alternatif olarak, çalışması için libcurl'e önceden ayrıştırılmış bir URL iletebilirler.

`CURLOPT_CURLU` seçeneğiyle bir URL dizesi yerine bir `CURLU` handle iletirsiniz.

Örnek:

    CURLU *h = curl_url();
    rc = curl_url_set(h, CURLUPART_URL, "https://example.com/", 0);

    CURL *easy = curl_easy_init();
    curl_easy_setopt(easy, CURLOPT_CURLU, h);
