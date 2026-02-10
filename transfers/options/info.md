# Seçenek bilgisini al

libcurl, uygulamaların o anda desteklenen tüm *easy seçenekleri* hakkında bilgi almasına izin veren bir API, aslında bir dizi işlev sunar. Seçenekler için *değerleri* döndürmez, bunun yerine seçeneğin adı, kimliği ve türü hakkında bilgi verir.

## Tüm seçenekler üzerinde yinele

Modern libcurl 300'den fazla farklı seçeneği destekler. `curl_easy_option_by_next()` kullanımıyla, bir uygulama bilinen tüm seçenekler üzerinde yineleme yapabilir ve bunlar için bir `struct curl_easyoption`'a işaretçi döndürebilir.

Bu işlev yalnızca bu tam libcurl derlemesinin bildiği seçenekler hakkında bilgi döndürür. Diğer seçenekler daha yeni libcurl derlemelerinde veya derleme zamanında seçenekleri farklı şekilde etkinleştiren/devre dışı bırakan derlemelerde mevcut olabilir.

Örnek, mevcut tüm seçenekler üzerinde yinele:

    const struct curl_easyoption *opt;
    opt = curl_easy_option_by_next(NULL);
    while(opt) {
      printf("Name: %s\n", opt->name);
      opt = curl_easy_option_by_next(opt);
    }

## Ada göre belirli bir seçeneği bul

Belirli bir easy seçenek adı verildiğinde, libcurl'den bunun için bir `struct curl_easyoption`'a işaretçi döndürmesini isteyebilirsiniz. Ad, `CURLOPT_` öneki olmadan sağlanmalıdır.

Örnek olarak, bir uygulama libcurl'e `CURLOPT_VERBOSE` seçeneğini şöyle sorabilir:

    const struct curl_easyoption *opt = curl_easy_option_by_name("VERBOSE");
    if(opt) {
      printf("This option wants CURLoption %x\n", (int)opt->id);
    }

## Kimliğe göre belirli bir seçeneği bul

Belirli bir easy seçenek kimliği verildiğinde, libcurl'den bunun için bir `struct curl_easyoption`'a işaretçi döndürmesini isteyebilirsiniz. "ID" (Kimlik), genel `curl/curl.h` başlık dosyasında sağlandığı şekliyle `CURLOPT_` önekli semboldür.

Bir uygulama libcurl'den `CURLOPT_VERBOSE` seçeneğinin adını şöyle isteyebilir:

    const struct curl_easyoption *opt =
      curl_easy_option_by_id(CURLOPT_VERBOSE);
    if(opt) {
      printf("This option has the name: %s\n", opt->name);
    }

## `curl_easyoption` yapısı

    struct curl_easyoption {
      const char *name;
      CURLoption id;
      curl_easytype type;
      unsigned int flags;
    };

'flags' içinde tanımlanmış bir anlama sahip tek bir bit vardır: `CURLOT_FLAG_ALIAS` ayarlanmışsa, bu seçeneğin bir "takma ad" olduğu anlamına gelir. Geriye dönük uyumluluk için sağlanan ve günümüzde daha çok başka bir ada sahip bir seçenek tarafından sunulan bir ad. Bir takma ad için kimliğe bakarsanız, o seçenek için yeni kanonik adı alırsınız.
