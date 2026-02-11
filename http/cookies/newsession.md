# Yeni çerez oturumu

Sunucu tarafından ayarlanan bir çerez, yalnızca *oturum* (session) sürdüğü sürece saklanması amaçlanan bir *oturum çerezi* olabilir. curl bir oturumun ne kadar sürdüğü veya ne zaman bittiği hakkında hiçbir fikre sahip değildir.

curl'e bir oturumun ne zaman bittiğini söylemek yerine, curl kullanıcının yeni bir oturumun ne zaman *başlayacağına* karar vermesini sağlayan bir seçeneğe sahiptir.

Yeni bir çerez oturumu, tüm eski oturum çerezlerinin atılması anlamına gelir. Bu, bir tarayıcıyı kapatıp yeniden başlatmanın eşdeğeridir.

curl'e yeni bir çerez oturumunun başladığını `-j, --junk-session-cookies` kullanarak söyleyin:

    curl -j -b cookies.txt http://example.com/
