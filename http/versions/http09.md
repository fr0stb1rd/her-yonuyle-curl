# HTTP/0.9

HTTP/1.0 kullanıma sunulmadan önce kullanılan HTTP sürümü genellikle HTTP/0.9 olarak adlandırılır. O günlerde, HTTP yanıtlarının başlıkları yoktu çünkü yalnızca bir yanıt gövdesi döndürür ve ardından bağlantıyı hemen kapatırlardı.

curl'e bu tür yanıtları desteklemesi söylenebilir ancak varsayılan olarak güvenlik nedenleriyle bunları tanımaz. Kötü olan hemen hemen her şey curl'e bir HTTP/0.9 yanıtı gibi görünür, bu nedenle seçeneğin dikkatli kullanılması gerekir.

curl'e verilen HTTP/0.9 seçeneği, yukarıda belirtilen diğer HTTP komut satırı seçeneklerinden farklıdır; çünkü bu, hangi yanıtın kabul edileceğini kontrol ederken, diğerleri hangi HTTP protokol sürümünün kullanılmaya çalışılacağı ile ilgilidir.

curl'e bir HTTP/0.9 yanıtını kabul etmesini şöyle söyleyin:

    curl --http0.9 https://example.com/
