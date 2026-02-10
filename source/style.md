# Kod stili

Ortak bir stile sahip kaynak kodunun okunması, farklı yerlerde farklı stiller kullanan koddan daha kolaydır. Kodun tek bir sürekli kod tabanı gibi hissettirmesine yardımcı olur. Okunması kolay olmak kodun önemli bir özelliğidir ve yeni şeyler eklendiğinde gözden geçirmeyi kolaylaştırmaya yardımcı olur ve geliştiriciler işlerin neden ters gittiğini anlamaya çalışırken kodda hata ayıklamaya yardımcı olur. Birleşik bir stil, bireysel katılımcıların kendi kişisel zevklerinin tatmin edilmesinden daha önemlidir.

C kodumuzun birkaç stil kuralı vardır. Bunların çoğu `checksrc.pl` komut dosyası tarafından doğrulanır ve desteklenir. `make checksrc` ile veya `./configure --enable-debug` kullanıldıktan sonra derlendiğinde derleme sistemi tarafından varsayılan olarak çağrılır.

Kaynak kodunda zaten kullanılan stili kopyalamanız gerektiğinden ve kural setimizde özellikle alışılmadık kurallar olmadığından, yönergeleri takip etmek normalde kimse için bir sorun değildir.

Ayrıca tüm büyük platformlarda ve genel olarak mümkün olduğunca çok platformda uyarısız (warning-free) kod yazmak için çok çalışıyoruz. Açıkça uyarılara neden olan kod olduğu gibi kabul edilmez.

## İsimlendirme

Yeni işlevleriniz ve değişken isimleriniz için kafa karıştırıcı olmayan bir isimlendirme şeması kullanmayı deneyin. Bu mutlaka kodun diğer yerlerindekiyle aynısını kullanmanız gerektiği anlamına gelmez, sadece isimlerin mantıklı, anlaşılır ve ne için kullanıldıklarına göre isimlendirilmesi gerektiği anlamına gelir. Dosya-yerel işlevler statik (static) yapılmalıdır. Küçük harfli isimleri severiz.
Tüm halka açık kullanım amaçlı semboller `curl` ile başlamalıdır. Küresel dahili semboller `Curl` ile başlar.

## Girintileme (Indentation)

Girintileme için sadece boşluk kullanırız, asla TAB kullanmayız. Her yeni açık parantez için iki boşluk kullanırız.

    if(something_is_true) {
      while(second_statement == fine) {
        moo();
      }
    }

## Yorumlar

C89 kodu yazdığımız için, `//` yorumlarına izin verilmez. Bunlar C99'a kadar C standardına dahil edilmemiştir. Sadece `/* comments */` kullanırız.

    /* bu bir yorumdur */

## Uzun satırlar

curl'deki kaynak kodu asla 79 sütundan daha geniş olamaz. Büyük ve yüksek çözünürlüklü ekranların olduğu modern çağda bile bunu sürdürmenin iki nedeni vardır:

1. Daha dar sütunların okunması geniş olanlardan daha kolaydır. Gazetelerin on yıllardır veya yüzyıllardır sütun kullanmasının bir nedeni var.

2. Daha dar sütunlar, geliştiricilerin kodun birden fazla parçasını farklı pencerelerde yan yana daha kolay görüntülemesine olanak tanır. Ben sıklıkla aynı ekranda yan yana iki veya üç kaynak kodu penceresinin yanı sıra birden fazla terminal ve hata ayıklama penceresine sahibim.

## Parantezler (Braces)

if/while/do/for ifadelerinde, açık parantezi (süslü parantez) anahtar kelimeyle aynı satıra yazarız ve ardından kapanış parantezini ilk anahtar kelimeyle aynı girinti düzeyine koyarız. Şunun gibi:

    if(yas < 40) {
      /* açıkça bir genç */
    }

Sadece tek satırlık bir ifade içereceklerse parantezleri atlayabilirsiniz:

    if(!x)
      continue;

Fonksiyonlar için açılış parantezi ayrı bir satırda olmalıdır:

    int main(int argc, char **argv)
    {
      return 1;
    }

## Sonraki satırda else

Parantez kullanarak koşullu bir ifadeye bir `else` cümlesi eklerken, onu kapanış parantezinden sonra yeni bir satıra ekleriz. Şunun gibi:

    if(yas < 40) {
      /* açıkça bir genç */
    }
    else {
      /* muhtemelen zeki */
    }

## Parantezlerden önce boşluk yok

if/while/do/for kullanarak ifadeler yazarken, anahtar kelime ile açık parantez arasında boşluk olmamalıdır. Şunun gibi:

    while(1) {
      /* sonsuza kadar döngü */
    }

## Mantıksal (Boolean) koşullar kullanın

if/while koşullarında bool gibi koşullu bir değeri TRUE veya FALSE'a karşı, bir işaretçiyi (pointer) NULL veya != NULL'a karşı ve bir int'i sıfır veya sıfır olmayana karşı test etmek yerine şunları tercih ederiz:

    sonuc = bir_sey_yap();
    if(!sonuc) {
      /* bir şeyler ters gitti */
      return sonuc;
    }

