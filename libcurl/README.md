# libcurl

curl komut satırı aracındaki motor libcurl'dür. libcurl aynı zamanda bugün internet veri transferlerini gerçekleştiren binlerce araç, hizmet ve uygulamadaki motordur.

## C API

libcurl, C ile yazılmış uygulamalar için bir C API'si ile sağlanan bir işlevler kütüphanesidir. Sadece birkaç hususla (bkz. [C++ programcıları için libcurl](cplusplus.md)) C++'tan da kolayca kullanabilirsiniz. Diğer diller için, libcurl kütüphanesi ile sevdiğiniz belirli dil için karşılık gelen işlevler arasında ara katmanlar olarak çalışan *bağlayıcılar* (bindings) mevcuttur.

## Transfer odaklı

libcurl'ü, kullanıcıları protokol uzmanı olmaya veya aslında ağ oluşturma veya ilgili protokoller hakkında çok fazla şey bilmeye zorlamadan genellikle transfer odaklı olacak şekilde tasarladık. Bir transferi yapabildiğiniz ve istediğiniz kadar ayrıntı ve özel bilgi ile ayarlarsınız ve ardından libcurl'e o transferi gerçekleştirmesini söylersiniz.

Bununla birlikte, ağ oluşturma ve protokoller birçok tuzak ve özel durum içeren alanlardır, bu nedenle bu şeyler hakkında ne kadar çok şey bilirseniz, libcurl'ün seçeneklerini ve çalışma yollarını o kadar iyi anlayabilirsiniz. Bahsetmeye gerek yok, işler planladığınız gibi gitmediğinde hata ayıklama yaparken ve bir sonraki adımda ne yapacağınızı anlamanız gerektiğinde bu tür bilgiler paha biçilmezdir.

En temel libcurl kullanan uygulama sadece birkaç satır kod kadar küçük olabilir, ancak çoğu uygulama elbette bundan daha fazla koda ihtiyaç duyar.

## Varsayılan olarak basit, talep üzerine daha fazlası

libcurl genellikle varsayılan olarak basit ve temel transferi yapar ve daha gelişmiş özellikler eklemek istiyorsanız, bunu doğru seçenekleri ayarlayarak eklersiniz. Örneğin, libcurl varsayılan olarak HTTP çerezlerini desteklemez, ancak ona söylediğinizde destekler.

Bu, libcurl'ün davranışlarını tahmin etmeyi ve bunlara güvenmeyi kolaylaştırır ve ayrıca eski davranışı sürdürmeyi ve yeni özellikler eklemeyi kolaylaştırır. Yalnızca yeni özellikleri gerçekten isteyen ve kullanan uygulamalar bu davranışı alır.

  * [Başlık dosyaları (Header files)](headers.md)
  * [Küresel başlatma (Global initialization)](globalinit.md)
  * [API uyumluluğu](api.md)
  * [--libcurl](--libcurl.md)
  * [çoklu iş parçacığı (multi-threading)](threading.md)
  * [CURLcode dönüş kodları](curlcode.md)
  * [Ayrıntılı operasyonlar](verbose.md)
  * [Önbellekler](caches.md)
  * [Performans](performance.md)
  * [C++ programcıları için](cplusplus.md)
