# Ad çözme (Name resolving)

libcurl'ün yapabileceği çoğu transfer, önce bir İnternet adresine çevrilmesi gereken bir ad içerir. Bu ad çözmedir. Sayısal bir IP adresini doğrudan URL'de kullanmak genellikle ad çözme aşamasını önler ancak çoğu durumda adı IP adresiyle manuel olarak değiştirmek kolay değildir.

libcurl, yeni bir bağlantı oluşturmak yerine [mevcut bir bağlantıyı yeniden kullanmaya](reuse.md) çok çalışır. Kullanılacak mevcut bir bağlantıyı kontrol eden işlev tamamen ada dayanır ve herhangi bir ad çözme denenmeden önce gerçekleştirilir. Yeniden kullanımın bu kadar hızlı olmasının nedenlerinden biri de budur. Yeniden kullanılan bir bağlantıyı kullanan bir transfer, ana bilgisayar adını tekrar çözmez.

Hiçbir bağlantı yeniden kullanılamazsa, libcurl ana bilgisayar adını çözüldüğü adresler kümesine çözer. Genellikle bu, hem IPv4 hem de IPv6 adreslerini istemek anlamına gelir ve libcurl'e döndürülen bunlardan oluşan koca bir küme olabilir. Bu adres kümesi daha sonra biri çalışana kadar denenir veya başarısızlık döndürür.

Bir uygulama, `CURLOPT_IPRESOLVE` seçeneğini tercih edilen değere ayarlayarak libcurl'ü yalnızca bir IPv4 veya IPv6 çözülmüş adresi kullanmaya zorlayabilir. Örneğin, yalnızca IPv6 adreslerini kullanmayı isteyin:

    curl_easy_setopt(easy, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V6);

## Ad çözümleyici arka uçları

libcurl, ad çözümlerini bu üç farklı yoldan biriyle yapacak şekilde oluşturulabilir ve hangi arka uç yolunun kullanıldığına bağlı olarak biraz farklı bir özellik seti ve bazen değiştirilmiş davranış alır.

1. Varsayılan arka uç, normal libc çözümleyici işlevlerini yeni bir yardımcı iş parçacığında çağırmaktır, böylece istenirse hala hassas zaman aşımları yapabilir ve engelleme çağrıları söz konusu olmaz.

2. Eski sistemlerde, libcurl standart eşzamanlı ad çözümleyici işlevlerini kullanır. Maalesef bunlar, işlemi sırasında bir multi handle içindeki tüm transferleri engeller ve güzel bir şekilde zaman aşımına uğraması çok daha zordur.

3. Ayrıca, iş parçacığı kullanmadan eşzamansız ad çözmeyi destekleyen c-ares üçüncü taraf kütüphanesiyle çözme desteği de vardır. Bu, çok sayıda paralel transfere daha iyi ölçeklenir ancak yerel ad çözümleyici işlevselliğiyle her zaman %100 uyumlu değildir.

### HTTPS üzerinden DNS (DNS over HTTPS)

libcurl hangi çözümleyici arka ucunu kullanacak şekilde oluşturulmuş olursa olsun, 7.62.0'dan bu yana kullanıcıya bir adın adresi için belirli bir DoH (HTTPS üzerinden DNS) sunucusuna sorması için bir yol da sağlar. Bu, normal, yerel çözümleyici yöntemini ve sunucusunu kullanmaktan kaçınır ve bunun yerine özel bir ayrı sunucuya sorar.

Bir DoH sunucusu, `CURLOPT_DOH_URL` seçeneğiyle tam bir URL olarak şöyle belirtilir:

    curl_easy_setopt(easy, CURLOPT_DOH_URL, "https://example.com/doh");

Bu seçeneğe iletilen URL https:// kullanmalıdır ve libcurl'ün DoH sunucusuna olan bağlantı üzerinden çoğullanan birden çok DoH isteğini gerçekleştirebilmesi için HTTP/2 desteğinin etkinleştirilmiş olması genellikle önerilir.

## Önbelleğe alma

Bir ad çözüldüğünde, sonuç libcurl'ün bellek içi önbelleğinde saklanır, böylece aynı adın sonraki çözümleri ad DNS önbelleğinde tutulduğu sürece anında gerçekleşir. Varsayılan olarak, her giriş önbellekte 60 saniye tutulur ancak bu değer `CURLOPT_DNS_CACHE_TIMEOUT` ile değiştirilebilir.

DNS önbelleği, `curl_easy_perform` kullanıldığında easy handle içinde veya multi arayüz kullanıldığında multi handle içinde tutulur. Ayrıca [paylaşım arayüzü](../../helpers/sharing.md) kullanılarak birden fazla easy handle arasında paylaşılabilir hale getirilebilir.

## Ana bilgisayarlar için özel adresler

Bazen gerçek ana bilgisayar adları için sahte, özel adresler sağlamak kullanışlıdır, böylece libcurl gerçek bir ad çözümlemesinin önereceği adres yerine farklı bir adrese bağlanır.

[CURLOPT_RESOLVE](https://curl.se/libcurl/c/CURLOPT_RESOLVE.html) seçeneğinin yardımıyla, bir uygulama libcurl'ün DNS önbelleğini belirli bir ana bilgisayar adı ve port numarası için özel bir adresle önceden doldurabilir.

example.com port 443'te istendiğinde libcurl'ün 127.0.0.1'e bağlanmasını sağlamak için bir uygulama şunları yapabilir:

    struct curl_slist *dns;
    dns = curl_slist_append(NULL, "example.com:443:127.0.0.1");
    curl_easy_setopt(curl, CURLOPT_RESOLVE, dns);

Bu, sahte adresi DNS önbelleğine koyduğundan, yönlendirmeleri vb. takip ederken bile çalışır.

## Ad sunucusu seçenekleri

c-ares kullanmak üzere oluşturulmuş libcurl için, hangi DNS sunucularının kullanılacağı ve nasıl kullanılacağı konusunda hassas kontrol sunan birkaç seçenek vardır. Bu, tamamen c-ares derlemesiyle sınırlıdır çünkü bunlar, ad çözme için standart sistem çağrıları kullanıldığında mevcut olmayan güçlerdir.

 - `CURLOPT_DNS_SERVERS` ile uygulama, bir dizi özel DNS sunucusu kullanmayı seçebilir.

 - `CURLOPT_DNS_INTERFACE` ile libcurl'e varsayılan yerine hangi ağ arayüzü üzerinden DNS konuşacağını söyleyebilir.

 - `CURLOPT_DNS_LOCAL_IP4` ve `CURLOPT_DNS_LOCAL_IP6` ile uygulama, DNS çözümlerini hangi belirli ağ adreslerine bağlayacağını belirtebilir.

## Küresel DNS önbelleği yok

`CURLOPT_DNS_USE_GLOBAL_CACHE` adlı seçenek bir zamanlar curl'e küresel bir DNS önbelleği kullanmasını söylüyordu. Bu işlevsellik 7.65.0'dan beri kaldırılmıştır, bu nedenle bu seçenek hala mevcut olsa da hiçbir şey yapmaz.
