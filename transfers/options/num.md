# Sayısal seçenekleri ayarla

`curl_easy_setopt()`, 3. argümanın duruma bağlı olarak farklı türler kullanabildiği bir değişken argümanlı (vararg) işlev olduğundan, normal C dili tür dönüşümü yapılamaz. Belgeler size öyle söylüyorsa, bir `int` değil, gerçekten bir `long` ilettiğinizden emin **olmalısınız**. Aynı boyutta oldukları mimarilerde herhangi bir sorun yaşamayabilirsiniz ancak hepsi böyle çalışmaz. Benzer şekilde, `curl_off_t` türünü kabul eden seçenekler için, o türü ve başka hiçbir türü kullanmayan bir argüman iletmeniz **çok önemlidir**.

Bir `long` zorla:

    curl_easy_setopt(handle, CURLOPT_TIMEOUT, 5L); /* 5 saniye zaman aşımı */

Bir `curl_off_t` zorla:

    curl_off_t no_larger_than = 0x50000;
    curl_easy_setopt(handle, CURLOPT_MAXFILESIZE_LARGE, no_larger_than);
