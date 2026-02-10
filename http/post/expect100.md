# Expect 100-continue

HTTP/1'in devam eden bir transferi (herhangi bir yönde) durdurup yine de bağlantıyı sürdürmenin uygun bir yolu yoktur. Bu nedenle, transfer başladıktan sonra transferin durmasının daha iyi olacağını anlarsak, ilerlemenin sadece iki yolu vardır: bağlantıyı kesmek ve bir sonraki istek için bağlantıyı yeniden kurmanın bedelini ödemek veya transferi devam ettirip bant genişliğini boşa harcamak ancak bir dahaki sefere bağlantıyı yeniden kullanabilmek.

Bunun ne zaman olabileceğine dair bir örnek, HTTP üzerinden büyük bir dosya gönderdiğinizde, ancak sunucunun kimlik doğrulaması gerektirdiğini ve hemen bir 401 yanıt kodu geri gönderdiğini keşfetmenizdir.

Bu senaryoyu daha az sık hale getirmek için mevcut azaltma yöntemi, curl'ün ekstra bir başlık, `Expect: 100-continue` iletmesidir; bu, sunucuya çok fazla veri gönderilmeden önce isteği reddetme şansı verir. curl, yaptığı POST'un bir megabayttan büyük olduğu biliniyorsa veya şüpheleniliyorsa varsayılan olarak bu `Expect:` başlığını gönderir. curl bunu PUT istekleri için de yapar.

Bir sunucu 100-continue içeren bir istek aldığında ve isteği uygun bulduğunda, istemcinin devam etmesini sağlayan bir 100 yanıtıyla yanıt verir. Sunucu isteği beğenmezse, ne olduğunu düşündüğü hata için yanıt kodunu geri gönderir.

Maalesef, dünyadaki pek çok sunucu Expect: başlığını düzgün bir şekilde desteklemiyor veya doğru şekilde işlemiyor, bu yüzden curl yine de devam etmeden önce o ilk yanıt için sadece 1000 milisaniye bekler.

`--expect100-timeout <saniye>` kullanarak curl'ün Expect yanıtı için beklediği süreyi değiştirebilirsiniz. Başlığı kaldırmak için `-H Expect:` kullanarak beklemekten tamamen kaçınabilirsiniz:

    curl -H Expect: -d "payload to send" http://example.com

Bazı durumlarda curl, göndermek üzere olduğu içerik küçükse (bir megabaytın altında) `Expect` başlığının kullanımını engeller, çünkü bu kadar küçük bir veri yığınını boşa harcamak çok büyük bir sorun olarak görülmez.

## HTTP/2 ve sonrası

HTTP/2 ve HTTP'nin sonraki sürümleri, bağlantıyı kapatmadan devam eden bir transferi durdurabilir, bu da `Expect:` başlığını anlamsız kılar.
