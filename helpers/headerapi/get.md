# Bir başlık al (Get a header)

    CURLHcode curl_easy_header(CURL *easy,
                               const char *name,
                               size_t index,
                               unsigned int origin,
                               int request,
                               struct curl_header **hout);

Bu işlev, belirli bir **ada** (name) sahip bir alan hakkında bilgi döndürür ve işlevden bunu bir veya daha fazla **kökende** (origins) aramasını istersiniz.

**index** argümanı, birden fazla mevcut olduğunda bir başlığın n'inci oluşumunu sormak istediğiniz zamandır. **index**'i 0 olarak ayarlamak ilk örneği döndürür - çoğu durumda tek olan budur.

**request** argümanı libcurl'e hangi istekten başlıkları istediğinizi söyler.

Bir uygulamanın son argümanda bir `struct curl_header *` işaretçisine bir işaretçi iletmesi gerekir, çünkü bir hata döndürülmediğinde oraya bir işaretçi döndürülür. Başarılı bir çağrının **out** sonucuyla ilgili ayrıntılar için [Başlık yapısı](struct.md) bölümüne bakın.

Verilen ad, verilen kökende alınan herhangi bir başlıkla eşleşmezse, işlev `CURLHE_MISSING` döndürür veya henüz *hiçbir* başlık alınmadıysa `CURLHE_NOHEADERS` döndürür.
