# Veri okuma (Read data)

Okuma geri çağırımı `CURLOPT_READFUNCTION` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_READFUNCTION, read_callback);

`read_callback` işlevi şu prototiple eşleşmelidir:

    size_t read_callback(char *buffer, size_t size, size_t nitems,
                         void *stream);

Bu geri çağırım işlevi, libcurl sunucuya veri göndermek istediğinde çağrılır. Bu, veri yüklemek veya başka bir şekilde sunucuya göndermek için ayarladığınız bir transferdir. Bu geri çağırım, tüm veriler teslim edilene veya transfer başarısız olana kadar tekrar tekrar çağrılır.

**stream** işaretçisi, `CURLOPT_READDATA` ile ayarlanan özel verilere işaret eder:

    curl_easy_setopt(handle, CURLOPT_READDATA, custom_pointer);

Bu geri çağırım ayarlanmazsa, libcurl varsayılan olarak 'fread' kullanır.

**buffer** işaretçisi tarafından işaret edilen veri alanı, işleviniz tarafından en fazla **nitems** sayısı ile çarpılan **size** kadar bayt ile doldurulmalıdır. Geri çağırım daha sonra o bellek alanında sakladığı bayt sayısını veya verilerin sonuna ulaştıysak 0 döndürmelidir. Geri çağırım ayrıca libcurl'ün hemen başarısız olmasına veya belirli transferi duraklatmasına neden olmak için birkaç "sihirli" dönüş kodu da döndürebilir. Ayrıntılar için [CURLOPT_READFUNCTION man sayfasına](https://curl.se/libcurl/c/CURLOPT_READFUNCTION.html) bakın.
