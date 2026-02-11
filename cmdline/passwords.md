# Parolalar

Parolalar alengirli ve hassastır. Bir parolanın sızdırılması, kaynaklara ve aksi takdirde korunan verilere sizden başka birinin erişmesine neden olabilir.

curl, kullanıcıdan parolaları almak ve ardından bunları başkasına iletmek veya başka bir şey için kullanmak üzere çeşitli yollar sunar.

En temel curl kimlik doğrulama seçeneği `-u / --user`dır. İki nokta üst üste ile ayrılmış kullanıcı adı ve parola olan bir argümanı kabul eder. `alice`'in HTTP kimlik doğrulaması gerektiren bir sayfa istemesi ve parolasının `12345` olması gibi:

    $ curl -u alice:12345 http://example.com/

## Komut satırı sızıntısı

Burada potansiyel olarak kötü birkaç şey oluyor. Birincisi, komut satırına bir parola giriyoruz ve komut satırı aynı sistemdeki diğer kullanıcılar tarafından okunabilir olabilir (çok kullanıcılı bir sisteminiz olduğunu varsayarsak). curl, işlem listelerinden parolaları silmeye çalışarak bu riski en aza indirmeye yardımcı olur.

Kullanıcı adını ve parolayı komut satırında geçmekten kaçınmanın bir yolu, bunun yerine bir [.netrc dosyası](../usingcurl/netrc.md) veya bir [yapılandırma dosyası](configfile.md) kullanmaktır. Ayrıca parolayı belirtmeden `-u` seçeneğini kullanabilirsiniz, bu durumda curl çalıştığında kullanıcıdan parolayı ister.

## Ağ sızıntısı

İkinci olarak, bu komut satırı kullanıcı kimlik bilgilerini bir HTTP sunucusuna gönderir; bu, aradaki adam saldırılarına (man-in-the-middle) veya bağlantıyı gözetleyen diğer meraklıların ne gönderildiğini görmesine açık olan düz metin bir protokoldür. Bu komut satırı örneğinde, curl'ün HTTP Temel kimlik doğrulamasını kullanmasını sağlar ve bu tamamen güvensizdir.

Bundan kaçınmanın birkaç yolu vardır ve anahtar, elbette, kimlik bilgilerini ağ üzerinden düz metin olarak gönderen protokollerden veya kimlik doğrulama şemalarından kaçınmaktır. En kolayı belki de protokollerin şifreli sürümlerini kullandığınızdan emin olmaktır. HTTP yerine HTTPS, FTP yerine FTPS kullanın, vb.

Düz metin ve güvensiz bir protokole bağlı kalmanız gerekiyorsa, kimlik bilgilerini açıkta göndermekten kaçınan bir kimlik doğrulama yöntemine geçip geçemeyeceğinize bakın. HTTP istiyorsanız, bu tür yöntemler Digest (`--digest`), Negotiate (`--negotiate`) ve NTLM (`--ntlm`) içerir.
