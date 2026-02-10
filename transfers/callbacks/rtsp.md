# RTSP serpiştirilmiş veriler

`CURLOPT_INTERLEAVEFUNCTION` seçeneğiyle birlikte geri çağırım.

Bu geri çağırım, bir RTSP transferi yaparken serpiştirilmiş (interleaved) RTP verilerini alır almaz libcurl tarafından çağrılır. Her `$` bloğu için çağrılır ve bu nedenle tam olarak bir üst katman protokol birimi (örneğin bir RTP paketi) içerir. libcurl, her çağrı için serpiştirilmiş başlığın yanı sıra dahil edilen verileri de yazar. İlk bayt her zaman bir ASCII dolar işaretidir. Dolar işareti, bir baytlık bir kanal tanımlayıcısı ve ardından ağ bayt sırasında 2 baytlık bir tamsayı uzunluğu izler. RTP serpiştirmenin nasıl davrandığı hakkında daha fazla bilgi için RFC2326 Bölüm 10.12'ye bakın. Ayarlanmazsa veya NULL olarak ayarlanırsa, curl varsayılan yazma işlevini kullanır.

`CURLOPT_INTERLEAVEDATA` işaretçisi, geri çağırımda userdata argümanında iletilir.
