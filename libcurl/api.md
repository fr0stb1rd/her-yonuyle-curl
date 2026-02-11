# API uyumluluğu

libcurl, API kararlılığı vaat eder ve bugün yazılan programınızın gelecekte de çalışmaya devam edeceğini garanti eder. Uyumluluğu bozmuyoruz.

Zamanla, API'lere özellikler, yeni seçenekler ve yeni işlevler ekliyoruz ancak davranışı uyumlu olmayan bir şekilde değiştirmiyoruz veya işlevleri kaldırmıyoruz.

API'yi uyumlu olmayan bir şekilde en son değiştirdiğimiz zaman 2006'daki 7.16.0 içindi ve bunu bir daha asla yapmayı planlamıyoruz.

## Sürüm numaraları

Curl ve libcurl ayrı ayrı sürümlendirilir, ancak çoğunlukla birbirlerini oldukça yakından takip ederler.

Sürüm numaralandırması her zaman aynı sistem kullanılarak oluşturulur:

    X.Y.Z

 - X ana sürüm numarasıdır
 - Y yayın sürüm numarasıdır
 - Z yama numarasıdır

## Numaraları yükseltme

Bu X.Y.Z numaralarından biri her yeni sürümde yükseltilir. Yükseltilen bir numaranın sağındaki numaralar sıfıra sıfırlanır.

Ana sürüm numarası X, *gerçekten* büyük, dünyayı çarpıştıran değişiklikler yapıldığında yükseltilir. Yayın numarası Y, değişiklikler yapıldığında veya şeyler/özellikler eklendiğinde yükseltilir. Yama numarası Z, değişiklikler sadece hata düzeltmeleri olduğunda yükseltilir.

Bu, 1.2.3 sürümünden sonra, gerçekten büyük bir şey yapılmışsa 2.0.0, o kadar büyük değişiklikler yapılmamışsa 1.3.0 veya çoğunlukla hatalar düzeltilmişse 1.2.4 yayınlayabileceğimiz anlamına gelir.

Yükseltme, numarayı 1 artırma olarak, koşulsuz olarak yalnızca numaralardan birini etkiler (ve sağındakiler sıfıra ayarlanır). 1, 2 olur; 3, 4 olur; 9, 10 olur; 88, 89 olur ve 99, 100 olur. Yani, 1.2.9'dan sonra 1.2.10 gelir. 3.99.3'ten sonra 3.100.0 gelebilir.

Tüm orijinal curl kaynak yayın arşivleri libcurl sürümüne göre adlandırılır (daha önce belirtildiği gibi farklı olabilen curl istemci sürümüne göre değil).

## Hangi libcurl sürümü

Hala eski sürümlerle derlenebilirken yeni libcurl özelliklerini desteklemek isteyebilecek herhangi bir uygulamaya hizmet olarak, tüm sürümlerin libcurl sürümü karşılaştırma için kullanılabilecek statik bir numaralandırma şeması kullanılarak `curl/curlver.h` dosyasında saklanır. Sürüm numarası şöyle tanımlanır:

    #define LIBCURL_VERSION_NUM 0xXXYYZZ

Burada `XX` , `YY` ve `ZZ` onaltılık (hexadecimal) olarak ana sürüm, yayın ve yama numaralarıdır. Her üç numara alanı da her zaman iki basamak kullanılarak temsil edilir (her biri sekiz bit). 1.2.0 `0x010200` olarak görünürken 9.11.7 sürümü `0x090b07` olarak görünür.

Bu 6 basamaklı onaltılık sayı, daha yeni bir sürümde her zaman daha büyük bir sayıdır. Büyüktür ve küçüktür ile karşılaştırmaların çalışmasını sağlar.

Bu numara ayrıca üç ayrı tanım olarak da mevcuttur:
`LIBCURL_VERSION_MAJOR`, `LIBCURL_VERSION_MINOR` ve `LIBCURL_VERSION_PATCH`.

Bu tanımlar elbette yalnızca *şu an* derlenen sürüm numarasını anlamak için uygundur ve şu andan üç yıl sonra çalışma zamanında hangi libcurl sürümünün kullanıldığını anlamanıza yardımcı olmaz.

## Hangi libcurl sürümü çalışıyor

