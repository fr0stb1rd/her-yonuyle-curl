# Multi ile yürütme

'multi' adı, hepsi aynı tek iş parçacığında yapılan çoklu paralel transferlerde olduğu gibi çoklu (multiple) anlamına gelir. Multi API engellemesizdir (non-blocking), bu nedenle tek transferler için kullanmak da mantıklı olabilir.

Transfer, [yukarıda](../easyhandle.md) açıklandığı gibi hala bir "easy" `CURL *` handle'ında ayarlanır, ancak multi arayüzüyle ayrıca oluşturulmuş bir multi `CURLM *` handle'ına ihtiyacınız vardır ve tüm bireysel transferleri yürütmek için bunu kullanırsınız. Multi handle, bir veya daha fazla easy handle'ı "tutabilir":

    CURLM *multi_handle = curl_multi_init();

Bir multi handle ayrıca `curl_multi_setopt()` ile belirli seçenekleri ayarlayabilir, ancak en basit durumda orada ayarlayacak hiçbir şeyiniz olmayabilir.

Bir multi arayüz transferini yürütmek için, önce multi handle'a aktarılması gereken tüm bireysel easy handle'ları eklemeniz gerekir. Bunları herhangi bir noktada multi handle'a ekleyebilir ve istediğiniz zaman tekrar kaldırabilirsiniz. Bir easy handle'ı bir multi handle'dan kaldırmak ilişkiyi kaldırır ve o belirli transfer hemen durur.

Multi handle'a bir easy handle eklemek kolaydır:

    curl_multi_add_handle( multi_handle, easy_handle );

Birini kaldırmak da bir o kadar kolay yapılır:

    curl_multi_remove_handle( multi_handle, easy_handle );

Gerçekleştirmek istediğiniz transferleri temsil eden easy handle'ları ekledikten sonra, transfer döngüsünü yazarsınız. Multi arayüz ile döngüyü siz yaparsınız, böylece libcurl'den bir dizi dosya tanımlayıcısı (file descriptors) ve bir zaman aşımı değeri isteyebilir ve `select()` çağrısını kendiniz yapabilirsiniz veya bunu bizim için yapan biraz basitleştirilmiş sürümü `curl_multi_wait` ile kullanabilirsiniz. En basit döngü şöyle görünebilir: (*gerçek bir uygulamanın dönüş kodlarını kontrol edeceğini unutmayın*)

    int transfers_running;
    do {
       curl_multi_wait ( multi_handle, NULL, 0, 1000, NULL);
       curl_multi_perform ( multi_handle, &transfers_running );
    } while (transfers_running);

Yukarıdaki örnekte 1000 olarak ayarlanan `curl_multi_wait`'in dördüncü argümanı milisaniye cinsinden bir zaman aşımıdır. Bu, işlevin yine de dönmeden önce herhangi bir etkinlik için beklediği en uzun süredir. `curl_multi_perform`'u tekrar çağırmadan önce çok uzun süre kilitlenmek istemezsiniz çünkü bunu yaparsanız hassasiyetini kaybedebilecek zaman aşımları, ilerleme geri çağırımları ve daha fazlası vardır.

Bunun yerine select()'i kendi başımıza yapmak için, libcurl'den dosya tanımlayıcılarını ve zaman aşımı değerini şöyle çıkarırız (*gerçek bir uygulamanın dönüş kodlarını kontrol edeceğini unutmayın*):

    int transfers_running;
    do {
      fd_set fdread;
      fd_set fdwrite;
      fd_set fdexcep;
      int maxfd = -1;
      long timeout;

      /* zaman aşımı değerini çıkar */
      curl_multi_timeout(multi_handle, &timeout);
      if (timeout < 0)
        timeout = 1000;

      /* select tarafından kullanılabilir yapıya dönüştür */
      timeout.tv_sec = timeout / 1000;
      timeout.tv_usec = (timeout % 1000) * 1000;

      FD_ZERO(&fdread);
      FD_ZERO(&fdwrite);
      FD_ZERO(&fdexcep);

      /* transferlerden dosya tanımlayıcılarını al */
      mc = curl_multi_fdset(multi_handle, &fdread, &fdwrite,
                            &fdexcep, &maxfd);

      if (maxfd == -1) {
        SHORT_SLEEP;
      }
      else
       select(maxfd+1, &fdread, &fdwrite, &fdexcep, &timeout);

      /* zaman aşımı veya okunabilir/yazılabilir soketler */
      curl_multi_perform(multi_handle, &transfers_running);
    } while ( transfers_running );

Bu döngülerin her ikisi de, kendi soketlerinizden veya bir borudan (pipe) veya benzerinden okumanız gibi, beklemek için kendi dosya tanımlayıcılarınızdan birini veya birkaçını kullanmanıza izin verir.

Tekrar: döngü sırasında herhangi bir noktada multi handle'a easy handle'lar ekleyebilir ve kaldırabilirsiniz. Transfer ortasında bir handle'ı kaldırmak o transferi iptal eder.

## Tek bir transfer ne zaman biter?

Yukarıdaki örneklerin gösterdiği gibi, bir program `transfers_running` değişkeninin azaldığını görerek tek bir transferin ne zaman tamamlandığını algılayabilir.

Ayrıca `curl_multi_info_read()` çağrılabilir; bu, bir transfer sona erdiyse bir yapıya (bir "mesaj") işaretçi döndürür ve daha sonra o yapıyı kullanarak o transferin sonucunu öğrenebilirsiniz.

Birden fazla paralel transfer yaptığınızda, aynı `curl_multi_perform` çağrısında elbette birden fazla transfer tamamlanabilir ve o zaman tamamlanan her transfer hakkında bilgi almak için `curl_multi_info_read`'e birden fazla çağrı yapmanız gerekebilir.
