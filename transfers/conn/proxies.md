# Vekil sunucular (Proxies)

Ağ bağlamında bir proxy (vekil sunucu), bir aracıdır; bir istemci olarak sizinle iletişim kurmak istediğiniz uzak sunucu arasında duran bir sunucudur. İstemci aracı ile iletişim kurar, o da sizin için uzak sunucuyla iletişim kurmaya devam eder.

Bu tarz proxy kullanımı bazen şirketler ve kuruluşlar tarafından kullanılır, bu durumda genellikle hedef sunucuya ulaşmak için bunları kullanmanız gerekir.

Birkaç farklı türde proxy ve bir proxy ile iletişim kurarken kullanılacak farklı protokoller vardır ve libcurl en yaygın proxy protokollerinden birkaçını destekler. Proxy ile kullanılan protokolün uzak sunucuyla kullanılan protokolle aynı olması gerekmediğini anlamak önemlidir.

libcurl ile bir transfer ayarlarken, proxy'nin sunucu adını ve port numarasını belirtmeniz gerekir. Favori tarayıcılarınızın bunu libcurl'den biraz daha gelişmiş yollarla yapabildiğini görebilirsiniz ve sonraki bölümlerde bu tür ayrıntılara gireceğiz.

## Proxy türleri

libcurl iki ana proxy türünü destekler: SOCKS ve HTTP proxy'leri. Daha spesifik olarak, hem SOCKS4 hem de SOCKS5'i (uzak ad araması olan veya olmayan), ayrıca yerel proxy'ye hem HTTP hem de HTTPS'i destekler.

Hangi tür proxy ile konuştuğunuzu belirtmenin en kolay yolu, proxy ana bilgisayar adı dizesinin (`CURLOPT_PROXY`) şema kısmını onunla eşleşecek şekilde ayarlamaktır:

    socks4://proxy.example.com:12345/
    socks4a://proxy.example.com:12345/
    socks5://proxy.example.com:12345/
    socks5h://proxy.example.com:12345/
    http://proxy.example.com:12345/
    https://proxy.example.com:12345/

`socks4` - yerel ad çözme ile SOCKS4 anlamına gelir

`socks4a` - proxy'nin ad çözmesi ile SOCKS4 anlamına gelir

`socks5` - yerel ad çözme ile SOCKS5 anlamına gelir

`socks5h` - proxy'nin ad çözmesi ile SOCKS5 anlamına gelir

`http` - HTTP anlamına gelir, bu her zaman proxy'nin adları çözmesine izin verir

`https` - **proxy'ye** HTTPS anlamına gelir, bu her zaman proxy'nin adları çözmesine izin verir.

Yalnızca ana bilgisayar adını ayarlamayı tercih ediyorsanız, `CURLOPT_PROXYTYPE` kullanarak proxy türünü ayrı bir seçenekle ayarlamayı da seçebilirsiniz. Benzer şekilde, `CURLOPT_PROXYPORT` ile kullanılacak proxy port numarasını ayarlayabilirsiniz.

## Yerel veya proxy ad araması

Yukarıdaki bir bölümde, farklı proxy kurulumlarının ad çözümlemesinin transfere dahil olan farklı taraflarca yapılmasına izin verdiğini görebilirsiniz. Birkaç durumda, istemcinin sunucu ana bilgisayar adını çözmesini ve bağlanmak için IP adresini proxy'ye iletmesini sağlayabilirsiniz - bu da elbette ad aramasının istemci sisteminde doğru bir şekilde çalıştığını varsayar - veya adı proxy'ye verip proxy'nin adı çözmesini sağlayabilirsiniz; bağlanmak için bir IP adresine dönüştürerek.

Bir HTTP veya HTTPS proxy kullanırken, adı her zaman çözmesi için proxy'ye verirsiniz.

## Hangi proxy?

Ağ bağlantınız hedefe ulaşmak için bir proxy kullanılmasını gerektiriyorsa, bunu anlamalı ve libcurl'e doğru proxy'yi kullanmasını söylemelisiniz. libcurl'de bir proxy'yi otomatik olarak anlamasını veya algılamasını sağlayacak bir destek yoktur.

Bir tarayıcı kullanırken, proxy'yi bir PAC betiği veya başka araçlarla sağlamak popülerdir ancak bunların hiçbiri libcurl tarafından tanınmaz.

### Proxy ortam değişkenleri

Hiçbir proxy seçeneği ayarlanmamışsa, libcurl transferini gerçekleştirmeden önce bir proxy'nin kullanılması istenip istenmediğini görmek için özel olarak adlandırılmış ortam değişkenlerinin varlığını kontrol eder.

Proxy ana bilgisayar adını tutmak için `[scheme]_proxy` adlı bir değişken ayarlayarak proxy'yi belirtebilirsiniz (ana bilgisayarı `-x` ile belirttiğiniz gibi). Bir HTTP sunucusuna erişirken curl'e bir proxy kullanmasını söylemek istiyorsanız `http_proxy` ortam değişkenini ayarlarsınız. Şöyle:

    http_proxy=http://proxy.example.com:80

