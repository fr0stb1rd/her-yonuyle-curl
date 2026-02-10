# Dize (string) seçeneklerini ayarla

Şu anda `curl_easy_setopt()` için üçüncü argümanı olarak bir dize kabul eden 80'den fazla seçenek vardır.

Bir handle'da bir dize ayarlandığında, libcurl verileri hemen kopyalar, böylece uygulamanın transfer yapılırken verileri etrafta tutması gerekmez - **bir önemli istisna dışında**: `CURLOPT_POSTFIELDS`.

Handle'da bir URL ayarla:

    curl_easy_setopt(handle, CURLOPT_URL, "https://example.com");

## `CURLOPT_POSTFIELDS`

libcurl'ün her zaman verileri kopyaladığı kuralının istisnası olan `CURLOPT_POSTFIELDS`, yalnızca verilere işaretçiyi saklar, yani bu seçeneği kullanan bir uygulama, ilişkili transferin tüm süresi boyunca belleği etrafta **tutmalıdır**.

Bu sorunluysa, bir alternatif bunun yerine verileri kopyalayan `CURLOPT_COPYPOSTFIELDS` kullanmaktır. Veriler ikiliyse ve bir null baytının ilk varlığında durmuyorsa, `CURLOPT_POSTFIELDSIZE`'ın bu seçenek kullanılmadan *önce* ayarlandığından emin olun.

### Neden?

`CURLOPT_POSTFIELDS`'ın bir istisna olmasının nedeni mirastan kaynaklanmaktadır. Başlangıçta (curl 7.17.0'dan önce), libcurl *hiçbir* dize argümanını kopyalamıyordu ve bu mevcut davranış tanıtıldığında, bu seçenek davranışı bozmadan dönüştürülemedi, bu yüzden eskisi gibi çalışmaya devam etmek zorundaydı. Şimdi bu göze batıyor, çünkü başka hiçbir seçenek bunu yapmıyor...

## C++

libcurl'ü bir C++ programından kullanırsanız, libcurl'ün bir dize beklediği yere bir dize nesnesi iletemeyeceğinizi hatırlamak önemlidir. Null ile sonlandırılmış bir C dizesi olmalıdır. Genellikle bunu `c_str()` yöntemiyle gerçekleştirebilirsiniz.

Örneğin, URL'yi bir dize nesnesinde tutun ve handle'da ayarlayın:

    std::string url("https://example.com/");
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