## Koşullarda atama yok

Okunabilirliği artırmak ve koşulların karmaşıklığını azaltmak için if/while koşulları içinde değişken atamaktan kaçınırız. Bu stile hoş bakmayız:

    if((ptr = malloc(100)) == NULL)
      return NULL;

Bunun yerine yukarıdaki sürümün daha net bir şekilde yazılmasını teşvik ediyoruz:

    ptr = malloc(100);
    if(!ptr)
      return NULL;

## Yeni bloğu yeni bir satırda

Kısa if() koşulları için bile olsa, aynı kaynak satırına asla birden fazla ifade yazmayız.

    if(a)
      return TRUE;
    else if(b)
      return FALSE;

Asla:

    if(a) return TRUE;
    else if(b) return FALSE;

## Operatörler etrafında boşluk

Lütfen C ifadelerinde operatörlerin her iki tarafında da boşluk kullanın. Sontakı (Postfix) **(), [], ->, ., ++, --** ve Tekil (Unary) **+, -, !, ~, &** operatörleri hariç, bunlarda boşluk olmamalıdır.

Örnekler:

    bla = func();
    who = name[0];
    age += 1;
    true = !false;
    size += -2 + 3 * (a + b);
    ptr->member = a++;
    struct.field = b--;
    ptr = &address;
    contents = *pointer;
    complement = ~bits;
    empty = (!*string) ? TRUE : FALSE;

## Dönüş değerleri için parantez yok

'return' ifadesini değerin etrafında fazladan parantez olmadan kullanırız:

    int calisir(void)
    {
      return TRUE;
    }

## sizeof argümanları için parantezler

Kodda sizeof operatörünü kullanırken, argümanı etrafında parantezlerle yazılmasını tercih ederiz:

    int size = sizeof(int);

## Sütun hizalama

Bazı ifadeler tek bir satırda tamamlanamaz çünkü satır çok uzun olur, ifadenin okunması çok zor olur veya yukarıdaki diğer stil yönergeleri nedeniyle. Böyle bir durumda ifade birden çok satıra yayılır.

Bir devam satırı bir ifadenin veya alt ifadenin parçasıysa, o zaman uygun sütunda hizalamalısınız, böylece ifadenin hangi parçası olduğunu söylemek kolay olur. Operatörler devam satırlarını başlatmamalıdır. Diğer durumlarda 2 boşluklu girinti kılavuzunu izleyin. İşte libcurl'den bazı örnekler:

    if(Curl_pipeline_wanted(handle->multi, CURLPIPE_HTTP1) &&
       (handle->set.httpversion != CURL_HTTP_VERSION_1_0) &&
       (handle->set.httpreq == HTTPREQ_GET ||
        handle->set.httpreq == HTTPREQ_HEAD))
      /* did not ask for HTTP/1.0 and a GET or HEAD */
      return TRUE;

Parantez yoksa, varsayılan girintiyi kullanın:

    data->set.http_disable_hostname_check_before_authentication =
      (0 != va_arg(param, long)) ? TRUE : FALSE;

Açık bir parantez ile fonksiyon çağırma:

    if(option) {
      result = parse_login_details(option, strlen(option),
                                   (userp ? &user : NULL),
                                   (passwdp ? &passwd : NULL),
                                   NULL);
    }

"Mevcut açık" parantez ile hizalama:

    DEBUGF(infof(data, "Curl_pp_readresp_ %d bytes of trailing "
                 "server response left\n",
                 (int)clipamount));

## Platforma bağımlı kod

Koşullu kod yapmak için **#ifdef HAVE_FEATURE** kullanın. #ifdef satırlarında belirli işletim sistemlerini veya donanımları kontrol etmekten kaçınırız. HAVE_FEATURE, unix benzeri sistemler için configure betiği tarafından oluşturulmalı ve diğerleri için `config-[system].h` dosyalarında sabit olarak kodlanmalıdır.

Ayrıca, kodu sorunsuz hale getirmek için, libcurl o özellik olmadan oluşturulduğunda muhtemelen boş olan veya sabitlere tanımlanan makroların/işlevlerin kullanılmasını teşvik ediyoruz. **magic()** işlevinin bir derleme zamanı koşuluna (build-time conditional) bağlı olarak farklı çalıştığı bu örnek gibi:

    #ifdef HAVE_MAGIC
    void magic(int a)
    {
      return a + 2;
    }
    #else
    #define magic(x) 1
    #endif

    int content = magic(3);

## Typedef edilmiş struct'lar yok

Struct'ları kesinlikle kullanın, ancak onları typedef yapmayın. Onları tanımlamanın `struct name` yolunu kullanın:

    struct something {
       void *valid;
       size_t way_to_write;
    };
    struct something instance;


**Uygun değil**:

    typedef struct {
       void *wrong;
       size_t way_to_write;
    } something;
    something instance;
