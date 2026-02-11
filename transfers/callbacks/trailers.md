# Sondaki başlıkları (Trailers) gönderme

"Trailers", başlıkların *bir transferin sonunda* iletilebildiği bir HTTP/1 özelliğidir. Bu geri çağırım, bir yükleme yapıldıktan sonra curl ile sondaki başlıkları göndermek istediğinizde kullanılır. Parçalı kodlanmış (chunked encoded) bir POST biçiminde bir yükleme.

`CURLOPT_TRAILERFUNCTION` ile ayarlanan geri çağırım çağrılır ve işlev daha sonra bir listeye başlıklar ekleyebilir. Bir veya birden çok. Tamamlandığında, libcurl bunları sunucuya sondaki başlıklar olarak gönderir.
