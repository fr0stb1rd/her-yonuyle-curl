# Sürekli Entegrasyon (Continuous Integration)

GitHub'daki curl projesine gönderilen her çekme isteği (pull request) için ve git deposundaki master dalına itilen (push) her taahhüt (commit) için, çok sayıda sanal makine çalışır, o kodu git'ten kontrol eder (check out), farklı seçeneklerle derler ve test paketini çalıştırır ve her şeyin iyi çalıştığından emin olur.

Linux, macOS, Windows, Solaris ve FreeBSD dahil olmak üzere çeşitli farklı işletim sistemlerinde CI işleri çalıştırıyoruz.

Birçok farklı arka ucu (ve bunların kombinasyonlarını) oluşturan ve test eden işler çalıştırıyoruz.

Farklı oluşturma yollarını kullanan işlerimiz var: autotools, cmake, Visual Studio, vb.

Dağıtım tarball'ının çalıştığını doğrularız.

Kaynak kodu çözümleyicileri çalıştırırız.

## Başarısız derlemeler

Ne yazık ki, dahil olan her şeyin karmaşıklığı nedeniyle genellikle "kalıcı başarısız" (permafailing) gibi görünen, işleri kalıcı olarak başarısızlığa uğratan bir veya iki CI işine sahibiz.

Onları öyle yapmamak için çok çalışıyoruz, ancak bu zor bir iş ve aksi takdirde tamamen yeşil olması gereken değişiklikler için bile sık sık kırmızı derlemeler görüyoruz.
