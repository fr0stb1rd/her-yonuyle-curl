# Yapılandırma dosyası (Config file)

Birden fazla komut satırı seçeneğine sahip curl komutlarıyla çalışmak külfetli olabilir. Karakter sayısı, terminal uygulamanızın izin verdiği maksimum uzunluğu bile aşabilir.

Bu tür durumlara yardımcı olmak için, curl komut satırı seçeneklerini düz bir metin yapılandırma dosyasına yazmanıza ve curl'e uygun olduğunda o dosyadan seçenekleri okumasını söylemenize izin verir.

Ayrıca verileri değişkenlere atamak ve verileri işlevlerle dönüştürmek için yapılandırma dosyalarını kullanabilirsiniz, bu da onları inanılmaz derecede kullanışlı hale getirir. Bu, [Değişkenler](variables.md) bölümünde tartışılmaktadır.

Aşağıdaki bazı örnekler okunabilirlik için birden fazla satır içerir. Ters eğik çizgi (`\`), terminale yeni satırı görmezden gelmesi talimatını vermek için kullanılır.

## Kullanılacak yapılandırma dosyasını belirtme

`-K` veya uzun form `--config` seçeneğini kullanmak, curl'e bir yapılandırma dosyasından okumasını söyler.

    curl  \
        --config configFile.txt \
        --url https://example.com

Belirtilen dosya yolu, terminalinizdeki geçerli dizine göredir.

Yapılandırma dosyasını istediğiniz gibi adlandırabilirsiniz. Yukarıdaki örnekte basitlik için `configFile.txt` kullanılmıştır.

## Sözdizimi

Satır başına bir komut girin. Yorumlar için kare sembolünü kullanın:

    # curl yapılandırma dosyası

    # Yönlendirmeleri izle
    --location

    # Bir HEAD isteği yap
    --head

## Komut satırı seçenekleri

Hem kısa hem de uzun seçenekleri, bir komut satırına yazdığınız gibi tam olarak kullanabilirsiniz.

Daha kolay okunması için uzun seçeneği baştaki iki tire OLMADAN da yazabilirsiniz.

    # curl yapılandırma dosyası

    # Yönlendirmeleri izle
    location

    # Bir HEAD isteği yap
    head

## Argümanlar

Bir argüman alan bir komut satırı seçeneğinin argümanı, seçenekle AYNI SATIRDA sağlanmalıdır.

    # curl yapılandırma dosyası

    user-agent "Everything-is-an-agent"

Seçenek ve argümanı arasında `=` veya `:` de kullanabilirsiniz. Yukarıda gördüğünüz gibi, gerekli değildir, ancak bazıları sunduğu netliği sever. user-agent seçeneğini tekrar ayarlamak:

    # curl yapılandırma dosyası

    user-agent = "Everything-is-an-agent"

Yukarıda kullandığımız kullanıcı aracısı dizesinde boşluk yoktur, bu nedenle tırnak işaretlerine teknik olarak gerek yoktur:

    # curl yapılandırma dosyası

    user-agent = Everything-is-an-agent

Tırnak işaretlerinin ne zaman kullanılması gerektiği hakkında daha fazla bilgi için aşağıdaki "Tırnak işaretleri ne zaman kullanılır" bölümüne bakın.

## URL'ler

Komut satırında URL girerken, seçenek olmayan her şey bir URL olarak varsayılır. Ancak, bir yapılandırma dosyasında, bir URL'yi `--url` veya `url` ile belirtmeniz gerekir.

    # curl yapılandırma dosyası

    url = https://example.com

## Tırnak işaretleri ne zaman kullanılır

Şu durumlarda çift tırnak kullanmanız gerekir:

* parametre boşluk içeriyorsa veya `:` veya `=` karakterleriyle başlıyorsa.
* kaçış dizilerini kullanmanız gerekiyorsa (mevcut seçenekler: `\\`, `\"`, `\t`, `\n`, `\r` ve `\v`. Başka herhangi bir harften önce gelen ters eğik çizgi yoksayılır).

Boşluk içeren bir parametre çift tırnak içine alınmazsa, curl bir sonraki boşluğu veya yeni satırı argümanın sonu olarak kabul eder.

## Varsayılan yapılandırma dosyası

curl çağrıldığında, her zaman ( `-q` kullanılmadıkça), varsayılan bir yapılandırma dosyasını kontrol eder ve bulunursa onu kullanır.

Curl, varsayılan yapılandırma dosyasını şu konumlarda, bu sırayla arar:

1) `$CURL_HOME/.curlrc`

2) `$XDG_CONFIG_HOME/.curlrc` (7.73.0 sürümünde eklendi)

3) `$HOME/.curlrc`

4) Windows: `%USERPROFILE%\\.curlrc`

5) Windows: `%APPDATA%\\.curlrc`

6) Windows: `%USERPROFILE%\\Application Data\\.curlrc`

7) Windows dışı: ev dizinini (home directory) bulmak için getpwuid kullanın

8) Windows'ta, yukarıda açıklanan sırada `.curlrc` dosyası bulamazsa, curl yürütülebilir dosyasının yerleştirildiği aynı dizinde bir tane kontrol eder.

Windows'ta konum başına iki dosya adı kontrol edilir: `.curlrc` ve `_curlrc`, öncelik ilkine verilir. Windows'taki eski curl sürümleri yalnızca `_curlrc`'yi kontrol ediyordu.
