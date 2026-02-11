# Gizli form alanları

`-d` ile bir gönderi (post) göndermek, bir HTML formu doldurulduğunda ve gönderildiğinde bir tarayıcının yaptığının eşdeğeridir.

Bu tür formları göndermek curl ile yaygın bir işlemdir; etkili bir şekilde, curl'ün otomatik bir şekilde bir web formunu doldurmasını sağlamaktır.

Bir formu curl ile göndermek ve bir tarayıcı ile yapılmış gibi görünmesini sağlamak istiyorsanız, formdaki tüm giriş alanlarını sağlamak önemlidir. Web sayfaları için yaygın bir yöntem, forma birkaç gizli giriş alanı ayarlamak ve bunlara doğrudan HTML içinde değerler atamaktır. Başarılı bir form gönderimi elbette bu alanları da içerir ve bunu otomatik olarak yapmak için önce formu tutan HTML sayfasını indirmeniz, ayrıştırmanız ve gizli alan değerlerini çıkarmanız gerekebilir, böylece onları curl ile gönderebilirsiniz.
