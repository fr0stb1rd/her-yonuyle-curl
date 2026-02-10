# Bağlantı yeniden kullanımı (Connection reuse)

libcurl eski bağlantılardan oluşan bir havuzu canlı tutar. Bir transfer tamamlandığında, mevcut bağlantılardan birini yeniden kullanabilecek bir sonraki transferin yeni bir bağlantı oluşturmak yerine onu kullanabilmesi için bir bağlantı havuzunda (bazen bağlantı önbelleği olarak da adlandırılır) N bağlantıyı canlı tutar. Yeni bir bağlantı oluşturmak yerine bir bağlantıyı yeniden kullanmak, hız ve gerekli kaynaklar açısından önemli avantajlar sunar.

libcurl bir transfer yapmak amacıyla yeni bir bağlantı kurmak üzereyken, önce havuzda yeniden kullanabileceği mevcut bir bağlantı olup olmadığını kontrol eder. Bağlantı yeniden kullanım kontrolü, herhangi bir DNS veya diğer ad çözümleme mekanizması kullanılmadan önce yapılır, bu nedenle tamamen ana bilgisayar adına dayalıdır. Doğru ana bilgisayar adına mevcut canlı bir bağlantı varsa, kullanılıp kullanılamayacağını görmek için diğer birçok özellik (port numarası, protokol vb.) de kontrol edilir.

## Easy API havuzu

Easy API'yi veya daha spesifik olarak `curl_easy_perform()`'u kullandığınızda, libcurl havuzu belirli easy handle ile ilişkili tutar. Ardından aynı easy handle'ı yeniden kullanmak, libcurl'ün bağlantısını yeniden kullanabilmesini sağlar.

## Multi API havuzu

Multi API'yi kullandığınızda, bağlantı havuzu bunun yerine multi handle ile ilişkili tutulur. Bu, bağlantı havuzunu kaybetme riski olmadan easy handle'ları serbestçe temizlemenize ve yeniden oluşturmanıza olanak tanır ve bir easy handle tarafından kullanılan bağlantının daha sonraki bir transferde ayrı bir easy handle tarafından yeniden kullanılmasına izin verir. Sadece multi handle'ı yeniden kullanın.

## Bağlantı önbelleğini paylaşma

libcurl 7.57.0'dan bu yana uygulamalar, aksi takdirde bağımsız transferlerin aynı bağlantı havuzunu paylaşmasını sağlamak için [paylaşım arayüzünü (share interface)](../../helpers/sharing.md) kullanabilir.

## Bağlantılar istediğiniz gibi yeniden kullanılmadığında

libcurl, açıkça yapmaması söylenmedikçe bağlantıları otomatik olarak ve her zaman yeniden kullanmaya çalışacaktır. Ancak bir bağlantının sonraki bir transfer için *kullanılmamasının* birkaç nedeni vardır.

 - Sunucu, bu transferden sonra bağlantının kapatılacağını bildirir. Örneğin `Connection: close` HTTP yanıt başlığını veya bir HTTP/2 veya HTTP/3 "go away" çerçevesini kullanarak.

 - Bir transferin HTTP/1 yanıtı, gövdenin sonunu algılamanın tek yolunun bağlantı kapatma olduğu bir şekilde gönderilir. Veya curl'ün bağlantıyı artık güvenli bir şekilde yeniden kullanamayacağına karar vermesini sağlayan bir HTTP/1 alma hatası.

 - libcurl yeniden kullanmaya çalıştığında bağlantı "ölü" kabul edilir. Sunucu tarafı önceki transfer tamamlandıktan sonra bağlantıyı kapattığında olabilir. Ayrıca durum bilgisi olan bir güvenlik duvarı/NAT veya ağ yolundaki bir şey bağlantıyı düşürürse veya gözetimsizken bağlantı üzerinde HTTP/2 veya HTTP/3 trafiği (PING çerçeveleri gibi) varsa da olabilir.

 - Önceki transfer yeniden kullanılamayacak kadar eski kabul edilir. `CURLOPT_MAXLIFETIME_CONN` ayarlanmışsa, libcurl saniye cinsinden ayarlanan değerden daha eski bir bağlantıyı yeniden kullanmaz.

 - Önceki transferin çok uzun süre boşta kaldığı kabul edilir. Varsayılan olarak libcurl, 118 saniyeden fazla boşta kalan bir bağlantıyı asla yeniden kullanmaya çalışmaz. Bu süre `CURLOPT_MAXAGE_CONN` ile değiştirilebilir.

 - Bir transfer sona erdiğinde ve oraya yeni bir bağlantı depolanmak üzereyken bağlantı havuzu doluysa, havuzdaki en eski boşta bağlantı kapatılır ve atılır ve bu nedenle artık yeniden kullanılamaz. Kullandığınız API'ye bağlı olarak `CURLMOPT_MAXCONNECTS` veya `CURLOPT_MAXCONNECTS` ile bağlantı havuzu boyutunu artırın.

 - Multi arayüz kullanılırken, bir sonraki transfer başlatıldığında önceki transfer sona ermemişse ve önceki bağlantı çoğullama (multiplexing) için kullanılamıyorsa.

Vb. Genellikle `CURLOPT_VERBOSE` özelliğini etkinleştirerek ve libcurl'ün uygulamaya ne bildirdiğini inceleyerek nedenini öğrenebilirsiniz.
