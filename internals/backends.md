# Arka uçlar (Backends)

curl'deki bir arka uç, **derleme zamanında seçilebilir alternatif bir uygulamadır**.

curl'ü derlediğinizde, birkaç farklı şey için alternatif uygulamalar seçebilirsiniz. Aynı özellik setinin farklı sağlayıcıları. curl'ü derlediğinizde hangi arka ucu veya arka uçları (çoğul) kullanacağınızı seçersiniz.

- Arka uçlar seçilebilir ve seçimi kaldırılabilir
- Genellikle platforma bağımlıdır
- Özelliklerde farklılık gösterebilir
- 3. taraf lisanslarında farklılık gösterebilir
- Olgunlukta farklılık gösterebilir
- Dahili API'ler asla harici olarak ifşa edilmez

## Farklı arka uçlar

libcurl kaynak kodunda, işlevsellik sağlamak için dahili API'ler vardır. Bu farklı alanlarda birden fazla farklı sağlayıcı vardır:

1. IDN
2. İsim çözümleme
3. TLS
4. SSH
6. HTTP/3
7. HTTP içerik kodlaması

## Görselleştirilmiş arka uçlar

![libcurl arka uçları](slide-libcurl-backends.jpg)

Uygulamalar (üstteki yeşil bulutta) libcurl'e genel API aracılığıyla erişir. API sabit ve kararlıdır.

Dahili olarak, libcurl'ün çekirdeği, yapması gereken farklı görevleri gerçekleştirmek için dahili API'leri kullanır. Bu dahili API'lerin her biri, çoğu zaman farklı üçüncü taraf kütüphaneler tarafından desteklenen alternatif uygulamalar tarafından desteklenir.

Yukarıdaki resim, farklı dahili API'leri destekleyen farklı üçüncü taraf kütüphaneleri göstermektedir. Mor kutular bir veya daha fazladır ve koyu gri olanlar "bunlardan biri"dir.

## HTTP/3 arka uçları

![HTTP/3 arka uçları](slide-http3-backends.jpg)

libcurl, bu resimde farklı sütunlar olarak görselleştirilen dört farklı arka uç sunar.

Her satırın belirli bir arka uç derlemesi olduğu bir tablodaki aynı veriler:

| durum        | HTTP/3 kütüphanesi | QUIC kütüphanesi | TLS kütüphaneleri (bir tanesi) |
|--------------|--------------------|------------------|--------------------------------|
| önerilen     | nghttp3            | ngtcp2           | fork ailesi, GnuTLS veya wolfSSL |
| deneysel     | quiche             | quiche           | BoringSSL veya quictls           |
| deneysel     | msh3               | msquic           | fork ailesi veya Schannel        |
| deneysel     | nghttp3            | OpenSSL 3.3.0+   | OpenSSL 3.3.0+                 |

*fork ailesi*, BoringSSL, LibreSSL, quictls ve AWS-LC anlamına gelir
