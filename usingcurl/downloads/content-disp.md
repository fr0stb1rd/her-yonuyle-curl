# Sunucudan gelen hedef dosya adını kullanma

HTTP sunucuları, yanıtlarda `Content-Disposition:` adında bir başlık sağlama seçeneğine sahiptir. Bu başlık, teslim edilen içerikler için önerilen bir dosya adı içerebilir ve curl'e yerel dosyasını adlandırmak için bu ipucunu kullanması söylenebilir. `-J / --remote-header-name` bunu etkinleştirir. Ayrıca `-O` seçeneğini de kullanırsanız, curl'ün varsayılan olarak URL'den gelen dosya adını kullanmasını sağlar ve yalnızca *eğer* gerçekten geçerli bir `Content-Disposition` başlığı mevcutsa, o adı kullanarak kaydetmeye geçer.

*Birden fazla* Content-Disposition başlığı varsa, curl gördüğü ilk başlıktan adı seçer.

Varsayılan olarak curl o dosyayı geçerli dizininize kaydeder, bu `--output-dir` ile değiştirilebilir.

`-J`'nin kullanıcıların dikkat etmesi gereken bazı zorlukları ve riskleri vardır:

- Yalnızca önerilen dosya adının en sağdaki kısmını kullanır; yol kısmı çıkarılır.

- Dosya adı sunucu tarafından sağlandığından, sunucu böyle bir dosya adı sağlarsa ( `--clobber` kullanmadığınız sürece) curl geçerli dizininizdeki önceden var olan herhangi bir yerel dosyanın üzerine yazmaz.

- dosya adı kodlaması ve karakter seti sorunları. curl adı hiçbir şekilde çözmez, bu nedenle bir tarayıcının aksi takdirde mantıklı bir karakter seti kullanarak daha okunabilir bir şeye çözeceği URL kodlu bir dosya adıyla baş başa kalabilirsiniz.

## Location: da

Yukarıda bahsedilen yaklaşım oldukça iyi çalışır, ancak sınırlamaları vardır. Bunlardan biri, sitenin bir `Content-Disposition` başlığı sağlamak yerine istemciyi indirmek için yeni bir URL'ye yönlendirmesi durumunda, curl'ün yeni adı almaması, bunun yerine orijinal olarak sağlanan URL'den gelen adı kullanmaya devam etmesidir.

curl 8.19.0'dan bu yana, -J aynı zamanda `Location:` başlıklarından dosya adını alır ve `Content-Disposition` başlığı gelmezse bu dosya adını kullanır.

Şunun gibi bir komut satırı çalıştırırsanız:

    curl -L -O -J https://example.com/download?id=6347d

Sitenin curl'ü indirmek istediğiniz tarball için gerçek indirme URL'sine şöyle yönlendirdiğini varsayarsak:

    HTTP/1 301 redirect

    Location: https://example.org/release.tar.gz

Bu, curl'ün o transferin içeriğini `release.tar.gz` adlı yerel bir dosyaya kaydetmesini sağlar.

Eğer *hem* bir yönlendirme *hem de* bir `Content-Disposition` başlığı varsa, ikincisi önceliklidir.

## Hangi dosya adı?

Verileri saklamak için kullanılan seçilen son ad, sunucudan geçirilen bir başlığın içeriğine göre seçildiğinden, bu seçeneği bir komut dosyası senaryosunda kullanmak şu zorluğu getirir: curl aslında hangi dosya adını kullandı?

Bir kullanıcı curl'ün [-w seçeneği](../verbose/writeout.md) ile bu bilgiyi kolayca çıkarabilir. Şöyle:

    curl -w '%{filename_effective}' -O -J -L \
      https://example.com/download?id=6347d

Bu komut satırı kullanılan dosya adını stdout'a çıktılar.

Komut satırını, o adı stderr'e veya belirli bir dosyaya vb. yönlendirmek için daha da değiştirin. Neyin işe yaradığını düşünüyorsanız.
