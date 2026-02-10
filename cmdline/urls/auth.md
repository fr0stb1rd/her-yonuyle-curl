# İsim ve parola

Bir URL'deki şemanın ardından, gömülü olası bir kullanıcı adı ve parola alanı olabilir. Bu sözdiziminin kullanımı, bu bilgileri betiklerde veya başka şekilde kolayca sızdırabileceğiniz için bugünlerde genellikle hoş karşılanmaz. Örneğin, belirli bir isim ve parola kullanarak bir FTP sunucusunun dizinini listelemek:

    curl ftp://user:password@example.com/

URL'de kullanıcı adı ve parolanın varlığı tamamen isteğe bağlıdır. curl, bu bilgilerin URL'nin dışında normal komut satırı seçenekleriyle sağlanmasına da izin verir.

Kullanıcı adı ve/veya parolanın bir parçası olarak ASCII olmayan bir harf veya belki bir `:` veya `@` istiyorsanız, o harfi URL kodlamayı (URL encode) unutmayın: `HH`nin onaltılık bayt değeri olduğu `%HH` olarak yazın. `:` `%3a` ve `@` `%40`'tır.
