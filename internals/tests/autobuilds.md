# Otomatik derlemeler (Autobuilds)

Gönüllü bireyler **otomatik derlemeleri** (autobuilds) çalıştırır. Bu, otomatik olarak çalışan bir betiktir:

- en son kodu git deposundan kontrol eder (check out)
- her şeyi derler
- test paketini çalıştırır
- tam günlüğü e-posta üzerinden curl sunucusuna gönderir

Daha sonra farklı derleme seçenekleriyle farklı platformlarda çalıştırıldıkları için, curl derleme sağlığı hakkında ekstra bir geri bildirim boyutu sunarlar.

## Durumu kontrol et

Tüm günlükler ayrıştırılır, yönetilir ve [curl sitesinde](https://curl.se/dev/builds.html) görüntülenir.

## Miras (Legacy)

Otomatik derleme sistemini 2003 yılında, [CI işlerinin](ci.md) ciddi bir alternatif olmaya başlamasından on yıl önce başlattık.

Şimdi, otomatik derlemeler daha çok bir miras sistemidir çünkü CI ve daha doğrudan ve daha erken geri bildirim dünyasına daha fazla geçiyoruz.
