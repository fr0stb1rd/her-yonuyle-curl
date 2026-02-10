# Nasıl başladı

1996 yılında, [Daniel Stenberg](https://daniel.haxx.se/) boş zamanlarında bir IRC botu yazıyordu; Amiga bilgisayarına (IRC ağı EFnet üzerindeki #amiga kanalı) adanmış bir sohbet odasındaki katılımcılar için hizmetler sunacak otomatik bir program. Güncel döviz kurlarını alıp botunun sohbet odası kullanıcılarına güncel kurları sunmasının, örneğin bot'a "lütfen 200 USD'yi SEK'e çevir" veya benzeri şeyler sormanın eğlenceli olacağını düşündü.

Sağlanan döviz kurlarının mümkün olduğunca doğru olması için, bot kurları barındıran bir web sitesinden günlük olarak indirecekti. Bu görev için HTTP üzerinden veri indirmek üzere küçük bir araca ihtiyaç duyuldu. O zamanlar yapılan hızlı bir araştırma sonucunda Daniel, httpget adlı küçük bir araç buldu (Brezilyalı geliştirici Rafael Sagula tarafından yazılmıştı). İşi görüyordu, neredeyse, sadece orada burada birkaç küçük ince ayara ihtiyacı vardı.

Rafael, HttpGet 0.1'i 11 Kasım 1996'da yayınladı ve hemen bir sonraki sürümde, o yılın Aralık ayında yayınlanan 0.2 sürümünde, Daniel'in ilk değişiklikleri dahil edildi. Bundan kısa bir süre sonra, Daniel birkaç yüz satırlık kodun bakımını devraldı.

HttpGet 1.0, 8 Nisan 1997'de yepyeni HTTP vekil sunucu (proxy) desteğiyle yayınlandı.

Kısa süre sonra GOPHER üzerinden para birimlerini alma desteğini bulduk ve düzelttik. FTP indirme desteği eklendiğinde, projenin adı değiştirildi ve urlget 2.0, Ağustos 1997'de yayınlandı. Sadece HTTP günleri çoktan geride kalmıştı.

Proje yavaş yavaş büyüdü. Yükleme yetenekleri eklendiğinde ve isim bir kez daha yanıltıcı hale geldiğinde, ikinci bir isim değişikliği yapıldı ve 20 Mart 1998'de curl 4 yayınlandı. (Önceki isimlerden gelen sürüm numaralandırması korundu.)

Biz **20 Mart 1998** tarihini curl'ün doğum günü olarak kabul ediyoruz.
