# Tarayıcılar

Tarayıcılar tipik olarak curl'ün kullandığından *farklı* bir URL standardını destekler ve kullanır. curl rehberlik için RFC 3986 kullanırken, tarayıcılar [WHATWG URL Spesifikasyonunu](https://url.spec.whatwg.org/) kullanır.

Bu önemlidir çünkü iki URL standardı aynı değildir. Çoğu günlük kullanımda bu farklılıklar nadiren ortaya çıksa da tamamen uyumlu değildirler. Bazen, spesifikasyonlardan birine göre yorumlanan bir URL, diğer spesifikasyon tarafından yorumlandığında farklı şekilde işlenir. Bu nedenle, curl ve tarayıcılar URL'lere her zaman aynı şekilde davranmaz.

WHATWG spesifikasyonu da zamanla *değişmektedir*.

curl bir tarayıcının yapabileceği aynı işlemleri yapabilmek için geliştirildiğinden, curl URL ayrıştırıcısı bazı farklılıklara hitap etmek için biraz ayarlanmıştır. Örneğin, gelen HTTP başlıklarından okunduğunda URL'deki boşlukları kabul eder ve şema ile ana bilgisayar adı arasında ayırıcı olarak bir, iki veya üç eğik çizgi kabul eder. Bu yüzden bazen curl'ün ayrıştırıcısının *RFC 3986+* uyumlu olduğunu söylüyoruz.

curl mevcut davranışı bozmamak için çok çabalar, bu da hala 1998'de desteklediği URL'leri ve URL formatını desteklemesini sağlar. Tarayıcılar bunu yapmaz.

## Tarayıcıların adres çubuğu

Modern bir web tarayıcısı kullandığınızda, ana pencerelerinin üst kısmında yer alan adres çubuğu URL'leri ve hatta URI'leri kullanmaz. Aslında çoğunlukla Latin olmayan semboller ve daha fazlası gibi uluslararasılaştırmaya izin vermek için URI'lerin bir üst kümesi olan IRI'leri kullanırlar, ancak genellikle bunun ötesine de geçerler; örneğin, boşlukları işlerler ve yüzde kodlamasında (percent encoding) belirtilen spesifikasyonların hiçbirinin bir istemcinin yapması gerektiğini söylemediği şekillerde sihirli şeyler yaparlar.

Adres çubuğu, insanların URI benzeri dizeleri girmesi ve görmesi için oldukça basit bir arayüzdür.

Bazen bir tarayıcının adres çubuğunda gördüğünüz ile curl'e iletebileceğiniz arasındaki farklar önemlidir.
