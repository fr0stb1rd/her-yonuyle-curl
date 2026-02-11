# HTML ve karakter setleri

curl, sunucunun gönderdiği tam ikili veriyi indirir. Örneğin, bir HTML sayfası veya tarayıcınızın daha sonra beklenen şekilde görüntülediği belirli bir karakter kodlaması kullanan başka metin verileri indirmeniz durumunda bu sizin için önemli olabilir. curl gelen verileri çevirmez.

Bunun bazı şaşırtıcı sonuçlara neden olduğu yaygın bir örnek, bir kullanıcının şunun gibi bir web sayfasını indirmesidir:

    curl https://example.com/ -o storage.html

…ve işlemden sonra `storage.html` dosyasını incelerken kullanıcı bir veya daha fazla karakterin komik veya tamamen yanlış göründüğünü fark eder. Bu, sunucunun karakterleri karakter seti X kullanarak göndermesi, düzenleyicinizin ve ortamınızın ise karakter seti Y kullanması nedeniyle olabilir. İdeal bir dünyada hepimiz her yerde UTF-8 kullanırdık ama ne yazık ki durum hala böyle değil.

Bu soruna yönelik makul bir şekilde çalışan yaygın bir geçici çözüm, bir metin dosyasını farklı karakter setlerine ve karakter setlerinden çevirmek için yaygın `iconv` yardımcı programını kullanmaktır.
