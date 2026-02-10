
import re

# Mapping of English terms to Turkish
# Based on SUMMARY.md and common translations
translations = {
    # General
    "Authentication": "Kimlik Doğrulama",
    "Backdoors": "Arka kapılar", # Guessing context
    "Bindings": "Bağlayıcılar",
    "Browser": "Tarayıcı",
    "Browsers": "Tarayıcılar",
    "Building": "Derleme",
    "Callbacks": "Geri çağırma işlevleri",
    "Certificates": "Sertifikalar",
    "Ciphers": "Şifreler",
    "Client": "İstemci",
    "Command line": "Komut satırı",
    "Compression": "Sıkıştırma",
    "Config file": "Yapılandırma dosyası",
    "Connections": "Bağlantılar",
    "Connection": "Bağlantı",
    "Connection pool": "Bağlantı havuzu",
    "Connection reuse": "Bağlantı yeniden kullanımı",
    "Connection cache": "Bağlantı önbelleği",
    "Content-Encoding": "İçerik Kodlama",
    "Cookies": "Çerezler",
    "Cookie engine": "Çerez motoru",
    "Credentials": "Kimlik bilgileri",
    "Debug": "Hata ayıklama",
    "Dependencies": "Bağımlılıklar",
    "Development": "Geliştirme",
    "Directory": "Dizin",
    "Download": "İndirme",
    "Downloads": "İndirmeler",
    "Email": "E-posta",
    "Environment variables": "Ortam değişkenleri",
    "Error codes": "Hata kodları",
    "Example": "Örnek",
    "Examples": "Örnekler",
    "Exit code": "Çıkış kodu",
    "Features": "Özellikler",
    "File format": "Dosya formatı",
    "FTP": "FTP", # Keep
    "FTPS": "FTPS", # Keep
    "Future": "Gelecek",
    "Global initialization": "Küresel başlatma",
    "Globbing": "Globbing", # or URL globbing -> URL globbing
    "Gopher": "Gopher",
    "Happy Eyeballs": "Mutlu Gözler", # SUMMARY uses "Mutlu Gözler (Happy Eyeballs)"
    "Headers": "Başlıklar",
    "Header callback": "Başlık geri çağırımı",
    "History": "Tarihçe",
    "Host": "Ana bilgisayar",
    "HTTP": "HTTP",
    "HTTP/2": "HTTP/2",
    "HTTP/3": "HTTP/3",
    "HTTPS": "HTTPS",
    "Identities": "Kimlikler",
    "IMAP": "IMAP",
    "Index": "Dizin",
    "Install": "Kurulum",
    "Internals": "İç yapı",
    "IPv4": "IPv4",
    "IPv6": "IPv6",
    "Keep-alive": "Canlı tutma",
    "Kerberos": "Kerberos",
    "Latency": "Gecikme",
    "LDAP": "LDAP",
    "Length": "Uzunluk",
    "License": "Lisans",
    "Logging": "Günlükleme",
    "Mailing lists": "E-posta listeleri",
    "Manual": "Kılavuz",
    "Memory": "Bellek",
    "Metalink": "Metalink",
    "Methods": "Yöntemler",
    "Multi-handle": "Multi-handle", # Keep?
    "Multiplexing": "Çoklama", # SUMMARY uses "Çoklama"
    "Name resolving": "İsim çözümleme",
    "Negotiate": "Negotiate",
    "Netrc": "Netrc",
    "Network": "Ağ",
    "NTLM": "NTLM",
    "Options": "Seçenekler",
    "Parallel": "Paralel",
    "Passwords": "Parolalar",
    "Performance": "Performans",
    "Persistence": "Kalıcılık",
    "Pipelining": "Boru hattı",
    "POP3": "POP3",
    "Port number": "Port numarası",
    "Post": "Post",
    "Progress meter": "İlerleme göstergesi",
    "Progress callback": "İlerleme geri çağırımı",
    "Protocols": "Protokoller",
    "Proxies": "Vekil sunucular",
    "Proxy": "Vekil sunucu",
    "Proxy header": "Vekil sunucu başlığı",
    "Public key": "Genel anahtar",
    "PUT": "PUT",
    "Quic": "Quic",
    "Ranges": "Aralıklar",
    "Read callback": "Okuma geri çağırımı",
    "Redirects": "Yönlendirmeler",
    "Releases": "Sürümler",
    "Requests": "İstekler",
    "Resolver": "Çözücü",
    "Responses": "Yanıtlar",
    "Resume": "Devam ettirme",
    "Retry": "Yeniden deneme",
    "RTMP": "RTMP",
    "RTSP": "RTSP",
    "SCP": "SCP",
    "Security": "Güvenlik",
    "Seek callback": "Arama geri çağırımı", # Seek -> Arama? Or Seek? "Seek ve ioctl" in SUMMARY.
    "SFTP": "SFTP",
    "Share": "Paylaşım",
    "SMTP": "SMTP",
    "SOCKS": "SOCKS",
    "SSH": "SSH",
    "SSL": "SSL",
    "Standards": "Standartlar",
    "TELNET": "TELNET",
    "TFTP": "TFTP",
    "Threads": "İş parçacıkları",
    "Timeouts": "Zaman aşımları",
    "TLS": "TLS",
    "Trace": "İzleme", # "Trace options" -> "İzleme seçenekleri"
    "Transfers": "Transferler",
    "Upload": "Yükleme",
    "Uploads": "Yüklemeler",
    "URL": "URL",
    "URL API": "URL API",
    "User-agent": "Kullanıcı aracısı",
    "Verbose": "Ayrıntılı",
    "Version": "Sürüm",
    "WebSockets": "WebSockets",
    "Windows": "Windows",
    "Write callback": "Yazma geri çağırımı",
    "Explicit": "Belirgin",
}

# Read existing index-words
with open("/home/vx/Desktop/g/tr/index-words", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Skip json markers and options
    if line.startswith("%") or line.startswith("-") or line.startswith("<") or line.startswith("."):
        new_lines.append(line)
        continue
    
    # Check if exact match exists in translations
    if line in translations:
        new_lines.append(translations[line])
    else:
        # Case insensitive check
        found = False
        for eng, tur in translations.items():
            if eng.lower() == line.lower():
                new_lines.append(tur)
                found = True
                break
        
        if not found:
            # If not found, keep original but log it (or just keep it)
            # Some proper names should be kept (e.g. Ubuntu, Debian, Wireshark)
            new_lines.append(line)

# Write back
with open("/home/vx/Desktop/g/tr/index-words", "w") as f:
    f.write("\n".join(new_lines) + "\n")

print("Updated index-words")
