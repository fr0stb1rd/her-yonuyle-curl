# Yazdır (Write out)

`--write-out` veya kısaca `-w`, bir transfer tamamlandıktan sonra metin ve bilgi çıktılar (yazdırır). Çıktıya dahil edebileceğiniz, değerlerle ve transferden gelen bilgilerle ayarlanmış çok sayıda değişken sunar.

Bu seçeneğe düz metin ileterek curl'den bir dize çıktılamasını isteyin:

    curl -w "formatted string" http://example.com/

…ve dizeyi '@' ile öncelerseniz curl'ün o dizeyi verilen bir dosyadan okumasını da sağlayabilirsiniz:

    curl -w @filename http://example.com/

…veya dosya adı olarak '-' kullanırsanız curl'ün dizeyi stdin'den okumasını bile sağlayabilirsiniz:

    curl -w @- http://example.com/

## Değişkenler

Mevcut olan değişkenlere dizeye `%{degisken_adi}` yazılarak erişilir ve bu değişken doğru değerle değiştirilir. Düz bir `%` çıktılamak için `%%` olarak yazarsınız. Ayrıca `\n` kullanarak yeni bir satır, `\r` ile satır başı ve `\t` ile bir sekme boşluğu çıktılayabilirsiniz.

Örnek olarak, bir HTTP transferinden Content-Type'ı ve yanıt kodunu, yeni satırlarla ve bunun gibi bazı ekstra metinlerle ayrılmış olarak çıktılayabiliriz:

    curl -w "Type: %{content_type}\nCode: %{response_code}\n" \
      http://example.com

Çıktı varsayılan olarak stdout'a gönderilir, bu nedenle indirilen içeriği de stdout'a göndermediğinizden emin olmak isteyebilirsiniz, aksi takdirde verileri ayırmakta zorlanabilirsiniz; veya çıktıyı stderr'e göndermek için `%{stderr}` kullanın.

## HTTP başlıkları

Bu seçenek ayrıca, en son transferden gelen HTTP yanıt başlıklarının içeriğini çıktılamanın kolay bir yolunu da sağlar.

Dizede `%header{isim}` kullanın; burada `isim`, başlığın büyük/küçük harfe duyarlı olmayan adıdır (sondaki iki nokta üst üste olmadan). Çıktı başlık içerikleri daha sonra ağ üzerinden gönderildiği gibi tam olarak gösterilir, baştaki ve sondaki boşluklar kırpılır. Şöyle:

    curl -w "Server: %header{server}\n" http://example.com

## Çıktı

Varsayılan olarak, bu seçenek seçilen verilerin stdout'ta çıktılamasını sağlar. Bu yeterince iyi değilse, `%{stderr}` sözde değişkeni (aşağıdaki) kısmı stderr'e yönlendirmek için kullanılabilir ve `%{stdout}` onu tekrar stdout'a getirir.

curl 8.3.0'dan itibaren, kullanıcıların write-out çıktısını bir dosyaya göndermesine olanak tanıyan bir özellik vardır: `%output{dosyaadı}`. Takip eden veriler daha sonra o dosyaya yazılır. curl'ün dosyayı sıfırdan oluşturmak yerine o dosyaya eklemesini tercih ederseniz, dosya adının önüne `>>` ekleyin. Şöyle: `%output{>>dosyaadı}`.

Bir write-out argümanı, kullanıcının uygun gördüğü şekilde stderr, stdout ve dosyalara çıktı içerebilir.

## Windows

**NOT:** Windows'ta `%` sembolü, ortam değişkenlerini genişletmek için kullanılan özel bir semboldür. Toplu işlem (batch) dosyalarında, bu seçeneği kullanırken düzgün bir şekilde kaçmak için tüm `%` oluşumları iki katına çıkarılmalıdır. Bu seçenek komut isteminde (command prompt) kullanılırsa `%` kaçılamaz ve istenmeyen genişletme mümkündür.

## Mevcut --write-out değişkenleri

Bu değişkenlerin bazıları gerçekten eski curl sürümlerinde mevcut değildir.

