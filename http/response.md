# Yanıtlar (Responses)

Bir HTTP istemcisi bir sunucuyla HTTP konuştuğunda, sunucu bir HTTP yanıt mesajıyla yanıt verir veya curl bunu bir hata olarak kabul eder ve `Empty reply from server` (Sunucudan boş yanıt) hata mesajıyla 52 döndürür.

## Bir HTTP yanıtının boyutu

Bir HTTP yanıtının belirli bir boyutu vardır ve curl'ün bunu bulması gerekir. Bir HTTP yanıtının sonunu işaret etmenin birkaç farklı yolu vardır ancak en temel yol yanıttaki `Content-Length:` başlığını kullanmak ve bununla yanıt gövdesindeki tam bayt sayısını belirtmektir.

Bazı eski HTTP sunucusu uygulamalarının 2 GB'den büyük dosya boyutlarıyla ilgili sorunları vardı ve Content-Length: başlıklarını negatif boyutlarla veya tamamen yanlış verilerle göndermeyi başardılar. curl'e `--ignore-content-length` ile Content-Length: başlığını tamamen görmezden gelmesi söylenebilir. Bunu yapmak başka olumsuz yan etkilere neden olabilir ancak en azından verileri almanızı sağlamalıdır.

## HTTP yanıt kodları

Bir HTTP transferi, ilk yanıt satırında 3 basamaklı bir yanıt kodu alır. Yanıt kodu, sunucunun isteğin nasıl işlendiği hakkında istemciye bir ipucu verme şeklidir.

İstenen belgenin teslim edilemediğini (veya benzeri bir şeyi) yanıt kodu gösterse bile curl'ün bunu bir hata olarak kabul etmediğini not etmek önemlidir. curl, HTTP'nin başarılı bir şekilde gönderilmesini ve alınmasını iyi olarak kabul eder.

HTTP yanıt kodunun ilk basamağı bir tür hata sınıfıdır:

 - 1xx: geçici yanıt, daha fazlası geliyor
 - 2xx: başarı
 - 3xx: bir yönlendirme
 - 4xx: istemci sunucunun teslim edemeyeceği veya etmeyeceği bir şey istedi
 - 5xx: sunucuda bir sorun var

Yanıt kodunu çıkarmak için curl'ün `--write-out` seçeneğini kullanabileceğinizi unutmayın. [--write-out](../usingcurl/verbose/writeout.md) bölümüne bakın.

curl'ün yanıt kodları >= 400 için bir hata döndürmesini sağlamak üzere `--fail` veya `--fail-with-body` kullanmanız gerekir. O zaman curl bu tür durumlar için hata kodu 22 ile çıkar.

## CONNECT yanıt kodları

Aynı curl transferinde bir HTTP isteği ve ayrı bir CONNECT isteği olabileceğinden, genellikle CONNECT yanıtını (vekil sunucudan gelen) uzak sunucunun HTTP yanıtından ayırırız.

CONNECT de bir HTTP isteğidir, bu nedenle aynı sayısal aralıkta yanıt kodları alır ve bu kodu da çıkarmak için `--write-out` kullanabilirsiniz.

## Parçalı (Chunked) aktarım kodlaması

Bir HTTP 1.1 sunucusu, parçalı kodlanmış bir yanıtla (chunked encoded response) yanıt vermeye karar verebilir; bu, HTTP 1.0'da bulunmayan bir özelliktir.

Parçalı bir yanıt alırken, yanıtın boyutunu belirtmek için bir Content-Length: yoktur. Bunun yerine, curl'e parçalı verilerin geldiğini söyleyen bir `Transfer-Encoding: chunked` başlığı vardır ve ardından yanıt gövdesinde veriler bir dizi parça halinde gelir. Her bir parça, o belirli parçanın boyutuyla (onaltılık olarak) başlar, ardından yeni bir satır ve ardından parçanın içeriği gelir. Bu, yanıtın sonuna kadar tekrar tekrar devam eder ve yanıtın sonu sıfır boyutlu bir parçayla işaretlenir. Bu yanıt kodlamasının amacı, sunucu göndermeye başlamadan önce tam boyutu bilmese bile istemcinin yanıtın ne zaman bittiğini anlayabilmesidir. Bu genellikle yanıtın dinamik olduğu ve istek geldiği anda oluşturulduğu durumlarda geçerlidir.

curl gibi istemciler parçaların kodunu çözer ve kullanıcılara parça boyutlarını göstermez.

## Gzip ile sıkıştırılmış transferler

HTTP üzerinden yanıtlar sıkıştırılmış formatta gönderilebilir. Bu en yaygın olarak sunucu tarafından yanıtta istemciye bir ipucu olarak `Content-Encoding: gzip` içerildiğinde yapılır. Sıkıştırılmış yanıtlar, statik kaynaklar gönderildiğinde (daha önce sıkıştırılmış olan) veya hatta bant genişliğinden daha fazla CPU gücünün mevcut olduğu çalışma zamanında çok mantıklıdır. Çok daha küçük bir veri miktarı göndermek genellikle tercih edilir.

curl'den, `--compressed` kullanarak hem sıkıştırılmış içerik istemesini *hem de* içerik kodlu gzip (veya aslında curl'ün anladığı diğer herhangi bir sıkıştırma algoritması) alırken gzipli verileri otomatik ve şeffaf bir şekilde açmasını isteyebilirsiniz:

    curl --compressed http://example.com/

## Aktarım kodlaması (Transfer encoding)

Aktarım kodlamasıyla kullanılan daha az yaygın bir özellik sıkıştırmadır.

Sıkıştırma başlı başına yaygındır. Zamanla HTTP için sıkıştırma yapmanın baskın ve web uyumlu yolu, yukarıdaki bölümde açıklandığı gibi `Content-Encoding` kullanmak olmuştur. HTTP başlangıçta şeffaf sıkıştırmanın bir aktarım kodlaması olarak yapılmasına izin vermek için tasarlanmış ve belirtilmişti ve curl bu özelliği destekler.

İstemci daha sonra sunucudan sıkıştırma aktarım kodlaması yapmasını ister ve kabul edilirse, bunu yaptığını belirten bir başlıkla yanıt verir ve ardından curl varışta verileri şeffaf bir şekilde açar. Bir curl kullanıcısı `--tr-encoding` ile sıkıştırılmış bir aktarım kodlaması ister:

    curl --tr-encoding http://example.com/

Doğadaki pek çok HTTP sunucusunun bunu desteklemediği not edilmelidir.

## Aktarım kodlamasını iletme (Pass on transfer encoding)

Bazı durumlarda curl'ü bir vekil sunucu veya başka bir ara yazılım olarak kullanmak isteyebilirsiniz. Bu durumlarda, curl'ün transfer-encoding başlıklarıyla ilgilenme ve ardından gerçek verileri şeffaf bir şekilde çözme yolu, son alıcı *aynı zamanda* aynısını yapmayı bekliyorsa istenmeyebilir.

O zaman curl'den alınan verileri çözmeden iletmesini isteyebilirsiniz. Bu, boyutları parçalı kodlama formatında veya sıkıştırılmış aktarım kodlaması kullanıldığında sıkıştırılmış formatta vb. iletmek anlamına gelir.

    curl --raw http://example.com/
