# .netrc

Unix sistemleri uzun zamandır kullanıcıların uzak FTP sunucuları için kullanıcı adlarını ve şifrelerini saklamaları için bir yol sunmuştur. ftp istemcileri bunu on yıllardır desteklemiş ve bu sayede kullanıcıların her seferinde kimlik bilgilerini manuel olarak yeniden girmek zorunda kalmadan bilinen sunuculara hızlı bir şekilde giriş yapmalarına izin vermiştir. `.netrc` dosyası tipik olarak bir kullanıcının ev dizininde saklanır. (Windows'ta, ev dizininde iki dosya adı kontrol edilir: `.netrc` ve `_netrc`, ilki tercih edilir. Windows'taki eski sürümler yalnızca `_netrc`'yi kontrol ediyordu.)

Bu yaygın ve iyi kullanılan bir kavram olduğundan, curl de bunu destekler—eğer isterseniz. Ancak curl bu özelliği FTP ile sınırlamaz, bununla herhangi bir protokol için makineler için kimlik bilgileri alabilir. Nasıl yapılacağı hakkında daha fazla bilgi için aşağıya bakın.

## .netrc dosya formatı

.netrc dosya formatı basittir: bir makine adıyla satırlar belirtir ve ardından o makineyle ilişkili giriş ve şifreyi takip edersiniz.

Her alan, bir boşluk veya yeni satırla biten bir harf dizisi olarak sağlanır. 7.84.0 sürümünden bu yana, curl tırnak içine alınmış dizeleri de destekler. Çift tırnakla (`"`) başlar ve biterler ve kaçış karakterli özel harfleri `\"`, (yeni satır), (satır başı) ve (TAB) desteklerler. Tırnak içine alınmış dizeler, bir kullanıcı adı veya şifrede boşluk karakterinin kullanılabilmesinin tek yoludur.

**machine name (makine adı)**

Uzak bir makine adını tanımlar. curl, URL'de belirtilen uzak makineyle eşleşen bir makine belirteci için .netrc dosyasını arar. Bir eşleşme yapıldığında, sonraki .netrc belirteçleri işlenir, dosyanın sonuna ulaşıldığında veya başka bir makineyle karşılaşıldığında durulur.

**default (varsayılan)**

Bu, `default`'un herhangi bir adla eşleşmesi dışında makine adıyla aynıdır. Yalnızca bir varsayılan belirteç olabilir ve tüm makine belirteçlerinden sonra olmalıdır. Başka türlü eşleşmeyen ana bilgisayarlar için varsayılan bir anonim giriş sağlamak üzere, sona şuna benzer bir satır ekleyin:

    default login anonymous password user@domain

**login name (giriş adı)**

Uzak makine için kullanıcı adı dizesi. Adda boşluk kullanamazsınız.

**password string (şifre dizesi)**

Bir şifre sağlayın. Bu belirteç mevcutsa ve uzak sunucu oturum açma işleminin bir parçası olarak bir şifre gerektiriyorsa, curl belirtilen dizeyi sağlar. Bu belirteç .netrc dosyasında mevcutsa, dosyanın kullanıcı dışında kimse tarafından okunamadığından gerçekten emin **olmalısınız**. Şifreyi girerken boşluk kullanamazsınız.

**macdef name**

Bir makro tanımlayın. Bu **curl tarafından desteklenmez**. `.netrc`'nin geri kalanının hala iyi çalışması için, curl bulduğu `macdef` ile yapılan her tanımı düzgün bir şekilde atlar.

'example.com' ana bilgisayarı için 'daniel' adında bir kullanıcı ve 'qwerty' şifresini kullanan örnek bir .netrc şöyle görünür:

    machine example.com
    login daniel
    password qwerty

Aynı işlevsellikle tek bir satıra da yazılabilir:

    machine example.com login daniel password qwerty

## Kullanıcı adı eşleştirme

Bir URL bir kullanıcı adıyla sağlandığında ve .netrc kullanıldığında, curl o makine ve giriş kombinasyonu için eşleşen şifreyi bulmaya çalışır.

## netrc'yi etkinleştir

`-n, --netrc` curl'e .netrc dosyasını aramasını ve kullanmasını söyler.

`--netrc-file [dosya]`, `--netrc`'ye benzer, ancak kullanılacak gerçek dosyanın yolunu da sağlarsınız. Bilgileri başka bir dizinde veya başka bir dosya adıyla sağlamak istediğinizde bu kullanışlıdır.

`--netrc-optional`, `--netrc`'ye benzer, ancak bu seçenek .netrc kullanımını isteğe bağlı hale getirir ve `--netrc` seçeneği gibi zorunlu kılmaz.
