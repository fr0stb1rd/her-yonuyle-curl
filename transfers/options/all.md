# Tüm seçenekler

Bu, `curl_easy_setopt()` için mevcut seçeneklerin bir tablosudur.

| Seçenek                              | Amaç                                                                   |
|--------------------------------------|------------------------------------------------------------------------|
| `CURLOPT_ABSTRACT_UNIX_SOCKET`       | soyut Unix etki alanı soketi                                           |
| `CURLOPT_ACCEPT_ENCODING`            | HTTP indirmelerinin otomatik açılması                                  |
| `CURLOPT_ACCEPTTIMEOUT_MS`           | FTP sunucusunun geri bağlanmasını beklerken zaman aşımı                |
| `CURLOPT_ADDRESS_SCOPE`              | IPv6 adresleri için kapsam kimliği                                     |
| `CURLOPT_ALTSVC_CTRL`                | alt-svc davranışını kontrol et                                         |
| `CURLOPT_ALTSVC`                     | alt-svc önbellek dosya adı                                             |
| `CURLOPT_APPEND`                     | uzak dosyaya ekle                                                      |
| `CURLOPT_AUTOREFERER`                | referer başlığını otomatik olarak güncelle                             |
| `CURLOPT_AWS_SIGV4`                  | V4 imzası                                                              |
| `CURLOPT_BUFFERSIZE`                 | alma tampon boyutu                                                     |
| `CURLOPT_CA_CACHE_TIMEOUT`           | önbelleğe alınan sertifika depoları için kullanım ömrü                 |
| `CURLOPT_CAINFO_BLOB`                | PEM formatında Sertifika Otoritesi (CA) demeti                         |
| `CURLOPT_CAINFO`                     | Sertifika Otoritesi (CA) demetine giden yol                            |
| `CURLOPT_CAPATH`                     | CA sertifikalarını tutan dizin                                         |
| `CURLOPT_CERTINFO`                   | SSL sertifika bilgisini iste                                           |
| `CURLOPT_CHUNK_BGN_FUNCTION`         | FTP joker eşleşmeli bir transferden önce geri çağırım                  |
| `CURLOPT_CHUNK_DATA`                 | FTP yığın geri çağırımlarına iletilen işaretçi                         |
| `CURLOPT_CHUNK_END_FUNCTION`         | FTP joker eşleşmeli bir transferden sonra geri çağırım                 |
| `CURLOPT_CLOSESOCKETDATA`            | soket kapatma geri çağırımına iletilen işaretçi                        |
| `CURLOPT_CLOSESOCKETFUNCTION`        | soket kapatma değişimi için geri çağırım                               |
| `CURLOPT_CONNECT_ONLY`               | hedef sunucuya bağlanıldığında dur                                     |
| `CURLOPT_CONNECT_TO`                 | URL'nin ana bilgisayarı ve portu yerine belirli bir ana bilgisayara ve porta bağlan |
| `CURLOPT_CONNECTTIMEOUT_MS`          | bağlanma aşaması için zaman aşımı                                      |
| `CURLOPT_CONNECTTIMEOUT`             | bağlanma aşaması için zaman aşımı                                      |
| `CURLOPT_CONV_FROM_NETWORK_FUNCTION` | verileri ağdan ana bilgisayar kodlamasına dönüştür                     |
| `CURLOPT_CONV_FROM_UTF8_FUNCTION`    | verileri UTF8'den ana bilgisayar kodlamasına dönüştür                  |
| `CURLOPT_CONV_TO_NETWORK_FUNCTION`   | verileri ana bilgisayar kodlamasından ağa dönüştür                     |
| `CURLOPT_COOKIE`                     | HTTP Çerez başlığı                                                     |
| `CURLOPT_COOKIEFILE`                 | çerezlerin okunacağı dosya adı                                         |
| `CURLOPT_COOKIEJAR`                  | çerezlerin saklanacağı dosya adı                                       |
| `CURLOPT_COOKIELIST`                 | bellekte tutulan çerezleri ekle veya değiştir                          |
| `CURLOPT_COOKIESESSION`              | yeni bir çerez oturumu başlat                                          |
| `CURLOPT_COPYPOSTFIELDS`             | libcurl'ün verileri POST'a kopyalamasını sağla                         |
| `CURLOPT_CRLF`                       | CRLF dönüşümü                                                          |
| `CURLOPT_CRLFILE`                    | Sertifika İptal Listesi dosyası                                        |
| `CURLOPT_CURLU`                      | CURLU * formatında URL                                                 |
| `CURLOPT_CUSTOMREQUEST`              | özel istek yöntemi                                                     |
| `CURLOPT_DEBUGDATA`                  | hata ayıklama geri çağırımına iletilen işaretçi                        |
| `CURLOPT_DEBUGFUNCTION`              | hata ayıklama geri çağırımı                                            |
| `CURLOPT_DEFAULT_PROTOCOL`           | URL eksikse kullanılacak varsayılan protokol                           |
| `CURLOPT_DIRLISTONLY`                | bir dizin listesinde sadece adları iste                                |
| `CURLOPT_DISALLOW_USERNAME_IN_URL`   | URL'de kullanıcı adı belirtilmesine izin verme                         |
| `CURLOPT_DNS_CACHE_TIMEOUT`          | DNS önbellek girişleri için kullanım ömrü                              |
| `CURLOPT_DNS_INTERFACE`              | DNS üzerinden konuşulacak arayüz                                       |
| `CURLOPT_DNS_LOCAL_IP4`              | DNS çözümlemelerinin bağlanacağı IPv4 adresi                           |
| `CURLOPT_DNS_LOCAL_IP6`              | DNS çözümlemelerinin bağlanacağı IPv6 adresi                           |
| `CURLOPT_DNS_SERVERS`                | kullanılacak DNS sunucuları                                            |
| `CURLOPT_DNS_SHUFFLE_ADDRESSES`      | ana bilgisayar adı için IP adreslerini karıştır                        |
| `CURLOPT_DNS_USE_GLOBAL_CACHE`       | küresel DNS önbelleği                                                  |
| `CURLOPT_DOH_SSL_VERIFYHOST`         | DoH SSL sertifikasındaki ana bilgisayar adını doğrula                  |
| `CURLOPT_DOH_SSL_VERIFYPEER`         | DoH SSL sertifikasını doğrula                                          |
| `CURLOPT_DOH_SSL_VERIFYSTATUS`       | DoH SSL sertifikasının durumunu doğrula                                |
| `CURLOPT_DOH_URL`                    | DNS-over-HTTPS URL'sini sağla                                          |
| `CURLOPT_EGDSOCKET`                  | EGD soket yolu                                                         |
| `CURLOPT_ERRORBUFFER`                | hata mesajları için hata arabelleği                                    |
| `CURLOPT_EXPECT_100_TIMEOUT_MS`      | Expect: 100-continue yanıtı için zaman aşımı                           |
| `CURLOPT_FAILONERROR`                | HTTP yanıtı >= 400 olduğunda istek başarısız olsun                     |
| `CURLOPT_FILETIME`                   | uzak kaynağın değişiklik zamanını al                                   |
| `CURLOPT_FNMATCH_DATA`               | fnmatch geri çağırımına iletilen işaretçi                              |
| `CURLOPT_FNMATCH_FUNCTION`           | joker eşleşme geri çağırımı                                            |
| `CURLOPT_FOLLOWLOCATION`             | HTTP 3xx yönlendirmelerini takip et                                    |
| `CURLOPT_FORBID_REUSE`               | kullanımdan hemen sonra bağlantının kapatılmasını sağla                |
| `CURLOPT_FRESH_CONNECT`              | yeni bir bağlantı kullanılmasını zorla                                 |
| `CURLOPT_FTP_ACCOUNT`                | FTP için hesap bilgisi                                                 |
| `CURLOPT_FTP_ALTERNATIVE_TO_USER`    | FTP ile USER yerine kullanılacak komut                                 |
| `CURLOPT_FTP_CREATE_MISSING_DIRS`    | FTP ve SFTP için eksik dizinleri oluştur                               |
| `CURLOPT_FTP_FILEMETHOD`             | FTP için dizin dolaşma yöntemini seç                                   |
| `CURLOPT_FTP_RESPONSE_TIMEOUT`       | FTP yanıtı için beklemeye izin verilen süre                            |
| `CURLOPT_FTP_SKIP_PASV_IP`           | PASV yanıtındaki IP adresini yoksay                                    |
| `CURLOPT_FTP_SSL_CCC`                | FTP ile kimlik doğrulamasından sonra SSL'i tekrar kapat                |
| `CURLOPT_FTP_USE_EPRT`               | FTP için EPRT kullan                                                   |
| `CURLOPT_FTP_USE_EPSV`               | FTP için EPSV kullan                                                   |
| `CURLOPT_FTP_USE_PRET`               | FTP için PRET kullan                                                   |
| `CURLOPT_FTPPORT`                    | FTP transferini aktif hale getir                                       |
| `CURLOPT_FTPSSLAUTH`                 | TLS ve SSL deneme sırası                                               |
| `CURLOPT_GSSAPI_DELEGATION`          | izin verilen GSS-API yetkilendirmesi                                   |
| `CURLOPT_HAPPY_EYEBALLS_TIMEOUT_MS`  | happy eyeballs için ipv6 başlama avantajı                              |
| `CURLOPT_HAPROXY_CLIENT_IP`          | HAProxy PROXY protokolü istemci IP'sini ayarla                         |
| `CURLOPT_HAPROXYPROTOCOL`            | HAProxy PROXY protokolü v1 başlığını gönder                            |
| `CURLOPT_HEADER`                     | başlıkları veri akışına geçir                                          |
| `CURLOPT_HEADERDATA`                 | başlık geri çağırımına iletilecek işaretçi                             |
| `CURLOPT_HEADERFUNCTION`             | başlık verilerini alan geri çağırım                                    |
| `CURLOPT_HEADEROPT`                  | HTTP başlıklarını hem proxy'ye hem de ana bilgisayara veya ayrı ayrı gönder |
| `CURLOPT_HSTS_CTRL`                  | HSTS davranışını kontrol et                                            |
| `CURLOPT_HSTS`                       | HSTS önbellek dosya adı                                                |
| `CURLOPT_HSTSREADDATA`               | HSTS okuma geri çağırımına iletilen işaretçi                           |
| `CURLOPT_HSTSREADFUNCTION`           | HSTS ana bilgisayarları için okuma geri çağırımı                       |
| `CURLOPT_HSTSWRITEDATA`              | HSTS yazma geri çağırımına iletilen işaretçi                           |
| `CURLOPT_HSTSWRITEFUNCTION`          | HSTS ana bilgisayarları için yazma geri çağırımı                       |
| `CURLOPT_HTTP09_ALLOWED`             | HTTP/0.9 yanıtına izin ver                                             |
| `CURLOPT_HTTP200ALIASES`             | HTTP 200 OK için alternatif eşleşmeler                                 |
| `CURLOPT_HTTP_CONTENT_DECODING`      | HTTP içerik çözme kontrolü                                             |
| `CURLOPT_HTTP_TRANSFER_DECODING`     | HTTP transfer çözme kontrolü                                           |
| `CURLOPT_HTTP_VERSION`               | kullanılacak HTTP protokol sürümü                                      |
| `CURLOPT_HTTPAUTH`                   | denecek HTTP sunucusu kimlik doğrulama yöntemleri                      |
| `CURLOPT_HTTPGET`                    | bir HTTP GET isteği iste                                               |
| `CURLOPT_HTTPHEADER`                 | HTTP başlıkları seti                                                   |
| `CURLOPT_HTTPPOST`                   | çok parçalı (multipart) formpost içeriği                               |
| `CURLOPT_HTTPPROXYTUNNEL`            | HTTP proxy üzerinden tünel aç                                          |
| `CURLOPT_IGNORE_CONTENT_LENGTH`      | içerik uzunluğunu (content length) yoksay                              |
| `CURLOPT_INFILESIZE_LARGE`           | gönderilecek girdi dosyasının boyutu                                   |
| `CURLOPT_INFILESIZE`                 | gönderilecek girdi dosyasının boyutu                                   |
| `CURLOPT_INTERFACE`                  | giden trafik için kaynak arayüz                                        |
| `CURLOPT_INTERLEAVEDATA`             | RTSP interleave geri çağırımına iletilen işaretçi                      |
| `CURLOPT_INTERLEAVEFUNCTION`         | RTSP interleaved verileri için geri çağırım                            |
| `CURLOPT_IOCTLDATA`                  | G/Ç (I/O) geri çağırımına iletilen işaretçi                            |
| `CURLOPT_IOCTLFUNCTION`              | G/Ç işlemleri için geri çağırım                                        |
| `CURLOPT_IPRESOLVE`                  | kullanılacak IP protokol sürümü                                        |
| `CURLOPT_ISSUERCERT_BLOB`            | bellek bloğundan veren (issuer) SSL sertifikası                        |
| `CURLOPT_ISSUERCERT`                 | veren (issuer) SSL sertifikası dosya adı                               |
| `CURLOPT_KEEP_SENDING_ON_ERROR`      | erken HTTP yanıtı >= 300'de göndermeye devam et                        |
| `CURLOPT_KEYPASSWD`                  | özel anahtar için parola                                               |
| `CURLOPT_KRBLEVEL`                   | FTP kerberos güvenlik seviyesi                                         |
| `CURLOPT_LOCALPORT`                  | soket için kullanılacak yerel port numarası                            |
| `CURLOPT_LOCALPORTRANGE`             | denenecek ek yerel port sayısı                                         |
| `CURLOPT_LOGIN_OPTIONS`              | giriş seçenekleri                                                      |
| `CURLOPT_LOW_SPEED_LIMIT`            | saniye başına bayt cinsinden düşük hız sınırı                          |
| `CURLOPT_LOW_SPEED_TIME`             | düşük hız sınırı zaman aralığı                                         |
| `CURLOPT_MAIL_AUTH`                  | SMTP kimlik doğrulama adresi                                           |
| `CURLOPT_MAIL_FROM`                  | SMTP gönderen adresi                                                   |
| `CURLOPT_MAIL_RCPT_ALLOWFAILS`       | RCPT TO komutunun bazı alıcılar için başarısız olmasına izin ver       |
| `CURLOPT_MAIL_RCPT`                  | SMTP posta alıcıları listesi                                           |
| `CURLOPT_MAX_RECV_SPEED_LARGE`       | veri indirme hızını sınırla                                            |
| `CURLOPT_MAX_SEND_SPEED_LARGE`       | veri yükleme hızını sınırla                                            |
| `CURLOPT_MAXAGE_CONN`                | bir bağlantıyı yeniden kullanmak için izin verilen maksimum boşta kalma süresi |
| `CURLOPT_MAXCONNECTS`                | maksimum bağlantı önbellek boyutu                                      |
| `CURLOPT_MAXFILESIZE_LARGE`          | indirmeye izin verilen maksimum dosya boyutu                           |
| `CURLOPT_MAXFILESIZE`                | indirmeye izin verilen maksimum dosya boyutu                           |
| `CURLOPT_MAXLIFETIME_CONN`           | bir bağlantıyı yeniden kullanmak için izin verilen maksimum ömür (oluşturulduğundan beri) |
| `CURLOPT_MAXREDIRS`                  | izin verilen maksimum yönlendirme sayısı                               |
| `CURLOPT_MIME_OPTIONS`               | MIME seçenek bayraklarını ayarla                                       |
| `CURLOPT_MIMEPOST`                   | mime yapısından veri gönder                                            |
| `CURLOPT_NETRC_FILE`                 | .netrc bilgisinin okunacağı dosya adı                                  |
| `CURLOPT_NETRC`                      | .netrc kullanımını etkinleştir                                         |
| `CURLOPT_NEW_DIRECTORY_PERMS`        | uzaktan oluşturulan dizinler için izinler                              |
| `CURLOPT_NEW_FILE_PERMS`             | uzaktan oluşturulan dosyalar için izinler                              |
| `CURLOPT_NOBODY`                     | indirme isteğini gövdeyi almadan yap                                   |
| `CURLOPT_NOPROGRESS`                 | ilerleme ölçeri kapat                                                  |
| `CURLOPT_NOPROXY`                    | belirli ana bilgisayarlar için proxy kullanımını devre dışı bırak      |
| `CURLOPT_NOSIGNAL`                   | tüm sinyal işlemeyi atla                                               |
| `CURLOPT_OPENSOCKETDATA`             | açık soket geri çağırımına iletilen işaretçi                           |
| `CURLOPT_OPENSOCKETFUNCTION`         | soket açma için geri çağırım                                           |
| `CURLOPT_PASSWORD`                   | kimlik doğrulamasında kullanılacak şifre                               |
| `CURLOPT_PATH_AS_IS`                 | nokta nokta dizilerini işleme                                          |
| `CURLOPT_PINNEDPUBLICKEY`            | sabitlenmiş genel anahtar                                              |
| `CURLOPT_PIPEWAIT`                   | pipelining/multiplexing için bekle                                     |
| `CURLOPT_PORT`                       | bağlanılacak uzak port numarası                                        |
| `CURLOPT_POST`                       | bir HTTP POST yap                                                      |
| `CURLOPT_POSTFIELDS`                 | sunucuya POST edilecek veriler                                         |
| `CURLOPT_POSTFIELDSIZE_LARGE`        | işaret edilen POST verilerinin boyutu                                  |
| `CURLOPT_POSTFIELDSIZE`              | işaret edilen POST verilerinin boyutu                                  |
| `CURLOPT_POSTQUOTE`                  | transferden sonra çalıştırılacak (S)FTP komutları                      |
| `CURLOPT_POSTREDIR`                  | bir HTTP POST yönlendirmesinde nasıl davranılacağı                     |
| `CURLOPT_PRE_PROXY`                  | kullanılacak ön proxy ana bilgisayarı                                  |
| `CURLOPT_PREQUOTE`                   | bir FTP transferinden önce çalıştırılacak komutlar                     |
| `CURLOPT_PREREQDATA`                 | ön istek geri çağırımına iletilen işaretçi                             |
| `CURLOPT_PREREQFUNCTION`             | bir bağlantı olduğunda çağrılan kullanıcı geri çağırımı                |
| `CURLOPT_PRIVATE`                    | özel bir işaretçi sakla                                                |
| `CURLOPT_PROGRESSDATA`               | ilerleme geri çağırımına iletilen işaretçi                             |
| `CURLOPT_PROGRESSFUNCTION`           | ilerleme ölçer geri çağırımı                                           |
| `CURLOPT_PROTOCOLS_STR`              | izin verilen protokoller                                               |
| `CURLOPT_PROTOCOLS`                  | izin verilen protokoller                                               |
| `CURLOPT_PROXY_CAINFO_BLOB`          | PEM formatında proxy Sertifika Otoritesi (CA) demeti                   |
| `CURLOPT_PROXY_CAINFO`               | proxy Sertifika Otoritesi (CA) demetine giden yol                      |
| `CURLOPT_PROXY_CAPATH`               | HTTPS proxy CA sertifikalarını tutan dizin                             |
| `CURLOPT_PROXY_CRLFILE`              | HTTPS proxy Sertifika İptal Listesi dosyası                            |
| `CURLOPT_PROXY_ISSUERCERT_BLOB`      | bellek bloğundan proxy veren (issuer) SSL sertifikası                  |
| `CURLOPT_PROXY_ISSUERCERT`           | proxy veren (issuer) SSL sertifikası dosya adı                         |
| `CURLOPT_PROXY_KEYPASSWD`            | proxy özel anahtarı için parola                                        |
| `CURLOPT_PROXY_PINNEDPUBLICKEY`      | https proxy için sabitlenmiş genel anahtar                             |
| `CURLOPT_PROXY_SERVICE_NAME`         | proxy kimlik doğrulama hizmet adı                                      |
| `CURLOPT_PROXY_SSL_CIPHER_LIST`      | HTTPS proxy için kullanılacak şifreler                                 |
| `CURLOPT_PROXY_SSL_OPTIONS`          | HTTPS proxy SSL davranış seçenekleri                                   |
| `CURLOPT_PROXY_SSL_VERIFYHOST`       | proxy sertifikasının adını ana bilgisayara karşı doğrula               |
| `CURLOPT_PROXY_SSL_VERIFYPEER`       | proxy'nin SSL sertifikasını doğrula                                    |
| `CURLOPT_PROXY_SSLCERT_BLOB`         | bellek bloğundan SSL proxy istemci sertifikası                         |
| `CURLOPT_PROXY_SSLCERT`              | HTTPS proxy istemci sertifikası                                        |
| `CURLOPT_PROXY_SSLCERTTYPE`          | proxy istemci SSL sertifikasının türü                                  |
| `CURLOPT_PROXY_SSLKEY_BLOB`          | bellek bloğundan proxy sertifikası için özel anahtar                   |
| `CURLOPT_PROXY_SSLKEY`               | HTTPS proxy istemci sertifikası için özel anahtar dosyası              |
| `CURLOPT_PROXY_SSLKEYTYPE`           | proxy özel anahtar dosyasının türü                                     |
| `CURLOPT_PROXY_SSLVERSION`           | tercih edilen HTTPS proxy TLS sürümü                                   |
| `CURLOPT_PROXY_TLS13_CIPHERS`        | proxy TLS 1.3 için şifre takımları                                     |
| `CURLOPT_PROXY_TLSAUTH_PASSWORD`     | proxy TLS kimlik doğrulaması için kullanılacak şifre                   |
| `CURLOPT_PROXY_TLSAUTH_TYPE`         | HTTPS proxy TLS kimlik doğrulama yöntemleri                            |
| `CURLOPT_PROXY_TLSAUTH_USERNAME`     | proxy TLS kimlik doğrulaması için kullanılacak kullanıcı adı           |
| `CURLOPT_PROXY_TRANSFER_MODE`        | proxy için URL'ye FTP transfer modunu ekle                             |
| `CURLOPT_PROXY`                      | kullanılacak proxy                                                     |
| `CURLOPT_PROXYAUTH`                  | HTTP proxy kimlik doğrulama yöntemleri                                 |
| `CURLOPT_PROXYHEADER`                | proxy'ye iletilecek HTTP başlıkları seti                               |
| `CURLOPT_PROXYPASSWORD`              | proxy kimlik doğrulamasıyla kullanılacak şifre                         |
| `CURLOPT_PROXYPORT`                  | proxy'nin dinlediği port numarası                                      |
| `CURLOPT_PROXYTYPE`                  | proxy protokol türü                                                    |
| `CURLOPT_PROXYUSERNAME`              | proxy kimlik doğrulaması için kullanılacak kullanıcı adı               |
| `CURLOPT_PROXYUSERPWD`               | proxy kimlik doğrulaması için kullanılacak kullanıcı adı ve şifre      |
| `CURLOPT_PUT`                        | bir HTTP PUT isteği yap                                                |
| `CURLOPT_QUICK_EXIT`                 | hızlı çıkışa izin ver                                                  |
| `CURLOPT_QUOTE`                      | transferden önce çalıştırılacak (S)FTP komutları                       |
| `CURLOPT_RANDOM_FILE`                | rastgele verilerin okunacağı dosya                                     |
| `CURLOPT_RANGE`                      | istenecek bayt aralığı                                                 |
| `CURLOPT_READDATA`                   | okuma geri çağırımına iletilen işaretçi                                |
| `CURLOPT_READFUNCTION`               | veri yüklemeleri için okuma geri çağırımı                              |
| `CURLOPT_REDIR_PROTOCOLS_STR`        | yönlendirmeye izin verilen protokoller                                 |
| `CURLOPT_REDIR_PROTOCOLS`            | yönlendirmeye izin verilen protokoller                                 |
| `CURLOPT_REFERER`                    | HTTP referer başlığı                                                   |
| `CURLOPT_REQUEST_TARGET`             | bu istek için alternatif hedef                                         |
| `CURLOPT_RESOLVE`                    | IP adresi çözümlemeleri için özel ana bilgisayar adı sağla             |
| `CURLOPT_RESOLVER_START_DATA`        | çözümleyici başlatma geri çağırımına iletilen işaretçi                 |
| `CURLOPT_RESOLVER_START_FUNCTION`    | yeni bir ad çözümlemesi başlatılmadan önce çağrılan geri çağırım       |
| `CURLOPT_RESUME_FROM_LARGE`          | transferi sürdürmek için ofset                                         |
| `CURLOPT_RESUME_FROM`                | transferi sürdürmek için ofset                                         |
| `CURLOPT_RTSP_CLIENT_CSEQ`           | RTSP istemci CSEQ numarası                                             |
| `CURLOPT_RTSP_REQUEST`               | RTSP isteği                                                            |
| `CURLOPT_RTSP_SERVER_CSEQ`           | RTSP sunucu CSEQ numarası                                              |
| `CURLOPT_RTSP_SESSION_ID`            | RTSP oturum kimliği                                                    |
| `CURLOPT_RTSP_STREAM_URI`            | RTSP akış (stream) URI                                                 |
| `CURLOPT_RTSP_TRANSPORT`             | RTSP Transport: başlık                                                 |
| `CURLOPT_SASL_AUTHZID`               | yetkilendirme kimliği (rol yapılacak kimlik)                           |
| `CURLOPT_SASL_IR`                    | ilk pakette ilk yanıtı gönder                                          |
| `CURLOPT_SEEKDATA`                   | seek geri çağırımına iletilen işaretçi                                 |
| `CURLOPT_SEEKFUNCTION`               | girdi akışında arama (seeking) yapmak için kullanıcı geri çağırımı     |
| `CURLOPT_SERVER_RESPONSE_TIMEOUT`    | sunucu yanıtı için saniye cinsinden beklemeye izin verilen süre        |
| `CURLOPT_SERVER_RESPONSE_TIMEOUT_MS` | sunucu yanıtı için milisaniye cinsinden beklemeye izin verilen süre    |
| `CURLOPT_SERVICE_NAME`               | kimlik doğrulama hizmet adı                                            |
| `CURLOPT_SHARE`                      | kullanılacak paylaşım handle'ı                                         |
| `CURLOPT_SOCKOPTDATA`                | sockopt geri çağırımına iletilecek işaretçi                            |
| `CURLOPT_SOCKOPTFUNCTION`            | soket seçeneklerini ayarlamak için geri çağırım                        |
| `CURLOPT_SOCKS5_AUTH`                | SOCKS5 proxy kimlik doğrulama yöntemleri                               |
| `CURLOPT_SOCKS5_GSSAPI_NEC`          | socks proxy gssapi pazarlık koruması                                   |
| `CURLOPT_SOCKS5_GSSAPI_SERVICE`      | SOCKS5 proxy kimlik doğrulama hizmet adı                               |
| `CURLOPT_SSH_AUTH_TYPES`             | SFTP ve SCP için yetkilendirme türleri                                 |
| `CURLOPT_SSH_COMPRESSION`            | SSH sıkıştırmasını etkinleştir                                         |
| `CURLOPT_SSH_HOST_PUBLIC_KEY_MD5`    | SSH sunucusu genel anahtarının MD5 sağlama toplamı                     |
| `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` | SSH sunucusu genel anahtarının SHA256 karması                          |
| `CURLOPT_SSH_HOSTKEYDATA`            | SSH ana bilgisayar anahtarı geri çağırımına iletilecek işaretçi        |
| `CURLOPT_SSH_HOSTKEYFUNCTION`        | ana bilgisayar anahtarını kontrol etmek için geri çağırım              |
| `CURLOPT_SSH_KEYDATA`                | SSH anahtar geri çağırımına iletilen işaretçi                          |
| `CURLOPT_SSH_KEYFUNCTION`            | bilinen ana bilgisayar eşleştirme mantığı için geri çağırım            |
| `CURLOPT_SSH_KNOWNHOSTS`             | SSH bilinen ana bilgisayarları tutan dosya adı                         |
| `CURLOPT_SSH_PRIVATE_KEYFILE`        | SSH yetkilendirme için özel anahtar dosyası                            |
| `CURLOPT_SSH_PUBLIC_KEYFILE`         | SSH yetkilendirme için genel anahtar dosyası                           |
| `CURLOPT_SSL_CIPHER_LIST`            | TLS için kullanılacak şifreler                                         |
| `CURLOPT_SSL_CTX_DATA`               | ssl_ctx geri çağırımına iletilen işaretçi                              |
| `CURLOPT_SSL_CTX_FUNCTION`           | OpenSSL, wolfSSL veya mbedTLS için SSL bağlam geri çağırımı            |
| `CURLOPT_SSL_EC_CURVES`              | anahtar değişim eğrileri                                               |
| `CURLOPT_SSL_ENABLE_ALPN`            | Uygulama Katmanı Protokol Anlaşması (ALPN)                             |
| `CURLOPT_SSL_ENABLE_NPN`             | NPN kullan                                                             |
| `CURLOPT_SSL_FALSESTART`             | TLS false start                                                        |
| `CURLOPT_SSL_OPTIONS`                | SSL davranış seçenekleri                                               |
| `CURLOPT_SSL_SESSIONID_CACHE`        | SSL oturum kimliği önbelleğini kullan                                  |
| `CURLOPT_SSL_VERIFYHOST`             | sertifikanın adını ana bilgisayara karşı doğrula                       |
| `CURLOPT_SSL_VERIFYPEER`             | eşin SSL sertifikasını doğrula                                         |
| `CURLOPT_SSL_VERIFYSTATUS`           | sertifikanın durumunu doğrula                                          |
| `CURLOPT_SSLCERT_BLOB`               | bellek bloğundan SSL istemci sertifikası                               |
| `CURLOPT_SSLCERT`                    | SSL istemci sertifikası                                                |
| `CURLOPT_SSLCERTTYPE`                | istemci SSL sertifikasının türü                                        |
| `CURLOPT_SSLENGINE_DEFAULT`          | SSL motorunu varsayılan yap                                            |
| `CURLOPT_SSLENGINE`                  | SSL motor tanımlayıcısı                                                |
| `CURLOPT_SSLKEY_BLOB`                | bellek bloğundan istemci sertifikası için özel anahtar                 |
| `CURLOPT_SSLKEY`                     | TLS ve SSL istemci sertifikası için özel anahtar dosyası               |
| `CURLOPT_SSLKEYTYPE`                 | özel anahtar dosyasının türü                                           |
| `CURLOPT_SSLVERSION`                 | tercih edilen TLS/SSL sürümü                                           |
| `CURLOPT_STDERR`                     | stderr'i başka bir akışa yönlendir                                     |
| `CURLOPT_STREAM_DEPENDS_E`           | bu transferin özel olarak bağlı olduğu akış                            |
| `CURLOPT_STREAM_DEPENDS`             | bu transferin bağlı olduğu akış                                        |
| `CURLOPT_STREAM_WEIGHT`              | sayısal akış ağırlığı                                                  |
| `CURLOPT_SUPPRESS_CONNECT_HEADERS`   | kullanıcı geri çağırımlarından proxy CONNECT yanıt başlıklarını gizle  |
| `CURLOPT_TCP_FASTOPEN`               | TCP Hızlı Açma                                                         |
| `CURLOPT_TCP_KEEPALIVE`              | TCP canlı tutma sondalaması                                            |
| `CURLOPT_TCP_KEEPIDLE`               | TCP canlı tutma bekleme süresi                                         |
| `CURLOPT_TCP_KEEPINTVL`              | TCP canlı tutma aralığı                                                |
| `CURLOPT_TCP_NODELAY`                | TCP_NODELAY seçeneği                                                   |
| `CURLOPT_TELNETOPTIONS`              | telnet seçenekleri seti                                                |
| `CURLOPT_TFTP_BLKSIZE`               | TFTP blok boyutu                                                       |
| `CURLOPT_TFTP_NO_OPTIONS`            | TFTP seçenek istekleri gönderme                                        |
| `CURLOPT_TIMECONDITION`              | zaman isteği için koşul seç                                            |
| `CURLOPT_TIMEOUT_MS`                 | transferin tamamlanmasına izin verilen maksimum süre                   |
| `CURLOPT_TIMEOUT`                    | transferin tamamlanmasına izin verilen maksimum süre                   |
| `CURLOPT_TIMEVALUE_LARGE`            | koşullu için zaman değeri                                              |
| `CURLOPT_TIMEVALUE`                  | koşullu için zaman değeri                                              |
| `CURLOPT_TLS13_CIPHERS`              | TLS 1.3 için kullanılacak şifre takımları                              |
| `CURLOPT_TLSAUTH_PASSWORD`           | TLS kimlik doğrulaması için kullanılacak şifre                         |
| `CURLOPT_TLSAUTH_TYPE`               | TLS kimlik doğrulama yöntemleri                                        |
| `CURLOPT_TLSAUTH_USERNAME`           | TLS kimlik doğrulaması için kullanılacak kullanıcı adı                 |
| `CURLOPT_TRAILERDATA`                | sondaki başlıklar geri çağırımına iletilen işaretçi                    |
| `CURLOPT_TRAILERFUNCTION`            | sondaki başlıkları göndermek için geri çağırım                         |
| `CURLOPT_TRANSFER_ENCODING`          | HTTP Transfer Encoding iste                                            |
| `CURLOPT_TRANSFERTEXT`               | FTP için metin tabanlı bir transfer iste                               |
| `CURLOPT_UNIX_SOCKET_PATH`           | Unix etki alanı soketi                                                 |
| `CURLOPT_UNRESTRICTED_AUTH`          | kimlik bilgilerini diğer ana bilgisayarlara da gönder                  |
| `CURLOPT_UPKEEP_INTERVAL_MS`         | bağlantı bakım aralığı                                                 |
| `CURLOPT_UPLOAD_BUFFERSIZE`          | yükleme tampon boyutu                                                  |
| `CURLOPT_UPLOAD`                     | veri yükleme                                                           |
| `CURLOPT_URL`                        | bu transfer için URL                                                   |
| `CURLOPT_USE_SSL`                    | transfer için SSL / TLS kullanılmasını iste                            |
| `CURLOPT_USERAGENT`                  | HTTP user-agent başlığı                                                |
| `CURLOPT_USERNAME`                   | kimlik doğrulamasında kullanılacak kullanıcı adı                       |
| `CURLOPT_USERPWD`                    | kimlik doğrulamasında kullanılacak kullanıcı adı ve şifre              |
| `CURLOPT_VERBOSE`                    | ayrıntılı (verbose) mod                                                |
| `CURLOPT_WILDCARDMATCH`              | dizin joker karakter transferleri                                      |
| `CURLOPT_WRITEDATA`                  | yazma geri çağırımına iletilen işaretçi                                |
| `CURLOPT_WRITEFUNCTION`              | alınan verileri yazmak için geri çağırım                               |
| `CURLOPT_WS_OPTIONS`                 | WebSocket davranış seçenekleri                                         |
| `CURLOPT_XFERINFODATA`               | ilerleme geri çağırımına iletilen işaretçi                             |
| `CURLOPT_XFERINFOFUNCTION`           | ilerleme ölçer geri çağırımı                                           |
| `CURLOPT_XOAUTH2_BEARER`             | OAuth 2.0 erişim belirteci                                             |
