# Bağımlılıklar

İyi yazılım yapmanın anahtarı, diğer harika yazılımların üzerine inşa etmektir. Birçok kişinin kullandığı kütüphaneleri kullanarak, aynı şeyleri daha az kez yeniden icat ederiz ve aynı kodu kullanan daha fazla insan olduğu için daha güvenilir yazılımlar elde ederiz.

curl'ün sağladığı bir yığın özellik, bir veya daha fazla harici kütüphaneyi kullanacak şekilde derlenmesini gerektirir. Bunlar o zaman curl'ün bağımlılıklarıdır. Hiçbiri *gerekli* değildir ancak çoğu kullanıcı en azından bazılarını kullanmak ister.

## HTTP Sıkıştırma

curl, uygun 3. taraf kütüphanelerle derlenirse HTTP üzerinden aktarılan verilerin otomatik olarak açılmasını (decompression) yapabilir. curl'ü bu kütüphanelerden birini veya daha fazlasını kullanacak şekilde derleyebilirsiniz:

 - [zlib](https://zlib.net/) ile gzip sıkıştırması
 - [brotli](https://github.com/google/brotli) ile brotli sıkıştırması
 - [libzstd](https://github.com/facebook/zstd) ile zstd sıkıştırması

Sıkıştırılmış verileri kablo üzerinden almak daha az bant genişliği kullanır, bu da daha kısa aktarım sürelerine neden olabilir.

## c-ares

<https://c-ares.org/>

curl, asenkron isim çözümlemesi yapabilmek için c-ares ile derlenebilir. Asenkron isim çözümlemesini etkinleştirmenin bir başka seçeneği de, curl'ü iş parçacıklı isim çözümleyici arka ucuyla (threaded name resolver backend) derlemektir; bu, her isim çözümlemesi için ayrı bir yardımcı iş parçacığı oluşturur. c-ares hepsini aynı iş parçacığı içinde yapar.

## nghttp2

<https://nghttp2.org/>

Bu, HTTP/2 çerçevelemesini (framing) işlemek için bir kütüphanedir ve curl'ün HTTP sürüm 2'yi desteklemesi için bir ön koşuldur.

## openldap

<https://www.openldap.org/>

Bu kütüphane, curl'ün LDAP ve LDAPS URL şemaları için destek almasına izin veren bir seçenektir. Windows'ta, curl'ü winldap kütüphanesini kullanacak şekilde derlemeyi de tercih edebilirsiniz.

## librtmp

<https://rtmpdump.mplayerhq.hu/>

curl'ün RTMP URL şeması desteğini etkinleştirmek için, curl'ü RTMPDump projesinden gelen librtmp kütüphanesiyle derlemelisiniz.

## libpsl

<https://rockdaboot.github.io/libpsl/>

curl'ü libpsl desteğiyle derlediğinizde, çerez ayrıştırıcı Public Suffix List (Kamu Sonek Listesi) hakkında bilgi sahibi olur ve bu tür çerezleri uygun şekilde işler.

## libidn2

<https://www.gnu.org/software/libidn/libidn2/manual/libidn2.html>

curl, Uluslararası Alan Adlarını (IDN) libidn2 kütüphanesinin yardımıyla işler.

## SSH kütüphaneleri

curl'ün SCP ve SFTP desteğine sahip olmasını istiyorsanız, bu SSH kütüphanelerinden biriyle derleyin:

- [libssh2](https://libssh2.org/)
- [libssh](https://www.libssh.org/)
- [wolfSSH](https://www.wolfssl.com/products/wolfssh/)

## TLS kütüphaneleri

Aralarından seçim yapabileceğiniz birçok farklı TLS kütüphanesi vardır, bu yüzden bunlar [ayrı bir bölümde](tls.md) ele alınmıştır.

## QUIC ve HTTP/3

curl'ü HTTP/3 desteğiyle derlemek için şu setlerden birine ihtiyacınız vardır:

- [ngtcp2](https://github.com/ngtcp2/ngtcp2) + [nghttp3](https://github.com/ngtcp2/nghttp3)
- [quiche](https://github.com/cloudflare/quiche) (**deneysel**)
- [msquic](https://github.com/microsoft/msquic) + [msh3](https://github.com/nibanks/msh3) (**deneysel**)
