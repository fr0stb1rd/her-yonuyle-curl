# Basit bir HTTP sayfası al (Get a simple HTTP page)

Bu örnek sadece verilen bir URL'den HTML'i getirir ve stdout'a gönderir. Muhtemelen yazabileceğiniz en basit libcurl programıdır.

URL'yi değiştirerek bu, diğer desteklenen protokoller üzerinden de içerik alabilir.

Çıktının stdout'a gönderilmesi varsayılan bir davranıştır ve genellikle aslında istediğiniz şey değildir. Çoğu uygulama bunun yerine gelen verileri almak için bir [yazma geri çağırımı](../transfers/callbacks/write.md) kurar.

    #include <stdio.h>
    #include <curl/curl.h>

    int main(void)
    {
      CURL *curl;
      CURLcode res;

      curl = curl_easy_init();
      if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "http://example.com/");

        /* İsteği gerçekleştir, 'res' dönüş kodunu tutar */
        res = curl_easy_perform(curl);
        /* Hataları kontrol et */
        if(res != CURLE_OK)
          fprintf(stderr, "curl_easy_perform() failed: %s\n",
                  curl_easy_strerror(res));

        /* her zaman temizle */
        curl_easy_cleanup(curl);
      }
      return 0;
    }
