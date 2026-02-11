# Sunucu sertifikalarını doğrulama

Bir sunucuyla güvenli bir bağlantıya sahip olmak, **doğru** ana bilgisayarla iletişim kurduğunuzdan da emin olamıyorsanız pek bir şey ifade etmez. Bunu bilmiyorsak, sadece sandığımız kişi *gibi görünen* bir sahtekarla da konuşuyor olabiliriz.

Doğru TLS sunucusuyla iletişim kurduğunu kontrol etmek için curl, sunucunun sertifikasının imzasını doğrulamak üzere bir CA deposu - bir sertifika seti - kullanır. Tüm sunucular, TLS el sıkışmasının bir parçası olarak istemciye bir sertifika sağlar ve tüm genel TLS kullanan sunucular bu sertifikayı yerleşik bir Sertifika Yetkilisinden edinmiştir.

Uygulanan bazı kripto büyülerinden sonra curl, sunucunun aslında curl'ün ona bağlanmak için kullandığı ana bilgisayar adı için o sertifikayı edinen doğru sunucu olduğunu bilir. Sunucunun sertifikasını doğrulayamamak bir TLS el sıkışma hatasıdır ve curl bir hatayla çıkar.

Nadir durumlarda, sertifika doğrulaması başarısız olsa bile bir TLS sunucusuyla iletişim kurmaya devam etmek istediğinize karar verebilirsiniz. O zaman iletişiminizin Ortadaki Adam (Man-In-The-Middle) saldırılarına maruz kalabileceği gerçeğini kabul edersiniz. `-k` veya `--insecure` seçeneğiyle korumalarınızı indirirsiniz.

## Yerel CA depoları

Windows ve macOS gibi işletim sistemleri kendi CA depolarına sahip olma eğilimindedir.

curl'ü Windows'ta Schannel ile çalıştırırsanız, curl varsayılan olarak Windows'un kendi CA deposunu kullanır.

curl'ü macOS'ta Secure Transport ile çalıştırırsanız, curl varsayılan olarak macOS'un kendi CA deposunu kullanır.

curl'ü Schannel veya Secure Transport dışındaki herhangi bir TLS arka ucuyla kullanırsanız, yerel CA deposundan bağımsız olarak ayrı bir dosyada veya dizinde sağlanan bir CA deposunu kullanır. Ancak, bazıları için yine de `--ca-native` komut satırı seçeneğini kullanarak curl'den yerel CA deposunu tercih etmesini isteyebilirsiniz. Bu seçenek OpenSSL (ve çatalları), wolfSSL ve GnuTLS ile desteklenir.

HTTPS vekil sunucuları için karşılık gelen seçenek `--proxy-ca-native` olarak adlandırılır.

## Dosya(lar)daki CA deposu

curl platformunuza özgü bir TLS kütüphanesini (Schannel veya Secure Transport gibi) kullanacak şekilde derlenmemişse, ya yerel CA deposunun nerede olduğunu bilecek şekilde derlenmiş olması gerekir ya da kullanıcıların curl çağrıldığında CA deposuna bir yol sağlaması gerekir.

TLS el sıkışmasında kullanılacak belirli bir CA paketini `--cacert` komut satırı seçeneğiyle belirtebilirsiniz. Bu paketin PEM formatında olması gerekir. Ayrıca `CURL_CA_BUNDLE` ortam değişkenini tam yola ayarlayabilirsiniz.

## Windows'ta CA deposu

Yerel TLS kütüphanesini (Schannel) kullanmayan Windows üzerinde derlenmiş curl, CA deposunun nasıl bulunup kullanılabileceği konusunda fazladan bir diziye sahiptir.

curl, `curl-ca-bundle.crt` adlı bir CA sertifika dosyasını şu dizinlerde ve şu sırayla arar:

 1. uygulamanın dizini
 2. geçerli çalışma dizini
 3. Windows Sistem dizini (örn. `C:\windows\system32`)
 4. Windows Dizini (örn. `C:\windows`)
 5. `%PATH%` boyuncaki tüm dizinler
