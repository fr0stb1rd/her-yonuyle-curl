# Sıkıştırma

Gönderilmeden önce verilerin otomatik olarak sıkıştırılması, gereken bant genişliğinin azalması nedeniyle verilerin diğer uca daha hızlı ulaşmasına yardımcı olabilir.

curl, SFTP, SCP ve HTTP(S) için otomatik sıkıştırma ve açma sunar. HTTP(S) ile bunu yalnızca indirmeler için yapmak mümkünken, SFTP ve SCP her iki yön için de sunar.

## HTTP için

Ayrıntılar için [HTTP sıkıştırma](../../http/modify/compression.md) bölümüne bakın.

## SFTP/SCP için

Komut satırında `--compressed-ssh` seçeneğini sağlayın ve transfer, yapabiliyorsa otomatik ve şeffaf bir şekilde sıkıştırma kullanacaktır. Şöyle:

    curl -O --compressed-ssh sftp://example.com/bigfile
