# URL globbing

Bazen, istekler arasında yalnızca küçük bir kısmı değişen, çoğunlukla aynı olan bir dizi URL almak istersiniz. Belki sayısal bir aralıktır veya belki bir dizi isimdir. curl, bunlar gibi birçok URL'yi kolayca belirtmenin bir yolu olarak "globbing" sunar.

Globbing bunun için [] ve {} ayrılmış sembollerini kullanır; bu semboller normalde yasal bir URL'nin parçası olamaz (sayısal IPv6 adresleri hariç ancak curl bunları zaten iyi işler). Globbing yolunuza çıkarsa, `-g, --globoff` ile devre dışı bırakın.

Bir komut satırı isteminden çağrıldığında [] veya {} dizilerini kullanırken, kabuğun buna müdahale etmesini önlemek için muhtemelen tam URL'yi çift tırnak içine almanız gerekir. Bu aynı zamanda '&', '?' ve '*' gibi özel işlem gören diğer karakterler için de geçerlidir.

curl'deki transferle ilgili çoğu işlevsellik libcurl kütüphanesi tarafından sağlanırken, URL globbing özelliği sağlanmaz.

## Sayısal aralıklar

[N-M] sözdizimi ile sayısal bir aralık isteyebilirsiniz, burada N başlangıç indeksidir ve M'ye kadar ve M dahil olmak üzere gider. Örneğin, sayısal olarak adlandırılmış 100 görüntüyü tek tek isteyebilirsiniz:

    curl -O "http://example.com/[1-100].png"

ve hatta sıfır önekleriyle aralıklar yapabilir, örneğin sayı her zaman üç basamaklıysa:

    curl -O "http://example.com/[001-100].png"

Veya belki de sadece çift sayılı görüntüleri istiyorsunuz, bu yüzden curl'e bir adım sayacı da söylersiniz. Bu örnek aralık 0'dan 100'e 2'lik artışlarla gider:

    curl -O "http://example.com/[0-100:2].png"

## Alfabetik aralıklar

curl, bir sitenin a'dan z'ye adlandırılmış bölümleri olduğu zamanki gibi alfabetik aralıklar da yapabilir:

    curl -O "http://example.com/section[a-z].html"

## Liste

Bazen parçalar bu kadar kolay bir deseni takip etmez ve o zaman bunun yerine tam listeyi kendiniz verebilirsiniz ancak o zaman aralıklar için kullanılan köşeli parantezler yerine süslü parantezler içinde:

    curl -O "http://example.com/{one,two,three,alpha,beta}.html"

## Kombinasyonlar

Aynı URL'de birkaç glob kullanabilirsiniz, bu da curl'ün bunlar üzerinde de yineleme yapmasını sağlar. Ben, Alice ve Frank'in görüntülerini hem 100 x 100 hem de 1000 x 1000 çözünürlüklerinde indirmek için bir komut satırı şuna benzeyebilir:

    curl -O "http://example.com/{Ben,Alice,Frank}-{100x100,1000x1000}.jpg"

Veya bir satranç tahtasının tüm görüntülerini, 0 ila 7 aralığındaki iki koordinatla indekslenmiş olarak indirin:

    curl -O "http://example.com/chess-[0-7]x[0-7].jpg"

Elbette aralıkları ve serileri karıştırabilirsiniz. Hem web sunucusu hem de posta sunucusu için bir haftalık günlükleri (logs) alın:

    curl -O "http://example.com/{web,mail}-log[0-6].txt"

## Globbing için çıktı değişkenleri

Bu bölümdeki önceki tüm globbing örneklerinde, curl'ün kullanılan URL'nin dosya adı kısmını kullanarak hedef dosyayı kaydetmesini sağlayan `-O / --remote-name` seçeneğini kullanmayı seçtik.

Bazen bu yeterli değildir. Birden fazla dosya indiriyorsunuz ve belki de bunları farklı bir alt dizine kaydetmek veya kaydedilen dosya adlarını farklı şekilde oluşturmak istiyorsunuz. curl'ün elbette bu durumlar için de bir çözümü var: çıktı dosya adı değişkenleri.

URL'de kullanılan her "glob" ayrı bir değişken alır. Bunlara `#[num]` olarak başvurulur - bu, tek karakter `#` ve ardından ilk glob için 1 ile başlayıp son glob ile biten glob numarası anlamına gelir.

İki farklı sitenin ana sayfalarını kaydedin:

    curl "http://{one,two}.example.com" -o "file_#1.txt"

Bir alt dizindeki iki glob ile bir komut satırından çıktıları kaydedin:

    curl "http://{site,host}.host[1-5].example.com" -o "subdir/#1_#2"

## URL'lerde `[]{}` kullanma

1990'larda curl'e globbing kavramı eklendiğinde, hepimiz URL sözdiziminin nasıl tanımlandığına dair aynı İnternet standardını kullanıyorduk ve bu standartta bu dört sembol *ayrılmış* (reserved) olarak belgelenmişti. Bunları kullanmak istiyorsanız URL'de URL kodlamanız gerekiyordu (`%HH` stili). Bu semboller bu nedenle URL'lerde kullanılmadı ve globbing amaçları için kullanılması düpedüz çekiciydi.

Daha sonra, URL sözdizimi yavaş yavaş gevşetildi ve değiştirildi ve bugünlerde arada sırada dört sembolden `[]{}` birinin URL kodlaması olmadan olduğu gibi kullanıldığı URL'lerin kullanıldığını görüyoruz. Böyle bir URL'yi curl'e iletmek, glob ayrıştırıcısı çıldırdığında sözdizimi hataları kusmasına neden olur.

Bu sorunu aşmak için iki ayrı seçeneğiniz vardır. Sembolleri kendiniz kodlarsınız ya da globbing'i kapatırsınız.

Sembolleri şu şekilde kodlayın:

|sembol | kodlama|
|-------|---------|
| `[`   | `%5b`   |
| `]`   | `%5d`   |
| `{`   | `%7b`   |
| `}`   | `%7d`   |

Veya `-g` veya `--globoff` ile globbing'i kapatın.
