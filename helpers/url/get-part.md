# URL parçalarını al (Get URL parts)

`CURLU` handle, bir URL'nin bireysel parçalarını saklar ve uygulama bu parçaları istediği zaman handle'dan ayrı ayrı çıkarabilir. Eğer ayarlanmışlarsa.

`curl_url_get()` işlevinin ikinci argümanı hangi parçanın çıkarılmasını istediğinizi belirtir. Hepsi null ile sonlandırılmış `char *` verisi olarak çıkarılır, bu nedenle böyle bir değişkene bir işaretçi iletirsiniz.

    char *host;
    rc = curl_url_get(h, CURLUPART_HOST, &host, 0);

    char *scheme;
    rc = curl_url_get(h, CURLUPART_SCHEME, &scheme, 0);

    char *user;
    rc = curl_url_get(h, CURLUPART_USER, &user, 0);

    char *password;
    rc = curl_url_get(h, CURLUPART_PASSWORD, &password, 0);

    char *port;
    rc = curl_url_get(h, CURLUPART_PORT, &port, 0);

    char *path;
    rc = curl_url_get(h, CURLUPART_PATH, &path, 0);

    char *query;
    rc = curl_url_get(h, CURLUPART_QUERY, &query, 0);

    char *fragment;
    rc = curl_url_get(h, CURLUPART_FRAGMENT, &fragment, 0);

    char *zoneid;
    rc = curl_url_get(h, CURLUPART_ZONEID, &zoneid, 0);

Bununla işiniz bittiğinde döndürülen dizeyi `curl_free` ile serbest bırakmayı unutmayın!

Kullanıcı `CURLU_URLDECODE` bayrağıyla istemedikçe, çıkarılan parçalar URL kod çözme işlemine tabi tutulmaz.

## URL parçaları

Farklı parçalar URL'deki rollerine göre adlandırılır. Şöyle görünen bir URL hayal edin:

    http://joe:7Hbz@example.com:8080/images?id=5445#footer

Bu URL curl tarafından ayrıştırıldığında, farklı bileşenleri şöyle saklar:

| metin         | parça                |
|---------------|----------------------|
| `http`        | `CURLUPART_SCHEME`   |
| `joe`         | `CURLUPART_USER`     |
| `7Hbz`        | `CURLUPART_PASSWORD` |
| `example.com` | `CURLUPART_HOST`     |
| `8080`        | `CURLUPART_PORT `    |
| `/images`     | `CURLUPART_PATH`     |
| `id=5445`     | `CURLUPART_QUERY`    |
| `footer`      | `CURLUPART_FRAGMENT` |

## Zone ID (Bölge Kimliği)

Biraz dışarı çıkabilecek tek şey Zone id'dir. IPv6 sayısal adresleri için kullanılabilen ve yalnızca bu tür adresler için kullanılabilen ek bir niteleyicidir. Şöyle kullanılır, burada `eth0` olarak ayarlanmıştır:

    http://[2a04:4e42:e00::347%25eth0]/

Bu URL için curl şunları çıkarır:

| metin                | parça              |
|----------------------|--------------------|
| `http`               | `CURLUPART_SCHEME` |
| `2a04:4e42:e00::347` | `CURLUPART_HOST`   |
| `eth0`               | `CURLUPART_ZONEID` |
| `/`                  | `CURLUPART_PATH`   |

Başka herhangi bir bileşeni istemek, eksik oldukları için sıfır olmayan bir değer döndürür.
