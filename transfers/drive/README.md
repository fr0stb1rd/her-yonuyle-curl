# Transferleri yürütme (Drive transfers)

libcurl, transferi gerçekleştirmek için üç farklı yol sunar. Sizin durumunuzda hangi yolun kullanılacağı tamamen size ve neye ihtiyacınız olduğuna bağlıdır.

1. 'easy' arayüzü, eşzamanlı (synchronous) bir şekilde tek bir transfer yapmanızı sağlar. libcurl, transferin tamamını yapar ve tamamlandığında - başarılı veya başarısız - kontrolü uygulamanıza geri döndürür.

2. 'multi' arayüzü, aynı anda birden fazla transfer yapmak istediğinizde veya sadece engellemeyen (non-blocking) bir transfer istediğinizde kullanılır.

3. 'multi_socket' arayüzü, normal multi arayüzün hafif bir varyasyonudur, ancak olay tabanlıdır (event-based) ve eşzamanlı transfer sayısını yüzlere veya binlere çıkarmayı düşünüyorsanız gerçekten kullanılması önerilen API'dir.

Her birine biraz daha yakından bakalım…

* [Easy ile yürütme](easy.md)
* [Multi ile yürütme](multi.md)
* [multi\_socket ile yürütme](multi-socket.md)
