# Testleri çalıştırma (Run tests)

Testleri çalıştıran ana betik `tests/runtests.pl` olarak adlandırılır ve daha yararlı özelliklerinden bazıları şunlardır:

## Bir test aralığını çalıştırma

Test 1'den 27'ye kadar çalıştır:

    ./runtests.pl 1 to 27

## Belirli bir kategoriye göre testleri çalıştırma

`SFTP` olarak işaretlenmiş tüm testleri çalıştır:

    ./runtests.pl SFTP

`FTP` olarak işaretlenmemiş tüm testleri çalıştır:

    ./runtests.pl '!FTP'

## Belirli bir testi gdb ile çalıştırma

    ./runtests.pl -g 144

gdb'yi başlatır, kesme noktaları vb. ayarlayabilirsiniz ve ardından `run` yazarsınız ve yola çıkar ve tüm işlemi hata ayıklayıcı aracılığıyla gerçekleştirir.

## Belirli bir testi valgrind olmadan çalıştırma

Test paketi, bulursa varsayılan olarak valgrind'i kullanır; bu, sorunları bulmak için mükemmel bir yoldur ancak aynı zamanda testin çok daha yavaş çalışmasını sağlar. Bazen daha hızlı yapmak istersiniz:

    ./runtests.pl -n 144
