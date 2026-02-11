# Kabuk yönlendirmeleri (Shell redirects)

curl'ü bir kabuktan veya başka bir komut satırı istemi sisteminden çağırdığınızda, o ortam genellikle size bir dizi çıktı yönlendirme yeteneği sağlar. Çoğu Linux ve Unix kabuğunda ve Windows komut istemlerinde, `> dosyaadı` ile stdout'u (standart çıktı) bir dosyaya yönlendirirsiniz. Bunu kullanmak, elbette -o veya -O kullanımını gereksiz kılar.

    curl http://example.com/ > example.html

Çıktıyı bir dosyaya yönlendirmek, curl'den gelen tüm çıktıları o dosyaya yönlendirir, bu nedenle birden fazla URL'yi stdout'a aktarmayı isteseniz bile, çıktıyı yönlendirmek tüm URL'lerin çıktısının o tek dosyada saklanmasını sağlar.

    curl http://example.com/1 http://example.com/2 > files

Unix kabukları genellikle *stderr* akışını ayrı olarak yönlendirmenize izin verir. stderr akışı genellikle terminalde de gösterilen bir akıştır, ancak onu stdout akışından ayrı olarak yönlendirebilirsiniz. stdout akışı veriler içindir, stderr ise veri olmayan meta veriler, hatalar vb. içindir. stderr'i `2>file` ile şu şekilde yönlendirebilirsiniz:

    curl http://example.com > files.html 2>errors
