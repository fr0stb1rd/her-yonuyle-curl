# Test dosya formatı

Her curl testi, XML benzeri bir format kullanılarak tek bir metin dosyasında tasarlanmıştır.

Etiketler tüm bölümlerin başlangıcını ve sonunu işaretler ve her etiket kendi satırına yazılmalıdır. Yorumlar XML tarzı (`<!--` ve `-->` ile çevrili) veya kabuk betiği tarzındadır (`#` ile başlayan) ve gerçek test verilerinin yanında değil kendi satırlarında görünmelidir. Çoğu test veri dosyası sözdizimsel olarak geçerli XML'dir, ancak birkaç dosya değildir (karakter varlıkları için destek eksikliği ve satır sonlarında satır başı ve satır besleme karakterlerinin korunması en büyük farklardır).

Tüm testler, dosyanın geri kalanını kapsayan bir `<testcase>` etiketiyle başlamalıdır. Diğer etiketler için aşağıya bakın.

Her test dosyası `tests/data/testNUMBER` olarak adlandırılır, burada `NUMBER` benzersiz bir sayısal test tanımlayıcısıdır. Her testin kendi özel numarasını kullanması gerekir. Sayının testi tanımlamak dışında bir anlamı yoktur.

Test dosyası, tam olarak hangi komut satırının veya aracın çalıştırılacağını, hangi test sunucularının çağrılacağını ve nasıl yanıt vermeleri gerektiğini, tam olarak hangi protokol değişiminin gerçekleşmesi gerektiğini, hangi çıktı ve dönüş kodunun beklendiğini ve çok daha fazlasını tanımlar.

İsim ayarlandığında her şey aşağıdaki gibi kendi özel etiketlerinin içine yazılır:

    <name>
    HTTP with host name written backwards
    </name>

## anahtar kelimeler (keywords)

Her testin dosyanın en üstünde ayarlanmış bir veya daha fazla `<keywords>` vardır. Bunlar, bu test senaryosu tarafından test edilen özellik ve protokolleri tanımlayan "etiketler" olması amaçlanmıştır. `runtests.pl`, yalnızca bu tür anahtar kelimelerle eşleşen (veya eşleşmeyen) testleri çalıştıracak şekilde yapılabilir.

## Önceden işlenmiş (Preprocessed)

Kaputun altında, her test girdi dosyası `runtests.pl` tarafından başlangıçta *önceden işlenir*. Bu, değişkenlerin, makroların ve anahtar kelimelerin genişletildiği ve dosyanın geçici bir sürümünün `tests/log/testNUMBER` içinde saklandığı anlamına gelir - ve *o* dosya daha sonra tüm test sunucuları vb. tarafından kullanılır.

Bu işlem, test formatının girdi dosyalarını buna karşılık gelen şekilde şişirmeden gerçekten büyük test dosyaları oluşturmak için `%repeat` gibi özellikler sunmasına olanak tanır.

## Base64 Kodlama

Ön işlem aşamasında, runtests.pl'nin belirli bir bölümü base64 kodlamasını ve oluşturulan çıktı dosyasına eklemesini sağlamak için özel bir talimat kullanılabilir. Bu, test aracının sunucu port numarası gibi bu belirli test çağrısı için benzersiz olan dinamik bilgileri kullanabilecek base64 kodlu içeriği iletmesinin beklendiği test durumları için özellikle iyidir.

Çıktıya base64 kodlu bir dize eklemek için şu sözdizimini kullanın:

    %b64[ kodlanacak veri ]b64%

Kodlanacak veri daha sonra aşağıda belirtilen mevcut değişkenlerden herhangi birini veya hatta yüzde kodlu bireysel baytları kullanabilir. Örnek olarak, HTTP sunucusunun port numarasını (ASCII olarak) ve ardından bir boşluk ve onaltılık bayt 9a'yı ekleyin:

    %b64[%HTTPPORT %9a]b64%

## Onaltılık şifre çözme (Hexadecimal decoding)

Ön işlem aşamasında, runtests.pl'nin bir ikili bayt dizisi oluşturmasını sağlamak için özel bir talimat kullanılabilir.

