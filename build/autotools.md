# Autotools

Autotools, `configure` betiğini oluşturmak için birlikte kullanılan farklı araçlardan oluşan bir koleksiyondur. Configure betiği, curl derlemek isteyen kullanıcı tarafından çalıştırılır ve bir sürü şey yapar:

 - Sisteminizde bulunan özellikleri ve işlevleri kontrol eder.

 - Bir derleyici (builder) olarak derlemede neyi etkinleştireceğinize ve devre dışı bırakacağınıza karar verebilmeniz için komut satırı seçenekleri sunar. Özellikler ve protokoller vb., hatta derleyici uyarı seviyeleri ve daha fazlası açılıp kapatılabilir.

 - Derleyicinin (builder), curl'ün kullanmak üzere derlenebileceği çeşitli üçüncü taraf bağımlılıkları için belirli kurulum yollarını işaret etmesine izin veren komut satırı seçenekleri sunar.

 - Sonuçta derleme yapıldığında ve `make install` çağrıldığında oluşturulan kurulumun hangi dosya yoluna yerleştirileceğini belirtir.

En temel kullanımda, kaynak dizininde sadece `./configure` çalıştırmak yeterlidir. Betik tamamlandığında, algıladığı/etkinleştirdiği seçeneklerin ve hala devre dışı olan özelliklerin bir özetini verir; bunlardan bazıları muhtemelen bu işlevlerin çalışması için gereken gerekli üçüncü taraf bağımlılıklarının varlığını algılayamadığı içindir. Özet beklediğiniz gibi değilse, configure'u yeni seçeneklerle veya daha önce kullanılan seçenekleri ayarlayarak tekrar çağırın.

Configure tamamlandıktan sonra, her şeyi derlemek için `make` komutunu ve son olarak curl, libcurl ve ilgili şeyleri kurmak için `make install` komutunu çağırırsınız. `make install`, sisteminizde kurulum dizininde dosya oluşturmak ve yazmak için doğru haklara sahip olmanızı gerektirir, aksi takdirde bir hata görüntülenir.

## Çapraz derleme (Cross-compiling)

Çapraz derleme, kaynağı bir mimaride derlediğiniz ancak çıktının farklı bir mimaride çalıştırılmak üzere oluşturulduğu anlamına gelir. Örneğin, kaynağı bir Linux makinesinde derleyebilir ancak çıktının bir Windows makinesinde çalışmasını sağlayabilirsiniz.

Çapraz derlemenin çalışması için, derlemek istediğiniz belirli hedef sistem için özel bir derleyici ve derleme sistemi kurulumuna ihtiyacınız vardır. Bu sistemin nasıl edinileceği ve kurulacağı bu kitapta ele alınmamaktadır.

Bir çapraz derleyiciniz olduğunda, configure'a curl derlerken yerel (native) derleyici yerine o derleyiciyi kullanmasını söyleyebilirsiniz, böylece sonuç diğer makineye taşınabilir ve orada kullanılabilir.

## Statik bağlama (Static linking)

Varsayılan olarak, configure derleme dosyalarını, aşağıdaki 'make' komutunun libcurl'ün hem paylaşılan hem de statik sürümlerini oluşturacağı şekilde ayarlar. Bunu configure'a `--disable-static` veya `--disable-shared` seçeneklerini vererek değiştirebilirsiniz.

Paylaşılan kütüphaneler yerine üçüncü taraf kütüphanelerin statik sürümleriyle derlemek isterseniz, kendinizi yokuş yukarı bir savaşa hazırlamanız gerekir. curl'ün configure betiği, paylaşılan kütüphanelerle kurulum yapmaya ve derlemeye odaklanmıştır.

