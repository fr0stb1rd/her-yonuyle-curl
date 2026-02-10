# İndirmeleri saklama

Örnek indirmeyi önceki bölümdeki gibi denerseniz, curl'ün başka bir şey yapması söylenmedikçe indirilen verileri stdout'a (standart çıktı) çıktıladığını fark edebilirsiniz. Verileri stdout'a çıktılamak, onu başka bir programa veya benzerine yönlendirmek (pipe) istediğinizde gerçekten yararlıdır, ancak indirmelerinizle başa çıkmanın her zaman en uygun yolu değildir.

curl'e indirmeyi kaydetmek için `-o [dosyaadı]` ile (seçeneğin uzun sürümü olarak `--output` ile) belirli bir dosya adı verin; burada dosya adı sadece bir dosya adı, bir dosya adına giden göreli bir yol veya dosyanın tam yolu olabilir.

Ayrıca `-o`'yu URL'den önce veya sonra koyabileceğinizi unutmayın; fark etmez:

    curl -o output.html http://example.com/
    curl -o /tmp/index.html http://example.com/
    curl http://example.com -o ../../folder/savethis.html

Bu elbette `http://` URL'leri ile sınırlı değildir, hangi tür URL indirirseniz indirin aynı şekilde çalışır:

    curl -o file.txt ftp://example.com/path/to/file-name.ext

curl'den çıktıyı terminale göndermesini isterseniz, terminalinizi ciddi şekilde bozabileceği (bazen çalışmayı durdurduğu noktaya kadar) için oraya ikili (binary) verilerin gönderilmesini algılamaya ve engellemeye çalışır. curl'ün ikili çıktı önleme özelliğini geçersiz kılabilir ve `-o -` kullanarak çıktının stdout'a gönderilmesini zorlayabilirsiniz.

curl'ün indirilen verileri saklamak ve adlandırmak için birkaç başka yolu daha vardır. Ayrıntılar aşağıdadır.

## Üzerine yazma (Overwriting)

curl yukarıda açıklandıği gibi uzak bir kaynağı yerel bir dosya adına indirdiğinde, zaten mevcut olması durumunda o dosyanın üzerine yazar. Onu *ezer* (clobbers).

curl bu ezmeyi önlemenin bir yolunu sunar: `--no-clobber`.

Bu seçeneği kullanırken ve curl verilen isme sahip bir dosyanın zaten mevcut olduğunu bulduğunda, curl bunun yerine kullanılmayan bir isim bulmak amacıyla dosya adının sonuna bir nokta artı bir sayı ekler. `1` ile başlar ve `100`'e ulaşana kadar sayılar denemeye devam eder ve mevcut olan ilkini seçer.

Örneğin, curl'den bir URL'yi `picture.png`ye indirmesini isterseniz ve o dizinde zaten `picture.png` ve `picture.png.1` adında iki dosya varsa, aşağıdakiler dosyayı `picture.png.2` olarak kaydeder:

    curl --no-clobber https://example.com/image -o picture.png

Bir kullanıcı, sonunda hangi ismin kullanıldığını anlamak için [--write-out](../verbose/writeout.md) seçeneğinin `%filename_effective` değişkenini kullanabilir.

## Hatalarda kalanlar

Varsayılan olarak, curl bir indirme sırasında bir sorunla karşılaşır ve bir hatayla çıkarsa, kısmen aktarılan dosya olduğu gibi bırakılır. Amaçlanan dosyanın küçük bir kısmı olabilir veya neredeyse tamamı olabilir. Kalanlarla ne yapılacağına karar vermek kullanıcıya kalmıştır.

`--remove-on-error` komut satırı seçeneği bu davranışı değiştirir. curl bir hatayla çıkarsa kısmen kaydedilmiş herhangi bir dosyayı silmesini söyler. Artık kalıntı yok.
