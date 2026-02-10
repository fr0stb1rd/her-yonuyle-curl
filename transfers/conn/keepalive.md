# Canlı tutma (Keep alive)

Bir TCP bağlantısı kurulduktan sonra, bu bağlantı bir taraf onu kapatana kadar geçerli olarak tanımlanır. Bağlantı bağlı duruma girdiğinde, süresiz olarak bağlı kalacaktır. Gerçekte, bağlantı süresiz olarak sürmeyecektir. Birçok güvenlik duvarı veya NAT sistemi, bir süre boyunca etkinlik olmadıysa bağlantıları kapatır. Canlı Tutma (Keep Alive) sinyali, ara ana bilgisayarların hareketsizlik nedeniyle boşta kalan bağlantıyı kapatmasını önlemek için kullanılabilir.

libcurl, oluşturduğu bağlantılar için TCP Canlı tutmayı etkinleştirmek ve kontrol etmek üzere birkaç seçenek sunar. Özelliği açmak/kapatmak için bir ana boolean seçenek vardır ve ilgili sayaçlar ve zaman aşımları için *üç* ayrı seçenek vardır.

Bu yöntemin boşta kalan bağlantıları kapatan orta kutuları (middle boxes) yenmeye çalışmasına rağmen, canlı tutma sondalarını (probes) basitçe görmezden gelen kutuların da olduğu belirtilebilir. Bunun gerçekten işe yarayacağının garantisi yoktur.

## Canlı tutmayı etkinleştir

Etkinleştirmek için `CURLOPT_TCP_KEEPALIVE` long değerini 1'e, devre dışı bırakmak için 0'a ayarlayın. Etkinleştirilirse, libcurl bu handle'ı kullanarak oluşturduğu herhangi bir yeni TCP bağlantısında TCP Canlı Tutma seçeneklerini ayarlayacaktır. UDP veya QUIC gibi diğer protokolleri kullanarak bağlantılar oluşturursa, bu bağlantılar etkilenmeyecektir.

## Boşta kalma süresi (Idle time)

İlk canlı tutma sondasını göndermeden önce bağlantının boşta kalmasını istediğiniz saniye sayısına `CURLOPT_TCP_KEEPIDLE` long değerini ayarlarsınız. Varsayılan değer 60 saniyedir. Bunu en katı orta kutunuzdaki zaman sınırından biraz daha düşük bir zamana ayarlamaya çalışmak mantıklıdır.

## Sonda aralığı (Probe interval)

Sonraki canlı tutma sondaları arasında beklenecek saniye sayısı için `CURLOPT_TCP_KEEPINTVL` long değerini ayarlayın. İlk canlı tutma sondası gönderildikten sonra gelen sondalar. Varsayılan 60 saniyedir.

## Sonda sayısı (Probe count)

Bazen canlı tutma yeniden denemesi olarak anılır. Uzak ucun mevcut olmadığını ilan etmeden ve bağlantıyı kapatmadan önce gerçekleştirilecek yeniden iletim sayısını tutan `CURLOPT_TCP_KEEPCNT` long değerini ayarlayın. Varsayılan 9'dur. Bu libcurl seçeneği, önceki seçeneklerden çok sonra 8.9.0'da eklendi.

## Örnek

TCP canlı tutmayı kullanarak transfer yapan küçük bir libcurl uygulaması örneği.

    int main(void)
    {
      CURL *curl = curl_easy_init();
      if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "https://example.com");

        /* bu transfer için TCP keep-alive etkinleştir */
        curl_easy_setopt(curl, CURLOPT_TCP_KEEPALIVE, 1L);

        /* keep-alive boşta kalma süresi 120 saniye */
        curl_easy_setopt(curl, CURLOPT_TCP_KEEPIDLE, 120L);

        /* keep-alive sondaları arasındaki zaman aralığı: 60 saniye */
        curl_easy_setopt(curl, CURLOPT_TCP_KEEPINTVL, 60L);

        /* maksimum keep-alive sonda sayısı: 3 */
        curl_easy_setopt(curl, CURLOPT_TCP_KEEPCNT, 3L);

        curl_easy_perform(curl);
      }
    }

## HTTP `Keep-Alive`

HTTP/1.0 için `Connection:` başlığında kullanılan `Keep-Alive` adlı eski bir anahtar kelime vardı. Tamamen ayrı bir işlevselliğe sahiptir ve TCP Canlı Tutma ile ilgili değildir: bağlantının sonraki transferlerde kalıcı kullanım için canlı tutulması gerektiği anlamına geliyordu. Bu, HTTP 1.1'de varsayılan hale geldi.

## QUIC ve HTTP/2

Hem QUIC hem de HTTP/2, iletişimde yer alan iki eş arasında gönderilebilen ve daha sonra TCP Canlı Tutma ile benzer etkilere sahip PING çerçevelerine (frames) sahiptir. Ancak bu seçenekler libcurl'ün PING çerçevelerini kullanımını kontrol etmez.
