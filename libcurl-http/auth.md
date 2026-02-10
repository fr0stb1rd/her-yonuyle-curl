# Kimlik Doğrulama

libcurl çok çeşitli HTTP kimlik doğrulama şemalarını destekler.

Bu kimlik doğrulama yönteminin, günümüzde web'de yaygın olarak kullanılan ve kimlik doğrulamanın bir HTTP POST ile gerçekleştirildiği ve ardından durumun çerezlerde tutulduğu şemadan farklı olduğunu unutmayın. Bunun nasıl yapılacağına dair ayrıntılar için [libcurl ile Çerezler](cookies.md) bölümüne bakın.

## Kullanıcı adı ve şifre

libcurl, verilen bir kullanıcı adı olmadan herhangi bir HTTP kimlik doğrulamasını denemez. Şöyle bir tane ayarlayın:

    curl_easy_setopt(curl, CURLOPT_USERNAME, "joe");

ve elbette çoğu kimlik doğrulaması ayrıca ayrı olarak ayarladığınız bir şifre gerektirir:

    curl_easy_setopt(curl, CURLOPT_PASSWORD, "secret");

İhtiyacınız olan tek şey budur. Bu, libcurl'ün bu transfer için varsayılan kimlik doğrulama yöntemini açmasını sağlar: *HTTP Basic*.

## Kimlik doğrulama gerekli

Bir istemci, kimliği doğrulanmış bir istek göndermek istediğine kendisi karar vermez. Bu sunucunun gerektirdiği bir şeydir. Sunucunun korunan ve kimlik doğrulama gerektiren bir kaynağı olduğunda, bir 401 HTTP yanıtı ve bir `WWW-Authenticate:` başlığı ile yanıt verir. Başlık, o kaynak için hangi belirli kimlik doğrulama yöntemlerini kabul ettiğine dair ayrıntıları içerir.

## Basic

Basic varsayılan HTTP kimlik doğrulama yöntemidir ve adından da anlaşılacağı gibi gerçekten basittir. Adı ve şifreyi alır, bunları iki nokta üst üste ile ayırır ve tüm şeyi isteğe bir `Authorization:` HTTP başlığına koymadan önce o dizeyi base64 ile kodlar.

Ad ve şifre yukarıda gösterilen örneklerdeki gibi ayarlanırsa, tam giden başlık şöyle görünür:

    Authorization: Basic am9lOnNlY3JldA==

Bu kimlik doğrulama yöntemi, kimlik bilgileri ağ üzerinden düz metin olarak gönderildiğinden HTTP üzerinden tamamen güvensizdir.

libcurl'e belirli bir transfer için Basic yöntemini kullanmasını açıkça şöyle söyleyebilirsiniz:

    curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);

## Digest

Başka bir HTTP kimlik doğrulama yöntemi Digest olarak adlandırılır. Bu yöntemin Basic'e kıyasla sahip olduğu bir avantaj, şifreyi kablo üzerinden düz metin olarak göndermemesidir. Ancak bu, tarayıcılar tarafından nadiren konuşulan ve dolayısıyla sık kullanılmayan bir kimlik doğrulama yöntemidir.

libcurl'e belirli bir transfer için Digest yöntemini kullanmasını açıkça şöyle söyleyebilirsiniz (yine de kullanıcı adı ve şifrenin ayarlanması gerekir):

    curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);

## NTLM

Başka bir HTTP kimlik doğrulama yöntemi NTLM olarak adlandırılır.

libcurl'e belirli bir transfer için NTLM yöntemini kullanmasını açıkça şöyle söyleyebilirsiniz (yine de kullanıcı adı ve şifrenin ayarlanması gerekir):

    curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_NTLM);

## Negotiate

Başka bir HTTP kimlik doğrulama yöntemi Negotiate olarak adlandırılır.

libcurl'e belirli bir transfer için Negotiate yöntemini kullanmasını açıkça şöyle söyleyebilirsiniz (yine de kullanıcı adı ve şifrenin ayarlanması gerekir):

    curl_easy_setopt(curl, CURLOPT_HTTPAUTH, CURLAUTH_NEGOTIATE);

## Bearer

Bir istekte OAuth 2.0 Bearer Erişim Belirteci iletmek için, örneğin `CURLOPT_XOAUTH2_BEARER` kullanın:

    CURL *curl = curl_easy_init();
    if(curl) {
      curl_easy_setopt(curl, CURLOPT_URL, "pop3://example.com/");
      curl_easy_setopt(curl, CURLOPT_XOAUTH2_BEARER, "1ab9cb22ba269a7");
      ret = curl_easy_perform(curl);
      curl_easy_cleanup(curl);
    }

## Önce dene (Try-first)

Bazı HTTP sunucuları birkaç kimlik doğrulama yönteminden birine izin verir, bazı durumlarda kendinizi bir istemci olarak önceden tek bir belirli yöntemi seçmek istemediğiniz veya seçemediğiniz bir durumda bulursunuz ve yine başka bir alt küme durumda, uygulamanız istenen URL'nin kimlik doğrulama gerektirip gerektirmediğini bile bilmez.

libcurl tüm bu durumları da kapsar.

libcurl'den birden fazla yöntem kullanmasını isteyebilirsiniz ve bunu yaptığınızda, curl'ün önce isteği hiç kimlik doğrulama olmadan denediğini ve ardından geri gelen HTTP yanıtına dayanarak, hem sunucunun hem de uygulamanızın izin verdiği yöntemlerden birini seçtiğini ima edersiniz. Birden fazla yöntem işe yararsa, curl bunları yöntemlerin ne kadar güvenli kabul edildiğine göre bir sırayla seçer ve mevcut yöntemlerin en güvenlisini seçer.

libcurl'e birden fazla yöntemi kabul etmesini söylemek için bunları şöyle bitsel VEYA (OR) ile birleştirin:

    curl_easy_setopt(curl, CURLOPT_HTTPAUTH,
                     CURLAUTH_BASIC | CURLAUTH_DIGEST);

libcurl'ün yalnızca tek bir belirli yönteme izin vermesini istiyorsanız ancak yine de kimlik doğrulama kullanmadan isteği yapıp yapamayacağını kontrol etmek için önce sondalamasını istiyorsanız, bit maskesine `CURLAUTH_ONLY` ekleyerek bu davranışı zorlayabilirsiniz.

Digest kullanmayı isteyin, ancak digest dışında hiçbir şey kullanmayın ve yalnızca gerçekten gerekli olduğu kanıtlanırsa:

    curl_easy_setopt(curl, CURLOPT_HTTPAUTH,
                     CURLAUTH_DIGEST | CURLAUTH_ONLY);
