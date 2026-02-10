# Çerezler (Cookies)

HTTP çerezleri, bir istemcinin bir sunucu adına sakladığı anahtar/değer çiftleridir. Sonraki isteklerde, istemcilerin istekler arasında durumu korumasını sağlamak için geri gönderilirler. HTTP protokolünün kendisinin bir durumu olmadığını, bunun yerine istemcinin sunucunun haberdar olmasını istediği sonraki isteklerde tüm verileri yeniden göndermesi gerektiğini unutmayın.

Çerezler, sunucu tarafından `Set-Cookie:` başlığı ile ayarlanır ve sunucu her çerezle birlikte istemcinin çerezi geri göndermesi için eşleşmesi gereken bir dizi ek özellik gönderir. Alan adı ve yol gibi ve belki de en önemlisi çerezin ne kadar süre yaşayacağı gibi.

Bir çerezin süresi ya gelecekte belirli bir zamana (veya belirli bir saniye sayısı kadar yaşayacak şekilde) ayarlanır ya da hiç süre almaz. Süresi olmayan bir çereze oturum çerezi denir ve *oturum* (session) boyunca yaşaması amaçlanır, ancak daha uzun değil. Bu açıdan bir oturum, tipik olarak bir siteyi görüntülemek için kullanılan tarayıcının ömrü olarak düşünülür. Tarayıcıyı kapattığınızda oturumunuzu sonlandırırsınız. Çerezleri destekleyen bir komut satırı istemcisiyle HTTP işlemleri yapmak, bir oturumun gerçekte ne zaman sona erdiği sorusunu akla getirir...

 * [Çerez motoru](engine.md)
 * [Çerezleri dosyadan okuma](reading.md)
 * [Çerezleri dosyaya yazma](writing.md)
 * [Yeni çerez oturumu](newsession.md)
 * [Çerez dosya formatı](fileformat.md)
