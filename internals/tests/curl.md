# curl testleri

Paketteki standart test "curl testi"dir. Hepsi bir curl komut satırını çağırır ve gönderdiği, geri aldığı ve döndürdüğü her şeyin tam olarak beklendiği gibi olduğunu doğrular. Herhangi bir uyuşmazlık durumunda test başarısız kabul edilir ve betik hata hakkındaki ayrıntıları gösterir.

`<client><command>` bölümünde testin içerdiği şey, komut satırında kullanılan şeydir, kelimesi kelimesine.

`tests/log/commands.log`, testte çalıştırılan tam komut satırını içerdiği için bir çalışmadan sonra bakmak için kullanışlıdır.

curl komut satırı aracını çağırmayan bir test yapmak istiyorsanız, bunun yerine [libcurl testlerini](libcurl.md) veya [birim testlerini](unit.md) düşünmelisiniz.
