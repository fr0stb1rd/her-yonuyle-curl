# HTTP/3

HTTP/3, seleflerinden birkaç yönden farklıdır. Belki de en belirgin şekilde, HTTP/3, HTTP/2'nin yapabildiği gibi aynı bağlantı üzerinde müzakere edilemez. HTTP/3'ün farklı bir taşıma protokolü kullanması nedeniyle, bunun için özel bir bağlantı kurması ve müzakere etmesi gerekir.

## QUIC

HTTP/3, QUIC üzerinden iletişim kurmak üzere tasarlanmış HTTP sürümüdür. QUIC, çoğu özel amaç için bir TCP+TLS yedeği olarak kabul edilebilir.

Bu nedenle HTTP/3 kullanan tüm transferler TCP kullanmaz. QUIC kullanırlar. QUIC, UDP üzerine inşa edilmiş güvenilir bir taşıma protokolüdür. HTTP/3, QUIC kullanımını ima eder.

## Yalnızca HTTPS

HTTP/3, her zaman TLS kullanan QUIC üzerinden gerçekleştirilir, bu nedenle HTTP/3 tanımı gereği her zaman şifreli ve güvenlidir. Bu nedenle curl, HTTP/3'ü yalnızca `HTTPS://` URL'leri için kullanır.

## Etkinleştirme

Doğrudan HTTP/3'e bir kısayol olarak, curl'ün verilen ana bilgisayar adı ve port numarasına doğrudan bir QUIC bağlantısı kurmaya çalışmasını sağlamak için `--http3` kullanın. Şöyle:

    curl --http3 https://example.com/

Normalde, `--http3` seçeneği olmadan, bir `HTTPS://` URL'si, bir istemcinin ona TCP (ve TLS) kullanarak bağlanması gerektiğini ima eder.

## Çoklama (Multiplexing)

HTTP/3 protokolündeki birincil özellik, aynı fiziksel bağlantı üzerinden birkaç mantıksal akışı çoklama yeteneğidir. curl komut satırı aracı, [paralel transferler yaparken](../../cmdline/urls/parallel.md) bu özellikten yararlanabilir.

## Alt-svc:

HTTP/3'e geçmenin [alt-svc](../https/altsvc.md) yöntemi, bir sunucu için HTTP/3'e önyükleme yapmanın (bootstrapping) resmi yoludur.

Bu özelliğin yerleşik olması gerektiğini ve alt-svc önbelleği zaten dolu değilse *mevcut* istek için HTTP/3'e geçmediğini, bunun yerine bilgiyi ana bilgisayara yapılacak *bir sonraki* istekte kullanmak üzere sakladığını unutmayın.

## QUIC reddedildiğinde

Belirli bir miktarda QUIC bağlantı girişimi başarısız olur; bunun nedeni kısmen birçok ağın ve ana bilgisayarın trafiği engellemesi veya kısıtlamasıdır.

`--http3` kullanıldığında, curl QUIC bağlantısı başlatıldıktan birkaç yüz milisaniye sonra HTTP/2 veya HTTP/1 kullanan ikinci bir transfer girişimi başlatır; böylece QUIC üzerinden bağlantı girişimi başarısız olursa veya dayanılmaz derecede yavaş olursa eski bir HTTP sürümünü kullanan bağlantı yine de başarılı olabilir ve transferi gerçekleştirebilir. Bu, kullanıcıların `--http3`'ü işlemin çalışacağına dair bir miktar güvenle kullanmasını sağlar.

`--http3-only`, paralel olarak eski herhangi bir sürümü denememek, ancak böylece hiçbir QUIC bağlantısı kurulamazsa transferin hemen başarısız olmasını sağlamak için açıkça sağlanmıştır.
