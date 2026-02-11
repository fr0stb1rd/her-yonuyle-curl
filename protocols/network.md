# Basitleştirilmiş ağ oluşturma

Ağ oluşturma, İnternet üzerindeki iki uç nokta (endpoint) arasında iletişim kurmak anlamına gelir. İnternet, her biri kendi bireysel adreslerini ([IP adresleri](https://en.wikipedia.org/wiki/IP_address) olarak adlandırılır) kullanan birbirine bağlı bir grup makinedir (gerçekte bilgisayarlar). Her makinenin sahip olduğu adresler farklı türlerde olabilir ve makinelerin geçici adresleri bile olabilir. Bu bilgisayarlara ana bilgisayarlar (host) da denir.

## İstemci ve sunucu (Client and Server)

Önünde oturduğunuz bilgisayar, tablet veya telefon genellikle *istemci* (client) olarak adlandırılır ve verileri takas etmek istediğiniz dışarıdaki makineye ise *sunucu* (server) denir. İstemci ve sunucu arasındaki temel fark, oynadıkları rollerdir. Rollerin sonraki bir işlemde tersine çevrilmesini engelleyen hiçbir şey yoktur.

Sunucu istemciyle iletişim kuramayacağı, ancak istemci sunucuyla iletişim kurabileceği için bir transfer girişimi her zaman istemci tarafından yapılır.

## Hangi makine

Biz bir istemci olarak dışarıdaki makinelerden birinden veya birine (bir sunucu) bir transfer başlatmak istediğimizde, genellikle IP adreslerini bilmeyiz, bunun yerine genellikle ismini biliriz. İletişim kurulacak makinenin adı genellikle curl veya bir tarayıcı gibi araçları kullandığımızda çalıştığımız URL'e gömülüdür.

`http://example.com/index.html` gibi bir URL kullanabiliriz, bu da istemcinin example.com adlı ana bilgisayara (host) bağlanıp onunla iletişim kurduğu anlamına gelir.

## Ana bilgisayar adı çözümleme (Hostname resolving)

İstemci ana bilgisayar adını bildiğinde, onunla iletişim kurabilmek için o ada sahip ana bilgisayarın hangi IP adreslerine sahip olduğunu bulması gerekir.

Adı bir IP adresine dönüştürmeye 'isim çözümleme' (name resolving) denir. Ad, bir veya bir dizi adrese *çözümlenir*. Bu genellikle bir *DNS sunucusu* tarafından yapılır; DNS, adları adreslere dönüştürebilen büyük bir arama tablosu gibidir—gerçekten de İnternet'teki tüm adlar. Bilgisayar normalde ağ kurulumunun bir parçası olduğu için DNS sunucusunu çalıştıran bilgisayarın adresini zaten bilir.

Bu nedenle ağ istemcisi DNS sunucusuna sorar: *Merhaba, lütfen bana `example.com` için tüm adresleri ver*. DNS sunucusu bir adres listesiyle yanıt verir. Veya yazım hataları durumunda, adın mevcut olmadığı yanıtını verebilir.

## Bir bağlantı kurun

İletişim kurmak istediği ana bilgisayar için bir veya daha fazla IP adresiyle istemci, bir *bağlantı isteği* (connect request) gönderir. Oluşturmak istediği bağlantıya TCP ([İletim Kontrol Protokolü](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)) veya [QUIC](https://en.wikipedia.org/wiki/QUIC) bağlantısı denir; bu, iki bilgisayar arasında görünmez bir ip bağlamak gibidir. Kurulduktan sonra ip, her iki yönde de bir veri akışı göndermek için kullanılabilir.

İstemci, ana bilgisayar için birden fazla adres aldıysa, bağlanırken bu adres listesini dolaşır ve bir adres başarısız olursa bir sonrakine bağlanmayı dener; bu işlem bir adres çalışana veya hepsi başarısız olana kadar tekrarlanır.

## Port numaralarına bağlanın

Uzak bir sunucuya TCP veya QUIC ile bağlanırken, bir istemci bunu hangi port numarasında yapacağını seçer. Bir port numarası, belirli bir hizmet için ayrılmış bir yerdir ve bu da aynı sunucunun aynı anda diğer port numaralarındaki diğer hizmetleri dinlemesine (listen) olanak tanır.

En yaygın protokollerin istemcilerin ve sunucuların kullandığı varsayılan port numaraları vardır. Örneğin, `http://example.com/index.html` URL'i kullanıldığında, bu URL, istemciye varsayılan olarak sunucudaki 80 numaralı TCP portunu denemesi gerektiğini söyleyen `HTTP` adlı bir *şema* (scheme) belirtir. URL bunun yerine `HTTPS` kullanıyorsa, varsayılan port numarası 443'tür.

URL, özel bir port numarası içerebilir. Bir port numarası belirtilmemişse, istemci URL'de kullanılan şema için varsayılan portu kullanır.

## Güvenlik

Bir TCP bağlantısı kurulduktan sonra, birçok transfer, devam etmeden önce her iki tarafın da daha iyi bir güvenlik düzeyi üzerinde anlaşmasını gerektirir (örneğin `HTTPS` kullanılıyorsa); bu, TLS ([Taşıma Katmanı Güvenliği](https://tr.wikipedia.org/wiki/Ta%C5%9F%C4%B1ma_Katman%C4%B1_G%C3%BCvenli%C4%9Fi)) ile yapılır. Eğer öyleyse, istemci ve sunucu önce bir TLS el sıkışması (handshake) yapar ve ancak o başarılı olursa daha ileriye devam eder.

Bağlantı QUIC kullanılarak yapılıyorsa, TLS el sıkışması bağlanma aşamasında otomatik olarak yapılır.

## Veri transferi

Bağlanan metaforik *ip* uzak bilgisayara takıldığında, iki makine arasında bir *bağlantı* (connection) kurulmuş olur. Bu bağlantı daha sonra veri alışverişi yapmak için kullanılabilir. Bu alışveriş, bir sonraki bölümde tartışıldığı gibi bir *protokol* kullanılarak yapılır.

Geleneksel olarak, *indirme* (download), verilerin bir sunucudan bir istemciye aktarılmasıdır; tersine, *yükleme* (upload), verilerin istemciden sunucuya gönderilmesidir. İstemci *aşağıdadır*; sunucu *yukarıdadır*.

## Bağlantıyı Kes (Disconnect)

Tek bir transfer tamamlandığında, bağlantı amacına hizmet etmiş olabilir. O zaman ya daha sonraki transferler için yeniden kullanılabilir ya da bağlantısı kesilip kapatılabilir.
