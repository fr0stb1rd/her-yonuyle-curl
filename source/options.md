# Derleme seçeneklerini yönetme

curl ve libcurl kaynak kodu, mevcut hemen hemen her bilgisayar platformunda derlenmek ve çalışmak üzere dikkatlice yazılmıştır. Bu ancak sıkı bir çalışmayla ve birkaç yönergeye (ve tabii ki makul miktarda teste) bağlı kalarak yapılabilir.

Altın kural, her zaman belirli özellikleri kontrol eden #ifdef'ler eklemek ve ardından kurulum komut dosyalarının (configure veya CMake veya sabit kodlanmış) program orada derlenmeden önce kullanıcının bilgisayar kurulumunda söz konusu özelliklerin varlığını kontrol etmesini sağlamaktır. Ek olarak ve bir bonus olarak, kodu bu şekilde yazma sayesinde, bazı özellikler sistemde mevcut olsalar ve *kullanılabilecek* olsalar bile açıkça kapatılabilir. Buna örnek olarak, kullanıcıların örneğin daha küçük bir ayak izine sahip veya belirli protokoller için desteği devre dışı bırakılmış vb. bir kütüphane sürümü derlemek istemeleri verilebilir.

Proje bazen, örneğin tek bir dosya belirli bir işletim sistemi veya belki de her zaman mevcut olmayan belirli bir özellik için sağlandığında, tüm kaynak dosyaların etrafında #ifdef koruması kullanır. Bu, tüm platformların her zaman tüm dosyaları derlemesini mümkün kılmak içindir—derleme komut dosyalarını ve makefile'larını çok basitleştirir. Tamamen #ifdef ile dışarıda bırakılan bir dosya, zaten derleme süresine neredeyse hiçbir şey eklemez.

Kodun içine #ifdef'ler serpiştirmek yerine, mümkün olduğu ölçüde, kodun mevcut özelliklerden bağımsız olarak aynı görünmesini ve çalışmasını sağlayan işlevler ve makrolar sağlarız. Bunların bazıları, özelliklerden yoksun derlemeler için boş makrolardır.

Hem TLS işleme hem de isim çözümleme, belirli uygulamayı ve 3. taraf yazılım kütüphanesi seçimini gizleyen dahili bir API ile gerçekleştirilir. Bu şekilde, çoğu iç yapı, libcurl'e hangi TLS kütüphanesini veya isim çözümleme sistemini kullanması söylendiğinden bağımsız olarak aynı şekilde çalışır.
