# Her şey multi'dir (Everything is multi)

libcurl, transfer yapmak için birkaç farklı API sunar; burada birincil farklar, senkron easy arayüzüne karşı bloklamayan multi arayüzüdür. Multi arayüzünün kendisi daha sonra olay güdümlü soket arayüzü veya normal perform arayüzü kullanılarak daha fazla kullanılabilir.

Ancak dahili olarak, her şey olay güdümlü arayüz için yazılmıştır. Her şeyin bloklamayan bir tarzda yazılması gerekir, böylece işlevler asla döngüde veya benzeri bir şekilde veri beklemez. O ifade edilen işlevselliğe sahip yüzey işlevleri olmadıkları sürece.

Tek bir transferi senkron olarak gerçekleştiren `curl_easy_perform()` işlevi, kendi içinde sadece multi arayüzünü dahili olarak kuran ve kullanan bir sarmalayıcı işlevdir.
