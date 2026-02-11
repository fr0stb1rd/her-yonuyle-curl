# İlerleme göstergesi

curl yerleşik bir ilerleme göstergesine sahiptir. curl veri aktarmak (yükleme veya indirme) için çağrıldığında, transferin nasıl ilerlediğini, yani mevcut transfer hızını, ne kadar süredir devam ettiğini ve tamamlanmasına ne kadar kaldığını düşündüğünü göstermek için bu göstergeyi terminal ekranında gösterebilir.

curl, terminale giden bir çıktı olduğuna karar verirse ilerleme göstergesi engellenir, çünkü ilerleme göstergesi bu çıktıya müdahale eder ve görüntülenen şeyi karıştırır. Bir kullanıcı ayrıca curl'e susmasını söyleyen `-s / --silent` seçeneğiyle ilerleme göstergesini zorla kapatabilir.

curl'ü çağırır ve ilerleme göstergesini almazsanız, çıktınızın terminalden başka bir yere yönlendirildiğinden emin olun.

curl ayrıca `-# / --progress-bar` ile etkinleştirebileceğiniz alternatif ve daha basit bir ilerleme göstergesine de sahiptir. Uzun ismin ima ettiği gibi, transferi bunun yerine bir ilerleme çubuğu olarak gösterir.

curl'den veri aktarması istendiğinde, bazen istenen işlemin toplam boyutunu hesaplayamaz ve bu da daha sonra ilerleme göstergesinin daha az ayrıntı içermesine neden olur ve örneğin transfer süreleri vb. için tahminlerde bulunamaz.

## Birimler

İlerleme göstergesi baytları ve saniye başına baytları görüntüler.

Ayrıca 1024 tabanlı sistemi kullanarak daha büyük miktarda bayt için son ekler kullanır, yani 1024 bir kilobayt (1K), 2048 2K vb.'dir. curl şunları destekler:

| Son ek  |  Miktar | İsim      |
|---------|---------|-----------|
| K       | 2^10    | kilobayt  |
| M       | 2^20    | megabayt  |
| G       | 2^30    | gigabayt  |
| T       | 2^40    | terabayt  |
| P       | 2^50    | petabayt  |

Zamanlar saat, dakika ve saniye için H:MM:SS kullanılarak görüntülenir.

## İlerleme göstergesi açıklaması

Bu, transferleri seri bir şekilde yaparken her bir tek transfer için gösterilen ilerleme göstergesidir. Paralel transferler etkinleştirildiğinde, curl bunun yerine aşağıda açıklanan formatı kullanır.

İlerleme göstergesi, kullanıcıya gerçekten bir şeyler olduğunu göstermek için vardır. Çıktıdaki farklı alanlar şu anlama gelir:

    % Total  % Received % Xferd Average Speed          Time             Curr.
                                Dload  Upload Total    Current  Left    Speed
    0  151M  0 38608    0     0  9406      0  4:41:43  0:00:04  4:41:39  9287

Soldan sağa:

| Başlık                 | Anlamı                                                                                             |
|------------------------|----------------------------------------------------------------------------------------------------|
| `%`                    | Tüm transferin tamamlanma yüzdesi                                                                  |
| `Total`                | Beklenen tüm transferin toplam boyutu (biliniyorsa)                                                |
| `%`                    | İndirmenin tamamlanma yüzdesi                                                                      |
| `Received`             | Şu anda indirilen bayt sayısı                                                                      |
| `%`                    | Yüklemenin tamamlanma yüzdesi                                                                      |
| `Xferd`                | Şu anda yüklenen bayt sayısı                                                                       |
| `Average Speed Dload`  | Tüm indirmenin şimdiye kadarki ortalama transfer hızı, saniyedeki bayt sayısı cinsinden            |
| `Average Speed Upload` | Tüm yüklemenin şimdiye kadarki ortalama transfer hızı, saniyedeki bayt sayısı cinsinden            |
| `Time Total`           | İşlemi tamamlamak için beklenen süre, saat, dakika ve saniye için `HH:MM:SS` gösteriminde          |
| `Time Current`         | Transferin başlangıcından bu yana geçen süre, saat, dakika ve saniye için `HH:MM:SS` gösteriminde  |
| `Time Left`            | Tamamlanmaya kalan beklenen süre, saat, dakika ve saniye için `HH:MM:SS` gösteriminde              |
| `Curr. Speed`          | Son 5 saniyedeki ortalama transfer hızı, saniyedeki bayt sayısı cinsinden                          |

## Paralel ilerleme göstergesi

--parallel kullanıldığında, curl birçok transferi aynı anda yapabilir ve o zaman yukarıda belirtilen ilerleme göstergesi gerçekten çalışmaz çünkü tek bir durum satırında çok sayıda transfer hakkındaki durumu kullanıcıya anlatması gerekir.

curl paralel transferler yaptığında, sürecin sonlarına kadar verilerin yalnızca bir alt kümesi hakkında boyut bilgisine sahip olabilir, bu da genellikle birkaç boş alan göstermesine neden olur. Örneğin, ilgili tüm transferlerin beklenen içerik boyutunu bilene kadar toplam beklenen transfer süresini söyleyemez.

    DL% UL%  Dled  Uled  Xfers  Live Total     Current  Left    Speed
    88  --  2682K     0    57    70  --:--:--  0:00:07 --:--:-- 1190k

Soldan sağa:

| Başlık    | Anlamı                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------|
| `DL%`     | İndirmenin tamamlanma yüzdesi                                                                                |
| `UL%`     | Yüklemenin tamamlanma yüzdesi                                                                                |
| `DLed`    | İndirilen bayt sayısı                                                                                        |
| `ULed`    | Yüklenen bayt sayısı                                                                                         |
| `Xfers`   | Tamamlanan transfer sayısı                                                                                   |
| `Live`    | Canlı, devam eden transfer sayısı                                                                            |
| `Total`   | Tüm transferlerin tamamlanması için beklenen toplam süre, saat, dakika ve saniye için `HH:MM:SS` gösteriminde|
| `Current` | Ne kadar süredir çalıştığı, saat, dakika ve saniye için `HH:MM:SS` gösteriminde                              |
| `Left`    | Tamamlanmaya kalan beklenen süre, saat, dakika ve saniye için `HH:MM:SS` gösteriminde                        |
| `Speed`   | Son 5 saniyedeki ortalama transfer hızı, saniyedeki bayt sayısı cinsinden                                    |
