# Transfer sonrası bilgi

libcurl transferlerinin *easy handle'lar* ile nasıl ilişkili olduğunu hatırlayın. Her transferin böyle bir handle'ı vardır ve bir transfer tamamlandığında, handle temizlenmeden veya başka bir transfer için yeniden kullanılmadan önce, önceki işlemden bilgi çıkarmak için kullanılabilir.

Bunu yapmak için arkadaşınızın adı `curl_easy_getinfo()` ve ona hangi belirli bilgileri ilgilendiğinizi söylersiniz, o da yapabilirse o bilgiyi döndürür.

Bu işlevi kullandığınızda, easy handle'ı, hangi bilgiyi istediğinizi ve cevabı tutacak bir değişkene işaretçiyi iletirsiniz. Doğru türde bir değişkene işaretçi iletmelisiniz, yoksa işlerin ters gitme riskiyle karşı karşıya kalırsınız. Bu bilgi değerleri, transfer tamamlandıktan *sonra* sağlanmak üzere tasarlanmıştır.

Aldığınız veri bir long, bir 'char *', bir 'struct curl_slist *', bir double veya bir soket olabilir.

Önceki HTTP transferinden `Content-Type:` değerini şu şekilde çıkarırsınız:

    CURLcode res;
    char *content_type;
    res = curl_easy_getinfo(curl, CURLINFO_CONTENT_TYPE, &content_type);

O bağlantıda kullanılan yerel port numarasını çıkarmak isterseniz:

    CURLcode res;
    long port_number;
    res = curl_easy_getinfo(curl, CURLINFO_LOCAL_PORT, &port_number);

## Mevcut bilgiler