Hex kodlu bir dizeden bir bayt dizisi eklemek için şu sözdizimini kullanın:

    %hex[ şifresi çözülecek %XX-kodlu veri ]hex%

Örneğin, test dosyasına ikili sekizliler 0, 1 ve 255'i eklemek için:

    %hex[ %00%01%FF ]hex%

## İçeriği tekrarlama (Repeat content)

Ön işlem aşamasında, runtests.pl'nin tekrarlayan bir bayt dizisi oluşturmasını sağlamak için özel bir talimat kullanılabilir.

Bir tekrar bayt dizisi eklemek için, `<string>`'in `<number>` kez tekrarlanmasını sağlamak üzere şu sözdizimini kullanın. Sayı 1 veya daha büyük olmalıdır ve dize `%HH` onaltılık kodlar içerebilir:

    %repeat[<number> x <string>]%

Örneğin, hello kelimesini 100 kez eklemek için:

    %repeat[100 x hello]%

## Koşullu satırlar (Conditional lines)

Test dosyasındaki satırlar, belirli bir özelliğin (aşağıdaki "özellikler" bölümüne bakın) ayarlanıp ayarlanmadığına bağlı olarak koşullu olarak görünebilir. Belirli özellik mevcutsa, aşağıdaki satırlar çıkarılır, aksi takdirde bir sonraki `else` veya `endif` cümlesine kadar hiçbir şey çıkarmaz. Şunun gibi:

    %if brotli
    Accept-Encoding
    %endif

Ayrıca ters koşulu da kontrol edebilir, bu nedenle özellik bir ünlem işareti kullanılarak *ayarlanmamışsa*:

    %if !brotli
    Accept-Encoding: not-brotli
    %endif

Karşıt durum için çıktı almak üzere bir "else" cümlesi de yapabilirsiniz, şöyle:

    %if brotli
    Accept-Encoding: brotli
    %else
    Accept-Encoding: nothing
    %endif

**Not** içiçe geçmiş koşullar olamaz. Bir seferde yalnızca bir koşullu yapabilirsiniz ve içinde yalnızca tek bir özelliği kontrol edebilirsiniz.

## Değişkenler (Variables)

Test önceden işlendiğinde, test dosyasındaki bir dizi değişken o andaki içerikleriyle değiştirilir.

Mevcut ikame değişkenleri şunları içerir:

