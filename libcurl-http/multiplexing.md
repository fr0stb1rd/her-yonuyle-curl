# Çoğullama (Multiplexing)

HTTP sürüm 2 ve 3, "çoğullama" (multiplexing) sunar. Bu protokol özelliğini kullanarak, bir HTTP istemcisi *aynı tek bir bağlantı üzerinden* bir sunucuya birkaç eşzamanlı transfer yapabilir. Bu özellik, HTTP protokolünün önceki sürümlerinde mevcut değildir. Daha önceki HTTP sürümlerinde, istemcinin ya birden çok bağlantı oluşturması ya da transferleri seri bir şekilde, biri diğerinden sonra yapması gerekirdi.

libcurl, hem HTTP/2 hem de HTTP/3 için HTTP çoğullamayı destekler.

HTTP çoğullamayı destekleyen bir sunucuya multi arayüzünü kullanarak birden çok transfer yaptığınızdan emin olun. libcurl, yalnızca sonraki transferler için aynı ana bilgisayar adı kullanıldığında transferleri çoğullayabilir.

Tüm pratik amaçlar ve API davranışları için, bir uygulamanın çoğullamanın yapılıp yapılmadığını umursaması gerekmez.

libcurl varsayılan olarak çoğullamayı etkinleştirir, ancak aynı anda birden çok transfer başlatırsanız kısa vadeli hıza öncelik verirler, bu nedenle çoğullamak için başka bir transfer tarafından bir bağlantının oluşturulmasını beklemek yerine yeni bağlantılar açabilirler. libcurl'e çoğullamaya öncelik vermesini söylemek için, `curl_easy_setopt()` ile transfer için `CURLOPT_PIPEWAIT` seçeneğini ayarlayın.

`curl_multi_setopt()`'un `CURLMOPT_PIPELINING` seçeneğiyle, belirli bir multi handle için çoğullamayı devre dışı bırakabilirsiniz.
