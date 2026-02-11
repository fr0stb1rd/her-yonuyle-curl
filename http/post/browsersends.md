# Bir tarayıcının ne gönderdiğini anlama

Yaygın bir kısayol, formu tarayıcınızla doldurup göndermek ve tarayıcının ağ geliştirme araçlarında tam olarak ne gönderdiğini kontrol etmektir.

Biraz farklı bir yol, formu içeren HTML sayfasını kaydetmek ve ardından o HTML sayfasını formun 'action=' kısmını kendi sunucunuza veya tam olarak ne aldığını çıktılayan bir test sunucusuna yönlendirecek şekilde düzenlemektir. O form gönderimini tamamlamak size bir tarayıcının onu tam olarak nasıl gönderdiğini gösterir.

Üçüncü bir seçenek, elbette, kablo üzerinden tam olarak neyin gönderildiğini kontrol etmek için Wireshark gibi bir ağ yakalama aracı kullanmaktır. HTTPS ile çalışıyorsanız, form gönderimlerini kablo üzerinde açık metin olarak göremezsiniz, bunun yerine Wireshark'ın TLS özel anahtarınızı tarayıcınızdan çıkarabilmesini sağlamanız gerekir. Bunu yapmayla ilgili ayrıntılar için [SSLKEYLOGFILE bölümüne](../../usingcurl/tls/sslkeylogfile.md) bakın.
