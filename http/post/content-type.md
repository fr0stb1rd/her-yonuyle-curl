# Content-Type

curl'ün `-d` seçeneğiyle POST yapmak, `Content-Type: application/x-www-form-urlencoded` gibi görünen varsayılan bir başlık içermesini sağlar. Tipik tarayıcınızın düz bir POST için kullandığı şey budur.

POST verilerinin birçok alıcısı Content-Type başlığını önemsemez veya kontrol etmez.

Eğer bu başlık sizin için yeterince iyi değilse, elbette bunu değiştirmeli ve yerine doğrusunu sağlamalısınız. Örneğin, bir sunucuya JSON gönderiyorsanız ve içeriğin ne olduğu hakkında sunucuya daha doğru bilgi vermek istiyorsanız:

    curl -d '{json}' -H 'Content-Type: application/json' https://example.com
