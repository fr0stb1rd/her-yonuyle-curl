# Bellek hata ayıklama (Memory debugging)

`lib/memdebug.c` dosyası, birkaç işlevin hata ayıklama sürümlerini içerir. `malloc()`, `free()`, `fopen()`, `fclose()` vb. gibi, sızdırırsak bize sorun çıkarabilecek kaynaklarla bir şekilde ilgilenen işlevler. Bellek hata ayıklama sistemindeki işlevler süslü bir şey yapmaz, normal işlevlerini yaparlar ve ardından az önce ne yaptıkları hakkında bilgi kaydederler. Kaydedilen veriler daha sonra tam bir oturumdan sonra analiz edilebilir,

`memanalyze.pl`, bellek izleme sistemi tarafından oluşturulan bir günlük dosyasını analiz eden ve `tests/` içinde bulunan Perl betiğidir. Kaynakların tahsis edilip edilmediğini ancak asla serbest bırakılmadığını ve kaynak yönetimiyle ilgili diğer tür hataları algılar.

Dahili olarak, önişlemci sembolü `DEBUGBUILD`'in tanımı, yalnızca hata ayıklama etkin derlemeler için derlenen kodu kısıtlar. `CURLDEBUG` sembolü, _yalnızca_ bellek izleme/hata ayıklama için kullanılan kodu ayırt etmek için kullanılır.

Bellek hata ayıklamasını etkinleştirmek için derlerken `-DCURLDEBUG` kullanın, bu ayrıca configure'u `--enable-curldebug` ile çalıştırarak da açılır. Hata ayıklama derlemesini etkinleştirmek için derlerken `-DDEBUGBUILD` kullanın veya configure'u `--enable-debug` ile çalıştırın.

`curl --version`, hata ayıklama etkin derlemeler için `Debug` özelliğini listeler ve curl hata ayıklama bellek izleme yetenekli derlemeler için `TrackMemory` özelliğini listeler. Bu özellikler bağımsızdır ve configure betiği çalıştırılırken kontrol edilebilir. `--enable-debug` verildiğinde, bellek izlemenin kullanılmasını engelleyen bir kısıtlama olmadığı sürece her iki özellik de etkinleştirilir.

## Bellek Sızıntılarını Takip Et

... bellek hata ayıklama sistemini kullanarak. Genel olarak, ilk tercih olarak valgrind kullanmanızı öneririz.

### Tek iş parçacıklı (Single-threaded)

Lütfen bu bellek sızıntısı sisteminin birden fazla iş parçacığında çalışacak şekilde ayarlanmadığını unutmayın. Çok iş parçacıklı bir uygulamada kullanmak istiyorsanız/ihtiyacınız varsa, lütfen buna göre ayarlayın.

### Derleme (Build)

libcurl'ü `-DCURLDEBUG` ile yeniden derleyin (genellikle configure'u `--enable-debug` ile yeniden çalıştırmak bunu düzeltir). Önce `make clean`, ardından `make` yapın, böylece tüm dosyalar aslında düzgün bir şekilde yeniden oluşturulur. Ayrıca libcurl'ü hata ayıklama seçeneğiyle (genellikle derleyiciye `-g`) derlemek mantıklıdır, böylece kütüphanede aslında bir sızıntı bulursanız hata ayıklama daha kolay olur.

Bu, bellek hata ayıklamanın etkin olduğu bir kütüphane oluşturur.

### Uygulamanızı Değiştirin

Uygulama kodunuza bir satır ekleyin:

    curl_dbg_memdebug("dump");

Bu, malloc hata ayıklama sisteminin, verilen dosya adına kaynakları kullanan işlevlerin tam bir izini çıkarmasını sağlar. Programınızı yeniden oluşturduğunuzdan ve yukarıda açıklandığı gibi bu amaçla oluşturduğunuz aynı libcurl ile bağladığınızdan emin olun.

### Uygulamanızı Çalıştırın

Programınızı her zamanki gibi çalıştırın. Belirtilen bellek izleme dosyasının büyümesini izleyin.

Programınızın çıkmasını sağlayın ve uygun libcurl temizleme işlevlerini vb. kullanın. Böylece tüm sızıntı olmayanlar düzgün bir şekilde döndürülür/serbest bırakılır.

### Akışı Analiz Edin

Döküm dosyasını analiz etmek için `tests/memanalyze.pl` Perl betiğini kullanın:

    $ tests/memanalyze.pl dump

Bu şimdi tahsis edilen ancak asla serbest bırakılmayan vb. kaynaklar hakkında bir rapor verir. Bu rapor listeye göndermek için uygundur.

Bu herhangi bir çıktı üretmezse, libcurl'de hiçbir sızıntı algılanmamıştır. O zaman sızıntı büyük olasılıkla sizin kodunuzdadır.
