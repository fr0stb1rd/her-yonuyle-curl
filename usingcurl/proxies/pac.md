# PAC

Bazı ağ ortamları farklı durumlarda kullanılması gereken birkaç farklı vekil sunucu sağlar ve bunu işlemenin özelleştirilebilir bir yolu tarayıcılar tarafından desteklenir. Buna "[vekil sunucu otomatik yapılandırması](https://en.wikipedia.org/wiki/Proxy_auto-config)" veya PAC (proxy auto-config) denir.

Bir PAC dosyası, belirli bir ağ bağlantısının (URL) hangi vekil sunucuyu kullanması gerektiğine ve hatta hiç vekil sunucu kullanmaması gerekip gerekmediğine karar veren bir JavaScript işlevi içerir. Tarayıcılar PAC dosyasını genellikle yerel ağdaki bir URL'den okur.

curl'ün JavaScript yetenekleri olmadığından, curl PAC dosyalarını desteklemez. Tarayıcınız ve ağınız PAC dosyaları kullanıyorsa, ilerlemenin en kolay yolu genellikle PAC dosyasını manuel olarak okumak ve curl'ü başarıyla çalıştırmak için belirtmeniz gereken vekil sunucuyu bulmaktır.
