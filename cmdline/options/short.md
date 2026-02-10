# Kısa seçenekler

Komut satırı seçenekleri, curl'e nasıl davranmasını istediğiniz hakkında bilgi aktarır. Örneğin, -v seçeneğiyle curl'den ayrıntılı (verbose) modunu açmasını isteyebilirsiniz:

    curl -v http://example.com

-v burada bir "kısa seçenek" olarak kullanılır. Bunları eksi sembolü ve hemen ardından gelen tek bir harfle yazarsınız. Birçok seçenek, bir şeyi açan veya iki bilinen durum arasında bir şeyi değiştiren anahtarlardır. Sadece o seçenek adıyla kullanılabilirler. Ayrıca eksiden sonra birkaç tek harfli seçeneği birleştirebilirsiniz. Hem ayrıntılı mod hem de curl'ün HTTP yönlendirmelerini takip etmesini istemek için:

    curl -vL http://example.com

curl'deki komut satırı ayrıştırıcısı her zaman tüm satırı ayrıştırır ve seçenekleri istediğiniz yere koyabilirsiniz; URL'den sonra da görünebilirler:

    curl http://example.com -Lv

ve iki ayrı kısa seçenek elbette ayrı ayrı da belirtilebilir, şöyle:

    curl -v -L http://example.com
