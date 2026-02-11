# SOCKS vekil sunucusu

SOCKS vekil sunucular için kullanılan bir protokoldür ve curl bunu destekler. curl hem SOCKS sürüm 4'ü hem de sürüm 5'i destekler ve her iki sürüm de iki çeşitte gelir.

Verilen vekil sunucu ana bilgisayarı için `-x` ile doğru şema parçasını kullanarak veya `-x` yerine ayrı bir seçenekle belirterek kullanılacak belirli SOCKS sürümünü seçebilirsiniz.

SOCKS4, sürüm 4 içindir ancak curl adı çözer:

    curl -x socks4://proxy.example.com http://www.example.com/

    curl --socks4 proxy.example.com http://www.example.com/

SOCKS4a, çözümlemenin vekil sunucu tarafından yapıldığı sürüm 4 içindir:

    curl -x socks4a://proxy.example.com http://www.example.com/

    curl --socks4a proxy.example.com http://www.example.com/

SOCKS5, sürüm 5 içindir ve SOCKS5-hostname, ana bilgisayar adını yerel olarak çözmeden sürüm 5 içindir:

    curl -x socks5://proxy.example.com http://www.example.com/

    curl --socks5 proxy.example.com http://www.example.com/

SOCKS5-hostname sürümleri. Bu, ana bilgisayar adını vekil sunucuya gönderir, böylece curl tarafından yerel olarak yapılan bir isim çözümlemesi yoktur:

    curl -x socks5h://proxy.example.com http://www.example.com/

    curl --socks5-hostname proxy.example.com http://www.example.com/

Hangi socks sürümü için ismin hangi taraf tarafından çözüldüğünü anlamak için yararlı tablo:

| SOCKS | ismi kim çözer | IPv6 ile çalışır mı |
|-------|----------------|---------------------|
| 4     | curl           | hayır               |
| 4a    | vekil sunucu   | hayır               |
| 5     | curl           | evet                |
| 5h    | vekil sunucu   | evet                |
