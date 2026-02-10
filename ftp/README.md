# Komut satırı FTP

FTP (Dosya Aktarım Protokolü), curl'ün desteklediği muhtemelen en eski ağ protokolüdür; 1970'lerin başında oluşturulmuştur. Hala başvurulan resmi belge, ilk curl sürümünden on yıldan fazla bir süre önce, 1985'te yayınlanan [RFC 959](https://www.ietf.org/rfc/rfc959.txt)'dur.

FTP, İnternet ve bilgisayarların farklı bir çağında yaratılmıştır ve bu nedenle diğer çoğu protokolden biraz farklı çalışır. Bu farklılıklar genellikle göz ardı edilebilir ve her şey çalışır, ancak işler planlandığı gibi gitmediğinde bunları bilmek de önemlidir.

## Ping-pong

FTP protokolü bir komut ve yanıt protokolüdür; istemci bir komut gönderir ve sunucu yanıt verir. curl'ün `-v` seçeneğini kullanırsanız, bir transfer sırasındaki tüm komutları ve yanıtları görürsünüz.

Sıradan bir transfer için, gönderilmesi gereken yaklaşık 5 ila 8 komut ve beklenip okunması gereken bir o kadar yanıt vardır. Belki de söylemeye gerek yok, eğer sunucu uzak bir konumdaysa, gerçek dosya transferi ayarlanıp başlayabilmeden önce ping pong'un gerçekleşmesi için çok zaman harcanır. Küçük dosyalar için, ilk komutlar gerçek veri transferinden daha uzun sürebilir.

## Transfer modu

Bir FTP istemcisi veri aktarmak üzereyken, sunucuya yaklaşan transferin hangi transfer modunu kullanmasını istediğini belirtir. curl'ün desteklediği iki transfer modu 'ASCII' ve 'BINARY'dir. Ascii metin içindir ve genellikle sunucunun dosyaları dönüştürülmüş yeni satırlarla gönderdiği anlamına gelirken, binary (ikili) verilerin değiştirilmeden gönderilmesi ve dosyanın metin olmadığının varsayılması anlamına gelir.

curl, FTP için varsayılan olarak binary transfer modunu kullanır ve bunun yerine `-B, --use-ascii` ile veya URL'nin `;type=A` ile bittiğinden emin olarak ascii modunu istersiniz.

## Kimlik Doğrulama

FTP, normalde bir kullanıcı adı ve şifre olmadan erişmediğiniz protokollerden biridir. Sadece anonim FTP erişimine izin veren sistemler için hemen hemen istediğiniz herhangi bir isim ve şifreyle giriş yapabilirsiniz. curl, herhangi bir kullanıcı adı veya şifre verilmeden transfer yapmak için bir FTP URL'sinde kullanıldığında, `anonymous` adını ve `ftp@example.com` şifresini kullanır.

Başka bir kullanıcı adı ve şifre sağlamak istiyorsanız, bunları curl'e `-u, --user` seçeneğiyle iletebilir veya bilgiyi URL'ye gömebilirsiniz:

    curl --user daniel:secret ftp://example.com/download

    curl ftp://daniel:secret@example.com/download

  * [FTP Dizin listeleme](dirlist.md)
  * [FTP ile yükleme](upload.md)
  * [Özel FTP komutları](cmds.md)
  * [İki bağlantı](twoconnections.md)
  * [Dizin dolaşma](traversedir.md)
  * [FTPS](ftps.md)
