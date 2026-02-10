# Tarayıcı benzeri görevleri senaryolaştırma (Scripting browser-like tasks)

curl, favori tarayıcınızın yapabileceği hemen hemen her HTTP işlemini ve transferini yapabilir. Aslında bundan çok daha fazlasını da yapabilir, ancak bu bölümde curl'ü aksi takdirde bir tarayıcıyla manuel olarak yapmanız gerekenleri yeniden üretmek veya senaryolaştırmak için kullanabileceğiniz gerçeğine odaklanıyoruz.

İşte bunu yaparken nasıl ilerleyeceğiniz konusunda bazı püf noktaları ve tavsiyeler.

## Tarayıcının ne yaptığını anlayın

Bu gerçekten gerekli bir ilk adımdır. Ne yaptığını tahmin etmeye çalışmak, yanlış sorun bataklığında kaybolma riskini taşır. Bu soruna bilimsel yaklaşım, öncelikle tarayıcının ne yaptığını anlamanızı gerektirir.

Tarayıcının belirli bir görevi yerine getirmek için ne yaptığını öğrenmek için, üzerinde çalıştığınız HTML sayfalarını okuyabilirsiniz ve yeterince derin bir bilgiyle, bir tarayıcının bunu başarmak için ne yapacağını görebilir ve ardından aynısını curl ile yapmaya çalışabilirsiniz.

Sayfanın gizlenmiş JavaScript ile dolu olduğu durumlarda bile çalışan biraz daha etkili yol, tarayıcıyı çalıştırmak ve hangi HTTP işlemlerini gerçekleştirdiğini izlemektir.

[Curl olarak kopyala](../cmdline/copyas.md) bölümü, bir tarayıcının isteğini nasıl kaydedebileceğinizi ve bunu kolayca bir curl komut satırına nasıl dönüştürebileceğinizi açıklar.

Kopyalanan curl komut satırları genellikle *tam olarak* o isteği kopyalama eğiliminde olduklarından yeterince iyi değildir; oysa muhtemelen aynı işlemi yeniden üretebilmek ve sadece kelimesi kelimesine isteği yeniden göndermemek için biraz daha dinamik olmak istersiniz.

## Çerezler (Cookies)

Bugün web'in çoğu bir yerlerde bir kullanıcı adı ve şifre giriş istemiyle çalışır. Çoğu durumda, bir süre önce tarayıcınızla giriş yapmışsınızdır ancak o durumu korumuş ve sizi giriş yapmış durumda tutmuştur.

Giriş yapmış durumu neredeyse her zaman [çerezler](cookies/) kullanılarak yapılır. Yaygın bir işlem, önce giriş yapmak ve dönen çerezleri bir dosyaya kaydetmek ve ardından siteyi curl ile dolaşırken sitenin sonraki komut satırlarında çerezleri güncellemesine izin vermektir.

## Web girişleri ve oturumları

https://example.com/ sitesi bir giriş istemi içerir. Web sitesindeki giriş, bir [HTTP POST](post/) gönderdiğiniz bir HTML formudur. Yanıt çerezlerini ve yanıt (HTML) çıktısını kaydedin.

Giriş sayfası (bir tarayıcı kullansaydınız) https://example.com/ üzerinde görünür olsa da, o sayfadaki HTML form etiketi `action` parametresini kullanarak POST'u tam olarak hangi URL'ye göndereceğiniz konusunda sizi bilgilendirir.

Hayali durumumuzda, form etiketi şöyle görünür:

    <form action="login.cgi" method="POST">
      <input type="text" name="user">
      <input type="password" name="secret">
      <input type="hidden" name="id" value="bc76">
    </form>

Önemli üç alan vardır. **user**, **secret** ve **id**. Sonuncusu, id, `hidden` (gizli) olarak işaretlenmiştir; bu, tarayıcıda görünmediği ve bir kullanıcının doldurduğu bir alan olmadığı anlamına gelir. Site tarafından oluşturulur ve curl girişinizin başarılı olması için o değeri çıkarmanız ve verilerin geri kalanıyla birlikte POST gönderiminizde kullanmanız gerekir.

