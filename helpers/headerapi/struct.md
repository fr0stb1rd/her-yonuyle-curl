# Başlık yapısı (Header struct)

Başlık API işlevlerinin döndürdüğü başlık yapısı işaretçisi, easy handle ile ilişkili belleğe işaret eder ve işlevlere yapılan sonraki çağrılar bu yapıyı bozar. Uygulamaların verileri saklamak istiyorlarsa kopyalamaları gerekir. Yapı için kullanılan bellek `curl_easy_cleanup()` çağrıldığında serbest bırakılır.

## Yapı

    struct curl_header {
       char *name;
       char *value;
       size_t amount;
       size_t index;
       unsigned int origin;
       void *anchor;
    };

**name**, başlığın adıdır. Bu ada sahip başlığın ilk örneği için kullanılan büyük/küçük harf kullanımını kullanır.

**value**, içeriktir. Ağ üzerinden tam olarak iletildiği gibi gelir ancak baştaki ve sondaki boşluklar ve yeni satırlar çıkarılır. Veriler her zaman null ile sonlandırılır.

**amount**, istenen köken ve istek bağlamında mevcut olan bu adı kullanan başlıkların sayısıdır.

**index**, bu belirli başlık adının sıfır tabanlı giriş numarasıdır; bu başlık istenen kapsamda birden fazla kez kullanıldıysa 0'dan büyük olabilir ancak her zaman **amount** değerinden küçüktür.

**origin**, (tam olarak) bir köken bitine sahiptir ve başlığın nereden kaynaklandığını belirtir.

**anchor**, libcurl dahili parametreleri tarafından kullanılan özel bir handle'dır. Değiştirmeyin. Hakkında hiçbir şey varsaymayın.
