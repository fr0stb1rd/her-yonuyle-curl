# Port numarası

Her protokolün, belirtilen bir port numarası verilmediği sürece curl'ün kullandığı varsayılan bir port numarası vardır. İsteğe bağlı port numarası, ana bilgisayar adı kısmından sonra, iki nokta üst üste ve ondalık olarak yazılmış port numarası olarak URL içinde sağlanabilir. Örneğin, 8080 numaralı portta bir HTTP belgesi istemek:

    curl http://example.com:8080/

Ad bir IPv4 adresi olarak belirtildiğinde:

    curl http://127.0.0.1:8080/

Ad bir IPv6 adresi olarak verildiğinde:

    curl http://[fdea::1]:8080/

Port numarası işaretsiz 16 bitlik bir sayıdır, bu nedenle 0 ila 65535 aralığında olması gerekir.

## TCP vs UDP

Verilen port numarası, URL'de belirtilen sunucuyla bağlantı kurulurken kullanılır. Port, kullanılan gerçek temel taşıma protokolüne bağlı olarak bir TCP port numarası veya bir UDP port numarasıdır. TCP en yaygın olanıdır, ancak TFTP ve HTTP/3 UDP kullanır.

`file://` şemasını kullanan URL'ler bir port numarasına sahip olamaz.
