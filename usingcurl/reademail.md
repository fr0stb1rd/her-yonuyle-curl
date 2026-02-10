# E-posta okuma

İnternet'te sunuculardan e-posta okumak/indirmek için iki baskın protokol vardır (en azından web tabanlı okumayı saymazsak) ve bunlar IMAP ve POP3'tür. İlki biraz daha modern alternatiftir. curl her ikisini de destekler.

## POP3

Mesaj numaralarını ve boyutlarını listelemek için:

    curl pop3://mail.example.com/

1 numaralı mesajı indirmek için:

    curl pop3://mail.example.com/1

1 numaralı mesajı silmek için:

    curl --request DELE pop3://mail.example.com/1

## IMAP

'stuff' posta kutusundan UID 57'yi kullanarak postayı alın:

    curl imap://server.example.com/stuff;UID=57

Bunun yerine, 'fun' posta kutusundan 57 indeksli postayı alın:

    curl imap://server.example.com/fun;MAILINDEX=57

'boring' posta kutusundanki postaları listeleyin:

    curl imap://server.example.com/boring

'boring' posta kutusundanki postaları listeleyin ve kullanıcı ile şifre sağlayın:

    curl imap://server.example.com/boring -u user:password

## E-postalar için TLS

POP3 ve IMAP'in her ikisi de güvenli bir bağlantı üzerinden yapılabilir ve her ikisi de açık (explicit) veya örtük (implicit) TLS kullanılarak yapılabilir. "Açık" yöntem muhtemelen en yaygın yaklaşımdır ve istemcinin sunucuya güvenli olmayan bir bağlantı kullanarak bağlanması ve `STARTTLS` komutunu kullanarak ilerlerken bunu TLS'ye *yükseltmesi* anlamına gelir. curl'e bunu denemesini `--ssl` ile söylersiniz veya güvenli bir bağlantıda *ısrar etmek* isterseniz `--ssl-reqd` kullanırsınız. Şöyle:

    curl pop3://mail.example.com/ --ssl-reqd

veya

    curl --ssl imap://mail.example.com/inbox

"Örtük" SSL, bağlantının daha ilk bağlantıda güvenli hale getirilmesi anlamına gelir; bunu curl'ün URL'deki şemada SSL kullanan bir şema belirterek denemesini sağlarsınız. Bu durumda ya `pop3s://` ya da `imaps://`. Bu tür bağlantılar için curl, daha baştan bağlanmak ve bir TLS bağlantısı müzakere etmek konusunda ısrar eder, aksi takdirde işlemi başarısız olur.

Örtük SSL ile yapılan önceki açık örnekler:

    curl pop3s://mail.example.com/

veya

    curl imaps://mail.example.com/inbox
