# İkili (Binary) gönderme

Bir dosyadan gönderilecek verileri okurken, `-d` satır başlarını ve yeni satırları çıkarır. curl'ün verilen dosyayı tam olarak verildiği gibi ikili (binary) olarak okumasını ve kullanmasını istiyorsanız `--data-binary` kullanın:

    curl --data-binary @filename http://example.com/
