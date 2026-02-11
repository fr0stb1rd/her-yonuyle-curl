# multi\_socket ile yürütme

multi_socket, normal multi arayüzünün ekstra baharatlı sürümüdür ve olay güdümlü (event-driven) uygulamalar için tasarlanmıştır. Önce [Multi arayüz ile yürütme](multi.md) bölümünü okuduğunuzdan emin olun.

multi_socket, hepsi aynı tek iş parçacığında yapılan çoklu paralel transferleri destekler ve tek bir uygulamada on binlerce transferi çalıştırmak için kullanılmıştır. Çok sayıda (>100 veya civarı) paralel transfer yapıyorsanız genellikle en mantıklı olan API'dir.

Bu durumda olay güdümlü, uygulamanızın bir dizi sokete abone olan bir sistem seviyesi kütüphanesi veya kurulumu kullandığı ve bu soketlerden biri okunabilir veya yazılabilir olduğunda uygulamanıza bildirdiği ve tam olarak hangisi olduğunu söylediği anlamına gelir.

Bu kurulum, istemcilerin eşzamanlı transfer sayısını diğer sistemlere göre çok daha yükseğe çıkarmasına ve yine de iyi performansı korumasına olanak tanır. Normal API'ler aksi takdirde tüm soketlerin listelerini taramak için çok fazla zaman harcar.

## Birini seç

Dışarıda seçebileceğiniz çok sayıda olay tabanlı sistem vardır ve libcurl hangisini kullandığınız konusunda tamamen agnostiktir. libevent, libev ve libuv popüler üç tanesidir ancak epoll, kqueue, /dev/poll, pollset veya Event Completion gibi işletim sisteminizin yerel çözümlerine de doğrudan gidebilirsiniz.

## Çok sayıda easy handle

Tıpkı normal multi arayüzde olduğu gibi, `curl_multi_add_handle()` ile bir multi handle'a easy handle'lar eklersiniz. Gerçekleştirmek istediğiniz her transfer için bir easy handle.

Bunları transferler çalışırken herhangi bir zamanda ekleyebilir ve benzer şekilde `curl_multi_remove_handle` çağrısını kullanarak easy handle'ları istediğiniz zaman kaldırabilirsiniz. Ancak genellikle, bir handle'ı yalnızca transferi tamamlandıktan sonra kaldırırsınız.

## multi_socket geri çağırımları (callbacks)

Yukarıda açıklandığı gibi, bu olay tabanlı mekanizma, libcurl tarafından hangi soketlerin kullanıldığını ve libcurl'ün bu soketlerde hangi etkinlikleri beklediğini bilmek için uygulamaya dayanır: soketin okunabilir, yazılabilir veya her ikisi olmasını bekliyorsa.

Uygulamanın ayrıca zaman aşımı süresi dolduğunda libcurl'e söylemesi gerekir, çünkü her şeyi yürütme kontrolü ondadır, libcurl bunu kendisi yapamaz. libcurl, uygulamaya güncellenmiş zaman aşımı değerlerini ihtiyaç duyduğu anda bildirir.

### socket_callback

