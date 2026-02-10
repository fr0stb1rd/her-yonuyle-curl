# Kimlik Doğrulama (Authentication)

curl ile bir SSH sunucusuna karşı kimlik doğrulama (bir SCP veya SFTP URL'si belirttiğinizde) aşağıdaki gibi yapılır:

1. curl sunucuya bağlanır ve bu sunucunun hangi kimlik doğrulama yöntemlerini sunduğunu öğrenir
2. curl daha sonra sunulan yöntemleri bir tanesi çalışana veya hepsi başarısız olana kadar tek tek dener

Sunucu açık anahtar kimlik doğrulamasını sunuyorsa, curl ev dizininizdeki `.ssh` alt dizininde bulunan açık anahtarınızı kullanmaya çalışır. Bunu yaparken, curl'e sunucuda hangi kullanıcı adını kullanacağını söylemeniz gerekir. Örneğin, 'john' kullanıcısı 'sftp.example.com' adlı uzak SFTP sunucusundaki ev dizinindeki girişleri listeler:

    curl -u john: sftp://sftp.example.com/

curl herhangi bir nedenle açık anahtarla kimlik doğrulaması yapamazsa, sunucu izin veriyorsa ve kimlik bilgileri komut satırında iletilirse bunun yerine kullanıcı adı + şifreyi kullanmaya çalışır.

Örneğin, yukarıdaki aynı kullanıcı uzak bir sistemde `RHvxC6wUA` şifresine sahiptir ve SCP aracılığıyla bir dosyayı şu şekilde indirebilir:

    curl -u john:RHvxC6wUA -O scp://ssh.example.com/file.tar.gz
