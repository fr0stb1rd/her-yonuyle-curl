# Şifreler (Ciphers)

curl bir TLS sunucusuna bağlandığında, protokolü nasıl konuşacağını müzakere eder ve bu müzakere her iki tarafın da üzerinde anlaşması gereken birkaç parametre ve değişken içerir. Parametrelerden biri, şifre (cipher) olarak adlandırılan hangi kriptografi algoritmalarının kullanılacağıdır. Zamanla, güvenlik araştırmacıları mevcut şifrelerdeki kusurları ve zayıflıkları bulurlar ve bunlar zamanla aşamalı olarak kaldırılır.

Ayrıntılı (verbose) seçeneğini, `-v` kullanarak, hangi şifrenin ve TLS sürümünün müzakere edildiği hakkında bilgi alabilirsiniz. `--ciphers` seçeneğini kullanarak müzakerede hangi şifrenin tercih edileceğini değiştirebilirsiniz, ancak unutmayın, bu, işleri daha da kötüleştirmeyen şekillerde nasıl kullanılacağını bilmeyi gerektiren güçlü bir özelliktir.
