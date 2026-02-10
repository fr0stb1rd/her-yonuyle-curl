# Zaman aşımları (Timeouts)

Ağ işlemleri, işlerin yürümesi için bir dizi hizmete ve ağa bağlı olduğundan, doğaları gereği oldukça güvenilmez veya belki de kırılgan işlemlerdir. Bu hizmetlerin kullanılabilirliği gidip gelebilir ve performansları da zaman zaman büyük ölçüde değişebilir.

TCP'nin tasarımı bile ağın, transferdeki katılımcılar tarafından mutlaka fark edilmeden uzun bir süre tamamen kopmasına izin verir.

Bunun sonucu olarak bazen İnternet transferleri uzun zaman alır. Ayrıca, curl'deki çoğu işlemin varsayılan olarak zaman aşımı yoktur.

## Harcamasına izin verilen maksimum süre

curl'e `-m / --max-time` ile, curl bir zaman aşımı hata koduyla (28) çıkmadan önce komut satırının harcamasına izin verdiğiniz maksimum süreyi saniye cinsinden söyleyin. Ayarlanan süre dolduğunda, curl o anda ne olursa olsun - veri aktarıyor olsa bile - çıkar. Bu gerçekten izin verilen maksimum süredir.

Verilen maksimum süre ondalık hassasiyetle belirtilebilir; `0.5` 500 milisaniye ve `2.37` 2370 milisaniye anlamına gelir.

Örnek:

    curl --max-time 5.5 https://example.com/

(Yerel ayarınız sayısal kesirleri ifade etmek için noktadan başka bir sembol kullanabilir.)

## Bağlanmak için asla bundan fazlasını harcama

`--connect-timeout`, curl'ün ana bilgisayara bağlanmaya çalışırken harcadığı süreyi sınırlar. Bağlantının tamamlandığı kabul edilmeden önce yapılan tüm gerekli adımların verilen zaman dilimi içinde tamamlanması gerekir. Verilen sürede bağlanılamaması, curl'ün bir zaman aşımı çıkış koduyla (28) çıkmasına neden olur.

Bir bağlantının başarılı kabul edilmesinden önce yapılan adımlar arasında DNS araması ve sonraki TCP, TLS veya QUIC el sıkışmaları bulunur.

Verilen maksimum bağlantı süresi ondalık hassasiyetle belirtilebilir; `0.5` 500 milisaniye ve `2.37` 2370 milisaniye anlamına gelir:

    curl --connect-timeout 2.37 https://example.com/
