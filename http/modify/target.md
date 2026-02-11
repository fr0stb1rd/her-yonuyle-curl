# İstek hedefi (Request target)

`http://example.com/file` gibi bir giriş URL'si verildiğinde, URL'nin yol (path) bölümü çıkarılır ve HTTP istek satırında `/file` haline getirilir. Protokoldeki bu öğeye HTTP'de *istek hedefi* (request target) denir. Bu, bu isteğin etkileşime girdiği kaynaktır. Normalde bu istek hedefi URL'den çıkarılır ve ardından istekte kullanılır ve bir kullanıcı olarak bunu düşünmenize gerek yoktur.

Bazı nadir durumlarda, kullanıcı yaratıcı olmak ve bu istek hedefini URL'nin gerçekten izin vermediği şekillerde değiştirmek isteyebilir. Örneğin, HTTP OPTIONS yönteminin belirli bir yol için değil *sunucu* ile ilgili sihir için özel olarak tanımlanmış bir istek hedefi vardır ve bunun için `*` kullanır. Evet, tek bir yıldız işareti. Bunu için bir URL belirtmenin bir yolu yoktur, yani OPTIONS gibi bir sunucuya istek hedefinde tek bir yıldız işareti iletmek istiyorsanız, bunu şöyle yapmanız gerekir:

    curl -X OPTIONS --request-target "*" http://example.com/

Bu örnek komut satırı, giden HTTP isteğinin ilk satırının şöyle görünmesini sağlar:

    OPTIONS * HTTP/1.1

## --path-as-is

URL'nin yol kısmı, ana bilgisayar adından sonraki ilk eğik çizgiyle başlayan ve URL'nin sonunda veya bir '?' veya '#' işaretinde (kabaca konuşursak) biten kısımdır.

Yolun içine `/../` veya `/./` içeren alt dizeler eklerseniz, curl, standartlar ve bu tür dizelerin yerel dosya sistemlerinde çalışma eğilimi tarafından dikte edildiği gibi, yol sunucuya gönderilmeden önce bunları otomatik olarak ezer (düzenler). `/../` dizisi önceki bölümü kaldırır, böylece `/hello/sir/../` sadece `/hello/` ile biter ve `/./` basitçe kaldırılır, böylece `/hello/./sir/` `/hello/sir/` olur.

Sunucuya gönderilmeden önce curl'ün bu sihirli dizileri ezmesini *önlemek* ve böylece geçmelerine izin vermek için `--path-as-is` seçeneği mevcuttur.

Sunucuyu `/etc/passwd` dosyasını teslim etmesi için kandırmaya yönelik (beceriksizce) bir girişim:

    curl --path-as-is https://example.com/../../etc/passwd
