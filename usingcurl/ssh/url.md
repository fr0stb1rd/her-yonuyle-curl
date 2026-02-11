# URL'ler (URLs)

SFTP ve SCP URL'leri diğer URL'lere benzer ve bu protokolleri kullanarak dosyaları diğerleriyle aynı şekilde indirirsiniz:

    curl sftp://example.com/file.zip -u user

ve:

    curl scp://example.com/file.zip -u user

SFTP (ancak SCP değil), URL bir eğik çizgiyle (trailing slash) bittiğinde bir dosya listesi almayı destekler:

    curl sftp://example.com/ -u user

Bu protokollerin her ikisinin de "kullanıcılar" ile çalıştığını ve bir dosyayı anonim olarak veya standart bir genel adla istemediğinizi unutmayın. Çoğu sistem, aşağıda belirtildiği gibi kullanıcıların kimlik doğrulamasını gerektirir.

Bir SFTP veya SCP URL'sinden bir dosya isterken, verilen dosya yolu, özellikle kullanıcının ana dizinine göre yolu sormadığınız sürece uzak sunucudaki mutlak yol (absolute path) olarak kabul edilir. Bunu, yolun `/~/` ile başladığından emin olarak yaparsınız. Bu, FTP URL'lerinin çalışma şeklinin tam tersidir ve kullanıcılar arasında yaygın bir kafa karışıklığı nedenidir.

`daniel` kullanıcısının ana dizininden `todo.txt` dosyasını transfer etmesi için şuna benzer görünür:

    curl sftp://example.com/~/todo.txt -u daniel

veya SCP için

    curl scp://example.com/~/todo.txt -u daniel:secret
