# Multipart form gönderileri

Multipart (çok parçalı) bir form gönderisi (multipart formpost), bir HTML formu *enctype* `multipart/form-data` olarak ayarlanmış şekilde gönderildiğinde bir HTTP istemcisinin gönderdiği şeydir. Bu, istek gövdesi MIME sınırlarıyla ayrılmış bir dizi parça olarak özel olarak biçimlendirilmiş şekilde gönderilen bir HTTP POST isteğidir.

Örnek bir HTML parçası şöyle görünür:

    <form action="submit.cgi" method="post" enctype="multipart/form-data">
      Name: <input type="text" name="person"><br>
      File: <input type="file" name="secret"><br>
      <input type="submit" value="Submit">
    </form>

Bu, bir web tarayıcısında şuna benzer görünebilir:

![bir multipart formu](multipart-form.png)

Bir kullanıcı 'Name' alanına metin girebilir ve `Browse` düğmesine basarak `Submit` düğmesine basıldığında yüklenecek yerel bir dosya seçilebilir.

## Böyle bir formu curl ile gönderme

curl ile, her ayrı multipart'ı bir `-F` (veya `--form`) bayrağıyla eklersiniz ve ardından forma göndermek istediğiniz her giriş alanı için bir -F ekleyerek devam edersiniz.

Yukarıdaki küçük örnek formun iki parçası vardır; biri düz metin alanı olan 'person' adında ve diğeri bir dosya olan 'secret' adında.

Verilerinizi o forma şöyle gönderin:

    curl -F person=anonymous -F secret=@file.txt http://example.com/submit.cgi

## Bunun oluşturduğu HTTP

**action**, POST'un nereye gönderildiğini belirtir. **method**, bunun bir POST olduğunu söyler ve **enctype**, bunun bir multipart form gönderisi olduğunu söyler.

