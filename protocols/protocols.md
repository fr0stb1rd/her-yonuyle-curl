# Protokoller

Verilerin gönderilmesini istemek için kullanılan dile — her iki yönde de — **protokol** denir. Protokol tam olarak sunucudan verilerin nasıl isteneceğini veya sunucuya veri geldiğini nasıl söyleyeceğini açıklar.

Protokoller genellikle her bir protokolün tam olarak nasıl çalıştığını açıklayan RFC belgelerini barındıran IETF ([İnternet Mühendisliği Görev Gücü](https://www.ietf.org/)) tarafından tanımlanır: İstemcilerin ve sunucuların nasıl davranması gerektiği, ne göndereceği vb.

## curl hangi protokolleri destekler?

curl, her iki yönde veya her iki yönde de veri transferine izin veren protokolleri destekler. Ayrıca genellikle kendimizi, curl transferi belirleyen girdi anahtarı olarak öncelikle URL'lerle (gerçekte URI'ler) çalıştığı için, RFC'de açıklanan bir URI formatına sahip olan veya en azından biraz yaygın olarak kullanılan protokollerle sınırlandırıyoruz.

En son curl (bu yazının yazıldığı sırada) şu protokolleri desteklemektedir:

DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS, WSS

İşleri daha da karmaşık hale getirmek için, protokoller genellikle farklı sürümlerde veya çeşitlerde de bulunur.

## Orada başka hangi protokoller var?

Dünya hem eski hem de yeni protokollerle doludur. Eski protokoller terk edilir ve düşürülür ve yenileri tanıtılır. Hiçbir zaman bir istikrar durumu yoktur ancak durum günden güne ve yıldan yıla değişir. Gelecekte yukarıdaki listeye eklenecek yeni protokoller olacağından ve halihazırda listelenen protokollerin yeni sürümleri olacağından emin olabilirsiniz.

Elbette, curl'ün henüz desteklemediği başka protokoller de mevcuttur. Genel curl paradigmalarına uyan daha fazla protokolü desteklemeye açığız, sadece geliştiricilerin onlar için gerekli kod ayarlamalarını yazmasına ihtiyacımız var.

## Protokoller nasıl geliştirilir?

Hem mevcut protokollerin yeni sürümleri hem de tamamen yeni protokoller genellikle mevcut olanların yeterince iyi olmadığını düşünen kişiler veya ekipler tarafından geliştirilir. Onlarla ilgili bir şey, onları belirli bir kullanım durumu için uygun hale getirmez veya belki de işleri iyileştirmek için uygulanabilecek yeni bir fikir ortaya çıkmıştır.

Elbette, hiç kimsenin kendi arka bahçesinde tamamen kendi zevkine göre bir protokol geliştirmesini engelleyen hiçbir şey yoktur, ancak büyük protokoller genellikle oldukça erken bir aşamada IETF'e getirilir; burada tartışılır, iyileştirilir, tartışılır ve parlatılır ve sonunda, ideal olarak, yayınlanmış bir RFC belgesine dönüştürülür.

Yazılım geliştiricileri daha sonra RFC özelliklerini (spesifikasyonlarını) okur ve kodlarını bu belgelerdeki kelimelerin yorumlarına dayanarak dünyaya dağıtırlar. Bazen bazı özelliklerin çok farklı yorumlara konu olduğu veya bazen mühendislerin sadece tembel olduğu ve özelliklerdeki sağlam tavsiyeleri görmezden geldiği ve uymayan bir şey dağıttığı ortaya çıkar.
Bu nedenle, diğer özellik uygulamalarıyla birlikte çalışan yazılım yazmak zor bir iş olabilir.

## Protokoller ne kadar değişir?

Yazılım gibi, protokol özellikleri de sık sık güncellenir ve yeni protokol sürümleri oluşturulur.

Çoğu protokol, zamanla yeni uzantıların (extensions) ortaya çıkmasına izin veren bir miktar genişletilebilirlik sağlar; desteklenmesi mantıklı olan uzantılar.

Bir protokolün yorumu, özellik (spec) aynı kalsa bile bazen değişir.

Bu bölümde bahsedilen protokollerin hepsi *Uygulama Protokolleri*'dir (Application Protocols), yani TCP, UDP ve TLS gibi daha düşük seviyeli protokoller üzerinden aktarılırlar. Ayrıca kendileri de zamanla değişen, yeni özellikler alan ve saldırıya uğrayan protokollerdir; böylece güvenlik vb. ile başa çıkmanın yeni yolları curl'ü uyum sağlamaya ve değişmeye zorlar.

## Standartlara uymak ve kimin haklı olduğu hakkında

Genellikle, belirli protokoller için verilerin nasıl gönderileceğini ve alınacağını bize söyleyen protokol özellikleri vardır. İzlediğimiz protokol özellikleri, IETF tarafından bir araya getirilen ve yayınlanan RFC'lerdir.

Bazı protokoller son bir RFC'de düzgün bir şekilde belgelenmemiştir; örneğin, uygulamamızın dayandığı bir Internet-draft (taslak) olan ve son mevcut olan bile olmayan SFTP gibi.

Bununla birlikte, protokoller iki tarafça konuşulur ve herhangi bir konuşmada olduğu gibi, bir şeyi anlamanın veya bir özellikteki verilen talimatları yorumlamanın iki tarafı vardır. Ayrıca, birçok ağ yazılımı, yazarların özelliğe çok dikkat etmemesiyle yazılır, bu nedenle bazı kısayollar alırlar veya belki de metni farklı yorumlamışlardır. Bazen hatalar ve bug'lar bile yazılımın özellik tarafından zorunlu kılınmayan ve bazen özelliklerde tamamen yasaklanan şekillerde davranmasına neden olur.

curl projesinde, yayınlanan özellikleri, başka bir şey öğrenene kadar nasıl hareket edileceğine dair kurallar olarak kullanırız. Popüler alternatif uygulamalar, özelliğin söylediğini düşündüğümüzden farklı davranıyorsa ve bu alternatif davranış büyük İnternet'te yaygın olarak işe yarıyorsa, o zaman muhtemelen adım değiştiririz ve bunun yerine diğerleri gibi davranmaya karar veririz. Bir sunucu, özelliği izlediğimizi düşündüğümüzde bizimle konuşmayı reddederse ancak kuralları çok az esnettiğimizde iyi çalışıyorsa, o zaman muhtemelen onları tam olarak o şekilde esnetiriz—eğer diğer uygulamalarla hala başarılı bir şekilde çalışabilirsek.

Sonuçta, bu kişisel bir karardır ve bir şartnamenin ve gerçek dünyanın uyuşmadığını düşündüğümüz her durumda tartışmaya açıktır.

En kötü durumlarda, uygulama geliştiricilerinin ve curl kullanıcılarının curl'ün ne yapması gerektiği konusunda son söze sahip olmalarını sağlamak için seçenekler sunuyoruz. En kötüsü diyorum çünkü kullanıcılardan bu kararları vermelerini istemek genellikle gerçekten zordur çünkü genellikle karmaşık ayrıntılar ve gariplikler içerir ve kullanıcılardan çok şey istenir. Bu tür protokol kararlarını kullanıcılara itmekten kaçınmak için her zaman elimizden gelenin en iyisini yapmalıyız.
