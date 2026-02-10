# Maksimum dosya boyutu

curl komut satırınızın çok büyük bir dosyayı indirmediğinden emin olmak istediğinizde, transfer başlamadan önce boyutu biliyorsa curl'e bunu yapmadan önce durması talimatını verin. Belki bu çok fazla bant genişliği kullanır, çok uzun sürer veya sabit diskinizde yeterli alanınız yoktur:

    curl --max-filesize 100000 https://example.com/

curl'e bayt sayısı cinsinden kabul edebileceğiniz en büyük indirmeyi verin ve curl transfer başlamadan önce boyutu anlayabilirse daha büyük bir şeyi indirmeyi denemeden önce iptal eder.

Transfer başladığı sırada curl'ün boyutu anlayamadığı birçok durum vardır. Bu tür transferler, ancak gerçekten o sınıra ulaştıklarında iptal edilir.
