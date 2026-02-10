# E-posta gönderme

curl ile e-posta göndermek SMTP protokolü ile yapılır. SMTP, [Basit Posta Aktarım Protokolü](https://tr.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) (Simple Mail Transfer Protocol) anlamına gelir.

curl, bir SMTP sunucusuna veri göndermeyi destekler; bu, doğru komut satırı seçenekleri setiyle birleştirildiğinde bir e-postanın seçtiğiniz bir alıcılar grubuna gönderilmesini sağlar.

curl ile SMTP gönderirken, kullanılması **gereken** iki gerekli komut satırı seçeneği vardır.

 - Sunucuya `--mail-rcpt` ile en az bir alıcı söylemeniz gerekir. Bu seçeneği birkaç kez kullanabilirsiniz ve ardından curl sunucuya tüm bu e-posta adreslerinin e-postayı alması gerektiğini söyler.

 - Sunucuya e-postanın göndericisinin hangi e-posta adresi olduğunu `--mail-from` ile söylemeniz gerekir. Bu e-posta adresinin e-posta metninin `From:` satırında gösterilenle aynı olması gerekmediğini fark etmek önemlidir.

Ardından, gerçek e-posta verilerini sağlamanız gerekir. Bu, [RFC 5322](https://tools.ietf.org/html/rfc5322.html)'ye göre biçimlendirilmiş bir (metin) dosyasıdır. Bir başlıklar seti ve bir gövdedir. Hem başlıkların hem de gövdenin doğru şekilde kodlanması gerekir. Başlıklar tipik olarak `To:`, `From:`, `Subject:`, `Date:` vb. içerir.

Bir e-posta göndermek için temel bir komut:

    curl smtp://mail.example.com --mail-from myself@example.com --mail-rcpt \
    receiver@example.com --upload-file email.txt

Örnek bir `email.txt` şöyle görünebilir:

    From: John Smith <john@example.com>
    To: Joe Smith <smith@example.com>
    Subject: an example.com example email
    Date: Mon, 7 Nov 2016 08:45:16

    Dear Joe,
    Welcome to this example email. What a lovely day.

## Güvenli posta transferi

Bazı posta sağlayıcıları SMTP için SSL kullanılmasına izin verir veya bunu gerektirir. SSL için özel bir port kullanabilirler veya açık metin bağlantısı üzerinden SSL yükseltmesine izin verebilirler.

Posta sağlayıcınızın özel bir SSL portu varsa, varsayılan olarak 465 numaralı SMTP SSL portunu kullanan ve tüm bağlantının SSL olmasını gerektiren smtp:// yerine smtps:// kullanabilirsiniz. Örneğin smtps://smtp.gmail.com/.

Ancak, sağlayıcınız açık metinden güvenli transferlere yükseltmeye izin veriyorsa şu seçeneklerden birini kullanabilirsiniz:

    --ssl           SSL/TLS Dene (FTP, IMAP, POP3, SMTP)
    --ssl-reqd      SSL/TLS Gerektir (FTP, IMAP, POP3, SMTP)


Komuta `--ssl` ekleyerek curl'e güvenli transferlere yükseltmeyi _denemesini_ ancak gerektirmemesini söyleyebilirsiniz:

    curl --ssl smtp://mail.example.com --mail-from myself@example.com \
         --mail-rcpt receiver@example.com --upload-file email.txt \
         --user 'user@your-account.com:your-account-password'

Komuta `--ssl-reqd` ekleyerek curl'e güvenli transferleri kullanmaya yükseltmeyi _gerektirmesini_ söyleyebilirsiniz:

    curl --ssl-reqd smtp://mail.example.com --mail-from myself@example.com \
         --mail-rcpt receiver@example.com --upload-file email.txt \
         --user 'user@your-account.com:your-account-password'

## SMTP URL'si

Bir SMTP isteğinin yol kısmı, posta sunucusuyla iletişim sırasında sunulacak ana bilgisayar adını belirtir. Yol atlanırsa, curl yerel bilgisayarın ana bilgisayar adını bulmaya ve onu kullanmaya çalışır. Ancak bu, bazı posta sunucuları tarafından gerekli kılınan tam nitelikli alan adını (FQDN) döndürmeyebilir ve bu yolu belirtmek, gethostname veya getaddrinfo gibi harici bir işlevden elde etmiş olabileceğiniz makinenizin tam nitelikli alan adı gibi alternatif bir ad ayarlamanıza olanak tanır.

`mail.example.com` adresindeki posta sunucusuna bağlanmak ve `HELO` veya `EHLO` komutunda yerel bilgisayarınızın ana bilgisayar adını göndermek için:

    curl smtp://mail.example.com

İstemci-sunucu iletişimini görmek için her zaman olduğu gibi `-v` seçeneğini kullanabilirsiniz.

Bunun yerine curl'ün `mail.example.com` adresindeki posta sunucusuna `HELO` / `EHLO` komutunda `client.example.com` göndermesini sağlamak için şunu kullanın:

    curl smtp://mail.example.com/client.example.com

## MX araması yok (No MX lookup)

Sıradan bir posta istemcisiyle e-posta gönderdiğinizde, önce e-posta göndermek istediğiniz belirli alan adı için bir MX kaydı olup olmadığını kontrol eder. `joe@example.com` adresine bir e-posta gönderirseniz, istemci example.com kullanıcılarına e-posta gönderirken hangi posta sunucu(ları)nı kullanacağını öğrenmek için `example.com` için MX kayıtlarını alır.

curl kendi başına hiçbir MX araması yapmaz. Belirli bir alan adı için hangi sunucuya e-posta göndereceğinizi bulmak istiyorsanız, bunu önce bulmanızı ve ardından curl'ü bu sunucuları kullanması için çağırmanızı öneririz. MX kayıtlarını almak için yararlı komut satırı araçları arasında 'dig' ve 'nslookup' bulunur.