Doğru içerikleri alanlara ve doğru hedef URL'ye gönderin:

    curl -d user=daniel -d secret=qwerty -d id=bc76 \
      https://example.com/login.cgi -o out

Birçok giriş sayfası, girişi sunarken size zaten bir oturum çerezi gönderir ve zaten genellikle `<form>` etiketinden gizli alanları çıkarmanız gerektiğinden, önce şuna benzer bir şey yapabilirsiniz:

    curl -c cookies https://example.com/ -o loginform

Genellikle oradan id alanını çıkarmak için bir HTML ayrıştırıcısına veya bir betik diline ihtiyacınız olur ve ardından yukarıda belirtildiği gibi ancak eklenen çerez yüklemesi ile devam edip giriş yapabilirsiniz (daha okunabilir hale getirmek için satırı iki satıra bölüyorum):

    curl -d user=daniel -d secret=qwerty -d id=bc76 \
      https://example.com/login.cgi -b cookies -c cookies -o out

Hem dosyadan çerez okumak için `-b`'yi hem de çerezleri tekrar saklamak için (sunucu güncellenmiş çerezler geri gönderdiğinde) `-c`'yi kullandığını görebilirsiniz.

Ayrıntıları çözerken komut satırlarına her zaman, *her zaman* `-v` ekleyin. Bununla ilgili daha fazla ayrıntı için [ayrıntılı](../usingcurl/verbose/) bölümüne de bakın.

## Yönlendirmeler (Redirects)

Sunucuların bir giriş POST'una yanıt verirken [yönlendirmeler](redirects.md) kullanması yaygındır. O kadar yaygındır ki, muhtemelen bir yönlendirme ile çözülmediği durumların nadir olduğunu söyleyebilirim.

O zaman sadece curl'ün yönlendirmeleri otomatik olarak takip etmediğini hatırlamanız gerekir. `-L` komut satırı seçeneğini ekleyerek ona bunu yapmasını söylemelisiniz. Bunu önceki komut satırına eklemek, tam halini şöyle yapar:

    curl -d user=daniel -d secret=qwerty -d id=bc76 \
      https://example.com/login.cgi -b cookies -c cookies -L -o out

## Giriş sonrası (Post-login)

Yukarıdaki örnek komut satırlarında, giriş yanıtı çıktısını 'out' adlı bir dosyaya kaydediyoruz ve betiğinizde muhtemelen girişin başarılı olduğunu onaylayan bir metin veya bir şey içerdiğini doğrulamalısınız.

Başarıyla giriş yaptıktan sonra, ihtiyacınız olan dosyaları alın veya HTTP işlemlerini gerçekleştirin ve çerezleri kullanmak ve güncellemek için komut satırlarında hem `-b` hem de `-c` kullanmaya devam etmeyi unutmayın.

## Referer

Bazı siteler, bir şey istediğinizde veya giriş yaptığınızda veya benzeri durumlarda `Referer:`'ın gerçekten meşru ana URL'yi tanımladığını doğrular. O zaman `-e https://example.com/` vb. kullanarak sunucuya hangi URL'den geldiğinizi bildirebilirsiniz. Bunu önceki giriş denemesine eklemek şöyle olur:

    curl -d user=daniel -d secret=qwerty -d id=bc76 \
      https://example.com/login.cgi \
      -b cookies -c cookies -L -e "https://example.com/" -o out

## TLS parmak izi (TLS fingerprinting)

Günümüzde bot karşıtı tespitler, bir isteğin bir tarayıcıdan gelip gelmediğini anlamak için TLS parmak izini kullanır. Curl'ün parmak izi ortamınıza bağlı olarak değişebilir ve büyük olasılıkla tarayıcılarınkinden farklıdır. Curl'ün CLI'sı parmak izinin tüm çeşitli parçalarını değiştirmek için seçeneklere sahip değildir, ancak ileri düzey bir kullanıcı libcurl kullanarak ve curl'ü kaynaktan kendisi derleyerek parmak izini özelleştirebilir.
