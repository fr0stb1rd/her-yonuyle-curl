# HTTP/2

curl, uygun ön koşullarla oluşturulduğu varsayılarak hem HTTP:// hem de HTTPS:// URL'leri için HTTP/2'yi destekler. Hatta bir HTTPS URL'si verildiğinde varsayılan olarak HTTP/2'yi kullanır çünkü bunu yapmak herhangi bir ceza (performans kaybı) anlamına gelmez ve curl HTTP/2'yi desteklemeyen sitelerle kullanıldığında istek bunun yerine HTTP/1.1'i müzakere eder.

Ancak HTTP:// URL'leri ile HTTP/2'ye yükseltme, fazladan bir gidiş-dönüşe (round-trip) neden olabilen ve belki daha da zahmetlisi, eski sunucuların önemli bir kısmının böyle bir başlık gördüğünde 400 yanıtı döndürdüğü bir `Upgrade:` başlığı ile yapılır.

Ayrıca `HTTP://` için HTTP/2'yi destekleyen bazı (çoğu?) sunucuların (ki bu başlı başına tüm sunucular değildir), örneğin POST'ta `Upgrade:` başlığını kabul etmediği de belirtilmelidir.

Bir sunucudan HTTP/2 kullanmasını istemek için sadece:

    curl --http2 http://example.com/

curl'ünüz HTTP/2'yi desteklemiyorsa, o komut satırı aracı bunu söyleyen bir hata döndürür. `curl -V` çalıştırmak curl sürümünüzün bunu destekleyip desteklemediğini gösterir.

Sunucunuzun HTTP/2 konuştuğunu zaten biliyorsanız (örneğin, makinelerinizde tam olarak neyin çalıştığını bildiğiniz kendi kontrollü ortamınızda), `--http2-prior-knowledge` ile HTTP/2 müzakeresini kısayoldan geçebilirsiniz.

## Çoklama (Multiplexing)

HTTP/2 protokolündeki birincil özellik, aynı fiziksel bağlantı üzerinden birkaç mantıksal akışı çoklama (multiplex) yeteneğidir. curl komut satırı aracı, [paralel transferler yaparken](../../cmdline/urls/parallel.md) bu özellikten yararlanabilir.
