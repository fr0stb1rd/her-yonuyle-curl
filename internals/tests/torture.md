# İşkence (Torture)

curl [hata ayıklama etkin](debug.md) olarak oluşturulduğunda, özel bir test türü sunar. **İşkence** testleri dediğimiz testler. Endişelenmeyin, kulağa geldiği kadar korkunç değildir.

libcurl ve curl çıkış yollarının herhangi bir çökme veya bellek sızıntısı olmadan çalıştığını doğrularlar,

İşkence testleri şu şekilde çalışır:

 - tek testi önce olduğu gibi çalıştır
 - çağrılan *hata verebilir* (fallible) işlevlerin sayısını say
 - testi her hata verebilir işlev çağrısı için bir kez yeniden çalıştır
 - her hata verebilir işlev çağrısını birer birer hata döndürmeye zorla
 - sızıntı veya çökme olmadığını doğrula
 - tüm hata verebilir işlevler başarısız olmaya zorlanana kadar devam et

Bu test yöntemi ciddi anlamda uzun zaman alabilir. Bunu denerken [valgrind](valgrind.md)'i kapatmanızı tavsiye ederim.

## Belirli bir hatayı yeniden çalıştır

Tek bir test başarısız olursa, `runtests.pl` sorunu tetikleyen "turu" tam olarak tanımlar ve gösterildiği gibi `-t` kullanarak, çağrıldığında *yalnızca* o belirli hata verebilir işlevi başarısız kılan bir komut satırını çalıştırabilirsiniz.

## Sığ (Shallow)

Bu test yöntemini biraz daha pratik hale getirmek için test paketi ayrıca bir `--shallow` seçeneği sunar. Bu, kullanıcının test senaryosu başına başarısız olacak maksimum hata verebilir işlev sayısını ayarlamasına olanak tanır. Bu değerle ayarlanandan daha fazla başarısız olacak çağrı varsa, betik hangilerinin başarısız olacağını rastgele seçer.

Özel bir özellik olarak, testlerde bir şeyleri rastgele hale getirmek rahatsız edici olabileceğinden, betik yıl + aya dayalı rastgele bir tohum (seed) kullanır, böylece her takvim ayı için aynı kalır. Kullanışlıdır, çünkü aynı testi aynı `--shallow` değeriyle yeniden çalıştırırsanız aynı rastgele testleri çalıştırır.

Runtests'in `--seed` seçeneğiyle farklı bir tohumu zorlayabilirsiniz.
