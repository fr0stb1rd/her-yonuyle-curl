# BoringSSL

## boringssl derleme

$HOME/src, bu örnekte kodu koyduğum yerdir. Siz istediğiniz yeri seçebilirsiniz.

    $ cd $HOME/src
    $ git clone https://boringssl.googlesource.com/boringssl
    $ cd boringssl
    $ mkdir build
    $ cd build
    $ cmake -DCMAKE_POSITION_INDEPENDENT_CODE=on ..
    $ make

## curl'ün configure betiği tarafından algılanması için derleme ağacını ayarlama

boringssl kaynak ağacı kökünde, bir `lib` ve bir `include` dizini bulunduğundan emin olun. `lib` dizini iki kütüphaneyi içermelidir (ben onları build dizinine sembolik bağlar (symlinks) yaptım). `include` dizini zaten varsayılan olarak mevcuttur. `lib` dizinini şu şekilde oluşturun ve doldurun (komutlar `build/` alt dizininde değil, kaynak ağacı kökünde verilmiştir).


    $ mkdir lib
    $ cd lib
    $ ln -s ../build/ssl/libssl.a
    $ ln -s ../build/crypto/libcrypto.a


## curl'ü yapılandırma (configure)

`LIBS=-lpthread ./configure --with-ssl=$HOME/src/boringssl` (boringssl ağacının kökünü işaret ettiğim yer)

Yapılandırmanın sonunda, kullanılacak BoringSSL'i algıladığını doğrulayın.

## curl derleme

curl kaynak ağacında `make` çalıştırın.

Şimdi `make install` vb. ile curl'ü normal şekilde kurabilirsiniz.
