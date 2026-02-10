# curl protokolleri

curl yaklaşık 28 protokolü destekler. *Yaklaşık* diyoruz çünkü bu, nasıl saydığınıza ve neleri belirgin şekilde farklı protokoller olarak kabul ettiğinize bağlıdır.

## DICT

DICT bir sözlük (dictionary) ağ protokolüdür, istemcilerin sözlük sunucularına kelimelerin anlamı veya açıklaması hakkında soru sormasına olanak tanır. Bkz. RFC 2229. Dict sunucuları ve istemcileri 2628 numaralı TCP portunu kullanır.

## FILE

FILE aslında bir *ağ* protokolü değildir. curl'e bir dosyayı uzak bir sunucudan ağ üzerinden almak yerine yerel dosya sisteminden almasını söylemenizi sağlayan bir URL şemasıdır. Bkz. RFC 1738.

## FTP

FTP, Dosya Transfer Protokolü (File Transfer Protocol) anlamına gelir ve dosyaları bir istemci ile sunucu arasında ileri geri aktarmanın eski (kökeni 1970'lerin başına dayanır) bir yoludur. Bkz. RFC 959. Yıllar içinde büyük ölçüde genişletilmiştir. FTP sunucuları ve istemcileri 21 numaralı TCP portunu ve bir port daha kullanır, ancak ikincisi genellikle iletişim sırasında dinamik olarak kurulur.

HTTP'den farkı için [FTP vs HTTP](https://daniel.haxx.se/docs/ftp-vs-http.html) harici sayfasına bakın.

## FTPS

FTPS, Güvenli Dosya Transfer Protokolü (Secure File Transfer Protocol) anlamına gelir. Protokolün normal FTP gibi yapıldığını ancak eklenmiş bir SSL/TLS güvenlik katmanıyla yapıldığını belirtmek için protokol adına bir 'S' ekleme geleneğini izler. Bkz. RFC 4217.

Bu protokolün güvenlik duvarları ve diğer ağ ekipmanları aracılığıyla kullanımı sorunludur.

## GOPHER

"İnternet üzerinden belgeleri dağıtmak, aramak ve almak" için tasarlanan Gopher, HTTP'nin aynı kullanım durumları için çoğunlukla tamamen devralması nedeniyle HTTP'nin büyükbabası sayılır. Bkz. RFC 1436. Gopher sunucuları ve istemcileri 70 numaralı TCP portunu kullanır.

## GOPHERS

TLS üzerinden Gopher. Eski protokole yeni bir uzantı.

## HTTP

Hiper Metin Transfer Protokolü (Hypertext Transfer Protocol), HTTP, web'de ve İnternet üzerinden veri aktarımı için en yaygın kullanılan protokoldür. Genel HTTP Semantiği için RFC 9110, HTTP/1.1 için RFC 9112, [HTTP/2](../http/versions/http2.md) için RFC 9113 ve HTTP/3 için RFC 9114'e bakın. HTTP sunucuları ve istemcileri 80 numaralı TCP portunu kullanır.

## HTTPS

Güvenli (Secure) HTTP, bir SSL/TLS bağlantısı üzerinden yapılan HTTP'dir. Bkz. RFC 2818. HTTPS sunucuları ve istemcileri, QUIC (RFC 8999) kullanan ve UDP üzerinden yapılan [HTTP/3](../http/versions/http3.md) konuşmadıkları sürece 443 numaralı TCP portunu kullanır.

## IMAP

İnternet Mesaj Erişim Protokolü (Internet Message Access Protocol), IMAP, e-postaya erişmek, kontrol etmek ve "okumak" için bir protokoldür. Bkz. RFC 3501. IMAP sunucuları ve istemcileri 143 numaralı TCP portunu kullanır. Sunucuya bağlantılar açık metin (cleartext) olarak başlasa da, istemci `STARTTLS` komutunu kullanarak bağlantıyı yükseltmeyi (upgrade) açıkça talep ederek SSL/TLS iletişimini destekleyebilir. Bkz. RFC 2595.

## IMAPS

Güvenli IMAP, bir SSL/TLS bağlantısı üzerinden yapılan IMAP'tir. Bu tür bağlantılar örtük olarak SSL/TLS kullanarak başlar ve bu nedenle sunucular ve istemciler birbirleriyle iletişim kurmak için 993 numaralı TCP portunu kullanır. Bkz. RFC 8314.

## LDAP

Hafif Dizin Erişim Protokolü (Lightweight Directory Access Protocol), LDAP, dağıtılmış dizin bilgilerine erişmek ve bunları sürdürmek için bir protokoldür. Temelde bir veritabanı aramasıdır. Bkz. RFC 4511. LDAP sunucuları ve istemcileri 389 numaralı TCP portunu kullanır.

## LDAPS

Güvenli LDAP, bir SSL/TLS bağlantısı üzerinden yapılan LDAP'tir.

## MQTT

Mesaj Kuyruğu Telemetri Taşıma (Message Queuing Telemetry Transport), MQTT, çoğunlukla daha küçük cihazları içeren veri alışverişi için IoT sistemlerinde yaygın olarak kullanılan bir protokoldür. Sözde bir "yayınla-abone ol" (publish-subscribe) protokolüdür.

## POP3

Postane Protokolü sürüm 3 (Post Office Protocol version 3 - POP3), bir sunucudan e-posta almak için bir protokoldür. Bkz. RFC 1939. POP3 sunucuları ve istemcileri 110 numaralı TCP portunu kullanır. Sunucuya bağlantılar açık metin olarak başlasa da, istemci `STLS` komutunu kullanarak bağlantıyı yükseltmeyi açıkça talep ederek SSL/TLS iletişimini destekleyebilir. Bkz. RFC 2595.

## POP3S

Güvenli POP3, bir SSL/TLS bağlantısı üzerinden yapılan POP3'tür. Bu tür bağlantılar örtük olarak SSL/TLS kullanarak başlar ve bu nedenle sunucular ve istemciler birbirleriyle iletişim kurmak için 995 numaralı TCP portunu kullanır. Bkz. RFC 8314.

## RTMP

Gerçek Zamanlı Mesajlaşma Protokolü (Real-Time Messaging Protocol - RTMP), ses, video ve veri akışı (streaming) için bir protokoldür. RTMP sunucuları ve istemcileri 1935 numaralı TCP portunu kullanır.

## RTSP

Gerçek Zamanlı Akış Protokolü (Real Time Streaming Protocol - RTSP), akış ortamı (streaming media) sunucularını kontrol etmek için bir ağ kontrol protokolüdür. Bkz. RFC 2326. RTSP sunucuları ve istemcileri 554 numaralı TCP ve UDP portunu kullanır.

## SCP

Güvenli Kopyalama (Secure Copy - SCP) protokolü, dosyaları uzak bir SSH sunucusuna ve sunucusundan kopyalamak için tasarlanmıştır. SCP sunucuları ve istemcileri 22 numaralı TCP portunu kullanır.

## SFTP

Güvenilir bir veri akışı üzerinden dosya erişimi, dosya transferi ve dosya yönetimi sağlayan SSH Dosya Transfer Protokolü (SSH File Transfer Protocol - SFTP). SFTP sunucuları ve istemcileri 22 numaralı TCP portunu kullanır.

## SMB

Sunucu Mesaj Bloğu (Server Message Block - SMB) protokolü CIFS olarak da bilinir. Esas olarak dosyalara, yazıcılara ve seri portlara paylaşımlı erişim sağlamak ve bir ağdaki düğümler arasında çeşitli iletişimler için kullanılan bir uygulama katmanı ağ protokolüdür. SMB sunucuları ve istemcileri 445 numaralı TCP portunu kullanır.

## SMBS

TLS üzerinden yapılan SMB.

## SMTP

Basit Posta Transfer Protokolü (Simple Mail Transfer Protocol - SMTP), e-posta iletimi için bir protokoldür. Bkz. RFC 5321. SMTP sunucuları ve istemcileri 25 numaralı TCP portunu kullanır. Sunucuya bağlantılar açık metin olarak başlasa da, istemci `STARTTLS` komutunu kullanarak bağlantıyı yükseltmeyi açıkça talep ederek SSL/TLS iletişimini destekleyebilir. Bkz. RFC 3207.

## SMTPS

Güvenli SMTP, bir SSL/TLS bağlantısı üzerinden yapılan SMTP'dir. Bu tür bağlantılar örtük olarak SSL/TLS kullanarak başlar ve bu nedenle sunucular ve istemciler birbirleriyle iletişim kurmak için 465 numaralı TCP portunu kullanır. Bkz. RFC 8314.

## TELNET

TELNET, sanal bir terminal bağlantısı kullanarak çift yönlü etkileşimli metin odaklı bir iletişim tesisi sağlamak için ağlar üzerinden kullanılan bir uygulama katmanı protokolüdür. Bkz. RFC 854. TELNET sunucuları ve istemcileri 23 numaralı TCP portunu kullanır.

## TFTP

Önemsiz Dosya Transfer Protokolü (Trivial File Transfer Protocol - TFTP), uzak bir ana bilgisayardan dosya almak veya dosya koymak için UDP üzerinden basit dosya transferleri yapmak için bir protokoldür. TFTP sunucuları ve istemcileri 69 numaralı UDP portunu kullanır.

## WS

WebSocket, bir HTTP(S) isteği üzerinden kurulan çift yönlü TCP benzeri bir protokoldür. WS, düz HTTP üzerinden yapılan açık metin sürümü için şemadır.

## WSS

WebSocket, bir HTTP(S) isteği üzerinden kurulan çift yönlü TCP benzeri bir protokoldür. WSS, HTTPS üzerinden yapılan güvenli sürüm için şemadır.
