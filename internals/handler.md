# Protokol işleyici (Protocol handler)

libcurl çok protokollü bir transfer kütüphanesidir. Kodun çekirdeği, genel olarak transferler için kullanılan ve çoğu protokol için çoğunlukla aynı şekilde çalışan bir dizi genel işlevdir. Örneğin yukarıda açıklanan ana durum makinesi ordadır ve tüm protokoller için çalışır - bazı protokoller tüm transferler için tüm durumları kullanmasa bile.

Ancak, libcurl'ün konuştuğu her farklı protokolün kendine özgü özellikleri ve uzmanlıkları da vardır. Kodun, protokol XYZ ise, o zaman yap... tarzı koşullarla dolu olmaması için, bunun yerine `Curl_handler` kavramına sahibiz. Desteklenen her protokol bunlardan birini tanımlar ve `lib/url.c` içinde `protocols[]` adında bu tür işleyicilere işaretçilerden oluşan bir dizi vardır.

Bir transfer yapılmak üzereyken, libcurl üzerinde işlem yapacağı URL'yi ayrıştırır ve diğer şeylerin yanı sıra hangi protokolü kullanacağını bulur. Normalde bu, URL'nin şema kısmına bakarak yapılabilir. `https://example.com` için bu `https`'tir ve `imaps://example.com` için `imaps`'tir. Sağlanan şemayı kullanarak libcurl, `conn->handler` işaretçisini bu URL'yi işleyen protokol için işleyici yapısına ayarlar.

![libcurl protokol işleyicileri](slide-protocol-handlers.jpg)

İşleyici yapısı, NULL olabilen veya o protokolün bir transfer için çalışması için gerekli şeyleri yapmak üzere protokole özgü bir işleve işaret edecek şekilde ayarlanabilen bir dizi işlev işaretçisi içerir. Diğer tüm protokollerin ihtiyaç duymadığı şeyler. İşleyici yapısı ayrıca protokolün adını ayarlar ve özellik setini bir bit maskesiyle açıklar.

Bir libcurl transferi, bir dizi farklı eylem etrafında oluşturulur ve işleyici bunların her birini genişletebilir. İşte bu yapıda bazı örnek işlev işaretçileri ve bunların nasıl kullanıldığı:

## Bağlantı kurulumu (Setup connection)

Bir bağlantı bir transfer için yeniden kullanılamazsa, URL'de verilen ana bilgisayara bir bağlantı kurması gerekir ve bunu yaptığında, bunun için protokol işleyicisinin işlevini de çağırabilir. Şöyle:

    if(conn->handler->setup_connection)
      result = conn->handler->setup_connection(data, conn);

## Bağlan (Connect)

Bir bağlantı kurulduktan sonra, bu işlev çağrılır

    if(conn->handler->connect_it)
      result = conn->handler->connect_it(data, &done);

## Yap (Do)

*Do simply* (Yap), URL'nin tanımladığı belirli kaynak için bir istek yayınlayan eylemdir. Tüm protokollerin bir do eylemi vardır, bu nedenle bu işlev sağlanmalıdır:

    result = conn->handler->do_it(data, &done);

## Bitti (Done)

Bir transfer tamamlandığında, *done* eylemi gerçekleştirilir:

    result = conn->handler->done(data, status, premature);

## Bağlantıyı kes (Disconnect)

Bağlantı kesilmek üzeredir.

    result = conn->handler->disconnect(data, conn, dead_connection);
