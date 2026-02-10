# MITM vekil sunucusu

MITM, Ortadaki Adam (Man-In-The-Middle) anlamına gelir. MITM vekil sunucuları genellikle ağ sahiplerinin TLS şifreli trafiği bile inceleme arzusuna sahip olduğu şirketlerdeki "kurumsal ortamlarda" ve başka yerlerde konuşlandırılır.

Bunu yapmak için, kullanıcıların istemciye özel bir "güven kökü" (Sertifika Yetkilisi (CA) sertifikası) yüklemesini gerektirirler ve ardından vekil sunucu istemciden gelen tüm TLS trafiğini sonlandırır, uzak sunucuyu taklit eder ve bir vekil sunucu gibi davranır. Vekil sunucu daha sonra özel CA tarafından imzalanmış oluşturulmuş bir sertifikayı geri gönderir. Bu tür vekil sunucu kurulumları genellikle istemcilerden uzak bir makinedeki TCP port 443'e giden tüm trafiği şeffaf bir şekilde yakalar. Böyle bir ağda curl çalıştırmak HTTPS trafiğinin de yakalanmasına neden olur.

Bu uygulama elbette ortadaki adamın tüm TLS trafiğinin şifresini çözmesine ve gözetlemesine izin verir.
