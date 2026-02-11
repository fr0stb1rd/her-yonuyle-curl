# Yerel port numarası

Yerel uçta bir IP adresi ve port numarası ile uzak uçta bir IP adresi ve port numarası arasında bir TCP bağlantısı oluşturulur. Uzak port numarası URL'de belirtilebilir ve genellikle hangi hizmeti hedeflediğinizi belirlemenize yardımcı olur.

Yerel port numarası genellikle ağ yığını tarafından TCP bağlantınıza rastgele atanır ve normalde bu konuda çok fazla düşünmeniz gerekmez. Ancak, bazı durumlarda kendinizi giden bağlantıları kurmasına izin verilebilecek kaynak port numaralarına kısıtlamalar getiren ağ ekipmanı, güvenlik duvarları veya benzeri kurulumların arkasında bulursunuz.

Bunun gibi durumlar için, curl'ün bağlantıyı hangi yerel portlara bağlaması gerektiğini belirtebilirsiniz. Kullanılacak tek bir port numarası veya bir port aralığı belirtebilirsiniz. Portlar kıt kaynaklar olduğundan ve istediğiniz tam port zaten kullanımda olabileceğinden bir aralık kullanmanızı öneririz. curl'den sizin için alamayacağı bir yerel port numarası (veya aralığı) isterseniz, bir hatayla çıkar.

Ayrıca, çoğu işletim sisteminde daha yüksek bir ayrıcalık düzeyine (root) sahip olmadan 1024'ün altındaki port numaralarına bağlanamazsınız ve genel olarak kaçınabilirseniz curl'ü root olarak çalıştırmamanızı öneririz.

Bu HTTPS sayfasını alırken curl'den 4000 ile 4200 arasında bir yerel port numarası kullanmasını isteyin:

    curl --local-port 4000-4200 https://example.com/
