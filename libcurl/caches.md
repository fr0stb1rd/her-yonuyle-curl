# Önbellekler

libcurl, sonraki transferlerin daha hızlı gerçekleşmesine yardımcı olmak için farklı bilgileri önbelleğe alır. Dört temel önbellek vardır: DNS, bağlantılar, TLS oturumları ve CA sertifikaları.

Multi arayüz kullanıldığında, bu önbellekler varsayılan olarak o tek multi handle'a eklenen tüm easy handle'lar arasında paylaşılır ve easy arayüz kullanıldığında o handle içinde tutulurlar.

libcurl'e [paylaşım arayüzü](../helpers/sharing.md) ile önbelleklerin bazılarını paylaşması talimatını verebilirsiniz.

## DNS önbelleği

libcurl bir ana bilgisayar adını bir veya daha fazla IP adresine çözümlediğinde, bu DNS önbelleğinde saklanır, böylece yakın vadede sonraki transferlerin aynı çözümlemeyi tekrar yapması gerekmez. Bir ad çözümlemesi kolayca birkaç yüz milisaniye ve bazen çok daha uzun sürebilir.

Varsayılan olarak, bu tür her ana bilgisayar adı önbellekte 60 saniye saklanır (`CURLOPT_DNS_CACHE_TIMEOUT` ile değiştirilebilir).

libcurl aslında DNS girişleri için TTL (Yaşam Süresi) değerinin ne olduğunu genellikle bilmez, çünkü bu genellikle bu amaçla kullandığı sistem fonksiyon çağrılarında ifşa edilmez, bu nedenle bu değeri artırmak, libcurl'ün eski adresleri gereğinden uzun süre kullanmaya devam etmesi riskiyle birlikte gelir.

## Bağlantı önbelleği

Ayrıca bazen bağlantı havuzu olarak da adlandırılır. Bu, kullanımdan sonra kapatılmak yerine canlı tutulan, böylece aynı ana bilgisayar adını hedefleyen ve diğer birkaç kontrolü de eşleşen sonraki transferlerin yeni bir bağlantı oluşturmak yerine bunları kullanabileceği, önceden kullanılmış bağlantıların bir koleksiyonudur.

Yeniden kullanılan bir bağlantı genellikle bir DNS araması, bir TCP bağlantısı kurma, bir TLS el sıkışması yapma ve daha fazlasını yapmaktan tasarruf sağlar.

Bağlantılar yalnızca ad aynıysa yeniden kullanılır. İki farklı ana bilgisayar adı aynı IP adreslerine çözümlense bile, libcurl ile her zaman iki ayrı bağlantı kullanırlar.

Bağlantı yeniden kullanımı ana bilgisayar adına dayandığından ve bir transfer için bağlantı yeniden kullanıldığında DNS çözümleme aşaması tamamen atlandığından, libcurl DNS'deki ana bilgisayar adının mevcut durumunu bilmez, çünkü bağlantı hayatta kalıp orijinal IP adresi üzerinden yeniden kullanılmaya devam ederken aslında zamanla IP değiştirebilir.

Bağlantı önbelleğinin boyutu - orada tutulacak canlı bağlantı sayısı - easy handle'lar için `CURLOPT_MAXCONNECTS` (varsayılan 5'tir) ve multi handle'lar için `CURLMOPT_MAXCONNECTS` ile ayarlanabilir. Multi handle'lar için varsayılan boyut, eklenen easy handle sayısının 4 katıdır.

## TLS oturum önbelleği

TLS oturum kimlikleri ve biletleri, bir istemcinin daha önce bağlantı kurduğu bir sunucuya sonraki TLS el sıkışmalarını kısayoldan yapmak için bir sunucuya iletebileceği özel TLS mekanizmalarıdır.

libcurl, ana bilgisayar adları ve bağlantı noktası numaralarıyla ilişkili oturum kimliklerini ve biletleri önbelleğe alır, bu nedenle libcurl'ün önbelleğe alınmış bir kimliğe veya bilete sahip olduğu bir ana bilgisayara sonraki bir bağlantı girişimi yapılırsa, bunu kullanmak TLS el sıkışma sürecini ve dolayısıyla tamamlanana kadar gereken süreyi büyük ölçüde azaltabilir.

## CA sertifika önbelleği

curl'ün desteklediği bazı TLS arka uçlarıyla, bellekte bir CA sertifika deposu önbelleği oluşturur ve sonraki transferlerin kullanması için orada tutar. Bu, transferlerin bazen oldukça büyük CA sertifika demetlerini (bundles) yüklemekten ve işlemekten kaynaklanan gereksiz yükleme ve ayrıştırma süresini atlamasını sağlar.

CA sertifika demeti güncellenebileceğinden, önbelleğin ömrü varsayılan olarak 24 saate ayarlanmıştır, böylece uzun süreli çalışan uygulamalar önbelleği temizler ve depolamanın yeni bir sürümünü yükleyip kullanabilmek için dosyayı en az günde bir kez yeniden yükler.

Bu varsayılanın yeterince iyi olmadığı durumlarda uygulamalar `CURLOPT_CA_CACHE_TIMEOUT` seçeneğiyle CA sertifika önbellek zaman aşımını değiştirebilir.
