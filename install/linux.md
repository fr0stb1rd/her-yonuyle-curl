# Linux

Linux dağıtımları, sundukları yazılımları kurmanızı sağlayan paket yöneticileriyle gelir. Çoğu Linux dağıtımı, varsayılan olarak kurulu değilse curl ve libcurl'ün kurulmasını önerir.

## Ubuntu ve Debian

`apt`, Debian Linux ve Ubuntu Linux dağıtımlarında ve türevlerinde önceden oluşturulmuş paketleri kurmak için kullanılan bir araçtır.

curl komut satırı aracını kurmak için genellikle sadece şunu yaparsınız:

    apt install curl

…ve bu daha sonra bağımlılıkların kurulduğundan emin olur ve genellikle libcurl de ayrı bir paket olarak kurulur.

libcurl'e karşı uygulamalar geliştirmek istiyorsanız, dahil etme (include) başlıklarını ve bazı ek belgeleri vb. almak için kurulu bir geliştirme paketine ihtiyacınız vardır. Daha sonra tercih ettiğiniz TLS arka ucuna sahip bir libcurl seçebilirsiniz:

    apt install libcurl4-openssl-dev

veya

    apt install libcurl4-gnutls-dev

## Redhat ve CentOS

Redhat Linux ve CentOS Linux türevlerinde paketleri kurmak için `yum` kullanırsınız. Komut satırı aracını şununla kurun:

    yum install curl

libcurl geliştirme paketini (include dosyaları ve bazı belgeler vb. ile birlikte) şununla kurarsınız:

    yum install libcurl-devel

## Fedora

Fedora Workstation ve diğer Fedora tabanlı dağıtımlar paketleri kurmak için `dnf` kullanır.

Komut satırı aracını şununla kurun:

    dnf install curl

libcurl geliştirme paketini kurmak için şunu çalıştırırsınız:

    dnf install libcurl-devel

## Değişmez (Immutable) Fedora dağıtımları

Silverblue, Kinoite, Sericea, Onyx vb. gibi dağıtımlar paketleri kurmak için `rpm-ostree` kullanır.
Kurulumdan sonra sistemi yeniden başlatmayı unutmayın.

    rpm-ostree install curl

libcurl geliştirme paketini kurmak için şunu çalıştırırsınız:

    rpm-ostree install libcurl-devel

## nix

[Nix](https://nixos.org/nix/), NixOS dağıtımı için varsayılan paket yöneticisidir, ancak herhangi bir Linux dağıtımında da kullanılabilir.

Komut satırı aracını kurmak için:

    nix-env -i curl

## Arch Linux

curl, Arch Linux'un çekirdek (core) deposunda bulunur. Bu, normal kurulum prosedürünü izlerseniz otomatik olarak kurulması gerektiği anlamına gelir.

curl kurulu değilse, Arch Linux paketleri kurmak için `pacman` kullanır:

    pacman -S curl

## SUSE ve openSUSE

SUSE Linux ve openSUSE Linux ile paketleri kurmak için `zypper` kullanırsınız. curl komut satırı yardımcı programını kurmak için:

    zypper install curl

libcurl geliştirme paketini kurmak için şunu çalıştırırsınız:

    zypper install libcurl-devel

### SUSE SLE Micro ve openSUSE MicroOS

SUSE/openSUSE Linux'un bu sürümleri değişmez (immutable) işletim sistemleridir ve salt okunur bir kök dosya sistemine sahiptir, paketleri kurmak için `zypper` yerine `transactional-update` kullanırsınız. curl komut satırı yardımcı programını kurmak için:

    transactional-update pkg install curl

libcurl geliştirme paketini kurmak için:

    transactional-update pkg install libcurl-devel

## Gentoo

Bu paket aracı, libcurl'ü, başlıkları ve pkg-config dosyalarını vb. kurar.

    emerge net-misc/curl

## Void Linux

Void Linux ile paketleri kurmak için `xbps-install` kullanırsınız.
curl komut satırı yardımcı programını kurmak için:

    xbps-install curl

libcurl geliştirme paketini kurmak için:

    xbps-install libcurl-devel
