# Özel FTP komutları

FTP protokolü, istemcinin curl'ün odaklandığı düz dosya transferleri dışındaki eylemleri gerçekleştirmesine izin veren çok çeşitli farklı komutlar sunar.

Bir curl kullanıcısı, dosya transfer dizisindeki bir adım olarak sunucuya bu tür ek (özel) komutları iletebilir. curl, bu komutların sürecin farklı noktalarında çalıştırılmasını bile teklif eder.

## Quote

Eskiden standart eski ftp istemcisinin *quote* adında bir komutu vardı. Komutları sunucuya kelimesi kelimesine göndermek için kullanılırdı. curl neredeyse aynı işlevsellik için aynı adı kullanır: belirtilen komutu sunucuya kelimesi kelimesine gönderin. Aslında bir veya daha fazla komut. `-Q` veya `--quote`.

Hangi komutların mevcut olduğunu ve bir sunucuya gönderilebileceğini bilmek için, FTP protokolü hakkında biraz bilgi sahibi olmanız ve muhtemelen ayrıntılar için RFC 959'u biraz okumanız gerekir.

Transfer başlamadan **önce** sunucuya basit bir `NOOP` (hiçbir şey yapmaz) göndermek için, curl'e şöyle verin:

    curl -Q NOOP ftp://example.com/file

Bunun yerine aynı komutu transferden hemen **sonra** göndermek için, FTP komutunun önüne bir tire koyun:

    curl -Q -NOOP ftp://example.com/file

curl ayrıca çalışma dizinini değiştirdikten sonra, transferi başlatan **komutlardan hemen önce** komut göndermeyi de teklif eder. O zaman komut göndermek için, komutun önüne bir '+' (artı) koyun.

## Bir komut serisi

Aslında komut satırında birden fazla `-Q` kullanarak üç farklı zamanda da komut gönderebilirsiniz. Ayrıca daha fazla `-Q` seçeneği kullanarak aynı konumda birden fazla komut da gönderebilirsiniz.

Varsayılan olarak, verilen komutlardan herhangi biri sunucudan bir hata döndürürse, curl işlemlerini durdurur, transferi iptal eder (transfer başlamadan önce gerçekleşirse) ve daha fazla özel komut göndermez.

Örnek, bir dosyayı yeniden adlandırın ve ardından bir transfer yapın:

    curl -Q "RNFR original" -Q "RNTO newname" ftp://example.com/newname

## Hata verebilir komutlar

Her şeyin durmasına neden olmadan sunucudan bir hata döndürülmesini sağlamak için, başarısız olmasına izin verilen bireysel quote komutları göndermeyi seçebilirsiniz.

Komutun önüne bir yıldız işareti (`*`) koyarak komutu hata verebilir hale getirirsiniz. Örneğin, bir transferden sonra bir silme (`DELE`) gönderin ve başarısız olmasına izin verin:

    curl -Q "-*DELE file" ftp://example.com/moo
