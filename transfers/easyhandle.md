# Easy handle

libcurl ile öğrenmeniz gereken temeller:

Önce bir "easy handle" oluşturursunuz, bu gerçekten bir transfere olan tutamacınızdır:

    CURL *easy_handle = curl_easy_init();

Daha sonra yaklaşan transferi kontrol etmek için o handle'da seçenekleri ayarlarsınız.
Bu örnek URL'yi ayarlar:

    /* üzerinde çalışılacak URL'yi ayarla */
    res = curl_easy_setopt(easy_handle, CURLOPT_URL, "http://example.com/");

`curl_easy_setopt()` `CURLE_OK` döndürürse, seçeneği sorunsuz bir şekilde sakladığını biliriz.

Easy handle oluşturmak ve üzerinde seçenekler ayarlamak, herhangi bir transferin gerçekleşmesini sağlamaz ve genellikle libcurl'ün isteğinizi daha sonra transfer gerçekleştiğinde kullanılmak üzere saklamasından başka pek bir şey yapmaz. Sözdizimi kontrolü ve girdinin doğrulanmasının çoğu da ertelenebilir, bu nedenle `curl_easy_setopt` şikayet etmedi diye, girdinin doğru ve geçerli olduğu anlamına gelmez; daha sonra bir hata döndürülebilir.

Daha fazlasını [easy seçenekleri](options/) hakkındaki ayrı bölümünde okuyun.

Easy handle'ınız için seçenekleri ayarlamayı bitirdiğinizde, gerçek transferi başlatabilirsiniz.

Transferin gerçek performansı, uygulamanızda ne tür bir davranış istediğinize ve libcurl'ün mimarinize en iyi nasıl entegre edildiğine bağlı olarak farklı yöntemler ve işlev çağrıları kullanılarak yapılabilir. Bunlar daha sonra bu bölümde daha ayrıntılı olarak açıklanmaktadır.

Transfer devam ederken libcurl, veri iletmek, veri okumak ve çeşitli şeyler yapmak için *[geri çağırımlar (callbacks)](callbacks/)* olarak bilinen belirtilen işlevlerinizi çağırır.

Transfer tamamlandıktan sonra, başarılı olup olmadığını anlayabilir ve transfer sırasında libcurl'ün topladığı istatistikleri ve diğer bilgileri easy handle'dan çıkarabilirsiniz. [Transfer sonrası bilgi](getinfo.md) bölümüne bakın.

## Yeniden kullanım (Reuse)

Easy handle'lar yeniden kullanılmak üzere tasarlanmıştır. Easy handle ile tek bir transfer yaptığınızda, bir sonraki transferiniz için hemen tekrar kullanabilirsiniz. Bundan elde edilecek çok fazla kazanç vardır.

Tüm seçenekler "yapışkandır". Aynı handle ile ikinci bir transfer yaparsanız, aynı seçenekler kullanılır. Siz onları tekrar değiştirene veya handle üzerinde `curl_easy_reset()` çağırana kadar handle'da ayarlı kalırlar.

## Sıfırlama (Reset)

`curl_easy_reset()` çağrılarak, verilen easy handle için tüm seçenekler sıfırlanır ve varsayılan değerlerine geri döndürülür. Handle ilk oluşturulduğunda seçeneklerin sahip olduğu değerlerle aynıdır. Önbellekler bozulmadan kalır.

## Çoğaltma (Duplicate)

Bir easy handle, şu anda ayarlanmış tüm seçenekleriyle birlikte, `curl_easy_duphandle()` kullanılarak çoğaltılabilir. Kendisine iletilen handle'ın bir kopyasını döndürür.

Önbellekler ve diğer durum bilgileri taşınmaz.
