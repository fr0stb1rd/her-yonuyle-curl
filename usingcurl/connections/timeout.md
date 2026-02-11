# Bağlantı zaman aşımı

curl tipik olarak ağ transferinin ilk bir parçası olarak ana bilgisayara bir TCP bağlantısı kurar. Titrek ağ koşulları veya hatalı uzak sunucular varsa, bu TCP bağlantısı başarısız olabilir veya yavaş olabilir.

Komut dosyalarınız veya diğer kullanımlarınız üzerindeki etkiyi azaltmak için, curl'ün bağlantı girişimi için izin verdiği maksimum süreyi saniye cinsinden ayarlayabilirsiniz. `--connect-timeout` ile curl'e bağlanmak için izin verilen maksimum süreyi söylersiniz ve curl bu sürede bağlanmamışsa bir hata döndürür.

Bağlantı zaman aşımı yalnızca curl'ün bağlandığı ana kadar harcamasına izin verilen süreyi sınırlar, bu nedenle TCP bağlantısı kurulduktan sonra daha uzun bir süre alabilir. Genel curl zaman aşımları hakkında daha fazla bilgi için [Zaman aşımları (Timeouts)](../timeouts.md) bölümüne bakın.

Düşük bir zaman aşımı belirtirseniz, curl'ün uzak sunuculara, yavaş sunuculara veya güvenilmez ağlar üzerinden eriştiğiniz sunuculara bağlanma yeteneğini etkili bir şekilde devre dışı bırakırsınız.

Bağlantı zaman aşımı, saniye altı hassasiyet için ondalık bir değer olarak belirtilebilir. Örneğin, bağlanmak için 2781 milisaniyeye izin vermek için:

    curl --connect-timeout 2.781 https://example.com/
