# TLS kimlik doğrulaması

TLS bağlantıları, Güvenli Uzak Şifreler (Secure Remote Passwords - SRP) adı verilen (nadiren kullanılan) bir özellik sunar. Bunu kullanarak, bir ad ve şifre kullanarak sunucu için bağlantının kimliğini doğrularsınız ve bunun için komut satırı bayrakları `--tlsuser <ad>` ve `--tlspassword <sır>` şeklindedir. Şöyle:

    curl --tlsuser daniel --tlspassword secret https://example.com
