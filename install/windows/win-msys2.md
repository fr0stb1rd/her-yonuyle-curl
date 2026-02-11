# MSYS2

[MSYS2](https://www.msys2.org/), [mingw-w64](https://www.mingw-w64.org/) tabanlı Windows için popüler bir derleme (build) sistemidir ve hem gcc hem de clang derleyicilerini içerir. MSYS2, `pacman` (arch-linux'tan bir port) adında bir paket yöneticisi kullanır ve yaklaşık 2000 önceden derlenmiş [mingw-paketine](https://github.com/msys2/MINGW-packages) sahiptir. MSYS2, bağımsız yazılımlar oluşturmak için tasarlanmıştır: mingw-w64 derleyicileri ile oluşturulan ikili dosyalar (binaries), MSYS2'ye bağlı değildir\[^1].

## MSYS2'de curl ve libcurl edinin

[`mingw-w64-curl`](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-curl/PKGBUILD) paketi hakkında güncel bilgiler msys2 web sitesinde bulunabilir: https://packages.msys2.org/base/mingw-w64-curl. Burada ayrıca çeşitli mevcut çeşitler için kurulum talimatlarını da bulabiliriz. Örneğin curl için varsayılan x64 ikili dosyasını kurmak için şunu çalıştırırız:

    pacman -Sy mingw-w64-x86_64-curl

Bu paket, hem `curl` komut satırı aracını hem de libcurl başlıklarını ve paylaşılan kütüphanelerini içerir. Varsayılan `curl` paketleri OpenSSL arka ucu ile oluşturulmuştur ve bu nedenle `mingw-w64-x86_64-openssl`e bağlıdır. Ayrıca `mingw-w64-x86_64-curl-gnutls` ve `mingw-w64-x86_64-curl-gnutls` paketleri de vardır, daha fazla ayrıntı için [msys2 web sitesine](https://packages.msys2.org/base/mingw-w64-curl) bakın.

Tıpkı Linux'ta olduğu gibi, libcurl'e karşı derleme yapmak için gereken bayrakları (flags) sorgulamak için `pkg-config` kullanabiliriz. mingw64 kabuğunu (shell) kullanarak msys2'yi başlatın (bu, `/mingw64`'ü dahil edecek yolu otomatik olarak ayarlar) ve çalıştırın:

    pkg-config --cflags libcurl
    # -IC:/msys64/mingw64/include

    pkg-config --libs libcurl
    # -LC:/msys64/mingw64/lib -lcurl

pacman paket yöneticisi önceden derlenmiş ikili dosyaları kurar. Sırada, örneğin yapılandırmayı özelleştirmek için curl'ü yerel olarak derlemek amacıyla pacman'i nasıl kullanacağımızı açıklıyoruz.

## MSYS2 üzerinde libcurl derleme

Pacman ile paket oluşturmak neredeyse kurulum kadar basittir. Tüm süreç, `mingw-w64-curl` paketinden [PKGBUILD](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-curl/PKGBUILD) dosyasında yer almaktadır. Paketi kendimiz yeniden oluşturmak için dosyayı kolayca değiştirebiliriz.

Temiz bir msys2 kurulumuyla başlarsak, önce `autoconf`, `patch` ve `git` gibi bazı derleme araçlarını kurmak isteriz. msys2 kabuğunu başlatın ve çalıştırın:

    # Depoları senkronize edin (Sync the repositories)
    pacman -Syu

    # git, autoconf, patch, vb. kurun
    pacman -S git base-devel

    # x86_64 için GCC kurun
    pacman -S mingw-w64-x86_64-toolchain

Şimdi `mingw-packages` deposunu klonlayın ve `mingw-w64-curl` paketine gidin:

    git clone https://github.com/msys2/MINGW-packages
    cd MINGW-packages/mingw-w64-curl

Bu dizin, curl'ü oluşturmak için kullanılan PKGBUILD dosyasını ve yamaları içerir. Neler olup bittiğini görmek için PKGBUILD dosyasına bir göz atın. Şimdi derlemek için şunları yapabiliriz:

    makepkg-mingw --syncdeps --skippgpcheck

İşte bu kadar. `--syncdeps` parametresı, `mingw-w64-curl` bağımlılıklarını henüz kurulu değilse otomatik olarak kontrol eder ve kurulmasını ister. İşlem tamamlandığında, geçerli dizinde 3 yeni dosyanız olur, örneğin:

* `pacman -U mingw-w64-x86_64-curl-7.80.0-1-any.pkg.tar.zst`
* `pacman -U mingw-w64-x86_64-curl-gnutls-7.80.0-1-any.pkg.tar.zst`
* `pacman -U mingw-w64-x86_64-curl-winssl-7.80.0-1-any.pkg.tar.zst`

Böyle bir yerel paket dosyasını kurmak için `pacman -u` komutunu kullanın:

    pacman -U mingw-w64-x86_64-curl-winssl-7.80.0-1-any.pkg.tar.zst

pacman ve msys2 ile derleme hakkında daha fazla bilgi edinmek için [msys2 belgelerine](https://www.msys2.org/docs/package-management/) bir göz atın veya [gitter](https://gitter.im/msys2/msys2)'a katılın.

\[^1]: `mingw-w64-curl` [mingw-paketi](https://github.com/msys2/MINGW-packages) ile `curl` ve `curl-devel` [msys-paketlerini](https://github.com/msys2/MSYS2-packages) karıştırmamaya dikkat edin. İkincisi, msys2 ortamının kendisinin bir parçasıdır (örneğin pacman indirmelerini desteklemek için), ancak yeniden dağıtım için uygun değildir. MSYS2'ye bağlı olmayan yeniden dağıtılabilir yazılımlar oluşturmak için her zaman `mingw-w64-…` paketlerine ve araç zincirlerine ihtiyacınız vardır.
