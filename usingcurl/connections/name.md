# İsim çözümleme hileleri

curl, normalde bağlanacağı ana bilgisayardan başka bir ana bilgisayarı kullanmasını sağlamak için birçok yol sunar.

## hosts dosyasını düzenleyin

Belki de `curl http://example.com` komutunun gerçek sunucu yerine yerel sunucunuza bağlanmasını istiyorsunuz.

Bunu normalde ve kolayca `hosts` dosyanızı (Linux ve Unix benzeri sistemlerde `/etc/hosts`) düzenleyerek ve örneğin ana bilgisayarı localhost'unuza yönlendirmek için `127.0.0.1 example.com` ekleyerek yapabilirsiniz. Ancak bu düzenleme yönetici erişimi gerektirir ve aynı anda diğer tüm uygulamaları etkilemesi gibi bir dezavantajı vardır.

## Host: başlığını değiştirin

`Host:` başlığı, bir HTTP istemcisinin HTTP sunucusuna hangi sunucuyla konuştuğunu söylemesinin normal yoludur, çünkü tipik olarak bir HTTP sunucusu aynı yazılım örneğini kullanarak birçok farklı isme hizmet eder.

Böylece, özel olarak değiştirilmiş bir `Host:` başlığı geçirerek, aslında o ana bilgisayar adına bağlanmadığınızda bile sunucunun sitenin içeriğiyle yanıt vermesini sağlayabilirsiniz.

Örneğin, ana siteniz `www.example.com`'un bir test örneğini yerel makinenizde çalıştırıyorsunuz ve curl'ün dizin html'ini istemesini istiyorsunuz:

    curl -H "Host: www.example.com" http://localhost/

Özel bir `Host:` başlığı ayarlayıp çerezleri kullanırken, curl özel adı çıkarır ve çerezleri gönderirken eşleştirmek için bunu ana bilgisayar olarak kullanır.

`Host:` başlığı bir HTTPS sunucusuyla iletişim kurarken yeterli değildir. HTTPS ile TLS protokolünde SNI (Server Name Indication - Sunucu Adı Göstergesi) adı verilen ve istemcinin sunucuya konuşmak istediği sunucunun adını söylemesini sağlayan ayrı bir uzantı alanı vardır. curl yalnızca verilen URL'den gönderilecek SNI adını çıkarır.

## Bir isim için özel bir IP adresi sağlayın

curl'ün nereye gitmesi gerektiğini isim çözümleyiciden daha mı iyi biliyorsunuz? O zaman curl'e kendiniz bir IP adresi verebilirsiniz. `example.com` için 80. port erişimini bunun yerine localhost'unuza ulaşacak şekilde yönlendirmek istiyorsanız:

    curl --resolve example.com:80:127.0.0.1 http://example.com/

Hatta bu türden birden fazla yönlendirme sağlamak için birden fazla `--resolve` anahtarı belirtebilirsiniz; bu, çalıştığınız URL HTTP yönlendirmeleri kullanıyorsa veya komut satırınızın birden fazla URL ile çalışmasını istiyorsanız kullanışlı olabilir.

`--resolve`, adresi curl'ün DNS önbelleğine ekler, bu nedenle etkili bir şekilde curl'ü, adı çözümlediğinde aldığı adresin bu olduğuna inandırır.

HTTPS konuşurken, bu URL'deki ad için SNI gönderir ve curl, URL'deki ad için hizmet verdiğinden emin olmak üzere sunucunun yanıtını doğrular.

Seçenekte belirttiğiniz desenin bir ana bilgisayar adı ve buna karşılık gelen port numarası olması gerekir ve yalnızca URL'de tam olarak o çift kullanılırsa adres değiştirilir. Örneğin, bir HTTPS URL'sindeki bir ana bilgisayar adını varsayılan port numarasında değiştirmek istiyorsanız, curl'e bunun 443. port için olduğunu söylemeniz gerekir, şöyle:

    curl --resolve example.com:443:192.168.0.1 https://example.com/

## Bir yedek isim sağlayın

`--resolve` seçeneğinin yakın bir akrabası olarak, `--connect-to` seçeneği küçük bir varyasyon sağlar. Belirli bir isim ve port numarası bağlanmak için kullanıldığında curl'ün kaputun altında kullanması için bir yedek isim ve port numarası belirtmenize olanak tanır.

Örneğin, yük dengeleme amacıyla aslında üç farklı bireysel HTTP sunucusu (load1, load2 ve load3) tarafından sunulan `www.example.com` adında tek bir siteniz olduğunu varsayalım. Tipik bir normal prosedürde, curl ana siteyi çözer ve yük dengeli sunuculardan biriyle konuşur (geri bir liste alır ve sadece birini seçer) ve her şey yolundadır. Yük dengeli setten belirli bir sunucuya (`load1.example.com` örneğin) bir test isteği göndermek istiyorsanız, curl'e bunu yapması talimatını verebilirsiniz.

load1'in belirli IP adresini biliyorsanız bunu başarmak için hala `--resolve` kullanabilirsiniz. Önce IP adresini ayrı ayrı çözüp düzeltmek zorunda kalmadan, curl'e şunları söyleyebilirsiniz:

    curl --connect-to www.example.com:80:load1.example.com:80 \
      http://www.example.com

KAYNAK İSMİ + KAYNAK PORTU'ndan HEDEF İSMİ + HEDEF PORTU'na yönlendirir. curl daha sonra `load1.example.com` adını çözer ve bağlanır, ancak diğer tüm yönlerden hala `www.example.com` ile konuştuğunu varsayar.

## c-ares ile isim çözümleme hileleri

Bu kitabın başka bir yerinde ayrıntılandırılması gerektiği gibi, curl birkaç farklı isim çözümleme arka ucuyla derlenebilir. Bu arka uçlardan biri c-ares kütüphanesi tarafından desteklenmektedir ve curl c-ares kullanacak şekilde derlendiğinde, diğer isim çözümleme arka uçlarını kullanacak şekilde derlenen curl'ün elde edemediği birkaç ekstra süper güç elde eder. Yani, hangi DNS sunucularının kullanılacağını ve bu DNS trafiğinin ağı nasıl kullandığını daha spesifik olarak talimat verme yeteneği kazanır.

`--dns-servers` ile, varsayılan yerine curl'ün tam olarak hangi DNS sunucusunu kullanması gerektiğini belirtebilirsiniz. Bu, farklı yanıt veren kendi deneysel sunucunuzu çalıştırmanıza veya normal sunucunuz güvenilmez veya ölü ise bir yedek kullanmanıza olanak tanır.

`--dns-ipv4-addr` ve `--dns-ipv6-addr` ile curl'den DNS iletişiminin yerel ucunu belirli bir IP adresine "bağlamasını" (bind) istersiniz ve `--dns-interface` ile curl'e DNS istekleri için kullanacağı belirli bir ağ arayüzünü kullanması talimatını verebilirsiniz.

Bu `--dns-*` seçenekleri gelişmiştir ve yalnızca ne yaptıklarını bilen ve bu seçeneklerin ne yaptığını anlayan kişiler içindir. Özelleştirilebilir DNS isim çözümleme işlemleri sunarlar.
