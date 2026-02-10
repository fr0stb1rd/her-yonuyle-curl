# JSON

curl 7.82.0, HTTP sunucularına POST kullanarak JSON biçimli veriler göndermenin yeni bir yolu olarak `--json` seçeneğini tanıttı. Bu seçenek bir kısayol olarak çalışır ve şu üçünün yerini alan tek bir seçenek sunar:

    --data-binary [arg]
    --header "Content-Type: application/json"
    --header "Accept: application/json"

Bu seçenek curl'ün gönderdiği JSON verilerini gerçekten anlamasını veya bilmesini sağlamaz, ancak göndermeyi kolaylaştırır. curl gönderdiği verilere dokunmaz veya ayrıştırmaz, bu nedenle geçerli JSON olduğundan kendiniz emin olmanız gerekir.

Bir sunucuya temel bir JSON nesnesi gönderin:

    curl --json '{"tool": "curl"}' https://example.com/

Yerel bir dosyadan JSON gönderin:

    curl --json @json.txt https://example.com/

stdin üzerinden curl'e iletilen JSON gönderin:

    echo '{"a":"b"}' | curl --json @- https://example.com/

Aynı komut satırında birden fazla `--json` seçeneği kullanabilirsiniz. Bu, curl'ün seçeneklerden gelen içerikleri birleştirmesini ve tüm verileri tek seferde sunucuya göndermesini sağlar. Birleştirmenin düz metin tabanlı olduğunu ve JSON nesnelerini JSON'a göre birleştirmediğini unutmayın.

Bir dosyadan JSON gönderin ve sonuna bir dize birleştirin:

    curl --json @json.txt --json ', "end": "true"}' https://example.com/

## Gönderilecek JSON oluşturma

JSON verilerinde kullanılan tırnak işaretleri bazen kabuklarda ve betiklerde yazmayı ve kullanmayı biraz zor ve hantal hale getirir.

Bu amaçla ayrı bir araç kullanmak işleri sizin için kolaylaştırabilir ve özellikle bunu başarmanıza yardımcı olabilecek bir araç [jo](https://github.com/jpmens/jo)'dur.

jo ve `--json` ile bir sunucuya temel bir JSON nesnesi gönderin

    jo name=jo n=17 parser=false | curl --json @- https://example.com/

## JSON alma

curl'ün kendisi, sunucu yanıtında JSON döndürdüğünde de dahil olmak üzere, gönderdiği veya aldığı içerikleri bilmez veya anlamaz.

JSON yanıtlarını ayrıştırmak veya güzel yazdırmak (pretty-print) amacıyla ayrı bir araç kullanmak işleri sizin için kolaylaştırabilir ve özellikle bunu başarmanıza yardımcı olabilecek bir araç [jq](https://stedolan.github.io/jq/)'dur.

Bir sunucuya temel bir JSON nesnesi gönderin ve JSON yanıtını güzel yazdırın:

    curl --json '{"tool": "curl"}' https://example.com/ | jq

JSON'u `jo` ile gönderin, yanıtı `jq` ile yazdırın:

    jo name=jo n=17 | curl --json @- https://example.com/ | jq

jq, JSON içeriğini çıkarmak, filtrelemek ve yönetmek için sadece güzel yazdırmanın çok ötesine geçen güçlü ve yetenekli bir araçtır.
