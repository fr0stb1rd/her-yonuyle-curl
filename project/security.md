# Güvenlik

Güvenlik, biz curl projesi için birincil endişe kaynağıdır. Bunu ciddiye alıyoruz ve tüm protokollerin ve ilgili kodun güvenli ve emniyetli uygulamalarını sağlamak için çok çalışıyoruz. Güvenlikle ilgili bir sorun veya sadece şüphelenilen bir sorun hakkında bilgi alır almaz, onunla ilgileniriz ve bir sonraki bekleyen sürümden en geç olmamak üzere bir düzeltme ve güvenlik bildirimi sağlamaya çalışırız.

Sorumlu bir açıklama politikası (responsible disclosure policy) kullanıyoruz, yani güvenlik düzeltmeleri üzerinde halka açık olmayan bir şekilde tartışmayı ve çalışmayı tercih ediyoruz ve sorunu ve düzeltmeyi dünyaya duyurmadan birkaç gün önce openwall.org listesindeki satıcıları uyarıyoruz. Bu, kötü niyetli kişilerin düzeltilmiş bir sürüm dağıtılana kadar bir sorundan yararlanabilecekleri süreyi kısaltmak amacıyla yapılır.

## Geçmiş güvenlik sorunları

Yıllar boyunca güvenlikle ilgili sorunlardan payımıza düşeni aldık. Kullanıcılara yardımcı olmak için listelenen ve açıkça belirtilen tüm ayrıntılarla [her sorunu belgelemek](https://curl.se/docs/security.html) için çok çalışıyoruz. curl kullanıcıları, kendi curl sürümlerinin ve kullanım durumlarının hangi sorunlara karşı savunmasız olduğunu anlayabilmelidir.

Buna yardımcı olmak için, tüm güvenlik açıklarının hangi curl sürümlerini nasıl etkilediğini gösteren [bu şelale grafiğini (waterfall chart)](https://curl.se/docs/vulnerabilities.html) sunuyoruz ve bu projenin doğuşundan bu yana bilinen tüm güvenlik sorunlarının bu tam listesine sahibiz.

## Arka kapılar (Backdoors) ve tedarik zinciri riskleri

Dünyanın her yerinde milyarlarca kurulumda ve sayısız farklı ortamda kurulu ve çalışan libcurl ile, bir yerlere arka kapı (backdoor) yerleştirmek isteyen biri için ideal bir hedef olduğunun farkındayız.

Yeni veya eski bir bakıcı (maintainer), herhangi bir noktada masum ve iyi niyetli görünen ancak gizli kötü niyetli bir amacı olan bir değişiklik önerebilir.

Bu tür riskleri azaltmak için yerleşik prosedürler ve teknikler uyguluyoruz:

- **GitHub**. curl projesi, 2010'dan beri ana kaynak kod git deposu olarak <https://github.com/curl/curl> kullanmaktadır. Erişim güvenliğini yapılandırmamıza göre sağlamak için onların barındırmasına güveniyoruz.
- **2FA (İki Faktörlü Doğrulama) gerekli**. Saldırganların kimliklerini taklit etme ve kaynak kod değişikliklerini itmek (push) için kimlik bilgilerini kullanma riskini azaltmak amacıyla, git'e itme (push) erişimi olan tüm bakıcıların iki faktörlü doğrulamayı etkinleştirmesini zorunlu kılıyoruz. GitHub'ın 2FA kurulumuna güveniyoruz.
- **İncelemeler (Reviews)**. Projeye dahil edilmek üzere önerilen her katkı bir bakıcı tarafından incelenir. Tüm değişiklikler, ilgili tüm tarafların katılmasına izin vermek için her zaman halka açık olarak yapılır. Davet gerekmez. Tüm değişiklikler kabul edilmeden önce çok sayıda araç tarafından otomatik olarak kontrol edilir, test edilir ve taranır.
- **Okunabilir kod**. Kod stilimizi takip eden okunabilir koda inanıyoruz. Okuması kolaysa hata ayıklaması da kolaydır. Kodun okunması zorsa, okunması kolay olana kadar geliştirilmelidir. Okunması kolay kodla, kötü niyetli yükleri kaçırmak veya hain işlevleri gizlemek dayanılmaz derecede zordur.
- **Testler**. Sürekli büyüyen büyük bir test takımımız (test suite) var ve mevcut testleri bozan değişiklikleri kabul etmiyoruz ve yeni işlevselliğin yeni işlevsellik için yeni testler getirmesi gerekiyor. Mevcut işlevselliğin etkilenmediğinden emin olmak için önerilen her değişiklikte *birkaç yüz bin* test çalıştırıyoruz. Buna fuzzer'lar, statik kod analizörleri, hata enjektörleri ve daha fazlası dahildir.
- **İkili (binary) blob yok**. Sürüm kontrolünde, git deposunda saklanan tüm dosyalar okunabilir veya aksi takdirde küçük ve belgelenmiştir. Herhangi bir gizli şifrelenmiş yük için hiçbir yerde yer yoktur. İkili dosyaları tespit etmek için her değişiklikte tüm dosyalarda bir tarayıcı çalıştırıyoruz ve ikili görünmeye devam etmesi gereken birkaç dosya, bir sağlama toplamına (checksum) karşı manuel olarak inceleniyor ve doğrulanıyor.
- **Tekrarlanabilir derlemeler (Reproducible builds)**. curl sürümleri, curl web sitesinde (<https://curl.se>) barındırılan tarball'lar (arşiv dosyaları) olarak gönderilir. Yayın derlemelerimizi kolayca yeniden üretmek isteyen herkesin aynı görüntüleri oluşturmasına izin vermek için belgeler, docker kurulumları ve yapılandırmaları vb. sağlıyoruz - gönderdiğimiz şeyin yalnızca git deposundan alınan içerikler artı diğer doğru ve uygun şekilde oluşturulmuş içerikler olduğunu kanıtlıyoruz.
- **İmzalı commit'ler**. Son commit'lerin %90'ından fazlası - hepsi değil - kaynağı kanıtlamaya yardımcı olmak için imzalandı. Commit'leri imzalamak, işleyenler (committers) için henüz zorunlu bir gereklilik değildir ancak zamanla payı kademeli olarak artırmayı ve yakında zorunlu hale getirmeyi umuyoruz.
- **İmzalı sürümler**. Her sürüm, yüklenen her tarball Daniel tarafından imzalanır. Bu, dosyaların üretildiklerinden beri kurcalanmadığını kanıtlamaya yardımcı olur. Nispeten küçük ekstra koruma için ek karmaşıklık nedeniyle bunları birden fazla kişi tarafından imzalamamayı tercih ettik.
- **İmzalı etiketler (tags)**. Her sürüm, karşılık gelen bir *imzalı* etiketin ayarlandığı git ağacının tam durumundan oluşturulur. Sürüm etiketinin adı, sürüm sürümüyle aynıdır.
- **Tüm güvenlik açıklarını hızla düzeltin**. Bir güvenlik açığı raporu aldığımızda, bir sonraki bekleyen sürümde bir düzeltme oluştururuz ve göndeririz. Bazen daha önce planlanandan daha erken. Bir sürüm döngüsünden daha uzun sürmesi son derece nadirdir, ancak doğruluk ve kesinlik adına, doğru olanı elde etmek için araştırmaya zaman ayırma hakkımızı saklı tutarız. Düzeltilen her güvenlik açığıyla birlikte, sorunu ortaya çıkaran tam commit, kullanıcılar için öneriler ve daha fazlasını içeren kusurun ayrıntılı bir açıklamasını yayınlıyoruz. Ayrıca, güvenlik tavsiyeleri dünyaya duyurulur.
