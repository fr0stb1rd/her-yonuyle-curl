# Kod düzeni

curl kaynak kodu ağacı ne büyük ne de karmaşıktır. Hatırlanması gereken önemli bir şey, libcurl'ün kütüphane olduğu ve bu kütüphanenin curl komut satırı aracının en büyük bileşeni olduğudur.

## kök (root)

Kaynak ağacı kökündeki dosya sayısını minimumda tutmaya çalışıyoruz. Bir sürüm arşivini git deposunda saklananla karşılaştırırsanız, sürüm komut dosyaları (scripts) tarafından birkaç dosya oluşturulduğundan dosyalarda küçük bir fark görebilirsiniz.

Daha dikkate değer olanlardan bazıları şunlardır:

- `buildconf`: (kullanımdan kaldırıldı) git deposundan kaynağı kullanarak curl derlerken yapılandırma (configure) ve daha fazlasını oluşturmak için kullanılan komut dosyası.
- `buildconf.bat`: buildconf'un Windows sürümü. Tam kaynak kodunu git'ten çektikten (checkout) sonra bunu çalıştırın.
- `CHANGES`: sürümde oluşturulur ve sürüm arşivine konur. Kaynak deposundaki en son 1000 değişikliği içerir.
- `configure`: curl derlerken bir kurulum oluşturmak için Unix benzeri sistemlerde kullanılan oluşturulmuş bir komut dosyası.
- `COPYING`: kodu kullanmanızla ilgili kuralları detaylandıran lisans.
- `GIT-INFO`: sadece git'te bulunur ve kodu git'ten çektikten sonra curl'ün nasıl derleneceği hakkında bilgi içerir.
- `maketgz`: sürüm arşivleri ve günlük anlık görüntüler (snapshots) üretmek için kullanılan komut dosyası.
- `README`: curl ve libcurl'ün ne olduğuna dair kısa bir özet.
- `RELEASE-NOTES`: en son sürüm için yapılan değişiklikleri içerir; git'te bulunduğunda, önceki sürümden bu yana yapılan ve gelecek sürüme girmesi hedeflenen değişiklikleri içerir.

## lib

Bu dizin, libcurl için tam kaynak kodunu içerir. Tüm platformlar için aynı kaynak kodudur—yüzden fazla C kaynak dosyası ve birkaç tane daha özel başlık dosyası. libcurl'e karşı uygulamalar derlenirken kullanılan başlık dosyaları bu dizinde saklanmaz; onlar için `include/curl` dizinine bakın.

Kendi derlemenizde hangi özelliklerin etkinleştirildiğine ve platformunuzun hangi işlevleri sağladığına bağlı olarak, kaynak dosyaların bazıları veya kaynak dosyaların bölümleri, sizin özel derlemenizde kullanılmayan kodlar içerebilir.

## lib/vtls

libcurl içindeki VTLS alt bölümü, libcurl'ün desteklemek üzere derlenebileceği tüm TLS arka uçlarının evidir. "Sanal" (virtual) TLS dahili API'si, ana kodun hangi özel TLS kütüphanesinin kullanıldığını bilmeden TLS ve kripto işlevlerine erişmek için dahili olarak kullanılan, arka uçtan bağımsız bir API'dir. Bu, libcurl'ü derleyen kişinin derleme yapmak için çok çeşitli TLS kütüphaneleri arasından seçim yapmasına olanak tanır.

