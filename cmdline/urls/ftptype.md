# FTP türü

Bu yaygın olarak kullanılan bir özellik değildir.

FTP sunucularındaki dosyaları tanımlayan URL'ler, istemciye (bu durumda curl) kaynağın hangi dosya türü olduğunu söylemenize de izin veren özel bir özelliğe sahiptir. Bunun nedeni FTP'nin biraz özel olması ve bir transfer için mod değiştirebilmesi ve böylece dosyayı başka bir mod kullanıyormuş gibi farklı şekilde işleyebilmesidir.

URL'ye `;type=A` ekleyerek curl'e FTP kaynağının bir ASCII türü olduğunu söylersiniz. `example.com`un kök dizininden `foo` dosyasını ASCII kullanarak almak şu şekilde yapılabilir:

    curl "ftp://example.com/foo;type=A"

curl, FTP için ikili transferleri varsayılan olarak kullanır, ancak URL formatı `type=I` ile ikili türü belirtmenize olanak tanır:

    curl "ftp://example.com/foo;type=I"

Son olarak, ilettiğiniz tür D ise, curl'e tanımlanan kaynağın bir dizin olduğunu söyleyebilirsiniz:

    curl "ftp://example.com/foo;type=D"

…bu, yukarıda belirtildiği gibi yolu eğik çizgiyle (trailing slash) sonlandırmak yerine alternatif bir format olarak çalışabilir.
