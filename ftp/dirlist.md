# FTP Dizin listeleme

URL'nin sonunun eğik çizgiyle bittiğinden emin olarak curl ile uzak bir FTP dizinini listeleyebilirsiniz. URL bir eğik çizgiyle bitiyorsa, curl listelemek istediğiniz şeyin bir dizin olduğunu varsayar. Eğer aslında bir dizin değilse, muhtemelen bunun yerine bir hata alırsınız.

    curl ftp://ftp.example.com/directory/

FTP ile, standart FTP komutu `LIST` kullanan bu tür bir komut için döndürülen dizin çıktısı için standart bir sözdizimi yoktur. Listeleme genellikle insanlar tarafından okunabilir ve tamamen anlaşılabilirdir ancak farklı sunucular listelemeyi biraz farklı düzenler kullanarak döndürebilir.

Bir dizindeki tüm isimlerin sadece bir listesini almanın ve böylece normal dizin listelemelerinin özel formatlamasından kaçınmanın bir yolu, curl'e `--list-only` (veya sadece `-l`) demektir. curl daha sonra bunun yerine `NLST` FTP komutunu verir:

    curl --list-only ftp://ftp.example.com/directory/

Ancak NLST'nin kendi tuhaflıkları vardır, çünkü bazı FTP sunucuları NLST'ye yanıtlarında yalnızca gerçek *dosyaları* listeler; dizinleri ve sembolik bağlantıları dahil etmezler.
