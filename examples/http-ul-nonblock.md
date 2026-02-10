# Bloklamayan HTTP form-post (Non-blocking HTTP form-post)

Bu örnek, multi arayüzünü kullanarak çok parçalı bir form gönderisi (multipart form-post) yapar.

    #include <stdio.h>
    #include <string.h>
    #include <sys/time.h>

    #include <curl/curl.h>

    int main(void)
    {
      CURL *curl;

      CURLM *multi_handle;
      int still_running = 0;

      curl_mime *form = NULL;
      curl_mimepart *field = NULL;
      struct curl_slist *headerlist = NULL;
      static const char buf[] = "Expect:";

      curl = curl_easy_init();
      multi_handle = curl_multi_init();

      if(curl && multi_handle) {
        /* Formu oluştur */
        form = curl_mime_init(curl);

        /* Dosya yükleme alanını doldur */
        field = curl_mime_addpart(form);
        curl_mime_name(field, "sendfile");
        curl_mime_filedata(field, "multi-post.c");

        /* Dosya adı alanını doldur */
        field = curl_mime_addpart(form);
        curl_mime_name(field, "filename");
        curl_mime_data(field, "multi-post.c", CURL_ZERO_TERMINATED);

        /* Nadiren gerekse bile gönder alanını da doldur */
        field = curl_mime_addpart(form);
        curl_mime_name(field, "submit");
        curl_mime_data(field, "send", CURL_ZERO_TERMINATED);

        /* özel başlık listesini başlat (Expect: 100-continue istenmediğini belirterek */
        headerlist = curl_slist_append(headerlist, buf);

        /* bu POST'u hangi URL alır */
        curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/upload.cgi");
        curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);

        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headerlist);
        curl_easy_setopt(curl, CURLOPT_MIMEPOST, form);

        curl_multi_add_handle(multi_handle, curl);

        do {
          CURLMcode mc = curl_multi_perform(multi_handle, &still_running);

          if(still_running)
            /* aktivite, zaman aşımı veya "hiçbir şey" bekle */
            mc = curl_multi_poll(multi_handle, NULL, 0, 1000, NULL);

          if(mc)
            break;
        } while(still_running);

        curl_multi_cleanup(multi_handle);

        /* her zaman temizle */
        curl_easy_cleanup(curl);

        /* sonra formu temizle */
        curl_mime_free(form);

        /* slist'i serbest bırak */
        curl_slist_free_all(headerlist);
      }
      return 0;
    }
