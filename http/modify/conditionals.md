# Koşullular (Conditionals)

Bazen kullanıcılar, aynı dosya belki bir gün önce zaten indirilmişse, bir dosyayı tekrar indirmekten kaçınmak isterler. Bu, HTTP transferini bir şeye koşullandırarak yapılabilir. curl iki farklı koşulu destekler: dosya zaman damgası ve etag.

## Değiştirilme tarihine göre kontrol et

Dosyayı `-z` veya `--time-cond` seçeneğiyle yalnızca belirli bir tarihten daha yeniyse indirin:

    curl -z "Jan 10, 2017" https://example.com/file -O

Veya tam tersi, tarihin başına bir tire koyarak dosyayı yalnızca belirli bir zamandan daha eskiyse alın:

    curl --time-cond "-Jan 10, 2017" https://example.com/file -O

Tarih ayrıştırıcısı liberaldir ve tarihi yazabileceğiniz çoğu biçimi kabul eder ve ayrıca bir saat ile tam olarak belirtebilirsiniz:

    curl --time-cond "Sun, 12 Sep 2004 15:05:58 -0700" \
      https://www.example.org/file.html

`-z` seçeneği ayrıca yerel bir dosyadan zaman damgasını çıkarabilir ve kullanabilir, bu da bir dosyayı yalnızca uzaktan güncellenmişse indirmek için kullanışlıdır:

    curl -z file.html https://example.com/file.html -O

`-z` kullanımını yerel olarak oluşturulan dosyanın zamanını uzak dosyanın sahip olduğu zaman damgasıyla aynı zamana ayarlayan `--remote-time` bayrağıyla birleştirmek genellikle yararlıdır:

    curl -z file.html -o file.html --remote-time https://example.com/file.html

## İçeriğin değiştirilmesine göre kontrol et

HTTP sunucuları, belirli bir kaynak sürümü için belirli bir *ETag* döndürebilir. Belirli bir URL'deki kaynak değişirse, yeni bir Etag değeri oluşturulmalıdır, böylece bir istemci ETag aynı kaldığı sürece içeriğin değişmediğini bilir.

ETag'leri kullanarak curl, zamanlara veya dosya tarihlerine güvenmek zorunda kalmadan uzaktan güncellemeleri kontrol edebilir. Bu ayrıca kontrolün saniye altı değişiklikleri algılamasını da sağlar ki zaman damgası tabanlı kontroller bunu yapamaz.

curl kullanarak uzak bir dosyayı indirebilir ve ETag'ini (eğer sağlıyorsa), `--etag-save` komut satırı seçeneğini kullanarak ayrı bir önbelleğe kaydedebilirsiniz. Şunun gibi:

    curl --etag-save etag.txt https://example.com/file -o output

Daha sonraki bir komut satırı, daha önce kaydedilmiş bu etag'i kullanabilir ve dosyayı yalnızca değişmişse tekrar indirdiğinden emin olabilir, şöyle:

    curl --etag-compare etag.txt https://example.com/file -o output

İki etag seçeneği aynı komut satırında da birleştirilebilir, böylece dosya gerçekten güncellendiyse curl güncelleme ETag'ini dosyaya tekrar kaydeder:

    curl --etag-compare etag.txt --etag-save etag.txt \
      https://example.com/file -o output
