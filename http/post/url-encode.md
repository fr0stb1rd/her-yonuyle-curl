# URL kodlanmış veri

Yüzde kodlaması (Percent-encoding), diğer adıyla URL kodlaması (URL encoding), teknik olarak verileri URL'lerde görünebilecek şekilde kodlamak için bir mekanizmadır. Bu kodlama tipik olarak `application/x-www-form-urlencoded` içerik türüyle POST gönderirken kullanılır; örneğin curl'ün `--data` ve `--data-binary` vb. ile gönderdikleri gibi.

Yukarıda belirtilen komut satırı seçeneklerinin tümü, uygun şekilde kodlanmış veriler sağlamanızı, verilerin zaten doğru biçimde var olduğundan emin olmanızı gerektirir. Bu size çok fazla özgürlük verirken, zaman zaman biraz zahmetli de olabilir.

Henüz kodlamadığınız verileri göndermenize yardımcı olmak için curl `--data-urlencode` seçeneğini sunar. Bu seçenek size verdiğiniz verileri URL kodlamak için birkaç farklı yol sunar.

Bunu diğer --data seçenekleriyle aynı tarzda `--data-urlencode data` şeklinde kullanırsınız. CGI uyumlu olması için, **data** kısmı bir ad, ardından bir ayırıcı ve içerik belirtimi ile başlamalıdır. **data** kısmı curl'e aşağıdaki sözdizimlerinden biri kullanılarak iletilebilir:

 - `content`: İçeriği URL kodlayın ve iletin. İçeriğin herhangi bir `=` veya `@` sembolü içermemesine dikkat edin, çünkü bu durumda sözdizimi aşağıdaki diğer durumlardan biriyle eşleşir.

 - `=content`: İçeriği URL kodlayın ve iletin. Başlangıçtaki `=` sembolü veriye dahil edilmez.

 - `name=content`: İçerik kısmını URL kodlayın ve iletin. Ad kısmının zaten URL kodlanmış olması beklendiğini unutmayın.

 - `@filename`: Verilen dosyadan verileri yükleyin (yeni satırlar dahil), verileri URL kodlayın ve POST içinde iletin.

 - `name@filename`: Verilen dosyadan verileri yükleyin (yeni satırlar dahil), verileri URL kodlayın ve POST içinde iletin. Ad kısmına bir eşittir işareti eklenir, sonuç `name=urlencoded-file-content` olur. Adın zaten URL kodlanmış olmasının beklendiğini unutmayın.

Örnek olarak, bir adı curl tarafından kodlanmış olarak POST ile gönderebilirsiniz:

    curl --data-urlencode "name=John Doe (Junior)" http://example.com

…bu, gerçek istek gövdesinde aşağıdaki verileri gönderir:

    name=John%20Doe%20%28Junior%29

`John Doe (Junior)` dizesini `contents.txt` adlı bir dosyada saklarsanız, curl'e bu içeriği 'user' alan adını kullanarak URL kodlanmış olarak göndermesini şu şekilde söyleyebilirsiniz:

    curl --data-urlencode user@contents.txt http://example.com

Yukarıdaki her iki örnekte de, alan adı URL kodlanmış değildir ancak olduğu gibi iletilir. Alan adını da URL kodlamak isterseniz, örneğin `user name` adlı bir alan adını iletmek isterseniz, curl'den tüm dizeyi başına bir eşittir işareti (gönderilmez) koyarak kodlamasını isteyebilirsiniz:

    curl --data-urlencode "=user name=John Doe (Junior)" http://example.com