- `%CLIENT6IP` - curl çalıştıran istemcinin IPv6 adresi
- `%CLIENTIP` - curl çalıştıran istemcinin IPv4 adresi
- `%CURL` - curl çalıştırılabilir dosyasının yolu
- `%FILE_PWD` - Geçerli dizin, windows'ta başında bir eğik çizgi ile
- `%FTP6PORT` - FTP sunucusunun IPv6 port numarası
- `%FTPPORT` - FTP sunucusunun port numarası
- `%FTPSPORT` - FTPS sunucusunun port numarası
- `%FTPTIME2` - Test FTP sunucusundan bir yanıt almak için yeterli olması gereken saniye cinsinden zaman aşımı
- `%FTPTIME3` - `%FTPTIME2`'den daha da uzun
- `%GOPHER6PORT` - Gopher sunucusunun IPv6 port numarası
- `%GOPHERPORT` - Gopher sunucusunun port numarası
- `%GOPHERSPORT` - Gophers sunucusunun port numarası
- `%HOST6IP` - Bu testi çalıştıran ana bilgisayarın IPv6 adresi
- `%HOSTIP` - Bu testi çalıştıran ana bilgisayarın IPv4 adresi
- `%HTTP6PORT` - HTTP sunucusunun IPv6 port numarası
- `%HTTPPORT` - HTTP sunucusunun port numarası
- `%HTTP2PORT` - HTTP/2 sunucusunun port numarası
- `%HTTPSPORT` - HTTPS sunucusunun port numarası
- `%HTTPSPROXYPORT` - HTTPS vekil sunucusunun port numarası
- `%HTTPTLS6PORT` - HTTP TLS sunucusunun IPv6 port numarası
- `%HTTPTLSPORT` - HTTP TLS sunucusunun port numarası
- `%HTTPUNIXPATH` - HTTP sunucusunun Unix soketine giden yol
- `%SOCKSUNIXPATH` - SOCKS sunucusunun Unix soketine mutlak yol
- `%IMAP6PORT` - IMAP sunucusunun IPv6 port numarası
- `%IMAPPORT` - IMAP sunucusunun port numarası
- `%MQTTPORT` - MQTT sunucusunun port numarası
- `%TELNETPORT` - telnet sunucusunun port numarası
- `%NOLISTENPORT` - Hiçbir servisin dinlemediği port numarası
- `%POP36PORT` - POP3 sunucusunun IPv6 port numarası
- `%POP3PORT` - POP3 sunucusunun port numarası
- `%POSIX_PWD` - Geçerli dizin biraz mingw dostu
- `%PROXYPORT` - HTTP vekil sunucusunun port numarası
- `%PWD` - Geçerli dizin
- `%RTSP6PORT` - RTSP sunucusunun IPv6 port numarası
- `%RTSPPORT` - RTSP sunucusunun port numarası
- `%SMBPORT` - SMB sunucusunun port numarası
- `%SMBSPORT` - SMBS sunucusunun port numarası
- `%SMTP6PORT` - SMTP sunucusunun IPv6 port numarası
- `%SMTPPORT` - SMTP sunucusunun port numarası
- `%SOCKSPORT` - SOCKS4/5 sunucusunun port numarası
- `%SRCDIR` - Kaynak dizinine tam yol
- `%SSHPORT` - SCP/SFTP sunucusunun port numarası
- `%SSHSRVMD5` - SSH sunucusunun genel anahtarının MD5'i
- `%SSHSRVSHA256` - SSH sunucusunun genel anahtarının SHA256'sı
- `%SSH_PWD` - SSH sunucusu için dostu geçerli dizin
- `%TESTNUMBER` - Test senaryosunun numarası
- `%TFTP6PORT` - TFTP sunucusunun IPv6 port numarası
- `%TFTPPORT` - TFTP sunucusunun port numarası
- `%USER` - Testi çalıştıran kullanıcının Oturum Açma Kimliği
- `%VERSION` - test edilen curl'ün tam sürüm numarası

# Etiketler (Tags)

Her test her zaman tamamen `<testcase>` etiketi içinde belirtilir. Her test senaryosu ayrıca dört ana bölüme ayrılır: `info`, `reply`, `client` ve `verify`.

- **info** test senaryosu hakkında bilgi sağlar

- **reply**, sunucunun curl'ün gönderdiği isteklere yanıt olarak ne göndereceğini bilmesi için kullanılır

- **client**, istemcinin nasıl davranması gerektiğini tanımlar

- **verify**, bir komut çalıştırıldıktan sonra saklanan verilerin doğru şekilde sonuçlandığını nasıl doğrulayacağınızı tanımlar

Her ana bölüm, belirtilebilen ve belirtilirse kontrol edilen/kullanılan bir dizi mevcut *alt etiketi* destekler.

## `<info>`

### `<keywords>`

Bu test senaryosunun neyi kullandığını ve test ettiğini açıklayan yeni satırla ayrılmış bir anahtar kelime listesi. Zaten kullanılmış anahtar kelimeleri kullanmaya çalışın. Bu anahtar kelimeler istatistiksel/bilgilendirme amaçlıdır ve test sınıflarını seçmek veya atlamak içindir. "Anahtar kelimeler" alfabetik bir karakter, "-", "[" veya "{" ile başlamalı ve tek bir tanımlayıcı olarak birlikte ele alınan boşluklarla ayrılmış birden fazla kelimeden oluşabilir.

## `<reply>`

### `<data [nocheck="yes"] [sendzero="yes"] [base64="yes"] [hex="yes"] [nonewline="yes"]>`

