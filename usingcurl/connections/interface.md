# Ağ arayüzü

Birden fazla ağa bağlı birden fazla ağ arayüzüne sahip makinelerde, giden ağ trafiğinin hangi ağ arayüzünü kullanmasını tercih edeceğinize karar verebileceğiniz durumlar vardır. Veya iletişimde hangi kaynak IP adresini (sahip olduğunuz birden fazla adresten) kullanacağınızı.

curl'e iletişimin yerel ucunu hangi ağ arayüzüne, hangi IP adresine ve hatta hangi ana bilgisayar adına "bağlamak" istediğinizi `--interface` seçeneğiyle söyleyin:

    curl --interface eth1 https://www.example.com/

    curl --interface 192.168.0.2 https://www.example.com/

    curl --interface machine2 https://www.example.com/

Burada bir ana bilgisayar adı kullanılmasını önermiyoruz, çünkü bu curl'ü bir IP adresini bulmak için bir isim çözümlemesi yapmaya zorlar. Bir arayüz adı belirtemiyorsanız, sabit bir IP adresi kullanmayı düşünün.

Buna ek olarak, curl'ün tahmin etmek zorunda kalmasını önlemek için açıkça bir IP adresi veya arayüz adı kullanılmasını isteyebilirsiniz. Bunu, arayüz adı için `if!` veya IP adresi için `host!` dizesini öne ekleyerek yapın. Şöyle:

    curl --interface "host!192.168.0.2" https://www.example.com/

    curl --interface "if!eth1" https://www.example.com/

Hatta ikisini de sağlayarak belirli bir IP ve belirli bir arayüz belirtebilirsiniz, şöyle:

    curl --interface "if!eith1!192.168.0.2" https://www.example.com/
