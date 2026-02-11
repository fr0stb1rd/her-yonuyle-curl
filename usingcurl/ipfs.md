# IPFS

IPFS, *Gezegenler Arası Dosya Sistemi* (Inter-Planetary File System) anlamına gelir. curl, IPFS'yi yalnızca bir *HTTP ağ geçidi* (HTTP gateway) aracılığıyla destekler. Bu, kendisine verildiğinde IPFS URL'lerini anladığı, ancak içeriği almak üzere curl'ün kullanması için çalışan bir ağ geçidi URL'si de sağlamanız gerektiği anlamına gelir. curl yerel olarak IPFS konuşmaz.

## Ağ geçidi (Gateway)

`--ipfs-gateway`, kullanıcının IPFS HTTP ağ geçidi URL'sini belirtmesini sağlar. Şöyle:

    curl --ipfs-gateway http://localhost:8080 ipfs://bafybeigagd5nmnn2iys2f3d/

Uzak bir ağ geçidine gitmeyi seçerseniz, ağ geçidine tamamen güvendiğinizin farkında olmalısınız. Kendiniz barındırdığınız için yerel ağ geçitlerinde bu sorun değildir. Uzak ağ geçitlerinde, yaptığınız istekle eşleşmeyen verileri size döndüren, isteği inceleyen ve hatta isteğe müdahale eden kötü niyetli bir aktör olma potansiyeli vardır. curl kullanarak IPFS alırken bunu fark etmeyebilirsiniz.

`--ipfs-gateway` seçeneği kullanılmazsa, curl rehberlik için `IPFS_GATEWAY` ortam değişkenini ve ayarlanmamışsa ağ geçidini tanımlamak için kullanılabilecek `~/.ipfs/gateway` dosyasını kontrol eder.

IPFS desteği curl'e ilk olarak 8.4.0 sürümünde eklendi.