Kullanıcılara yardımcı olmak için web sitesinde bir [SSL karşılaştırma tablosu](https://curl.se/docs/ssl-compared.html) da tutuyoruz.

- AmiSSL: AmigaOS için yapılmış bir OpenSSL çatalı (`openssl.c` kullanır)
- BearSSL
- BoringSSL: Google tarafından bakımı yapılan bir OpenSSL çatalı. (`openssl.c` kullanır)
- GnuTLS
- LibreSSL: OpenBSD ekibi tarafından bakımı yapılan bir OpenSSL çatalı. (`openssl.c` kullanır)
- mbedTLS
- OpenSSL
- rustls: rust ile yazılmış bir TLS kütüphanesi
- Schannel: Windows üzerindeki yerel (native) TLS kütüphanesi.
- Secure Transport: macOS üzerindeki yerel (native) TLS kütüphanesi
- wolfSSL

## src

Bu dizin, curl komut satırı aracı için kaynak kodunu tutar. Aracı çalıştıran tüm platformlar için aynı kaynak kodudur.

Komut satırı aracının yaptığı şeylerin çoğu, verilen komut satırı seçeneklerini karşılık gelen libcurl seçeneklerine veya seçenek setine dönüştürmek ve ardından kullanıcının isteklerine göre ağ transferini yönlendirmek için bunları doğru bir şekilde verdiğinden emin olmaktır.

Bu kod, libcurl'ü tıpkı diğer herhangi bir uygulamanın yaptığı gibi kullanır.

## include/curl

Burada libcurl kullanan uygulamalar için sağlanan halka açık başlık dosyaları bulunmaktadır. Bazıları yapılandırma (configure) veya sürüm sırasında oluşturulur, bu nedenle git deposunda bir sürüm arşivinde göründükleri gibi görünmezler.

Modern libcurl ile, bir uygulamanın C kaynak koduna dahil etmesi beklenen tek şey `#include <curl/curl.h>` satırıdır.

## docs

Ana dokümantasyon konumu. Bu dizindeki metin dosyaları tipik olarak düz metin dosyalarıdır. Yavaş yavaş Markdown formatına geçmeye başladık, bu nedenle birkaç (ancak artan sayıda) dosya bunu belirtmek için `.md` uzantısını kullanıyor.

Bu belgelerin çoğu curl web sitesinde de otomatik olarak metinden web dostu bir formata/görünüme dönüştürülerek gösterilir.

- `BINDINGS`: bilinen tüm libcurl dil bağlayıcılarını ve bunların nerede bulunacağını listeler
- `BUGS`: hataların nasıl ve nereye bildirileceği
- `CODE_OF_CONDUCT.md`: bu projede insanların nasıl davranmasını beklediğimiz
- `CONTRIBUTE`: projeye katkıda bulunurken nelere dikkat edilmeli
- `curl.1`: nroff formatında curl komut satırı aracı kılavuz (man) sayfası
- `curl-config.1`: nroff formatında curl-config kılavuz sayfası
- `FAQ`: curl ile ilgili çeşitli konular hakkında sıkça sorulan sorular
- `FEATURES`: curl özelliklerinin eksik bir listesi
- `HISTORY`: projenin nasıl başladığını ve yıllar içinde nasıl geliştiğini açıklar
- `HTTP2.md`: curl ve libcurl ile HTTP/2 kullanımı
- `HTTP-COOKIES`: curl HTTP çerezlerini (cookies) nasıl destekler ve onlarla nasıl çalışır
- `index.html`: dokümantasyon dizin sayfası olarak temel bir HTML sayfası
- `INSTALL`: curl ve libcurl'ün kaynaktan nasıl derleneceği ve kurulacağı
- `INSTALL.cmake`: CMake ile curl ve libcurl nasıl derlenir
- `INSTALL.devcpp`: devcpp ile curl ve libcurl nasıl derlenir
- `INTERNALS`: curl ve libcurl iç yapılarını detaylandırır
- `KNOWN_BUGS`: bilinen hatalar ve sorunların listesi
- `LICENSE-MIXING`: farklı üçüncü taraf modüllerinin ve bunların bireysel lisanslarının nasıl birleştirileceğini açıklar
- `MAIL-ETIQUETTE`: posta listelerimizde nasıl iletişim kurulacağı
- `MANUAL`: curl'ün nasıl kullanılacağına dair öğretici benzeri bir rehber
- `mk-ca-bundle.1`: nroff formatında mk-ca-bundle aracı kılavuz sayfası
- `README.cmake`: CMake ayrıntıları
- `README.netware`: Netware ayrıntıları
- `README.win32`: win32 ayrıntıları
- `RELEASE-PROCEDURE`: bir curl ve libcurl sürümü nasıl yapılır
- `RESOURCES`: curl'ün neyi, neden ve nasıl yaptığına dair daha fazla okuma için ek kaynaklar
- `ROADMAP.md`: gelecekte üzerinde çalışmak istediğimiz şeyler
- `SECURITY`: güvenlik açıkları üzerinde nasıl çalıştığımız
- `SSLCERTS`: TLS sertifika işleme belgelendi
- `SSL-PROBLEMS`: yaygın SSL sorunları ve nedenleri
- `THANKS`: bu kapsamlı dost canlısı insanlar listesi sayesinde, curl bugün var.
- `TheArtOfHttpScripting`: curl ile HTTP komut dosyası oluşturmaya (scripting) giriş dersi
- `TODO`: bizim veya sizin uygulayabileceğiniz şeyler
- `VERSIONS`: libcurl sürüm numaralandırmasının nasıl çalıştığı

## docs/libcurl

Tüm libcurl işlevleri, bu dizinde nroff formatında, .3 uzantılı ayrı dosyalarda kendi kılavuz sayfalarına sahiptir. Aşağıda açıklanan birkaç başka dosya da vardır.

- `ABI`
- `index.html`
- `libcurl.3`
- `libcurl-easy.3`
- `libcurl-errors.3`
- `libcurl.m4`
- `libcurl-multi.3`
- `libcurl-share.3`
- `libcurl-thread.3`
- `libcurl-tutorial.3`
- `symbols-in-versions`

## docs/libcurl/opts

Bu dizin, üç farklı libcurl işlevi için bireysel seçeneklerin kılavuz sayfalarını içerir.

`curl_easy_setopt()` seçenekleri `CURLOPT_` ile başlar,
`curl_multi_setopt()` seçenekleri `CURLMOPT_` ile başlar ve
`curl_easy_getinfo()` seçenekleri `CURLINFO_` ile başlar.

## docs/examples

Okuyucuların libcurl'ün nasıl kullanılabileceğini anlamalarına yardımcı olmayı amaçlayan yaklaşık 100 bağımsız örnek içerir.

Ayrıca bu kitabın [libcurl örnekleri](../examples/) bölümüne de bakın.

## scripts

Kullanışlı komut dosyaları.

- `contributors.sh`: belirli bir hash/etiketten bu yana tüm katkıda bulunanları git deposundan çıkarır. Amaç, RELEASE-NOTES dosyası için bir liste oluşturmak ve manuel olarak eklenen isimlerin güncellemelerde bile orada kalmasına izin vermektir. Komut dosyası, bazı isimleri yeniden yazmak için `THANKS-filter` dosyasını kullanır.
- `contrithanks.sh`: belirli bir hash/etiketten bu yana katkıda bulunanları git deposundan çıkarır, `THANKS` dosyasında zaten belirtilen tüm isimleri filtreler ve ardından yeni katkıda bulunanların listesini sona ekleyerek `THANKS` dosyasını stdout'a (standart çıktı) verir; THANKS belgesinin daha kolay güncellenmesini sağlamak içindir. Komut dosyası, bazı isimleri yeniden yazmak için `THANKS-filter` dosyasını kullanır.
- `log2changes.pl`: sürüm komut dosyası tarafından kullanıldığı gibi, sürümler için `CHANGES` dosyasını oluşturur. Basitçe git log çıktısını dönüştürür.
- `zsh.pl`: zsh kabuğu kullanıcılarına curl komut satırı tamamlamaları sağlamak için yardımcı komut dosyası.
