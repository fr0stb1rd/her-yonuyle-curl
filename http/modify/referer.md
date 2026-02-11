# Referer

Bir kullanıcı bir web sayfasındaki bir bağlantıya tıkladığında ve tarayıcı kullanıcıyı bir sonraki URL'ye götürdüğünde, yeni URL'ye nereden geldiğini söyleyen bir `Referer:` başlığı gönderir. Bu referer başlığıdır. `Referer:` yanlış yazılmıştır (İngilizcede doğrusu Referrer'dır) ancak olması gereken şekli budur.

curl ile referer başlığını `-e` veya `--referer` ile şu şekilde ayarlarsınız:

    curl --referer http://comes-from.example.com https://www.example.com/
