# çoklu iş parçacığı (multi-threading)

libcurl iş parçacığı güvenlidir (thread safe) ancak dahili iş parçacığı senkronizasyonu yoktur. libcurl'ü iş parçacıklı olarak düzgün bir şekilde kullanmak için kendi kilitlemenizi sağlamanız veya seçenekleri değiştirmeniz gerekebilir. Tam olarak neyin gerekli olduğu libcurl'ün nasıl derlendiğine bağlıdır. Lütfen en son bilgileri içeren [libcurl iş parçacığı güvenliği](https://curl.se/libcurl/c/threadsafe.html) web sayfasına bakın.
