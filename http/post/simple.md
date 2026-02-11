# Basit POST

Form verilerini göndermek için bir tarayıcı, verileri ve işareti (`&`) sembolleriyle ayrılmış bir dizi `ad=değer` çifti olarak URL kodlar. Ortaya çıkan dize bir POST isteğinin gövdesi olarak gönderilir. Aynısını curl ile yapmak için `-d` (veya `--data`) argümanını şu şekilde kullanın:

    curl -d 'name=admin&shoesize=12' http://example.com/

Komut satırında birden fazla `-d` seçeneği belirtirken, curl bunları birleştirir ve aralarına ve işareti ekler, bu nedenle yukarıdaki örnek şu şekilde de yazılabilir:

    curl -d name=admin -d shoesize=12 http://example.com/

Gönderilecek veri miktarı komut satırında sadece bir dize olamayacak kadar büyükse, verileri standart curl tarzında bir dosya adından da okuyabilirsiniz:

    curl -d @filename http://example.com

Sunucu verilerin özel bir şekilde kodlandığını varsayabilirken, curl göndermesini söylediğiniz verileri kodlamaz veya değiştirmez. **curl tam olarak verdiğiniz baytları gönderir** (bir dosyadan okurken `-d`'nin satır başlarını ve yeni satırları atlaması dışında; bu nedenle bunların veriye dahil edilmesini istiyorsanız `--data-binary` kullanmanız gerekir).

`@` sembolüyle başlayan bir POST gövdesi göndermek için, curl'ün bunu bir dosya adı olarak yüklemeye çalışmasını önlemek üzere, bunun yerine `--data-raw` kullanın. Bu seçeneğin dosya yükleme yeteneği yoktur:

    curl --data-raw '@string' https://example.com
