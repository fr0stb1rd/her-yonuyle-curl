# FTPS

FTPS, TLS ile güvenli FTP'dir. Düz FTP'nin açık metin güvensiz bağlantılar kullandığı yerde, tam güvenli TLS bağlantıları için pazarlık yapar.

curl ile FTPS yapmanın iki yolu vardır. *Zımni* (implicit) yol ve *açık* (explicit) yol. (Bu terimler FTPS RFC'sinden gelmektedir). Genellikle çalıştığınız sunucu, ona karşı bu yöntemlerden hangisini kullanabileceğinizi ve kullanmanız gerektiğini belirler.

## Zımni FTPS

*Zımni* yol, URL'nizde `ftps://` kullandığınız zamandır. Bu, curl'ün ana bilgisayara bağlanmasını ve açıkta hiçbir şey yapmadan hemen bir TLS el sıkışması yapmasını sağlar. URL'de hiçbir bağlantı noktası numarası belirtilmezse, curl bunun için 990 portunu kullanır. Bu genellikle FTPS'in yapılma şekli değildir.

## Açık FTPS

FTPS yapmanın *açık* yolu, bir `ftp://` URL'si kullanmaya devam etmek ancak curl'e `AUTH TLS` FTP komutunu kullanarak bağlantıyı güvenli bir bağlantıya yükseltmesi talimatını vermektir.

curl'e bir yükseltme *denemesini* ve yükseltme başarısız olursa (`--ssl` ile) her zamanki gibi devam etmesini söyleyebilir veya `--ssl-reqd` kullanarak curl'ü yükseltmeye zorlayabilir veya yükseltme başarısız olursa her şeyi sert bir şekilde başarısızlığa uğratabilirsiniz. İkinciyi kullanmanızı şiddetle tavsiye ederiz, böylece - eğer yapılacaksa - güvenli bir transferin yapıldığından emin olabilirsiniz.

## Yaygın FTPS sorunları

FTPS ile ilgili en yaygın tek sorun, FTP protokolünün (FTPS transferlerinin dayandığı) veri transferi için ayrı bir bağlantı kurulumu kullanmasından kaynaklanmaktadır. Bu bağlantı başka bir porta yapılır ve FTP açık metin (FTPS olmayan) üzerinden yapıldığında, güvenlik duvarları ve ağ denetçileri vb. bunun devam eden FTP olduğunu anlayabilir ve yeni bağlantı için şeyleri ve kuralları uyarlayabilir.

FTP kontrol kanalı TLS ile şifrelendiğinde, güvenlik duvarları neler olduğunu göremez ve hiçbir dış taraf buna dayanarak ağ kurallarını veya izinlerini dinamik olarak uyarlayamaz.
