# Test sunucuları (Test servers)

curl test paketinin büyük bir kısmı, test sırasında sadece test amaçlı olarak yerel makinede başlatılan ve test turunun sonunda tekrar kapatılan sunucularla etkileşime giren curl komut satırlarını çalıştırır.

Test sunucuları, bu amaçla yazılmış ve HTTP, FTP, IMAP, POP3, SMTP, TFTP, MQTT, SOCKS vekil sunucuları ve daha fazlasını konuşan özel sunuculardır.

Tüm test sunucuları test dosyası aracılığıyla kontrol edilir: her test senaryosunun çalışması için hangi sunuculara sahip olması gerektiği, ne döndürmeleri gerektiği ve her test için nasıl davranmaları gerektiği.

Test sunucuları eylemlerini tipik olarak `tests/log` içindeki özel dosyalara kaydeder ve testiniz istediğiniz gibi davranmıyorsa kontrol etmek yararlı olabilir.
