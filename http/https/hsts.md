# HSTS

*HTTPS'in otomatik kullanımı*.

HTTP Strict Transport Security, HSTS, HTTPS sunucularını protokol düşürme (downgrade) saldırıları ve çerez ele geçirme (cookie hijacking) gibi ortadaki adam saldırılarına karşı korumaya yardımcı olan bir protokol mekanizmasıdır. Bir HTTPS sunucusunun, istemcilerin bundan sonra bu ana bilgisayar adıyla otomatik olarak yalnızca HTTPS bağlantılarını kullanarak etkileşime girmesi gerektiğini - ve açıkça onunla düz metin protokolleri kullanmamasını - beyan etmesini sağlar.

## HSTS önbelleği

Belirli bir sunucu adı için HSTS durumu bir yanıt başlığında ayarlanır ve bir sona erme süresi vardır. Her HSTS ana bilgisayar adı için durumun, curl'ün onu alması ve durumu ve sona erme süresini güncellemesi için bir dosyaya kaydedilmesi gerekir.

curl'ü çağırın ve ona hsts önbelleği olarak hangi dosyayı kullanacağını söyleyin:

    curl --hsts hsts.txt https://example.com

curl, hsts bilgisini yalnızca başlık güvenli bir transfer üzerinden okunduğunda günceller, yani düz metin protokolü üzerinden yapıldığında değil.

## Güvenli olmayan protokolleri güncellemek için HSTS kullanın

Önbellek dosyası şimdi verilen ana bilgisayar adı için bir giriş içeriyorsa, güvenli olmayan bir protokolle bağlanmaya çalışsanız bile otomatik olarak güvenli bir protokole geçer:

    curl --hsts hsts.txt http://example.com
