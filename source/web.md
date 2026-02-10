# Web sitesi

curl web sitesinin çoğu, genellikle aynı kişiler için ilginç olmadığından ve gönderme haklarına (push rights) sahip farklı bir kişi listesini sürdürebildiğimizden vb., kaynak kodu deposundan ayrı olsa da, genel bir git deposunda da mevcuttur.

Web sitesi git deposu GitHub'da şu URL'de mevcuttur:
[https://github.com/curl/curl-www](https://github.com/curl/curl-www) ve web kodunun bir kopyasını şu şekilde klonlayabilirsiniz:

    git clone https://github.com/curl/curl-www.git

## Web sitesini oluşturma (Building the web)

Web sitesi, çoğunlukla bir dizi kaynak dosyadan statik HTML dosyaları oluşturan özel yapım bir kurulumdur. Kaynak dosyalar, [fcpp](https://daniel.haxx.se/projects/fcpp/) adı verilen güçlendirilmiş bir C önişlemcisi ve bir dizi perl komut dosyası ile ön işleme tabi tutulur. Kılavuz (man) sayfaları, [roffit](https://daniel.haxx.se/projects/roffit/) ile HTML'e dönüştürülür. fcpp, perl, roffit, make ve curl'ün $PATH yolunuzda olduğundan emin olun.

Git deposunu ilk kez klonladığınızda, bir sembolik bağ ve bazı ilk yerel dosyaların kurulumunu almak için `sh bootstrap.sh` komutunu bir kez çağırın ve ardından kaynak kök ağacında `make` komutunu çağırarak web sitesini yerel olarak oluşturabilirsiniz.

Bunun sizi tam bir web sitesi aynası (mirror) yapmadığını, bazı komut dosyalarının ve dosyaların yalnızca gerçek sitede mevcut olduğunu unutmayın, ancak çoğu HTML sayfasını yerel olarak görüntülemenize izin verecek kadarını vermelidir.

## Yerel bir klon çalıştırın

Web sitesi, üretimdeki resmi siteye göndermeden (push) önce değişikliklere göz atmak ve test etmek için yerel bir kopyayı barındırmayı kolay ve rahat hale getirecek bir şekilde oluşturulmuştur. Daha sonra siteye `curl.local` adını vermenizi ve bunu yerel `/etc/hosts` dosyanıza bir giriş olarak eklemenizi öneririz. Ardından HTTP sunucunuzun belge kökünü (document root) curl-www kaynak kodu köküne yönlendirin.

## Web sitesi altyapısı

- Halka açık curl web sitesi [curl.se](https://curl.se) adresinde barındırılmaktadır.
- Alan adı **Daniel Stenberg**'e aittir
- Ana kaynak makine **Haxx** tarafından desteklenmektedir (sponsor)
- curl.se alanı, **Kirei** tarafından desteklenen herhangi bir noktaya dağıtılmış (anycast distributed) DNS sunucuları tarafından sunulmaktadır
- Site dünyaya **Fastly** tarafından işletilen bir CDN aracılığıyla sunulmaktadır
- Web sitesi her N dakikada bir GitHub'dan kendini günceller. CDN ön uçları içeriği Y dakika önbelleğe alır (farklı türler içeriği farklı sürelerde önbelleğe alır)
