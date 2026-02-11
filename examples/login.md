# HTTP üzerinden bir giriş formu gönder (Submit a login form over HTTP)

HTTP üzerinden bir giriş gönderimi, genellikle bir POST içinde tam olarak hangi verilerin gönderileceğini ve hangi hedef URL'ye gönderileceğini bulma meselesidir.

Giriş yapıldıktan sonra, uygun çerezler kullanılırsa hedef URL getirilebilir. Birçok giriş sistemi HTTP yönlendirmeleriyle çalıştığından, libcurl'den gelirse bunları takip etmesini isteriz.

Bazı giriş formları bunu daha karmaşık hale getirir ve giriş formunu gösteren sayfadan vb. çerezler almanızı gerektirir, bu nedenle buna ihtiyacınız varsa bu kodu biraz genişletmek isteyebilirsiniz.

Var olmayan bir çerez dosyası ileterek, bu örnek çerez ayrıştırıcısını etkinleştirir, böylece giriş yanıtından gelen yanıt geldiğinde gelen çerezler saklanır ve ardından kaynak için sonraki istek bunları kullanır ve sunucuya aslında doğru bir şekilde giriş yaptığımızı kanıtlar.

    #include <stdio.h>
    #include <string.h>
    #include <curl/curl.h>

    int main(void)
    {
      CURL *curl;
      CURLcode res;

      static const char *postthis = "user=daniel&password=monkey123";

      curl = curl_easy_init();
      if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/login.cgi");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, postthis);
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L); /* yönlendirme */
        curl_easy_setopt(curl, CURLOPT_COOKIEFILE, ""); /* dosya yok */
        res = curl_easy_perform(curl);
        /* Hataları kontrol et */
        if(res != CURLE_OK)
          fprintf(stderr, "curl_easy_perform() failed: %s\n",
                  curl_easy_strerror(res));
        else {
          /*
           * Giriş POST'undan sonra yeni çerezleri aldık. Bir GET'e geçin
           * ve giriş korumalı URL'yi isteyin.
           */
          curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/file");
          curl_easy_setopt(curl, CURLOPT_HTTPGET, 1L); /* daha fazla
                                                          POST yok */
          res = curl_easy_perform(curl);
          /* Hataları kontrol et */
          if(res != CURLE_OK)
            fprintf(stderr, "second curl_easy_perform() failed: %s\n",
                    curl_easy_strerror(res));
        }
        /* her zaman temizle */
        curl_easy_cleanup(curl);
      }
      return 0;
    }
