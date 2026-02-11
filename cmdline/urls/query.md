# Sorgu (Query)

Bir URL'nin sorgu kısmı, soru işaretinin (`?`) sağında ancak kare (`#`) ile başlayan [bölümün (fragment)](fragment.md) solunda yer alan veridir.

Sorgu, URL kodlanmış olduğu sürece herhangi bir karakter dizesi olabilir. Ve (`&`) işaretleriyle ayrılmış bir anahtar/değer çiftleri dizisi kullanmak yaygın bir uygulamadır. `https://example.com/?name=daniel&tool=curl` örneğinde olduğu gibi.

Kullanıcıların bu tür sorgu kümelerini düzgün bir şekilde kodlanmış olarak oluşturmalarına yardımcı olmak için curl, `--url-query [content]` komut satırı seçeneğini sunar. Bu seçenek, sağlanan URL'nin sorgu kısmının sonuna içerik, genellikle bir ad + değer çifti ekler.

Sorgu parçaları eklerken, curl ve (`&`) ayırıcıları ekler.

Sözdizimi, bir uzantı ile `--data-urlencode` tarafından kullanılanla aynıdır: `+` öneki. Aşağıya bakın.

 - `content`: İçeriği URL kodlayın ve bunu sorguya ekleyin. Sözdiziminin aşağıdaki diğer durumlardan biriyle eşleşmesine neden olduğundan, içeriğin herhangi bir `=` veya `@` sembolü içermemesine dikkat edin.

 - `=content`: İçeriği URL kodlayın ve bunu sorguya ekleyin. Başlangıçtaki `=` sembolü verilere dahil edilmez.

 - `name=content`: İçerik kısmını URL kodlayın ve bunu sorguya ekleyin. İsim kısmının zaten URL kodlanmış olmasının beklendiğini unutmayın.

 - `@filename`: Verilen dosyadan (yeni satırlar dahil) verileri yükleyin, verileri URL kodlayın ve bunu sorguya ekleyin.

 - `name@filename`: Verilen dosyadan (yeni satırlar dahil) verileri yükleyin, verileri URL kodlayın ve bunu sorguya ekleyin. İsim kısmına bir eşittir işareti eklenir ve sonuç `name=urlencoded-file-content` olur. İsim kısmının zaten URL kodlanmış olmasının beklendiğini unutmayın.

 - `+content`: İçeriği herhangi bir kodlama yapmadan sorguya ekleyin.
