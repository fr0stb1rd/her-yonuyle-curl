# Hız sınırlama (Rate limiting)

curl veri transfer ettiğinde, bunu mümkün olduğunca hızlı yapmaya çalışır. Bu hem yüklemeler hem de indirmeler için geçerlidir. Bunun tam olarak ne kadar hızlı olacağı, bilgisayarınızın yeteneği, kendi ağ bağlantınızın bant genişliği, transfer yaptığınız/aldığınız uzak sunucudaki yük ve o sunucuya olan gecikme dahil olmak üzere çeşitli faktörlere bağlıdır. curl transferlerinizin, verilerin üzerinden geçtiği ağlardaki diğer transferlerle, diğer kullanıcılardan veya aynı kullanıcının diğer uygulamalarından gelenlerle rekabet etmesi de muhtemeldir.

Ancak birçok kurulumda, tek bir curl komut satırı ile kendi ağ bağlantınızı az çok doyurabilirsiniz. İnternete saniyede 10 megabitlik bir bağlantınız varsa, curl'ün veri aktarmak için bu 10 megabitin tamamını kullanabilme şansı yüksektir.

Çoğu kullanım durumu için mümkün olduğunca fazla bant genişliği kullanmak iyi bir şeydir. Transferi hızlandırır, curl komutunun daha erken tamamlanmasını sağlar ve transferin sunucudaki kaynakları daha kısa bir süre kullanmasını sağlar.

Bazen curl'ün yerel ağ bağlantınızdaki diğer ağ işlevlerini aç bırakması sakıncalıdır. Bu durumlarda, diğer ağ kullanıcılarının da verilerini iletme şansının daha yüksek olması için curl'e yavaşlamasını söylemek isteyebilirsiniz. `--limit-rate [hız]` ile curl'e verilen saniyedeki bayt sayısından daha hızlı gitmemesini söyleyebilirsiniz. Hız sınırı değeri, kilobayt, megabayt ve gigabayt için K, M ve G harf eklerinden biri kullanılarak verilebilir.

curl'ün verileri saniyede 200 kilobayttan daha hızlı indirmemesini sağlamak için:

    curl https://example.com/ --limit-rate 200K

Verilen sınır, birkaç saniyelik bir süre boyunca izin verilen maksimum *ortalama hızdır*. Bu, curl'ün kısa süreli patlamalarda daha yüksek transfer hızları kullanabileceği, ancak zamanla ortalamasının verilen hızdan fazla olmayacağı anlamına gelir.

curl mümkün olan maksimum hızın ne olduğunu bilmez — sadece olabildiğince ve izin verildiği kadar hızlı gider. Bağlantınızın maksimum hızını biliyor olabilirsiniz, curl bilmez.
