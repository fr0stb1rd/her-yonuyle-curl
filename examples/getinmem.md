# Belleğe bir yanıt al (Get a response into memory)

Bu örnek, alınan verileri stdout'a (ki bu genellikle istediğiniz şey değildir) göndermek yerine, gelen veriler büyüdükçe genişletilen bir bellek tamponunda saklayan önceki örneğin bir varyasyonudur.

Bunu, verileri almak için bir [yazma geri çağırımı](../transfers/callbacks/write.md) kullanarak başarır.

Bu örnek, ayarlanmış bir URL şemasıyla sabit bir URL dizesi kullanır, ancak elbette bunu başka herhangi bir desteklenen protokolü kullanacak ve bunun yerine ondan bir kaynak alacak şekilde değiştirebilirsiniz.

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>

    #include <curl/curl.h>

    struct MemoryStruct {
      char *memory;
      size_t size;
    };

    static size_t
    mem_cb(void *contents, size_t size, size_t nmemb, void *userp)
    {
      size_t realsize = size * nmemb;
      struct MemoryStruct *mem = (struct MemoryStruct *)userp;

      mem->memory = realloc(mem->memory, mem->size + realsize + 1);
      if(mem->memory == NULL) {
        /* bellek yetersiz */
        printf("not enough memory (realloc returned NULL)\n");
        return 0;
      }

      memcpy(&(mem->memory[mem->size]), contents, realsize);
      mem->size += realsize;
      mem->memory[mem->size] = 0;

      return realsize;
    }

    int main(void)
    {
      CURL *curl_handle;
      CURLcode res;

      struct MemoryStruct chunk;

      chunk.memory = malloc(1);  /* yukarıdaki realloc tarafından gerektiği gibi büyütülür */
      chunk.size = 0;    /* bu noktada veri yok */

      curl_global_init(CURL_GLOBAL_ALL);

      /* curl oturumunu başlat */
      curl_handle = curl_easy_init();

      /* alınacak URL'yi belirt */
      curl_easy_setopt(curl_handle, CURLOPT_URL, "https://www.example.com/");

      /* tüm verileri bu işleve gönder  */
      curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, mem_cb);

      /* 'chunk' yapımızı geri çağırım işlevine iletiyoruz */
      curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void *)&chunk);

      /* bazı sunucular user-agent alanı olmadan yapılan istekleri sevmez,
         bu yüzden bir tane sağlıyoruz */
      curl_easy_setopt(curl_handle, CURLOPT_USERAGENT, "libcurl-agent/1.0");

      /* al onu! */
      res = curl_easy_perform(curl_handle);

      /* hataları kontrol et */
      if(res != CURLE_OK) {
        fprintf(stderr, "curl_easy_perform() failed: %s\n",
                curl_easy_strerror(res));
      }
      else {
        /*
         * Şimdi, chunk.memory'miz chunk.size bayt büyüklüğünde olan ve uzak dosyayı
         * içeren bir bellek bloğuna işaret ediyor.
         *
         * Onunla güzel bir şey yap
         */

        printf("%lu bytes retrieved\n", (long)chunk.size);
      }

      /* curl şeylerini temizle */
      curl_easy_cleanup(curl_handle);

      free(chunk.memory);

      /* libcurl ile işimiz bitti, temizleyin */
      curl_global_cleanup();

      return 0;
    }
