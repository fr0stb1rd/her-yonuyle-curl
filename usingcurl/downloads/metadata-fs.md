# Dosya sisteminde meta verileri saklama

curl ile bir indirmeyi dosyaya kaydederken, `--xattr` seçeneği curl'e belirli dosya meta verilerini "genişletilmiş dosya özniteliklerinde" (extended file attributes) saklamasını söyler. Bu genişletilmiş öznitelikler, desteklenen dosya sistemlerinden ve işletim sistemlerinden birinin kullanıldığı varsayılarak dosya sisteminde saklanan standartlaştırılmış ad/değer çiftleridir.

Şu anda URL `xdg.origin.url` özniteliğinde saklanır ve HTTP için içerik türü `mime_type` özniteliğinde saklanır. Bu seçenek ayarlandığında dosya sistemi genişletilmiş öznitelikleri desteklemiyorsa bir uyarı verilir.
