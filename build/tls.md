# TLS kütüphaneleri

curl'ün HTTPS, FTPS, SMTPS, POP3S, IMAPS ve daha fazlası gibi TLS tabanlı protokolleri desteklemesini sağlamak için, curl TLS protokolünü kendisi uygulamadığından, üçüncü taraf bir TLS kütüphanesi ile derlemeniz gerekir.

curl, çok sayıda TLS kütüphanesi ile çalışmak üzere yazılmıştır:

 - AmiSSL
 - AWS-LC
 - BearSSL
 - BoringSSL
 - GnuTLS
 - libressl
 - mbedTLS
 - OpenSSL
 - rustls
 - Schannel (yerel Windows)
 - Secure Transport (yerel macOS)
 - WolfSSL

curl ve libcurl'ü bu kütüphanelerden birini kullanacak şekilde derlediğinizde, kütüphanenin ve include başlıklarının derleme makinenizde kurulu olması önemlidir.

## configure

Aşağıda, configure'a farklı kütüphaneleri kullanmasını nasıl söyleyeceğinizi öğrenirsiniz. Configure betiği varsayılan olarak herhangi bir TLS kütüphanesi seçmez. Bir tane seçmelisiniz veya `--without-ssl` kullanarak configure'a TLS desteği olmadan derlemek istediğinizi belirtmelisiniz.

### OpenSSL, BoringSSL, libressl

    ./configure --with-openssl

configure varsayılan olarak OpenSSL'i varsayılan yolunda algılar. İsteğe bağlı olarak configure'a OpenSSL'i bulabileceği özel bir kurulum yolu öneki gösterebilirsiniz:

    ./configure --with-openssl=/home/user/installed/openssl

Alternatifler [BoringSSL](boringssl.md) ve libressl, configure'un onları OpenSSL ile aynı şekilde algılayacağı kadar benzer görünür. Daha sonra belirli türlerden hangisini kullandığını anlamak için ek önlemler kullanır.

### GnuTLS

    ./configure --with-gnutls

configure varsayılan olarak GnuTLS'i varsayılan yolunda algılar. İsteğe bağlı olarak configure'a gnutls'i bulabileceği özel bir kurulum yolu öneki gösterebilirsiniz:

    ./configure --with-gnutls=/home/user/installed/gnutls

### WolfSSL

    ./configure --with-wolfssl

configure varsayılan olarak WolfSSL'i varsayılan yolunda algılar. İsteğe bağlı olarak configure'a WolfSSL'i bulabileceği özel bir kurulum yolu öneki gösterebilirsiniz:

    ./configure --with-wolfssl=/home/user/installed/wolfssl

### mbedTLS

    ./configure --with-mbedtls

configure varsayılan olarak mbedTLS'i varsayılan yolunda algılar. İsteğe bağlı olarak configure'a mbedTLS'i bulabileceği özel bir kurulum yolu öneki gösterebilirsiniz:

    ./configure --with-mbedtls=/home/user/installed/mbedtls

### Secure Transport

    ./configure --with-secure-transport

configure varsayılan olarak Secure Transport'u varsayılan yolunda algılar. İsteğe bağlı olarak configure'a Secure Transport'u bulabileceği özel bir kurulum yolu öneki gösterebilirsiniz:

    ./configure --with-secure-transport=/home/user/installed/darwinssl

### Schannel

    ./configure --with-schannel

configure varsayılan olarak Schannel'i varsayılan yolunda algılar.

(WinSSL daha önce Schannel için alternatif bir isimdi ve önceki curl sürümleri bunun yerine `--with-winssl` gerektiriyordu)

### BearSSL

    ./configure --with-bearssl

configure varsayılan olarak BearSSL'i varsayılan yolunda algılar. İsteğe bağlı olarak configure'a BearSSL'i bulabileceği özel bir kurulum yolu öneki gösterebilirsiniz:

    ./configure --with-bearssl=/home/user/installed/bearssl

### Rustls

    ./configure --with-rustls

rustls kullanması söylendiğinde, curl aslında rustls kütüphanesi için C API'si olan rustls-ffi kütüphanesini bulmaya ve kullanmaya çalışır. configure varsayılan olarak rustls-ffi'yi varsayılan yolunda algılar. İsteğe bağlı olarak configure'a rustls-ffi'yi bulabileceği özel bir kurulum yolu öneki gösterebilirsiniz:

    ./configure --with-rustls=/home/user/installed/rustls-ffi
