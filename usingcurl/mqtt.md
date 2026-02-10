# MQTT

Düz bir GET, konuya abone olur ve yayınlanan tüm mesajları yazdırır.
Bir POST yapmak, gönderi verilerini konuya yayınlar ve çıkar.

example.com tarafından yayınlanan `home/bedroom` konusundaki sıcaklığa abone olun:

    curl mqtt://example.com/home/bedroom/temp

example.com sunucusu tarafından barındırılan `home/bedroom/dimmer` konusuna `75` değerini gönderin:

    curl -d 75 mqtt://example.com/home/bedroom/dimmer

## curl bir aboneye yanıt olarak ne sunar

İki bayt konu uzunluğu (MSB | LSB), konu ve ardından yükü (payload) çıktılar.

## Uyarılar (Caveats)

Eylül 2022 itibarıyla curl'ün MQTT desteğinde kalan sınırlamalar:

 - Yayınlamak için yalnızca QoS seviyesi 0 uygulanmıştır
 - Yayınlamak için tutma (retain) bayrağını ayarlamanın bir yolu yoktur
 - TLS (mqtts) desteği yoktur
