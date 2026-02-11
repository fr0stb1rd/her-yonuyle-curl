# İstekler (Requests)

Bir HTTP isteği, curl'ün sunucuya ne yapacağını söylediğinde gönderdiği şeydir. Veri almak veya veri göndermek istediğinde. HTTP içeren tüm transferler bir HTTP isteğiyle başlar.

Bir HTTP isteği bir yöntem, bir yol, HTTP sürümü ve bir dizi istek başlığı içerir. libcurl kullanan bir uygulama tüm bu alanları değiştirebilir.

## İstek yöntemi

Her HTTP isteği, bazen "fiil" olarak da adlandırılan bir "yöntem" içerir. Genellikle GET, HEAD, POST veya PUT gibi bir şeydir ancak DELETE, PATCH ve OPTIONS gibi daha ezoterik olanlar da vardır.

Genellikle bir transferi kurmak ve gerçekleştirmek için libcurl kullandığınızda, belirli istek yöntemi kullandığınız seçenekler tarafından ima edilir. Sadece bir URL isterseniz, yöntem `GET` anlamına gelirken, örneğin `CURLOPT_POSTFIELDS` ayarlarsanız bu libcurl'ün `POST` yöntemini kullanmasını sağlar. `CURLOPT_UPLOAD` seçeneğini true olarak ayarlarsanız, libcurl HTTP isteğinde bir `PUT` yöntemi gönderir vb. `CURLOPT_NOBODY` istemek libcurl'ün `HEAD` kullanmasını sağlar.

Ancak bazen bu varsayılan HTTP yöntemleri yeterince iyi değildir veya transferinizin kullanmasını istediğiniz yöntemler değildir. O zaman `CURLOPT_CUSTOMREQUEST` ile libcurl'e istediğiniz belirli yöntemi kullanmasını söyleyebilirsiniz. Örneğin, seçtiğiniz URL'ye bir `DELETE` yöntemi göndermek istiyorsunuz:

    curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "DELETE");
    curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/file.txt");

CURLOPT_CUSTOMREQUEST ayarı, HTTP istek satırında yöntem olarak kullanılacak tek anahtar kelime olmalıdır. HTTP istek başlıklarını değiştirmek veya eklemek istiyorsanız aşağıdaki bölüme bakın.

## HTTP istek başlıklarını özelleştirme

libcurl, istediğiniz veri transferlerini gerçekleştirmenin bir parçası olarak HTTP istekleri yayınladığında, bunları kendisine verilen görevi yerine getirmek için uygun olan bir dizi HTTP başlığıyla gönderir.

Sadece `http://localhost/file1.txt` URL'si verildiğinde, libcurl sunucuya şu isteği gönderir:

    GET /file1.txt HTTP/1.1
    Host: localhost
    Accept: */*

Uygulamanıza `CURLOPT_POSTFIELDS` seçeneğini "foobar" dizesine (6 harf, tırnak işaretleri sadece burada görsel sınırlayıcı olarak kullanılmıştır) ayarlamasını da söylerseniz, şu başlıkları gönderir:

    POST /file1.txt HTTP/1.1
    Host: localhost
    Accept: */*
    Content-Length: 6
    Content-Type: application/x-www-form-urlencoded

libcurl'ün gönderdiği varsayılan başlık setinden memnun değilseniz, uygulama HTTP isteğindeki başlıkları ekleme, değiştirme veya kaldırma gücüne sahiptir.

### Bir başlık ekle

Aksi takdirde istekte bulunmayacak bir başlık eklemek için `CURLOPT_HTTPHEADER` ile ekleyin. `Mr. Smith` içeren `Name:` adında bir başlık istediğinizi varsayalım:

    struct curl_slist *list = NULL;
    list = curl_slist_append(list, "Name: Mr Smith");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, list);
    curl_easy_perform(curl);
    curl_slist_free_all(list); /* listeyi tekrar serbest bırak */

### Bir başlığı değiştir

Bu varsayılan başlıklardan biri memnuniyetinizi karşılamıyorsa bunları değiştirebilirsiniz. Örneğin varsayılan `Host:` başlığının yanlış olduğunu düşünüyorsanız (libcurl'e verdiğiniz URL'den türetilmiş olsa bile), libcurl'e kendinizinkini söyleyebilirsiniz:

    struct curl_slist *list = NULL;
    list = curl_slist_append(list, "Host: Alternative");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, list);
    curl_easy_perform(curl);
    curl_slist_free_all(list); /* listeyi tekrar serbest bırak */

### Bir başlığı kaldır

libcurl'ün bir istekte gerçekten kullanmaması gerektiğini düşündüğünüz bir başlık kullandığını düşündüğünüzde, ona o başlığı istekten kaldırmasını kolayca söyleyebilirsiniz. Örneğin `Accept:` başlığını kaldırmak istiyorsanız. Sadece iki nokta üst üstenin sağında hiçbir şey olmayan başlık adını sağlayın:

    struct curl_slist *list = NULL;
    list = curl_slist_append(list, "Accept:");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, list);
    curl_easy_perform(curl);
    curl_slist_free_all(list); /* listeyi tekrar serbest bırak */

### İçeriği olmayan bir başlık sağla

Yukarıdaki bölümlerde fark etmiş olabileceğiniz gibi, iki nokta üst üstenin sağ tarafında içeriği olmayan bir başlık eklemeye çalışırsanız, bu bir kaldırma talimatı olarak ele alınır ve bunun yerine o başlığın gönderilmesini tamamen engeller. Bunun yerine *gerçekten* sağ tarafında sıfır içerik olan bir başlık göndermek istiyorsanız, özel bir işaretleyici kullanmanız gerekir. Başlığı düzgün bir iki nokta üst üste yerine noktalı virgül ile sağlamalısınız. `Header;` gibi. Giden HTTP isteğine iki nokta üst üstenin ardından hiçbir şey gelmeyen sadece `Moo:` olan bir başlık eklemek isterseniz, şöyle yazabilirsiniz:

    struct curl_slist *list = NULL;
    list = curl_slist_append(list, "Moo;");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, list);
    curl_easy_perform(curl);
    curl_slist_free_all(list); /* listeyi tekrar serbest bırak */

## Yönlendiren (Referrer)

`Referer:` başlığı (evet, yanlış yazılmıştır), sunucuya kullanıcı aracısının şu anda talep ettiği URL'ye ulaştığında hangi URL'den yönlendirildiğini söyleyen standart bir HTTP başlığıdır. Normal bir başlıktır, bu nedenle yukarıda gösterildiği gibi `CURLOPT_HEADER` yaklaşımıyla kendiniz ayarlayabilir veya `CURLOPT_REFERER` olarak bilinen kısayolu kullanabilirsiniz. Şöyle:

    curl_easy_setopt(curl, CURLOPT_REFERER, "https://example.com/fromhere/");
    curl_easy_perform(curl);

### Otomatik yönlendiren

libcurl'den `CURLOPT_FOLLOWLOCATION` seçeneğiyle yönlendirmeleri kendisinin takip etmesi istendiğinde ve yine de `Referer:` başlığının yönlendirmeyi yaptığı doğru önceki URL'ye ayarlanmasını istiyorsanız, libcurl'den bunu kendisinin ayarlamasını isteyebilirsiniz:

    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    curl_easy_setopt(curl, CURLOPT_AUTOREFERER, 1L);
    curl_easy_setopt(curl, CURLOPT_URL, "https://example.com/redirected.cgi");
    curl_easy_perform(curl);
