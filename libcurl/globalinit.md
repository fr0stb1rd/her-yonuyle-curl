# Küresel başlatma (Global initialization)

Programınızda libcurl ile ilgili herhangi bir şey yapmadan önce, `curl_global_init()` ile küresel bir libcurl başlatma çağrısı yapmalısınız. Bu gereklidir çünkü libcurl'ün kullanabileceği bazı temel kütüphanelerin düzgün bir şekilde kurulması ve başlatılması için önceden bir çağrıya ihtiyacı vardır.

curl_global_init(), ne yazık ki, iş parçacığı güvenli (thread safe) değildir, bu nedenle bunu yalnızca bir kez yaptığınızdan ve asla başka bir çağrıyla aynı anda yapmadığınızdan emin olmalısınız. Küresel durumu başlatır, bu nedenle yalnızca bir kez çağırmalısınız ve programınız libcurl'ü kullanmayı tamamen bitirdiğinde, init çağrısının ayırdığı ilişkili küresel kaynakları serbest bırakmak ve temizlemek için `curl_global_cleanup()` işlevini çağırabilirsiniz.

libcurl, `curl_global_init()` çağrısını atladığınız durumu ele almak için oluşturulmuştur, ancak bunu (herhangi bir gerçek dosya transferi başlamadan önce yapmadıysanız) kendisi çağırarak yapar ve ardından kendi varsayılanlarını kullanır. O zaman bile iş parçacığı güvenli olmadığına dikkat edin, bu nedenle sizin için bazı "ilginç" yan etkilere neden olabilir. curl_global_init()'i kontrollü bir şekilde kendiniz çağırmak çok daha iyidir.
