# Çerezler (Cookies)

Varsayılan olarak ve tasarım gereği, libcurl transferleri mümkün olduğunca temel yapar ve özelliklerin kullanılması için etkinleştirilmesi gerekir. Böyle bir özellik HTTP çerezleridir, daha çok sadece düz ve basit çerezler olarak bilinir.

Çerezler, sunucu tarafından (`Set-Cookie:` başlığı kullanılarak) istemcide saklanmak üzere gönderilen ad/değer çiftleridir ve daha sonra sunucudan geldiğinde çerezle birlikte belirtilen ana bilgisayar ve yol gereksinimleriyle eşleşen isteklerde (`Cookie:` başlığı kullanılarak) tekrar geri gönderilmesi gerekir. Günümüzün modern web'inde, sitelerin bazen çok sayıda çerez kullandığı bilinmektedir.

## Çerez motoru

Belirli bir easy handle için çerez motorunu etkinleştirdiğinizde, bu, gelen çerezleri kaydettiği, bunları easy handle ile ilişkili bellek içi çerez deposunda sakladığı ve daha sonra eşleşen bir HTTP isteği yapılırsa uygun olanları geri gönderdiği anlamına gelir.

Çerez motorunu açmanın iki yolu vardır:

### Okuma ile çerez motorunu etkinleştir

libcurl'den `CURLOPT_COOKIEFILE` seçeneğiyle belirli bir dosya adından easy handle'a çerezleri içe aktarmasını isteyin:

    curl_easy_setopt(easy, CURLOPT_COOKIEFILE, "cookies.txt");

Yaygın bir numara, çerez motorunu başlangıçta boş bir çerez deposuyla etkinleştirmek için var olmayan bir dosya adı veya düz `""` belirtmektir.

Bu seçenek birden çok kez ayarlanabilir ve ardından verilen dosyaların her biri okunur.

### Yazma ile çerez motorunu etkinleştir

Alınan çerezlerin `CURLOPT_COOKIEJAR` seçeneğiyle bir dosyada saklanmasını isteyin:

    curl_easy_setopt(easy, CURLOPT_COOKIEJAR, "cookies.txt");

daha sonra `curl_easy_cleanup()` ile easy handle kapatıldığında, bilinen tüm çerezler verilen dosyada saklanır. Dosya formatı, tarayıcıların da bir zamanlar kullandığı iyi bilinen Netscape çerez dosyası formatıdır.

## Özel çerezleri ayarlama

Çerez deposuna herhangi bir çerez eklemeyen ve hatta çerez motorunu etkinleştirmeyen bir istekte sadece bir dizi belirli çerezi iletmenin daha basit ve daha doğrudan bir yolu, seti `CURLOPT_COOKIE` ile ayarlamaktır:

    curl_easy_setopt(easy, CURLOPT_COOKIE, "name=daniel; present=yes;");

Oraya ayarladığınız dize, HTTP isteğinde gönderilecek ham dizedir ve noktalı virgül ayırıcı dahil olmak üzere tekrarlanan `NAME=VALUE;` dizileri formatında olmalıdır.

## İçe aktar dışa aktar

Çerez bellek içi deposu bir sürü çerez tutabilir ve libcurl, bir uygulamanın bunlarla oynaması için güçlü yollar sunar. Yeni çerezler ayarlayabilir, mevcut bir çerezi değiştirebilir ve mevcut çerezleri çıkarabilirsiniz.

### Çerez deposuna bir çerez ekle

Basitçe `CURLOPT_COOKIELIST` ile yeni bir çerez ileterek çerez deposuna yeni bir çerez ekleyin. Girdi formatı, çerez dosyası formatında tek bir satırdır veya bir `Set-Cookie:` yanıt başlığı olarak biçimlendirilmiştir ancak çerez dosyası stilini öneririz:

    #define SEP  "\t"  /* Alanları Tab ayırır */

    char *my_cookie =
      "example.com"    /* Ana Bilgisayar Adı */
      SEP "FALSE"      /* Alt alanları dahil et */
      SEP "/"          /* Yol */
      SEP "FALSE"      /* Güvenli */
      SEP "0"          /* Epoch zaman formatında bitiş süresi. 0 == Oturum */
      SEP "foo"        /* Ad */
      SEP "bar";       /* Değer */

    curl_easy_setopt(curl, CURLOPT_COOKIELIST, my_cookie);

Verilen o çerez zaten mevcut bir çerezle eşleşirse (aynı alan adı ve yol vb. ile), eskisinin üzerine yeni içerikle yazar.

### Çerez deposundan tüm çerezleri al

Bazen handle'ı kapattığınızda çerez dosyasını yazmak yeterli değildir ve o zaman uygulamanız depodan şu anda bilinen tüm çerezleri şöyle çıkarmayı seçebilir:

    struct curl_slist *cookies
    curl_easy_getinfo(easy, CURLINFO_COOKIELIST, &cookies);

Bu, çerezlerden oluşan bir bağlantılı listeye bir işaretçi döndürür ve her çerez (yeniden) çerez dosyası formatının tek bir satırı olarak belirtilir. Liste sizin için ayrılmıştır, bu nedenle uygulama bilgiyle işini bitirdiğinde `curl_slist_free_all` çağırmayı unutmayın.

### Çerez deposu komutları

Çerezleri ayarlamak ve çıkarmak yeterli değilse, çerez deposuna daha fazla yolla müdahale edebilirsiniz:

Tüm bellek içi depolamayı şununla silin:

    curl_easy_setopt(curl, CURLOPT_COOKIELIST, "ALL");

Bellekten tüm oturum çerezlerini (son kullanma tarihi olmayan çerezler) silin:

    curl_easy_setopt(curl, CURLOPT_COOKIELIST, "SESS");

Daha önce `CURLOPT_COOKIEJAR` ile belirtilen dosya adına tüm çerezlerin yazılmasını zorlayın:

    curl_easy_setopt(curl, CURLOPT_COOKIELIST, "FLUSH");

Daha önce `CURLOPT_COOKIEFILE` ile belirtilen dosya adından çerezlerin yeniden yüklenmesini zorlayın:

    curl_easy_setopt(curl, CURLOPT_COOKIELIST, "RELOAD");

## Çerez dosyası formatı

Çerez dosyası formatı metin tabanlıdır ve satır başına bir çerez saklar. `#` ile başlayan satırlar yorum olarak kabul edilir.

Her biri tek bir çerezi belirten her satır, TAB karakterleriyle ayrılmış yedi metin alanından oluşur.

| Alan | Örnek       | Anlamı                                        |
|-------|-------------|-----------------------------------------------|
| 0     | example.com | Alan adı                                      |
| 1     | FALSE       | Alt alanları dahil et boolean                 |
| 2     | /foobar/    | Yol                                           |
| 3     | FALSE       | Güvenli bir taşıma üzerinden ayarla           |
| 4     | 1462299217  | Bitiş tarihi – 1 Ocak 1970'ten beri saniye, veya 0 |
| 5     | person      | Çerezin adı                                   |
| 6     | daniel      | Çerezin değeri                                |

