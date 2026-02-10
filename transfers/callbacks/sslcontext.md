# SSL bağlamı (SSL context)

libcurl, `CURLOPT_SSL_CTX_FUNCTION` adlı özel bir TLS ile ilgili geri çağırım sunar. Bu seçenek yalnızca OpenSSL, wolfSSL veya mbedTLS tarafından desteklenen libcurl için çalışır ve libcurl başka bir TLS arka ucu ile oluşturulmuşsa hiçbir şey yapmaz.

Bu geri çağırım, uygulamanın TLS başlatma davranışını değiştirmesi için son bir şans vermek üzere diğer tüm TLS ile ilgili seçenekleri işledikten sonra, bir TLS bağlantısının başlatılmasından hemen önce libcurl tarafından çağrılır. İkinci argümanda geri çağırıma iletilen `ssl_ctx parametresi`, aslında OpenSSL veya wolfSSL için SSL kütüphanesinin `SSL_CTX`'ine bir işaretçi ve mbedTLS için `mbedtls_ssl_config`'e bir işaretçidir. Geri çağırımdan bir hata döndürülürse, bağlantı kurma girişimi yapılmaz ve işlem geri çağırımın hata kodunu döndürür. `userptr` argümanını `CURLOPT_SSL_CTX_DATA` seçeneğiyle ayarlayın.

Bu işlev, TLS pazarlığı sırasında bir sunucuya yapılan tüm yeni bağlantılarda çağrılır. TLS bağlamı her seferinde yeni başlatılan bir nesneye işaret eder.
