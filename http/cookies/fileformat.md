# Çerez dosya formatı

Netscape bir zamanlar çerezleri diskte saklamak için bir dosya formatı oluşturdu, böylece tarayıcı yeniden başlatmalarında hayatta kalabilirlerdi. curl, çerezleri tarayıcılarla paylaşmaya izin vermek için bu dosya formatını benimsedi, ancak kısa süre sonra tarayıcıların bu formattan uzaklaşmasını izledi. Modern tarayıcılar artık onu kullanmıyor, ancak curl hala kullanıyor.

Netscape çerez dosya formatı, dosyadaki her fiziksel satırda bir çerez saklar ve her alan TAB ile ayrılmış bir dizi ilişkili meta veriye sahiptir. Bu dosyaya curl terminolojisinde çerez kavanozu (cookiejar) denir.

libcurl bir çerez kavanozu kaydettiğinde, bu belgenin web sürümüne bağlanan bir URL bahsinin bulunduğu kendi dosya başlığını oluşturur.

## Dosya formatı

Çerez dosya formatı metin tabanlıdır ve her satırda bir çerez depolar. `#` ile başlayan satırlar yorum olarak kabul edilir.

Tek bir çerezi belirten her satır, TAB karakterleriyle (ASCII sekizlisi 9) ayrılmış yedi metin alanından oluşur. Geçerli bir satır yeni satır karakteriyle bitmelidir.

## Dosyadaki alanlar

Alan numarası, hangi tür ve örnek veri ve anlamı:

  0. dize `example.com` - alan adı
  1. boolean `FALSE` - alt alan adlarını dahil et
  2. dize `/foobar/` - yol
  3. boolean `TRUE` - yalnızca HTTPS üzerinden gönder/al
  4. sayı `1462299217` - sona erme zamanı - 1 Ocak 1970'ten bu yana saniye veya 0
  5. dize `person` - çerezin adı
  6. dize `daniel` - çerezin değeri
