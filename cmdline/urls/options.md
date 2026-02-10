# Birçok seçenek ve URL

Yukarıda belirtildiği gibi, curl yüzlerce komut satırı seçeneğini destekler ve aynı zamanda sınırsız sayıda URL'yi de destekler. Kabuğunuz veya komut satırı sisteminiz destekliyorsa, curl'e iletebileceğiniz komut satırının uzunluğunun gerçekten bir sınırı yoktur.

curl önce tüm komut satırını ayrıştırır, kullanılan komut satırı seçeneklerinden gelen istekleri uygular ve ardından işlemleri gerçekleştirmek için URL'lerin üzerinden tek tek (soldan sağa sırayla) geçer.

Bazı seçenekler için (örneğin curl'e transferi nerede saklayacağını söyleyen `-o` veya `-O`), komut satırındaki her URL için bir seçenek belirtmek isteyebilirsiniz.

curl, kullanılan son URL üzerindeki işlemi için bir çıkış kodu döndürür. Bunun yerine curl'ün kümedeki başarısız olan ilk URL'de bir hatayla çıkmasını istiyorsanız, `--fail-early` seçeneğini kullanın.

## Verilen her URL için bir çıktı

İki URL içeren bir komut satırı kullanıyorsanız, curl'e her ikisini de nasıl işleyeceğini söylemelisiniz. `-o` ve `-O` seçenekleri, curl'e çıktıyı URL'lerden *biri* için nasıl kaydedeceğini söyler, bu nedenle komut satırında URL'leriniz olduğu kadar bu seçeneklere sahip olmak isteyebilirsiniz.

Komut satırında çıktı seçeneklerinden daha fazla URL'niz varsa, karşılık gelen bir çıktı talimatı olmayan URL içeriği bunun yerine stdout'a (standart çıktı) gönderilir.

`--remote-name-all` bayrağını kullanmak, curl'ün otomatik olarak herhangi bir çıktı seçeneğine sahip olmayan tüm verilen URL'ler için `-O` kullanılmış gibi davranmasını sağlar.

## URL başına ayrı seçenekler

Önceki bölümlerde curl'ün her zaman tüm komut satırındaki tüm seçenekleri nasıl ayrıştırdığını ve bunları transfer ettiği tüm URL'lere nasıl uyguladığını anlattık.

Bu bir basitleştirmeydi: curl ayrıca, seçenekleri uyguladığı bir dizi seçenek ve URL arasına bir sınır ekleyen bir seçenek (`-:`, `--next`) sunar. Komut satırı ayrıştırıcısı bir `--next` seçeneği bulduğunda, aşağıdaki seçenekleri bir sonraki URL setine uygular. `--next` seçeneği böylece bir dizi seçenek ve URL arasında bir *ayırıcı* olarak çalışır. İstediğiniz kadar `--next` seçeneği kullanabilirsiniz.

Örnek olarak, bir URL'ye HTTP GET yapıyoruz ve yönlendirmeleri izliyoruz, sonra farklı bir URL'ye ikinci bir HTTP POST yapıyoruz ve bunu üçüncü bir URL'ye bir HEAD isteği ile tamamlıyoruz. Hepsi tek bir komut satırında:

    curl --location http://example.com/1 --next
      --data sendthis http://example.com/2 --next
      --head http://example.com/3

Komut satırında `--next` seçenekleri _olmadan_ böyle bir şey denemek, curl hem POST hem de HEAD'i birleştirmeye çalışacağı için geçersiz bir komut satırı oluşturacaktır:

    Warning: You can only select one HTTP request method! You asked for both
    Warning: POST (-d, --data) and HEAD (-I, --head).
