# Temizleme (Cleanup)

Önceki bölümlerde handle'ların nasıl kurulacağını ve transferlerin nasıl yürütüleceğini tartıştık. Tüm transferler bir noktada, ya başarıyla ya da bir başarısızlıkla sona erer.

## Multi API

Multi API ile tek bir transferi bitirdiğinizde, tam olarak hangi easy handle'ın tamamlandığını belirlemek için `curl_multi_info_read()` kullanırsınız ve `curl_multi_remove_handle()` ile o easy handle'ı multi handle'dan kaldırırsınız.

Son easy handle'ı multi handle'dan kaldırırsanız ve artık devam eden bir transfer yoksa, multi handle'ı şöyle kapatabilirsiniz:

    curl_multi_cleanup( multi_handle );

## easy handle

Easy handle amacına hizmet etmeyi bitirdiğinde onu kapatabilirsiniz. Başka bir transfer yapmayı düşünüyorsanız, handle'ı kapatıp yenisini oluşturmak yerine yeniden kullanmanız önerilir.

Easy handle ile başka bir transfer yapmayı düşünmüyorsanız, libcurl'den temizlemesini istersiniz:

    curl_easy_cleanup( easy_handle );