Uygulamanızın *şu an* hangi libcurl sürümünü kullandığını anlamak için `curl_version_info()` sizin içindir.

Uygulamalar, dinamik/DLL kütüphaneler uygulamalardan bağımsız olarak değiştirilebildiğinden, derleme zamanı kontrollerini kullanmak yerine, işlerin yapılıp yapılamayacağını değerlendirmek için bu işlevi kullanmalıdır.

curl_version_info(), çalışan libcurl sürümündeki sürüm numaraları ve çeşitli özellikler hakkında bilgi içeren bir yapıya (struct) işaretçi döndürür. Ona özel bir yaş sayacı vererek çağırırsınız, böylece libcurl onu çağıran libcurl'ün yaşını bilir. Yaş, `CURLVERSION_NOW` adlı bir tanımdır ve curl gelişimi boyunca düzensiz aralıklarla artırılan bir sayaçtır. Yaş numarası, libcurl'e hangi yapı setini döndürebileceğini söyler.

İşlevi şöyle çağırırsınız:

    curl_version_info_data *version = curl_version_info( CURLVERSION_NOW );

Veriler daha sonra aşağıdaki düzene sahip olan veya en azından sahip olabilen yapıya işaret eder:

    struct {
      CURLversion age;          /* aşağıda açıklamaya bakın */

      /* 'age' 0 veya daha yüksek olduğunda, aşağıdaki üyeler de mevcuttur: */
      const char *version;      /* insan tarafından okunabilir dize */
      unsigned int version_num; /* sayısal temsil */
      const char *host;         /* insan tarafından okunabilir dize */
      int features;             /* bitmask, aşağıya bakın */
      char *ssl_version;        /* insan tarafından okunabilir dize */
      long ssl_version_num;     /* kullanılmaz, her zaman sıfır */
      const char *libz_version; /* insan tarafından okunabilir dize */
      const char * const *protocols; /* protokoller */

      /* 'age' 1 veya daha yüksek olduğunda, aşağıdaki üyeler de mevcuttur: */
      const char *ares;         /* insan tarafından okunabilir dize */
      int ares_num;             /* numara */

      /* 'age' 2 veya daha yüksek olduğunda, aşağıdaki üye de mevcuttur: */
      const char *libidn;       /* insan tarafından okunabilir dize */

      /* 'age' 3 veya daha yüksek olduğunda (7.16.1 veya daha yenisi),
         aşağıdaki üyeler de mevcuttur */
      int iconv_ver_num;       /* iconv etkinse '_libiconv_version' */

      const char *libssh_version; /* insan tarafından okunabilir dize */

      /* 'age' 4 veya daha yüksek olduğunda, aşağıdaki üye de mevcuttur: */
      unsigned int brotli_ver_num; /* Sayısal Brotli sürümü
                                      (MAJOR << 24) | (MINOR << 12) | PATCH */
      const char *brotli_version; /* insan tarafından okunabilir dize. */

      /* 'age' 5 veya daha yüksek olduğunda, aşağıdaki üye de mevcuttur: */
      unsigned int nghttp2_ver_num; /* Sayısal nghttp2 sürümü
                                       (MAJOR << 16) | (MINOR << 8) | PATCH */
      const char *nghttp2_version; /* insan tarafından okunabilir dize. */
      const char *quic_version;    /* insan tarafından okunabilir quic
                                      (+ HTTP/3) kütüphanesi + sürüm veya
                                      NULL */

      /* 'age' 6 veya daha yüksek olduğunda, aşağıdaki üye de mevcuttur: */
      const char *cainfo;          /* yerleşik varsayılan CURLOPT_CAINFO, NULL
                                      olabilir */
      const char *capath;          /* yerleşik varsayılan CURLOPT_CAPATH, NULL
                                      olabilir */

      /* 'age' 7 veya daha yüksek olduğunda, aşağıdaki üye de mevcuttur: */
      unsigned int zstd_ver_num; /* Sayısal Zstd sürümü
                                      (MAJOR << 24) | (MINOR << 12) | PATCH */
      const char *zstd_version; /* insan tarafından okunabilir dize. */

      /* 'age' 8 veya daha yüksek olduğunda, aşağıdaki üye de mevcuttur: */
      const char *hyper_version; /* insan tarafından okunabilir dize. */

    } curl_version_info_data;
