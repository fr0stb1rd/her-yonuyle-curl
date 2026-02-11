# Zaman aşımları (Timeouts)

Tüm iç yapının bloklamayan bir şekilde yazılması gerekir ve sadece takılıp olayların gerçekleşmesini bekleyemez. Aynı zamanda, multi arayüzü kullanıcıların libcurl'ü neredeyse herhangi bir zamanda, hiçbir eylem gerçekleşmemiş veya bir zaman aşımı tetiklenmemiş olsa bile gerçekleştirmeye (perform) çağırmasına izin verir.

## Uygulamalara yalnızca tek bir zaman aşımı sunar

Harici API'de libcurl, kaç tane eşzamanlı transferin ve hangi seçeneklerin ayarlandığına bakılmaksızın aynı anda tek bir zaman aşımı sağlar. Bir uygulama, hangi API'yi kullanmak istediğine bağlı olarak `curl_multi_timeout()` ile veya bir `CURLMOPT_TIMERFUNCTION` geri çağırımında zaman aşımı değerini alabilir.

Dahili olarak bu şu şekilde yapılır:

- Her easy handle, zaman aşımlarını sıralı bir düzende tutan bir diziye sahiptir. Zamana en yakın olan (bir sonraki zaman aşımı) listede ilk sıradadır.
- Tüm easy handle'lar, zaman aşımlarına bağlı olarak düğümleri eklemeyi ve kaldırmayı hızlandıran ikili kendi kendini dengeleyen bir arama ağacı olan bir *splay ağacına* konur.
- Herhangi bir handle'ın bir sonraki zaman aşımı değişir değişmez, splay ağacı yeniden dengelenir.

Zaman aşımları dolan easy handle'ların çıkarılması hızlı bir işlemdir.

## Bir zaman aşımı ayarla

Bir zaman aşımını *ayarlamak* için dahili işlev `Curl_expire()` olarak adlandırılır. libcurl'ün bu handle için gelecekte belirli bir milisaniye içinde tekrar çağrılmasını ister. Bir zaman aşımı, aynı zaman aşımı vb. için ayarlanan önceki değerleri geçersiz kıldığından emin olmak için belirli bir kimlikle (ID) ayarlanır. Mevcut zaman aşımı kimlikleri sınırlıdır ve set sabit kodlanmıştır.

Bir zaman aşımı, verilen easy handle için zaman aşımları listesinden o zaman aşımını kaldıran `Curl_expire_clear()` ile tekrar kaldırılabilir.

## Süresi dolmuş zaman aşımları

Bir zaman aşımının süresinin dolması, uygulamanın libcurl'ü tekrar çağırması gerektiğini bildiği anlamına gelir. *socket_action* API'si kullanıldığında, zaman aşımı dolan belirli bir easy handle için libcurl'ü tekrar çağırmayı bile bilir.

Bir zaman aşımı süresi dolduğunda, perform işlevinin çağrılmasından başka özel bir eylem veya etkinlik gerçekleşmez. Her durum veya dahili işlev, (tekrar) çağrıldığında hangi zamanları veya durumları kontrol edeceğini ve buna göre hareket edeceğini bilmelidir.
