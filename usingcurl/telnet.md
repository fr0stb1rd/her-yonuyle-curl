# TELNET

Telnet, çift yönlü **açık metin** iletişimi için eski bir uygulama protokolüdür. Etkileşimli metin odaklı iletişimler için tasarlanmıştır ve Telnet'in *şifreli veya güvenli bir sürümü yoktur*.

TELNET, curl için mükemmel bir eşleşme değildir. Protokol düz yüklemeleri veya indirmeleri işlemek için yapılmamıştır, bu nedenle olağan curl paradigmaları curl'ün onunla uygun şekilde başa çıkmasını sağlamak için biraz esnetilmek zorunda kalmıştır.

curl, alınan verileri stdout'a gönderir ve stdin'e gönderilecek girdiyi okur. Bağlantı kesildiğinde veya kullanıcı control-c tuşlarına bastığında transfer tamamlanır.

## Tarihi TELNET

Bir zamanlar, sistemler giriş için telnet erişimi sağlıyordu. O zaman bir sunucuya bağlanabilir ve bugün SSH ile yaptığınız gibi ona giriş yapabilirdiniz. Bu uygulama neyse ki protokolün güvensiz doğası nedeniyle artık çoğunlukla müze dolaplarına taşındı.

telnet için varsayılan port numarası 23'tür.

## TELNET ile hata ayıklama

TELNET'in temel olarak hedef ana bilgisayar ve porta basit bir açık metin TCP bağlantısı olması gerçeği, onu zaman zaman diğer protokolleri ve hizmetleri hata ayıklamak için biraz yararlı kılar.

Örnek, 80. porttaki yerel HTTP sunucunuza bağlanın ve manuel olarak `GET /` girip return tuşuna iki kez basarak ona (bozuk) bir istek gönderin:

    curl telnet://localhost:80

Web sunucunuz büyük olasılıkla şuna benzer bir şey döndürür:

    HTTP/1.1 400 Bad Request
    Date: Tue, 07 Dec 2021 07:41:16 GMT
    Server: softeare/7.8.9
    Content-Length: 31
    Connection: close
    Content-Type: text/html

    [message]

## Seçenekler

curl bir sunucuya bir TELNET bağlantısı kurduğunda, ondan seçenekleri iletmesini isteyebilirsiniz. Bunu `--telnet-option` (veya `-t`) ile yaparsınız ve kullanılabilecek üç seçenek vardır:

- `TTYPE=<term>` oturum için "terminal türünü" `<term>` olacak şekilde ayarlar.
- `XDISPLOC=<X display>` X ekran konumunu ayarlar
- `NEW_ENV=<var,val>` uzak oturumda `var` ortam değişkenini `val` değerine ayarlar

Yerel makinenizin telnet sunucusuna giriş yapın ve bir `vt100` terminali kullandığınızı söyleyin:

    curl --telnet-option TTYPE=vt100 telnet://localhost

İstendiğinde adınızı ve şifrenizi manuel olarak girmeniz gerekir.
