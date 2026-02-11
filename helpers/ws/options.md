# Seçenekler (Options)

Uygulamanın bir WebSocket iletişimini kontrol etmesi için özel bir setopt seçeneği vardır: `CURLOPT_WS_OPTIONS`.

Bu seçenek libcurl'e bir bayrak bit maskesi ayarlar, ancak şu anda kullanılan sadece tek bir bit vardır.

## Ham mod (Raw mode)

Bit maskesinde `CURLWS_RAW_MODE` bitini ayarlayarak, libcurl tüm WebSocket trafiğini WebSocket trafiğini kendisi ayrıştırmak yerine ham olarak yazma geri çağırımına iletir. Bu ham mod, WebSocket işlemeyi zaten uygulamış olabilecek ve transfer için sadece libcurl kullanmaya geçip kendi WebSocket mantığını sürdürmek isteyen uygulamalar için tasarlanmıştır.

Ham modda, libcurl ayrıca herhangi bir PING trafiğini otomatik olarak işleme almaz.
