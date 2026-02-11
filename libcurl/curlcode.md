# CURLcode dönüş kodları

Birçok libcurl işlevi bir CURLcode döndürür. Bu, hata kodları için libcurl'de typedef edilmiş özel bir değişkendir. Her şey yolundaysa `CURLE_OK` (değeri sıfırdır) döndürür ve bir sorun algılanırsa sıfır olmayan bir sayı döndürür. Kullanımda neredeyse yüz `CURLcode` hatası vardır ve hepsini `curl/curl.h` başlık dosyasında bulabilir ve libcurl-errors kılavuz sayfasında belgelenmiş olarak görebilirsiniz.

Bir CURLcode'u `curl_easy_strerror()` işleviyle insan tarafından okunabilir bir dizeye dönüştürebilirsiniz—ancak bu hataların nadiren bir kullanıcı arayüzünde veya bir son kullanıcıya gösterilmeye uygun bir şekilde ifade edildiğini unutmayın:

    const char *str = curl_easy_strerror( error );
    printf("libcurl said %s\n", str);

Hata durumunda biraz daha iyi bir hata metni almanın başka bir yolu, `CURLOPT_ERRORBUFFER` seçeneğini programınızdaki bir arabelleği işaret edecek şekilde ayarlamaktır; libcurl bir hata döndürmeden önce ilgili bir hata mesajını orada saklar:

    char error[CURL_ERROR_SIZE]; /* en az bu kadar büyük olması gerekir */
    CURLcode ret = curl_easy_setopt(handle, CURLOPT_ERRORBUFFER, error);
