# Aralıklar (Ranges)

Ya istemci uzak bir kaynaktan yalnızca ilk 200 baytı veya ortada bir yerde 300 baytı istiyorsa? HTTP protokolü, bir istemcinin yalnızca belirli bir veri aralığını istemesine izin verir. İstemci sunucudan bir başlangıç ofseti ve bir bitiş ofseti ile belirli aralığı ister. Hatta şeyleri birleştirebilir ve sadece bir sürü parçayı yan yana listeleyerek aynı istekte birkaç aralık isteyebilir. Bir sunucu böyle bir talebi yanıtlamak için birden fazla bağımsız parça geri gönderdiğinde, bunları mime sınır dizeleriyle ayrılmış olarak alırsınız ve buna göre işlemek kullanıcı uygulamasına bağlıdır. curl böyle bir yanıtı daha fazla ayırmaz.

Ancak, bir bayt aralığı sunucuya yalnızca bir istektir. İsteğe saygı duymak zorunda değildir ve sunucunun içeriği istendiğinde anında otomatik olarak oluşturduğu durumlar gibi birçok durumda, bunu yapmayı reddeder ve bunun yerine tam içeriği yanıtlar.

curl'ün `-r` veya `--range` ile bir aralık istemesini sağlayabilirsiniz. Bir şeyin ilk 200 baytını istiyorsanız:

    curl -r 0-199 http://example.com

Veya 200. indisten başlayan dosyadaki her şeyi:

    curl -r 200- http://example.com

İndeks 0'dan 200 bayt *ve* indeks 1000'den 200 bayt alın:

    curl -r 0-199,1000-1199 http://example.com/
