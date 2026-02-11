# Çerez motoru

curl'ün aksi söylenmedikçe yalnızca asgariyi yapma genel kavramı, varsayılan olarak çerezleri tanımasını engeller. curl'ün aldığı çerezleri takip etmesini ve ardından eşleşen çerezlere sahip isteklerde bunları göndermesini sağlamak için çerez motorunu açmanız gerekir.

Çerez motorunu curl'den çerez okumasını veya yazmasını isteyerek etkinleştirirsiniz. curl'e boş isimli dosyadan çerez okumasını söylerseniz, yalnızca motoru açarsınız ancak boş bir dahili çerez deposuyla başlarsınız:

    curl -b "" http://example.com

Sadece çerez motorunu açmak, tek bir kaynak almak ve ardından çıkmak anlamsız olurdu çünkü curl'ün aldığı herhangi bir çerezi gerçekten gönderme şansı olmazdı. Bu örnekteki sitenin çerezleri ayarlayacağını ve ardından bir yönlendirme yapacağını varsayarsak şunu yapardık:

    curl -L -b "" http://example.com
