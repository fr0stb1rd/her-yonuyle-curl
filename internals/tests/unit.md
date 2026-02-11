# Birim testleri (Unit tests)

**Birim testleri yalnızca [hata ayıklama derlemelerinde](debug.md) çalışır.**

Birim testleri, libcurl dahili olan ve bu nedenle herhangi bir genel API, başlık veya harici belgeden parçası olmayan işlevleri kullanan testlerdir.

Test etmek istediğiniz dahili işlev `static` yapılmışsa, bunun yerine `UNITTEST` olarak ayarlanmalıdır - bu daha sonra hata ayıklama derlemelerinin bunlar için static kullanmamasını sağlar ve böylece birim testlerinden test edilmek üzere erişilebilir hale gelirler.

Birim testleri için bunları hızlı ve kolay yazmayı sağlamak üzere bir dizi kolaylık işlevi ve makrosu sağlıyoruz.

Tüm birim test programları `tests/unit` içinde tutulur
