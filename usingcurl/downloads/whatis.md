# İndirme nedir?

curl'e bir URL vererek indirilecek kaynağı belirtirsiniz. curl, aksi söylenmedikçe bir URL indirmeyi varsayar ve URL ne indirileceğini tanımlar. Bu örnekte indirilecek URL `http://example.com`:

    curl http://example.com

URL kendi bileşenlerine ayrılır
([başka bir yerde açıklandığı gibi](../../cmdline/urls/)), doğru sunucuyla iletişime geçilir ve ardından belirli kaynağı — genellikle bir dosyayı — teslim etmesi istenir. Sunucu daha sonra verileri teslim eder veya reddeder ya da belki istemci yanlış verileri istemiştir ve o zaman o veriler teslim edilir.

Bir kaynak isteği protokole özgüdür, bu nedenle bir `FTP://` URL'si bir `HTTP://` URL'sinden veya bir `SFTP://` URL'sinden farklı çalışır.

Yol (path) kısmı olmayan bir URL, yani yalnızca bir ana bilgisayar adı kısmı olan bir URL (yukarıdaki `http://example.com` örneği gibi) dahili olarak kendisine bir eğik çizgi ('/') ekler ve ardından curl'ün sunucudan istediği kaynak bu olur.

Komut satırında birden fazla URL belirtirseniz, curl her URL'yi tek tek indirir. Önceki tamamlanana kadar ikinci transfere başlamaz, vb.
