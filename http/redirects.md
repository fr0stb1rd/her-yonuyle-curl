# Yönlendirmeler (Redirects)

"Yönlendirme" (redirect), HTTP protokolünün temel bir parçasıdır. Kavram zaten 1996'da yayınlanan ilk spesifikasyonda (RFC 1945) mevcuttu ve belgelenmişti ve o zamandan beri iyi bir şekilde kullanılmaya devam etti.

Bir yönlendirme tam olarak kulağa geldiği gibidir. Sunucunun istemcinin istediği içeriği geri vermek yerine istemciye bir talimat göndermesidir. Sunucu, "istediğin o şey için *şuraya* bak" der.

Yönlendirmelerin hepsi aynı değildir. Yönlendirme kalıcı mı? İstemci bir sonraki istekte hangi istek yöntemini kullanmalı?

Tüm yönlendirmelerin ayrıca, istenmesi gereken yeni URI ile (mutlak veya göreceli olabilir) bir `Location:` başlığı geri göndermesi gerekir.

## Kalıcı ve geçici

Yönlendirme kalıcı mı yoksa sadece şimdilik geçerli mi? Bir GET'in kullanıcıları kalıcı olarak başka bir GET ile B kaynağına yönlendirmesini istiyorsanız, bir 301 geri gönderin. Bu ayrıca kullanıcı aracısının (tarayıcınızın) bunu önbelleğe alması ve orijinal URI istendiğinde bundan sonra yeni URI'ye gitmeye devam etmesi gerektiği anlamına gelir.

Geçici alternatif 302'dir. Şu anda sunucu istemcinin B'ye bir GET isteği göndermesini istiyor ancak bunu önbelleğe almamalı, bir dahaki sefere yönlendirildiğinde orijinal URI'yi denemeye devam etmelidir.

Hem 301 hem de 302'nin tarayıcıların bir sonraki istekte bir GET yapmasını sağladığını unutmayın; bu, bir POST (ve sadece POST ise) ile başladıysa yöntemi değiştirmek anlamına gelebilir. 301 ve 302 yanıtları için HTTP yönteminin GET olarak değiştirilmesinin "tarihsel nedenlerle" olduğu söylenir ancak tarayıcıların yaptığı yine de budur, bu nedenle genel webin çoğu bu şekilde davranır.

Uygulamada, 303 kodu 302'ye benzer. Önbelleğe alınmaz ve istemcinin bir sonraki istekte bir GET vermesini sağlar. 302 ve 303 arasındaki farklar incedir, ancak 303 sadece bir yönlendirmeden ziyade orijinal isteğe "dolaylı bir yanıt" için daha fazla tasarlanmış gibi görünmektedir.

Bu üç kod, HTTP/1.0 spesifikasyonundaki tek yönlendirme kodlarıydı.

Ancak curl, hiçbir yönlendirmeyi hatırlamaz veya önbelleğe almaz, bu nedenle onun için kalıcı ve geçici yönlendirmeler arasında gerçekten hiçbir fark yoktur.

## curl'e yönlendirmeleri izlemesini söyleyin

curl'ün aksi söylenmedikçe yalnızca temel olanı yapma geleneğinde, varsayılan olarak HTTP yönlendirmelerini takip etmez. Bunu yapmasını söylemek için `-L, --location` seçeneğini kullanın.

Yönlendirmeleri izleme etkinleştirildiğinde, curl varsayılan olarak 30'a kadar yönlendirmeyi izler. Sonsuz döngülere yakalanma riskini önlemek için çoğunlukla bir maksimum sınır vardır. 30 sizin için yeterli değilse, `--max-redirs` seçeneğiyle izlenecek maksimum yönlendirme sayısını değiştirebilirsiniz.

## GET mi POST mu?

Bu yanıt kodlarının üçü de, 301 ve 302/303, istemcinin ilk istekte bir POST göndermiş olsa bile yeni URI'yi almak için bir GET gönderdiğini varsayar. Bu, en azından GET kullanmayan bir şey yapıyorsanız önemlidir.

Sunucu bunun yerine istemciyi yeni bir URI'ye yönlendirmek ve ikinci istekte ilkinde yaptığı gibi aynı yöntemi göndermesini istiyorsa, örneğin önce POST gönderdiyse bir sonraki istekte tekrar POST göndermesini istiyorsa, sunucu farklı yanıt kodları kullanır.

