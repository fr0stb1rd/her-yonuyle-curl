# TLS sürümleri

SSL 90'ların ortasında icat edildi ve o zamandan beri gelişti. SSL sürüm 2 İnternet'te kullanılan ilk yaygın sürümdü ancak uzun zaman önce güvenli olmadığı kabul edildi. Oradan SSL sürüm 3 devraldı ve o da kullanım için yeterince güvenli görülmedi.

TLS sürüm 1.0 ilk standarttı. RFC 2246, 1999'da yayınlandı. TLS 1.1, güvenliği daha da iyileştirerek 2006'da çıktı, ardından 2008'de TLS 1.2 geldi. TLS 1.2, on yıl boyunca TLS için altın standart haline geldi.

TLS 1.3 (RFC 8446), Ağustos 2018'de IETF tarafından bir standart olarak kesinleştirildi ve yayınlandı. Bu, bugüne kadarki en güvenli ve en hızlı TLS sürümüdür. Ancak o kadar yenidir ki birçok yazılım, araç ve kütüphane henüz desteklememektedir.

curl varsayılan olarak SSL/TLS'nin güvenli bir sürümünü kullanacak şekilde tasarlanmıştır. Bu, özellikle söylenmedikçe SSLv2 veya SSLv3'ü müzakere etmediği anlamına gelir ve aslında çeşitli TLS kütüphaneleri artık bu protokoller için destek sağlamadığından birçok durumda curl ciddi bir çaba sarf etmezseniz bu protokol sürümlerini konuşamaz bile.

| Seçenek   | Kullanım           |
|-----------|--------------------|
| --sslv2   | SSL sürüm 2        |
| --sslv3   | SSL sürüm 3        |
| --tlsv1   | TLS >= sürüm 1.0   |
| --tlsv1.0 | TLS >= sürüm 1.0   |
| --tlsv1.1 | TLS >= sürüm 1.1   |
| --tlsv1.2 | TLS >= sürüm 1.2   |
| --tlsv1.3 | TLS >= sürüm 1.3   |
