# Komut satırı kavramları

curl bir komut satırı aracı olarak başladı ve yıllar boyunca sayısız kullanıcı tarafından kabuk istemlerinden (shell prompts) ve komut dosyalarının içinden çağrıldı.

## Çöp girerse çöp çıkar (Garbage in gives garbage out)

curl'ün kendi iradesi pek yoktur. Sizi ve isteklerinizi büyük ölçüde memnun etmeye çalışır. Bu aynı zamanda ona ne verirseniz onunla oynamaya çalıştığı anlamına gelir. Bir seçeneği yanlış yazarsanız, istenmeyen bir şey yapabilir. Biraz geçersiz bir URL verirseniz, curl'ün yine de onunla ilgilenmesi ve devam etmesi muhtemeldir. Bu, bazı seçeneklerde çılgın veriler iletebileceğiniz ve curl'ün bu çılgın verileri transfer işleminde aktarmasını sağlayabileceğiniz anlamına gelir.

Bu bir tasarım tercihidir, çünkü curl'ün protokol iletişimlerini nasıl yaptığını gerçekten ince ayar yapmanıza olanak tanır ve sunucu uygulamalarınıza en yaratıcı yollarla masaj yapmasını sağlayabilirsiniz.

  * [Farklılıklar](differences.md)
  * [Komut satırı seçenekleri](options/README.md)
  * [Yardım](help.md)
  * [Sürüme bağlı seçenekler](versions.md)
  * [URL'ler](urls/README.md)
  * [Yapılandırma dosyası (Config file)](configfile.md)
  * [Değişkenler](variables.md)
  * [Parolalar](passwords.md)
  * [İlerleme göstergesi](progressmeter.md)
  * [Sürüm](curlver.md)
  * [Çıkış kodu (Exit code)](exitcode.md)
  * [curl olarak kopyala](copyas.md)
