# FTP ile yükleme

Bir FTP sunucusuna yükleme yapmak için, URL'de tüm hedef dosya yolunu ve adını belirtirsiniz ve yüklenecek yerel dosya adını `-T, --upload-file` ile belirtirsiniz. İsteğe bağlı olarak, hedef URL'yi bir eğik çizgiyle bitirirsiniz ve ardından yerel yoldaki dosya bileşeni curl tarafından eklenir ve uzak dosya adı olarak kullanılır.

Şöyle:

    curl -T localfile ftp://ftp.example.com/dir/path/remote-file

veya yerel dosya adını uzak ad olarak kullanmak için:

    curl -T localfile ftp://ftp.example.com/dir/path/

Yükleme yaparken üzerine yazmak yerine `--append` seçeneğiyle yerel dosyayı hedef dosyaya ekleyin:

    curl -T uploadthis --append ftp://example.com/directory/remotename

curl ayrıca `-T` argümanında [globbing](../cmdline/urls/globbing.md) destekler, böylece bir dizi dosyayı kolayca yüklemeyi seçebilirsiniz:

    curl -T 'image[1-99].jpg' ftp://ftp.example.com/upload/

veya bir dosya serisi:

    curl -T '{file1,file2}' ftp://ftp.example.com/upload/

veya

    curl -T '{Huey,Dewey,Louie}.jpg' ftp://ftp.example.com/nephews/
