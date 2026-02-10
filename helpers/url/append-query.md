# Sorguya ekle (Append to the query)

Bir uygulama, `CURLU_APPENDQUERY` bayrağıyla mevcut sorgu parçasının sağ ucuna bir dize ekleyebilir.

`https://example.com/?shoes=2` URL'sini tutan bir handle düşünün. Bir uygulama daha sonra `hat=1` dizesini sorgu parçasına şöyle ekleyebilir:

    rc = curl_url_set(urlp, CURLUPART_QUERY, "hat=1", CURLU_APPENDQUERY);

Hatta bir ampersand (`&`) ayırıcısının eksikliğini fark eder ve bir tane de o enjekte eder ve handle'ın tam URL'si o zaman `https://example.com/?shoes=2&hat=1` olur.

Eklenen dize elbette eklenirken URL olarak kodlanabilir ve istenirse kodlama `=` karakterini atlar. Örneğin, `candy=M&M` dizesini zaten sahip olduğumuz şeye ekleyin ve verideki ampersand ile başa çıkmak için URL olarak kodlayın:

    rc = curl_url_set(urlp, CURLUPART_QUERY, "candy=M&M",
                      CURLU_APPENDQUERY | CURLU_URLENCODE);

Şimdi URL `https://example.com/?shoes=2&hat=1&candy=M%26M` gibi görünür.
