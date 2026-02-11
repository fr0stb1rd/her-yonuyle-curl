# TLS'yi etkinleştirme

curl birçok protokolün TLS sürümünü destekler. HTTP'nin HTTPS'i, FTP'nin FTPS'i, LDAP'ın LDAPS'ı, POP3'ün POP3S'i, IMAP'in IMAPS'i ve SMTP'nin SMTPS'i vardır.

Sunucu tarafı destekliyorsa, bu protokollerin TLS sürümünü curl ile kullanabilirsiniz.

Protokollerle TLS yapmak için iki genel yaklaşım vardır. Bunlardan biri daha ilk bağlantı el sıkışmasından itibaren TLS konuşmak, diğeri ise protokole özel talimatlar kullanarak bağlantıyı düz metinden TLS'ye yükseltmektir.

curl ile, URL'de protokolün TLS sürümünü (adı 'S' karakteriyle biten) açıkça belirtirseniz, curl baştan TLS ile bağlanmaya çalışır; URL'de TLS olmayan sürümü belirtirseniz, bağlantıyı genellikle `--ssl` seçeneğiyle TLS tabanlıya yükseltebilirsiniz.

Destek tablosu şöyledir:

| Açık   | TLS sürümü  | --ssl   |
|--------|-------------|---------|
| HTTP   | HTTPS       | hayır   |
| LDAP   | LDAPS       | hayır   |
| FTP    | FTPS        | **evet**|
| POP3   | POP3S       | **evet**|
| IMAP   | IMAPS       | **evet**|
| SMTP   | SMTPS       | **evet**|

`--ssl` yapabilen protokollerin hepsi bu yöntemi tercih eder. `--ssl` kullanmak, curl'ün bağlantıyı TLS'ye yükseltmeye *çalıştığı*, ancak bu başarısız olursa yine de protokolün düz metin sürümünü kullanarak transfere devam ettiği anlamına gelir. `--ssl` seçeneğinin devam etmek için TLS'yi **gerektirmesini** sağlamak için, bunun yerine curl TLS'yi başarılı bir şekilde müzakere edemezse transferin başarısız olmasını sağlayan `--ssl-reqd` seçeneği vardır.

FTP transferiniz için TLS güvenliğini gerektirin:

    curl --ssl-reqd ftp://ftp.example.com/file.txt

FTP transferiniz için TLS kullanılmasını önerin:

    curl --ssl ftp://ftp.example.com/file.txt

Doğrudan TLS ile bağlanmak (`HTTPS://`, `LDAPS://`, `FTPS://` vb. ile), TLS'nin zorunlu olduğu ve TLS müzakere edilmezse curl'ün bir hata döndürdüğü anlamına gelir.

HTTPS üzerinden bir dosya alın:

    curl https://www.example.com/
