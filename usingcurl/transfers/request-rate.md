# İstek hızı sınırlama

Tek bir komut satırında birden fazla transfer yapması söylendiğinde, bir kullanıcının bu birden fazla transferin mümkün olduğunca hızlı değil de daha yavaş yapılmasını tercih edeceği zamanlar olabilir. Buna *istek hızı sınırlama* (request rate limiting) diyoruz.

`--rate` seçeneğiyle, curl'ün kullanmasına izin verdiğiniz maksimum transfer sıklığını - zaman birimi başına transfer başlangıcı sayısı (bazen istek hızı olarak adlandırılır) olarak - belirtirsiniz. Bu seçenek olmadan, curl bir sonraki transfere mümkün olduğunca hızlı başlar.

Birkaç URL verilirse ve bir transfer izin verilen hızdan daha hızlı tamamlanırsa, curl istenen hızı korumak için bir sonraki transferi başlatmayı geciktirir. Bu seçenek seri transferler içindir ve [--parallel](../../cmdline/urls/parallel.md) kullanıldığında hiçbir etkisi yoktur.

İstek hızı **N/U** olarak sağlanır; burada N bir tam sayı ve U bir zaman birimidir. Desteklenen birimler `s` (saniye), `m` (dakika), `h` (saat) ve `d` (gün, 24 saatlik bir birim olarak) şeklindedir. Varsayılan zaman birimi, **/U** sağlanmazsa saat başına transfer sayısıdır.

curl'e dakikada 10 isteğe izin verilmesi söylenirse, önceki transferin başlatılmasından bu yana 6 saniye geçene kadar bir sonraki isteği başlatmaz.

Bu işlev milisaniye çözünürlüğü kullanır. İzin verilen sıklık saniyede 1000'den fazla ayarlanırsa, bunun yerine sınırsız çalışır.

[--retry](../downloads/retry.md) ile etkinleştirilen transferleri yeniden denerken, bu ayar değil, ayrı yeniden deneme gecikmesi mantığı kullanılır.

Bu seçenek birkaç kez kullanılırsa sonuncusu kullanılır.

Örneğin, curl'ün 100 resim indirmesini sağlayın ancak bunu saniyede 2 transferden daha hızlı yapmamasını sağlayın:

    curl --rate 2/s -O https://example.com/[1-100].jpg

curl'ün 10 resim indirmesini sağlayın ancak bunu saatte 3 transferden daha hızlı yapmamasını sağlayın:

    curl --rate 3/h -O https://example.com/[1-10].jpg

curl'ün 200 resim indirmesini sağlayın ancak dakikada 14 transferden daha hızlı yapmamasını sağlayın:

    curl --rate 14/m -O https://example.com/[1-200].jpg

## Birim sayısı

curl 8.10.0'dan başlayarak, bu seçenek isteğe bağlı bir *birim sayısı* kabul eder. İstek hızı daha sonra **N** / **Z** **U** (boşluksuz) olarak sağlanır; burada **N** bir sayıdır, **Z** bir zaman birimi sayısıdır ve **U** bir zaman birimidir.

Sayı ve birimler yukarıda belirtilenlerle aynıdır, ancak artık bir zaman birimi sayısı da belirtebilirsiniz. **Z** sayısı kadar **U** biriminde **N** istek.

Örneğin, her beş saniyede sekizden fazla transfer yapmayın:

    curl --rate 8/5s -O https://example.com/[1-100].jpg
