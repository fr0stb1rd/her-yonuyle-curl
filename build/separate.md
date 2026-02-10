# Ayrı kurulum

Bazen curl ve libcurl'ü kaynaktan derlediğinizde, bunu deneme, test etme veya belki de hata ayıklama amacıyla yaparsınız. Bu senaryolarda, sistem genelindeki libcurl kurulumunuzu değiştirmeye hazır olmayabilirsiniz.

Birçok modern sistemde zaten sistemde kurulu libcurl vardır, bu nedenle test sürümünüzü derleyip kurduğunuzda, amaçlarınız için yeni derlemenizin kullanıldığından emin olmanız gerekir.

Kendi curl ve libcurl sürümünü derleyip kuran ancak daha sonra yeni curl derlemelerini çağırdıklarında yeni aracın sistemde daha eski bir libcurl bulup onun yerine onu kullandığını söyleyen insanlardan çok sayıda rapor alıyoruz. Bu durum kullanıcıların kafasını karıştırma eğilimindedir.

## Statik bağlama

Bunun yerine libcurl ile statik olarak bağlayarak curl'ün daha eski bir dinamik libcurl kütüphanesi bulması sorunundan kaçınabilirsiniz. Ancak bu, bunun yerine bir yığın başka zorluğu tetikler çünkü modern kütüphaneleri birkaç üçüncü taraf bağımlılığıyla statik olarak bağlamak zor bir iştir. Statik olarak bağladığınızda, tüm bağımlılıkları bağlayıcıya (linker) sağladığınızdan emin olmanız gerekir. Bu önerdiğimiz bir yöntem değildir.

## Dinamik bağlama

Modern bir sistemde `curl`ü çağırdığınızda, yürütülebilir dosyanın kullanmak üzere oluşturulduğu paylaşılan kütüphaneleri yükleyen bir çalışma zamanı bağlayıcısı (genellikle `ld.so` olarak adlandırılır) vardır. Paylaşılan kütüphaneler bir dizi yolda (paths) aranır ve yüklenir.

Sorun genellikle sistem libcurl kütüphanesinin o yolda mevcut olması, ancak yeni derlediğiniz libcurl'ün olmamasıdır. Veya her ikisi de yolda mevcuttur ancak önce sistemdeki bulunur.

Çalışma zamanı bağlayıcı yol sırası genellikle Linux sistemlerinde `/etc/ld.so.conf` dosyasında tanımlanır. Sıralamayı değiştirebilir ve aranacak dizinler listesine yeni dizinler ekleyebilirsiniz. Bir güncellemeden sonra `ldconfig` çalıştırmayı unutmayın.

## Geçici kurulumlar

Bir libcurl derlerseniz ve bir yere kurarsanız ve sadece tek bir uygulama için kullanmak isterseniz veya belki de sadece bir şeyi biraz test etmek isterseniz, dinamik kütüphane yolunu düzenlemek ve değiştirmek çok müdahaleci olabilir.

Normal bir unix, önerdiğimiz birkaç başka alternatif sunar.

### `LD_LIBRARY_PATH`

Çalışma zamanı bağlayıcısının belirli bir dizine bakmasını sağlamak için kabuğunuzda bu ortam değişkenini ayarlayabilirsiniz. Bu, bu değişkenin ayarlandığı yerde yüklenen tüm yürütülebilir dosyaları etkiler.

Hızlı kontroller için veya hatta dönüşümlü olarak kullanmak ve tek `curl` yürütülebilir dosyanızın farklı çağrılarda farklı libcurl'ler kullanmasını sağlamak istiyorsanız kullanışlıdır.

Yeni curl derlemenizi `$HOME/install` dizinine kurduğunuzda şöyle görünebilir:

    export LD_LIBRARY_PATH=$HOME/install/lib
    $HOME/install/bin/curl https://example.com/

### `rpath`

Genellikle, sisteminki yerine kendi ayrı libcurl'ünüzü yüklemeye zorlamanın daha iyi bir yolu, derlediğiniz belirli `curl` yürütülebilir dosyasının `rpath`ini ayarlamaktır. Bu, çalışma zamanı bağlayıcısına bu belirli yürütülebilir dosya için kontrol etmesi gereken belirli bir yol verir.

Bu, bağlama zamanında (link time) yapılır ve uygulamanızı kullanarak kendi libcurl'ünüzü derlerseniz, özel libcurl derlemenizi bunun gibi yüklemesini sağlayabilirsiniz:

    gcc -g example.c -L$HOME/install/lib -lcurl -Wl,-rpath=$HOME/install/lib

`rpath` ayarlandığında, `$HOME/install/lib/libcurl.so`ya karşı bağlanan yürütülebilir dosya, çalışma zamanı bağlayıcısının o belirli yolu ve kütüphaneyi kullanmasını sağlarken, sisteminizdeki diğer ikili dosyalar sistem libcurl'ünü kullanmaya devam eder.

Kendi özel `curl` derlemenizin kendi libcurl'ünü kullanmasını istediğinizde ve bunları `$HOME/install` dizinine kurduğunuzda, bunun için bir configure komut satırı şuna benzer:

    LDFLAGS="-Wl,-rpath,$HOME/install/lib" ./configure ...

Sisteminiz rpath'in runpath biçimini destekliyorsa, bunun yerine onu kullanmak genellikle daha iyidir çünkü `LD_LIBRARY_PATH` ortam değişkeni tarafından geçersiz kılınabilir. Ayrıca curl'ün ağaç içi (in-tree) derlemelerini test ederken libtool hatalarını da önleyebilir, çünkü o zaman libtool `LD_LIBRARY_PATH` kullanabilir. Daha yeni bağlayıcılar, rpath belirtildiğinde varsayılan olarak rpath'in runpath biçimini kullanabilir ancak diğerlerinin bunun gibi ek bir bağlayıcı bayrağına `-Wl,--enable-new-dtags` ihtiyacı vardır:

    LDFLAGS="-Wl,-rpath,$HOME/install/lib -Wl,--enable-new-dtags" \
      ./configure ...
