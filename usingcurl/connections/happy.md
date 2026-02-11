# Mutlu Gözler (Happy Eyeballs)

curl belirli bir ana bilgisayara bağlanmak üzere olduğunda, denenecek adreslerin bir listesine sahiptir. Adres listesi iki listeye ayrılır: IPv4 adreslerini içeren bir liste ve IPv6 adreslerini içeren bir liste.

curl, IPv6 listesindeki ilk adrese bir bağlantı girişimi başlatarak başlar. Bağlantı girişimi başarısız olursa, bir tanesi çalışana kadar hepsini tek tek yineleyerek listedeki bir sonraki adrese geçer.

İki yüz milisaniye sonra curl hala IPv6'ya bağlanmaya çalışıyorsa, paralel olarak IPv4 üzerinden ikinci bir girişim serisi başlatır. Aynı tarzda, bağlantı hatalarında IPv4 adresleri listesi üzerinde yineler. İsterseniz bir bağlantı yarışı.

Çalışan ilk bağlantı kazanır ve diğer tüm girişimler atılır.

## HTTP/3 yarışı

HTTP/3'ü denemesi istendiğinde (`--http3` ile), curl bağlantı yarışı oyununu bir seviye yukarı taşır.

curl önce yukarıda açıklandığı gibi QUIC için Mutlu Gözler bağlantı girişimini başlatır. Önce IPv6 QUIC'i ve bir zaman aşımından sonra IPv4 QUIC'i dener. İlk iki yüz milisaniye içinde başarılı bir QUIC bağlantısı yoksa (veya zaman aşımı penceresinin yarısı içinde hiç UDP paketi alınmadıysa, varsayılan olarak yüz milisaniye), curl TCP için *ikinci* bir Mutlu Gözler senaryosu başlatır - önce IPv6 TCP ve zaman aşımından sonra IPv4 TCP.

Çalışan en fazla dört paralel girişimden başarılı olan ilk bağlantı girişimi kazanır. "Kaybedenler" daha sonra basitçe atılır.

## İnce ayar (Tweak)

İki yüz milisaniye bağlantılarınızı istediğinizden daha uzun süre geciktirebilir. Örneğin, IPv6 üzerinden TCP paketleri belirli bir ağ yolunda veya sunucuda hiç yanıt almadığında.

Veya tam tersi, yüksek gecikmeli bir sunucuyla iletişim kurmanız gerekebilir, bu durumda varsayılan zaman aşımı çok erken devreye girebilir.

Bunun gibi anlar ve senaryolar için curl, `--happy-eyeballs-timeout-ms` komut satırı seçeneğini sunar. Varsayılan iki yüz milisaniyeyi belirttiğiniz herhangi bir şeye değiştirir. Sıfıra ayarlamak curl'ün bağlantı girişimlerini tam olarak aynı anda başlatmasını sağlar.
