# Başlık verileri (Header data)

Başlık geri çağırımı `CURLOPT_HEADERFUNCTION` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_HEADERFUNCTION, header_callback);

`header_callback` işlevi şu prototiple eşleşmelidir:

    size_t header_callback(char *ptr, size_t size, size_t nmemb,
                           void *userdata);

Bu geri çağırım işlevi, bir başlık alınır alınmaz libcurl tarafından çağrılır. *ptr*, teslim edilen verileri işaret eder ve bu verilerin boyutu *nmemb* ile çarpılan *size*'dır. libcurl başlıkları tamponlar ve bu geri çağırıma yalnızca "tam" başlıkları teker teker teslim eder.

Bu işleve iletilen veriler sıfır ile sonlandırılmaz. Örneğin, içeriği görüntülemek için printf'in `%s` operatörünü kullanamazsınız veya kopyalamak için strcpy kullanamazsınız.

Bu geri çağırım, gerçekten ilgilenilen bayt sayısını döndürmelidir. Bu sayı, geri çağırım işlevinize iletilen sayıdan farklıysa, kütüphaneye bir hata durumu bildirir. Bu, transferin iptal edilmesine neden olur ve kullanılan libcurl işlevi `CURLE_WRITE_ERROR` döndürür.

*userdata* argümanında geri çağırıma iletilen kullanıcı işaretçisi `CURLOPT_HEADERDATA` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_HEADERDATA, custom_pointer);
