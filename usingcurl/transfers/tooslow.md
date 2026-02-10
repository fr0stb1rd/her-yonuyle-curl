# Yavaş transferleri durdurma

Bir curl işlemi için sabit bir maksimum süreye sahip olmak zahmetli olabilir, özellikle de örneğin komut dosyasıyla transferler yapıyorsanız ve dosya boyutları ile transfer süreleri çok değişiyorsa. Sabit bir zaman aşımı değerinin, en kötü durumları kapsayacak şekilde gereksiz yere yüksek ayarlanması gerekir.

Sabit bir zaman aşımına alternatif olarak, curl'e transfer belirli bir hızın altına düşerse ve belirli bir süre boyunca bu eşiğin altında kalırsa transferi terk etmesini söyleyebilirsiniz.

Örneğin, bir transfer hızı 15 saniye boyunca saniyede 1000 baytın altına düşerse durdurun:

    curl --speed-time 15 --speed-limit 1000 https://example.com/
