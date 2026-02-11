# SSH anahtarı

Bu geri çağırım `CURLOPT_SSH_KEYFUNCTION` ile ayarlanır.

`known_host` eşleşmesi yapıldığında, uygulamanın harekete geçmesine ve libcurl için nasıl devam edileceğine karar vermesine izin vermek için çağrılır. `CURLOPT_SSH_KNOWNHOSTS` da ayarlanmışsa geri çağırım çağrılır.

Geri çağırıma verilen argümanlarda eski anahtar ve yeni anahtar bulunur ve geri çağırımın libcurl'e nasıl hareket edeceğini söyleyen bir dönüş kodu döndürmesi beklenir:

`CURLKHSTAT_FINE_REPLACE` - Yeni ana bilgisayar+anahtar kabul edilir ve libcurl bağlantıya devam etmeden önce known_hosts dosyasındaki eski ana bilgisayar+anahtarı değiştirir. Bu ayrıca yeni ana bilgisayar+anahtar birleşimini, zaten orada mevcut değilse bellekte tutulan known_host havuzuna ekler. Dosyaya veri ekleme işlemi, dosyanın tamamen yeni bir kopyayla değiştirilmesiyle yapılır, bu nedenle dosyanın izinleri buna izin vermelidir.

`CURLKHSTAT_FINE_ADD_TO_FILE` - Ana bilgisayar+anahtar kabul edilir ve libcurl bağlantıya devam etmeden önce onu known_hosts dosyasına ekler. Bu ayrıca ana bilgisayar+anahtar birleşimini, zaten orada mevcut değilse bellekte tutulan known_host havuzuna ekler. Dosyaya veri ekleme işlemi, dosyanın tamamen yeni bir kopyayla değiştirilmesiyle yapılır, bu nedenle dosyanın izinleri buna izin vermelidir.

`CURLKHSTAT_FINE` - Ana bilgisayar+anahtar kabul edilir, libcurl bağlantıya devam eder. Bu ayrıca ana bilgisayar+anahtar birleşimini, zaten orada mevcut değilse bellekte tutulan known_host havuzuna ekler.

`CURLKHSTAT_REJECT` - Ana bilgisayar+anahtar reddedilir. libcurl bağlantının devam etmesini reddeder ve kapanır.

`CURLKHSTAT_DEFER` - Ana bilgisayar+anahtar reddedilir ancak SSH bağlantısının canlı tutulması istenir. Bu özellik, uygulama bir şekilde geri dönüp ana bilgisayar+anahtar durumuna göre hareket etmek ve ardından sıfırdan tekrar kurma yükü olmadan yeniden denemek istediğinde kullanılabilir.
