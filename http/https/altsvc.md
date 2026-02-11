# Alternatif Hizmetler (Alternative Services)

[RFC 7838](https://www.rfc-editor.org/rfc/rfc7838.txt), bir sunucunun, `Alt-Svc:` yanıt başlığını kullanarak bir istemciye o sunucu için başka bir yerde bir veya daha fazla *alternatif* olduğunu söylemesini sağlayan bir HTTP başlığı tanımlar.

Sunucunun önerdiği *alternatifler*, aynı ana bilgisayarda başka bir bağlantı noktasında, tamamen farklı bir ana bilgisayar adında çalışan bir sunucuyu içerebilir ve hatta belki hizmeti başka bir protokol üzerinden sunabilir.

## Etkinleştirme

curl'ün sunulan alternatifleri dikkate almasını sağlamak için, curl'e şunun gibi belirli bir alt-svc önbellek dosyası kullanmasını söyleyin:

    curl --alt-svc altcache.txt https://example.com/

o zaman curl başlangıçta mevcut alternatif hizmet girişlerini dosyadan yükler ve HTTP istekleri yaparken bunları dikkate alır ve sunucular yeni veya güncellenmiş `Alt-Svc:` başlıkları gönderirse, curl bunları çıkışta önbelleğe kaydeder.

## alt-svc önbelleği

alt-svc önbelleği bir çerez kavanozuna benzer. Satır başına bir alternatif depolayan metin tabanlı bir dosyadır ve her girişi o belirli alternatifin geçerli olduğu süre için bir sona erme zamanına da sahiptir.

## Yalnızca HTTPS

`Alt-Svc:`, yalnızca HTTPS üzerinden bağlanıldığında sunuculardan güvenilir ve ayrıştırılır.

## HTTP/3

`Alt-Svc:` başlıklarının kullanımı, Ağustos 2019 itibarıyla bir istemci ve sunucuyu HTTP/3 kullanmaya önyüklemenin (bootstrap) tek tanımlı yoludur. Sunucu daha sonra HTTP/1 veya HTTP/2 üzerinden istemciye HTTP/3 üzerinden de kullanılabilir olduğunu ima eder ve ardından alt-svc önbelleği öyle söylüyorsa curl sonraki istekte HTTP/3 kullanarak ona bağlanabilir.
