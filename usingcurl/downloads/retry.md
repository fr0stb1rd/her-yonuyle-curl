# Yeniden deneme (Retry)

Normalde curl, bir transfer gerçekleştirmek için yalnızca tek bir girişimde bulunur ve başarılı olmazsa bir hata döndürür. `--retry` seçeneğini kullanarak curl'e belirli başarısız transferleri yeniden denemesini söyleyebilirsiniz.

curl bir transfer gerçekleştirmeye çalışırken geçici bir hata döndürülürse, pes etmeden önce bu sayı kadar yeniden dener. Sayıyı 0'a ayarlamak curl'ün yeniden deneme yapmamasını sağlar (bu varsayılandır). Geçici hata şunlardan biri anlamına gelir: bir zaman aşımı, bir FTP 4xx yanıt kodu veya bir HTTP 408, 429, 500, 502, 503 veya 504 yanıt kodu.

## Yeniden denemelerinizi ayarlayın

curl bir transferi yeniden denemek üzereyken, önce bir saniye bekler ve ardından gelen tüm yeniden denemeler için bekleme süresini 10 dakikaya ulaşana kadar ikiye katlar; bu daha sonra geri kalan yeniden denemeler arasındaki gecikmedir. `--retry-delay` kullanarak bu üstel geri çekilme algoritmasını devre dışı bırakabilir ve denemeler arasına kendi gecikmenizi ayarlayabilirsiniz. `--retry-max-time` ile yeniden denemeler için izin verilen toplam süreyi sınırlarsınız. `--max-time` seçeneği yine de bu transferlerin tek birinin harcamasına izin verilen en uzun süreyi belirtir.

curl'ü 5 defaya kadar yeniden denemeye zorlayın, ancak iki dakikadan fazla değil:

    curl --retry 5 --retry-max-time 120 https://example.com

## Bağlantı reddedildi

Varsayılan yeniden deneme mekanizması, yalnızca geçici hatalar olarak kabul edilenler için transferleri yeniden dener. Bunlar, sunucunun kendisinin ipucu verdiği ve şu anda orada olduğunu ancak daha sonraki bir zamanda gidebileceğini nitelendirdiği hatalardır.

Bazen bir kullanıcı olarak durum hakkında daha fazla bilgi sahibi olursunuz ve o zaman curl'ün daha iyi yeniden denemeler yapmasına yardımcı olabilirsiniz. Başlangıç ​​olarak, curl'e "bağlantı reddedildi" (connection refused) hatasını geçici bir hata olarak kabul etmesini söyleyebilirsiniz. Belki iletişim kurduğunuz sunucunun istikrarsız biri olduğunu biliyorsunuzdur veya belki de yeniden başlatıldığında bazen ondan indirmeye çalıştığınızı biliyorsunuzdur. Bunun için `--retry-connrefused` kullanırsınız.

Örneğin: 5 defaya kadar yeniden deneyin ve `ECONNREFUSED`'ı yeniden deneme nedeni olarak kabul edin:

    curl --retry 5 --retry-connrefused https://example.com

## Herhangi bir ve tüm hatalarda yeniden deneyin

Yeniden denemenin en agresif biçimi, URL'nin çalışması gerektiğini **bildiğiniz** ve herhangi bir başarısızlığa tahammül etmediğiniz durumlar içindir. `--retry-all-errors` kullanmak, curl'ün tüm transfer başarısızlıklarını yeniden deneme nedeni olarak görmesini sağlar.

Örneğin: tüm hatalar için 12 defaya kadar yeniden deneyin:

    curl --retry 12 --retry-all-errors https://example.com
