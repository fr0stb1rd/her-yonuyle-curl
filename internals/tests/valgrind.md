# Valgrind

Valgrind, programlarda hata ayıklamak ve özellikle bellek kullanımlarını ve suiistimallerini bulmak için popüler ve güçlü bir araçtır.

`runtests.pl`, sisteminizde valgrind'in kurulu olup olmadığını otomatik olarak algılar ve varsayılan olarak bulunursa valgrind kullanarak testleri çalıştırır. Valgrind kullanımını devre dışı bırakmak için runtests'e `-n` geçirebilirsiniz.

Valgrind yürütmeyi çok daha yavaşlatır, ancak bellek sızıntılarını ve başlatılmamış bellek kullanımını bulmak için mükemmel bir araçtır.
