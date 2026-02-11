# Ana bilgisayar (Host)

URL'nin ana bilgisayar adı kısmı, elbette, sayısal bir IP adresine çözümlenebilen basit bir ad veya sayısal adresin kendisidir.

    curl http://example.com

Sayısal bir adres belirtirken, IPv4 adresleri için noktalı sürümü kullanın:

    curl http://127.0.0.1/

…ve IPv6 adresleri için sayısal sürümün köşeli parantez içinde olması gerekir:

    curl http://[2a04:4e42::561]/

Bir ana bilgisayar adı kullanıldığında, adın bir IP adresine dönüştürülmesi tipik olarak sistemin çözümleyici (resolver) işlevleri kullanılarak yapılır. Bu normalde bir sistem yöneticisinin `/etc/hosts` dosyasında (veya eşdeğerinde) yerel ad aramaları sağlamasına izin verir.

## Uluslararası Alan Adları (IDN)

curl, IDN adlarıyla nasıl başa çıkacağını bilir ve bunları normal bir ad gibi iletirsiniz:

    curl https://räksmörgås.se
