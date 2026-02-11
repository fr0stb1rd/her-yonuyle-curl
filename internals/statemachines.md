# Durum makineleri (State machines)

Baştan sona bloklamayan davranışı kolaylaştırmak için, curl kaynağı durum makineleriyle doludur. Olabildiğince çok veri üzerinde çalışın ve durum makinesini mevcut olana göre gidebileceği yere sürün ve işlevlerin daha sonra durum makinesini daha da ileri götürebilecek daha fazla veri geldiğinde o noktadan devam etmesine izin verin.

Belirli bir transfer için birçok farklı seviyede bu tür durumlar vardır ve her bir protokol için kodun kendi durum makineleri seti olabilir.

## mstate

Birincil durumlardan biri, easy handle'ın tuttuğu ana transfer "modu"dur; bu, mevcut transferin çözümlenip çözümlenmediğini, bir çözümleme bekleyip beklemediğini, bağlanıp bağlanmadığını, bir bağlantı bekleyip beklemediğini, bir istek yayınlayıp yayınlamadığını, bir transfer yapıp yapmadığını vb. söyler (`lib/multihandle.h` içindeki `CURLMstate` numaralandırmasına bakın). libcurl ile yapılan her transferin ilişkili bir easy handle'ı vardır ve her easy handle o durum makinesini çalıştırır.

Aşağıdaki resim tüm durumları ve olası durum geçişlerini göstermektedir. Aşağıdaki diğer açıklamalara bakın.

![libcurl transfer durum makinesi](slide-transfer-state-machine.jpg)

Tüm transferler **INIT** ile başlar ve **MSGSENT** ile biter

**sarı**: ilk kurulum durumları

**mavi**: isimleri çözümleme ve bağlantıyı kurma

**yeşil**: transferi başlatma ve kurma

**beyaz**: transfer

**kırmızı**: transfer sonrası
