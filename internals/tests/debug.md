# Hata ayıklama derlemeleri (Debug builds)

*Hata ayıklama derlemelerinden* bahsettiğimizde, genellikle hata ayıklama kodunun ve sembollerin hala mevcut olduğu curl derlemelerine atıfta bulunuruz. curl geliştirmeyle çalışmak istiyorsanız, test etmeyi ve hata ayıklamayı kolaylaştırdığı için bunu yapmanızı şiddetle tavsiye ederiz.

Configure kullanarak bir hata ayıklama derlemesini şu şekilde yaparsınız:

    ./configure --enable-debug

Hata ayıklama derlemeleri, runtests.pl ile gdb ile bireysel test durumlarını çalıştırmayı mümkün kılar, bu da kullanışlıdır - özellikle örneğin bir yerde çökmesini sağlayabilirseniz, o zaman gdb onu yakalayabilir ve tam olarak nerede olduğunu vb. gösterebilir.

Hata ayıklama derlemeleri ayrıca normal *sürüm derlemelerinden* biraz farklıdır çünkü curl'ü test etmeyi kolaylaştıran bazı kod parçacıkları içerirler. Örneğin test paketinin rastgele sayı üretecini geçersiz kılmasına izin verir, böylece aksi takdirde rastgele olan değerler için test yapmak gerçekten çalışır. Ayrıca, birim testleri yalnızca hata ayıklama derlemelerinde çalışır.

## Memdebug

Hata ayıklama derlemeleri ayrıca *memdebug* dahili bellek izleme ve hata ayıklama sistemini de etkinleştirir.

Açıldığında, memdebug sistemi bellekle ilgili birçok seçenek hakkında ayrıntılı bilgiyi bir günlük dosyasına çıkarır, böylece olaydan sonra analiz edilebilir ve doğrulanabilir. Tüm belleğin serbest bırakıldığı, tüm dosyaların kapatıldığı vb. doğrulandı.

Bu, valgrind'in fakir adam versiyonudur ancak özellikleriyle hiç kıyaslanamaz. Ancak oldukça taşınabilir ve düşük etkilidir.

Bir hata ayıklama derlemesinde, `CURL_MEMDEBUG` ortam değişkeni günlük için kullanılan bir dosya adına ayarlanmışsa memdebug sistemi curl tarafından etkinleştirilir. Test paketi bu değişkeni bizim için ayarlar (bkz. `tests/log/memdump`) ve varsa her test çalışmasından sonra doğrular.
