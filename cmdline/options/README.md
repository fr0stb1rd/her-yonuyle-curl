# Komut satırı seçenekleri

curl'e bir şey yapmasını söylediğinizde, curl'ü, transferin hakkında olmasını istediğiniz URL veya URL setine eşlik edecek sıfır, bir veya birkaç komut satırı seçeneğiyle çağırırsınız. curl iki yüzden fazla farklı seçeneği destekler.

## Kısa seçenekler

Komut satırı seçenekleri, curl'e nasıl davranmasını istediğiniz hakkında bilgi aktarır. Örneğin, -v seçeneğiyle curl'den ayrıntılı (verbose) modunu açmasını isteyebilirsiniz:

    curl -v http://example.com

-v burada bir "kısa seçenek" olarak kullanılır. Bunları eksi sembolü ve hemen ardından gelen tek bir harfle yazarsınız. Birçok seçenek, bir şeyi açan veya iki bilinen durum arasında bir şeyi değiştiren anahtarlardır. Sadece o seçenek adıyla kullanılabilirler. Ayrıca eksiden sonra birkaç tek harfli seçeneği birleştirebilirsiniz. Hem ayrıntılı mod hem de curl'ün HTTP yönlendirmelerini takip etmesini istemek için:

    curl -vL http://example.com

curl'deki komut satırı ayrıştırıcısı her zaman tüm satırı ayrıştırır ve seçenekleri istediğiniz yere koyabilirsiniz; URL'den sonra da görünebilirler:

    curl http://example.com -Lv

ve iki ayrı kısa seçenek elbette ayrı ayrı da belirtilebilir, şöyle:

    curl -v -L http://example.com

## Uzun seçenekler

Tek harfli seçenekler, yazılması ve kullanılması hızlı olduğu için uygundur, ancak alfabede yalnızca sınırlı sayıda harf olduğundan ve kontrol edilecek çok şey olduğundan, tüm seçenekler bu şekilde mevcut değildir. Bu nedenle bunlar için uzun seçenek adları sağlanmıştır. Ayrıca, kolaylık olması ve betiklerin daha okunabilir olması için, çoğu kısa seçeneğin daha uzun isim takma adları vardır.

Uzun seçenekler her zaman *iki* eksi (veya onlara ne demek isterseniz *tire*) ve ardından isimle yazılır ve çift eksi başına yalnızca bir seçenek adı yazabilirsiniz. Uzun seçenek formatını kullanarak ayrıntılı mod istemek şöyle görünür:

    curl --verbose http://example.com

ve uzun formatı kullanarak HTTP yönlendirmelerini de istemek şöyle görünür:

    curl --verbose --location http://example.com

## Seçeneklere verilen argümanlar

Tüm seçenekler özellikleri etkinleştiren veya devre dışı bırakan basit boole bayrakları değildir. Bazıları için, belki bir kullanıcı adı veya bir dosyaya giden yol gibi veriler aktarmanız gerekir. Bunu önce seçeneği sonra argümanı, aralarında bir boşluk bırakarak yazarak yaparsınız. Örneğin, bir sunucuya HTTP POST ile rastgele bir veri dizesi göndermek istiyorsanız:

    curl -d arbitrary http://example.com

ve seçeneğin uzun formunu kullansanız bile aynı şekilde çalışır:

    curl --data arbitrary http://example.com

Kısa seçenekleri argümanlarla kullandığınızda, aslında verileri boşluk ayırıcı olmadan da yazabilirsiniz:

    curl -darbitrary http://example.com

## Boşluklu argümanlar

Bazen bir seçeneğe bir argüman iletmek istersiniz ve bu argüman bir veya daha fazla boşluk içerir. Örneğin, curl'ün kullandığı kullanıcı aracısı (user-agent) alanını, o üç boşluk dahil olmak üzere tam olarak `I am your father` olacak şekilde ayarlamak istersiniz. O zaman komut satırında curl'e iletirken dizenin etrafına tırnak işaretleri koymanız gerekir. Kullanılacak tam tırnak işaretleri kabuğunuza/komut isteminize bağlı olarak değişir, ancak genellikle çoğu yerde çift tırnak işe yarar:

    curl -A "I am your father" http://example.com

Tırnak işareti kullanmamak, örneğin komut satırını şöyle yazarsanız:

    curl -A I am your father http://example.com

… curl'ün kullanıcı aracısı dizesi olarak yalnızca 'I' kullanmasına neden olur ve `am`, `your` ve `father` dizeleri, seçenek olduklarını belirtmek için `-` ile başlamadıkları ve curl yalnızca seçenekleri ve URL'leri işlediği için bunun yerine ayrı URL'ler olarak ele alınır.

Dizenin kendisinin çift tırnak içermesini sağlamak için (örneğin sunucuya bir JSON dizesi göndermek istediğinizde yaygındır), tek tırnak kullanmanız gerekebilir (tek tırnakların aynı şekilde çalışmadığı Windows hariç). JSON dizesi `{ "name": "Darth" }` gönderelim:

    curl -d '{ "name": "Darth" }' http://example.com

Veya tek tırnak olayından kaçınmak isterseniz, verileri curl'e bir dosya aracılığıyla göndermeyi tercih edebilirsiniz, bu da ekstra tırnak içine almayı gerektirmez. Yukarıda belirtilen verileri içeren dosyaya 'json' dediğimizi varsayalım:

    curl -d @json http://example.com

## Negatif seçenekler

Bir şeyi açan seçenekler için, onu kapatmanın da bir yolu vardır. O zaman seçeneğin uzun formunu, ismin önünde bir `no-` öneki ile kullanırsınız. Örnek olarak, ayrıntılı modu kapatmak için:

    curl --no-verbose http://example.com
