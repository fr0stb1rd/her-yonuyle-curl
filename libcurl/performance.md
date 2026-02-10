# Performans

Bu bölüm, libcurl'den maksimum performans elde etmek için bir uygulama yazarı olarak yapabilecekleriniz hakkında genel tavsiyeleri toplar.

libcurl varsayılan olarak mümkün olduğunca hızlı çalışacak şekilde tasarlanmış ve amaçlanmıştır. Özellikle fazladan bir şey yapmadan zaten en yüksek performansı almanız beklenir. Ancak bakılması gereken bazı yaygın şeyler veya belki kaçınılması gereken hatalar vardır.

## handle'ları yeniden kullanın

Bu, libcurl ne zaman tartışılsa genel bir mantradır. Easy arayüzü kullanıyorsanız, yüksek performansın *birincil* anahtarı, sonraki transferleri yaparken handle'ları (tanıtıcıları) yeniden kullanmaktır. Bu, libcurl'ün bağlantıları yeniden kullanmasını, TLS oturumlarını yeniden kullanmasını, DNS önbelleğini mümkün olduğunca kullanmasını ve daha fazlasını sağlar.

## tampon boyutları

Veri indiriyorsanız, `CURLOPT_BUFFERSIZE`'ı uygun bir boyuta ayarlayın. Başlangıçta daha küçük bir boyuttadır ve özellikle yüksek hızlı transferlerde, boyutunu artırarak libcurl'den daha fazlasını elde edebilirsiniz. Kullanım durumunuzla bir kıyaslamada (benchmark) birkaç boyutu denemenizi öneririz.

Benzer şekilde, veri yüklüyorsanız, aynı nedenlerle `CURLOPT_UPLOAD_BUFFERSIZE`'ı ayarlamak isteyebilirsiniz.

## havuz boyutu

`CURLOPT_MAXCONNECTS` ile ayarladığınız bağlantı havuzunda tutulan canlı bağlantı sayısı, ince ayar yapmak için ilginç olabilir. Elbette uygulamanızın bağlantıları nasıl kullandığına bağlı olarak, ancak örneğin kısa bir süre içinde N ana bilgisayar adı üzerinde yineleniyorsa, libcurl'ün tüm bu bağlantıları canlı tutabildiğinden emin olmak sizin için mantıklı olabilir.

## CA deposu önbelleğe alma

TLS kullanılarak yapılan her yeni bağlantı için, libcurl'ün uzak sunucunun sertifikasını doğrulamak üzere CA deposuna erişmesi gerekir. Uygulamalarınız çok sayıda bağlantı yapıyorsa, libcurl'ün diskten yüzlerce kilobayt'ı tekrar tekrar yüklemekten ve ayrıştırmaktan kaçınabilmesi için libcurl'ün CA önbelleğe almasından yararlandığınızdan emin olun. Ancak bu henüz tüm TLS arka uçları tarafından desteklenmemektedir.

## geri çağırımları (callback) mümkün olduğunca hızlı yapın

Yüksek hızlı veri indirmelerinde, yazma geri çağırımı birçok kez çağrılır. Bu işlev mümkün olan en hızlı şekilde yürütülecek şekilde yazılmazsa, bu işlevin tek başına *tüm* transferleri aksi takdirde olabileceklerinden daha yavaş hale getirme riski vardır.

Aynısı elbette yüklemeler için okuma geri çağırımı için de geçerlidir.

libcurl geri çağırımlarınızda karmaşık mantık yapmaktan veya kilitler/mutexler kullanmaktan kaçının.

## verileri paylaşın

Birden fazla easy handle kullanıyorsanız, performansı artırmak için verileri ve önbellekleri aralarında yine de paylaşabilirsiniz. [Paylaşım API'sine](../helpers/sharing.md) daha yakından bakın.

## iş parçacıkları (threads)

Transfer iş parçacığınız %100 CPU tüketmeye başlarsa, bant genişliğini artırmak için yükü birden fazla iş parçacığına dağıtmaktan fayda sağlayabilirsiniz.

Normalde o zaman, birbirlerinin performansına müdahale etmekten kaçınmak veya paylaşılan handle'lar nedeniyle iş parçacığı güvenliği sorunlarına girme riskinden kaçınmak için her iş parçacığının transferleri mümkün olduğunca bağımsız yapmasını istersiniz. Bağlantı yeniden kullanımının optimize edilebilmesi için aynı ana bilgisayar adlarının aynı iş parçacığında aktarılmasını sağlamaya çalışın.

## `curl_multi_socket_action`

Uygulamanız birçok paralel transfer gerçekleştiriyorsa, örneğin yüzden fazla eşzamanlı transfer gibi, o zaman "normal" multi API yerine `curl_multi_socket_action()` ve olay tabanlı API'ye geçmeyi *kesinlikle* düşünmelisiniz. Bu, uygulamanızın hem `poll()` hem de `select()` kullanmaktan kaçınmasını sağlayan olay tabanlı bir yaklaşım kullanmanıza izin verir ve sizi buna zorlar; bu, yüksek derecede paralellik ile birlikte yüksek performansın anahtarıdır.
