# Yardım

curl'ün iki yüz altmıştan fazla komut satırı seçeneği vardır ve seçeneklerin sayısı zamanla artmaya devam etmektedir. Seçenek sayısının önümüzdeki yıllarda üç yüze ulaşması ve hatta aşması muhtemeldir.

## Seçenekleri listeleme

Belirli bir eylemi gerçekleştirmek için hangi seçeneklere ihtiyacınız olduğunu bulmak için, curl'ün bunları listelemesini sağlayabilirsiniz. İlk olarak, `curl --help` veya basitçe `curl -h`, size en önemli ve sık kullanılan seçeneklerin bir listesini verir. O belirli alan için daha fazla seçeneğin listelenmesini sağlamak üzere `-h`'ye ek bir "kategori" sağlayabilirsiniz. Mevcut tüm kategorileri listelemek için `curl -h category` veya *tüm* mevcut seçenekleri listelemek için `curl -h all` kullanın.

## Belirli bir seçenekle ilgili yardım

curl'ün tek bir belirli komut satırı seçeneği hakkındaki belgeleri görüntülemesini sağlamak için, seçeneği `-h`'den sonra ekleyin. Tek tire (`-`) ile kısa adı veya iki tire (`--`) ile uzun sürümü kullanın.

Örneğin, `-U`'nun ne yaptığını şunu çalıştırarak öğrenin:

    curl -h -U

Veya `--insecure` açıklamasını şu şekilde alın:

    curl -h --insecure

## Tam kılavuz (manual)

`curl --manual` seçeneği, curl için tüm man sayfasını (kılavuz sayfası) çıktılar. Bu, her seçeneğin nasıl çalıştığına dair birkaç bin satırlık dokümantasyonu bir araya getiren kapsamlı ve eksiksiz bir belgedir. Bunların içinden geçmek de sıkıcı bir iştir ve bu metin yığınları arasında bir arama işlevinin kullanılmasını teşvik ediyoruz. Bazı insanlar man sayfasının [web sürümünü](https://curl.se/docs/manpage.html) de takdir edebilir.
