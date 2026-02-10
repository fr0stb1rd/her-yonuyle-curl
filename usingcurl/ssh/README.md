# SCP ve SFTP

curl, ön koşul olarak 3. taraf kütüphanelerinden biriyle oluşturulmuşsa SCP ve SFTP protokollerini destekler: [libssh2](https://www.libssh2.org/),
[libssh](https://www.libssh.org/) veya
[wolfSSH](https://www.wolfssl.com/products/wolfssh/).

SCP ve SFTP, TLS'ye benzeyen ancak birkaç önemli yönden farklılık gösteren, güvenli ve şifreli bir veri protokolü olan SSH'nin üzerine inşa edilmiş protokollerdir. Örneğin, SSH herhangi bir türde sertifika kullanmaz, bunun yerine açık ve özel anahtarlar kullanır. Hem SSH hem de TLS, doğru kullanıldığında güçlü şifreleme ve güvenli transferler sağlar.

SCP protokolü genellikle taşınabilir olmadığı ve genellikle yalnızca Unix sistemleri arasında çalıştığı için ikisinin kara koyunu olarak kabul edilir.

 * [URL](url.md)
 * [Kimlik Doğrulama (Authentication)](auth.md)
 * [Bilinen ana bilgisayarlar (Known hosts)](knownhosts.md)
