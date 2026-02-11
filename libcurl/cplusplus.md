# C++ programcıları için

libcurl bir C API'si sağlar. C ve C++ benzerdir ancak aynı değildir. libcurl'ü C++ içinde kullanırken akılda tutulması gereken birkaç şey vardır.

## Dizeler C++ dize nesneleri değil, C dizeleridir

`char *` kabul eden libcurl API'lerine dizeler ilettiğinizde, bu, o işlevlere C++ dizeleri veya nesneleri iletemeyeceğiniz anlamına gelir.

Örneğin, C++ ile bir dize oluşturursanız ve ardından o dizenin bir URL olarak kullanılmasını isterseniz:

    std::string url = "https://example.com/foo.asp?name=" + i;
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

## Geri çağırım (Callback) hususları

libcurl bir C kütüphanesi olduğundan, C++ üye işlevleri veya nesneleri hakkında hiçbir şey bilmez. Sınıfa bir işaretçi iletilen statik bir üye işlevi kullanarak bu sınırlamanın üstesinden nispeten kolaylıkla gelebilirsiniz.

İşte geri çağırım olarak bir C++ yöntemini kullanan bir yazma geri çağırımı örneği:

    // f, nesnenize olan işaretçidir.
    static size_t YourClass::func(void *buffer, size_t sz, size_t n, void *f)
    {
      // Statik olmayan üye işlevini çağırın.
      static_cast<YourClass*>(f)->nonStaticFunction();
    }

    // Statik işleve işaretçiyi şöyle iletirsiniz:
    curl_easy_setopt(hcurl, CURLOPT_WRITEFUNCTION, YourClass::func);
    curl_easy_setopt(hcurl, CURLOPT_WRITEDATA, this);