| Getinfo seçeneği                     | Tür               | Açıklama                                                                      |
|-------------------------------------------------|-------------------|---------------------------------------------|
| `CURLINFO_ACTIVESOCKET`              | `curl_socket_t`       | Oturumun aktif soketi                                                         |
| `CURLINFO_APPCONNECT_TIME`           | `double`              | Başlangıçtan SSL/SSH el sıkışması tamamlanana kadar geçen süre                |
| `CURLINFO_APPCONNECT_TIME_T`         | `curl_off_t`          | Başlangıçtan SSL/SSH el sıkışması tamamlanana kadar geçen süre (mikrosaniye)  |
| `CURLINFO_CAINFO`                    | `char *`              | libcurl'ün kullanmak üzere oluşturulduğu varsayılan CA dosyasının yolu        |
| `CURLINFO_CAPATH`                    | `char *`              | libcurl'ün kullanmak üzere oluşturulduğu CA dizininin yolu                    |
| `CURLINFO_CERTINFO`                  | `struct curl_slist *` | Sertifika zinciri                                                             |
| `CURLINFO_CONDITION_UNMET`           | `long`                | Bir zaman koşulunun karşılanıp karşılanmadığı                                 |
| `CURLINFO_CONNECT_TIME`              | `double`              | Başlangıçtan uzak ana bilgisayar veya proxy tamamlanana kadar geçen süre      |
| `CURLINFO_CONNECT_TIME_T`            | `curl_off_t`          | Başlangıçtan uzak ana bilgisayar veya proxy tamamlanana kadar geçen süre (mikrosaniye) |
| `CURLINFO_CONN_ID`                   | `curl_off_t`          | Mevcut bağlantının sayısal kimliği (geri çağırımlar için)                     |
| `CURLINFO_CONTENT_LENGTH_DOWNLOAD`   | `double`              | Content-Length başlığından içerik uzunluğu                                    |
| `CURLINFO_CONTENT_LENGTH_DOWNLOAD_T` | `curl_off_t`          | Content-Length başlığından içerik uzunluğu                                    |
| `CURLINFO_CONTENT_LENGTH_UPLOAD`     | `double`              | Yükleme boyutu                                                                |
| `CURLINFO_CONTENT_LENGTH_UPLOAD_T`   | `curl_off_t`          | Yükleme boyutu                                                                |
| `CURLINFO_CONTENT_TYPE`              | `char *`              | Content-Type başlığından içerik türü                                          |
| `CURLINFO_COOKIELIST`                | `struct curl_slist *` | Bilinen tüm çerezlerin listesi                                                |
| `CURLINFO_EFFECTIVE_METHOD`          | `char *`              | Son kullanılan HTTP istek yöntemi                                             |
| `CURLINFO_EFFECTIVE_URL`             | `char *`              | Son kullanılan URL                                                            |
| `CURLINFO_FILETIME`                  | `long`                | Alınan belgenin uzak zamanı                                                   |
| `CURLINFO_FILETIME_T`                | `curl_off_t`          | Alınan belgenin uzak zamanı                                                   |
| `CURLINFO_FTP_ENTRY_PATH`            | `char *`              | Bir FTP sunucusuna giriş yaptıktan sonraki giriş yolu                         |
| `CURLINFO_HEADER_SIZE`               | `long`                | Alınan tüm başlıkların bayt sayısı                                            |
| `CURLINFO_HTTP_CONNECTCODE`          | `long`                | Son proxy CONNECT yanıt kodu                                                  |
| `CURLINFO_HTTP_VERSION`              | `long`                | Bağlantıda kullanılan HTTP sürümü                                             |
| `CURLINFO_HTTPAUTH_AVAIL`            | `long`                | Mevcut HTTP kimlik doğrulama yöntemleri (bitmask)                             |
| `CURLINFO_LASTSOCKET`                | `long`                | Kullanılan son soket                                                          |
| `CURLINFO_LOCAL_IP`                  | `char *`              | Son bağlantının yerel uç IP adresi                                            |
| `CURLINFO_LOCAL_PORT`                | `long`                | Son bağlantının yerel uç portu                                                |
| `CURLINFO_NAMELOOKUP_TIME`           | `double`              | Başlangıçtan ad çözme tamamlanana kadar geçen süre                            |
| `CURLINFO_NAMELOOKUP_TIME_T`         | `curl_off_t`          | Başlangıçtan ad çözme tamamlanana kadar geçen süre (mikrosaniye)              |
| `CURLINFO_NUM_CONNECTS`              | `long`                | Önceki transfer için kullanılan yeni başarılı bağlantı sayısı                 |
| `CURLINFO_OS_ERRNO`                  | `long`                | Son bağlanma hatasından kaynaklanan errno                                     |
| `CURLINFO_PRETRANSFER_TIME`          | `double`              | Başlangıçtan transferin başlamasından hemen öncesine kadar geçen süre         |
| `CURLINFO_PRETRANSFER_TIME_T`        | `curl_off_t`          | Başlangıçtan transferin başlamasından hemen öncesine kadar geçen süre (mikrosaniye) |
| `CURLINFO_PRIMARY_IP`                | `char *`              | Son bağlantının IP adresi                                                     |
| `CURLINFO_PRIMARY_PORT`              | `long`                | Son bağlantının portu                                                         |
| `CURLINFO_PRIVATE`                   | `char *`              | Kullanıcının özel veri işaretçisi                                             |
| `CURLINFO_PROTOCOL`                  | `long`                | Bağlantı için kullanılan protokol                                             |
| `CURLINFO_PROXY_ERROR`               | `long`                | Transferden `CURLE_PROXY` döndürüldüyse ayrıntılı (SOCKS) proxy hatası        |
| `CURLINFO_PROXY_SSL_VERIFYRESULT`    | `long`                | Proxy sertifika doğrulama sonucu                                              |
| `CURLINFO_PROXYAUTH_AVAIL`           | `long`                | Mevcut HTTP proxy kimlik doğrulama yöntemleri                                 |
| `CURLINFO_QUEUE_TIME_T`              | `curl_off_t`          | Bu transferin başlamayı beklerken kuyrukta tutulduğu süre (mikrosaniye)       |
| `CURLINFO_REDIRECT_COUNT`            | `long`                | Takip edilen toplam yönlendirme sayısı                                        |
| `CURLINFO_REDIRECT_TIME`             | `double`              | Son transferden önceki tüm yönlendirme adımları için harcanan süre            |
| `CURLINFO_REDIRECT_TIME_T`           | `curl_off_t`          | Son transferden önceki tüm yönlendirme adımları için harcanan süre (mikrosaniye) |
| `CURLINFO_REDIRECT_URL`              | `char *`              | Yönlendirmeleri etkinleştirmiş olsaydınız bir yönlendirmenin sizi götüreceği URL |
| `CURLINFO_REFERER`                   | `char *`              | Kullanılan istek `Referer:` başlığı                                           |
| `CURLINFO_REQUEST_SIZE`              | `long`                | Gönderilen HTTP isteklerinde gönderilen bayt sayısı                           |
| `CURLINFO_RESPONSE_CODE`             | `long`                | Son alınan yanıt kodu                                                         |
| `CURLINFO_RETRY_AFTER`               | `curl_off_t`          | Yanıt `Retry-After:` başlığından gelen değer                                  |
| `CURLINFO_RTSP_CLIENT_CSEQ`          | `long`                | RTSP sonraki beklenen istemci CSeq                                            |
| `CURLINFO_RTSP_CSEQ_RECV`            | `long`                | RTSP son alınan                                                               |
| `CURLINFO_RTSP_SERVER_CSEQ`          | `long`                | RTSP sonraki beklenen sunucu CSeq                                             |
| `CURLINFO_RTSP_SESSION_ID`           | `char *`              | RTSP oturum kimliği                                                           |
| `CURLINFO_SCHEME`                    | `char *`              | Bağlantı için kullanılan şema                                                 |
| `CURLINFO_SIZE_DOWNLOAD`             | `double`              | İndirilen bayt sayısı                                                         |
| `CURLINFO_SIZE_DOWNLOAD_T`           | `curl_off_t`          | İndirilen bayt sayısı                                                         |
| `CURLINFO_SIZE_UPLOAD`               | `double`              | Yüklenen bayt sayısı                                                          |
| `CURLINFO_SIZE_UPLOAD_T`             | `curl_off_t`          | Yüklenen bayt sayısı                                                          |
| `CURLINFO_SPEED_DOWNLOAD`            | `double`              | Ortalama indirme hızı                                                         |
| `CURLINFO_SPEED_DOWNLOAD_T`          | `curl_off_t`          | Ortalama indirme hızı                                                         |
| `CURLINFO_SPEED_UPLOAD`              | `double`              | Ortalama yükleme hızı                                                         |
| `CURLINFO_SPEED_UPLOAD_T`            | `curl_off_t`          | Ortalama yükleme hızı                                                         |
| `CURLINFO_SSL_ENGINES`               | `struct curl_slist *` | OpenSSL kripto motorlarının bir listesi                                       |
| `CURLINFO_SSL_VERIFYRESULT`          | `long`                | Sertifika doğrulama sonucu                                                    |
| `CURLINFO_STARTTRANSFER_TIME`        | `double`              | Başlangıçtan ilk baytın alındığı ana kadar geçen süre                         |
| `CURLINFO_STARTTRANSFER_TIME_T`      | `curl_off_t`          | Başlangıçtan ilk baytın alındığı ana kadar geçen süre (mikrosaniye)           |
| `CURLINFO_TLS_SSL_PTR`               | `struct curl_slist *` | Daha fazla işlem için kullanılabilecek TLS oturum bilgisi                     |
| `CURLINFO_TOTAL_TIME`                | `double`              | Önceki transferin toplam süresi                                               |
| `CURLINFO_TOTAL_TIME_T`              | `curl_off_t`          | Önceki transferin toplam süresi (mikrosaniye)                                 |
| `CURLINFO_XFER_ID`                   | `curl_off_t`          | Mevcut transferin sayısal kimliği (geri çağırımlar için)                      |
