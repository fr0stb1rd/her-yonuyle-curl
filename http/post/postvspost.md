# -d vs -F

Önceki bölümler [normal POST](simple.md) ve [multipart form gönderisi](multipart.md) hakkında konuştu ve tipik komut satırlarınızda bunları `-d` veya `-F` ile yaparsınız.

Hangisini ne zaman kullanırsınız?

Yukarıda belirtilen bölümlerde açıklandığı gibi, bu seçeneklerin her ikisi de belirtilen verileri sunucuya gönderir. Fark, verilerin kablo üzerinden nasıl biçimlendirildiğindedir. Çoğu zaman, alıcı uç belirli bir biçimi bekleyecek şekilde yazılmıştır ve gönderenin verileri doğru şekilde biçimlendirip göndermesini bekler. Bir istemci kendi seçimine göre bir biçim seçemez.

## HTML web formları

Tarayıcılar ve HTML'den bahsettiğimizde, standart yol kullanıcıya form doldurulduğunda verileri gönderen bir form sunmaktır. `<form>` etiketi bunlardan birinin web sayfasında görünmesini sağlayan şeydir. Etiket, tarayıcıya POST'unu nasıl biçimlendireceğini söyler. Form etiketi `enctype=multipart/form-data` içeriyorsa, bu tarayıcıya verileri curl'ün `-F` seçeneğiyle yaptığınız bir [multipart form gönderisi](multipart.md) olarak göndermesini söyler. Bu yöntem genellikle dosya yüklemeleri için form bir `<input type=file>` etiketi içerdiğinde kullanılır.

Formlar tarafından kullanılan ve varsayılan olduğu için HTML'de nadiren açıkça belirtilen varsayılan `enctype`, `application/x-www-form-urlencoded`'dir. Bu, tarayıcının girdiyi ad=değer çiftleri olarak URL kodlamasını ve verilerin güvenli olmayan karakterlerden kaçınmak için kodlanmasını sağlar. Buna sık sık [normal POST](simple.md) deriz ve bunu curl'ün `-d` ve arkadaşlarıyla gerçekleştirirsiniz.

## HTML dışında POST

POST normal bir HTTP yöntemidir ve HTML tarafından tetiklenmesi veya bir tarayıcı içermesi şartı yoktur. Pek çok hizmet, API ve diğer sistemler bugünlerde işleri halletmek için veri iletmenize izin verir.

Bu hizmetler düz ham veri veya belki JSON veya benzeri şekilde biçimlendirilmiş veri bekliyorsa, [normal POST](simple.md) yaklaşımını istersiniz. curl'ün `-d` seçeneği verileri hiç değiştirmez veya kodlamaz, sadece tam olarak söylediğinizi gönderir. `-d`'nin varsayılan bir `Content-Type:` ayarladığına dikkat edin, bu istediğiniz şey olmayabilir.
