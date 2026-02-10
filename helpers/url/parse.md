# Bir URL'yi ayrıştır (Parse a URL)

Handle'da `CURLUPART_URL` parçasını *ayarlayarak* tam bir URL'yi ayrıştırırsınız:

    CURLU *h = curl_url();
    rc = curl_url_set(h, CURLUPART_URL,
                      "https://example.com:449/foo/bar?name=moo", 0);

Başarılıysa, `rc`, `CURLUE_OK` içerir ve farklı URL bileşenleri handle'da tutulur. Bu, URL'nin libcurl açısından geçerli olduğu anlamına gelir.

İşlev çağrısının dördüncü argümanı bir bit maskesidir. Ayrıştırıcının davranışını değiştirmek için bunda hiç, bir veya daha fazla bit ayarlayın:

## `CURLU_NON_SUPPORT_SCHEME`

`curl_url_set()` işlevinin desteklenmeyen bir şemayı kabul etmesini sağlar. Ayarlanmazsa, kabul edilebilir tek şemalar libcurl'ün bildiği ve yerleşik desteğe sahip olduğu protokoller içindir.

## `CURLU_URLENCODE`

İşlevin, içindeki herhangi bir bayt bundan faydalanacaksa yol parçasını URL olarak kodlamasını sağlar: boşluklar veya "kontrol karakterleri" gibi.

## `CURLU_DEFAULT_SCHEME`

İletilen dize bir şema kullanmıyorsa, varsayılanın amaçlandığını varsayın. Varsayılan şema HTTPS'tir. Bu ayarlanmazsa, şema parçası olmayan bir URL geçerli olarak kabul edilmez. Her ikisi de ayarlanmışsa `CURLU_GUESS_SCHEME` seçeneğini geçersiz kılar.

## `CURLU_GUESS_SCHEME`

libcurl'ün URL'nin bir şema olmadan ayarlanmasına izin vermesini sağlar ve bunun yerine ana bilgisayar adına dayanarak hangi şemanın amaçlandığını "tahmin eder". En dıştaki alt alan adı DICT, FTP, IMAP, LDAP, POP3 veya SMTP ile eşleşirse o şema kullanılır, aksi takdirde HTTP'yi seçer. Her ikisi de ayarlanmışsa öncelikli olan `CURLU_DEFAULT_SCHEME` seçeneğiyle çakışır.

## `CURLU_NO_AUTHORITY`

Yetki (authority) kontrollerini atlar. RFC, bireysel şemaların ana bilgisayar parçasını (normalde yetkinin tek zorunlu parçası) atlamasına izin verir, ancak libcurl bunun özel şemalar için izin verilip verilmediğini bilemez. Bayrağı belirtmek, dosya şemasının nasıl işlendiğine benzer şekilde boş yetki bölümlerine izin verir. Gerçekten yalnızca `CURLU_NON_SUPPORT_SCHEME` ile birlikte kullanılabilir.

## `CURLU_PATH_AS_IS`

libcurl'ün yolun normalleştirilmesini atlamasını sağlar. Bu, curl'ün aksi takdirde nokta-eğik çizgi ve nokta-nokta vb. dizilerini kaldırdığı prosedürdür. Transferler için kullanılan aynı seçenek `CURLOPT_PATH_AS_IS` olarak adlandırılır.

## `CURLU_ALLOW_SPACE`

URL ayrıştırıcısının mümkün olduğunda boşluğa (ASCII 32) izin vermesini sağlar. URL sözdizimi normalde hiçbir yerde boşluklara izin vermez, ancak bunlar `%20` veya `+` olarak kodlanmalıdır. Boşluklara izin verildiğinde, şemada yine de izin verilmez. Bir URL'de boşluk kullanıldığında ve izin verildiğinde, `CURLU_URLENCODE` da ayarlanmadıkça olduğu gibi saklanır; bu da libcurl'ün saklamadan önce boşluğu URL olarak kodlamasını sağlar. Bu, `curl_url_get()` daha sonra tam URL'yi veya bireysel parçaları çıkarmak için kullanıldığında URL'nin nasıl oluşturulduğunu etkiler.
