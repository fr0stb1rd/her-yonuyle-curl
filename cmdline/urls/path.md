# Yol (Path)

Her URL bir yol içerir. Hiçbir yol verilmezse, `/` ima edilir. Örneğin sadece ana bilgisayar adını kullandığınızda:

    curl https://example.com

Yol, tam olarak hangi kaynağın istendiğini veya sağlandığını tanımlamak için belirtilen sunucuya gönderilir.

Yolun tam kullanımı protokole bağlıdır. Örneğin, `README` dosyasını varsayılan anonim kullanıcıdan bir FTP sunucusundan almak:

    curl ftp://ftp.example.com/README

Dizin kavramına sahip protokoller için, URL'yi eğik çizgi (slash) ile sonlandırmak, bunun bir dosya değil bir dizin olduğu anlamına gelir. Bu nedenle bir FTP sunucusundan bir dizin listesi istemek böyle bir eğik çizgi ile ima edilir:

    curl ftp://ftp.example.com/tmp/

Yol alanının bir parçası olarak ASCII olmayan bir harf veya hatta boşluk (` `) istiyorsanız, o harfi "URL kodlamayı" (URL-encode) unutmayın: `HH`nin onaltılık bayt değeri olduğu `%HH` olarak yazın. ` ` `%20`dir.
