# Vekil sunucu başlıkları

Uzak sunucu için değil, özellikle bir HTTP veya HTTPS vekil sunucusu için tasarlanmış HTTP başlıkları eklemek istediğinizde, `--header` seçeneği yetersiz kalır.

Örneğin, bir HTTP vekil sunucusu üzerinden bir HTTPS isteği gönderirseniz, bu önce vekil sunucuya uzak sunucuya bir tünel kuran bir `CONNECT` göndererek ve ardından isteği o sunucuya göndererek yapılır. Bu ilk `CONNECT` yalnızca vekil sunucuya verilir ve yalnızca onun özel başlığınızı aldığından emin olmak ve uzak sunucuya başka bir dizi özel başlık göndermek isteyebilirsiniz.

Yalnızca vekil sunucuya belirli bir farklı `User-Agent:` ayarlayın:

    curl --proxy-header "User-Agent: magic/3000" -x proxy https://example.com/
