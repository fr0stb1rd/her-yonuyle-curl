# Sürüm

Hangi curl sürümünü yüklediğinizi öğrenmek için şunu çalıştırın:

    curl --version

veya kısa versiyonu kullanın:

    curl -V

Bu komut satırından gelen çıktı tipik olarak dört satırdır; bunlardan bazıları oldukça uzundur ve terminal pencerenizde sarılabilir.

Haziran 2020'de bir Debian Linux'tan örnek çıktı:

    curl 7.68.0 (x86_64-pc-linux-gnu) libcurl/7.68.0 OpenSSL/1.1.1g
    zlib/1.2.11 brotli/1.0.7 libidn2/2.3.0 libpsl/0.21.0 (+libidn2/2.3.0)
    libssh2/1.8.0 nghttp2/1.41.0 librtmp/2.3
    Release-Date: 2020-01-08
    Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3
    pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
    Features: AsynchDNS brotli GSS-API HTTP2 HTTPS-proxy IDN IPv6 Kerberos
    Largefile libz NTLM NTLM_WB PSL SPNEGO SSL TLS-SRP UnixSockets

aynı tarihte bir Windows 10 makinesinde çağrılan aynı komut satırı şöyle görünürken:

    curl 7.55.1 (Windows) libcurl/7.55.1 WinSSL
    Release-Date: [unreleased]
    Protocols: dict file ftp ftps http https imap imaps pop3 pop3s smtp smtps
    telnet tftp
    Features: AsynchDNS IPv6 Largefile SSPI Kerberos SPNEGO NTLM SSL

Dört satırın anlamı nedir?

## Satır 1: curl

İlk satır `curl` ile başlar ve önce aracın ana sürüm numarasını gösterir. Ardından parantez içinde aracın hangi platform için oluşturulduğu ve libcurl sürümü gelir. Bu üç alan tüm curl derlemeleri için ortaktır.

curl sürüm numarasının sonuna `-DEV` eklenmişse, bu sürümün doğrudan geliştirilmekte olan bir kaynak kodundan oluşturulduğu ve resmi olarak yayınlanmış ve onaylanmış bir sürüm olmadığı anlamına gelir.

Bu satırın geri kalanı, curl'ün bu derlemesinin kullandığı üçüncü taraf bileşenlerin adlarını içerir, genellikle eğik çizgi ayırıcısıyla birlikte kendi sürüm numaraları yanlarında bulunur. `OpenSSL/1.1.1g` ve `nghttp2/1.41.0` gibi. Bu örneğin size bu curl'ün hangi TLS arka uçlarını kullandığını söyleyebilir.

### Satır 1: TLS sürümleri

Satır 1 bir veya daha fazla TLS kütüphanesi içerebilir. curl birden fazla TLS kütüphanesini destekleyecek şekilde oluşturulabilir, bu da curl'ün - başlangıçta - bu çağrı için hangi belirli arka ucun (backend) kullanılacağını seçmesini sağlar.

curl bu şekilde birden fazla TLS kütüphanesini destekliyorsa, varsayılan olarak *seçilmeyenler* parantez içinde listelenir. Böylece, hangi arka ucun kullanılacağını belirtmezseniz (`CURL_SSL_BACKEND` ortam değişkeni ile), parantez olmadan listelenen kullanılır.

## Satır 2: Sürüm Tarihi (Release-Date)

Bu satır, bu curl sürümünün curl projesi tarafından yayınlandığı tarihi gösterir ve orijinal olarak yayınlandıktan sonra bir şekilde güncellendiyse ikincil bir "Yama tarihi" de gösterebilir.

curl bir sürüm tarball'ı yerine başka bir yolla oluşturulduysa `[unreleased]` yazar ve yukarıda görebileceğiniz gibi Microsoft'un Windows 10 için yaptığı budur ve curl projesi bunu önermez.

## Satır 3: Protokoller (Protocols)

Bu, bu curl derlemesinin desteklediği tüm transfer protokollerinin (aslında URL şemalarının) alfabetik sıraya göre bir listesidir. Tüm adlar küçük harflerle gösterilir.

Bu liste şu protokolleri içerebilir:

dict, file, ftp, ftps, gopher, http, https, imap, imaps, ldap, ldaps, mqtt,
pop3, pop3s, rtmp, rtsp, scp, sftp, smb, smbs, smtp, smtps, telnet ve tftp

## Satır 4: Özellikler (Features)

curl'ün bu derlemesinin desteklediği özelliklerin listesi. İsim listede varsa, o özellik etkindir. İsim yoksa, o özellik etkin değildir.

Orada bulunabilecek özellikler:

 - **alt-svc** - alt-svc: başlığı desteği
 - **AsynchDNS** - Bu curl senkronize olmayan ad çözümlemeleri kullanır. Senkronize olmayan
   ad çözümlemeleri c-ares veya iş parçacıklı çözücü arka uçları kullanılarak yapılabilir.
 - **brotli** - HTTP(S) üzerinden otomatik brotli sıkıştırma desteği
 - **CharConv** - curl karakter seti dönüşümleri (EBCDIC gibi) desteği ile oluşturuldu
 - **Debug** - Bu curl Debug ile oluşturulmuş bir libcurl kullanır. Bu daha fazla
   hata izleme ve bellek hata ayıklama vb. sağlar. Sadece curl geliştiricileri içindir.
 - **GSS-API** - GSS-API kimlik doğrulaması etkindir
 - **HTTP2** - HTTP/2 desteği yerleşiktir.
 - **HTTP3** - HTTP/3 desteği yerleşiktir.
 - **HTTPS-proxy** - Bu curl HTTPS proxy'yi desteklemek için oluşturulmuştur.
 - **IDN** - Bu curl IDN'i - uluslararası alan adlarını destekler.
 - **IPv6** - Bununla IPv6 kullanabilirsiniz.
 - **krb4** - FTP için Krb4 desteklenir
 - **Largefile** - Bu curl büyük dosyaların, 2GB'dan büyük dosyaların transferini destekler.
 - **libz** - HTTP üzerinden sıkıştırılmış dosyaların otomatik gzip açılması desteklenir.
 - **Metalink** - Bu curl Metalink'i destekler. Modern curl sürümlerinde bu
   seçenek asla mevcut değildir.
 - **MultiSSL** - Bu curl birden fazla TLS arka ucunu destekler. İlk satır
    tam olarak hangi TLS kütüphaneleri olduğunu detaylandırır.
 - **NTLM** - NTLM kimlik doğrulaması desteklenir.
 - **NTLM_WB** - NTLM kimlik doğrulaması desteklenir.
 - **PSL** - Public Suffix List (PSL) mevcuttur ve bu, bu curl'ün
   tanımlama bilgileri (cookies) için kullanılan *genel son ekler* hakkında bilgi sahibi olarak oluşturulduğu anlamına gelir.
 - **SPNEGO** - SPNEGO kimlik doğrulaması desteklenir.
 - **SSL** - HTTPS, FTPS, POP3S vb. gibi çeşitli protokollerin SSL sürümleri desteklenir.
 - **SSPI** - SSPI desteklenir
 - **TLS-SRP** - TLS için SRP (Secure Remote Password) kimlik doğrulaması desteklenir.
 - **UnixSockets** - Unix soketleri desteği sağlanır.
