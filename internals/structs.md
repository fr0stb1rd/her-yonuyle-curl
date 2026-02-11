# Yapılar (Structs)

Bu bölüm dahili yapıları belgeler. Bunlar gerçekten dahili olduklarından, zaman zaman onları değiştiririz ve bu da bu bölümü bazen biraz güncel olmayan hale getirebilir.

## Curl_easy

  `Curl_easy` yapısı, harici API'de opak bir `CURL *` olarak dışarıya döndürülen yapıdır. Bu işaretçi genellikle API belgelerinde ve örneklerinde easy handle (kolay tutaç) olarak bilinir.

  Gerçek bağlantıyla ilgili bilgi ve durum `connectdata` yapısındadır. Bir transfer yapılmak üzereyken, libcurl ya yeni bir bağlantı oluşturur ya da mevcut birini yeniden kullanır. Bu handle tarafından kullanılan mevcut connectdata `Curl_easy->conn` tarafından işaret edilir.

  Bu belirli tek transfere ilişkin veriler ve bilgiler `SingleRequest` alt yapısına konur.

  `Curl_easy` yapısı bir multi handle'a eklendiğinde (herhangi bir transfer yapmak için eklenmelidir), `->multi` üyesi ait olduğu `Curl_multi` yapısına işaret eder. `->prev` ve `->next` üyeleri daha sonra multi kodu tarafından aynı multi handle'a eklenen `Curl_easy` yapılarının bağlantılı bir listesini tutmak için kullanılır. libcurl her zaman multi kullanır, bu nedenle bir transfer devam ederken `->multi` bir `Curl_multi`'ye işaret eder.

  `->mstate`, bu belirli `Curl_easy`'nin multi durumudur. `multi_runsingle()` çağrıldığında, hangi durumda olduğuna göre bu handle üzerinde işlem yapar. mstate ayrıca [`curl_multi_fdset()`][12] vb. çağrıldığında belirli bir `Curl_easy` için hangi soketlerin döndürüleceğini söyleyen şeydir.

  libcurl kaynak kodu genellikle `Curl_easy` yapısına işaret eden yerel değişken için her yerde `data` adını kullanır.

  Çoğullanmış (multiplexed) HTTP/2 transferleri yaparken, her `Curl_easy`, aynı connectdata yapısını paylaşan ayrı bir akışla ilişkilendirilir. Çoğullama, şeyleri doğru şeyle ilişkili tutmayı daha da önemli hale getirir.

## connectdata

  libcurl'deki genel bir fikir, bağlantıları kullanıldıktan sonra tekrar kullanılmaları durumunda bir bağlantı önbelleğinde tutmak ve ardından yeni bir tane oluşturmak yerine mevcut birini yeniden kullanmaktır; bu önemli bir performans artışı yaratır.

  Her `connectdata` yapısı bir sunucuya tek bir fiziksel bağlantıyı tanımlar. Bağlantı canlı tutulamazsa, kullanımdan sonra bağlantı kapatılır ve ardından bu yapı önbellekten çıkarılabilir ve serbest bırakılabilir.

  Böylece, aynı `Curl_easy` birden çok kez kullanılabilir ve her seferinde bağlantı için kullanılacak başka bir `connectdata` yapısı seçebilir. Bunu aklınızda bulundurun, çünkü seçeneklerin veya seçimlerin bağlantıya mı yoksa `Curl_easy`'ye mi dayalı olduğunu düşünmek o zaman önemlidir.

  Özel bir karmaşıklık olarak, libcurl tarafından desteklenen bazı protokoller, sadece soketi kapatmaktan daha fazlası olan özel bir bağlantı kesme prosedürü gerektirir. Bunu yapmadan önce sunucuya bir veya daha fazla komut göndermeyi içerebilir. Bağlantılar kullanımdan sonra bağlantı önbelleğinde tutulduğundan, belirli bir bağlantıyı kapatma zamanı geldiğinde orijinal `Curl_easy` artık etrafta olmayabilir. Bu amaçla libcurl, gerektiğinde kullanmak üzere `Curl_multi` yapısında özel bir kukla `closure_handle` `Curl_easy` tutar.

  FTP, tipik bir transfer için iki TCP bağlantısı kullanır ancak her ikisini de bu tek yapıda tutar ve bu nedenle çoğu dahili endişe için tek bir bağlantı olarak kabul edilebilir.

  libcurl kaynak kodu genellikle connectdata'ya işaret eden yerel değişken için `conn` adını kullanır.

