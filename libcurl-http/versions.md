# Sürümler (Versions)

Tüm İnternet protokolleri gibi, HTTP protokolü de yıllar içinde gelişmeye devam etti ve artık dünya genelinde ve zaman içinde dağıtılmış, farklı başarı seviyelerinde farklı sürümler konuşan istemciler ve sunucular var. libcurl'ün ilettiğiniz URL'lerle çalışmasını sağlamak için libcurl, hangi HTTP sürümünü kullanacağınızı belirtmeniz için yollar sunar. libcurl, isterseniz en mantıklı varsayılan değerleri, en yaygın olanları kullanmaya çalışacak şekilde tasarlanmıştır ancak bazen bu yeterli değildir ve o zaman libcurl'e ne yapacağını söylemeniz gerekebilir.

Yerleşik HTTP/2 yeteneklerine sahip bir libcurl derlemesi kullanıyorsanız, libcurl HTTPS sunucuları için varsayılan olarak HTTP/2 kullanır. libcurl daha sonra otomatik olarak HTTP/2 kullanmayı dener veya pazarlık başarısız olursa 1.1'e geri döner. HTTP/2 yetenekli olmayan libcurl'ler varsayılan olarak HTTPS üzerinden HTTP/1.1 kullanır. Düz HTTP istekleri varsayılan olarak HTTP/1.1'dir.

Varsayılan davranış transferiniz için yeterince iyi değilse, `CURLOPT_HTTP_VERSION` seçeneği sizin içindir.

| Seçenek                             | Açıklama |
|-------------------------------------|-------------|
| CURL_HTTP_VERSION_NONE              | Varsayılan davranışa geri dön
| CURL_HTTP_VERSION_1_0               | Eski HTTP/1.0 protokol sürümünün kullanımını zorla
| CURL_HTTP_VERSION_1_1               | İsteği HTTP/1.1 protokol sürümünü kullanarak yap
| CURL_HTTP_VERSION_2_0               | HTTP/2 kullanmayı dene
| CURL_HTTP_VERSION_2TLS              | Yalnızca HTTPS bağlantılarında HTTP/2 kullanmayı dene, aksi takdirde HTTP/1.1 yap
| CURL_HTTP_VERSION_2_PRIOR_KNOWLEDGE | 1.1'den "yükseltme" yapmadan doğrudan HTTP/2 kullan. Bu sunucunun bununla uyumlu olduğunu bilmenizi gerektirir.
| CURL_HTTP_VERSION_3 | HTTP/3 dene, eski sürüme geri dönüşe izin ver.
| CURL_HTTP_VERSION_3ONLY | HTTP/3 kullan veya mümkün değilse başarısız ol

## Sürüm 2 zorunlu değildir

libcurl'den HTTP/2 kullanmasını istediğinizde, bu bir istektir, bir gereklilik değildir. libcurl daha sonra sunucunun HTTP/1.1 veya HTTP/2 kullanmayı seçmesine izin verir ve sonuçta hangi protokolün kullanılacağına karar veren budur.

## Sürüm 3 zorunlu olabilir

libcurl'den `CURL_HTTP_VERSION_3` seçeneğiyle HTTP/3 kullanmasını istediğinizde, libcurl'ün paralel olarak ancak biraz gecikmeli ikinci bir bağlantı girişimi yapmasını sağlar, böylece HTTP/3 bağlantısı başarısız olursa, yine de eski bir HTTP sürümünü kullanmayı deneyebilir.

`CURL_HTTP_VERSION_3ONLY` kullanmak, geri dönüş mekanizmasının kullanılmadığı ve başarısız bir QUIC bağlantısının transferi tamamen başarısız kıldığı anlamına gelir.
