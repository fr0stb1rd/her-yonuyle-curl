# Sertifika sabitleme (Certificate pinning)

TLS sertifikası sabitleme, sunucu sertifikasını imzalamak için kullanılan açık anahtarın değişmediğini doğrulamanın bir yoludur. *Sabitlenmiştir*.

Bir TLS veya SSL bağlantısı müzakere edilirken, sunucu kimliğini belirten bir sertifika gönderir. Bu sertifikadan bir açık anahtar çıkarılır ve bu seçeneğe sağlanan açık anahtarla tam olarak eşleşmezse, curl herhangi bir veri göndermeden veya almadan önce bağlantıyı iptal eder.

curl'e sha256 değerini okuması için bir dosya adı söylersiniz veya base64 kodlu karma (hash) değerini doğrudan komut satırında bir `sha256//` önekiyle belirtirsiniz. Noktalı virgül (;) ile ayrılmış olarak bu şekilde bir veya daha fazla karma belirtebilirsiniz.

    curl --pinnedpubkey "sha256//83d34tasd3rt…" https://example.com/

Bu özellik tüm TLS arka uçları tarafından desteklenmez.
