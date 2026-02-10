# GET'e dönüştürme

Bu bağlamda bahsetmeye uygun olabilecek küçük bir kolaylık özelliği, farklı `-d` varyantlarıyla belirttiğiniz tüm verileri alan ve bu verileri girilen URL'ye örn. ```http://example.com``` bir '?' ile ayrılmış olarak ekleyen ve ardından curl'ün bunun yerine bir GET göndermesini sağlayan `-G` veya `--get` seçeneğidir.

Bu seçenek, örneğin bir formu POST gönderme ve GET gönderme arasında geçiş yapmayı kolaylaştırır.

URL'de bir sorgu olarak kodlanmış bir veri parçası ekleyen bir örnek:

    curl -G --data-urlencode "name=daniel stenberg" https://example.com/