Statik bir kütüphane ile bağlama ile paylaşılan bir kütüphane ile bağlama arasındaki farklardan biri, paylaşılan kütüphanelerin kendi bağımlılıklarını nasıl ele aldığı, statik olanların ise almadığıdır. `xyz` kütüphanesini paylaşılan bir kütüphane olarak bağlamak için, `xyz`'nin kendisinin kullanmak üzere oluşturulduğu diğer kütüphaneler ne olursa olsun, bağlayıcı (linker) komut satırına `-lxyz` eklemek temel olarak yeterlidir. Ancak, eğer bu `xyz` bunun yerine statik bir kütüphaneyse, `xyz`'nin her bir bağımlılığını da bağlayıcı komut satırında belirtmemiz gerekir. curl'ün configure betiği, birlikte derlenebileceği tüm kütüphaneler için tüm olası bağımlılıklara ayak uyduramaz veya bunları bilemez, bu nedenle statik kütüphanelerle derlemek isteyen kullanıcıların çoğunlukla bağlanacak kütüphanelerin listesini sağlaması gerekir.

## TLS arka ucunu seçin

Configure tabanlı derleme, kullanıcıya derleme sırasında çok çeşitli farklı TLS kütüphaneleri arasından seçim yapma olanağı sunar. Doğru komut satırı seçeneklerini kullanarak bunları seçersiniz. curl 7.77.0'dan önce, configure betiği OpenSSL'i otomatik olarak kontrol ederdi, ancak modern sürümler etmez.

 - AmiSSL: `--with-amissl`
 - AWS-LC: `--with-openssl`
 - BearSSL: `--with-bearssl`
 - BoringSSL: `--with-openssl`
 - GnuTLS: `--with-gnutls`
 - LibreSSL: `--with-openssl`
 - mbedTLS: `--with-mbedtls`
 - OpenSSL: `--with-openssl`
 - Rustls: `--with-rustls` (rustls-ffi kurulum yolunu gösterin)
 - Schannel: `--with-schannel`
 - Secure Transport: `--with-secure-transport`
 - wolfSSL: `--with-wolfssl`

Hangi TLS kütüphanesinin kullanılacağını belirtmezseniz, configure betiği başarısız olur. TLS desteği *olmadan* derlemek isterseniz, bunu `--without-ssl` ile açıkça istemeniz gerekir.

Bu `--with-*` seçenekleri, configure'un belirli kütüphaneyi söylediğiniz yerde araması için kurulum önekini (install prefix) sağlamanıza da olanak tanır. Şunun gibi:

    ./configure --with-gnutls=/home/user/custom-gnutls

Configure komut satırında birden fazla `--with-*` seçeneği belirterek **birden fazla** TLS kütüphanesi desteğiyle derlemeyi seçebilirsiniz. `--with-default-ssl-backend=[ISIM]` ile hangisinin varsayılan TLS arka ucu olacağını seçin. Örneğin, hem GnuTLS hem de OpenSSL desteğiyle derleyin ve OpenSSL'i varsayılan yapın:

    ./configure --with-openssl --with-gnutls \
      --with-default-ssl-backend=openssl

## SSH arka ucunu seçin

Configure tabanlı derleme, kullanıcıya derleme sırasında çeşitli farklı SSH kütüphaneleri arasından seçim yapma olanağı sunar. Doğru komut satırı seçeneklerini kullanarak bunları seçersiniz.

 - libssh2: `--with-libssh2`
 - libssh: `--with-libssh`
 - wolfSSH: `--with-wolfssh`

Bu `--with-*` seçenekleri, configure'un belirli kütüphaneyi söylediğiniz yerde araması için kurulum önekini sağlamanıza da olanak tanır. Şunun gibi:

    ./configure --with-libssh2=/home/user/custom-libssh2

## HTTP/3 arka ucunu seçin

Configure tabanlı derleme, kullanıcıya derleme sırasında farklı HTTP/3 kütüphaneleri arasından seçim yapma olanağı sunar. Doğru komut satırı seçeneklerini kullanarak bunları seçersiniz.

 - quiche: `--with-quiche`
 - ngtcp2: `--with-ngtcp2 --with-nghttp3`
 - msh3: `--with-msh3`
