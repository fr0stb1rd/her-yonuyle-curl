# Bilinen ana bilgisayarlar (Known hosts)

Güvenli bir ağ istemcisinin, uzak ana bilgisayarın tam olarak iletişim kurduğunu düşündüğü ana bilgisayar olduğundan emin olması gerekir. TLS tabanlı protokollerle bu, istemcinin sunucunun sertifikasını doğrulamasıyla yapılır.

SSH protokolleriyle sunucu sertifikaları yoktur, bunun yerine her sunucu kendi benzersiz anahtarını sağlayabilir. TLS'nin aksine, SSH'nin sertifika yetkilileri veya benzeri bir şeyi yoktur, bu nedenle istemcinin ana bilgisayarın anahtarının (diğer yollarla) neye benzemesi gerektiğini bildiği şeyle eşleştiğinden emin olması gerekir.

Anahtarların eşleştirilmesi tipik olarak anahtarın karmaları (hash) kullanılarak yapılır ve istemcinin bilinen sunucular için karmaları sakladığı dosya genellikle `known_hosts` olarak adlandırılır ve özel bir SSH dizinine konur. Linux sistemlerinde bu genellikle `~/.ssh` olarak adlandırılır.

curl bir SFTP ve SCP ana bilgisayarına bağlandığında, ana bilgisayarın anahtar karmasının zaten bilinen ana bilgisayarlar (known hosts) dosyasında mevcut olduğundan emin olur veya sunucunun doğru sunucu olduğuna güvenemediği için devam eden işlemi reddeder. `known_hosts` içinde doğru karma mevcut olduğunda curl transferleri gerçekleştirebilir.

curl'ü `known_hosts` dosyasını kontrol etmeye ve ona uymaya zorlamayı atlamak için `-k / --insecure` komut satırı seçeneğini kullanabilirsiniz. Ortadaki adam (man-in-the-middle) saldırılarının tespit edilmemesini mümkün kıldığı için bu seçeneği son derece dikkatli kullanmalısınız.
