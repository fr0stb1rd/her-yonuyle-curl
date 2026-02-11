# SSLKEYLOGFILE

![Wireshark ile ağ trafiğini görüntüleyin](wireshark-screenshot.png)

Uzun zamandır, saygıdeğer ağ analiz aracı Wireshark (yukarıdaki ekran görüntüsü), Firefox ve Chrome tarafından gönderilen ve alınan TLS trafiğinin şifresini çözmek ve incelemek için bir yol sağlamıştır.

Bunu curl ile yapmak da benzer şekilde mümkündür.

Bunu, tarayıcının veya curl'ün şifreleme sırlarını Wireshark'a söylemesini sağlayarak yaparsınız, böylece şifrelerini çözebilir:

1. tarayıcıyı veya curl'ü başlatmadan önce `SSLKEYLOGFILE` adlı ortam değişkenini seçtiğiniz bir dosya adına ayarlayın
2. Aynı dosya yolu yolunu Wireshark'taki Master-secret alanına ayarlayın. Tercihler->Protokoller->TLS'ye (Prenences->Protocols->TLS) gidin ve yolu aşağıdaki ekran görüntüsünde gösterildiği gibi düzenleyin.

![ssl anahtar dosya adını ayarlayın](wireshark-ssl-master-secret.png)

Bu basit işlemi yaptıktan sonra artık Wireshark'ta curl'ün veya tarayıcınızın HTTPS trafiğini inceleyebilirsiniz. Sadece süper kullanışlı ve harika.

Sadece unutmayın, TLS trafiğini kaydederseniz ve daha sonra analiz etmek için saklamak isterseniz, o trafik yakalamasının şifresini daha sonra da çözebilmek için dosyayı sırlarla birlikte kaydetmeniz gerekir.

## libcurl kullanan uygulamalar da

`SSLKEYLOGFILE` desteği libcurl'ün kendisi tarafından sağlanır - bu da sadece curl komut satırı aracı için değil, libcurl'ü kullanmak üzere oluşturulmuş herhangi bir uygulama için TLS ağ verilerini izlemenizi ve incelemenizi mümkün kılar.

## Kısıtlamalar

`SSLKEYLOGFILE` desteği, curl'ün bu özelliği destekleyen bir TLS arka ucuyla derlenmiş olmasını gerektirir. SSLKEYLOGFILE'ı destekleyen arka uçlar şunlardır: OpenSSL, AWS-LC, BoringSSL, GnuTLS ve wolfSSL. LibreSSL (OpenSSL'in bir çatalı) bunu yalnızca TLS <= 1.2 için destekler.

curl başka bir arka uç kullanacak şekilde derlenmişse, curl TLS trafiğinizi bu şekilde kaydedemezsiniz.
