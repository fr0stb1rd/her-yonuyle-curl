# User-agent

User-Agent, her istemcinin sunucuya hangi kullanıcı aracısı olduğunu bildirmek için istekte ayarlayabileceği bir başlıktır . Bazen sunucular bu başlığa bakar ve içeriğine göre nasıl davranacaklarını belirler.

Varsayılan başlık değeri 'curl/[sürüm]'dür; curl sürüm 7.54.1 için `User-Agent: curl/7.54.1` gibi.

`-A` veya `--user-agent` seçeneğini artı kullanılacak dizeyi kullanarak veya sadece bir başlık olduğu için `-H "User-Agent: foobar/2000"` kullanarak istediğiniz herhangi bir değeri ayarlayabilirsiniz.

Karşılaştırma olarak, bir Linux makinesindeki Firefox'un test sürümü bir zamanlar şu User-Agent başlığını gönderdi:

`User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0`
