# sockopt

sockopt geri çağırımı `CURLOPT_SOCKOPTFUNCTION` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_SOCKOPTFUNCTION, sockopt_callback);

`sockopt_callback` işlevi şu prototiple eşleşmelidir:

    int sockopt_callback(void *clientp,
                         curl_socket_t curlfd,
                         curlsocktype purpose);

Bu geri çağırım işlevi, yeni bir soket oluşturulduğunda ancak bağlan çağrısından önce, uygulamaların belirli soket seçeneklerini değiştirmesine izin vermek için libcurl tarafından çağrılır.

**clientp** işaretçisi, `CURLOPT_SOCKOPTDATA` ile ayarlanan özel verilere işaret eder:

    curl_easy_setopt(handle, CURLOPT_SOCKOPTDATA, custom_pointer);

Bu geri çağırım şunları döndürmelidir:

 - Başarılı durumda CURL_SOCKOPT_OK
 - libcurl'e kurtarılamaz bir hata bildirmek için CURL_SOCKOPT_ERROR
 - Başarıyı ancak aynı zamanda soketin aslında zaten hedefe bağlı olduğunu bildirmek için CURL_SOCKOPT_ALREADY_CONNECTED
