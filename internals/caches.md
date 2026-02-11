# Önbellekler ve durum (Caches and state)

libcurl İnternet transferleri için kullanıldığında, sonraki transferleri daha hızlı ve daha iyi yapmak için verileri önbelleklerde ve durum depolamasında saklar.

Önbellekler, hangi libcurl API'sinin kullanıldığına (easy veya multi) bağlı olarak `CURL` veya `CURLM` handle'larıyla ilişkili tutulur.

## DNS önbelleği (DNS cache)

libcurl bir ana bilgisayar adının IP adreslerini çözümlediğinde sonucu (varsayılan 60 saniyelik bir ömürle) DNS önbelleğinde saklar, böylece sonraki aramalar (potansiyel olarak yavaş) çözümleme işlemini tekrar yapmak yerine önbelleğe alınmış verileri hemen kullanabilir. Bu önbellek yalnızca bellekte bulunur.

## bağlantı önbelleği (connection cache)

Bağlantı havuzu olarak da bilinir. Burası, bir transfer tamamlandıktan sonra curl'ün canlı bağlantıları koyduğu yerdir, böylece sonraki bir transfer yeni bir tane kurmak zorunda kalmak yerine zaten mevcut bir bağlantıyı kullanabilir. Bir bağlantı yeniden kullanıldığında, curl ad aramalarından, TLS el sıkışmalarından ve daha fazlasından kaçınır. Bu önbellek yalnızca bellekte bulunur.

## TLS oturum-ID önbelleği (TLS session-ID cache)

curl TLS kullandığında, *oturum-ID*'yi bir önbellekte kaydeder. Sonraki bir transfer, önbelleğe alınmış bir oturum-ID'sine sahip olduğu bir ana bilgisayarla TLS el sıkışmasını tekrar yapması gerektiğinde, el sıkışması daha hızlı tamamlanabilir. Bu önbellek yalnızca bellekte bulunur.

## CA deposu önbelleği (CA store cache)

curl yeni bir bağlantı oluşturduğunda ve bir TLS el sıkışması gerçekleştirdiğinde, uzak sunucu tarafından sunulan sertifikayı doğrulamak için kullanmak üzere bir *CA deposu* yüklemesi ve ayrıştırması gerekir. CA deposu önbelleği, ayrıştırılmış CA deposunu bir süre (varsayılan 24 saattir) bellekte tutar, böylece sonraki el sıkışmalar bu potansiyel olarak büyük veri miktarını yeniden ayrıştırmak zorunda kalmayarak çok daha hızlı yapılır. Bu önbellek yalnızca bellekte bulunur. 7.87.0'da eklendi.

## HSTS

HSTS, HTTP Strict Transport Security'dir (HTTP Katı Taşıma Güvenliği). HTTPS sunucuları, istemcileri `HTTP://` URL'leri kullanılsa bile, ileriye dönük olarak kendi ana bilgisayar adlarına yalnızca HTTPS kullanarak ve HTTP kullanmadan bağlanmalarını istediklerini bildirebilirler. curl bu bağlantı yükseltme bilgilerini bellekte tutar ve diske kaydetmesi ve diskten yüklemesi de söylenebilir.

## Alt-Svc

`Alt-Svc:`, istemciyi aynı hizmetin de mevcut olduğu alternatif ana bilgisayar adları, port numaraları ve protokol sürümleri hakkında bilgilendiren bir HTTP yanıt başlığıdır. curl bu alternatif hizmet bilgilerini bellekte tutar ve diske kaydetmesi ve diskten yüklemesi de söylenebilir.

## Çerezler (Cookies)

Çerezler, bir HTTP sunucusundan istemciye gönderilen ve koşullarla eşleşen sonraki isteklerde geri gönderilmesi amaçlanan ad değer çiftleridir. curl tüm çerezleri bellekte tutar ve bunları diskten yüklemesi ve diske kaydetmesi de söylenebilir.
