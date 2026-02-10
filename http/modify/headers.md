# Başlıkları özelleştirme

Bir HTTP isteğinde, ilk istek satırından sonra tipik olarak bir dizi istek başlığı gelir. Bu, başlıkları izleyen istek gövdesinden (bazen boştur) ayıran boş bir satırla biten bir `ad: değer` (name: value) çiftleri kümesidir.

curl, isteklerde kendi adına `Host:`, `Accept:`, `User-Agent:` gibi varsayılan birkaç başlığı ve kullanıcının curl'den ne yapmasını istediğine bağlı olabilecek diğer birkaç başlığı iletir.

curl tarafından ayarlanan tüm başlıklar kullanıcı tarafından değiştirilebilir. O zaman curl'ün `-H` veya `--header` seçeneğine kullanılacak yeni başlığı söylersiniz ve başlık alanı o başlıklardan biriyle eşleşirse dahili olanı değiştirir veya belirtilen başlığı istekte gönderilecek başlıklar listesine ekler.

`Host:` başlığını değiştirmek için şunu yapın:

    curl -H "Host: test.example" http://example.com/

Bir `Elevator: floor-9` başlığı eklemek için şunu yapın:

    curl -H "Elevator: floor-9" http://example.com/

Dahili olarak oluşturulan bir başlığı silmek istiyorsanız, onu curl'e bir değer olmadan, iki nokta üst üstenin sağ tarafında hiçbir şey olmadan verin.

`User-Agent:` başlığını kapatmak için şunu yapın:

    curl -H "User-Agent:" http://example.com/

Son olarak, eğer gerçekten iki nokta üst üstenin sağ tarafında içerik olmayan bir başlık eklemek istiyorsanız (ki bu nadir bir durumdur), bunun için sihirli işaretleyici, başlık alanı adını bunun yerine bir *noktalı virgül* ile bitirmektir. Şunun gibi:

    curl -H "Empty;" http://example.com
