# İki bağlantı

FTP iki TCP bağlantısı kullanır. İlk bağlantı, istemci bir FTP sunucusuna bağlandığında kurulur ve *kontrol bağlantısı* olarak adlandırılır. İlk bağlantı olarak, kimlik doğrulama ve uzak sunucuda doğru dizine geçme vb. işlemleri halleder. İstemci daha sonra bir dosya aktarmaya hazır olduğunda, ikinci bir TCP bağlantısı kurulur ve veriler bunun üzerinden aktarılır.

İkinci bir bağlantının kurulması, çeşitli nedenlerle sıkıntılara ve baş ağrılarına neden olur.

## Aktif bağlantılar

İstemci, sunucunun istemciye bağlanarak kurulumu yapmasını, yani *aktif* bir bağlantı talep etmeyi seçebilir. Bu, PORT veya EPRT komutları ile yapılır. Uzak bir ana bilgisayarın, istemcinin açtığı bir bağlantı noktasına geri bağlanmasına izin vermek, arada bunun geçmesini engelleyen bir güvenlik duvarı veya başka bir ağ cihazı olmamasını gerektirir ve bu durum her zaman böyle olmaktan uzaktır. `curl -P [arg]` (uzun biçimde `--ftp-port` olarak da bilinir) kullanarak aktif bir transfer istersiniz ve seçenek tam olarak hangi adresin kullanılacağını belirtmenize izin verirken, geldiğiniz adresi ayarlamak neredeyse her zaman doğru seçimdir ve bunu `-P -` ile yaparsınız, işte bir dosya istemenin yolu:

    curl -P - ftp://example.com/foobar.txt

Ayrıca `--no-eprt` komut satırı seçeneğiyle curl'den açıkça EPRT (PORT'tan biraz daha yeni bir komuttur) kullanmamasını isteyebilirsiniz.

## Pasif bağlantılar

Curl varsayılan olarak *pasif* bir bağlantı istemeyi seçer; bu, sunucuya bir PASV veya EPSV komutu gönderdiği ve ardından sunucunun, curl'ün bağlandığı ikinci bağlantı için yeni bir bağlantı noktası açtığı anlamına gelir. Yeni bir bağlantı noktasına yapılan giden bağlantılar genellikle son kullanıcılar ve istemciler için daha kolay ve daha az kısıtlıdır ancak sunucunun tarafındaki ağın buna izin vermesini gerektirir.

Pasif bağlantılar varsayılan olarak etkindir, ancak daha önce aktifi açtıysanız, `--ftp-pasv` ile tekrar pasife geçebilirsiniz.

Ayrıca `--no-epsv` komut satırı seçeneğiyle curl'den açıkça EPSV (PASV'tan biraz daha yeni bir komuttur) kullanmamasını isteyebilirsiniz.

Bazen sunucu garip bir kurulum çalıştırıyor olabilir, öyle ki curl PASV komutunu verdiğinde ve sunucu curl'ün bağlanması için bir IP adresiyle yanıt verdiğinde, bu adres yanlıştır ve curl veri bağlantısını kuramaz. Bu (nadir) durum için, curl'den PASV yanıtında belirtilen IP adresini yok saymasını (`--ftp-skip-pasv-ip`) ve bunun yerine ikinci bağlantı için bile kontrol bağlantısı için sahip olduğu aynı IP adresini kullanmasını isteyebilirsiniz.

## Güvenlik duvarı sorunları

Aktif veya pasif transferler kullanıldığında, ağ yolundaki mevcut güvenlik duvarlarının, FTP trafiğinin durum bilgisine sahip denetimini (stateful inspection) yapması, açılacak yeni bağlantı noktasını bulması ve ikinci bağlantı için kabul etmesi gerekir.
