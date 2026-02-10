# Çoklu indirmeler

curl'e tek bir komut satırında birçok URL'yi indirmesi söylenebildiğinden, elbette bu indirmeleri güzelce adlandırılmış yerel dosyalarda saklamak istediğiniz zamanlar olur.

Bunu anlamanın anahtarı, her indirme URL'sinin kendi "saklama talimatına" ihtiyaç duymasıdır. Söz konusu "saklama talimatı" olmadan curl varsayılan olarak verileri stdout'a gönderir. İki URL isterseniz ve curl'e yalnızca ilk URL'yi nereye kaydedeceğini söylerseniz, ikincisi stdout'a gönderilir. Şöyle:

    curl -o one.html http://example.com/1 http://example.com/2

"Saklama talimatları" indirme URL'leriyle aynı sırayla okunur ve işlenir, bu nedenle URL'nin yanında olmaları gerekmez. Tüm çıktı seçeneklerini en başta, en sonda veya URL'lerle serpiştirilmiş olarak toplayabilirsiniz. Siz seçin.

Bu örneklerin hepsi aynı şekilde çalışır:

    curl -o 1.txt -o 2.txt http://example.com/1 http://example.com/2
    curl http://example.com/1 http://example.com/2 -o 1.txt -o 2.txt
    curl -o 1.txt http://example.com/1 http://example.com/2 -o 2.txt
    curl -o 1.txt http://example.com/1 -o 2.txt http://example.com/2

`-O` benzer şekilde tek bir indirme için sadece bir talimattır, bu nedenle birden fazla URL indirirseniz bunlardan daha fazlasını kullanın:

    curl -O -O http://example.com/1 http://example.com/2

## Paralel

Aksi belirtilmedikçe, curl verilen tüm URL'leri seri bir şekilde, tek tek indirir. `-Z` (veya `--parallel`) kullanarak curl bunun yerine transferleri [paralel olarak](../../cmdline/urls/parallel.md) yapabilir: aynı anda birkaç tane.
