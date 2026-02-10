# İlerleme bilgisi (Progress information)

İlerleme geri çağırımı, transferin tüm ömrü boyunca her transfer için düzenli ve tekrar tekrar çağrılan şeydir. Eski geri çağırım `CURLOPT_PROGRESSFUNCTION` ile ayarlanıyordu ancak modern ve tercih edilen geri çağırım `CURLOPT_XFERINFOFUNCTION` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_XFERINFOFUNCTION, xfer_callback);

`xfer_callback` işlevi şu prototiple eşleşmelidir:

    int xfer_callback(void *clientp, curl_off_t dltotal, curl_off_t dlnow,
                      curl_off_t ultotal, curl_off_t ulnow);

Bu seçenek ayarlanırsa ve `CURLOPT_NOPROGRESS` 0'a (sıfır) ayarlanırsa, bu geri çağırım işlevi libcurl tarafından sık bir aralıkla çağrılır. Veriler aktarılırken sık sık çağrılır ve hiçbir şeyin aktarılmadığı yavaş dönemlerde saniyede yaklaşık bir çağrıya kadar yavaşlayabilir.

**clientp** işaretçisi, `CURLOPT_XFERINFODATA` ile ayarlanan özel verilere işaret eder:

    curl_easy_setopt(handle, CURLOPT_XFERINFODATA, custom_pointer);

Geri çağırıma libcurl'ün ne kadar veri aktarmak üzere olduğu ve bayt cinsinden ne kadar aktardığı söylenir:

 - `dltotal`, libcurl'ün bu transferde indirmeyi beklediği toplam bayt sayısıdır.
 - `dlnow`, şimdiye kadar indirilen bayt sayısıdır.
 - `ultotal`, libcurl'ün bu transferde yüklemeyi beklediği toplam bayt sayısıdır.
 - `ulnow`, şimdiye kadar yüklenen bayt sayısıdır.

Geri çağırıma iletilen bilinmeyen/kullanılmayan argüman değerleri sıfıra ayarlanır (örneğin sadece veri indiriyorsanız, yükleme boyutu sıfır kalır). Çoğu zaman geri çağırım, veri boyutlarını bilmeden önce bir veya daha fazla kez çağrılır, bu nedenle bir program bunu ele alacak şekilde yapılmalıdır.

Bu geri çağırımdan sıfır olmayan bir değer döndürmek, libcurl'ün transferi iptal etmesine ve `CURLE_ABORTED_BY_CALLBACK` döndürmesine neden olur.

Multi arayüz ile veri aktarırsanız, transferleri gerçekleştiren uygun libcurl işlevini çağırmadığınız sürece bu işlev boşta kalma sürelerinde çağrılmaz.

(Kullanımdan kaldırılan geri çağırım `CURLOPT_PROGRESSFUNCTION` aynı şekilde çalışıyordu ancak `curl_off_t` türünde argümanlar almak yerine `double` kullanıyordu.)
