# Easy ile yürütme

'easy' (kolay) adı sadece libcurl'ü kullanmanın gerçekten kolay yolu olduğu için seçildi ve easy ile elbette birkaç sınırlama gelir. Örneğin, aynı anda yalnızca bir transfer yapabilmesi ve tüm transferi tek bir işlev çağrısında yapması ve tamamlandığında geri dönmesi gibi:

    res = curl_easy_perform( easy_handle );

Sunucu yavaşsa, transfer büyükse veya ağda bazı hoş olmayan zaman aşımları veya benzeri durumlar varsa, bu işlev çağrısı uzun zaman alabilir. Elbette, N saniyeden fazla harcamasına izin vermemek için zaman aşımları ayarlayabilirsiniz ancak bu yine de belirli koşullara bağlı olarak önemli miktarda zaman anlamına gelebilir.

libcurl easy arayüzüyle transfer yaparken uygulamanızın başka bir şey yapmasını istiyorsanız, birden fazla iş parçacığı (threads) kullanmanız gerekir. Easy arayüzünü kullanırken birden fazla eşzamanlı transfer yapmak istiyorsanız, transferlerin her birini kendi iş parçacığında gerçekleştirmeniz gerekir.
