# İstemci sertifikaları

TLS istemci sertifikaları, istemcilerin sunuculara gerçekten doğru eş olduklarını kriptografik olarak kanıtlamalarının bir yoludur (bazen Karşılıklı TLS veya mTLS olarak da bilinir). İstemci sertifikası kullanan bir komut satırı, sertifikayı ve karşılık gelen anahtarı belirtir ve bunlar daha sonra sunucuyla yapılan TLS el sıkışmasında iletilir.

Bunu yaparken istemci sertifikanızın zaten bir dosyada saklanmış olması gerekir ve bunu daha önce farklı bir kanal aracılığıyla doğru örnekten almış olmanız gerekir.

Anahtar genellikle sağlamanız gereken veya etkileşimli olarak istenecek bir şifreyle korunur.

curl, hem istemci sertifikası hem de özel anahtarın birleştirildiği tek bir dosyayı `--cert` kullanarak belirtmenize izin veren seçenekler sunar veya anahtar dosyasını `--key` ile bağımsız olarak belirtebilirsiniz:

    curl --cert mycert:mypassword https://example.com
    curl --cert mycert:mypassword --key mykey https://example.com

Bazı TLS arka uçları için anahtarı ve sertifikayı farklı türler kullanarak da iletebilirsiniz:

    curl --cert mycert:mypassword --cert-type PEM \
         --key mykey --key-type PEM https://example.com
