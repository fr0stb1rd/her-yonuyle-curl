# Sıkıştırma (Compression)

curl, HTTP ve HTTPS sunucularından verilerin sıkıştırılmış sürümlerini sağlamasını ve ardından varışta otomatik olarak açılmasını istemeyi destekler. Bant genişliğinin CPU'dan daha sınırlı olduğu durumlarda bu, daha fazla veriyi daha kısa sürede almanıza yardımcı olur.

HTTP sıkıştırması iki farklı mekanizma kullanılarak yapılabilir; biri "Doğru Yol" olarak kabul edilebilecek, diğeri ise herkesin aslında kullandığı ve bunu yapmanın yaygın ve popüler yolu olandır. HTTP içeriğini sıkıştırmanın yaygın yolu **Content-Encoding** başlığını kullanmaktır. curl'den bunu `--compressed` seçeneğiyle kullanmasını istersiniz:

    curl --compressed http://example.com/

Bu seçenek etkinleştirildiğinde (ve sunucu destekliyorsa), verileri sıkıştırılmış bir şekilde teslim eder ve curl kaydetmeden veya stdout'a göndermeden önce açar. Bu genellikle bir kullanıcı olarak, daha hızlı bir transfer fark etmek dışında sıkıştırmayı gerçekten görmediğiniz veya deneyimlemediğiniz anlamına gelir.

`--compressed` seçeneği, desteklenen sıkıştırma algoritmalarından birini kullanarak Content-Encoding sıkıştırması ister. Ayrıca, bu otomatik yöntem için oluşturulan ancak hiçbir zaman gerçekten yaygın olarak benimsenmeyen istek başlığı olan nadir **Transfer-Encoding** yöntemi de vardır. curl'e `--tr-encoding` ile Transfer-Encoded sıkıştırma istemesini söyleyebilirsiniz:

    curl --tr-encoding http://example.com/

Teoride, aynı komut satırında ikisini de kullanmanızı engelleyen hiçbir şey yoktur, ancak pratikte, iki farklı şekilde sıkıştırma istendiğinde bazı sunucuların kafasının biraz karıştığını deneyimleyebilirsiniz. Genellikle sadece birini seçmek daha güvenlidir.

## HTTP başlıkları

HTTP/1.x başlıkları sıkıştırılamaz. Öte yandan HTTP/2 ve HTTP/3 başlıkları her zaman sıkıştırılır ve sıkıştırılmamış olarak gönderilemez. Ancak, kullanıcılara bir kolaylık olarak, curl, çıktıyı ve görünümü tutarlı hale getirmek için başlıkları her zaman HTTP/1.x için göründükleri stile benzer bir tarzda sıkıştırılmamış olarak gösterir.

## HTTP yüklemeleri (HTTP uploads)

POST veya PUT ile HTTP yüklemeleri için sıkıştırma yapmanın standart bir yolu yoktur. Yukarıda belirtilen HTTP sıkıştırma yöntemleri yalnızca indirmeler için çalışır.

Elbette verileri sunucuya göndermeden önce yerel olarak sıkıştırabilirsiniz.
