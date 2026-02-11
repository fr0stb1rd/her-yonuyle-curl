# Yükleme (Upload)

HTTP üzerinden yüklemeler birçok farklı şekilde yapılabilir ve farkları fark etmek önemlidir. POST veya PUT gibi farklı yöntemler kullanabilirler ve POST kullanırken gövde biçimlendirmesi farklılık gösterebilir.

Bu HTTP farklılıklarına ek olarak, libcurl yüklenecek verileri sağlamak için farklı yollar sunar.

## HTTP POST

POST genellikle verileri uzak bir web uygulamasına iletmek için kullanılan HTTP yöntemidir. Tarayıcılarda bunu yapmanın yaygın bir yolu, bir HTML formu doldurup gönder'e basmaktır. Bir HTTP isteğinin verileri sunucuya iletmesinin standart yoludur. libcurl ile normalde bu verileri bir işaretçi ve bir uzunluk olarak sağlarsınız:

    curl_easy_setopt(easy, CURLOPT_POSTFIELDS, dataptr);
    curl_easy_setopt(easy, CURLOPT_POSTFIELDSIZE, (long)datalength);

Veya libcurl'e bunun bir post olduğunu ancak libcurl'ün verileri bunun yerine normal [okuma geri çağırımını (read callback)](../transfers/callbacks/read.md) kullanarak almasını tercih ettiğinizi söylersiniz:

    curl_easy_setopt(easy, CURLOPT_POST, 1L);
    curl_easy_setopt(easy, CURLOPT_READFUNCTION, read_callback);

Bu "normal" POST ayrıca istek başlığını `Content-Type: application/x-www-form-urlencoded` olarak ayarlar.

## HTTP çok parçalı form gönderileri (multipart formposts)

Çok parçalı bir form gönderisi hala aynı HTTP yöntemi POST'u kullanır; fark yalnızca istek gövdesinin biçimlendirmesindedir. Çok parçalı bir form gönderisi, MIME tarzı sınır dizeleriyle ayrılmış bir dizi ayrı "parçadan" oluşur. Ne kadar parça gönderebileceğiniz konusunda bir sınır yoktur.

Böyle her parçanın bir adı, bir başlık seti ve birkaç başka özelliği vardır.

libcurl, böyle bir parça serisi oluşturmak ve bunu sunucuya göndermek için hepsi `curl_mime` ile ön eklenmiş bir dizi kolaylık işlevi sunar. Çok parçalı bir post oluşturun ve verideki her parça için adı, veriyi ve belki ek meta verileri ayarlayın. Temel bir kurulum şöyle görünebilir:

    /* Formu oluştur */
    form = curl_mime_init(curl);

    /* Dosya yükleme alanını doldur */
    field = curl_mime_addpart(form);
    curl_mime_name(field, "sendfile");
    curl_mime_filedata(field, "photo.jpg");

Sonra o postu libcurl'e şöyle iletirsiniz:

    curl_easy_setopt(easy, CURLOPT_MIMEPOST, form);

(`curl_formadd`, çok parçalı form gönderileri oluşturmak için eski API'dir ancak artık onu kullanmanızı önermiyoruz)

## HTTP PUT

libcurl ile bir PUT, verileri okuma geri çağırımını kullanarak ilettiğinizi varsayar, çünkü libcurl'ün kullandığı ve sağladığı tipik "dosya yükleme" deseni budur. Geri çağırımı ayarlarsınız, PUT istersiniz (`CURLOPT_UPLOAD` isteyerek), yüklemenin boyutunu ayarlarsınız ve URL'yi hedefe ayarlarsınız:

    curl_easy_setopt(easy, CURLOPT_UPLOAD, 1L);
    curl_easy_setopt(easy, CURLOPT_INFILESIZE_LARGE, (curl_off_t) size);
    curl_easy_setopt(easy, CURLOPT_READFUNCTION, read_callback);
    curl_easy_setopt(easy, CURLOPT_URL, "https://example.com/handle/put");

Transfer başlamadan önce yüklemenin boyutunu bir nedenden dolayı bilmiyorsanız ve HTTP 1.1 kullanıyorsanız, [CURLOPT_HTTPHEADER](requests.md) ile bir `Transfer-Encoding: chunked` başlığı ekleyebilirsiniz. HTTP 1.0 için boyutu önceden sağlamanız gerekir ve HTTP 2 ve sonrası için ne boyuta ne de ekstra başlığa gerek yoktur.

## Expect: başlıkları

HTTP 1.1 kullanarak HTTP yüklemeleri yaparken, libcurl bazı durumlarda bir `Expect: 100-continue` başlığı ekler. Bu başlık, sunucuya transferi erken reddetme ve istemcinin sunucu reddetme şansı bulmadan önce boşuna çok fazla veri göndermek zorunda kalmasını önleme yolu sunar.

Başlık, HTTP yüklemesi `CURLOPT_UPLOAD` ile yapılırsa veya gövde boyutu bilinmeyen veya 1024 bayttan büyük olduğu bilinen bir HTTP POST yapması istenirse libcurl tarafından eklenir.

libcurl kullanan bir istemci, [CURLOPT_HTTPHEADER](requests.md) seçeneğiyle `Expect:` başlığının kullanımını açıkça devre dışı bırakabilir.

Bu başlık HTTP/2 veya HTTP/3 ile kullanılmaz.

## Yüklemeler aynı zamanda indirmelerdir

HTTP, verileri ona yüklediğinizde bile içeriğin geri yanıtlanabildiği bir protokoldür - karar vermek sunucuya kalmıştır. Yanıt verileri, yükleme tamamlanmadan önce bile istemciye geri gönderilmeye başlayabilir.
