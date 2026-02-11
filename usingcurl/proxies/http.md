# HTTP vekil sunucusu

HTTP vekil sunucusu, istemcinin transferi gerçekleştirmek için HTTP konuştuğu bir vekil sunucudur. curl varsayılan olarak `-x` veya `--proxy` ile işaret ettiğiniz bir ana bilgisayarın bir HTTP vekil sunucusu olduğunu varsayar ve ayrıca bir port numarası belirtmezseniz varsayılan olarak 1080 numaralı portu kullanır (ve bu belirli port numarasının nedeni tamamen tarihseldir).

192.168.0.1 port 8080 üzerindeki bir vekil sunucuyu kullanarak example.com web sayfasını istemek isterseniz, komut satırı şöyle görünebilir:

    curl -x 192.168.0.1:8080 http://example.com/

Vekil sunucunun isteğinizi aldığını, gerçek sunucuya ilettiğini, ardından sunucudan gelen yanıtı okuduğunu ve ardından bunu istemciye geri verdiğini hatırlayın.

Bir vekil sunucuyla konuşurken `-v` ile ayrıntılı modu etkinleştirirseniz, curl'ün uzak sunucu yerine vekil sunucuya bağlandığını gösterir ve biraz farklı bir istek satırı kullandığını görebilirsiniz.

## HTTP vekil sunucusu ile HTTPS

HTTPS, istemciden sunucuya (ve geriye) güvenli ve emniyetli uçtan uca gizlilik sağlamak için tasarlanmıştır. Bir HTTP vekil sunucusuyla konuşurken bunu sağlamak için, HTTP protokolünün curl'ün vekil sunucu üzerinden bir tünel kurmak için kullandığı ve ardından şifreleyip doğrulayabileceği özel bir isteği vardır. Bu HTTP yöntemi `CONNECT` olarak bilinir.

Bir CONNECT yöntemi kurduktan sonra vekil sunucu şifreli verileri uzak sunucuya tünellediğinde, vekil sunucu şifrelemeyi kırmadan trafiği göremez veya değiştiremez:

    curl -x proxy.example.com:80 https://example.com/

## HTTP vekil sunucusu üzerinden HTTP olmayan protokoller

Bir HTTP vekil sunucusu, vekil sunucunun kendisinin HTTP konuştuğu anlamına gelir. HTTP vekil sunucuları öncelikle HTTP'ye vekillik etmek için kullanılır ancak diğer protokolleri de desteklemeleri oldukça yaygındır. Özellikle FTP oldukça yaygın olarak desteklenir.

Bir HTTP vekil sunucusu üzerinden FTP konuşurken, bu genellikle diğer protokolün HTTP gibi çalıştığını taklit ederek ve URL HTTP kullanmasa bile vekil sunucudan bu URL'yi almasını isteyerek yapılır. Bu ayrım önemlidir çünkü bu şekilde bir HTTP vekil sunucusu üzerinden gönderildiğinde, curl bir FTP URL'si verilmesine rağmen gerçekten FTP konuşmaz; bu nedenle FTP'ye özgü özellikler çalışmaz:

    curl -x http://proxy.example.com:80 ftp://ftp.example.com/file.txt

Bunun yerine yapabileceğiniz şey, HTTP vekil sunucusu üzerinden tünel açmaktır.

## HTTP vekil sunucusu tünelleme

Çoğu HTTP vekil sunucusu, istemcilerin diğer taraftaki bir sunucuya tünel açmasına izin verir. HTTP vekil sunucusu üzerinden HTTPS'yi her kullandığınızda yapılan tam olarak budur.

curl ile `-p` veya `--proxytunnel` kullanarak bir HTTP vekil sunucusu üzerinden tünel açarsınız.

Bir vekil sunucu üzerinden HTTPS yaptığınızda normalde varsayılan HTTPS uzak TCP port numarası 443'e bağlanırsınız. Çoğu HTTP vekil sunucusu beyaz listeye alır ve yalnızca o port numarasındaki ana bilgisayarlara ve belki birkaç başkasına bağlantılara izin verir. Çoğu vekil sunucu, istemcilerin rastgele herhangi bir porta bağlanmasını reddeder (yalnızca vekil sunucu yöneticilerinin bildiği nedenlerle).

Yine de, HTTP vekil sunucusunun buna izin verdiğini varsayarsak, herhangi bir port numarasındaki uzak bir sunucuya tünel açmasını isteyebilirsiniz, böylece tünel açarken bile diğer protokolleri normal şekilde yapabilirsiniz. Şöyle FTP tünellemesi yapabilirsiniz:

    curl -p -x http://proxy.example.com:80 ftp://ftp.example.com/file.txt

curl'e, `-x` yerine `--proxy1.0 [vekil sunucu]` kullanarak HTTP vekil sunucusuna verdiği CONNECT isteğinde HTTP/1.0 kullanmasını söyleyebilirsiniz.
