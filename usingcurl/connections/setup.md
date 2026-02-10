# Kurulum

Kullanıcının bağlantıların nasıl kurulacağının farklı yönlerini kontrol etmesini sağlayan birkaç seçenek vardır.

## VLAN

`--vlan-priority` komut satırı seçeneğiyle Ethernet başlığında ayarlanan 0 ile 7 arasında bir öncelik değeri belirlersiniz. Bu nedenle yalnızca yerel ağınızla sınırlıdır ve herhangi bir yönlendiricide (router) kullanılmayacaktır.

IEEE 802.1Q'da tanımlandığı gibi VLAN önceliği.

Örnek:

    curl --vlan-priority 4 https://example.com

## Hizmet Türü (Type of Service)

IPv4 protokol başlığında bir "Hizmet Türü (TOS)" alanı bulunur. IPv6'da buna "Trafik Sınıfı" denir. Bir kullanıcı `--ip-tos` seçeneğini kullanarak değeri sıfır ile 255 arasında sayısal bir değere veya tanınan adlardan birini kullanarak ayarlayabilir:

    CS0, CS1, CS2, CS3, CS4, CS5, CS6, CS7, AF11, AF12, AF13,
    AF21, AF22, AF23, AF31, AF32, AF33, AF41, AF42, AF43, EF,
    VOICE-ADMIT, ECT1, ECT0, CE, LE, LOWCOST, LOWDELAY,
    THROUGHPUT, RELIABILITY, MINCOST

Örnek:

    curl --ip-tos CS5 https://example.com

## Multipath TCP

Multipath TCP, sıradan TCP'nin kullandığı normal tek yola kıyasla, verimi en üst düzeye çıkarmak ve yedekliliği artırmak için bir TCP bağlantısının birden fazla eşzamanlı ağ yolunu kullanmasının bir yoludur.

`--mptcp` seçeneğiyle curl'den Multipath TCP kullanmasını isteyebilirsiniz. Yalnızca Linux'ta çalışır ve Linux 5.6 veya üstünü gerektirir. QUIC veya UDP bağlantıları üzerinde hiçbir etkisi yoktur.

curl'ün bağlandığı sunucunun da MPTCP'yi desteklemesi gerekir. Değilse, bağlantı sorunsuz bir şekilde "normal" TCP'ye geri döner.

Örnek:

    curl --mptcp https://example.com
