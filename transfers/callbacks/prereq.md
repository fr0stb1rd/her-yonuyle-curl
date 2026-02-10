# Ön koşul (Prereq)

Burada "Prereq", istek gönderilmeden hemen öncesi anlamına gelir. Bu geri çağırımın çağrıldığı an budur.

İşlevi `CURLOPT_PREREQFUNCTION` ile ayarlayın; çağrılır ve kullanılan IP adresi ve port numaraları argümanlarda iletilir. Bu, uygulamanın transfer hakkında başlamadan hemen önce bilgi sahibi olmasını sağlar ve ayrıca isterse bu belirli transferi iptal etmesine de izin verir.
