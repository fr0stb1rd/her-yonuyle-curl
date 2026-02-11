# Her Yönüyle curl

*Her Yönüyle curl*, curl ile ilgili her şey için kapsamlı bir rehberdir. Projenin kendisi, komut satırı aracı, kütüphane, her şeyin nasıl başladığı ve bugünkü yararlı araç haline nasıl geldiği anlatılmaktadır. Onu daha da geliştirmek için nasıl çalıştığımızı, kullanmak için nelerin gerektiğini, kod veya hata raporlarıyla nasıl katkıda bulunabileceğinizi ve milyonlarca mevcut kullanıcının onu neden kullandığını açıklar.

Kısacası: her yönüyle curl.

Bu kitap, hem sıradan okuyucular hem de biraz daha deneyimli geliştiriciler için ilginç ve yararlı olmayı amaçlamaktadır. Herkesin içinden seçip alabileceği bir şeyler sunar.

Bu kitabı baştan sona okumayın. Merak ettiğiniz bölümleri veya içerikleri okuyun ve uygun gördüğünüz şekilde ileri geri göz atın.

Bu kitap kendi başına bir açık kaynak projesidir: açık, indirmesi ve okuması tamamen ücretsizdir. Herkesin yorum yapmasına açıktır ve herkesin katkıda bulunması ve yardım etmesi için uygundur. Hata raporlarınızı, fikirlerinizi, "pull request"lerinizi (çekme isteklerinizi) veya eleştirilerinizi bize gönderin; ben veya bir başkası kitabı buna göre geliştirmek için çalışacaktır.

Bu kitap asla bitmeyecek. Üzerinde çalışmaya devam etmeye niyetliyim. Bir noktada, projenin çoğu yönünü kapsayan (bu aşılmaz bir hedef gibi görünse de) oldukça eksiksiz olduğunu düşünsem bile, curl projesi ilerlemeye devam edecek, bu yüzden kitapta da her zaman güncellenecek şeyler olacaktır.

Bu kitap projesi Eylül 2015'in sonunda başladı.

## Site

[https://everything.curl.dev](https://everything.curl.dev) bu kitabın ingilizce orijinal sayfasıdır. Kitabın ingilizce web sürümünü içerir. Türkçe web sürümüne [https://fr0stb1rd.github.io/her-yonuyle-curl](https://fr0stb1rd.github.io/her-yonuyle-curl) adresinden ulaşılabilir.

Bu kitap ayrıca ingilizce olarak [PDF](https://daniel.haxx.se/everything-curl/everything-curl.pdf) ve [ePUB](https://daniel.haxx.se/everything-curl/everything-curl.epub) biçimlerinde de sunulmaktadır. Türkçe sürümleri ise [Releases](https://github.com/fr0stb1rd/her-yonuyle-curl/releases/latest) sayfasında **PDF**, **EPUB** ve **HTML/mdbook** paketleri (ZIP) olarak sunulmaktadır.

İngilizce web sitesi Fastly tarafından barındırılmaktadır. Türkçe web sitesi GitHub Pages tarafından barındırılmaktadır. Kitap içeriği 18 Mart 2024'ten beri [mdBook](https://github.com/rust-lang/mdBook) tarafından oluşturulmaktadır.

## İçerik

Tüm kitap içeriği GitHub'da [https://github.com/curl/everything-curl](https://github.com/curl/everything-curl) deposunda barındırılmaktadır. Türkçe içeriği ise [https://github.com/fr0stb1rd/her-yonuyle-curl](https://github.com/fr0stb1rd/her-yonuyle-curl) deposunda barındırılmaktadır.

## Yazar

Bu materyalin sadece ortak yazarı olma umuduyla, ben Daniel Stenberg. curl projesini kurdum ve özünde bir geliştiriciyim; eğlence ve kazanç için. Stokholm, İsveç'te yaşıyorum ve çalışıyorum.

Daniel hakkında bilinmesi gereken her şey [daniel.haxx.se](https://daniel.haxx.se/) adresinde bulunabilir.

## Katkıda Bulunun

Bu belgede hatalar, eksiklikler, yanlışlar veya bariz yalanlar bulursanız, lütfen etkilenen paragrafın yenilenmiş bir sürümünü bize gönderin, biz de düzeltip güncelleyelim. Yardımcı olan herkesi takdir ediyor ve tanıyoruz.

Tercihen, orijinal kitabın GitHub sayfasında [hatalar (errors)](https://github.com/curl/everything-curl/issues) veya [pull request'ler](https://github.com/curl/everything-curl/pulls) gönderebilirsiniz.

## Çeviri

Bu kitabın Türkçe çevirisi (ve kapak fotoğrafının Türkçe tasarımı) [fr0stb1rd](https://fr0stb1rd.gitlab.io/) tarafından orijinaline sadık kalınarak yapılmıştır. Çeviri ile ilgili hataları bildirmek veya katkıda bulunmak (PR göndermek) için [her-yonuyle-curl](https://github.com/fr0stb1rd/her-yonuyle-curl) deposunu kullanabilirsiniz.

## Katkıda Bulunanlar

Birçok insan hata bildirdi, bölümleri geliştirdi veya bu kitabın bugünkü başarısına ulaşmasına yardımcı oldu. Bu arkadaşlar şunları içerir:

AaronChen0 on github,
alawvt on github,
Amin Khoshnood,
amnkh on github,
Anders Roxell,
Angad Gill,
Aris (Karim) Merchant,
auktis on github,
Ben Bodenmiller
Ben Peachey,
bookofportals on github,
Bruno Baguette,
Carlton Gibson,
Chris DeLuca,
Citizen Esosa,
Dan Fandrich,
Daniel Brown,
Daniel Sabsay,
David Piano,
DrDoom74 at GitHub,
Emil Hessman,
enachos71 on github,
ethomag on github,
Fabian Keil,
faterer on github,
Frank Dana,
Frank Hassanabad,
fr0stb1rd on github,
Gautham B A,
Geir Hauge,
Harry Wright,
Helena Udd,
Hubert Lin,
i-ky on github,
infinnovation-dev on GitHub,
Jay Ottinger,
Jay Satiro,
Jeroen Ooms,
Johan Wigert,
John Simpson,
JohnCoconut on github,
Jonas Forsberg,
Josh Vanderhook,
JoyIfBam5,
KJM on github,
knorr3 on github,
lowttl on github,
Luca Niccoli,
Manuel on github,
Marius Žilėnas,
Mark Koester,
Martin van den Nieuwelaar,
mehandes on github,
Michael Kaufmann,
Ms2ger,
Mohammadreza Hendiani,
Nick Travers,
Nicolas Brassard,
Oscar on github,
Oskar Köök,
Patrik Lundin,
RekGRpth on github,
Ryan McQuen,
Saravanan Musuwathi Kesavan,
Senthil Kumaran,
Shusen Liu,
Sonia Hamilton,
Spiros Georgaras,
Stephen,
Steve Holme,
Stian Hvatum,
strupo on github,
Viktor Szakats,
Vitaliy T,
Wayne Lai,
Wieland Hoffmann,
谭九鼎

## Lisans

Bu belge [Creative Commons Atıf 4.0 Uluslararası lisansı](https://creativecommons.org/licenses/by/4.0/) altında lisanslanmıştır.
