# Güvenlik açıklarını bildirme

Bilinen ve halka açık tüm curl veya libcurl ile ilgili güvenlik açıkları [curl web sitesi güvenlik sayfasında](https://curl.se/docs/security.html) listelenmiştir.

Soruna erişimi yalnızca raporlayan kişi ve projenin güvenlik ekibiyle sınırlayacak gerekli yapılandırma mevcut olmadığı sürece, güvenlik açıkları projenin halka açık hata izleyicisine (bug tracker) girilmemelidir.

## Güvenlik açığı yönetimi

Yeni bir güvenlik açığını ele almanın tipik süreci aşağıdaki gibidir.

Bu sürecin sonunda resmi olarak duyurulana kadar bir güvenlik açığı hakkında hiçbir bilgi halka açıklanmamalıdır. Bu, örneğin, sorunu izlemek için bir hata izleyici girişinin OLUŞTURULMAMASI gerektiği anlamına gelir çünkü bu sorunu halka açık hale getirir ve projenin halka açık posta listelerinde tartışılmamalıdır. Ayrıca, halka açık duyurudan önce yapıldıysa, herhangi bir işlemeyle (commit) ilişkili mesajlar, işlemenin güvenlik doğasına herhangi bir atıfta bulunmamalıdır.

- Sorunu keşfeden kişi, raporlayan, güvenlik açığını [https://hackerone.com/curl](https://hackerone.com/curl) adresinde bildirir. Oraya dosyalanan sorunlar bir avuç seçilmiş ve güvenilir kişiye ulaşır.

- curl veya libcurl'deki açıklanmamış bir güvenlik açığının raporlanması veya yönetilmesiyle ilgili olmayan mesajlar yok sayılır ve başka bir işlem gerekmez.

- Güvenlik ekibinden bir kişi, raporu aldığını bildirmek için orijinal raporlayıcıya bir e-posta gönderir.

- Güvenlik ekibi raporu araştırır ve reddeder ya da kabul eder.

- Rapor reddedilirse, ekip raporlayıcıya nedenini açıklamak için yazar.

- Rapor kabul edilirse, ekip raporlayıcıya kabul edildiğini ve bir düzeltme üzerinde çalıştıklarını bildirmek için yazar.

- Güvenlik ekibi sorunu tartışır, bir düzeltme geliştirir, sorunun etkisini değerlendirir ve bir yayın takvimi önerir. Bu tartışma, raporlayıcıyı mümkün olduğunca dahil etmelidir.

- Bilginin yayınlanması mümkün olan en kısa sürede olmalıdır ve en sık olarak düzeltmeyi içeren yaklaşan bir sürümle senkronize edilir. Raporlayan veya başka biri bir sonraki planlanan sürümün çok uzak olduğunu düşünürse, güvenlik nedenleriyle ayrı bir erken sürüm düşünülebilir.

- Sorunun ne olduğunu, etkisini, hangi sürümleri etkilediğini, herhangi bir çözümü veya geçici çözümü ve düzeltmenin ne zaman yayınlandığını açıklayan, tüm katkıda bulunanlara düzgün bir şekilde atıfta bulunulan sorun hakkında bir güvenlik tavsiyesi taslağı yazın.

- HackerOne'ın bu amaçla formunu kullanarak bir CVE numarası ([Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)) isteyin.

- Güvenlik tavsiyesini CVE numarası ile güncelleyin.

-Yaklaşan halka açık güvenlik açığı duyurusu hakkında onları hazırlamak için [distros@openwall](https://oss-security.openwall.org/wiki/mailing-lists/distros)'u bilgilendirmeyi düşünün - bilgi için tavsiye taslağını ekleyin. 'Distros'un 14 günden uzun bir ambargoyu kabul etmediğini ve Windows'a özgü kusurları umursamadığını unutmayın.

- Güvenlik ekibi, düzeltmeyi özel bir dalda (private branch) işler (commits). İşleme mesajı ideal olarak CVE numarasını içermelidir. Bu düzeltme genellikle halka açık duyurudan önce düzeltmeyi kullanmalarına izin vermek için 'distros' posta listesine de dağıtılır.

- Bir sonraki sürüm gününde, özel dal master dalına birleştirilir (merged) ve gönderilir (pushed). Gönderildikten sonra, bilgi halka erişilebilir olur ve gerçek sürüm hemen ardından gelmelidir.

- Proje ekibi, düzeltmeyi içeren bir sürüm oluşturur.

- Proje ekibi, sürümü ve güvenlik açığını dünyaya her zaman sürümleri duyurduğumuz şekilde duyurur—curl-announce, curl-library ve curl-users posta listelerine gönderilir.

- Web sitesindeki güvenlik web sayfası yeni güvenlik açığından bahsetmelidir.

## curl-security@haxx.se

Bu listede kimler var? Karşılamanız gereken birkaç kriter var ve ardından listeye katılmanızı isteyebiliriz veya siz katılmayı isteyebilirsiniz. Gerçekten resmi değil. Sadece curl projesinde uzun vadeli bir varlığınız olmasını ve projeyi ve çalışma şeklini anladığınızı göstermenizi istiyoruz. İyi bir süredir buralarda olmalısınız ve yakın gelecekte ortadan kaybolma planlarınız olmamalı.

Katılımcı listesini halka açık yapmıyoruz çünkü çoğunlukla zamanla biraz değişme eğilimindedir ve bir yerdeki liste sadece güncelliğini yitirme riski taşır.
