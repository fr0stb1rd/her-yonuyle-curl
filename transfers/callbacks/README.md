# Geri çağırımlar (Callbacks)

libcurl içindeki birçok işlem *geri çağırımlar* kullanılarak kontrol edilir. Bir geri çağırım, libcurl'e sağlanan ve libcurl'ün daha sonra belirli bir işi yapmak için bir noktada çağırdığı bir işlev işaretçisidir.

Her geri çağırımın kendine özgü belgelenmiş bir amacı vardır ve doğru argümanları kabul etmesi ve libcurl'ün istediğiniz şekilde çalışması için belgelenmiş dönüş kodunu ve dönüş değerini döndürmesi için tam işlev prototipiyle yazmanızı gerektirir.

Her geri çağırım seçeneğinin ayrıca ilişkili kullanıcı işaretçisini ayarlayan bir yardımcı seçeneği vardır. Bu kullanıcı işaretçisi, libcurl'ün dokunmadığı veya umursamadığı, sadece bir argüman olarak geri çağırıma ilettiği bir işaretçidir. Bu, örneğin, yerel verilere işaretçileri geri çağırım işlevinize kadar iletmenize olanak tanır.

Bir libcurl işlev belgesinde açıkça belirtilmedikçe, bir libcurl geri çağırımı içinden libcurl işlevlerini çağırmak yasal değildir.

 * [Veri yazma (Write data)](write.md)
 * [Veri okuma (Read data)](read.md)
 * [İlerleme bilgisi (Progress information)](progress.md)
 * [Başlık verileri (Header data)](header.md)
 * [Hata ayıklama (Debug)](debug.md)
 * [sockopt](sockopt.md)
 * [SSL bağlamı (SSL context)](sslcontext.md)
 * [Arama ve ioctl (Seek and ioctl)](seek.md)
 * [Ağ veri dönüşümü](conversions.md)
 * [Soket açma ve kapama (Opensocket and closesocket)](openclosesocket.md)
 * [SSH anahtarı](sshkey.md)
 * [RTSP serpiştirilmiş veriler](rtsp.md)
 * [FTP joker karakter eşleştirme](ftpmatch.md)
 * [Çözümleyici başlatma](resolver.md)
 * [Sondaki başlıkları (Trailers) gönderme](trailers.md)
 * [HSTS](hsts.md)
 * [Ön koşul (Prereq)](prereq.md)
