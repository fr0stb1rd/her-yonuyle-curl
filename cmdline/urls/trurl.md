# trurl

*trurl*, URL'leri ve URL parçalarını ayrıştırma, işleme ve çıktı olarak verme tek amacına sahip ayrı bir komut satırı aracıdır. Komut satırlarınız ve betik ihtiyaçlarınız için curl'e yardımcı bir araçtır.

trurl, libcurl'ün URL ayrıştırıcısını kullanır. Bu, curl ve trurl'ün URL'ler hakkında her zaman aynı fikre sahip olmasını ve her iki aracın da bunları aynı ve tutarlı bir şekilde ayrıştırmasını sağlar.

## Kullanım

Genellikle trurl'e bir veya daha fazla URL iletirsiniz ve hangi bileşenlerin çıktısını istediğinizi belirtirsiniz. Muhtemelen URL(ler)i değiştirirken de.

trurl URL'leri bilir ve her URL on adede kadar ayrı ve bağımsız *bileşenden* oluşur. Bu bileşenler trurl ile çıkarılabilir, kaldırılabilir ve güncellenebilir.

## trurl örnek komut satırları

**Bir URL'nin ana bilgisayar adını değiştirin:**

    $ trurl --url https://curl.se --set host=example.com
    https://example.com/

**Bileşenleri ayarlayarak bir URL oluşturun:**

    $ trurl --set host=example.com --set scheme=ftp
    ftp://example.com/

**Bir URL'yi yeniden yönlendirin:**

    $ trurl --url https://curl.se/we/are.html --redirect here.html
    https://curl.se/we/here.html

**Port numarasını değiştirin:**

    $ trurl --url https://curl.se/we/../are.html --set port=8080
    https://curl.se:8080/are.html

**URL'den yolu (path) çıkarın:**

    $ trurl --url https://curl.se/we/are.html --get '{path}'
    /we/are.html

**URL'den portu çıkarın:**

    $ trurl --url https://curl.se/we/are.html --get '{port}'
    443

**Bir URL'ye yol segmenti ekleyin:**

    $ trurl --url https://curl.se/hello --append path=you
    https://curl.se/hello/you

**Bir URL'ye sorgu segmenti ekleyin:**

    $ trurl --url "https://curl.se?name=hello" --append query=search=string
    https://curl.se/?name=hello&search=string

**stdin'den URL'leri okuyun:**

    $ cat urllist.txt | trurl --url-file -
    ...

**JSON çıktısı:**

    $ trurl "https://fake.host/hello#frag" --set user=::moo:: --json
    [
      {
        "url": "https://%3a%3amoo%3a%3a@fake.host/hello#frag",
        "parts": {
          "scheme": "https",
          "user": "::moo::",
          "host": "fake.host",
          "path": "/hello",
          "fragment": "frag"
        }
      }
    ]

**Sorgudan izleme demetlerini (tuples) kaldırın:**

    $ trurl "https://curl.se?search=hey&utm_source=tracker" \
      --trim query="utm_*"
    https://curl.se/?search=hey

**Belirli bir sorgu anahtarı değerini gösterin:**

    $ trurl "https://example.com?a=home&here=now&thisthen" -g '{query:a}'
    home

**Sorgu bileşenindeki anahtar/değer çiftlerini sıralayın:**

    $ trurl "https://example.com?b=a&c=b&a=c" --sort-query
    https://example.com?a=c&b=a&c=b

**Noktalı virgül ayırıcı kullanan bir sorguyla çalışın:**

    $ trurl "https://curl.se?search=fool;page=5" --trim query="search" \
      --query-separator ";"
    https://curl.se?page=5

**URL yolundaki boşlukları kabul edin:**

    $ trurl "https://curl.se/this has space/index.html" --accept-space
    https://curl.se/this%20has%20space/index.html

## Daha fazlası

trurl hakkında bilmek istediğiniz her şey <https://curl.se/trurl> adresinde bulunur. Muhtemelen tercih ettiğiniz Linux dağıtımı için zaten mevcuttur.
