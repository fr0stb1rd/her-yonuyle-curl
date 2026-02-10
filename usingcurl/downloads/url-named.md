# URL ile adlandırılan bir dosyaya indirme

Ancak birçok URL, dosya adı kısmını zaten en sağ uçta içerir. curl, bunu bir kısayol olarak kullanmanıza izin verir, böylece `-o` ile tekrarlamak zorunda kalmazsınız. Şunun yerine:

    curl -o file.html http://example.com/file.html

Uzak URL kaynağını şununla yerel 'file.html' dosyasına kaydedebilirsiniz:

    curl -O http://example.com/file.html

Bu `-O` (büyük harf O) seçeneğidir veya uzun isim sürümü için `--remote-name`dir. `-O` seçeneği, sağladığınız URL'nin dosya adı kısmını seçerek kullanılacak yerel dosya adını seçer. Bu önemlidir. URL'yi belirtirsiniz ve curl bu verilerden adı seçer. Site curl'ü daha uzağa yönlendirirse (ve curl'e yönlendirmeleri izlemesini söylerseniz), curl'ün bunu saklamak için kullandığı dosya adını değiştirmez.

## Başka bir dizinde saklama

Kullanılacak doğru dosya adı yukarıda açıklandığı gibi seçildiğinde, `--output-dir` kullanarak o dosyanın kaydedileceği dizini yine de değiştirebilirsiniz. Özellikle `-O` ile birlikte kullanıldığında yararlıdır, çünkü bu seçenek aksi takdirde dosyanın geçerli dizine kaydedilmesini ifade eder.

Yeni dosyayı URL'den alınan bir dosya adını kullanarak `/tmp` dizinine kaydetmek için:

    curl -O --output-dir /tmp http://example.com/file.html

## Tüm URL'ler için URL'nin dosya adı kısmını kullanma

Yüzlerce URL kullanırken yüzlerce `-O` seçeneği eklemeye bir tepki olarak, `--remote-name-all` adında bir seçenek sunduk. Bu, `-O`'yu verilen tüm URL'ler için varsayılan işlem yapar. URL'ler için hala bireysel "saklama talimatları" sağlayabilirsiniz ancak indirilen bir URL için bir tane bırakırsanız, varsayılan eylem o zaman stdout'tan -O stiline geçer.
