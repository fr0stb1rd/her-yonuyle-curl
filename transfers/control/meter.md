# İlerleme ölçer (Progress meter)

libcurl'ün stderr'de bir ilerleme ölçer çıktısı vermesi sağlanabilir. Bu özellik varsayılan olarak devre dışıdır ve adında garip bir olumsuzlama bulunan seçeneklerden biridir: `CURLOPT_NOPROGRESS` - ilerleme ölçeri *devre dışı bırakmak* için `1L` olarak ayarlayın. Etkinleştirmek için `0L` olarak ayarlayın.

Transferi durdurmak için hata döndür

Kodda şuna benzer görünebilir:

    #include <stdio.h>
    #include <curl/curl.h>

    int main(void)
    {
      CURL *curl;
      CURLcode res = CURLE_OK;

      curl = curl_easy_init();
      if(curl) {
        /* ilerleme ölçeri etkinleştir */
        curl_easy_setopt(curl, CURLOPT_NOPROGRESS, 0L);

        curl_easy_setopt(curl, CURLOPT_URL, "https://curl.se/");

        res = curl_easy_perform(curl);

        curl_easy_cleanup(curl);
      }

      return (int)res;
    }
