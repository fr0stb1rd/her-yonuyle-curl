# Veri yazma (Write data)

Yazma geri çağırımı `CURLOPT_WRITEFUNCTION` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_WRITEFUNCTION, write_callback);

`write_callback` işlevi şu prototiple eşleşmelidir:

    size_t write_callback(char *ptr, size_t size, size_t nmemb,
                          void *userdata);

Bu geri çağırım işlevi, kaydedilmesi gereken veriler alındığında libcurl tarafından çağrılır. *ptr*, teslim edilen verileri işaret eder ve bu verilerin boyutu *nmemb* ile çarpılan *size*'dır.

Bu geri çağırım ayarlanmazsa, libcurl varsayılan olarak 'fwrite' kullanır.

Yazma geri çağırımına tüm çağrılarda mümkün olduğunca fazla veri iletilir ancak hiçbir varsayımda bulunulmamalıdır. Bir bayt olabilir, binlerce olabilir. Yazma geri çağırımına iletilen maksimum gövde verisi miktarı curl.h başlık dosyasında tanımlanmıştır: `CURL_MAX_WRITE_SIZE` (olağan varsayılan 16KB'dir). Bu transfer için `CURLOPT_HEADER` etkinleştirilirse, bu da başlık verilerinin yazma geri çağırımına iletilmesini sağlar, içine iletilen `CURL_MAX_HTTP_HEADER` baytına kadar başlık verisi alabilirsiniz. Bu genellikle 100KB anlamına gelir.

Aktarılan dosya boşsa bu işlev sıfır bayt veri ile çağrılabilir.

Bu işleve iletilen veriler sıfır ile sonlandırılmaz. Örneğin, içeriği görüntülemek için printf'in `%s` operatörünü kullanamazsınız veya kopyalamak için strcpy kullanamazsınız.

Bu geri çağırım, gerçekten ilgilenilen bayt sayısını döndürmelidir. Bu sayı, geri çağırım işlevinize iletilen sayıdan farklıysa, kütüphaneye bir hata durumu bildirir. Bu, transferin iptal edilmesine neden olur ve kullanılan libcurl işlevi `CURLE_WRITE_ERROR` döndürür.

*userdata* argümanında geri çağırıma iletilen kullanıcı işaretçisi `CURLOPT_WRITEDATA` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_WRITEDATA, custom_pointer);

## Bellekte sakla

Popüler bir talep, alınan yanıtı bellekte saklamaktır ve yukarıda açıklanan geri çağırım bunu destekler. Bunu yaparken, yanıt potansiyel olarak muazzam olabileceğinden dikkatli olun.

Geri çağırımı şuna benzer bir şekilde uygularsınız:

    struct response {
      char *memory;
      size_t size;
    };

    static size_t
    mem_cb(void *contents, size_t size, size_t nmemb, void *userp)
    {
      size_t realsize = size * nmemb;
      struct response *mem = (struct response *)userp;

      char *ptr = realloc(mem->memory, mem->size + realsize + 1);
      if(!ptr) {
        /* bellek tükendi! */
        printf("yeterli bellek yok (realloc NULL döndürdü)\n");
        return 0;
      }

      mem->memory = ptr;
      memcpy(&(mem->memory[mem->size]), contents, realsize);
      mem->size += realsize;
      mem->memory[mem->size] = 0;

      return realsize;
    }

    int main()
    {
      struct response chunk = {.memory = malloc(0),
                               .size = 0};

      /* tüm verileri bu işleve gönder */
      curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, mem_cb);

      /* 'chunk' yapımızı geri çağırım işlevine iletiyoruz */
      curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void *)&chunk);

      free(chunk.memory);
    }
