# Hız sınırı (Rate limit)

Bir uygulamanın bir hız sınırı belirlemesine izin verir. Saniyede ayarlanan bayt sayısından daha hızlı veri transfer etmeyin. libcurl daha sonra ortalama hızı birden çok saniyelik bir süre boyunca verilen eşiğin altında tutmaya çalışır.

Alma (`CURLOPT_MAX_RECV_SPEED_LARGE`) ve gönderme (`CURLOPT_MAX_SEND_SPEED_LARGE`) için ayrı seçenekler vardır.

İşte kullanımını gösteren örnek bir kaynak kodu:

    #include <stdio.h>
    #include <curl/curl.h>

    int main(void)
    {
      CURL *curl;
      CURLcode res = CURLE_OK;

      curl = curl_easy_init();
      if(curl) {
        curl_off_t maxrecv = 31415;
        curl_off_t maxsend = 67954;

        curl_easy_setopt(curl, CURLOPT_MAX_RECV_SPEED_LARGE, maxrecv);
        curl_easy_setopt(curl, CURLOPT_MAX_SEND_SPEED_LARGE, maxsend);

        curl_easy_setopt(curl, CURLOPT_URL, "https://curl.se/");

        res = curl_easy_perform(curl);

        curl_easy_cleanup(curl);
      }

      return (int)res;
    }
