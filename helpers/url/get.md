# Bir URL al (Get a URL)

`CURLU *` handle tek bir URL'yi temsil eder ve `curl_url_get` ile o tam URL'yi veya bireysel parçalarını kolayca çıkarabilirsiniz:

    char *url;
    rc = curl_url_get(h, CURLUPART_URL, &url, CURLU_NO_DEFAULT_PORT);
    curl_free(url);

Handle, istenen parçayı döndürmek için yeterli bilgiye sahip değilse hata döndürür.

Döndürülen bir dize, işiniz bittiğinde `curl_free()` ile serbest bırakılmalıdır.

# Bayraklar (Flags)

`curl_url_get()` kullanarak bir URL parçasını alırken, API içeriğin tam olarak nasıl döndürülmesi gerektiğini daha iyi belirtmek için birkaç farklı geçiş sunar. Bunlar, işlevin dördüncü argümanı olan `flags` bit maskesi parametresinde ayarlanır. Sıfır, bir veya daha fazla bit ayarlayabilirsiniz.

## `CURLU_DEFAULT_PORT`

URL handle'ında saklanan bir port numarası yoksa, bu seçenek `curl_url_get()` işlevinin kullanılan şema için varsayılan portu döndürmesini sağlar.

## `CURLU_DEFAULT_SCHEME`

Handle'da saklanan bir şema yoksa, bu seçenek `curl_url_get()` işlevinin hata yerine varsayılan şemayı döndürmesini sağlar.

## `CURLU_NO_DEFAULT_PORT`

`curl_url_get()` işlevine, port numarası şema için kullanılan varsayılan portla eşleşirse oluşturulan URL'de bir port numarası *kullanmamasını* talimat verir. Örneğin, 443 numaralı port ayarlanmışsa ve şema `https` ise, çıkarılan URL port numarasını içermez.

## `CURLU_URLENCODE`

Bu bayrak, tam bir URL alındığında `curl_url_get()` işlevinin ana bilgisayar adı parçasını URL olarak kodlamasını sağlar. Ayarlanmazsa (varsayılan), libcurl IDN adlarının olduğu gibi görünmesini desteklemek için URL'yi ana bilgisayar adı "ham" olarak döndürür. IDN ana bilgisayar adları tipik olarak aksi takdirde yüzde kodlu olan ASCII dışı baytlar kullanır.

URL kodlaması istenmediğinde bile, `%` (bayt 37) karakterinin, ana bilgisayar adının geçerli kaldığından emin olmak için ana bilgisayar adlarında URL olarak kodlandığını unutmayın.

## `CURLU_URLDECODE`

`curl_url_get()` işlevine içeriği döndürmeden önce URL kodunu çözmesini söyler. Şemayı, port numarasını veya tam URL'yi çözmeye çalışır. Sorgu bileşeni de bu bit ayarlandığında bonus olarak artı-boşluk dönüşümü alır. Bu URL kod çözme işleminin karakter seti duyarsız olduğunu ve belirli bir kodlama için amaçlanabilecek verilerle sıfır ile sonlandırılmış bir dize geri aldığınızı unutmayın. Çözülen dizede 32'den düşük herhangi bir bayt değeri varsa, alma işlemi bunun yerine hata döndürür.

## `CURLU_PUNYCODE`

Ayarlanırsa ve `CURLU_URLENCODE` ayarlanmazsa ve `CURLUPART_HOST` veya `CURLUPART_URL` parçalarının alınması istenirse, libcurl herhangi bir ASCII dışı sekizli içeriyorsa (ve bir IDN adıysa) ana bilgisayar adını punycode sürümünde döndürür. libcurl IDN yetenekleri olmadan oluşturulmuşsa, bu bitin kullanılması, ana bilgisayar adı ASCII aralığı dışında herhangi bir şey içeriyorsa `curl_url_get()` işlevinin `CURLUE_LACKS_IDN` döndürmesine neden olur.
