# Zaten yapılmışsa indirmeyi atla

Bazen arada sırada İnternet transferleri yapmak için bir komut dosyası veya benzeri yazarken, hedef dosya yerel olarak zaten mevcutsa curl'ün transfer yapmayı atlamasını tercih ettiğiniz bir duruma düşersiniz. Belki önceki çağrıdan sonra, belki de başka bir nedenden dolayı.

Bu tür ekstra mantık, birçok durumda curl çağrılmadan önce kesinlikle yaygın kabuk komut dosyası mantığına eklenebilir ancak her zaman değil. Örneğin, curl'den [globbing indirme aralıkları](../../cmdline/urls/globbing.md) kullanmasını istediğinizde işler karmaşıklaşır.

Örneğin, bir siteden bin resim indirin ancak daha önce indirdiğimiz resimleri atlayın:

    curl --skip-existing -O https://example.com/image[0-999].jpg

Bunun yalnızca yerel dosyanın *varlığını* kontrol ettiği, aslında doğru içeriğe sahip olduğunu doğrulamak için hiçbir girişimde bulunmadığı ve bu tür kontrolleri yapmanın bir yolu olmadığı unutulmamalıdır.

curl, değiştirilme tarihine veya HTTP transferleri için içeriklere dayalı olarak [koşullu transferler](../../http/modify/conditionals.md) yapmak için başka seçenekler sunar.
