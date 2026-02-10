# Hata bildirme

Geliştirme ekibi çok fazla test yapar. Tüm kodu çalıştırmak ve her şeyin beklendiği gibi çalıştığından emin olmak için her gün sayısız platformda sık sık çalıştırılan koca bir test takımımız (test suite) var.

Yine de, işlerin olması gerektiği gibi çalışmadığı zamanlar olur ve insanların bunu bize bildirmesine güveniriz.

## Hata (bug) bir sorundur

Herhangi bir sorun bir hata (bug) olarak kabul edilebilir. Kılavuzda bir şeyi anlamanızı engelleyen garip bir ifade bir hatadır. Birden fazla seçeneği birleştirmenin şaşırtıcı bir yan etkisi bir hata olabilir — ya da belki daha iyi belgelenmesi gerekir? Belki de seçenek hiç beklediğiniz şeyi yapmıyordur? Bu bir sorundur ve düzeltmemiz gerekir.

## Düzeltilmesi için sorunların bilinmesi gerekir

Bu kulağa kolay ve karmaşık olmayan gelebilir ancak bizim ve diğer projelerde temel bir gerçektir. Sırf eski bir proje olması ve binlerce kullanıcısı olması, geliştirme ekibinin az önce tökezlediğiniz sorundan haberdar olduğu anlamına gelmez. Belki kullanıcılar ayrıntılara sizin kadar dikkat etmemiştir, ya da belki de başka hiç kimse için tetiklenmemiştir.

Sorun yaşayan kullanıcıların bunları bildirmesine güveniyoruz. Bunları düzeltebilmemiz için varlıklarından haberdar olmamız gerekir.

## Sorunları düzeltme

Yazılım mühendisliği, büyük ölçüde, sorunları düzeltmekle ilgilidir. Bir sorunu düzeltmek için bir geliştiricinin onu nasıl tekrarlayacağını anlaması gerekir ve bunu yapmak için hangi koşullar kümesinin sorunu tetiklediğinin söylenmesi gerekir.

## İyi bir hata raporu

İyi bir rapor, ne olduğunu ve ne olacağını düşündüğünüzü açıklar. Bize kullandığınız farklı bileşenlerin tam olarak hangi sürümlerini kullandığınızı söyleyin ve soruna ulaşmak için ne yaptığınızı adım adım anlatın.

Bir hata raporu gönderdikten sonra, geliştiricinin şüphelileri daraltabilmesi ve sorununuzun doğru bir şekilde konumlandırıldığından emin olabilmesi için takip soruları veya belki de çeşitli şeyleri denemeniz yönünde istekler olmasını bekleyebilirsiniz.

Gönderilen ve ardından gönderen tarafından terk edilen bir hata raporu, geliştirici onu anlamayı başaramazsa, yeniden üretemezse veya üzerinde çalışırken başka sorunlarla karşılaşırsa kapatılma riskiyle karşı karşıya kalır. Raporunuzu terk etmeyin.

curl hatalarını [GitHub'daki curl hata takip sisteminde](https://github.com/curl/curl/issues) bildirin.

## Test etme

Yazılımı kapsamlı ve düzgün bir şekilde test etmek çok iştir. Düzinelerce işletim sisteminde ve CPU mimarisinde çalışan, kendi hata kümelerine ve özelliklerin yorumlarına sahip sunucu uygulamalarıyla çalışan yazılımları test etmek daha da fazla iştir.

curl projesi, mevcut tüm test durumları üzerinde yineleme yapan, her testi çalıştıran ve sonucun doğru olduğunu ve bellek sızıntısı veya protokol katmanında şüpheli bir şey gibi başka bir sorunun olmadığını doğrulayan bir test takımına sahiptir.

Test takımı, curl'ü kendiniz derledikten sonra çalıştırılmak üzere tasarlanmıştır. Ayrıca, en son commit'lerin test edildiğinden emin olmak için test takımını günde birkaç kez otomatik olarak çalıştırarak yardımcı olan bir dizi gönüllü de vardır. Bu sayede en kötü kusurları, tanıtılmalarından kısa bir süre sonra keşfederiz.

Her şeyi test etmiyoruz ve test etmeye çalıştığımızda bile her zaman aradan sızan ince hatalar oluyor, bazıları ancak yıllar sonra keşfediliyor.

Farklı sistemlerin doğası ve İnternet'teki garip kullanım durumları nedeniyle, eninde sonunda en iyi testlerin bazıları, kullanıcılar kodu kendi kullanım durumlarını gerçekleştirmek için çalıştırdıklarında yapılır.

Test takımıyla ilgili bir başka sınırlayıcı faktör de, test kurulumunun kendisinin curl ve libcurl'den daha az taşınabilir olmasıdır, bu nedenle aslında curl'ün iyi çalıştığı ancak test takımının hiç çalışamadığı platformlar vardır.
