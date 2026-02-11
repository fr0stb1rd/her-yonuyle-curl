# Durdurma (Stop)

Bir İnternet transferi kısa olabilir ancak uzun zaman da alabilir. Belki de sonsuz miktarda zaman.

libcurl normalde transferleri tamamlanana veya bir hata oluşana kadar gerçekleştirir. Bu olaylardan hiçbiri gerçekleşmezse, transfer devam eder.

Bazen, bir libcurl transferini aksi takdirde duracağı zamandan önce durdurmak isteyebilirsiniz.

## easy API

Başka bir yerde açıklandığı gibi, `curl_easy_perform()` işlevi eşzamanlı bir işlev çağrısıdır. Dönmeden önce tüm transferi yapar.

Bir transferi aksi takdirde sona ereceği zamandan önce durdurmanın birkaç farklı yolu vardır:

1. bir geri çağırımdan hata döndürmek
2. transferin belirli bir süre sonra durmasını sağlayan bir seçenek ayarlamak

Her [geri çağırım (callback)](../callbacks/) bir hata döndürebilir ve o işlevlerden birinden bir hata döndürüldüğünde tüm transfer durdurulur. Örneğin okuma, yazma veya ilerleme geri çağırımları.

İkinci yol, bir süre sonra veya belirli bir durumda transferi durduran bir zaman aşımı veya başka bir seçenek ayarlamaktır. Örneğin aşağıdakilerden biri veya birkaçı:

1. `CURLOPT_TIMEOUT` - tüm transferin alabileceği maksimum süreyi ayarla
2. `CURLOPT_CONNECTTIMEOUT` - "bağlantı aşamasının" alabileceği maksimum süreyi ayarla
3. `CURLOPT_LOW_SPEED_LIMIT` - kabul edilebilir en düşük transfer hızını ayarla. `CURLOPT_LOW_SPEED_TIME` saniye sayısı boyunca bu hızdan daha yavaşsa transfer durur.

Uygulamanızın devam eden bir `curl_easy_perform()` çağrısını başka bir iş parçacığından durdurmasına izin veren sağlanan bir işlev yoktur. Yaygın öneri, bu niyeti bir geri çağırımda algılayabileceğiniz özel bir yolla bildirmeniz ve bu gerçekleştiğinde o geri çağırımın hata döndürmesini sağlamanızdır.

## multi API

Multi arayüz genellikle engellemeyen (non-blocking) bir API'dir, bu nedenle çoğu durumda ilgili easy handle'ı `curl_multi_remove_handle()` kullanarak multi handle'dan kaldırarak bir transferi durdurabilirsiniz.

Multi API'yi kullandığınızda, libcurl'ü libcurl'ün çalıştığı soketlerdeki etkinlikleri veya trafiği beklemesi için çağırabilirsiniz. `curl_multi_poll()` gibi bir şeyin olmasını (veya bir zaman aşımının dolmasını) beklerken engelleyebilecek bir çağrı.

Bir uygulama, başka bir iş parçacığından `curl_multi_wakeup()` çağırarak engellenen bir `curl_multi_poll()` çağrısının uyanmasını ve zorla ve hemen dönmesini sağlayabilir.
