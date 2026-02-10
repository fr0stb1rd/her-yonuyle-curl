# Yüklemeler (Uploads)

Yükleme, uzak bir sunucuya veri göndermek için kullanılan bir terimdir. Yükleme her protokol için farklı şekilde yapılır ve hatta birkaç protokol verileri yüklemenin farklı yollarına izin verebilir.

## Yüklemeye izin veren protokoller

Şu protokollerden birini kullanarak veri yükleyebilirsiniz: FILE, FTP, FTPS, HTTP, HTTPS, IMAP, IMAPS, SCP, SFTP, SMB, SMBS, SMTP, SMTPS ve TFTP.

## HTTP çeşitli yüklemeler sunar

HTTP ve onun büyük kardeşi HTTPS, bir sunucuya veri yüklemek için birkaç farklı yol sunar ve curl, aşağıda açıklanan en yaygın üç yolu yapmak için kolay komut satırı seçenekleri sağlar.

HTTP ile ilgili ilginç bir ayrıntı, bir yüklemenin aynı işlemde bir indirme de olabilmesidir ve aslında birçok indirme bir HTTP POST ile başlatılır.

### POST

POST, bir alıcı web uygulamasına veri göndermek için icat edilen HTTP yöntemidir ve örneğin web'deki en yaygın HTML formlarının çalışma şeklidir. Genellikle alıcıya nispeten küçük miktarlarda veri parçası gönderir.

Yükleme türü genellikle `-d` veya `--data` seçenekleriyle yapılır, ancak birkaç ek değişiklik daha vardır.

Bunu curl ile nasıl yapacağınıza dair ayrıntılı açıklamayı [curl ile HTTP POST](../http/post/) bölümünde okuyun.

### multipart formpost

Multipart (çok parçalı) form gönderileri, web sitelerindeki HTML formlarında da kullanılır; genellikle bir dosya yüklemesi söz konusu olduğunda. Bu tür bir yükleme de bir HTTP POST'tur ancak verileri, multipart adının anlamı olan bazı özel kurallara göre biçimlendirilmiş olarak gönderir.

Verileri tamamen farklı biçimlendirilmiş olarak gönderdiğinden, hangi tür POST'u kullanacağınızı kendi isteğinize göre seçemezsiniz, ancak bu tamamen alıcı sunucu tarafının ne beklediğine ve neyi işleyebileceğine bağlıdır.

HTTP multipart form gönderileri `-F` ile yapılır. [HTTP multipart form gönderileri](../http/post/multipart.md) bölümündeki ayrıntılı açıklamaya bakın.

### PUT

HTTP PUT, uzak siteye olduğu gibi konulması veya hatta orada mevcut bir kaynağın yerini alması amaçlanan tam bir kaynağı göndermek için tasarlanmış yükleme yöntemidir. Bununla birlikte, bu aynı zamanda bugün web'de HTTP için en az kullanılan yükleme yöntemidir ve çoğu olmasa da birçok web sunucusunda PUT etkin bile değildir.

Yüklenecek dosyayla birlikte -T seçeneğini kullanarak bir HTTP yüklemesi gönderirsiniz:

    curl -T uploadthis http://example.com/

## FTP ve SFTP yüklemeleri

FTP ve SFTP ile çalışırken, eriştiğiniz uzak dosya sistemini görürsünüz. Sunucuya yüklemenin tam olarak hangi dizine yerleştirilmesini istediğinizi ve hangi dosya adının kullanılacağını tam olarak söylersiniz. Yükleme URL'sini sonunda bir eğik çizgi ile belirtirseniz, curl yerel olarak kullanılan dosya adını URL'ye ekler ve daha sonra uzak olarak saklandığında kullanılan dosya adı o olur:

    curl -T uploadthis ftp://example.com/this/directory/

FTP ve SFTP ayrıca üzerine yazmak yerine yüklerken hedef dosyaya *eklemeyi* (appending), `--append` seçeneğiyle destekler:

    curl -T uploadthis --append ftp://example.com/directory/remotename

"FTP with curl" ([curl ile FTP](../ftp/)) bölümünde FTP kullanımı hakkında çok daha fazla bilgi edinin.

## SMTP yüklemeleri

Bir e-posta göndermeyi yükleme olarak düşünmeyebilirsiniz, ancak curl için öyledir. Posta gövdesini SMTP sunucusuna yüklersiniz. SMTP ile, curl hiç eklemediği için ihtiyacınız olan tüm posta başlıklarını (`To:`, `From:`, `Date:` vb.) posta gövdesine de eklemeniz gerekir.

    curl -T mail smtp://mail.example.com/ --mail-from user@example.com

[E-posta gönderme](smtp.md) bölümünde curl ile SMTP kullanımı hakkında daha fazla bilgi edinin.

## Yüklemeler için ilerleme göstergesi

curl'ün sağladığı genel ilerleme göstergesi ([İlerleme göstergesi](../cmdline/progressmeter.md) bölümüne bakın) yüklemeler için de gayet iyi çalışır.
Hatırlanması gereken şey, çıktıyı stdout'a gönderdiğinizde ilerleme göstergesinin otomatik olarak devre dışı bırakıldığıdır ve curl'ün desteklediği çoğu protokol bir yükleme için bile bir şeyler çıktılayabilir.

Bu nedenle, yükleme için ilerleme göstergesinin görüntülenmesini sağlamak için indirilen verileri açıkça bir dosyaya (kabuk yönlendirmesi '>', `-o` veya benzerini kullanarak) yönlendirmeniz gerekebilir.

## Globbing

curl ayrıca `-T` argümanında [globbing](../cmdline/urls/globbing.md) desteği sunar, böylece bir dizi dosyayı kolayca yüklemeyi seçebilirsiniz:

    curl -T 'image[1-99].jpg' ftp://ftp.example.com/upload/

veya bir dosya serisi:

    curl -T '{file1,file2}' https://example.com/upload/

veya

    curl -T '{Huey,Dewey,Louie}.jpg' ftp://ftp.example.com/nephews/
