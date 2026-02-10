# Yavaş transferleri durdurma

Varsayılan olarak, bir transfer duraklayabilir veya verileri herhangi bir süre boyunca son derece yavaş aktarabilir ve bu bir hata olmaz.

**M** saniye boyunca **N** bayt/sn'nin altındaysa bir transferi durdurun. **N**'yi `CURLOPT_LOW_SPEED_LIMIT` ile ve **M**'yi `CURLOPT_LOW_SPEED_TIME` ile ayarlayın.

Bu seçenekleri gerçek kodda kullanmak şöyle görünebilir:

    #include <stdio.h>
    #include <curl/curl.h>

    int main(void)
    {
      CURL *curl;
      CURLcode res = CURLE_OK;

      curl = curl_easy_init();
      if(curl) {
        /* 60 saniye boyunca 30 bayt/sn'den yavaşsa iptal et */
        curl_easy_setopt(curl, CURLOPT_LOW_SPEED_TIME, 60L);
        curl_easy_setopt(curl, CURLOPT_LOW_SPEED_LIMIT, 30L);

        curl_easy_setopt(curl, CURLOPT_URL, "https://curl.se/");

        res = curl_easy_perform(curl);

        curl_easy_cleanup(curl);
      }

      return (int)res;
    }
