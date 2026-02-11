# Dosyaları dahil et (Include files)

URL API'sini kullanmak istediğinizde kodunuza `<curl/curl.h>` dahil edersiniz.

    #include <curl/curl.h>

    CURLU *h = curl_url();
    rc = curl_url_set(h, CURLUPART_URL, "ftp://example.com/no/where", 0);
