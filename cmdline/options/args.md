# Seçeneklere verilen argümanlar

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
