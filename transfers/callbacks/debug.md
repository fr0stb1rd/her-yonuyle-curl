# Hata ayıklama (Debug)

Hata ayıklama geri çağırımı `CURLOPT_DEBUGFUNCTION` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_DEBUGFUNCTION, debug_callback);

`debug_callback` işlevi şu prototiple eşleşmelidir:

    int debug_callback(CURL *handle,
                       curl_infotype type,
                       char *data,
                       size_t size,
                       void *userdata);

Bu geri çağırım işlevi, kütüphanedeki varsayılan ayrıntılı çıktı işlevinin yerini alır ve uygulamaların neler olup bittiğini anlamasına yardımcı olmak için tüm hata ayıklama ve izleme mesajları için çağrılır. *type* argümanı ne tür veri sağlandığını açıklar: başlık, veri veya SSL verisi ve hangi yönde aktığı.

Bu geri çağırımın yaygın bir kullanımı, libcurl'ün gönderdiği ve aldığı tüm verilerin tam bir izini almaktır. Bu geri çağırıma gönderilen veriler, örneğin HTTPS veya diğer şifreli protokoller kullanıldığında bile her zaman şifrelenmemiş sürümdür.

Bu geri çağırım sıfır döndürmeli veya transferin bir hata koduyla durmasına neden olmalıdır.

*userdata* argümanında geri çağırıma iletilen kullanıcı işaretçisi `CURLOPT_DEBUGDATA` ile ayarlanır:

    curl_easy_setopt(handle, CURLOPT_DEBUGDATA, custom_pointer);
