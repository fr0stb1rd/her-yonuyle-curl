# Bölüm (Fragment)

URL'ler bir bölüm parçası sunar. Bu genellikle tarayıcılarda bir web sayfası içindeki belirli bir ad için bir kare sembolü (`#`) ve bir ad olarak görülür. Böyle bir URL'nin bir örneği şuna benzer:

    https://www.example.com/info.html#the-plot

curl, kendisine bir URL iletildiğinde bölümleri iyi destekler, ancak bölüm kısmı asla kablo üzerinden gönderilmez, bu nedenle mevcut olup olmaması curl'ün işlemleri için bir fark yaratmaz.

`#` karakterini bölümü ayıran değil de yolun bir parçası yapmak istiyorsanız, onu URL kodlu olarak, `%23` şeklinde ilettiğinizden emin olun:

    curl https://www.example.com/info.html%23the-plot

## Bir bölüm hilesi

Bölüm kısmının aslında ağ üzerinden kullanılmadığı gerçeği, komut satırları oluştururken avantaj olarak kullanılabilir.

Örneğin, bir sunucudan aynı URL'yi 10 kez istemek istiyorsanız, bir döngü yapabilir ve döngü talimatını bölüm kısmına koyabilirsiniz. Şunun gibi:

    curl https://example.com/#[1-10]
