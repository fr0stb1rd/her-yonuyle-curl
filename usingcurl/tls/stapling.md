# OCSP zımbalama (OCSP stapling)

Bu, sunucudan el sıkışmada CA'dan sertifikanın hala geçerli olduğuna dair taze bir "kanıt" sağlamasını istemek için Sertifika Durum İsteği (Certificate Status Request) adı verilen TLS uzantısını kullanır. Bu, sunucunun sertifikasının iptal edilmediğinden gerçekten emin olmanın bir yoludur.

Sunucu bu uzantıyı desteklemiyorsa, test başarısız olur ve curl bir hata döndürür. Sunucuların bunu desteklememesi hala yaygındır.

El sıkışmasının durum isteğini şu şekilde kullanmasını isteyin:

    curl --cert-status https://example.com/

Bu özellik yalnızca OpenSSL ve GnuTLS arka uçları tarafından desteklenir.
