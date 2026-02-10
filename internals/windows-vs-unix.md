# Windows vs Unix

Unix yoluna kıyasla Windows yolunda curl programlamada birkaç fark vardır. Belki de en dikkat çekici dört ayrıntı şunlardır:

## Soket işlemleri için farklı işlev adları

  curl'de bu, tanımlar ve makrolarla çözülür, böylece kaynak kodu bunları tanımlayan başlık dosyası dışında her yerde aynı görünür. Kullanımdaki makrolar `sclose()`, `sread()` ve `swrite()`'tır.

## Init çağrıları

  Windows soket işleri için birkaç init çağrısı gerektirir.

  Bu `curl_global_init()` çağrısı tarafından halledilir, ancak diğer kütüphaneler de bunu yapıyorsa vb. uygulamaların bu davranışı değiştirmesi için nedenler olabilir.

  WinSock sürüm 2.2'ye ihtiyacımız var ve bu sürümü genel başlatma sırasında yüklüyoruz.

## Dosya tanımlayıcıları (File descriptors)

  Ağ iletişimi ve dosya işlemleri için dosya tanımlayıcıları Unix'teki kadar kolay değiştirilebilir değildir.

  Dosya tanımlayıcılarında herhangi bir komik numara denemeyerek bundan kaçınıyoruz.

## Stdout

  stdout'a veri yazarken, Windows satır sonlarını DOS tarzında yapar, böylece ikili verileri yok eder, ancak gelen metinse o dönüşümü istersiniz... (iç çeker)

  Windows altında stdout'u ikiliye ayarlıyoruz

## Ifdefs

Kaynak kodunun içinde, `#ifdef [İşletim Sisteminiz]`'den kaçınmak için çaba gösteriyoruz. Özelliklerle ilgilenen tüm koşullular bunun yerine `#ifdef O_TUHAF_ISLEV_VAR` formatında *olmalıdır*. Windows configure betiklerini çalıştıramadığından, lib dizininde, bir Windows makinesinde bir `curl_config.h` dosyasının görüneceği gibi görünmesi gereken bir `curl_config-win32.h` dosyasını koruyoruz.

Genel olarak konuşursak: curl sıklıkla birkaç düzine işletim sisteminde derlenir. Kenarda yürümeyin.
