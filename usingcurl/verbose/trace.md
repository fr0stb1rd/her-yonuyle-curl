# İzleme seçenekleri (Trace options)

`-v`'nin yeterli olmadığı zamanlar vardır. Özellikle, iletilen gerçek veriler de dahil olmak üzere tüm akışı depolamak istediğinizde.

curl'ün HTTPS, FTPS veya SFTP gibi protokollerle şifreli dosya transferleri yaptığı durumlar için, diğer ağ izleme araçları (Wireshark veya tcpdump gibi) bu işi sizin için o kadar kolay yapamaz.

Bunun için curl, `-v` yerine kullanabileceğiniz iki seçenek daha sunar.

`--trace [dosyaadı]`, verilen dosya adına tam bir iz kaydeder. Ayrıca stdout'a (standart çıktı) geçirilmesi için dosya adı yerine '-' (tek bir eksi) de kullanabilirsiniz. Bunu şöyle kullanırsınız:

    $ curl --trace dump http://example.com

Tamamlandığında, oldukça büyük olabilecek bir 'dump' dosyası oluşur. Bu durumda, döküm dosyasının ilk 15 satırı şöyle görünür:

    == Info: Rebuilt URL to: http://example.com/
    == Info:   Trying 93.184.216.34...
    == Info: Connected to example.com (93.184.216.34) port 80 (#0)
    => Send header, 75 bytes (0x4b)
    0000: 47 45 54 20 2f 20 48 54 54 50 2f 31 2e 31 0d 0a GET / HTTP/1.1..
    0010: 48 6f 73 74 3a 20 65 78 61 6d 70 6c 65 2e 63 6f Host: example.co
    0020: 6d 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 63 m..User-Agent: c
    0030: 75 72 6c 2f 37 2e 34 35 2e 30 0d 0a 41 63 63 65 url/7.45.0..Acce
    0040: 70 74 3a 20 2a 2f 2a 0d 0a 0d 0a                pt: */*....
    <= Recv header, 17 bytes (0x11)
    0000: 48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d HTTP/1.1 200 OK.
    0010: 0a                                              .
    <= Recv header, 22 bytes (0x16)
    0000: 41 63 63 65 70 74 2d 52 61 6e 67 65 73 3a 20 62 Accept-Ranges: b
    0010: 79 74 65 73 0d 0a                               ytes..

Gönderilen ve alınan her bir bayt, onaltılık sayılarla ayrı ayrı görüntülenir. Alınan başlıklar satır satır çıktılanır.

Onaltılık sayıların yardımcı olmadığını düşünüyorsanız, bunun yerine `--trace-ascii [dosyaadı]` seçeneğini deneyebilirsiniz; bu da stdout için '-' kabul eder ve izlemenin ilk 15 satırının şöyle görünmesini sağlar:

    == Info: Rebuilt URL to: http://example.com/
    == Info:   Trying 93.184.216.34...
    == Info: Connected to example.com (93.184.216.34) port 80 (#0)
    => Send header, 75 bytes (0x4b)
    0000: GET / HTTP/1.1
    0010: Host: example.com
    0023: User-Agent: curl/7.45.0
    003c: Accept: */*
    0049:
    <= Recv header, 17 bytes (0x11)
    0000: HTTP/1.1 200 OK
    <= Recv header, 22 bytes (0x16)
    0000: Accept-Ranges: bytes
    <= Recv header, 31 bytes (0x1f)
    0000: Cache-Control: max-age=604800

## Zaman damgaları

`--trace-time` seçeneği, satırın ne zaman yazdırıldığına dair yüksek çözünürlüklü bir zamanlayıcı ile tüm ayrıntılı/izleme çıktılarına önek ekler. Bu, `--trace` ve `--trace-ascii` ile olduğu kadar normal `-v / --verbose` seçeneğiyle de çalışır.

Bir örnek şöyle görünebilir:

    $ curl -v --trace-time http://example.com
    23:38:56.837164 * Rebuilt URL to: http://example.com/
    23:38:56.841456 *   Trying 93.184.216.34...
    23:38:56.935155 * Connected to example.com (93.184.216.34) port 80 (#0)
    23:38:56.935296 > GET / HTTP/1.1
    23:38:56.935296 > Host: example.com
    23:38:56.935296 > User-Agent: curl/7.45.0
    23:38:56.935296 > Accept: */*
    23:38:56.935296 >
    23:38:57.029570 < HTTP/1.1 200 OK
    23:38:57.029699 < Accept-Ranges: bytes
    23:38:57.029803 < Cache-Control: max-age=604800
    23:38:57.029903 < Content-Type: text/html
    ---- snip ----

Satırların hepsi saat:dakika:saniye ve ardından o saniyedeki mikrosaniye sayısı olarak yerel saattir.

## Transferleri ve bağlantıları tanımlayın

Bu seçenekleri kullanarak ekranda veya bir dosyada gösterilen izleme bilgi akışı sürekli bir akış olduğundan, komut satırınız curl'ün çok sayıda ayrı bağlantı ve farklı transfer kullanmasına neden olsa bile, aşağıdaki çeşitli bilgilerin hangi belirli transferlere veya bağlantılara ait olduğunu görmek istediğiniz zamanlar olabilir. İzleme çıktısını daha iyi anlamak için.

O zaman satıra `--trace-ids` ekleyebilirsiniz ve curl'ün tüm izleme işlemlerine iki numara eklediğini görürsünüz: bağlantı numarası ve transfer numarası. Bunlar iki ayrı tanımlayıcıdır çünkü bağlantılar yeniden kullanılabilir ve birden fazla transfer aynı bağlantıyı kullanabilir.

## Daha fazla veri

İzleme verisi miktarı yeterli değilse. Örneğin, daha temel bir alt protokol seviyesinde bir sorundan şüphelendiğinizde ve hata ayıklamak istediğinizde curl sizin için `--trace-config` seçeneğini sunar.

Bu seçenekle curl'e, TLS, HTTP/2 veya HTTP/3 protokol bitleri hakkındaki ayrıntılar gibi varsayılan olarak dahil etmediği bileşenler hakkında günlüğe kaydetmeyi de dahil etmesini söylersiniz. Ayrıca bağlantı ve transfer tanımlayıcılarını ve zaman damgalarını eklemek için kolaylık seçeneklerine de sahiptir.

`--trace-config` seçeneği, izlemesini istediğiniz alanlarla virgülle ayrılmış bir liste belirttiğiniz bir argümanı kabul eder. Örneğin, tanımlayıcıları dahil edin ve bana HTTP/2 ayrıntılarını gösterin:

    curl --trace-config ids,http/2 https://example.com

Seçeneklerin tam seti değişir, ancak deneyebileceğiniz bazıları şunlardır:

| alan     | açıklama                                        |
|----------|-------------------------------------------------|
| `ids`    | `--trace-ids` ile aynı tanımlayıcıları sağlar   |
| `time`   | `--trace-time` ile aynı zaman çıktısını sağlar  |
| `all`    | mümkün olan her şeyi göster                     |
| `tls`    | TLS protokol değişimi ayrıntıları               |
| `http/2` | HTTP/2 çerçeve bilgisi                          |
| `http/3` | HTTP/3 çerçeve bilgisi                          |
| `*`      | gelecek sürümlerdeki ek olanlar                 |

`all` ile hızlı bir çalıştırma yapmak, hangi belirli alanların gösterildiğini görmek için genellikle iyi bir yoldur, çünkü o zaman daha belirli alanlar ayarlanmış olarak takip çalışmaları yapabilirsiniz.
