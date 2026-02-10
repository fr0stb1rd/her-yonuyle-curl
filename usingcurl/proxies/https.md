# HTTPS vekil sunucusu

Vekil sunucuyla konuşmak için bahsedilen diğer tüm protokoller açık metin protokolleridir, HTTP ve SOCKS sürümleri. Bu yöntemleri kullanmak, birinin sizin veya vekil sunucunun bulunduğu yerel ağdaki trafiğinize kulak misafiri olmasına izin verebilir. Çünkü curl ile vekil sunucu arasındaki bağlantı üzerinden veriler açık olarak gönderilir.

Bunun bir çözümü, vekil sunucuyla HTTPS konuşan bir HTTPS vekil sunucusu kullanmaktır; bu daha sonra kolay gözetimden güvenli, güvenli ve şifreli bir bağlantı kurar.

Bir HTTPS vekil sunucusu belirtildiğinde, o ana bilgisayarda kullanılan varsayılan port 443'tür.

Diğer birçok yönden HTTPS vekil sunucuları [HTTP vekil sunucuları](http.md) gibi çalışır.

## HTTP/2

curl bir HTTPS vekil sunucusuyla konuştuğunda, curl'den vekil sunucuyla HTTP/2 kullanmayı denemesini istemek için `--proxy-http2` kullanma seçeneğiniz vardır.

Varsayılan olarak, curl HTTPS vekil sunucularıyla HTTP/1.1 konuşur, ancak bu seçenek kullanılırsa curl bunun yerine HTTP/2'yi görüşmeye ve kullanmaya çalışır.
