# Canlı tutma (Keep alive)

TCP bağlantıları kullanılmadıklarında her iki yönde de tamamen trafiksiz olabilir. Bu nedenle tamamen boşta olan bir bağlantı, ağ veya sunucu sorunları nedeniyle tamamen bayatlamış bir bağlantıdan açıkça ayrılamaz.

Aynı zamanda, güvenlik duvarları veya NAT'lar gibi birçok ağ ekipmanı, adresleri çevirebilmek, "yanlış" gelen paketleri engelleyebilmek vb. için bugünlerde TCP bağlantılarını takip ediyor. Bu cihazlar genellikle tamamen boşta olan bağlantıları N dakika sonra ölü olarak sayar; burada N cihazdan cihaza değişir ancak bazen 10 dakika veya daha kısa bir süre kadar kısadır.

Gerçekten yavaş bir bağlantının (veya boşta olanın) ölü muamelesi görmesini ve yanlışlıkla sonlandırılmasını önlemeye yardımcı olmanın bir yolu, TCP canlı tutmanın (keep alive) kullanılmasını sağlamaktır. TCP keepalive, TCP protokolünde, aksi takdirde tamamen boşta olacakken ileri geri "ping çerçeveleri" göndermesini sağlayan bir özelliktir. Boşta olan bağlantıların üzerinden trafik akmadığında bile kopukluğu algılamasına yardımcı olur ve ara sistemlerin bağlantıyı ölü olarak görmemesine yardımcı olur.

curl, burada belirtilen nedenlerden dolayı varsayılan olarak TCP keepalive kullanır. keepalive'ı *devre dışı bırakmak* istediğiniz zamanlar olabilir veya TCP "pingleri" arasındaki aralığı değiştirmek isteyebilirsiniz (curl varsayılan olarak 60 saniyedir). keepalive'ı şununla kapatabilirsiniz:

    curl --no-keepalive https://example.com/

veya aralığı 5 dakikaya (300 saniye) şununla değiştirebilirsiniz:

    curl --keepalive-time 300 https://example.com/

curl 8.9.0'dan başlayarak, `--keepalive-cnt` ile curl'ün pes etmeden önce gönderdiği ancak yanıt alamadığı keepalive problarının sayısını ayarlayabilirsiniz. Şöyle:

    curl --keepalive-cnt 3 https://example.com