## Curl_multi

  Dahili olarak, easy arayüzü multi arayüzü işlevlerinin etrafında bir sarmalayıcı olarak uygulanır. Bu her şeyi multi arayüzü yapar.

  `Curl_multi`, harici API'lerde opak `CURLM *` olarak sunulan multi handle yapısıdır.

  Bu yapı, [`curl_multi_add_handle()`][13] ile bu handle'a eklenmiş `Curl_easy` yapılarının bir listesini tutar. Listenin başı `->easyp`'dir ve `->num_easy`, eklenen `Curl_easy`'lerin bir sayacıdır.

  `->msglist`, [`curl_multi_info_read()`][14] çağrıldığında geri gönderilecek mesajların bağlantılı bir listesidir. Temel olarak, bireysel bir `Curl_easy`'nin transferi tamamlandığında o listeye bir düğüm eklenir.

  `->hostcache` isim önbelleğine işaret eder. İsimden IP'ye arama yapmak için bir karma tablosudur. Düğümlerin orada sınırlı bir ömrü vardır ve bu önbellek, aynı ismin kısa bir süre içinde istendiği zaman süreyi azaltmak içindir.

  `->timetree`, kontrol edilmesi gereken kalan süreye göre sıralanmış `Curl_easy` ağacına işaret eder - normalde bir tür zaman aşımı. Her `Curl_easy` ağaçta bir düğüme sahiptir.

  `->sockhash`, hangi `Curl_easy`'nin o tanımlayıcıyı kullandığına dair soket tanımlayıcısının hızlı aramalarına izin vermek için bir karma tablosudur. Bu, `multi_socket` API'si için gereklidir.

  `->conn_cache` bağlantı önbelleğine işaret eder. Kullanımdan sonra tutulan tüm bağlantıları takip eder. Önbelleğin maksimum bir boyutu vardır.

  `->closure_handle`, `connectdata` bölümünde açıklanmıştır.

  libcurl kaynak kodu genellikle `Curl_multi` yapısına işaret eden değişken için `multi` adını kullanır.

