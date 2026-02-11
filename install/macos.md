# macOS

macOS, uzun yıllardır işletim sistemiyle birlikte gelen curl aracıyla birlikte gelir. curl projesi tarafından gönderilen en son sürüme yükseltmek istiyorsanız, [homebrew](https://brew.sh/) (bir macOS yazılım paket yöneticisi) kurmanızı ve ardından curl paketini onlardan kurmanızı öneririz:

    brew install curl

curl'ü kurarken, brew'in macOS sürümüyle çakışmaları önlemek için varsayılan homebrew klasöründe bir `curl` sembolik bağı (symlink) oluşturmadığını unutmayın.

brew curl'ü kabuğunuzda (shell) varsayılan yapmak için aşağıdakini çalıştırın:

    echo 'export PATH="$(brew --prefix)/opt/curl/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc


## macOS için libcurl edinin

Yukarıda açıklandığı gibi homebrew ile `curl` aracını kurduğunuzda, libcurl'ü de ilgili başlıklarıyla birlikte kurar.

libcurl ayrıca macOS'un kendisiyle birlikte kurulur ve her zaman mevcuttur. Apple'dan `XCode` geliştirme ortamını kurarsanız, curl include dosyaları orada paketlendiğinden ekstra bir şey kurmanıza gerek kalmadan libcurl'ü doğrudan kullanabilirsiniz.