| Değişken                  | Açıklama                                                                                                                                                                                                                         |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `certs`                   | En son TLS el sıkışmasından sertifika zincirini çıktılar - ayrıntılarla birlikte. (7.88.0'da tanıtıldı)                                                                                                                          |
| `conn_id`                 | Transfer tarafından en son kullanılan bağlantı tanımlayıcısı. Bağlantı kimliği, aynı bağlantı önbelleğini kullanan tüm bağlantılar arasında benzersiz bir sayıdır. (8.2.0'da tanıtıldı)                                          |
| `content_type`            | İstek yapılan belgenin Content-Type'ı, eğer varsa.                                                                                                                                                                               |
| `errormsg`                | Transferden gelen hata mesajı. Hata oluşmadıysa boş. (7.75.0'da tanıtıldı)                                                                                                                                                       |
| `exitcode`                | Transferden gelen sayısal çıkış kodu. Hata oluşmadıysa 0. (7.75.0'da tanıtıldı)                                                                                                                                                  |
| `filename_effective`      | curl'ün yazdığı nihai dosya adı. curl'e `--remote-name` veya `--output` seçeneğiyle bir dosyaya yazması söylendiğinde pratiktir. En çok `--remote-header-name` seçeneğiyle birlikte kullanıldığında yararlıdır.                  |
| `ftp_entry_path`          | Uzak FTP sunucusunda oturum açıldığında curl'ün son bulduğu ilk yol.                                                                                                                                                             |
| `header_json`             | Son transferden gelen tüm HTTP yanıt başlıklarını içeren bir JSON nesnesi. Değerler diziler olarak sağlanır, çünkü birden fazla başlık olması durumunda birden fazla değer olabilir. (7.83.0'da tanıtıldı)                       |
| `http_code`               | Artık `response_code` olarak bilinen şeyin eski değişken adı.                                                                                                                                                                    |
| `http_connect`            | Bir curl CONNECT isteğine (bir vekil sunucudan) son yanıtta bulunan sayısal kod.                                                                                                                                                 |
| `http_version`            | Kullanılan HTTP sürümü.                                                                                                                                                                                                          |
| `json`                    | Tek bir JSON nesnesi olarak tüm write-out değişkenleri. (7.72.0'da tanıtıldı)                                                                                                                                                    |
| `local_ip`                | En son kullanılan bağlantının yerel ucunun IP adresi - IPv4 veya IPv6 olabilir                                                                                                                                                   |
| `local_port`              | En son kullanılan bağlantının yerel port numarası                                                                                                                                                                                |
| `method`                  | En son isteğin kullandığı HTTP yöntemi. (7.72.0'da tanıtıldı)                                                                                                                                                                    |
| `num_certs`               | En son TLS el sıkışmasındaki sertifika sayısı. (7.88.0'da tanıtıldı)                                                                                                                                                             |
| `num_connects`            | Son transferde yapılan yeni bağlantıların sayısı.                                                                                                                                                                                |
| `num_headers`             | Son yanıttaki yanıt başlıklarının sayısı                                                                                                                                                                                         |
| `num_redirects`           | İstekte takip edilen yönlendirme sayısı.                                                                                                                                                                                         |
| `num_retries`             | `--retry` kullanıldığında gerçekten gerçekleştirilen yeniden deneme sayısı. (8.9.0'da tanıtıldı)                                                                                                                                 |
| `onerror`                 | Transfer bir hatayla sonuçlandıysa, dizenin geri kalanını göster, aksi takdirde burada dur. (7.75.0'da tanıtıldı)                                                                                                                |
| `proxy_ssl_verify_result` | Bir vekil sunucuyla iletişim kurarken istenen SSL eş sertifika doğrulamasının sonucu. 0, doğrulamanın başarılı olduğu anlamına gelir.                                                                                            |
| `proxy_used`              | Önceki transfer bir vekil sunucu kullandıysa 1, aksi takdirde 0 döndürür. Örneğin, bir `NOPROXY` deseninin ana bilgisayar adıyla eşleşip eşleşmediğini belirlemek için kullanışlıdır. (8.7.0'da tanıtıldı)                       |
| `redirect_url`            | Yönlendirmeleri takip etmek için `-L` olmadan bir HTTP isteği yapıldığında bir yönlendirmenin sizi _götüreceği_ gerçek URL.                                                                                                      |
| `referer`                 | Referer: başlığı, eğer varsa. (7.76.0'da tanıtıldı)                                                                                                                                                                              |
| `remote_ip`               | En son kullanılan bağlantının uzak IP adresi — IPv4 veya IPv6 olabilir.                                                                                                                                                          |
| `remote_port`             | En son yapılan bağlantının uzak port numarası.                                                                                                                                                                                   |
| `response_code`           | Son transferde bulunan sayısal yanıt kodu.                                                                                                                                                                                       |
| `scheme`                  | Önceki URL'de kullanılan şema                                                                                                                                                                                                    |
| `size_download`           | İndirilen toplam bayt sayısı.                                                                                                                                                                                                    |
| `size_header`             | İndirilen başlıkların toplam bayt sayısı.                                                                                                                                                                                        |
| `size_request`            | HTTP isteğinde gönderilen toplam bayt sayısı.                                                                                                                                                                                    |
| `size_upload`             | Yüklenen toplam bayt sayısı.                                                                                                                                                                                                     |
| `speed_download`          | curl'ün tam indirme için ölçtüğü saniyedeki bayt cinsinden ortalama indirme hızı.                                                                                                                                                |
| `speed_upload`            | curl'ün tam yükleme için ölçtüğü saniyedeki bayt cinsinden ortalama yükleme hızı.                                                                                                                                                |
| `ssl_verify_result`       | İstenen SSL eş sertifika doğrulamasının sonucu. 0, doğrulamanın başarılı olduğu anlamına gelir.                                                                                                                                  |
| `stderr`                  | Çıktının geri kalanının stderr'e yazılmasını sağlar.                                                                                                                                                                             |
| `stdout`                  | Çıktının geri kalanının stdout'a yazılmasını sağlar.                                                                                                                                                                             |
| `time_appconnect`         | Başlangıçtan uzak ana bilgisayara SSL/SSH/vb. bağlantı/el sıkışma tamamlanana kadar geçen saniye cinsinden süre.                                                                                                                 |
| `time_connect`            | Başlangıçtan uzak ana bilgisayara (veya vekil sunucuya) TCP bağlantısı tamamlanana kadar geçen saniye cinsinden süre.                                                                                                            |
| `time_namelookup`         | Başlangıçtan isim çözümleme tamamlanana kadar geçen saniye cinsinden süre.                                                                                                                                                       |
| `time_pretransfer`        | Başlangıçtan dosya transferi başlamak üzere olana kadar geçen saniye cinsinden süre. Bu, ilgili protokol(ler)e özgü tüm transfer öncesi komutları ve görüşmeleri içerir.                                                         |
| `time_redirect`           | Son işlem başlamadan önce isim arama, bağlanma, transfer öncesi ve transfer dahil tüm yönlendirme adımları için geçen saniye cinsinden süre. time\_redirect birden fazla yönlendirme için tam yürütme süresidir.                 |
| `time_starttransfer`      | Başlangıçtan ilk bayt transfer edilmek üzere olana kadar geçen saniye cinsinden süre. Bu, time\_pretransfer'i ve ayrıca sunucunun sonucu hesaplamak için ihtiyaç duyduğu süreyi içerir.                                          |
| `time_total`              | Tam işlemin sürdüğü saniye cinsinden toplam süre. Süre mikrosaniye çözünürlüğüyle görüntülenir.                                                                                                                                  |
| `url`                     | Transferde kullanılan URL. (7.75.0'da tanıtıldı)                                                                                                                                                                                 |
| `url_effective`           | En son getirilen URL. Bu, curl'e Location: başlıklarını takip etmesini söylediyseniz ( `-L` ile) özellikle anlamlıdır.                                                                                                           |
| `urlnum`                  | Transferde kullanılan URL'nin 0 tabanlı sayısal dizini. (7.75.0'da tanıtıldı)                                                                                                                                                    |
| `xfer_id`                 | Yapılan son transferin sayısal tanımlayıcısı. Tanıtıcı için henüz bir transfer başlatılmadıysa -1. Transfer kimliği, aynı bağlantı önbelleğini kullanarak gerçekleştirilen tüm transferler arasında benzersizdir. (8.2.0'da tanıtıldı) |

curl 8.1.0'da, `url` veya `url_effective` değişkenlerinin istediğinizden fazlasını gösterdiği durumlar için yalnızca belirli URL bileşenlerini çıktılama değişkenleri eklendi.

| Değişken        | Açıklama                                                                                                          |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| `url.fragment`  | Getirilen URL'nin bölüm (fragment) kısmı.                                                                         |
| `url.host`      | Getirilen URL'nin ana bilgisayar adı kısmı.                                                                       |
| `url.options`   | Getirilen URL'nin seçenekler kısmı. Yalnızca bazı şemalar için geçerlidir.                                        |
| `url.password`  | Getirilen URL'nin parola kısmı.                                                                                   |
| `url.path`      | Getirilen URL'nin yol (path) kısmı.                                                                               |
| `url.port`      | Getirilen URL'nin port numarası.                                                                                  |
| `url.query`     | Getirilen URL'nin sorgu kısmı.                                                                                    |
| `url.scheme`    | Getirilen URL'nin şema kısmı.                                                                                     |
| `url.user`      | Getirilen URL'nin kullanıcı kısmı.                                                                                |
| `url.zoneid`    | Getirilen URL'nin bölge kimliği (zone id) kısmı. Yalnızca ana bilgisayar adı bir IPv6 adresiyse mevcuttur.        |
| `urle.fragment` | Getirilen etkili (son) URL'nin bölüm kısmı.                                                                       |
| `urle.host`     | Getirilen etkili (son) URL'nin ana bilgisayar adı kısmı.                                                          |
| `urle.options`  | Getirilen etkili (son) URL'nin seçenekler kısmı. Yalnızca bazı şemalar için geçerlidir.                           |
| `urle.password` | Getirilen etkili (son) URL'nin parola kısmı.                                                                      |
| `urle.path`     | Getirilen etkili (son) URL'nin yol kısmı.                                                                         |
| `urle.port`     | Getirilen etkili (son) URL'nin port numarası.                                                                     |
| `urle.query`    | Getirilen etkili (son) URL'nin sorgu kısmı.                                                                       |
| `urle.scheme`   | Getirilen etkili (son) URL'nin şema kısmı.                                                                        |
| `urle.user`     | Getirilen etkili (son) URL'nin kullanıcı kısmı.                                                                   |
| `urle.zoneid`   | Getirilen etkili (son) URL'nin bölge kimliği kısmı. Yalnızca ana bilgisayar adı bir IPv6 adresiyse mevcuttur.     |
