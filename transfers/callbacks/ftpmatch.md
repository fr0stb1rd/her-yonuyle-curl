# FTP joker karakter eşleştirme

libcurl, FTP joker karakter eşleştirmeyi destekler. Bu özelliği `CURLOPT_WILDCARDMATCH` seçeneğini `1L` olarak ayarlayarak ve ardından URL'nin dosya adı kısmında bir "joker karakter deseni" kullanarak kullanırsınız.

## Joker karakter desenleri

Varsayılan libcurl joker karakter eşleştirme işlevi şunları destekler:

`*` - ASTERISK (Yıldız)

    ftp://example.com/some/path/*.txt

`some/path` dizinindeki tüm txt dosyalarıyla eşleşmesi için. Aynı desen dizesi içinde yalnızca iki yıldıza izin verilir.

`?` - SORU İŞARETİ

Bir soru işareti herhangi bir (tam olarak bir) karakterle eşleşir. `photo1.jpeg` ve `photo7.jpeg` adında dosyalarınız varsa, bu desen onlarla eşleşebilir:

    ftp://example.com/some/path/photo?.jpeg

`[` - KÖŞELİ PARANTEZ İFADESİ

Sol köşeli parantez bir köşeli parantez ifadesi açar. Soru işareti ve yıldızın köşeli parantez ifadesinde özel bir anlamı yoktur. Her köşeli parantez ifadesi sağ köşeli parantez (`]`) ile biter ve tam olarak bir karakterle eşleşir. Bazı örnekler şunlardır:

`[a-zA-Z0-9]` veya `[f-gF-G]` - karakter aralıkları

`[abc]`  - karakter numaralandırması

`[^abc]` veya `[!abc]` - olumsuzlama

`[[:name:]]` sınıf ifadesi. Desteklenen sınıflar alnum, lower, space, alpha, digit, print, upper, blank, graph, xdigit.

`[][-!^]` - özel durum, yalnızca `\-`, `]`, `[`, `!` veya `^` ile eşleşir.

`[\\[\\]\\\\]` - kaçış sözdizimi. `[`, `]` veya `\\` ile eşleşir.

Yukarıdaki kuralları kullanarak bir dosya adı deseni oluşturulabilir:

    ftp://example.com/some/path/[a-z[:upper:]\\\\].jpeg

## FTP yığın geri çağırımları

FTP joker karakter eşleştirme kullanıldığında, eşleşen bir dosya için bir transfer başlatılmadan önce `CURLOPT_CHUNK_BGN_FUNCTION` geri çağırımı çağrılır.

Geri çağırım daha sonra libcurl'e dosya ile ne yapılacağını söylemek için bu dönüş kodlarından birini döndürmeyi seçebilir:

 - `CURL_CHUNK_BGN_FUNC_OK` dosyayı transfer et
 - `CURL_CHUNK_BGN_FUNC_SKIP`
 - `CURL_CHUNK_BGN_FUNC_FAIL` hata nedeniyle dur

Eşleşen dosya transfer edildikten veya atlandıktan sonra, `CURLOPT_CHUNK_END_FUNCTION` geri çağırımı çağrılır.

Son yığın geri çağırımı yalnızca başarı veya hata döndürebilir.

## FTP eşleştirme geri çağırımı

Varsayılan desen eşleştirme işlevi hoşunuza gitmiyorsa, `CURLOPT_FNMATCH_FUNCTION` seçeneğini alternatifinize ayarlayarak kendi değiştirme işlevinizi sağlayabilirsiniz.
