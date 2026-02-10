# TFTP

Önemsiz Dosya Aktarım Protokolü (Trivial File Transfer Protocol - TFTP), bir istemcinin uzak bir ana bilgisayardan dosya almasına veya ona dosya koymasına izin veren basit bir açık metin protokolüdür.

Bu protokol için birincil kullanım durumları, önyükleme görüntüsünü (boot image) yerel bir ağ üzerinden almak olmuştur. TFTP ayrıca, diğer birçok protokolün kullandığı TCP'nin aksine UDP üzerinden yapılması gerçeğiyle diğer birçok protokolün yanında biraz öne çıkar.

TFTP'nin güvenli bir sürümü veya çeşidi yoktur.

## İndirme (Download)

Seçtiğiniz TFTP sunucusundan bir dosya indirin:

    curl -O tftp://localserver/file.boot

## Yükleme (Upload)

Seçtiğiniz TFTP sunucusuna bir dosya yükleyin:

    curl -T file.boot tftp://localserver/

## TFTP seçenekleri

TFTP protokolleri, verileri iletişimin diğer ucuna "bloklar" kullanarak iletir. Bir TFTP transferi kurulduğunda, her iki taraf da ya varsayılan blok boyutu olan 512 baytı kullanmayı kabul eder ya da farklı bir tane üzerinde anlaşır. curl, 8 ila 65464 bayt arasındaki blok boyutlarını destekler.

curl'den varsayılandan farklı bir boyut kullanmasını `--tftp-blksize` ile istersiniz. Şöyle 8192 baytlık bloklar isteyin:

    curl --tftp-blksize 8192 tftp://localserver/file

Seçenek müzakeresini hiç işlemeyen sunucu uygulamaları olduğu gösterilmiştir, bu nedenle curl ayrıca tüm seçenek ayarlama girişimlerini tamamen kapatma yeteneğine de sahiptir. Böyle bir sunucuyla çalışma talihsizliğindeyseniz, bayrağı şöyle kullanın:

    curl --tftp-no-options tftp://localserver/file
