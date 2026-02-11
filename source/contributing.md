# Katkıda bulunma

Katkıda bulunmak, yardım etmek demektir.

Projeye herhangi bir şekilde katkıda bulunduğunuzda—kod, dokümantasyon, hata düzeltmeleri, öneriler veya sadece iyi tavsiyeler—bunu izinle yaptığınızı ve bize bu katkıyı sağlarken herhangi bir sözleşmeyi veya yasayı ihlal etmediğinizi varsayıyoruz. İzniniz yoksa, katkıda bulunmayın.

curl gibi bir projeye katkıda bulunmak birçok farklı şey olabilir. Kaynak kodu ürünleri oluşturmak için gereken şey olsa da, aynı zamanda iyi dokümantasyona, test etmeye (hem test kodu hem de test altyapısı), web içeriğine, kullanıcı desteğine ve daha fazlasına da güveniyoruz.

Değişikliklerinizi veya önerilerinizi ekebe gönderin ve birlikte çalışarak sorunları çözebilir, işlevselliği geliştirebilir, belgeleri netleştirebilir, özellikler ekleyebilir veya yardım ettiğiniz diğer her şeyin doğru yere ulaşmasını sağlayabiliriz. İyileştirilmiş kodun ve belgelerin kaynak ağacına düzgün bir şekilde birleştirildiğinden (merge) ve diğer katkı türlerinin uygun şekilde alındığından emin oluruz.

Katkılarınızı bir [posta listesine](../project/comm.md) gönderin, bir sorun (issue) açın veya bir çekme isteği (pull request) gönderin.

## Öneriler

Fikirler kolaydır, uygulamalar zordur. Evet, ne yapılması gerektiği ve nasıl yapılması gerektiği konusundaki iyi fikirleri ve önerileri takdir ediyoruz, ancak fikri gerçeğe dönüştürmeye katılmaya gönüllü olursanız, fikirlerin gerçek özelliklere dönüşme şansı önemli ölçüde artar.

Zaten `TODO` belgesinde fikirleri topluyoruz ve genel olarak popüler ağ protokollerindeki mevcut trendlerin farkındayız, bu yüzden genellikle bunları bize hatırlatmanıza gerek yoktur.

## Ne eklenmeli

curl veya libcurl'e herhangi bir şey eklemek için en iyi yaklaşım, elbette, önce fikri ve öneriyi curl proje ekibi üyelerine getirmek ve onlarla fikrin dahil edilmesinin mümkün olup olmadığını ve ardından bir uygulamanın en iyi nasıl yapılacağını—ve istediğiniz buysa kaynak kodu deposuna birleştirilmek için mümkün olan en iyi şekilde nasıl yapılacağını—tartışmaktır.

Proje genellikle mevcut protokoller için desteği iyileştiren işlevleri, özellikle popüler istemcilerin veya tarayıcıların sahip olduğu ancak curl'ün hala eksik olduğu özellikleri onaylar.

Elbette, projeye kod olmayan içerikler de ekleyebilirsiniz; dokümantasyon, grafikler veya web sitesi içerikleri gibi, ancak genel kurallar bunlar için de aynı şekilde geçerlidir.

Sahip olduğunuz bir sorunu veya başkalarının bildirdiği bir sorunu düzeltiyorsanız, düzeltmelerinizi almaktan ve bunları mümkün olan en kısa sürede birleştirmekten heyecan duyarız.

## Ne eklenmemeli

Hangi özellikleri ekleyip ekleyemeyeceğinizi veya neleri asla kabul etmeyeceğimizi söyleyen iyi kurallar yoktur, ancak daha az sürtünme yaşamak ve daha hızlı başarılı olmak için kaçınmanız gereken birkaç şeyden bahsetmeye çalışayım:

- Önce devasa bir yama (patch) yazıp sonra tartışmak için listeye göndermeyin. Her zaman listede tartışarak başlayın ve tasarımınız ve yaklaşımınız hakkında geri bildirim almak için ilk inceleme isteklerinizi erken gönderin. Bu, sonunda yeniden yazılması gerekebilecek bir yolda zaman kaybetmenizi önler.

- Koda yeni şeyler eklerken, zaten var olan stili ve mimariyi takip etmeniz gerekir. Normal transfer kodu yoluna (code path) kod eklediğinizde, örneğin, engellemeyen (non-blocking) bir şekilde asenkron olarak çalışması gerekir. Engelleme davranışları getiren yeni kodları kabul etmiyoruz—henüz kaldıramadığımız bunlardan zaten çok fazla var.

- Çalıştırmadığınız platformlarda veya bilmediğiniz mimarilerde çalışmama riski yüksek olan hızlı hack'ler veya kirli çözümler. Aceleniz olup olmaması veya sizin için çalışıyor olması umrumuzda değil. Yüksek riskli kodu veya okunması veya anlaşılması zor kodu kabul etmiyoruz.

- Derlemeyi (build) bozan kod. Elbette, bazen belirli alanlara, yeni işlevselliğin belki de belirli bir 3. taraf kütüphanesine veya belirli bir işletim sistemine ve benzerlerine bağlı olmasını sağlayan kod eklememiz gerektiğini kabul ediyoruz, ancak bunu **asla** diğer tüm sistemler pahasına yapamayız. Derlemeyi bozmuyoruz ve tüm testlerin başarıyla çalışmaya devam ettiğinden emin oluyoruz.

## git

