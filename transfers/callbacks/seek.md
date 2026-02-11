# Arama ve ioctl (Seek and ioctl)

Bu geri çağırım `CURLOPT_SEEKFUNCTION` ile ayarlanır.

Geri çağırım, giriş akışında belirli bir konuma arama yapmak (seek) için libcurl tarafından çağrılır ve devam ettirilen bir yüklemede (yüklenen tüm baytları normal okuma işlevi/geri çağırımı ile okumak yerine) bir dosyayı hızlı ileri sarmak için kullanılabilir. Ayrıca, veriler sunucuya zaten gönderildiğinde ve tekrar gönderilmesi gerektiğinde bir akışı geri sarmak için de çağrılır. Bu, çok geçişli bir kimlik doğrulama yöntemiyle bir HTTP PUT veya POST yaparken veya mevcut bir HTTP bağlantısı çok geç yeniden kullanıldığında ve sunucu bağlantıyı kapattığında olabilir. İşlev fseek(3) veya lseek(3) gibi çalışmalı ve başlangıç için argüman olarak `SEEK_SET`, `SEEK_CUR` veya `SEEK_END` almalıdır; ancak libcurl şu anda yalnızca `SEEK_SET` iletir.

Geri çağırıma gönderilen özel `userp`, `CURLOPT_SEEKDATA` ile ayarladığınız işaretçidir.

Geri çağırım işlevi başarılı olduğunda `CURL_SEEKFUNC_OK`, yükleme işleminin başarısız olmasına neden olmak için `CURL_SEEKFUNC_FAIL` veya arama başarısız olsa da libcurl'ün mümkünse sorunu aşmakta serbest olduğunu belirtmek için `CURL_SEEKFUNC_CANTSEEK` döndürmelidir. İkincisi, bazen bunun yerine girdiden okuma veya benzeri yöntemlerle yapılabilir.

Giriş argümanlarını doğrudan fseek(3) veya lseek(3)'e iletiyorsanız, ofset için veri türünün birçok sistemde `curl_off_t` için tanımlananla aynı olmadığına dikkat edin.
