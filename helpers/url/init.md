# Oluştur, temizle, çoğalt (Create, cleanup, duplicate)

Bu API'yi kullanırken ilk adım, URL bilgilerini ve kaynaklarını tutan bir `CURLU *` handle (tutaç) oluşturmaktır. Handle, tek bir URL ve tüm farklı bileşenleri hakkında bilgi tutan ilişkili bir veri nesnesine referanstır.

API, her URL bileşenini ayrı ayrı veya tam bir URL olarak ayarlamanıza veya almanıza olanak tanır.

Şöyle bir URL handle oluşturun:

    CURLU *h = curl_url();

İşiniz bittiğinde temizleyin:

    curl_url_cleanup(h);

Bir handle'ın kopyasına ihtiyacınız olduğunda, sadece çoğaltın:

    CURLU *nh = curl_url_dup(h);
