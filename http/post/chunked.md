# Parçalı (Chunked) kodlanmış POST'lar

Bir HTTP 1.1 sunucusuyla konuşurken, curl'e POST'un tam olarak ne kadar büyük olduğunu belirten bir `Content-Length:` başlığı olmadan istek gövdesini göndermesini söyleyebilirsiniz. curl'ün parçalı (chunked) Transfer-Encoding kullanmasında ısrar ederek, curl POST'u parça parça, her bir parça için boyutu da gönderen özel bir tarzda gönderir.

curl ile parçalı bir POST'u şu şekilde gönderirsiniz:

    curl -H "Transfer-Encoding: chunked" -d @file http://example.com

## Uyarılar (Caveats)

Bu, bunu bir HTTP/1.1 sunucusuna karşı yaptığınızı bildiğinizi varsayar. 1.1'den önce parçalı kodlama yoktu ve 1.1 sürümünden sonra parçalı kodlama kullanımdan kaldırıldı (deprecated).
