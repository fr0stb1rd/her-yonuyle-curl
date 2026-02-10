# İndirme (Download)

GET yöntemi, bir HTTP URL'si istendiğinde ve belirli başka bir yöntem istenmediğinde libcurl'ün kullandığı varsayılan yöntemdir. Sunucudan belirli bir kaynağı ister—standart HTTP indirme isteği:

    easy = curl_easy_init();
    curl_easy_setopt(easy, CURLOPT_URL, "http://example.com/");
    curl_easy_perform(easy);

Easy handle'da ayarlanan seçenekler yapışkan olduğundan ve değiştirilinceye kadar kaldığından, GET dışında başka bir istek yöntemi istediğiniz ve ardından sonraki bir istek için tekrar GET'e geri dönmek istediğiniz zamanlar olabilir. Bu amaçla `CURLOPT_HTTPGET` seçeneği vardır:

    curl_easy_setopt(easy, CURLOPT_HTTPGET, 1L);

## Başlıkları da indir

Bir HTTP transferi ayrıca bir set yanıt başlığı içerir. Yanıt başlıkları, yanıt gövdesi adı verilen asıl yük ile ilişkili meta verilerdir. Tüm indirmeler de bir set başlık alır, ancak libcurl kullanırken bunların indirilmesini (görülmesini) isteyip istemediğinizi seçebilirsiniz.

libcurl'den başlıkları normal gövdenin olduğu aynı akışa iletmesini `CURLOPT_HEADER` kullanarak isteyebilirsiniz:

    easy = curl_easy_init();
    curl_easy_setopt(easy, CURLOPT_HEADER, 1L);
    curl_easy_setopt(easy, CURLOPT_URL, "http://example.com/");
    curl_easy_perform(easy);

Veya [yazma](../transfers/callbacks/write.md) ve [başlık geri çağırımlarının](../transfers/callbacks/header.md) varsayılan davranışlarına güvenerek başlıkları ayrı bir indirme dosyasında saklamayı seçebilirsiniz:

    easy = curl_easy_init();
    FILE *file = fopen("headers", "wb");
    curl_easy_setopt(easy, CURLOPT_HEADERDATA, file);
    curl_easy_setopt(easy, CURLOPT_URL, "http://example.com/");
    curl_easy_perform(easy);
    fclose(file);

Başlıklara sadece şöyle bir göz atmak istiyorsanız, geliştirme sırasında sadece ayrıntılı (verbose) modu ayarlayarak stderr'e gönderilen hem giden hem de gelen başlıkları gösterdiği için yeterince memnun olabilirsiniz:

    curl_easy_setopt(easy, CURLOPT_VERBOSE, 1L);
