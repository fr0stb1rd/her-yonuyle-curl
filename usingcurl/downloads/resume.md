# Devam ettirme ve aralıklar

Bir indirmeyi devam ettirmek, önce yerel olarak neyin mevcut olduğunun boyutunu kontrol etmek ve ardından sunucudan geri kalanını göndermesini istemek anlamına gelir, böylece eklenebilir. curl ayrıca aslında yerel olarak önceden mevcut bir şeye sahip olmadan transferi özel bir noktada devam ettirmeye izin verir.

curl, çeşitli protokollerde devam ettirilen indirmeleri destekler. Transferin nereden başlayacağını, nereden başlayacağını belirten düz sayısal bir bayt sayacı ofseti alan veya curl'den bildiklerine dayanarak bunu kendisinin bulmasını isteyen `-` dizesini alan `-C, --continue-at` seçeneğiyle söyleyin. `-` kullanıldığında, curl yerel olarak ne kadar verinin mevcut olduğunu anlamak için hedef dosya adını kullanır ve sunucudan daha fazla veri isterken bunu bir ofset olarak kullanır.

Bayt ofseti 100'den bir FTP dosyası indirmeye başlamak için:

    curl --continue-at 100 ftp://example.com/bigfile

Daha önce kesintiye uğramış bir indirmeyi indirmeye devam edin:

    curl --continue-at - http://example.com/bigfile -O

Bunun yerine uzak kaynaktan sadece belirli bir bayt aralığının transfer edilmesini istiyorsanız, sadece bunu isteyebilirsiniz. Örneğin, tüm devasa uzak dosyayı indirmek zorunda kalmamak için ofset 100'den sadece 1000 bayt istediğinizde:

    curl --range 100-1099 http://example.com/bigfile
