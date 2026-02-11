# Değişkenler

Komut satırı ve yapılandırma dosyaları için değişkenler kavramı curl 8.3.0'da eklendi.

Bir kullanıcı, `--variable varName=content` ile düz bir dizeye veya dosya tek bir tire (`-`) olarak ayarlandıysa stdin olabilen bir dosyadan `--variable varName@file` ile içeriklere bir *değişken* ayarlar.

Bu bağlamda bir değişkene belirli bir ad verilir ve içerik tutar. İstenilen sayıda değişken ayarlanabilir. Aynı değişken adını tekrar ayarlarsanız, yeni içerikle üzerine yazılır. Değişken adları büyük/küçük harfe duyarlıdır, 128 karaktere kadar uzunlukta olabilir ve a-z, A-Z, 0-9 ve alt çizgi karakterlerinden oluşabilir.

Aşağıdaki bazı örnekler okunabilirlik için birden fazla satır içerir. Ters eğik çizgi (`\`), terminale yeni satırı görmezden gelmesi talimatını vermek için kullanılır.

## Değişkenleri ayarlama

Değişkenleri komut satırında `--variable` ile veya yapılandırma dosyalarında `variable` (tire olmadan) ile ayarlayabilirsiniz:

    curl --variable varName=content

veya bir yapılandırma dosyasında:

    # Curl yapılandırma dosyası

    variable varName=content

## Dosyadan içerik atama

Düz bir metin dosyasının içeriğini de bir değişkene atayabilirsiniz:

    curl --variable varName@filename

curl 8.12.0'dan başlayarak, değişken adının sonuna `[N-M]` ekleyerek içerikten bir bayt aralığı alabilirsiniz; burada `N` ve `M` içeriğe doğru sayısal bayt ofsetleridir ve ikinci sayı verinin sonuna kadar anlamına gelmek üzere atlanabilir. Örneğin, bir dosyadan 100 ile 199 arasındaki bayt ofsetinden (dahil) içerikleri alın:

    curl --variable "varName[100-199]@filename"

Alternatif olarak, düz bir metinden üç ile on iki arasındaki ofseti alın:

    curl --variable "varName[3-12]=rangealinacaktammetin"

Verisi olmayan bir bayt aralığı verildiğinde boş bir dize elde edilir. İçerikten daha büyük bir aralık istemek, curl'ün verinin mevcut olan parçasını kullanmasına neden olur.

## Genişletme (Expand)

Değişkenler, seçenek adı `--expand-` ile öneklendiğinde `{{varName}}` kullanılarak seçenek parametrelerinde genişletilebilir. Bu, `varName` değişkeninin içeriğinin eklenmesini sağlar.

Değişken olarak mevcut olmayan bir ada başvurursanız, boş bir dize eklenir.

Dizeye `{{` karakterini ters eğik çizgi ile kaçış yaparak olduğu gibi ekleyin:

`\{{`.

Aşağıdaki örnekte, `host` değişkeni ayarlanır ve ardından genişletilir:

    curl \
        --variable host=example \
        --expand-url "https://{{host}}.com"

`--expand-` öneki olmadan belirtilen seçenekler için değişkenler genişletilmez.

Genişletildiğinde kodlanmamış null baytları tutan değişken içeriği, curl'ün bir hatayla çıkmasına neden olur.

## Ortam değişkenleri

`--variable %VARNAME` ile bir ortam değişkenini içe aktarın. Bu içe aktarma, verilen ortam değişkeni ayarlanmamışsa curl'ün bir hatayla çıkmasına neden olur. Bir kullanıcı ayrıca, yukarıda açıklandığı gibi `=content` veya `@file` kullanarak ortam değişkeni mevcut değilse varsayılan bir değer ayarlamayı da seçebilir.

Örnek olarak, `%USER` ortam değişkenini bir curl değişkenine atayın ve bunu bir URL'ye ekleyin. Varsayılan bir değer belirtilmediğinden, ortam değişkeni mevcut değilse bu işlem başarısız olur:

    curl \
        --variable %USER \
        --expand-url "https://example.com/api/{{USER}}/method"

Bunun yerine, `%USER` mevcut değilse varsayılan değer olarak `dummy` kullanalım:

    curl \
        --variable %USER=dummy \
        --expand-url "https://example.com/api/{{USER}}/method"

Veya varsayılan içerikleri yerel bir dosyadan alın:

    curl \
        --variable %USER@file \
        --expand-url "https://example.com/api/{{USER}}/method"

## `--variable` genişletme

`--variable` seçeneğinin kendisi de genişletilebilir, bu da değişkenleri diğer değişkenlerin içeriğine atamanıza olanak tanır.

    curl \
        --expand-variable var1={{var2}} \
        --expand-variable fullname="Mrs {{first}} {{last}}" \
        --expand-variable source@{{filename}}

Veya bir yapılandırma dosyasında yapılır:

    # Curl yapılandırma dosyası

    variable host=example

    expand-variable url=https://{{host}}.com

    expand-variable source@{{filename}}

## İşlevler (Functions)

Değişkenleri genişletirken, curl bunların nasıl genişletileceğini değiştirmek için bir dizi *işlev* sunar. İşlevler, değişkenden sonra iki nokta üst üste + işlev adı ile uygulanır, şöyle: `{{varName:function}}`.

Değişkene birden fazla işlev uygulanabilir. Bunlar daha sonra soldan sağa sırayla uygulanır: `{{varName:func1:func2:func3}}`

Şu işlevler mevcuttur: `trim`, `json`, `url` ve `b64`

## İşlev: `trim`

Değişkeni baştaki ve sondaki boşluklar olmadan genişletir. Boşluk şu şekilde tanımlanır:

* yatay sekmeler (tabs)
* boşluklar
* yeni satırlar
* dikey sekmeler
* form besleme (form feed) ve satır başı (carriage returns)

Bu, dosyalardan veri okurken ekstra kullanışlıdır.

    --expand-url "https://example.com/{{path:trim}}"

## İşlev: `json`

Değişkeni geçerli bir JSON dizesi olarak genişletir. Bu, bir argümana geçerli JSON eklemeyi kolaylaştırır (Tırnak işaretleri ortaya çıkan JSON'a dahil edilmez).

    --expand-json "\"full name\": \"{{first:json}} {{last:json}}\""

Önce değişkeni kırpmak (trim) için, her iki işlevi de uygulayın (bu sırayla):

    --expand-json "\"full name\": \"{{varName:trim:json}}\""


## İşlev: `url`

Değişkeni URL kodlu olarak genişletir. *Yüzde kodlu* (percent encoded) olarak da bilinir. Bu işlev, tüm çıktı karakterlerinin bir URL içinde yasal olmasını ve geri kalanının, ascii değeri için iki basamaklı onaltılık bir sayı olan `HH` olduğu `%HH` olarak kodlanmasını sağlar.

    --expand-data "varName={{varName:url}}"

Önce değişkeni kırpmak için, her iki işlevi de uygulayın (bu sırayla):

    --expand-data "varName={{varName:trim:url}}"

## İşlev: `b64`

Değişkeni base64 kodlu olarak genişletir. Base64, ikili veriler için yalnızca 64 belirli karakteri kullanan bir kodlamadır.

    --expand-data "content={{value:b64}}"

Önce değişkeni kırpmak için, her iki işlevi de uygulayın (bu sırayla):

    --expand-data "content={{value:trim:b64}}"

Örnek: `$HOME/.secret` adlı bir dosyanın içeriğini `fix` adlı bir değişkene alın. İçeriğin kırpıldığından ve yüzde kodlu olarak POST verisi olarak gönderildiğinden emin olun:

    curl \
        --variable %HOME=/home/default \
        --expand-variable fix@{{HOME}}/.secret \
        --expand-data "{{fix:trim:url}}" \
        --url https://example.com/ \
