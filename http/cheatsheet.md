# HTTP kopya kağıdı (cheat sheet)

[burada çevrimiçi](https://curl.github.io/curl-cheat-sheet/http-sheet.html)

| Ayrıntılı        | İlerlemeyi gizle        | ekstra bilgi      | Çıktıyı yaz      | Zaman aşımı    |
| ---------------- | ----------------------- | ----------------- | ---------------- | -------------- |
| -v               | -s                      | -w "format"       | -O               | -m             |
| --trace-ascii    |                         |                   | -o               |                |
| **POST**         | **multipart**           | **PUT**           | **HEAD**         | **özel (custom)** |
| -d "string"      | -F name=value           | -T                | -I               | -X "METHOD"    |
| -d @file         | -F name=@file           |                   |                  |                |
| **Temel kimlik doğrulama** | **çerezleri oku**     | **çerezleri yaz** | **çerezleri gönder** | **user-agent** |
| -u user:password | -b                      | -c                | -b "c=1; d=2"    | -A "string"    |
| **Vekil sunucu kullan** | **Başlıklar, ekle/kaldır** | **yönlendirmeleri takip et** | **gzip**         | **güvensiz**   |
| -x               | -H "name: value"        | -L                | --compressed     | -k             |
|                  | -H "name:"              |                   |                  |                |