Yukarıdaki proxy örneği HTTP içindir, ancak elbette proxy yapmak istediğiniz belirli protokoller için `ftp_proxy`, `https_proxy` vb. de ayarlayabilirsiniz. http_proxy dışındaki tüm bu proxy ortam değişkeni adları `HTTPS_PROXY` gibi büyük harfle de belirtilebilir.

*Tüm* protokolleri kontrol eden tek bir değişken ayarlamak için `ALL_PROXY` mevcuttur. Belirli bir protokol değişkeni mevcutsa, o önceliklidir.

Proxy ayarlamak için ortam değişkenlerini kullanırken, bir veya birkaç ana bilgisayar adının proxy'den geçmesinin hariç tutulması gereken bir duruma kolayca düşebilirsiniz. Bu, `NO_PROXY` değişkeniyle - veya karşılık gelen `CURLOPT_NOPROXY` libcurl seçeneğiyle - yapılabilir. Bunu, erişilirken bir proxy kullanmaması gereken, virgülle ayrılmış ana bilgisayar adları listesine ayarlayın. NO_PROXY'yi tüm ana bilgisayarlarla eşleşmesi için tek bir yıldıza ('\*') ayarlayabilirsiniz.

## HTTP proxy

HTTP protokolü, bir HTTP proxy'sinin tam olarak nasıl kullanılması gerektiğini ayrıntılandırır. İsteği asıl uzak sunucuya göndermek yerine, istemci (libcurl) bunun yerine proxy'den belirli kaynağı ister. HTTP proxy'sine bağlantı, düz şifrelenmemiş HTTP kullanılarak yapılır.

Bir HTTPS kaynağı istenirse, libcurl bunun yerine proxy'ye bir `CONNECT` isteği gönderir. Böyle bir istek, proxy üzerinden verileri anlamadan geçirdiği bir tünel açar. Bu şekilde, bir HTTP proxy'si mevcut olsa bile libcurl uçtan uca güvenli bir TLS bağlantısı kurabilir.

HTTP olmayan protokolleri bir HTTP proxy üzerinden proxy *yapabilirsiniz*, ancak bu çoğunlukla verileri tünellemek için CONNECT yöntemiyle yapıldığından, proxy'nin istemcinin o diğer belirli uzak port numaralarına bağlanmasına izin verecek şekilde yapılandırılmasını gerektirir. Birçok HTTP proxy'si, 80 ve 443 dışındaki port numaralarına bağlantıları engelleyecek şekilde ayarlanmıştır.

## HTTPS proxy

Bir HTTPS proxy'si, bir HTTP proxy'sine benzer ancak istemcinin ona güvenli bir HTTPS bağlantısı kullanarak bağlanmasına izin verir. Proxy bağlantısı uzak siteye olan bağlantıdan ayrı olduğundan (bu durumda bile uzak siteye HTTPS, proxy'ye HTTPS bağlantısı üzerinden tünellenir), libcurl proxy bağlantısı için uzak ana bilgisayara olan bağlantıdan ayrı bir dizi TLS seçeneği sunar.

Örneğin, `CURLOPT_PROXY_CAINFO` uzak ana bilgisayar için `CURLOPT_CAINFO` neyse HTTPS proxy için aynı işlevdir. `CURLOPT_PROXY_SSL_VERIFYPEER`, `CURLOPT_SSL_VERIFYPEER`'ın proxy sürümüdür vb.

libcurl varsayılan olarak HTTPS proxy'lerine HTTP/1 konuşur. Proxy de bir `https://` şeması kullanacak şekilde ayarlandığında `CURLOPT_PROXYTYPE`'ı `CURLPROXY_HTTPS2` olarak ayarlayarak HTTP/2 kullanmayı denemesini sağlayabilirsiniz. Proxy'ye HTTP/2 kullanırken, libcurl uzak protokol TLS tabanlı olmadığı sürece farklı uzak sunucuyla konuşurken proxy bağlantısını yeniden kullanabilir ve bunun üzerinden çoğullanmış transferler yapabilir.

## Proxy kimlik doğrulaması

Bir proxy ile kimlik doğrulama, proxy'nin kendisiyle yapılan el sıkışma pazarlığında geçerli kimlik bilgileri sağlamanız gerektiği anlamına gelir. Proxy kimlik doğrulaması, uzak ana bilgisayarla olası kimlik doğrulamasına veya kimlik doğrulama eksikliğine ek olarak ve ondan ayrıdır.

libcurl HTTP, HTTPS ve SOCKS5 proxy'leri ile kimlik doğrulamayı destekler. Anahtar seçenek o zaman kullanılacak kullanıcı adını ve şifreyi ayarlayan `CURLOPT_PROXYUSERPWD`'dir - `CURLOPT_PROXY` dizesi içinde ayarlamadıysanız.

## HTTP Proxy başlıkları

Bir HTTP veya HTTPS proxy ile, libcurl proxy'ye bir dizi başlık içeren bir istek gönderir. Bir uygulama, tıpkı sunuculara gönderilen isteklerde olduğu gibi başlıkları değiştirebilir.

libcurl, **sunucuya gönderilen ayrı bir istek olduğunda** bir proxy'ye gönderilen başlıkları kontrol etmek için `CURLOPT_PROXYHEADER` sunar. Bu genellikle proxy üzerinden bir tünel kurmak için bir proxy'ye gönderilen ilk `CONNECT` isteği anlamına gelir.
