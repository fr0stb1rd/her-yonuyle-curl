# Handle'lar arasında veri paylaşımı

Bazen uygulamaların transferler arasında veri paylaşması gerekir. Aynı multi handle'a eklenen tüm easy handle'lar, o aynı multi handle'daki handle'lar arasında otomatik olarak birçok paylaşım yapar, ancak bazen istediğiniz tam olarak bu olmayabilir.

## Multi handle

Aynı multi handle'a eklenen tüm easy handle'lar [bağlantı önbelleğini (connection cache)](../transfers/conn/reuse.md) ve [dns önbelleğini (dns cache)](../transfers/conn/names.md) otomatik olarak paylaşır.

## Easy handle'lar arasında paylaşım

libcurl, uygulamanın herhangi bir sayıda easy handle tarafından paylaşılabilecek verileri tutan bir "paylaşım nesnesi" (share object) oluşturduğu genel bir "paylaşım arayüzüne" (sharing interface) sahiptir. Veriler daha sonra onu paylaşan handle'ların içinde tutulmak yerine paylaşılan nesneden saklanır ve okunur.

    CURLSH *share = curl_share_init();

Paylaşılan nesne, çerezlerin, bağlantı önbelleğinin, dns önbelleğinin ve SSL oturum kimliği önbelleğinin tümünü veya herhangi birini paylaşacak şekilde ayarlanabilir.

Örneğin, paylaşımı çerezleri ve dns önbelleğini tutacak şekilde ayarlamak:

    curl_share_setopt(share, CURLSHOPT_SHARE, CURL_LOCK_DATA_COOKIE);
    curl_share_setopt(share, CURLSHOPT_SHARE, CURL_LOCK_DATA_DNS);

Daha sonra ilgili transferi bu paylaşım nesnesini kullanacak şekilde ayarlarsınız:

    curl_easy_setopt(curl, CURLOPT_SHARE, share);

Bu `curl` handle'ı ile yapılan transferler, çerez ve dns bilgilerini `share` handle'ında kullanır ve saklar. Birkaç easy handle'ı aynı paylaşım nesnesini paylaşacak şekilde ayarlayabilirsiniz.

## Ne paylaşılmalı

`CURL_LOCK_DATA_COOKIE` - çerez kavanozunu paylaşmak için bu biti ayarlayın. Çerezleri kullanmaya başlamak için her easy handle'ın yine de çerez "motorunu" düzgün bir şekilde başlatması gerektiğini unutmayın. Bu seçeneğin birden çok eşzamanlı iş parçacığıyla kullanılması desteklenmez.

`CURL_LOCK_DATA_DNS` - DNS önbelleği, libcurl'ün sonraki aramaları daha hızlı hale getirmek için çözümlenmiş ana bilgisayar adları için adresleri bir süreliğine sakladığı yerdir.

`CURL_LOCK_DATA_SSL_SESSION` - SSL oturum kimliği önbelleği, libcurl'ün bir önceki bağlantıyı daha hızlı sürdürebilmek için SSL bağlantıları için sürdürme bilgilerini sakladığı yerdir.

`CURL_LOCK_DATA_CONNECT` - ayarlandığında, bu handle paylaşılan bir bağlantı önbelleği kullanır ve bu nedenle yeniden kullanılacak mevcut bağlantıları bulma olasılığı daha yüksektir vb., bu da aynı ana bilgisayara seri bir şekilde birden çok transfer yaparken daha hızlı performansla sonuçlanabilir. Bu seçeneğin birden çok eşzamanlı iş parçacığıyla kullanılması desteklenmez.

`CURL_LOCK_DATA_PSL` - bu bit, handle'lar arasında Genel Sonek Listesini (Public Suffix List) paylaşır. Üst düzey İnternet alan adları olarak da bilinen genel soneklerin listesi, çerezlerin güvenliğini yönetmeye yardımcı olmak için kullanılır. Listeyi paylaşmak, listenin birden çok kopyasını işlemek zorunda kalmanın getirdiği ek yükü önler.

`CURL_LOCK_DATA_HSTS` - bu bit, bellek içi HSTS (HTTP Strict Transport Security) önbelleğini paylaşır. HSTS, web siteleri tarafından HTTP isteklerine bunun yerine HTTPS kullanılarak güvenli bir şekilde erişilmesi gerektiğini belirtmek için kullanılır. Bu seçeneğin birden çok eşzamanlı iş parçacığıyla kullanılması desteklenmez.

## Kilitleme (Locking)

Paylaşım nesnesinin çok iş parçacıklı bir ortamda transferler tarafından paylaşılmasını istiyorsanız. Belki de birçok çekirdeğe sahip bir CPU'nuz var ve her çekirdeğin kendi iş parçacığını çalıştırmasını ve veri aktarmasını istiyorsunuz, ancak yine de farklı transferlerin veri paylaşmasını istiyorsunuz. O zaman mutex (karşılıklı dışlama) geri çağırımlarını ayarlamanız gerekir.

İş parçacığı kullanmıyorsanız ve paylaşılan nesneye seri bir şekilde birer birer eriştiğinizi *biliyorsanız*, herhangi bir kilit ayarlamanıza gerek yoktur. Paylaşım nesnesine aynı anda erişen birden fazla transfer varsa, veri bozulmasını ve hatta muhtemelen çökmeleri önlemek için mutex geri çağırımlarının kurulması gerekir.

libcurl'ün kendisi şeyleri nasıl kilitleyeceğini veya hatta hangi iş parçacığı modelini kullandığınızı bilmediğinden, aynı anda yalnızca bir erişime izin veren mutex kilitleri yaptığınızdan emin olmalısınız. pthreads kullanan bir uygulama için bir kilit geri çağırımı şuna benzer olabilir:

    static void lock_cb(CURL *handle, curl_lock_data data,
                        curl_lock_access access, void *userptr)
    {
      pthread_mutex_lock(&lock[data]); /* küresel bir kilit dizisi kullanır */
    }
    curl_share_setopt(share, CURLSHOPT_LOCKFUNC, lock_cb);

Karşılık gelen kilit açma geri çağırımı ile şuna benzer olabilir:

    static void unlock_cb(CURL *handle, curl_lock_data data,
                          void *userptr)
    {
      pthread_mutex_unlock(&lock[data]); /* küresel bir kilit dizisi
                                            kullanır */
    }
    curl_share_setopt(share, CURLSHOPT_UNLOCKFUNC, unlock_cb);

## Paylaşımı kaldırma (Unshare)

Bir transfer, transferi sırasında paylaşım nesnesini kullanır ve o nesnenin paylaşmak üzere belirtildiği şeyi aynı nesneyi paylaşan diğer handle'larla paylaşır.

Sonraki bir transferde, bir transferin paylaşmaya devam etmesini önlemek için `CURLOPT_SHARE`, NULL olarak ayarlanabilir. Bu durumda, handle bir sonraki transferi daha önce paylaşılan veriler için boş önbelleklerle başlatabilir.

İki transfer arasında, bir paylaşım nesresi, o nesneyi paylaşan handle'ların bir sonraki sefer farklı bir veri setini paylaşması için farklı bir özellik setini paylaşacak şekilde güncellenebilir. DNS verilerini paylaşmayı kaldırırken curl_share_setopt()'un `CURLSHOPT_UNSHARE` seçeneğiyle paylaşılan bir nesneden paylaşılacak bir öğeyi şöyle kaldırırsınız:

    curl_share_setopt(share, CURLSHOPT_UNSHARE, CURL_LOCK_DATA_DNS);
