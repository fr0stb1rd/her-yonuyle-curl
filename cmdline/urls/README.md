# URL'ler

curl'e curl denir çünkü adının içinde URL (Uniform Resource Locator - Tekdüzen Kaynak Bulucu) alt dizesi geçer. URL'ler üzerinde çalışır. URL, `HTTP://` ile öneklenmiş veya www ile başlayanlar gibi web adresi dizeleri için gündelik olarak kullandığımız addır.

URL, tam konuşmak gerekirse, bunların eski adıdır. URI (Uniform Resource Identifier - Tekdüzen Kaynak Tanımlayıcı), bunlar için daha modern ve doğru addır. Sözdizimi [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt)'da tanımlanmıştır.

curl'ün girdi olarak bir "URL" kabul ettiği yerde, bu aslında bir "URI"dir. curl'ün anladığı protokollerin çoğu, o belirli URI formatının nasıl çalıştığını açıklayan karşılık gelen bir URI sözdizimi belgesine de sahiptir.

* [Şema (Scheme)](scheme.md)
* [İsim ve parola](auth.md)
* [Ana bilgisayar (Host)](host.md)
* [Port numarası](port.md)
* [Yol (Path)](path.md)
* [Sorgu (Query)](query.md)
* [FTP türü](ftptype.md)
* [Bölüm (Fragment)](fragment.md)
* [Tarayıcılar](browsers.md)
* [Birçok seçenek ve URL](options.md)
* [URL globbing](globbing.md)
* [Bağlantı yeniden kullanımı](connreuse.md)
* [Paralel transferler](parallel.md)
* [trurl](trurl.md)
