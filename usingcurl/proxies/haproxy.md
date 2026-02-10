# haproxy

haproxy protokolü, adında hala proxy (vekil sunucu) olsa da, diğer vekil sunucu seçeneklerinden farklıdır ve vekil sunucularla diğer vekil sunucu seçeneklerinin çalıştığı şekilde çalışmaz.

Bu, trafiğin ona nasıl ulaştığına bakılmaksızın bir istemcinin IP adresini sunucuya iletmesinin bir yoludur: tüneller, TCP vekil sunucuları, yük dengeleyiciler, şeffaf vekil sunucular ve ne varsa. Trafik sunucuya ulaştığında hangi kaynak IP adresinin kullanıldığını bir şekilde değiştiren hizmetler, sunucunun istemcinin IP adresini kendi başına bulmasını imkansız hale getirir.

haproxy protokolü basittir. Sunucu tarafından desteklenmesi gerekir, yani bir kullanıcı isteksiz veya işbirliği yapmayan bir sunucuyla bunu kullanmaya karar veremez. *Desteklerse*, curl'e kendi IP adresini sunucuya iletmek için bunu kullanmasını söyleyebilirsiniz.

## curl ve haproxy

curl yalnızca haproxy protokolü v1'i destekler.

Şu anda kullanılmakta olan bağlantının gerçek IP adresini iletmek için, şu şekilde boolean bayrağını eklemeniz yeterlidir:

    curl --haproxy-protocol https://example.com/

Böyle bir komut satırı bir nedenden dolayı iletmesi gerektiğini düşündüğünüz IP adresini sağlamıyorsa, bir IPv4 veya bir IPv6 sayısal adresi kullanarak tam adresi kendiniz belirtebilirsiniz:

    curl --haproxy-clientip 10.0.0.1 https://example.com/
    curl --haproxy-clientip fe80::fea3:8a22 https://example.com/
