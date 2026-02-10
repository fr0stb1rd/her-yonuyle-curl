# Farklılıklar

## İkili dosyalar (Binaries) ve farklı platformlar

Komut satırı aracı `curl`, *ikili (binary) yürütülebilir bir dosyadır*. curl projesi kendi başına ikili dosyalar dağıtmaz veya sağlamaz. İkili dosyalar büyük ölçüde sisteme özgüdür ve genellikle belirli sistem sürümlerine de bağlıdır.

Farklı platformlarda farklı kişiler tarafından, farklı derleme zamanı seçenekleriyle farklı üçüncü taraf kütüphaneler kullanılarak oluşturulan farklı curl sürümleri, aracın farklı yerlerde farklı özellikler sunmasına neden olur. Ayrıca, curl sürekli olarak geliştirilmektedir, bu nedenle aracın daha yeni sürümlerinin eski sürümlerden daha fazla ve daha iyi özelliklere sahip olması muhtemeldir.

## Komut satırları, tırnak işaretleri ve takma adlar (aliases)

curl'ün kullanılabileceği birçok farklı komut satırı ortamı, kabuğu ve istemi vardır. Hepsi, uyulması gereken kendi sınırlamaları, kuralları ve yönergeleriyle birlikte gelir. curl aracı, sorun çıkarmadan bunlardan herhangi biriyle çalışacak şekilde tasarlanmıştır ancak özel komut satırı sisteminizin başkalarının kullandığıyla veya başka şekilde belgelenenle uyuşmadığı zamanlar olabilir.

Komut satırı sistemlerinin farklılık gösterdiği bir yol, örneğin, boşlukları veya özel sembolleri gömmek gibi argümanların etrafına nasıl tırnak işareti koyabileceğinizdir. Çoğu Unix benzeri kabukta, tırnak içine alınmış dize içinde değişken genişletmelerine (variable expansions) izin verip vermemek istediğinize bağlı olarak çift tırnak (") ve tek tırnak (') kullanırsınız, ancak Windows'ta tek tırnak sürümü için destek yoktur.

Windows'taki PowerShell gibi bazı ortamlarda, komut satırı sisteminin yazarları daha iyisini bildiklerine karar verdiler ve bir komut satırı çalıştırıldığında öncelik alan bir takma ad sağlayarak, `curl` yazıldığında kullanıcının curl yerine başka bir aracı kullanmasına "yardımcı" olduzar. curl'ü PowerShell ile düzgün bir şekilde kullanmak için, uzantı dahil tam adını yazmanız gerekir: `curl.exe` veya takma adı kaldırın.

Farklı komut satırı ortamları farklı maksimum komut satırı uzunluklarına sahiptir ve kullanıcıları tek bir satıra ne kadar büyük miktarda veri konulacağını sınırlamaya zorlar. curl, [-K seçeneğini](configfile.md) kullanarak bir dosya veya stdin (standart girdi) aracılığıyla komut satırı seçenekleri sağlama yolu sunarak buna uyum sağlar.
