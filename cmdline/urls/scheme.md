# Şema (Scheme)

URL'ler, `http://` kısmının resmi adı olan "şema" ile başlar. Bu, URL'nin hangi protokolü kullandığını söyler. Şema, curl'ün bu sürümünün desteklediği bilinen bir şema olmalıdır, aksi takdirde bir hata mesajı gösterir ve durur. Ayrıca, şema ne boşlukla başlamalı ne de herhangi bir boşluk içermelidir.

## Şema ayırıcı

Şema tanımlayıcısı, URL'nin geri kalanından `://` dizisi ile ayrılır. Bu iki nokta üst üste ve iki eğik çizgidir. Yalnızca bir eğik çizgi içeren URL formatları mevcuttur, ancak curl bunlardan hiçbirini desteklemez. Eğik çizgi sayısı hakkında bilinmesi gereken iki ek not vardır:

curl bazı geçersiz sözdizimlerine izin verir ve bunları dahili olarak düzeltmeye çalışır; bu nedenle, aslında düzgün biçimlendirilmiş URL'ler olmamasına rağmen, bir veya üç eğik çizgili URL'leri de anlar ve kabul eder. curl bunu yapar çünkü tarayıcılar bu uygulamayı başlattı, bu yüzden bu tür URL'lerin arada sırada vahşi doğada kullanılmasına yol açtı.

`file://` URL'leri `file://<anabilgisayar>/<yol>` olarak yazılır ancak kullanılması uygun olan tek ana bilgisayar adları (hostnames) `localhost`, `127.0.0.1` veya boş (hiçbir şey) olanlardır:

    file://localhost/path/to/file
    file://127.0.0.1/path/to/file
    file:///path/to/file

Oraya başka bir ana bilgisayar adı eklemek, curl'ün son sürümlerinin bir hata döndürmesine neden olur.

Yukarıdaki üçüncü örneğe (`file:///path/to/file`) özellikle dikkat edin. Bu, yoldan önce *üç* eğik çizgidir. Bu yine yaygın hataların olduğu ve tarayıcıların kullanıcıların yanlış sözdizimini kullanmasına izin verdiği bir alandır, bu nedenle özel bir istisna olarak Windows'ta curl bu yanlış formata da izin verir:

    file://X:/path/to/file

… burada X, windows tarzı bir sürücü harfidir.

## Şema olmadan

Kolaylık sağlamak için, curl kullanıcıların URL'lerden şema kısmını çıkarmasına da izin verir. O zaman ana bilgisayar adının ilk kısmına göre hangi protokolün kullanılacağını tahmin eder. Bu tahmin basittir, çünkü sadece ana bilgisayar adının ilk kısmının bir protokol setiyle eşleşip eşleşmediğini kontrol eder ve o protokolü kullanmak istediğinizi varsayar. Bu buluşsal yöntem, sunucuların geleneksel olarak böyle adlandırıldığı gerçeğine dayanmaktadır. Bu şekilde algılanan protokoller FTP, DICT, LDAP, IMAP, SMTP ve POP3'tür. Şemasız bir URL'deki diğer herhangi bir ana bilgisayar adı, curl'ün varsayılan olarak HTTP kullanmasını sağlar.

Örneğin, bu bir FTP sitesinden bir dosya alır:

    curl ftp.funet.fi/README

Bu ise hır HTTP sunucusundan veri alırken:

    curl example.com

`--proto-default` seçeneği ile varsayılan protokolü HTTP dışında bir şeye değiştirebilirsiniz.

## Desteklenen şemalar

curl aşağıdaki transfer şemalarını ve protokollerini destekler veya desteklemesi sağlanabilir (eğer öyle derlenmişse):

DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS,
MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS,
TELNET, TFTP, WS ve WSS
