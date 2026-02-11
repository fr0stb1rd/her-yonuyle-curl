# Parça (Fragment)

Bir URL, URL'nin sonunda bir kare (diez) işareti ve dize ile yazılan, parça (fragment) olarak da bilinen bir çapa (anchor) içerebilir. Örneğin `http://example.com/foo.html#here-it-is` gibi. O parça kısmı, kare/diez işaretinden URL'nin sonuna kadar olan her şey, yalnızca yerel kullanım içindir ve ağ üzerinden gönderilmez. curl bu veriyi basitçe kesip atar.

## Bir aralık hilesi

Parçanın kablo üzerinden gönderilmediği gerçeğinden yararlanmanın pratik bir yolu, aynı URL'yi komut satırında birçok kez kullanmak istiyorsanız bu alanı aralıklar için kullanmaktır.

Örneğin, bu URL'yi yirmi kez indirin:

    curl "https://example.com/#[1-20]"