libcurl, beklenecek soket etkinliği hakkında uygulamayı [CURLMOPT_SOCKETFUNCTION](https://curl.se/libcurl/c/CURLMOPT_SOCKETFUNCTION.html) adlı bir geri çağırımla bilgilendirir. Uygulamanızın böyle bir işlevi uygulaması gerekir:

    int socket_callback(CURL *easy,      /* easy handle */
                        curl_socket_t s, /* soket */
                        int what,        /* ne beklenecek */
                        void *userp,     /* özel geri çağırım işaretçisi */
                        void *socketp)   /* özel soket işaretçisi */
    {
       /* 's' soketi hakkında bilgi verildi */
    }

    /* geri çağırımı multi handle'da ayarla */
    curl_multi_setopt(multi_handle, CURLMOPT_SOCKETFUNCTION, socket_callback);

Bunu kullanarak libcurl, uygulamanızın izlemesi gereken soketleri ayarlar ve kaldırır. Uygulamanız, altta yatan olay tabanlı sisteme soketleri beklemesini söyler. Beklenecek birden fazla soket varsa bu geri çağırım birden fazla kez çağrılır ve durum değiştiğinde tekrar çağrılır; belki de yazılabilir bir soketi beklemekten, okunabilir olmasını beklemeye geçmelisinizdir.

Uygulamanın libcurl adına izlediği soketlerden biri, istendiği gibi okunabilir veya yazılabilir hale geldiğini kaydettiğinde, `curl_multi_socket_action()`'ı çağırarak ve etkilenen soketi ve hangi soket etkinliğinin kaydedildiğini belirten ilişkili bir bit maskesini ileterek libcurl'e bunu bildirirsiniz:

    int running_handles;
    ret = curl_multi_socket_action(multi_handle,
                                   sockfd, /* etkinliğe sahip soket */
                                   ev_bitmask, /* belirli etkinlik */
                                   &running_handles);

### timer_callback

Uygulama kontroldedir ve soket etkinliğini bekler. Soket etkinliği olmasa bile libcurl'ün yapması gereken şeyler vardır. Zaman aşımı şeyleri, ilerleme geri çağırımını çağırma, bir yeniden denemeyi baştan başlatma veya çok uzun süren bir transferi başarısız kılma vb. Bunun çalışması için, uygulamanın libcurl'ün ayarladığı tek seferlik (single-shot) bir zaman aşımını da ele aldığından emin olması gerekir.

libcurl zaman aşımını timer_callback [CURLMOPT_TIMERFUNCTION](https://curl.se/libcurl/c/CURLMOPT_TIMERFUNCTION.html) ile ayarlar:

    int timer_callback(multi_handle,   /* multi handle */
                       timeout_ms,     /* beklenecek milisaniye */
                       userp)          /* özel geri çağırım işaretçisi */
    {
      /* beklenecek yeni zaman aşımı değeri 'timeout_ms' içindedir */
    }

    /* geri çağırımı multi handle'da ayarla */
    curl_multi_setopt(multi_handle, CURLMOPT_TIMERFUNCTION, timer_callback);

Kaç tane bireysel easy handle eklenmiş olduğuna veya kaç transferin devam ettiğine bakılmaksızın, uygulamanın tüm multi handle için ele alması gereken yalnızca bir zaman aşımı vardır. Zamanlayıcı geri çağırımı, beklenecek mevcut en yakın zaman periyoduyla güncellenir. libcurl, soket etkinliği nedeniyle zaman aşımı süresi dolmadan önce çağrılırsa, süresi dolmadan önce zaman aşımı değerini tekrar güncelleyebilir.

Seçtiğiniz olay sistemi sonunda size zamanlayıcının süresinin dolduğunu söylediğinde, bunu libcurl'e bildirmeniz gerekir:

    curl_multi_socket_action(multi, CURL_SOCKET_TIMEOUT, 0, &running);

…birçok durumda, bu libcurl'ün timer_callback'i tekrar çağırmasını ve bir sonraki sona erme dönemi için yeni bir zaman aşımı ayarlamasını sağlar.

### Her şey nasıl başlatılır

Multi handle'a bir veya daha fazla easy handle eklediğinizde ve multi handle'da soket ve zamanlayıcı geri çağırımlarını ayarladığınızda, transferi başlatmaya hazırsınız demektir.

Her şeyi başlatmak için, libcurl'e zaman aşımına uğradığını söylersiniz (çünkü tüm easy handle'lar kısa bir zaman aşımıyla başlar), bu da libcurl'ün işleri ayarlamak için geri çağırımları çağırmasını sağlar ve o andan itibaren olay sisteminizin sürmesine izin verebilirsiniz:

    /* tüm easy handle'lar ve geri çağırımlar ayarlandı */

    curl_multi_socket_action(multi, CURL_SOCKET_TIMEOUT, 0, &running);

    /* şimdi geri çağırımlar çağrılmış olmalı ve beklememiz gereken
       soketlerimiz ve muhtemelen bir zaman aşımımız da var.
       Olay sisteminin sihrini yapmasını sağlayın */

    event_base_dispatch(event_base); /* libevent2 bu API'ye sahiptir */

    /* bu noktada olay döngüsünden çıktık */

### Ne zaman biter?

`curl_multi_socket_action` tarafından döndürülen 'running_handles' (çalışan handle'lar) sayacı, henüz tamamlanmamış mevcut transfer sayısını tutar. Bu sayı sıfıra ulaştığında, devam eden transfer olmadığını biliriz.

'running_handles' sayacı her değiştiğinde, `curl_multi_info_read()` tamamlanan belirli transferler hakkında bilgi döndürür.
