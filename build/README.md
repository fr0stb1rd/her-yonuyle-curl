# curl ve libcurl derleme

Bu projenin kaynak kodu, mümkün olduğunca az kısıtlama ve gereksinimle hemen hemen her işletim sisteminde ve platformda derlenmesine ve oluşturulmasına izin verecek şekilde yazılmıştır.

32 bit (veya daha büyük) bir CPU mimarisine sahipseniz, C89 uyumlu bir derleyiciniz varsa ve kabaca POSIX destekleyen bir soket API'niz varsa, o zaman muhtemelen hedef sisteminiz için curl ve libcurl derleyebilirsiniz.

En popüler platformlar için curl projesi, kendi başınıza kolayca derlemenize izin vermek için zaten yapılmış ve hazırlanmış derleme sistemleriyle birlikte gelir.

Ayrıca curl ve libcurl'ün ikili (binary) paketlerini bir araya getiren ve bunları indirmeye sunan dost canlısı insanlar ve kuruluşlar da vardır. Farklı seçenekler aşağıda incelenmiştir.

## En son sürüm?

[curl web sitesine](https://curl.se) bakarak projeden yayınlanan en son curl ve libcurl sürümünü görebilirsiniz. Bu, alabileceğiniz en son kaynak kodu sürüm paketidir.

İşletim sisteminiz veya tercih ettiğiniz dağıtım için önceden oluşturulmuş ve paketlenmiş bir sürümü tercih ettiğinizde, her zaman en son sürümü bulamayabilirsiniz, ancak birisinin ortamınız için paketlediği en son sürümle yetinmeniz veya kaynaktan kendiniz derlemeniz gerekebilir.

curl projesi ayrıca şu URL'de biraz daha makine tarafından okunabilir bir formatta en son sürüm hakkında bilgi sağlar: `https://curl.se/info`.

## Sürüm (Releases) kaynak kodu

curl projesi, iki ürün olan curl ve libcurl'ü üretmek için derlenebilen kaynak kodu oluşturur. Kaynak kodundan ikili dosyalara (binaries) dönüştürme işlemine genellikle "derleme" (building) denir. curl ve libcurl'ü kaynaktan derlersiniz.

curl projesi herhangi bir derlenmiş ikili dosya sağlamaz — sadece kaynak kodunu gönderir. curl web sitesinin indirme sayfasında bulunan ve İnternet'teki diğer yerlerden yüklenen ikili dosyaların tümü, diğer dost canlısı insanlar ve kuruluşlar tarafından derlenmiş ve dünyaya sunulmuştur.

Kaynak kodu, C kodu içeren çok sayıda dosyadan oluşur. Genel olarak konuşursak, curl'ün desteklediği tüm platformlar ve bilgisayar mimarileri için ikili dosyalar oluşturmak üzere aynı dosya seti kullanılır. curl çok sayıda platformda derlenebilir ve çalıştırılabilir. Nadir bir işletim sistemi kullanıyorsanız, curl'ü kaynaktan derlemek, curl'ü edinmenin en kolay veya belki de tek yolu olabilir.

Her zaman başarılı olamasak da, curl'ü derlemeyi kolaylaştırmak curl projesi için bir önceliktir.

## git vs sürüm tarball'ları

Sürüm tarball'ları oluşturulduğunda, birkaç dosya oluşturulur ve son sürüm paketine dahil edilir. Bu oluşturulan dosyalar git deposunda mevcut değildir, çünkü bunlar oluşturulmuştur ve bunları git'te saklamaya gerek yoktur.

Elbette, [git deposunda](https://github.com/curl/curl) bulunan en son sürümü derlemeyi de tercih edebilirsiniz. Ancak bu biraz daha kırılgandır ve muhtemelen ayrıntılara biraz daha fazla dikkat gerektirir.

curl'ü bir git checkout'undan derlerseniz, derlemeden önce bazı dosyaları kendiniz oluşturmanız gerekir. Linux ve Unix benzeri sistemlerde bunu `autoreconf -fi` çalıştırarak, Windows'ta ise `buildconf.bat` çalıştırarak yapın.

## Linux ve Unix benzeri sistemlerde

Linux ve diğer Unix benzeri sistemlerde curl derlemenin belirgin şekilde iki farklı yolu vardır; biri [configure betiğini](autotools.md) kullanan yol, diğeri ise [CMake yaklaşımıdır](cmake.md).

İnsanların farklı görüşlerine ve zevklerine hitap etmek için iki farklı derleme ortamı vardır. Configure tabanlı derleme, tartışmasız daha olgun ve daha kapsamlı derleme sistemidir ve muhtemelen varsayılan olarak kabul edilmelidir.

## Windows'ta

Windows'ta derleme yapmanın en az dört farklı yolu vardır. Yukarıda belirtilen yollar, [CMake yaklaşımı](cmake.md) ve msys ile [configure](autotools.md) kullanmak işe yarar, ancak daha popüler ve yaygın yöntemler muhtemelen Microsoft'un Visual Studio derleyicisini `nmake` veya proje dosyaları kullanarak derlemektir. [windows](windows.md) üzerinde derleme bölümüne bakın.

## Daha fazlasını öğrenin

* [Autotools](autotools.md) - configure ile derleme
* [CMake](cmake.md)
* [Ayrı kurulum (Separate install)](separate.md)
* [Windows'ta](windows.md) - Windows'a özgü derleme yolları
* [Bağımlılıklar](deps.md)
* [TLS kütüphaneleri](tls.md)
