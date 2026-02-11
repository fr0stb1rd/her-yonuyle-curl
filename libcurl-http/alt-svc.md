# alt-svc

Alternatif Hizmetler (Alternative Services), diğer adıyla alt-svc, bir sunucunun istemciye `Alt-Svc:` yanıt başlığını kullanarak başka bir yerde o sunucu için bir veya daha fazla *alternatif* olduğunu söylemesini sağlayan bir HTTP başlığıdır.

Sunucunun önerdiği *alternatifler*, aynı ana bilgisayarda başka bir portta çalışan bir sunucuyu, tamamen farklı başka bir ana bilgisayar adını içerebilir ve ayrıca hizmeti *başka bir protokol üzerinden* sunabilir.

## Etkinleştir

libcurl'ün sunucular tarafından sunulan alternatifleri dikkate almasını sağlamak için önce bunu handle'da etkinleştirmeniz gerekir. Bunu `CURLOPT_ALTSVC_CTRL` seçeneğine doğru bit maskesini ayarlayarak yaparsınız. Bit maskesi, uygulamanın hangi HTTP sürümlerine izin verileceğini ve diskteki önbellek dosyasının yalnızca okumak için kullanılıp kullanılmayacağını (yazmak için değil) sınırlamasına izin verir.

alt-svc'yi etkinleştirin ve HTTP/1 veya HTTP/2'ye geçmesine izin verin:

    curl_easy_setopt(curl, CURLOPT_ALTSVC_CTRL, CURLALTSVC_H1|CURLALTSVC_H2);

libcurl'e şöyle belirli bir alt-svc önbellek dosyası kullanmasını söyleyin:

    curl_easy_setopt(curl, CURLOPT_ALTSVC, "altsvc-cache.txt");

libcurl, alternatiflerin listesini bellek tabanlı bir önbellekte tutar ancak başlangıçta mevcut tüm alternatif hizmet girişlerini alt-svc dosyasından yükler ve sonraki HTTP isteklerini yaparken bunları dikkate alır. Sunucular yeni veya güncellenmiş `Alt-Svc:` başlıklarıyla yanıt verirse, libcurl çıkışta bunları önbellek dosyasına saklar (`CURLALTSVC_READONLYFILE` biti ayarlanmadıkça).

## alt-svc önbelleği

alt-svc önbelleği bir çerez kavanozuna (cookie jar) benzer. Satır başına bir alternatif saklayan metin tabanlı bir dosyadır ve her girişte o belirli alternatifin ne kadar süre geçerli olduğuna dair bir bitiş süresi de vardır.

## Yalnızca HTTPS

`Alt-Svc:`, yalnızca HTTPS üzerinden bağlanıldığında sunuculardan güvenilir kabul edilir ve ayrıştırılır.

## HTTP/3

`Alt-Svc:` başlıklarının kullanımı, Mart 2022 itibarıyla bir istemci ve sunucuyu HTTP/3 kullanmaya başlatmanın hala tek tanımlanmış yoludur. Sunucu daha sonra istemciye HTTP/1 veya HTTP/2 üzerinden kendisinin HTTP/3 üzerinden de kullanılabilir olduğunu ima eder ve ardından alt-svc önbelleği öyle diyorsa curl sonraki istekte HTTP/3 kullanarak ona bağlanabilir.
