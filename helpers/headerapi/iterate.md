# Başlıklar üzerinde yineleme (Iterate over headers)

    struct curl_header *curl_easy_nextheader(CURL *easy,
                                             unsigned int origin,
                                             int request,
                                             struct curl_header *previous);

Bu işlev uygulamanın, **request** içinde gelen verilen **origins** içindeki mevcut tüm başlıklar üzerinde yineleme yapmasını sağlar.

**request** argümanı libcurl'e hangi istekten başlıkları istediğinizi söyler.

**previous** NULL olarak ayarlanırsa, bu işlev ilk başlığa bir işaretçi döndürür. Uygulama daha sonra bu işaretçiyi, aynı **origin** ve **request** bağlamındaki mevcut tüm başlıklar üzerinde yineleme yapmak için bir sonraki çağrıya bir argüman olarak kullanabilir.

Bu işlev NULL döndürdüğünde, bağlam içinde daha fazla başlık yoktur.

Bu işlevin işaretçi döndürdüğü `curl_header` yapısıyla ilgili ayrıntılar için [Başlık yapısı](struct.md) bölümüne bakın.
