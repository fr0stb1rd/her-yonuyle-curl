# Yanıtlar (Responses)

Her HTTP isteği bir HTTP yanıtı içerir. Bir HTTP yanıtı, bir dizi meta veri ve bazen sıfır bayt olabilen ve dolayısıyla mevcut olmayan bir yanıt gövdesidir. Ancak bir HTTP yanıtı her zaman yanıt başlıklarına sahiptir.

## Yanıt gövdesi

Yanıt gövdesi [yazma geri çağırımına](../transfers/callbacks/write.md) ve yanıt başlıkları [başlık geri çağırımına](../transfers/callbacks/header.md) iletilir.

Hemen hemen tüm libcurl kullanan uygulamaların, alınan başlıklar ve verilerle ne yapacağını libcurl'e bildiren bu geri çağırımlardan en az birini ayarlaması gerekir.

## Yanıt meta verileri

libcurl, bir uygulamanın önceden gerçekleştirilen transferden bilgi almak için libcurl'ü sorgulamasına izin veren `curl_easy_getinfo()` işlevini sunar.

Bazen bir uygulama sadece verinin boyutunu bilmek ister. Bir yanıtın *sunucu başlıkları tarafından belirtilen* boyutu `curl_easy_getinfo()` ile şöyle çıkarılabilir:

    curl_off_t size;
    curl_easy_getinfo(curl, CURLINFO_CONTENT_LENGTH_DOWNLOAD_T, &size);

Transfer zaten tamamlanana kadar bekleyebilirseniz (tüm URL'ler boyutu önceden sağlamadığından bu da daha güvenilir bir yoldur, örneğin talep üzerine içerik üreten sunucular için), bunun yerine en son transferde indirilen veri miktarını isteyebilirsiniz.

    curl_off_t size;
    curl_easy_getinfo(curl, CURLINFO_SIZE_DOWNLOAD_T, &size);

## HTTP yanıt kodu

Her HTTP yanıtı, HTTP yanıt kodunu içeren tek bir satırla başlar. Bu, sunucunun istek için durum fikrini içeren üç basamaklı bir sayıdır. Sayılar HTTP standart özelliklerinde ayrıntılandırılmıştır ancak şöyle çalışan aralıklara ayrılmıştır:

| Kod | Anlamı                                |
|------|---------------------------------------|
|1xx   | Geçici kod, yeni bir tane takip ediyor|
|2xx   | İşler YOLUNDA (OK)                    |
|3xx   | İçerik başka bir yerde                |
|4xx   | İstemci sorunu nedeniyle başarısız    |
|5xx   | Sunucu sorunu nedeniyle başarısız     |

Bir transferden sonra yanıt kodunu şöyle çıkarabilirsiniz:

    long code;
    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &code);

## HTTP yanıt kodu "hataları" hakkında

Yanıt kodu numaraları (4xx ve 5xx aralıklarında), sunucunun isteği işlerken bir hata olduğunu belirtmek için kullandığı numaralar içerebilse de, bunun libcurl'ün bir hata döndürmesine neden olmadığını anlamak önemlidir.

libcurl'den bir HTTP transferi gerçekleştirmesi istendiğinde, o HTTP transferi başarısız olursa bir hata döndürür. Ancak, bir HTTP 404 veya benzeri bir şey geri almak libcurl için bir sorun değildir. Bu bir HTTP transfer hatası değildir. Bir kullanıcı, bir sunucunun HTTP yanıtlarını test etmek için bir istemci yazıyor olabilir.

curl'ün 400 ve üzeri HTTP yanıt kodlarını hata olarak ele almasında ısrar ederseniz, libcurl `CURLOPT_FAILONERROR` seçeneğini sunar; bu ayarlanırsa curl'e bu durumda `CURLE_HTTP_RETURNED_ERROR` döndürmesini söyler. O zaman mümkün olan en kısa sürede hata döndürür ve yanıt gövdesini teslim etmez.
