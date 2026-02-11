# --libcurl

Kullanıcıları, yapmak istedikleri transferi önce curl komut satırı aracıyla denemeye ve kabaca istedikleri gibi çalıştıktan sonra komut satırına `--libcurl [dosyaadı]` seçeneğini ekleyip tekrar çalıştırmaya aktif olarak teşvik ediyoruz.

`--libcurl` komut satırı seçeneği, sağlanan dosya adında bir C programı oluşturur. Bu C programı, curl komut satırı aracına az önce yaptırdığınız transferi çalıştırmak için libcurl kullanan bir uygulamadır. Bazı istisnalar vardır ve her zaman %100 eşleşme olmaz, ancak hangi libcurl seçeneklerini istediğinizi veya kullanabileceğinizi ve bunlara hangi ek argümanları sağlayacağınızı görmek için mükemmel bir ilham kaynağı olarak hizmet edebileceğini görebilirsiniz.

Dosya adını tek bir tire olarak belirtirseniz (`--libcurl -` şeklinde), programın bir dosya yerine stdout'a yazılmasını sağlarsınız.

Örnek olarak, `http://example.com` adresini almak için bir komut çalıştırıyoruz:

    curl http://example.com --libcurl example.c

Bu, mevcut dizinde şuna benzer görünen `example.c` dosyasını oluşturur:

    /****** curl komut satırı aracı tarafından oluşturulan örnek kod ******/
     * Tüm curl_easy_setopt() seçenekleri şurada belgelenmiştir:
     * https://curl.se/libcurl/c/curl_easy_setopt.html
     ************************************************************************/
    #include <curl/curl.h>

    int main(int argc, char *argv[])
    {
      CURLcode ret;
      CURL *hnd;

      hnd = curl_easy_init();
      curl_easy_setopt(hnd, CURLOPT_URL, "http://example.com");
      curl_easy_setopt(hnd, CURLOPT_NOPROGRESS, 1L);
      curl_easy_setopt(hnd, CURLOPT_USERAGENT, "curl/7.45.0");
      curl_easy_setopt(hnd, CURLOPT_MAXREDIRS, 50L);
      curl_easy_setopt(hnd, CURLOPT_SSH_KNOWNHOSTS,
                       "/home/daniel/.ssh/known_hosts");
      curl_easy_setopt(hnd, CURLOPT_TCP_KEEPALIVE, 1L);

      /* İşte curl kodunun kullandığı ancak kaynak olarak
         kolayca oluşturulamayan seçeneklerin bir listesi.
         Bunları kullanmamayı veya kendiniz uygulamayı seçebilirsiniz.

      CURLOPT_WRITEDATA set to a objectpointer
      CURLOPT_WRITEFUNCTION set to a functionpointer
      CURLOPT_READDATA set to a objectpointer
      CURLOPT_READFUNCTION set to a functionpointer
      CURLOPT_SEEKDATA set to a objectpointer
      CURLOPT_SEEKFUNCTION set to a functionpointer
      CURLOPT_ERRORBUFFER set to a objectpointer
      CURLOPT_STDERR set to a objectpointer
      CURLOPT_HEADERFUNCTION set to a functionpointer
      CURLOPT_HEADERDATA set to a objectpointer

      */

      ret = curl_easy_perform(hnd);

      curl_easy_cleanup(hnd);
      hnd = NULL;

      return (int)ret;
    }
    /**** Örnek kodun sonu ****/
