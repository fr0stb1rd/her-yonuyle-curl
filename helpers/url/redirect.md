# URL'ye yönlendir (Redirect to URL)

Handle zaten ayrıştırılmış bir URL'ye sahip olduğunda, ikinci bir göreli URL ayarlamak onun buna uyum sağlamak için "yönlenmesini" sağlar.

Örnek, önce orijinal URL'yi ayarlayın sonra "yönlendiğimiz" URL'yi ayarlayın:

    CURLU *h = curl_url();
    rc = curl_url_set(h, CURLUPART_URL,
                      "https://example.com/foo/bar?name=moo", 0);

    rc = curl_url_set(h, CURLUPART_URL, "../test?another", 0);
