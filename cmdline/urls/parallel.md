# Paralel transferler

Belirtilen URL'leri seri bir şekilde tek tek almanın varsayılan davranışı, her URL'nin tam olarak ne zaman getirildiğini anlamayı kolaylaştırır ancak yavaş olabilir.

curl, bunun yerine curl'e belirtilen transferleri paralel bir şekilde yapmaya çalışmasını emreden `-Z` (veya `--parallel`) seçeneğini sunar. Bu etkinleştirildiğinde, curl seri yerine aynı anda birçok transfer gerçekleştirir. Varsayılan olarak aynı anda 50'ye kadar transfer yapar ve bunlardan biri tamamlanır tamamlanmaz bir sonraki başlatılır.

Farklı kaynaklardan birçok dosya indirmek istediğiniz ve bunlardan bazılarının yavaş, bazılarının hızlı olabileceği durumlar için bu, işleri muazzam bir şekilde hızlandırabilir.

50 paralel transfer sizin için yanlışsa, bu miktarı değiştirmenize izin vermek için `--parallel-max` seçeneği mevcuttur.

## Paralel transfer ilerleme göstergesi

Doğal olarak, tek bir transfer için dosya transferi ilerlemesini gösteren sıradan ilerleme göstergesi ekranı paralel transferler için o kadar yararlı değildir, bu nedenle curl paralel transferler gerçekleştirdiğinde, tek bir satırda mevcut devam eden tüm transferler hakkında bilgi görüntüleyen farklı bir ilerleme göstergesi gösterir.

## Multiplex öncesi bağlantı

curl'den paralel transferler yapması istendiğinde, önceden var olan bağlantılar üzerinden ek transfer yeniden kullanımı ve çoklamanın (multiplexing) gerçekleşmesine öncelik verir. Bu, gerekli toplam bağlantı miktarını (ve dolayısıyla kaynakları) potansiyel olarak azaltabilir, ancak başlangıçta biraz daha yavaş olabilir.

`--parallel-immediate` ile, curl'e önceliklendirmeyi tersine çevirmesi ve transferin başka bir bağlantıda çoklanıp çoklanamayacağını görmek için biraz beklemeyi göze almak yerine hemen yeni bir bağlantı oluşturmayı tercih etmesi talimatı verilir.