Alanlar yukarıda gösterildiği gibi doldurulduğunda, curl example.com ana bilgisayarına şu HTTP istek başlıklarını oluşturur ve gönderir:

    POST /submit.cgi HTTP/1.1
    Host: example.com
    User-Agent: curl/7.46.0
    Accept: */*
    Content-Length: 313
    Expect: 100-continue
    Content-Type: multipart/form-data; boundary=------------d74496d66958873e

**Content-Length**, elbette sunucuya ne kadar veri beklemesi gerektiğini söyler. Bu örneğin 313 baytı gerçekten küçüktür.

**Expect** başlığı [Expect 100 continue](expect100.md) bölümünde açıklanmıştır.

**Content-Type** başlığı biraz özeldir. Bunun bir multipart form gönderisi olduğunu söyler ve ardından sınır (boundary) dizesini ayarlar. Sınır dizesi, formun gönderilen farklı parçaları arasında ayırıcı görevi gören, içinde bir yerlerde bir sürü rastgele basamak bulunan bir karakter satırıdır. Bu örnekte gördüğünüz belirli sınır `d74496d66958873e` rastgele parçasına sahiptir ancak elbette curl çalıştırdığınızda (veya böyle bir formu bir tarayıcıyla gönderdiğinizde) farklı bir şey alırsınız.

Bu ilk başlık setinden sonra istek gövdesi gelir

    --------------------------d74496d66958873e
    Content-Disposition: form-data; name="person"

    anonymous
    --------------------------d74496d66958873e
    Content-Disposition: form-data; name="secret"; filename="file.txt"
    Content-Type: text/plain

    contents of the file
    --------------------------d74496d66958873e--

Burada gönderilen iki parçayı, sınır dizeleriyle ayrılmış olarak açıkça görürsünüz. Her parça, bireysel parçayı adı ve muhtemelen daha fazla ayrıntı ile tanımlayan bir veya daha fazla başlıkla başlar. Sonra parçanın başlıklarından sonra, herhangi bir kodlama olmadan parçanın gerçek verileri gelir.

Son sınır dizesinde bitişi işaret etmek için iki ekstra tire `--` eklenmiştir.

## Content-Type

curl'ün `-F` seçeneğiyle POST yapmak, yukarıdaki örnekte gösterildiği gibi isteğine varsayılan bir `Content-Type` başlığı eklemesini sağlar. Bu `multipart/form-data` der ve ardından MIME sınır dizesini belirtir. Bu `Content-Type` multipart form gönderileri için varsayılandır ancak elbette bunu kendi komutlarınız için yine de değiştirebilirsiniz ve yaparsanız, curl değiştirilen başlığa sınır sihirini yine de ekleyecek kadar zekidir. Sınır dizesini gerçekten değiştiremezsiniz, çünkü curl POST akışını üretmek için buna ihtiyaç duyar.

Başlığı değiştirmek için `-H`'yi şöyle kullanın:

    curl -F 'name=Dan' -H 'Content-Type: multipart/magic' https://example.com

## Bir web formunu dönüştürme

HTML'de görülen bir multipart formu göndermek için bir curl komut satırının nasıl yazılacağını bulmanın birkaç farklı yolu vardır.

1. HTML'yi yerel olarak kaydedin, seçilen bir port numarasını dinlemek için yerel olarak `nc` çalıştırın, POST'u yerel `nc` örneğinize göndermek için `action` URL'sini değiştirin. Formu gönderin ve `nc`'nin bunu nasıl gösterdiğini izleyin. Sonra bir curl komut satırına çevirin.

2. Favori tarayıcınızdaki geliştirme araçlarını kullanın ve gönderdikten sonra ağ sekmesinde POST isteğini inceleyin. Sonra o HTTP verilerini bir curl komut satırına dönüştürün. Ne yazık ki, tarayıcılardaki [curl olarak kopyala](../../cmdline/copyas.md) özelliği genellikle multipart form gönderilerini özellikle iyi yapmaz.

3. Kaynak HTML'yi inceleyin ve doğrudan ondan bir curl komut satırına dönüştürün.

## `<form>`'dan -F'ye

`enctype="multipart/form-data"` kullanan bir `<form>`'da ilk adım, POST için hedefi söylediği için `action=` özelliğini bulmaktır. Bunu curl komut satırınız için tam bir URL'ye dönüştürmeniz gerekir.

Örnek bir action şöyle görünür:

    <form action="submit.cgi" method="post" enctype="multipart/form-data">

Form örneğin `https://example.com/user/login` gibi bir URL'de barındırılan bir web sayfasında bulunuyorsa, `action=submit.cgi` formun kendisiyle aynı dizin içinde göreceli bir yoldur. Bu formu göndermek için tam URL böylece `https://example.com/user/submit.cgi` olur. Bu, curl komut satırında kullanılacak URL'dir.

Ardından, gizli olarak işaretlenmiş olanlar da dahil olmak üzere form içinde kullanılan her `<input>` etiketini tanımlamanız gerekir. Gizli, sadece web sayfasında gösterilmedikleri anlamına gelir, ancak yine de POST içinde gönderilmeleri gerekir.

Formdaki her `<input>` için komut satırında karşılık gelen bir `-F` olmalıdır.

### metin girişi (text input)

Şu tarzdaki metin kullanan normal bir etiket

    <input type="text" name="person">

alan adını şu şekilde içerikle ayarlamalıdır:

    curl -F "person=Mr Smith" https://example.com/

### dosya girişi (file input)

Giriş türü bir dosyaya ayarlandığında, şunun gibi:

    <input type="file" name="image">

Dosya adını belirterek ve `@` ve dahil edilecek dosyanın yolunu kullanarak bu parça için bir dosya sağlarsınız:

    curl -F image=@funnycat.gif https://example.com/

### gizli giriş (hidden input)

Bir formdan durum iletmek için yaygın bir teknik, bir dizi `<input>` etiketini `type="hidden"` olarak ayarlamaktır. Bu temelde zaten doldurulmuş bir form alanıyla aynı şeydir, bu nedenle bunu ad ve değeri kullanarak bir komut satırına dönüştürürsünüz. Örneğin:

    <input type="hidden" name="username" value="bob123">

Bu normal metin alanı gibi dönüştürülür ve burada içeriğin ne olması gerektiğini bilirsiniz:

    curl -F "username=bob123" https://example.com/

### Tüm alanlar aynı anda

Yukarıdaki örneklerde gösterilen üç farklı `<input>` etiketinin aynı `<form>` içinde kullanıldığı fikriyle oynarsak, yukarıda çıkarılan doğru URL dahil olmak üzere gönderilecek tam bir curl komut satırı şuna benzer:

    curl -F "person=Mr Smith" -F image=@funnycat.gif -F "username=bob123" \
      https://example.com/user/submit.cgi