Tercih ettiğimiz kaynak kontrol aracımız [git](https://git-scm.com/)'tir.

git bazen öğrenmesi ve ustalaşması en kolay araç olmasa da, sıradan bir geliştiricinin ve katkıda bulunan kişinin bilmesi gereken tüm temel adımlar basittir ve öğrenmesi çok fazla zaman veya çaba gerektirmez.

Bu kitap size git öğrenmenizde yardımcı olmaz. Bu devirde tüm yazılım geliştiricileri zaten git öğrenmelidir.

curl git ağacına [https://github.com/curl/curl](https://github.com/curl/curl) adresindeki GitHub sayfamızdan bir web tarayıcısı ile göz atılabilir.

curl kaynak kodunu git'ten çekmek (check out) için şu şekilde klonlayabilirsiniz:

    git clone https://github.com/curl/curl.git

## Çekme isteği (Pull request)

Kendi değişikliklerinizi yapmanın ve bunları projeye geri katkıda bulunmanın popüler ve kullanışlı bir yolu, GitHub üzerinde sözde bir çekme isteği (pull request) yapmaktır.

İlk olarak, Github web sitesinde kaynak ağacının kendi sürümünü, yani bir çatalını (fork) oluşturursunuz. Bu sayede, yerel bir kopyaya klonlayabileceğiniz curl git ağacının kendi sürümüne sahip olursunuz.

Kendi yerel kopyanızı düzenler, değişiklikleri işler (commit), bunları Github'daki git deposuna gönderir (push) ve ardından Github web sitesinde orijinal curl deposunun yerel depo klonuna yaptığınız değişikliklere dayanarak bir çekme isteği oluşturmayı seçebilirsiniz.

Çekme isteği için tasarladığınız çalışmanızı master dalında (branch) değil, ayrı bir özel dalda yapmanızı öneririz; bu sadece bir çekme isteğini güncellemenizi, örneğin incelemeden sonra veya bunun bir çıkmaz sokak olduğunu fark edip sadece çöpe atmaya karar verirseniz, daha kolay hale getirmek içindir.

## Posta listesi için bir yama yapın

Bir çekme isteği yapmamayı tercih etseniz ancak yamayı curl-library posta listesine gönderme şeklindeki eski moda ve güvenilir yöntemi tercih etseniz bile, yerel bir git dalında çalışmak ve değişikliklerinizi orada işlemek (commit) yine de iyi bir uygulamadır.

Bir dal, değiştirmeler gerektiğinde düzenlemeyi ve yeniden temellendirmeyi (rebase) kolaylaştırır ve yukarı akışta (upstream) güncellemeler olduğunda master dalıyla senkronize kalmayı kolaylaştırır.

İşlemeleriniz (commits) posta listesine gönderilecek kadar iyi olduğunda, `git format-patch` ile yamalar oluşturur ve gönderirsiniz. Daha da meraklı kullanıcılar doğrudan `git send-email`'e gider ve e-postanın kendisini git'e gönderttirir.

## git işleme (commit) stili

Git'e bir yama işlediğinizde (commit), ona işlediğiniz değişikliği açıklayan bir işleme mesajı verirsiniz. Projede kullanmanızı istediğimiz belirli bir stilimiz var:

    [alan]: [ana etkiyi açıklayan kısa satır]

    [yukarıdaki tek satırı geri kalanından boş bir satırla ayırın]

    [bu değişikliğin neden yapıldığına ve muhtemelen neleri düzelttiğine
    ve ilgili diğer her şeye dair mümkün olduğunca çok şeyi açıklayan,
    72 sütundan geniş olmayan tam açıklama]

    [Bug: raporun kaynağına bağlantı veya daha fazla ilgili tartışma]
    [Reported-by: John Doe—raporlayan kişiye atıf]
    [whatever-else-by: tüm yardımcılara, bulanlara, yapanlara atıf]

Başkasının çalışmasını işliyorsanız `git commit --author="Jane Doe <jane@example.com>"` kullanmayı unutmayın ve aşağıdaki komutlarla işlemeden önce git'te kendi Github kullanıcı adınızın ve e-postanızın doğru ayarlandığından emin olun:

    git config --global user.name "johndoe"
    git config --global user.email "johndoe@example.com"


Yazar ve \*-by: satırları elbette projede uygun krediyi verdiğimizden emin olmak içindir. Başkasının çalışmasını, nereden geldiğini açıkça belirtmeden almak istemiyoruz. Doğru krediyi vermek son derece önemlidir.

## İçeriye neyin gireceğine kim karar verir?

İlk olarak, herkes için açık olmayabilir ancak işlemeleri (commits) gerçek resmi git deposuna birleştirebilen (merge) sadece sınırlı sayıda insan vardır. Onlara çekirdek ekip (core team) diyelim.

Diğer herkes değişiklikleri işleyip (commit) gönderebileceği (push), çevrimiçi barındırabileceği ve kendi curl sürümlerini oluşturabileceği kendi curl deposunu çatallayabilir (fork), ancak değişiklikleri *resmi* depoya almak için güvenilir bir kişi tarafından gönderilmeleri (push) gerekir.

Çekirdek ekip, birkaç yıldır buralarda olan, yetenekli geliştiriciler olduklarını ve bu projede yaptığımız geliştirme değerlerini ve stilini tam olarak kavradıklarını gösteren küçük bir curl geliştiricileri kümesidir. Onlar [Geliştirme ekibi](../project/devteam.md) bölümünde listelenen kişilerden bazılarıdır.

Her zaman bir tartışmayı posta listesine getirebilir ve değişikliklerinizin neden kabul edilmesi gerektiğini tartışabilir veya belki de içeri giren diğer değişikliklere itiraz edebilirsiniz vb. Kendinizi veya başka birini "gönderme hakları" (push rights) verilmesi ve o ekipteki seçilmiş birkaç kişiden biri olması için bile önerebilirsiniz.

Daniel proje lideri olmaya devam ediyor ve nadiren ihtiyaç duyulsa da, her iki yöne de sallanmayan veya fikir birliğine varılamayan tartışmalarda son sözü o söylüyor.