İsteği üzerine istemciye gönderilecek ve daha sonra güvenli bir şekilde ulaştığı doğrulanacak veriler. Test betiğinin bu verilerin gelişini doğrulamasını önlemek için `nocheck="yes"` olarak ayarlayın.

Veriler başlangıç ve bitiş etiketi içinde herhangi bir yerde `swsclose` içeriyorsa ve bu bir HTTP testiyse, bu yanıt gönderildikten sonra sunucu tarafından bağlantı kapatılır. Değilse, bağlantı kalıcı tutulur.

Veriler başlangıç ve bitiş etiketi içinde herhangi bir yerde `swsbounce` içeriyorsa, HTTP sunucusu bunun aynı test ve parça numarasını kullanan ikinci bir istek olup olmadığını algılar ve ardından parça numarasını bir artırır. Bu, kimlik doğrulama testleri ve benzerleri için yararlıdır.

`sendzero=yes`, boyut sıfır bayt olsa bile (FTP) sunucusunun verileri "gönderdiği" anlamına gelir. curl'ün sıfır bayt transferlerindeki davranışını doğrulamak için kullanılır.

`base64=yes`, test dosyasında sağlanan verilerin base64 ile kodlanmış bir veri yığını olduğu anlamına gelir. Bir test senaryosunun ikili veriler içerebilmesinin tek yolu budur. (Bu öznitelik aslında herhangi bir bölümde kullanılabilir, ancak "data" dışındaki diğer bölümler için pek mantıklı değildir).

`hex=yes`, verilerin onaltılık çiftlerin bir dizisi olduğu anlamına gelir. Kodu çözülür ve "ham" veri olarak kullanılır.

`nonewline=yes`, son baytın (sondaki yeni satır karakteri) göndermeden veya karşılaştırmadan önce verilerden kesilmesi gerektiği anlamına gelir.

FTP dosya listeleri için, `<data>` bölümü *yalnızca* önce `test-[number]` adlı bir dizine CWD yapıldığından eminseniz kullanılır; burada `[number]` test senaryosu numarasıdır. Aksi takdirde ftp sunucusu liste içeriğini hangi test dosyasından yükleyeceğini bilemez.

### `<dataNUMBER>`

`<data>` yerine bu içeriği geri gönderin. `NUMBER` sayısı şu şekilde ayarlanır:

 - İstek satırındaki test numarası >10000 ve bu [test senaryosu numarası]%10000'in kalanıdır.
 - İstek HTTP idi ve 1000 sayısını ekleyen özet (digest) ayrıntılarını içeriyordu
 - Bir HTTP isteği NTLM tip-1 ise, sayıya 1001 ekler
 - Bir HTTP isteği NTLM tip-3 ise, sayıya 1002 ekler
 - Bir HTTP isteği Temel (Basic) ve sayı zaten >=1000 ise, 1 ekler
 - Bir HTTP isteği Negotiate ise, aynı test senaryosunda Negotiate yetkilendirme başlığına sahip her istek için sayı bir artırılır.

Test numarasını bu şekilde dinamik olarak değiştirmek, test donanımının bir transferi tamamlamak için birkaç farklı isteğin gönderilmesi gereken kimlik doğrulama müzakeresini test etmek için kullanılmasına olanak tanır. Her isteğe verilen yanıt kendi veri bölümünde bulunur. Tüm müzakere sırasını doğrulamak bir `datacheck` bölümü belirterek yapılabilir.

### `<connect>`

Connect bölümü, tüm CONNECT istekleri için 'data' yerine kullanılır. Veri bölümü kurallarının geri kalanı o zaman geçerlidir ancak bir connect öneki ile.

### `<socks>`

SOCKS vekil sunucusu tarafından kaydedilen adres türü ve adres ayrıntıları.

### `<datacheck [mode="text"] [nonewline="yes"]>`

veriler gönderilir ancak daha sonra kontrol edilmesi gereken şey budur. `nonewline=yes` ayarlanırsa, runtests istemci tarafından gerçekten alınanla karşılaştırmadan önce verilerden sondaki yeni satırı keser.

Metin/ikili farkı olan platformlarda çıktı metin modundaysa `mode="text"` özniteliğini kullanın.

