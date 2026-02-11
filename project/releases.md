# Sürümler

curl projesinde bir sürüm, kod deposunun (repository) master dalındaki (branch) tüm kaynak kodunu paketlemek, paketi imzalamak, kod deposundaki noktayı etiketlemek (tag) ve ardından dünyanın indirebilmesi için web sitesine koymak anlamına gelir.

curl'ün çalışabileceği tüm platformlar için tek bir kaynak kodu arşividir. Hem curl hem de libcurl için tek ve biricik pakettir.

Projeden asla herhangi bir curl veya libcurl _ikili dosyası (binaries)_ göndermeyiz, tek istisna: Windows kullanıcıları için derlenmiş resmi curl ikili dosyalarını barındırırız. İşletim sistemleriyle veya diğer indirme sitelerinde sağlanan diğer tüm paketlenmiş ikili dosyalar, proje dışındaki nazik gönüllüler tarafından yapılır.

Birkaç yıl öncesinden itibaren, sürümlerimizi sekiz haftalık bir döngüde yapmaya çabalıyoruz ve gerçekten ciddi ve acil bir sorun ortaya çıkmadıkça bu programa sadık kalıyoruz. Bir Çarşamba günü yayınlıyoruz ve ardından sekiz hafta sonra tekrar bir Çarşamba günü ve bu böyle devam ediyor. Durmaksızın.

Her sürüm için depodaki kaynak kodunu curl sürüm numarasıyla etiketliyoruz ve [değişiklik günlüğünü (changelog)](https://curl.se/changes.html) güncelliyoruz.

Şubat 2025'e kadar toplam 265 sürüm yaptık. Tüm sürüm geçmişi ve değişiklik günlüğü [curl sürüm günlüğümüzde (release log)](https://curl.se/docs/releases.html) mevcuttur.

## Sürüm döngüsü

![Görselleştirilmiş curl sürüm döngüsü](release-cycle.jpg)

## Günlük anlık görüntüler (snapshots)

Kaynak koda yapılan her bir değişiklik işlenir (committed) ve kaynak kod deposuna itilir (pushed). Bu depo github.com'da barındırılmaktadır ve bugünlerde git kullanmaktadır (ancak her zaman böyle değildi). Depodan curl derlerken, oluşturmanız ve ayarlamanız gereken birkaç şey vardır, bu da bazen insanların bazı sorunlar veya sadece sürtünme yaşamasına neden olur. Buna yardımcı olmak için günlük anlık görüntüler (snapshots) sağlıyoruz.

Günlük anlık görüntüler, sanki o noktada bir sürüm yapılmış gibi günlük olarak oluşturulur (zekice isimlendirme, değil mi?). Tüm kaynak kodunu ve normalde bir sürümün parçası olan tüm dosyaları içeren bir paket üretir ve ilgili kişilerin test etmek, denemek veya her neyse en son kodu almasına izin vermek için [bu özel yere](https://curl.se/snapshots/) yükler.

Anlık görüntüler silinene kadar yaklaşık 20 gün saklanır.
