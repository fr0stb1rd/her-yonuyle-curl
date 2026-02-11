# HTTP PUT

PUT ve POST arasındaki fark incedir. Farklı yöntem dizeleri dışında hemen hemen aynı iletimlerdir. POST'un verileri uzak bir kaynağa iletmesi amaçlanırken, PUT'un o kaynağın yeni sürümü olması amaçlanır.

Bu açıdan PUT, diğer protokollerde bulunan eski güzel standart dosya yüklemesine benzer. Kaynağın yeni bir sürümünü PUT ile yüklersiniz. URL kaynağı tanımlar ve siz oraya koyulacak yerel dosyayı işaret edersiniz:

    curl -T localfile http://example.com/new/resource/file

`-T` bir PUT anlamına gelir ve curl'e hangi dosyanın gönderileceğini söyler. POST ve PUT arasındaki benzerlikler, `-d` kullanan normal curl POST mekanizmasını kullanarak ancak bunun yerine bir PUT kullanmasını isteyerek bir dize (string) ile bir PUT göndermenize de olanak tanır:

    curl -d "data to PUT" -X PUT http://example.com/new/resource/file
