# Ayrıntılı operasyonlar

Tamam, hatayı insan tarafından okunabilir bir metin olarak nasıl alacağımızı gösterdik, çünkü bu belirli bir transferde neyin yanlış gittiğini anlamak için mükemmel bir yardımdır ve genellikle neden böyle yapılabileceğini veya o anki sorunun ne olduğunu açıklar.

libcurl uygulamaları geliştirirken herkesin bilmesi ve kapsamlı bir şekilde kullanması gereken bir sonraki cankurtaran, en azından libcurl uygulamaları geliştirirken veya libcurl'ün kendisinde hata ayıklarken, `CURLOPT_VERBOSE` ile ayrıntılı (verbose) modu etkinleştirmektir:

    CURLcode ret = curl_easy_setopt(handle, CURLOPT_VERBOSE, 1L);

libcurl'e ayrıntılı olması söylendiğinde, transfer devam ederken transferle ilgili ayrıntıları ve bilgileri stderr'e verir. Bu, işlerin neden başarısız olduğunu anlamak ve ona farklı şeyler sorduğunuzda libcurl'ün tam olarak ne yaptığını öğrenmek için harikadır. `CURLOPT_STDERR` ile stderr'i değiştirerek çıktıyı başka bir yere yönlendirebilir veya hata ayıklama geri çağırımı (debug callback) (sonraki bir bölümde daha ayrıntılı açıklanacaktır) ile daha süslü bir şekilde daha fazla bilgi alabilirsiniz.

## Her şeyi izle

Ayrıntılı kesinlikle iyidir, ancak bazen daha fazlasına ihtiyacınız olur. libcurl ayrıca, ayrıntılı modun yaptığı her şeyi size göstermenin yanı sıra, gönderilen ve alınan *tüm* verileri de ileten bir izleme geri çağırımı (trace callback) sunar, böylece uygulamanız her şeyin tam bir izini alır.

İzleme geri çağırımına iletilen gönderilen ve alınan veriler, geri çağırıma şifrelenmemiş biçimde verilir; bu, ağdan verileri yakalamanın hata ayıklama için pratik olmadığı durumlarda TLS veya SSH tabanlı protokollerle çalışırken kullanışlı olabilir.

`CURLOPT_DEBUGFUNCTION` seçeneğini ayarladığınızda, yine de `CURLOPT_VERBOSE`'un etkinleştirilmiş olması gerekir ancak izleme geri çağırımı ayarlandığında, libcurl dahili işlemi yerine o geri çağırımı kullanır.

İzleme geri çağırımı şuna benzer bir prototiple eşleşmelidir:

    int my_trace(CURL *handle, curl_infotype type, char *data, size_t size,
                 void *user);

**handle** ilgili easy handle'dır, **type** geri çağırıma iletilen belirli veriyi tanımlar (veri giriş/çıkış, başlık giriş/çıkış, TLS veri giriş/çıkış ve metin), **data**, **size** bayt sayısı kadar olan verilere işaret eden bir işaretçidir. **user**, `CURLOPT_DEBUGDATA` ile ayarladığınız özel işaretçidir.

**data** tarafından işaret edilen veriler null ile sonlandırılmış *değildir*, ancak tam olarak **size** argümanıyla belirtilen boyuttadır.

Geri çağırım 0 döndürmelidir, aksi takdirde libcurl bunu bir hata olarak kabul eder ve transferi iptal eder.

curl web sitesinde, ilham almak için basit bir izleme işlevi içeren [debug.c](https://curl.se/libcurl/c/debug.html) adında bir örnek barındırıyoruz.

Ayrıca [CURLOPT_DEBUGFUNCTION man sayfasında](https://curl.se/libcurl/c/CURLOPT_DEBUGFUNCTION.html) ek ayrıntılar da mevcuttur.

## Transfer ve bağlantı tanımlayıcıları

Hata ayıklama geri çağırımına geçen izleme bilgi akışı sürekli bir akış olduğundan, uygulamanız libcurl'ün çok sayıda ayrı bağlantı ve farklı transfer kullanmasını sağlasa bile, çeşitli bilgilerin hangi belirli transferlere veya bağlantılara ait olduğunu görmek istediğiniz zamanlar vardır. İzleme çıktısını daha iyi anlamak için.

Daha sonra transfer ve bağlantı tanımlayıcılarını geri çağırımın içinden alabilirsiniz:

    curl_off_t conn_id;
    curl_off_t xfer_id;
    res = curl_easy_getinfo(curl, CURLINFO_CONN_ID, &conn_id);
    res = curl_easy_getinfo(curl, CURLINFO_XFER_ID, &xfer_id);

Bunlar iki ayrı tanımlayıcıdır çünkü bağlantılar yeniden kullanılabilir ve birden fazla transfer aynı bağlantıyı kullanabilir. Bu tanımlayıcıları (gerçekte sayılar) kullanarak, hangi günlüklerin hangi transferler ve bağlantılarla ilişkili olduğunu görebilirsiniz.

## Daha fazlasını izle

Hata ayıklama geri çağırımına iletilen varsayılan izleme verisi miktarı yeterli değilse. Daha temel bir alt protokol seviyesinde bir sorundan şüphelendiğinizde ve hata ayıklamak istediğinizde, libcurl sizin için `curl_global_trace()` işlevini sağlar.

Bu işlevle libcurl'e, aksi takdirde varsayılan olarak dahil etmediği bileşenler hakkında ayrıntılı günlük kaydı da eklemesini söylersiniz. TLS, HTTP/2 veya HTTP/3 protokol parçaları hakkındaki ayrıntılar gibi.

`curl_global_trace()` işlevleri, izlemesini istediğiniz alanları içeren virgülle ayrılmış bir liste tutan bir dize belirttiğiniz bir argüman alır. Örneğin, TLS ve HTTP/2 ayrıntılarını dahil edin:

    /* HTTP/2 ve SSL işlemenin ayrıntılarını günlüğe kaydet */
    curl_global_trace("http/2,ssl");

Tam seçenek seti değişir, ancak denenecek bazıları şunlardır:

| alan     | açıklama                                        |
|----------|-------------------------------------------------|
| `all`    | mümkün olan her şeyi göster                     |
| `tls`    | TLS protokol değişimi ayrıntıları               |
| `http/2` | HTTP/2 çerçeve bilgisi                          |
| `http/3` | HTTP/3 çerçeve bilgisi                          |
| `*`      | gelecek sürümlerde ek olanlar                   |

`all` ile hızlı bir çalıştırma yapmak, hangi belirli alanların gösterildiğini görmenin genellikle iyi bir yoludur, çünkü daha sonra daha spesifik alanlar ayarlanarak takip çalışmaları yapabilirsiniz.
