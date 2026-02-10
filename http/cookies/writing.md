# Çerezleri dosyaya yazma

Çerezlerin saklandığı yer bazen çerez kavanozu (cookie jar) olarak adlandırılır. curl'de çerez motorunu etkinleştirdiğinizde ve çerezleri aldığında, curl'e çıkmadan önce bilinen tüm çerezlerini bir dosyaya, çerez kavanozuna yazmasını söyleyebilirsiniz. curl'ün verilen girişin işlenmesi ne kadar sürerse sürsün, çıktı çerez kavanozunu kullanım ömrü boyunca değil, yalnızca çıkışta güncellediğini unutmamak önemlidir.

Çerez kavanozu çıktısını `-c` ile belirtirsiniz:

    curl -c cookie-jar.txt http://example.com

`-c` çerezleri bir dosyaya *yazma* talimatıdır, `-b` çerezleri bir dosyadan *okuma* talimatıdır. Genellikle her ikisini de istersiniz.

curl çerezleri bu dosyaya yazdığında, oturum çerezleri (belirli bir yaşam süresi olmayanlar) dahil bilinen tüm çerezleri kaydeder. curl'ün kendisinin bir oturum kavramı yoktur ve bir oturumun ne zaman bittiğini bilmez, bu nedenle siz ona söylemedikçe oturum çerezlerini temizlemez.
