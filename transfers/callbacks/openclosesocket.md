# Soket açma ve kapama (Opensocket and closesocket)

Bazen uygulamanızın libcurl'ün operasyonları için tam olarak hangi soketi kullanacağını daha hassas bir şekilde kontrol etmesini istediğiniz bir duruma düşersiniz. libcurl, libcurl'ün kendi `socket()` çağrısının ve ardından aynı dosya tanımlayıcısının `close()` çağrısının yerini alan bu geri çağırım çiftini sunar.

## Bir dosya tanımlayıcısı (file descriptor) sağla

`CURLOPT_OPENSOCKETFUNCTION` geri çağırımını ayarlayarak, libcurl'ün kullanması için bir dosya tanımlayıcısı döndürmek üzere özel bir işlev sağlayabilirsiniz:

    curl_easy_setopt(handle, CURLOPT_OPENSOCKETFUNCTION, opensocket_callback);

`opensocket_callback` işlevi şu prototiple eşleşmelidir:

    curl_socket_t opensocket_callback(void *clientp,
                                      curlsocktype purpose,
                                      struct curl_sockaddr *address);

Geri çağırım ilk argüman olarak *clientp*'yi alır; bu, `CURLOPT_OPENSOCKETDATA` ile ayarladığınız opak bir işaretçidir.

Diğer iki argüman, soketin hangi *amaç (purpose)* ve *adres* için kullanılacağını tanımlayan verileri iletir. *purpose*, soketin hangi koşulda oluşturulduğunu tanımlayan `CURLSOCKTYPE_IPCXN` veya `CURLSOCKTYPE_ACCEPT` değerine sahip bir typedef'tir. "accept" durumu, FTP aktif modu kullanıldığında libcurl'ün gelen bir FTP bağlantısını kabul etmek için kullanıldığı durumdur ve diğer tüm durumlarda libcurl kendi giden bağlantıları için bir soket oluşturduğunda *IPCXN* değeri iletilir.

*address* işaretçisi, bu soketin oluşturulduğu ağ hedefinin IP adresini tanımlayan bir `struct curl_sockaddr`'a işaret eder. Geri çağırımınız örneğin bu bilgiyi belirli adresleri veya adres aralıklarını beyaz listeye veya kara listeye almak için kullanabilir.

Soket açma geri çağırımının, bir tür ağ filtresi veya çeviri katmanı sunmak istiyorsanız, o yapıdaki hedef adresi değiştirmesine de açıkça izin verilir.

Geri çağırım bir dosya tanımlayıcısı veya `CURL_SOCKET_BAD` döndürmelidir; bu daha sonra libcurl içinde kurtarılamaz bir hataya neden olur ve perform işlevinden `CURLE_COULDNT_CONNECT` döndürür.

Bir sunucuya *zaten bağlı* bir dosya tanımlayıcısı döndürmek istiyorsanız, o zaman [sockopt geri çağırımını](sockopt.md) da ayarlamalı ve doğru dönüş değerini döndürdüğünden emin olmalısınız.

`curl_sockaddress` yapısı şöyle görünür:

    struct curl_sockaddr {
      int family;
      int socktype;
      int protocol;
      unsigned int addrlen;
      struct sockaddr addr;
    };

## Soket kapatma geri çağırımı

Açık sokete karşılık gelen geri çağırım elbette soketi kapatmaktır. Genellikle bir dosya tanımlayıcısı sağlamak için özel bir yol sağladığınızda, kendi temizleme sürümünüzü de sağlamak istersiniz:

    curl_easy_setopt(handle, CURLOPT_CLOSESOCKETFUNCTION,
                     closesocket_callback);

`closesocket_callback` işlevi şu prototiple eşleşmelidir:

    int closesocket_callback(void *clientp, curl_socket_t item);
