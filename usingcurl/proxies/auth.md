# Vekil sunucu kimlik doğrulaması

HTTP ve SOCKS vekil sunucuları kimlik doğrulaması gerektirebilir, bu nedenle curl'ün kullanılmasına izin verilmesi için vekil sunucuya uygun kimlik bilgilerini sağlaması gerekir. Bunu yapmamak (veya yanlış kimlik bilgilerini sağlamak), vekil sunucunun 407 kodunu kullanarak HTTP yanıtları döndürmesine neden olur.

Vekil sunucular için kimlik doğrulama, "normal" HTTP kimlik doğrulamasına benzer. İstemcilerin hem normal ana bilgisayar kimlik doğrulamasını hem de vekil sunucu kimlik doğrulamasını bağımsız olarak kullanmalarına izin vermek için sunucu kimlik doğrulamasından ayrıdır.

curl ile, `-U user:password` veya `--proxy-user user:password` seçeneğiyle vekil sunucu kimlik doğrulaması için kullanıcı adı ve şifreyi ayarlarsınız:

    curl -U daniel:secr3t -x myproxy:80 http://example.com

Bu örnek varsayılan olarak Basic kimlik doğrulama şemasını kullanır. Bazı vekil sunucular diğer kimlik doğrulama şemalarını gerektirir (ve 407 yanıtı aldığınızda döndürülen başlıklar hangisi olduğunu söyler) ve ardından `--proxy-digest`, `--proxy-negotiate`, `--proxy-ntlm` ile belirli bir yöntem isteyebilirsiniz. Yukarıdaki örnek komut tekrar, ancak vekil sunucu ile NTLM yetkilendirmesi isteyerek:

    curl -U daniel:secr3t -x myproxy:80 http://example.com --proxy-ntlm

Ayrıca, curl'den vekil sunucunun hangi yöntemi istediğini ve desteklediğini bulmasını ve ardından (ekstra gidiş-dönüş masrafıyla) `--proxy-anyauth` kullanarak onunla gitmesini isteyen bir seçenek de vardır. curl'den vekil sunucunun istediği herhangi bir yöntemi kullanmasını istemek şöyledir:

    curl -U daniel:secr3t -x myproxy:80 http://example.com --proxy-anyauth