## Curl_handler

  libcurl tarafından desteklenen her benzersiz protokolün en az bir `Curl_handler` yapısı sağlaması gerekir. Protokolün ne olarak adlandırıldığını ve ana kodun protokole özgü sorunlarla başa çıkmak için hangi işlevleri çağırması gerektiğini tanımlar. Genel olarak, içinde `struct Curl_handler Curl_handler_[protocol]` bildirilmiş `[protocol].c` adında bir kaynak dosyası vardır. `url.c` içinde, libcurl'e çalışması için bir URL verildiğinde taranan tek bir diziden işaret edilen tüm bireysel `Curl_handler` yapılarına sahip ana dizi vardır.

  Somut işlev işaretçisi prototipleri `lib/urldata.h` içinde bulunabilir.

  - `->scheme`, genellikle büyük harflerle yazılan URL şema adıdır. Yani HTTP veya FTP vb. Protokolün SSL sürümlerinin kendi `Curl_handler` kurulumuna ihtiyacı vardır, bu nedenle HTTPS HTTP'den ayrıdır.

  - `->setup_connection`, protokol kodunun daha sonra bu transferin geri kalanı için o `Curl_easy` ile ilişkilendirilecek protokole özgü verileri tahsis etmesine izin vermek için çağrılır. Transferin sonunda tekrar serbest bırakılır. Transfer için `connectdata` seçilmeden/oluşturulmadan önce çağrılır. Çoğu protokol burada özel `struct [PROTOCOL]` yapısını tahsis eder ve `Curl_easy->req.p.[protocol]`'u buna atar.

  - `->connect_it`, bir protokolün TCP bağlantısı yapıldıktan sonra bazı belirli eylemleri yapmasına izin verir, bu hala bağlantı aşamasının bir parçası olarak kabul edilebilir. Bazı protokoller bu işlevde `connectdata->recv[]` ve `connectdata->send[]` işlev işaretçilerini değiştirir.

  - `->connecting` benzer şekilde protokol kendini hala bağlantı aşamasında gördüğü sürece çağrılmaya devam eden bir işlevdir.

  - `->do_it`, transfer isteğini yayınlamak için çağrılan işlevdir. Dahili olarak DO eylemi dediğimiz şey. DO yeterli değilse ve tüm DO dizisinin tamamlanması için bir şeylerin yapılmaya devam etmesi gerekiyorsa, o zaman genellikle `->doing` de sağlanır. Do/doing için birden fazla komut veya benzerini yapması gereken her protokolün kendi durum makinelerini uygulaması gerekir (bkz. SCP, SFTP, FTP). Bazı protokoller (yalnızca FTP ve yalnızca tarihsel nedenlerden dolayı) `DO_MORE` adı verilen DO durumunun ayrı bir parçasına sahiptir.

  - `->doing`, transfer isteği komut(lar)ını yayınlarken çağrılmaya devam eder

  - `->done`, transfer tamamlandığında ve BİTTİĞİNDE çağrılır. Yani ana veriler transfer edildikten sonra.

  - `->do_more`, `DO_MORE` durumu sırasında çağrılır. FTP protokolü ikinci bağlantıyı kurarken bu durumu kullanır.

  - `->proto_getsock`, `->doing_getsock`, `->domore_getsock`, `->perform_getsock` Soket bilgisi döndüren işlevler. Belirli multi durumu sırasında hangi G/Ç eylem(ler)i için hangi soket(ler)in bekleneceği.

  - `->disconnect`, TCP bağlantısı kapatılmadan hemen önce çağrılır.

  - `->readwrite`, protokolün fazladan okuma/yazma yapmasına izin vermek için transfer sırasında çağrılır

  - `->attach`, bir transferi bağlantıya ekler.

  - `->defport`, bu protokolün kullandığı varsayılan rapor TCP veya UDP portudur

  - `->protocol`, `CURLPROTO_*` setindeki bir veya daha fazla bittir. SSL sürümlerinin temel protokol seti ve ardından SSL varyasyonu vardır. `HTTP|HTTPS` gibi.

  - `->flags`, protokol hakkında genel motor tarafından farklı muamele görmesini sağlayan ek bilgiler içeren bir bit maskesidir:
    - `PROTOPT_SSL` - bağlanmasını ve SSL anlaşmasını sağlar
    - `PROTOPT_DUAL` - bu protokol iki bağlantı kullanır
    - `PROTOPT_CLOSEACTION` - bu protokolün bağlantıyı kapatmadan önce
      yapması gereken eylemleri vardır. Bu bayrak artık kod tarafından
      kullanılmıyor, ancak yine de bir dizi protokol işleyicisi için
      ayarlanmış.
    - `PROTOPT_DIRLOCK` - yön kilidi. SSH protokolleri, ana motorun
      kendisiyle ilgilendiği soket eylemlerinin hangi yönünü sınırlamak
      için bu biti ayarlar.
    - `PROTOPT_NONETWORK` - ağı kullanmayan bir protokol (`file:` okuma)
    - `PROTOPT_NEEDSPWD` - bu protokol bir parolaya ihtiyaç duyar ve bir
      tane sağlanmadıkça varsayılan bir tane kullanır
    - `PROTOPT_NOURLQUERY` - bu protokol URL'deki bir sorgu parçasını
      işleyemez (?foo=bar)

## conncache

  Daha sonra yeniden kullanılmak üzere bağlantıları olan bir karma tablosudur. Her `Curl_easy`'nin kendi bağlantı önbelleğine bir işaretçisi vardır. Her multi handle, eklenen tüm `Curl_easy`'lerin varsayılan olarak paylaştığı bir bağlantı önbelleği kurar.

## Curl_share

  libcurl paylaşım API'si, harici API'ye `CURLSH *` olarak sunulan bir `Curl_share` yapısı tahsis eder.

  Fikir, yapının kendi önbellek ve havuz sürümlerine sahip olabilmesi ve ardından bu yapıyı `CURLOPT_SHARE` seçeneğinde sağlayarak, bu belirli `Curl_easy`'lerin bu paylaşım handle'ının tuttuğu önbellekleri/havuzları kullanmasıdır.

  Daha sonra bireysel `Curl_easy` yapıları, aksi takdirde paylaşmayacakları çerezler gibi belirli şeyleri paylaşacak şekilde yapılabilir.

  `Curl_share` yapısı şu anda çerezleri, DNS önbelleğini ve SSL oturum önbelleğini tutabilir.

## CookieInfo

  Bu ana çerez yapısıdır. Bilinen tüm çerezleri ve ilgili bilgileri tutar. Bir multi handle'a eklendiklerinde bile her `Curl_easy`'nin kendi özel `CookieInfo`'su vardır. Paylaşım API'si kullanılarak çerezleri paylaşmaları sağlanabilir.
