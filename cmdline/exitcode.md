# Çıkış kodu (Exit code)

Projeye, bir şeyler ters gittiğinde curl'ün kullanılabilir bir çıkış kodu döndürmesi ve işlem planlandığı gibi gittiğinde her zaman 0 (sıfır) döndürmesi için çok çaba sarf edilmiştir.

curl'ü çağıran bir kabuk betiği veya toplu işlem dosyası yazarsanız, çağrılan komuttaki sorunları algılamak için her zaman dönüş kodunu kontrol edebilirsiniz. Aşağıda, bu yazının yazıldığı tarih itibariyle dönüş kodlarının bir listesini bulabilirsiniz. Zamanla yavaş yavaş yenilerini ekleme eğilimindeyiz, bu nedenle burada listelenmeyen bir kod alırsanız, lütfen yardım için daha güncel curl belgelerine bakın.

Temel bir Unix kabuk betiği şuna benzer bir şeye benzeyebilir:

    #!/bin/sh
    curl http://example.com
    res=$?
    if test "$res" != "0"; then
       echo "the curl command failed with: $res"
    fi

## Mevcut çıkış kodları

 1. Unsupported protocol. Bu curl derlemesinin bu protokol için desteği yoktur. Genellikle bu, URL'nin ya önünde bir boşluk olan ya da `http`yi `htpt` veya benzeri şekilde yazan bir şema parçası kullanmak için yanlış yazılmasından kaynaklanır. Başka bir yaygın hata, bir veya daha fazla protokolü devre dışı bırakılmış olarak oluşturulmuş bir libcurl kurulumu kullanmanız ve şimdi libcurl'den derlemede devre dışı bırakılan protokollerden birini kullanmasını istemenizdir.

 2. Failed to initialize. Bu çoğunlukla dahili bir hatadır veya libcurl kurulumu veya libcurl'ün içinde çalıştığı sistemle ilgili bir sorundur.

 3. URL malformed. Sözdizimi doğru değildi. Bu, bir URL'yi yanlış yazdığınızda ve yanlış sonuçlandığında veya nadir durumlarda, sırf herkesin uyduğu evrensel bir URL standardı olmadığı için curl'ün desteklemediği ancak başka bir aracın kabul ettiği bir URL kullandığınızda olur.

 4. İstenen isteği gerçekleştirmek için gereken bir özellik veya seçenek etkinleştirilmedi veya derleme zamanında açıkça devre dışı bırakıldı. curl'ün bunu yapabilmesi için muhtemelen başka bir libcurl derlemesine ihtiyacınız var.

 5. Could not resolve proxy. Verilen proxy ana bilgisayarının adresi çözümlenemedi. Ya verilen proxy adı yanlıştır ya da DNS sunucusu hatalı çalışıyordur ve olması gerektiği halde bu adı bilmiyordur ya da belki de curl'ü çalıştırdığınız sistem yanlış yapılandırılmıştır, bu nedenle doğru DNS sunucusunu bulmuyor/kullanmıyordur.

 6. Could not resolve host. Verilen uzak ana bilgisayarın adresi çözümlenemedi. Verilen sunucunun adresi çözümlenemedi. Ya verilen ana bilgisayar adı yanlıştır ya da DNS sunucusu hatalı çalışıyordur ve olması gerektiği halde bu adı bilmiyordur ya da belki de curl'ü çalıştırdığınız sistem yanlış yapılandırılmıştır, bu nedenle doğru DNS sunucusunu bulmuyor/kullanmıyordur.

 7. Failed to connect to host. curl makineye bir IP adresi almayı başardı ve ana bilgisayara bir TCP bağlantısı kurmaya çalıştı ancak başarısız oldu. Bunun nedeni yanlış port numarasını belirtmeniz, yanlış ana bilgisayar adını girmeniz, yanlış protokolü girmeniz veya belki de arada trafiğin geçmesini engelleyen bir güvenlik duvarı veya başka bir ağ ekipmanı olması olabilir.

 8. Unknown FTP server response. Sunucu curl'ün ayrıştıramadığı veriler gönderdi. Bu ya curl'deki bir hatadan, ya sunucudaki bir hatadan ya da sunucunun curl'ün desteklemediği bir FTP protokolü uzantısı kullanmasından kaynaklanmaktadır. Bunun için tek gerçek geçici çözüm, belki de bu bilinmeyen sunucu yanıtını geri almayan diğer FTP komutlarını kullanmasını sağlamak için curl seçeneklerini değiştirmektir.

 9. FTP access denied. Sunucu oturum açmayı reddetti veya erişmek istediğiniz belirli kaynağa veya dizine erişimi reddetti. Çoğu zaman sunucuda bulunmayan bir dizine geçmeye çalıştınız. Dizin elbette URL'de belirttiğiniz şeydir.

 10. FTP accept failed. Etkin bir FTP oturumu kullanılırken sunucunun geri bağlanmasını beklerken, kontrol bağlantısı veya benzeri üzerinden bir hata kodu gönderildi.

 11. FTP weird PASS reply. Curl, PASS isteğine gönderilen yanıtı ayrıştıramadı. PASS, curl'ün sunucuya şifreyi gönderdiği komuttur ve FTP sunucusuna anonim bağlantılar bile aslında bir şifre gönderir - sabit bir anonim dize. Bu komuttan curl'ün anlamadığı bir yanıt almak, bunun hiç de bir FTP sunucusu olmadığının veya sunucunun fena halde bozuk olduğunun güçlü bir göstergesidir.

 12. Etkin bir FTP oturumu sırasında (PORT kullanılır) sunucunun bağlanmasını beklerken zaman aşımı süresi doldu. Sunucunun geri dönmesi çok uzun sürdü. Bu genellikle bir güvenlik duvarı veya diğer ağ düzenlemeleri gibi bir şeyin sunucunun curl'e başarıyla ulaşmasını engellediğinin bir işaretidir.

 13. Unknown response to FTP PASV command. Curl, PASV isteğine gönderilen yanıtı ayrıştıramadı. Bu garip bir sunucu. PASV, ikinci veri transferi bağlantısını pasif modda kurmak için kullanılır, bu konuda daha fazla bilgi için [FTP uses two connections](../ftp/twoconnections.md) bölümüne bakın. `--ftp-port` seçeneğiyle bunun yerine PORT kullanarak bu sorunu aşabilirsiniz.

 14. Unknown FTP 227 format. Curl, sunucunun gönderdiği 227 satırını ayrıştıramadı. Bu kesinlikle bozuk bir sunucu. 227, curl'ün pasif modda ona nasıl geri bağlanması gerektiği hakkında bilgi geri gönderirken FTP sunucusunun yanıtıdır. `--ftp-port` seçeneğiyle bunun yerine PORT kullanarak bu sorunu aşabilirsiniz.

 15. FTP cannot get host. 227 satırında aldığımız ana bilgisayar IP adresini kullanamadık. Bu muhtemelen dahili bir hatadır.

 16. HTTP/2 error. HTTP2 çerçeveleme katmanında bir sorun algılandı. Bu biraz geneldir ve birkaç sorundan biri olabilir, ayrıntılar için hata mesajına bakın.

 17. FTP could not set binary. Transfer yöntemi ikili (binary) olarak değiştirilemedi. Bu sunucu bozuk. curl'ün transfer başlamadan önce transferi doğru moda ayarlaması gerekir, aksi takdirde transfer çalışmaz.

 18. Partial file. Dosyanın sadece bir kısmı transfer edildi. Transfer tamamlanmış olarak kabul edildiğinde, curl aslında önceden alacağı söylenen aynı miktarda veriyi aldığını doğrular. İki sayı eşleşmezse, bu hata kodudur. curl'ün reklamı yapılandan daha az bayt aldığı veya daha fazlasını aldığı anlamına gelebilir. curl'ün kendisi hangi sayının yanlış veya hangisinin doğru olduğunu, eğer varsa, bilemez.

 19. FTP could not download/access the given file. RETR (veya benzeri) komutu başarısız oldu. Curl, dosyayı indirmeye çalışırken sunucudan bir hata aldı.

 20. **Kullanılmıyor**

 21. Quote error. Bir alıntı (quote) komutu sunucudan bir hata döndürdü. curl, bir IMAP, POP3, SMTP veya FTP sunucusuna özel komutlar göndermek için birkaç farklı yola izin verir ve komutların çalıştığını genel olarak kontrol eden bir özelliğe sahiptir. Bireysel olarak verilen komutlardan herhangi biri başarısız olduğunda, döndürülen çıkış durumu budur. Tavsiye genellikle tam olarak neyin ve nasıl başarısız olduğunu daha iyi anlamak için FTP iletişimindeki başlıkları izlemektir.

 22. HTTP page not retrieved. İstenen URL bulunamadı veya HTTP hata kodu 400 veya üzeri olan başka bir hata döndürdü. Bu dönüş kodu yalnızca `-f, --fail` kullanılırsa görünür.

 23. Write error. Curl yerel bir dosya sistemine veya benzerine veri yazamadı. curl ağdan parça parça veri alır ve bunu bir seferde bir parça olmak üzere (veya stdout'a yazar) olduğu gibi depolar. Bu yazma işlemi bir hata alırsa, çıkış durumu budur.

 24. **Kullanılmıyor**

 25. Upload failed. Sunucu, curl'ün ona göndermeye çalıştığı dosyayı kabul etmeyi veya saklamayı reddetti. Bu genellikle sunucudaki yanlış erişim haklarından kaynaklanır ancak disk alanının bitmesi veya diğer kaynak kısıtlamaları nedeniyle de olabilir. Bu hata birçok protokol için olabilir.

 26. Read error. Çeşitli okuma sorunları. Çıkış durumu 23'ün tersi. curl bir sunucuya veri gönderdiğinde, yerel bir dosyadan veya stdin'den veya benzerinden parça parça veri okur ve bu okuma bir şekilde başarısız olursa curl'ün döndürdüğü çıkış durumu budur.

 27. Out of memory. Bir bellek ayırma isteği başarısız oldu. curl, sistemin ona vermeye istekli olduğundan daha fazla bellek ayırması gerekti ve curl çıkmak zorunda kaldı. Daha küçük dosyalar kullanmayı deneyin veya curl'ün çalışması için daha fazla bellek aldığından emin olun.

 28. Operation timeout. Belirtilen zaman aşımı süresine koşullara göre ulaşıldı. curl çeşitli [zaman aşımları](../usingcurl/timeouts.md) sunar ve bu çıkış kodu bu zaman aşımı sınırlarından birine ulaşıldığını söyler. Zaman aşımını uzatın veya curl'ün işlemini daha hızlı bitirmesini sağlayan başka bir şeyi değiştirmeyi deneyin. Genellikle bu, yerel olarak etkileyemeyeceğiniz ağ ve uzak sunucu durumları nedeniyle olur.

 29. **Kullanılmıyor**

 30. FTP PORT failed. PORT komutu başarısız oldu. Tüm FTP sunucuları PORT komutunu desteklemez; bunun yerine PASV kullanarak bir transfer yapmayı deneyin. PORT komutu, sunucudan curl'e *geri bağlanarak* veri bağlantısını oluşturmasını istemek için kullanılır. Ayrıca [FTP uses two connections](../ftp/twoconnections.md) bölümüne bakın.

 31. FTP could not use REST. REST komutu başarısız oldu. Bu komut devam ettirilen FTP transferleri için kullanılır. curl, aralık veya devam ettirilen transferler yapmak için REST komutunu vermesi gerekir. Sunucu bozuk, kaba bir geçici çözüm olarak aralık/devam ettirme olmadan aynı işlemi deneyin.

 32. **Kullanılmıyor**

 33. HTTP range error. Aralık isteği çalışmadı. Devam ettirilen HTTP istekleri mutlaka kabul edilmez veya desteklenmez, bu nedenle bu çıkış kodu, bu sunucudaki bu kaynak için aralık veya devam ettirilen transferler olamayacağını belirtir.

 34. HTTP post error. Dahili post isteği oluşturma hatası. Bu hatayı alırsanız, lütfen tam koşulları curl projesine bildirin.

 35. A TLS/SSL connect error. SSL el sıkışması başarısız oldu. SSL el sıkışması çok sayıda farklı nedenden dolayı başarısız olabilir, bu nedenle hata mesajı bazı ek ipuçları sunabilir. Belki taraflar bir SSL/TLS sürümü, uygun bir şifre paketi veya benzeri üzerinde anlaşamadılar.

 36. Bad download resume. Daha önce iptal edilmiş bir indirme işlemine devam edilemedi. Daha sonra yapılması mümkün olmayan bir transferin devam ettirilmesi istendiğinde, bu hata döndürülebilir. FILE, FTP veya SFTP için.

 37. Could not read the given file when using the FILE:// scheme. Dosya açılamadı. Dosya mevcut olmayabilir veya belki bir izin sorunu olabilir?

 38. LDAP cannot bind. LDAP "bind" işlemi başarısız oldu, bu LDAP işleminde gerekli bir adımdır ve bu nedenle LDAP sorgusunun gerçekleştirilemediği anlamına gelir. Bu, yanlış bir kullanıcı adı veya parola nedeniyle veya başka nedenlerle olabilir.

 39. LDAP search failed. Verilen arama terimleri LDAP aramasının bir hata döndürmesine neden oldu.
 
 40. **Kullanılmıyor**

 41. **Kullanılmıyor**

 42. Aborted by callback. Bir uygulama libcurl'e işlemi iptal etmesini söyledi. Bu hata kodu genellikle kullanıcılara ve curl aracının kullanıcılarına görünür yapılmaz.

 43. Bad function argument. Bir işlev kötü bir parametreyle çağrıldı - bu dönüş kodu, uygulama yazarlarının libcurl'ün neden belirli eylemleri gerçekleştiremediğini anlamalarına yardımcı olmak için mevcuttur ve asla curl aracı tarafından döndürülmemelidir. Bu başınıza gelirse lütfen curl projesine bir hata raporu gönderin.

 44. **Kullanılmıyor**

 45. Interface error. Belirtilen bir giden ağ arayüzü kullanılamadı. curl tipik olarak giden ağ ve IP adreslerine kendisi karar verir, ancak curl'ün kullanamayacağı belirli birini kullanması açıkça istendiğinde bu hata oluşabilir.

 46. **Kullanılmıyor**

 47. Too many redirects. HTTP yönlendirmelerini takip ederken, libcurl uygulama tarafından ayarlanan maksimum sayıya ulaştı. Yönlendirme sayısı libcurl tarafından sınırsızdır ancak curl aracı tarafından varsayılan olarak 50'ye ayarlanmıştır. Sınır, sonsuz yönlendirme döngülerini durdurmak için mevcuttur. Sınırı `--max-redirs` ile değiştirin.

 48. Unknown option specified to libcurl. Bu, temel libcurl sürümüyle senkronize olmayan bir curl sürümü kullanırsanız olabilir. Belki daha yeni curl'ünüz, kullandığınız libcurl sürümünden sonrasına kadar tanıtılmayan ancak daha yeni olduğu için curl araç kodunuz tarafından bilinen eski libcurl'deki bir seçeneği kullanmaya çalışıyordur. Bunun riskini azaltmak ve olmadığından emin olmak için: aynı sürüm numarasına sahip curl ve libcurl kullanın.

 49. Malformed telnet option. curl'e sağladığınız telnet seçeneği doğru sözdizimini kullanmadı.

 50. **Kullanılmıyor**

 51. Sunucunun SSL/TLS sertifikası veya SSH parmak izi doğrulaması başarısız oldu. curl o zaman sunucunun iddia ettiği kişi olduğundan emin olamaz. Daha fazla ayrıntı için [using TLS with curl](../usingcurl/tls.md) ve [using SCP and SFTP with curl](../usingcurl/ssh/) bölümlerine bakın.

 52. Sunucu hiçbir şey yanıtlamadı, bu bağlamda bu bir hata olarak kabul edilir. Bir HTTP(S) sunucusu bir HTTP(S) isteğine yanıt verdiğinde, canlı ve sağlam olduğu sürece her zaman *bir şeyler* döndürür. Tüm geçerli HTTP yanıtlarının bir durum satırı ve yanıt başlığı vardır. Hiçbir şey geri almamak, sunucunun hatalı olduğunun veya belki bir şeyin curl'ün doğru sunucuya ulaşmasını engellediğinin veya yanlış port numarasına bağlanmaya çalıştığınızın vb. bir göstergesidir.

 53. SSL crypto engine not found.

 54. Cannot set SSL crypto engine as default.

 55. Failed sending network data. Ağ üzerinden veri göndermek çoğu curl işleminin çok önemli bir parçasıdır ve curl en alt ağ katmanlarından gönderimin başarısız olduğuna dair bir hata aldığında, bu çıkış durumu döndürülür. Bunun neden olduğunu tam olarak belirlemek için genellikle ciddi bir araştırma gerekir. Ayrıntılı modu etkinleştirerek başlayın, izleme yapın ve mümkünse Wireshark veya benzeri bir araçla ağ trafiğini kontrol edin.

 56. Failure in receiving network data. Ağ üzerinden veri almak çoğu curl işleminin çok önemli bir parçasıdır ve curl en alt ağ katmanlarından veri alımının başarısız olduğuna dair bir hata aldığında, bu çıkış durumu döndürülür. Bunun neden olduğunu tam olarak belirlemek için genellikle ciddi bir araştırma gerekir. Ayrıntılı modu etkinleştirerek başlayın, izleme yapın ve mümkünse Wireshark veya benzeri bir araçla ağ trafiğini kontrol edin.

 57. **Kullanılmıyor**

 58. Problem with the local certificate. İstemci sertifikasında bir sorun vardı, bu yüzden kullanılamadı. İzinler? Yanlış parola?

 59. Could not use the specified SSL cipher. Şifre adlarının tam olarak belirtilmesi gerekir ve maalesef curl'ün kullanmak üzere oluşturulduğu belirli TLS arka ucuna da özgüdürler. Desteklenen şifrelerin güncel listesi ve bunların nasıl yazılacağı için [https://curl.se/docs/ssl-ciphers.html](https://curl.se/docs/ssl-ciphers.html) adresindeki çevrimiçi belgelere bakın.

 60. Peer certificate cannot be authenticated with known CA certificates. Bu genellikle sertifikanın ya kendinden imzalı olduğu ya da curl'ün kullandığı CA deposunda bulunmayan bir CA (Sertifika Yetkilisi) tarafından imzalandığı anlamına gelir.

 61. Unrecognized transfer encoding. Sunucudan alınan içerik curl tarafından ayrıştırılamadı.

 62. **Kullanılmıyor**

 63. Maximum file size exceeded. curl'e indirmeleri dosya çok büyükse yapmaması üzere kısıtlama getirmesi söylendiğinde, bu durum için çıkış kodu budur.

 64. Requested SSL (TLS) level failed. Çoğu durumda bu, curl'ün istendiğinde bağlantıyı TLS'ye yükseltemediği anlamına gelir.

 65. Sending the data requires a rewind that failed. Bazı durumlarda curl'ün verileri tekrar göndermek için geri sarması gerekir ve bu yapılamazsa işlem başarısız olur.

 66. Failed to initialize the OpenSSL SSL Engine. Bu yalnızca OpenSSL kullanıldığında olabilir ve ciddi bir dahili soruna işaret eder.

 67. Kullanıcı adı, parola veya benzeri kabul edilmedi ve curl oturum açamadı. Kimlik bilgilerinin doğru sağlandığını ve doğru şekilde kodlandığını doğrulayın.

 68. File not found on TFTP server.

 69. Permission problem on TFTP server.

 70. Out of disk space on TFTP server.

 71. Illegal TFTP operation.

 72. Unknown TFTP transfer ID.

 73. File already exists (TFTP).

 74. No such user (TFTP).

 75. **Kullanılmıyor**

 76. **Kullanılmıyor**

 77. Problem with reading the SSL CA cert. Varsayılan veya belirtilen CA sertifika paketi sunucu sertifikasını doğrulamak için okunamadı/kullanılamadı.

 78. URL'de başvurulan kaynak (dosya) mevcut değil.

 79. SSH oturumu sırasında belirtilmemiş bir hata oluştu. Bu bazen, curl'ün kullandığı SSH libcurl ile curl'ün konuştuğu sunucu tarafından kullanılan SSH sürümü arasında bir uyumsuzluk sorununu gösterir.

 80. Failed to shut down the SSL connection.

 81. **Kullanılmıyor**

 82. Could not load CRL file, missing or wrong format

 83. TLS certificate issuer check failed. Bunun en yaygın nedeni, sunucunun TLS el sıkışmasında uygun ara sertifikayı göndermemesidir.

 84. FTP `PRET` command failed. Bu standart olmayan bir komuttur ve tüm sunucular tarafından desteklenmekten uzaktır.

 85. RTSP: mismatch of CSeq numbers

 86. RTSP: mismatch of Session Identifiers

 87. Unable to parse FTP file list. Sunucu tarafından kullanılan FTP dizin listeleme formatı curl tarafından ayrıştırılamadı. FTP joker karakterleri (wildcards) bu sunucuda kullanılamaz.

 88. FTP chunk callback reported error

 89. No connection available, the session is queued

 90. SSL public key does not match pinned public key. Ya kötü bir ortak anahtar sağladınız ya da sunucu değişti.

 91. Invalid SSL certificate status. Sunucu TLS el sıkışmasında uygun ve geçerli bir sertifika sağlamadı.

 92. Stream error in HTTP/2 framing layer. Bu genellikle kurtarılamaz bir hatadır, ancak curl'ü bunun yerine HTTP/1 konuşmaya zorlamayı denemek bunu atlatabilir.

 93. An API function was called from inside a callback. curl aracı bunu döndürürse, dahili olarak bir şeyler ters gitmiştir

 94. Authentication error.

 95. HTTP/3 layer error. Bu biraz geneldir ve birkaç sorundan biri olabilir, ayrıntılar için hata mesajına bakın.

 96. QUIC connection error. Bu hataya bir TLS kütüphanesi hatası neden olabilir. QUIC, HTTP/3 için kullanılan taşıma protokolüdür.

 97. Proxy handshake error. Genellikle bu, bir SOCKS proxy'sinin uyumlu davranmadığı anlamına gelir.

 98. A TLS client certificate is required but was not provided.

 99. An internal call to poll() or select() returned error that is not recoverable.

## Hata mesajı

curl sıfır olmayan bir kodla çıktığında, bir hata mesajı da çıktılar ( `--silent` kullanılmadığı sürece). Bu hata mesajı, çıkış durumu numarasına bazı ek bilgiler veya koşullar ekleyebilir, böylece aynı hata numarası farklı hata mesajları alabilir.

Kullanıcılar ayrıca [--write-out](../usingcurl/verbose/writeout.md) ile kendi hata mesajlarını oluşturabilirler. `%{onerror}` sözde değişkeni, yalnızca hatalarda görüntülenen bir mesaj ayarlamanıza olanak tanır ve tüm değişkenler arasında `%{errormsg}` ve `%{exitcode}` seçeneklerini sunar.

Örneğin:

    curl --write-out "%{onerror}curl says: (%{exitcode}) %{errormsg}" \
      https://curl.se/

## "Kullanılmıyor"

Yukarıdaki çıkış kodları listesi, 'kullanılmıyor' olarak işaretlenmiş bir dizi değer içerir. Bunlar, curl'ün modern sürümlerinde kullanılmayan ancak geçmişte kullanılan veya kullanılması amaçlanan çıkış durumu kodlarıdır. Gelecekteki bir curl sürümünde kullanılabilirler.

Ek olarak, bu listedeki en yüksek kullanılan hata durumu 99'dur, ancak gelecekteki curl sürümleri bu sayıdan sonra daha fazla çıkış kodu eklemiş olabilir.
