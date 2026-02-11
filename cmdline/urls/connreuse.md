# Bağlantı yeniden kullanımı

Sitelere bağlantılar kurarken, curl eski bağlantıları bir süre ortalıkta tutar, böylece bir sonraki transfer önceki bir transferle aynı ana bilgisayarı kullanılarak yapılırsa, aynı bağlantıyı tekrar kullanabilir ve böylece çok fazla zaman kazanabilir. Buna kalıcı (persistent) bağlantılar diyoruz. curl her zaman bağlantıları canlı tutmaya çalışır ve mevcut bağlantıları elinden geldiğince yeniden kullanır.

Bağlantılar *bağlantı havuzunda* (connection pool), bazen *bağlantı önbelleği* (connection cache) olarak da adlandırılır, tutulur.

Ancak curl komut satırı aracı, bağlantıları yalnızca çalıştığı sürece canlı tutabilir, bu nedenle komut satırınıza geri döner dönmez o anda açık olan tüm bağlantıları kapatmak (ve ayrıca sonraki işlemlerin süresini azaltmak için kullandığı diğer tüm önbellekleri serbest bırakmak ve temizlemek) zorundadır. Canlı bağlantılar havuzuna *bağlantı önbelleği* diyoruz.

Aynı ana bilgisayara veya aynı temel URL'ye karşı N transfer veya işlem gerçekleştirmek istiyorsanız, curl'ü her seferinde bir URL ile tekrar tekrar çağırmak yerine, bunları mümkün olduğunca az curl komut satırında yapmaya çalışarak çok fazla hız kazanabilirsiniz.
