# Vekil sunucu ortam değişkenleri

curl, bir vekil sunucunun kullanılması istenip istenmediğini görmek için çalışmadan önce özel olarak adlandırılmış ortam değişkenlerinin varlığını kontrol eder.

Vekil sunucu ana bilgisayar adını tutmak için `[scheme]_proxy` adlı bir değişken ayarlayarak vekil sunucuyu belirtirsiniz (ana bilgisayarı `-x` ile belirttiğiniz şekilde). Bir HTTP sunucusuna erişirken curl'e bir vekil sunucu kullanmasını söylemek istiyorsanız `http_proxy` ortam değişkenini ayarlarsınız. Şöyle:

    http_proxy=http://proxy.example.com:80
    curl -v www.example.com

Yukarıdaki örnek HTTP'yi gösterse de, elbette `ftp_proxy`, `https_proxy` vb. de ayarlayabilirsiniz. `http_proxy` dışındaki tüm bu vekil sunucu ortam değişkeni adları, `HTTPS_PROXY` gibi büyük harflerle de belirtilebilir.

*Tüm* protokolleri kontrol eden tek bir değişken ayarlamak için `ALL_PROXY` mevcuttur. Belirli bir protokol değişkeni varsa, o önceliklidir.

## Vekil sunucu yok (No proxy)

Bazen normalde kullanılacak vekil sunucudan geçmekten hariç tutulması gereken bir veya birkaç ana bilgisayar adının olduğu bir duruma düşersiniz. Bu daha sonra `NO_PROXY` değişkeni ile yapılır. Bunu, erişilirken bir vekil sunucu kullanmaması gereken ana bilgisayar adlarının virgülle ayrılmış bir listesine ayarlayın. `NO_PROXY`'yi tüm ana bilgisayarlarla eşleşecek şekilde tek bir yıldız ('\*') olarak ayarlayabilirsiniz.

Hariç tutma listesindeki bir ad bir nokta (`.`) ile başlıyorsa, ad o tüm etki alanıyla eşleşir. Örneğin `.example.com` hem `www.example.com` hem de `home.example.com` ile eşleşir ancak `nonexample.com` ile eşleşmez.

`NO_PROXY` değişkenine bir alternatif olarak, aynı amaca hizmet eden ve aynı şekilde çalışan bir `--noproxy` komut satırı seçeneği de vardır.

curl 7.86.0'dan bu yana, bir kullanıcı CIDR gösterimini kullanarak bir IP ağını hariç tutabilir: eşleşecek ağın bit boyutunu belirtmek için bir IP adresine bir eğik çizgi ve bit sayısı ekleyin. Örneğin, `192.168.0.0/16` desenini sağlayarak `192.168` ile başlayan tüm 16 bitlik ağla eşleştirin.

## `http_proxy` sadece küçük harfle

Vekil sunucu ortam değişkenlerinin HTTP sürümü diğerlerinden farklı muamele görür. Kullanıcıların bir HTTP sunucusu tarafından çağrıldığında bir sunucuda komut dosyaları çalıştırmasına izin veren CGI protokolü nedeniyle yalnızca küçük harfli sürümünde kabul edilir. Bir CGI betiği bir sunucu tarafından çağrıldığında, istekteki gelen başlıklara dayalı olarak betik için otomatik olarak ortam değişkenleri oluşturur. Bu ortam değişkenleri büyük harf `HTTP_` ile öne eklenir.

Bu nedenle `Proxy: yada` gibi bir istek başlığı kullanan bir HTTP sunucusuna gelen bir istek, CGI betiği başlatılmadan önce `yada` içerecek şekilde ayarlanmış `HTTP_PROXY` ortam değişkenini oluşturur. Böyle bir CGI betiği curl çalıştırırsa, curl'ün bunu kullanılacak bir vekil sunucu olarak görmemesi önemlidir.

Bu ortam değişkeninin büyük harfli sürümünü kabul etmek, zaman içinde birçok yazılımda birçok güvenlik sorununun kaynağı olmuştur.