### `<datacheckNUM [nonewline="yes"] [mode="text"]>`

Numaralandırılmış `datacheck` bölümlerinin içeriği numaralandırılmamış olana eklenir.

### `<size>`

bir ftp SIZE komutunda döndürülecek sayı (bu komutun başarısız olmasını sağlamak için -1'e ayarlayın)

### `<mdtm>`

İstemci bir FTP `MDTM` komutu gönderirse ne geri gönderilecek, dosyanın mevcut olmadığını döndürmesi için -1'e ayarlayın

### `<postcmd>`

yanıt gönderildikten *sonra* davranışını kontrol etmek için özel amaçlı sunucu komutu
HTTP/HTTPS için bunlar desteklenir:

`wait [saniye]` - Belirtilen süre boyunca duraklat

### `<servercmd>`

Sunucu için özel komutlar.

Bu dosyanın ilk satırı, sunucuların istemcinin hangi testi yapmak üzere olduğunu bilmek için bunu okumasına izin vermek üzere test betiği tarafından her zaman `Testnum [number]` olarak ayarlanır.

#### FTP/SMTP/POP/IMAP İçin

- `REPLY [komut] [dönüş değeri] [yanıt dizesi]` - Sunucunun [komut]'a nasıl yanıt vereceğini değiştirir. [yanıt dizesi] bir perl dizesi olarak değerlendirilir, böylece örneğin gömülü `\r\n` içerebilir. Bağlantıda bir karşılama olarak hemen gönderilen dize olan "welcome" (tırnak işaretleri olmadan) adında özel bir [komut] vardır.
- `REPLYLF` (yukarıdaki gibi ama yanıtı CRLF yerine yalnızca LF ile sonlandırılmış olarak gönderir)
- `COUNT [komut] [sayı]` - `REPLY` değişikliğini `[komut]` için yalnızca `[sayı]` kez yapın ve ardından yerleşik yaklaşıma geri dönün
- `DELAY [komut] [saniye]` - Bu komuta yanıt vermeyi belirtilen süre kadar geciktirin
- `RETRWEIRDO` - Bir dosya transfer edildiğinde birden fazla yanıt satırı aynı anda göründüğünde "weirdo" (tuhaf) RETR durumunu etkinleştirin
- `RETRNOSIZE` - RETR yanıtının dosyanın boyutunu içermediğinden emin olun
- `NOSAVE` - Alınanları kaydetmeyin
- `SLOWDOWN` - FTP yanıtlarını her bayt arasında 0,01 saniye gecikmeyle gönderin
- `PASVBADIP` - PASV'nin 227 yanıtında yasadışı bir IP geri göndermesini sağlar
- `CAPA [yetenekler]` - IMAP `CAPABILITY`, POP3 `CAPA` ve SMTP `EHLO` komutları için istemciye döndürülecek boşlukla ayrılmış yetenekler listesini belirtir ve desteği etkinleştirir
- `AUTH [mekanizmalar]` - SASL kimlik doğrulaması desteğini etkinleştirir ve IMAP, POP3 ve SMTP için boşlukla ayrılmış mekanizmaların bir listesini belirtir
- `STOR [mesaj]` - `STOR`'dan sonra varsayılan yerine bununla yanıt verin

#### HTTP/HTTPS İçin

- `auth_required` bu ayarlanmışsa ve kimlik doğrulama olmadan bir POST/PUT yapılırsa, sunucu tam istek gövdesinin gönderilmesini BEKLEMEZ
- `idle` - isteği aldıktan sonra hiçbir şey yapma, sadece "boşta otur"
- `stream` - istemciye sürekli veri gönder, hiç bitmeyen
- `writedelay: [milisaniye]` - yanıt paketleri arasında bu miktar kadar gecik
- `skip: [sayı]` - sunucuya bir PUT veya POST isteğinden bu kadar bayt okumayı görmezden gelmesini talimat verir
- `rtp: part [sayı] channel [sayı] size [sayı]` - verilen yük boyutu ile seçilen bir kanalda verilen parça için sahte bir RTP paketi yayınla
- `connection-monitor` - Kullanıldığında, bağlantı kesildiğinde `server.input` günlüğüne `[DISCONNECT]` kaydeder.
- `upgrade` - bir HTTP yükseltme başlığı bulunduğunda, sunucu http2'ye yükseltir
- `swsclose` - yanıttan sonra sunucuya bağlantıyı kapatmasını talimat ver
- `no-expect` - Expect: mevcutsa istek gövdesini okuma

#### TFTP İçin

`writedelay: [saniye]` yanıt paketleri arasında bu miktar kadar gecik (her paket 512 bayt yük olmak üzere)

## `<client>`

### `<server>`

Bu test senaryosunun gerektirdiği/kullandığı sunucu(lar). Mevcut sunucular:

- `file`
- `ftp-ipv6`
- `ftp`
- `ftps`
- `gopher`
- `gophers`
- `http-ipv6`
- `http-proxy`
- `http-unix`
- `http/2`
- `http`
- `https`
- `httptls+srp-ipv6`
- `httptls+srp`
- `imap`
- `mqtt`
- `none`
- `pop3`
- `rtsp-ipv6`
- `rtsp`
- `scp`
- `sftp`
- `smtp`
- `socks4`
- `socks5`

Satır başına yalnızca bir sunucu girin. Bu alt bölüm zorunludur.

### `<features>`

Bu testin çalışabilmesi için istemcide/kütüphanede mevcut OLMASI GEREKEN özelliklerin bir listesi. Gerekli bir özellik mevcut değilse test ATLANIR.

Alternatif olarak, bir özelliğin gerekli OLMADIĞINI belirtmek için bir özelliğin önüne ünlem işareti konabilir. Özellik mevcutsa test ATLANIR.

Burada test edilebilir özellikler şunlardır:

- `alt-svc`
- `bearssl`
- `c-ares`
- `cookies`
- `crypto`
- `debug`
- `DoH`
- `getrlimit`
- `GnuTLS`
- `GSS-API`
- `h2c`
- `HSTS`
- `HTTP-auth`
- `http/2`
- `idn`
- `ipv6`
- `Kerberos`
- `large_file`
- `ld_preload`
- `libssh2`
- `libssh`
- `oldlibssh` (0.9.4 öncesi sürümler)
- `libz`
- `manual`
- `Mime`
- `netrc`
- `NTLM`
- `OpenSSL`
- `parsedate`
- `proxy`
- `PSL`
- `rustls`
- `Schannel`
- `sectransp`
- `shuffle-dns`
- `socks`
- `SPNEGO`
- `SSL`
- `SSLpinning`
- `SSPI`
- `threaded-resolver`
- `TLS-SRP`
- `TrackMemory`
- `typecheck`
- `Unicode`
- `unittest`
- `unix-sockets`
- `verbose-strings`
- `wakeup`
- `win32`
- `wolfssh`
- `wolfssl`

curl'ün desteklediği tüm protokollere ek olarak. Bir protokolün yalnızca sunucudan farklıysa belirtilmesi gerekir (sunucu `none` olduğunda yararlıdır).

### `<killserver>`

`<server>` ile aynı sözdizimini kullanarak, ancak burada belirtildiğinde bu sunucular bu test senaryosu tamamlandığında açıkça ÖLDÜRÜLÜR. Bunu yalnızca başka alternatif yoksa kullanın. Bunu kullanmak elbette sonraki testlerin sunucuları yeniden başlatmasını gerektirir.

### `<precheck>`

Test betiği tarafından testten önce çalıştırılmak üzere ayarlanan bir komut satırı. Komut tarafından bir çıktı görüntülenirse veya dönüş kodu sıfır değilse, test atlanır ve (tek satırlık) çıktı testi çalıştırmama nedeni olarak görüntülenir.

### `<postcheck>`

Test betiği tarafından testten sonra çalıştırılmak üzere ayarlanan bir komut satırı. Komut sıfır olmayan bir durum koduyla mevcutsa, test başarısız kabul edilir.

### `<tool>`

"curl" yerine çağrılacak aracın adı. Bu araç oluşturulmalı ve `libtest/` dizininde (araç adı `lib` ile başlıyorsa) veya `unit/` dizininde (araç adı `unit` ile başlıyorsa) bulunmalıdır.

### `<name>`

Kısa test senaryosu açıklaması, test çalışırken gösterilir.

### `<setenv>`

    variable1=contents1
    variable2=contents2

Gerçek komut çalıştırılmadan önce verilen ortam değişkenlerini belirtilen değere ayarlayın. Komut çalıştırıldıktan sonra tekrar temizlenirler.

### `<command [option="no-output/no-include/force-output/binary-trace"] [timeout="secs"][delay="secs"][type="perl/shell"]>`

Çalıştırılacak komut satırı.

Sunucuya iletilen URL'in aslında hangi verilerin döndürüleceğini kontrol ettiğini unutmayın. URL'deki son eğik çizgi bir sayı ile takip edilmelidir. Bu sayı (N), test sunucusu tarafından test senaryosu N'yi yüklemek ve `<reply><data></data></reply>` bölümünde tanımlanan verileri döndürmek için kullanılır.

Yukarıda test numarası bulunamazsa, HTTP test sunucusu verilen ana bilgisayar adındaki son noktadan sonraki sayıyı kullanır (böylece bir CONNECT yine de test numarasını geçebilir), böylece "foo.bar.123" test senaryosu 123 olarak ele alınır. Alternatif olarak, CONNECT'e bir IPv6 adresi sağlanırsa, adresteki son onaltılık grup test numarası olarak kullanılır. Örneğin "[1234::ff]" adresi test senaryosu 255 olarak ele alınır.

`type="perl"` ayarlayarak test senaryosunu bir perl betiği olarak yazın. Bu test için bellek hatası ayıklamanın olmadığını ve valgrind'in kapatıldığını ima eder.

`type="shell"` ayarlayarak test senaryosunu bir kabuk betiği olarak yazın. Bu test için bellek hatası ayıklamanın olmadığını ve valgrind'in kapatıldığını ima eder.

`option="no-output"` ayarlayarak test betiğinin çıktıyı bir dosyaya yönlendiren `--output` argümanını eklemesini önleyin. verify/stdout bölümü kullanılıyorsa `--output` da eklenmez.

`option="force-output"` ayarlayarak testin stdout'u doğrulamak için yazıldığı durumlarda bile `--output` kullanımını sağlayın.

`option="no-include"` ayarlayarak test betiğinin `--include` argümanını eklemesini önleyin.

`option="binary-trace"` ayarlayarak izleme için `--trace-ascii` yerine `--trace` kullanın. MQTT gibi ikili yönelimli protokoller için uygundur.

`timeout="saniye"` ayarlayarak varsayılan sunucu günlükleri danışmanı okuma kilidi zaman aşımını geçersiz kılın. Bu zaman aşımı, komut yürütmeyi tamamladıktan sonra test donanımı tarafından test sunucusunun sunucu tarafı günlük dosyalarını yazmasını ve bunları okumamasını tavsiye eden kilidi kaldırmasını beklemek için kullanılır. "Saniye" parametresi, zaman aşımı için negatif olmayan tam sayı saniye sayısıdır. Bu `timeout` özniteliği bütünlük adına belgelenmiştir, ancak derin test donanımı işidir ve yalnızca belirli test durumları için gereklidir. Kullanmaktan kaçının.

`delay="saniye"` ayarlayarak komut yürütmeyi tamamladıktan sonra ve `<postcheck>` bölümü çalışmadan önce bir zaman gecikmesi ekleyin. "Saniye" parametresi, gecikme için negatif olmayan tam sayı saniye sayısıdır. Bu 'delay' özniteliği belirli test durumları için tasarlanmıştır ve normalde gerekli değildir.

### `<file name="log/filename" [nonewline="yes"]>`

Bu, test senaryosu çalıştırılmadan önce bu içerikle adlandırılan dosyayı oluşturur; bu, test senaryosunun üzerinde işlem yapması gereken bir dosyaya ihtiyacı varsa kullanışlıdır.

`nonewline="yes"` kullanılırsa, oluşturulan dosyanın sonundaki yeni satır soyulur.

### `<stdin [nonewline="yes"]>`

Bu verilen verileri stdin üzerinden araca iletin.

`nonewline` ayarlanırsa, istemci tarafından gerçekten alınanla karşılaştırmadan önce bu verilen verilerin sondaki yeni satırını keseriz.

## `<verify>`

### `<errorcode>`

curl'ün döndürmesi gereken sayısal hata kodu. Birden fazla sayıyı virgülle ayırarak kabul edilen hata kodlarının bir listesini belirtin. Bir örnek için test 237'ye bakın.

### `<strip>`

Karşılaştırma yapılmadan önce protokol dökümlerinden kaldırılan satır başına bir regex. Bu, port numaraları veya kullanıcı aracısı (user-agent) dizeleri gibi dinamik olarak değişen protokol verilerine olan bağımlılıkları kaldırmak için yararlıdır.

### `<strippart>`

Protokol dökümü üzerinde çalışan satır başına bir perl op. Bu oldukça gelişmiştir. Örnek: `s/^EPRT .*/EPRT stripped/`.

### `<protocol [nonewline="yes"]>`

curl'ün iletmesi gereken protokol dökümü, `nonewline` ayarlanırsa, istemci tarafından gerçekten gönderilenle karşılaştırmadan önce bu verilen verilerin sondaki yeni satırını keseriz `<strip>` ve `<strippart>` kuralları karşılaştırmalar yapılmadan önce uygulanır.

### `<proxy [nonewline="yes"]>`

curl'ün bir HTTP vekil sunucusuna (http-proxy sunucusu kullanıldığında) iletmesi gereken protokol dökümü, `nonewline` ayarlanırsa, istemci tarafından gerçekten gönderilenle karşılaştırmadan önce bu verilen verilerin sondaki yeni satırını keseriz `<strip>` ve `<strippart>` kuralları karşılaştırmalar yapılmadan önce uygulanır.

### `<stderr [mode="text"] [nonewline="yes"]>`

Bu, bu verilerin stderr'e geçirildiğini doğrular.

Metin/ikili farkı olan platformlarda çıktı metin modundaysa `mode="text"` özniteliğini kullanın.

`nonewline` ayarlanırsa, istemci tarafından gerçekten alınanla karşılaştırmadan önce bu verilen verilerin sondaki yeni satırını keseriz.

### `<stdout [mode="text"] [nonewline="yes"]>`

Bu, bu verilerin stdout'a geçirildiğini doğrular.

Metin/ikili farkı olan platformlarda çıktı metin modundaysa `mode="text"` özniteliğini kullanın.

`nonewline` ayarlanırsa, istemci tarafından gerçekten alınanla karşılaştırmadan önce bu verilen verilerin sondaki yeni satırını keseriz.

### `<file name="log/filename" [mode="text"]>`

Dosyanın içeriği test tamamlandıktan sonra bununla aynı olmalıdır. Metin/ikili farkı olan platformlarda çıktı metin modundaysa `mode="text"` özniteliğini kullanın.

### `<file1>`

Daha fazla dosyayı karşılaştırmak için 'file'a 1 ila 4 eklenebilir.

### `<file2>`

### `<file3>`

### `<file4>`

### `<stripfile>`

Çıktı dosyası veya stdout üzerinde çalışan ve test dosyasında saklananla karşılaştırılmadan önce satır başına bir perl op. Bu oldukça gelişmiştir. Örnek: "s/^EPRT .*/EPRT stripped/"

### `<stripfile1>`

İlgili `<fileN>` içeriğini soymak için `stripfile`'a 1 ila 4 eklenebilir

### `<stripfile2>`

### `<stripfile3>`

### `<stripfile4>`

### `<upload>`

curl'ün göndermiş olması gereken yükleme verilerinin içeriği

### `<valgrind>`

disable - bu test için valgrind günlük kontrolünü devre dışı bırakır