İstemciye "POST gönderdiğin URI kalıcı olarak B'ye yönlendirildi, POST'unu şimdi ve gelecekte oraya göndermelisin" demek için sunucu bir 308 ile yanıt verir. İşleri karmaşıklaştırmak gerekirse, 308 kodu yalnızca yakın zamanda tanımlanmıştır ([spesifikasyon](https://tools.ietf.org/html/rfc7238#section-3) Haziran 2014'te yayınlandı), bu nedenle eski istemciler bunu doğru işlemeyebilir. Eğer öyleyse, sizin için kalan tek yanıt kodu şudur...

Bir müşteriye bir sonraki istekte de POST göndermesini, ancak geçici olarak söyleyen (eski) yanıt kodu 307'dir. Ancak bu yönlendirme istemci tarafından önbelleğe alınmaz, bu nedenle tekrar istenirse yine A'ya gönderir. 307 kodu HTTP/1.1'de tanıtıldı.

Ve, yönlendirmeler HTTP/2'de HTTP/1.1'de olduğu gibi aynı şekilde çalışır.

|                     |Kalıcı   | Geçici      |
|---------------------|----------|-------------|
|GET'e geçiş yap      | 301      | 302 ve 303  |
|Orijinal yöntemi koru| 308      | 307         |

### Yönlendirmelerde hangi yöntemin kullanılacağına karar verin

Dünyada orijinal URL'ye bir POST gönderilmesini isteyen, ancak 301, 302 veya 303 yanıt kodlarını kullanan HTTP yönlendirmeleriyle yanıt veren ve *hala* HTTP istemcisinin bir sonraki isteği bir POST olarak göndermesini isteyen web hizmetleri olduğu ortaya çıktı. Yukarıda açıklandığı gibi, tarayıcılar bunu yapmaz ve varsayılan olarak curl de yapmaz.

Bu kurulumlar var olduğundan ve aslında çok nadir olmadığından, curl davranışını değiştirmek için seçenekler sunar.

curl'e 30x yanıtından sonra GET olmayan istek yöntemini GET olarak değiştirmemesini, buna özel seçenekleri kullanarak söyleyebilirsiniz: `--post301`, `--post302` ve `--post303`. Bunun yerine libcurl tabanlı bir uygulama yazıyorsanız, bu davranışı `CURLOPT_POSTREDIR` seçeneğiyle kontrol edersiniz.

## Diğer ana bilgisayar adlarına yönlendirme

curl kullandığınızda belirli bir site için kullanıcı adı ve şifre gibi kimlik bilgileri sağlayabilirsiniz, ancak bir HTTP yönlendirmesi farklı bir ana bilgisayara taşınabileceğinden, curl aynı transfer içinde orijinalden başka ana bilgisayarlara gönderdiklerini sınırlar.

Kimlik bilgilerinin, orijinalle aynı olmasalar bile (muhtemelen onlara güvendiğiniz ve bunu yapmanın bir zararı olmadığını bildiğiniz için) aşağıdaki ana bilgisayar adlarına da gönderilmesini istiyorsanız, `--location-trusted` seçeneğini kullanarak curl'e bunun uygun olduğunu söyleyebilirsiniz.

# HTTP olmayan yönlendirmeler

Tarayıcılar, yönlendirmeleri yapmak için bazen bir curl kullanıcısı için hayatı karmaşıklaştıran daha fazla yolu destekler, çünkü bu yöntemler curl tarafından desteklenmez veya tanınmaz.

## HTML yönlendirmeleri

Yukarıdakiler yeterli değilse, web dünyası ayrıca tarayıcıları düz HTML ile yönlendirmek için bir yöntem sağlar. Aşağıdaki örnek `<meta>` etiketine bakın. Bu curl ile biraz karmaşıktır çünkü curl asla HTML'yi ayrıştırmaz ve bu nedenle bu tür yönlendirmeler hakkında hiçbir bilgisi yoktur.

    <meta http-equiv="refresh" content="0; url=http://example.com/">

## JavaScript yönlendirmeleri

Modern web JavaScript ile doludur ve bildiğiniz gibi, JavaScript, web sitelerini ziyaret ederken tarayıcıda kodun yürütülmesine izin veren bir dil ve tam bir çalışma zamanıdır.

JavaScript ayrıca tarayıcıya başka bir siteye geçmesi - isterseniz bir yönlendirme - talimatı vermesi için araçlar sağlar.

