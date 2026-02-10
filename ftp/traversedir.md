# Dizin dolaşma

Uzak dosya sistemini dolaşmak için FTP komutları yaparken, curl'ün hedef dosyaya, kullanıcının aktarmak istediği dosyaya ulaşmak için izleyebileceği birkaç farklı yol vardır.

## multicwd

curl, dosya ağacı hiyerarşisindeki her bir dizin için bir dizin değiştirme (CWD) komutu yapabilir. Tam yol `one/two/three/file.txt` ise, bu yöntem `file.txt` dosyasının aktarılmasını istemeden önce üç `CWD` komutu yapmak anlamına gelir. Bu yöntem, yol birçok seviye derinliğindeyse oldukça fazla sayıda komut oluşturur. Bu yöntem erken bir spesifikasyon (RFC 1738) tarafından zorunlu kılınmıştır ve curl varsayılan olarak böyle davranır:

    curl --ftp-method multicwd ftp://example.com/one/two/three/file.txt

Bu daha sonra şu FTP komut/yanıt dizisine eşittir (basitleştirilmiş):

    > CWD one
    < 250 OK. Current directory is /one
    > CWD two
    < 250 OK. Current directory is /one/two
    > CWD three
    < 250 OK. Current directory is /one/two/three
    > RETR file.txt

## nocwd

Her dizin parçası için bir CWD yapmanın tersi, dizini hiç değiştirmemektir. Bu yöntem, tüm yolu kullanarak sunucuya bir kerede istekte bulunur ve bu nedenle hızlıdır. Ara sıra sunucuların bununla ilgili bir sorunu olur ve tamamen standartlara uygun değildir:

    curl --ftp-method nocwd ftp://example.com/one/two/three/file.txt

Bu daha sonra şu FTP komut/yanıt dizisine eşittir (basitleştirilmiş):

    > RETR one/two/three/file.txt

## singlecwd

Bu, diğer iki FTP yönteminin arasındadır. Bu, hedef dizine tek bir `CWD` komutu yapar ve ardından verilen dosyayı ister:

    curl --ftp-method singlecwd ftp://example.com/one/two/three/file.txt

Bu daha sonra şu FTP komut/yanıt dizisine eşittir (basitleştirilmiş):

    > CWD one/two/three
    < 250 OK. Current directory is /one/two/three
    > RETR file.txt
