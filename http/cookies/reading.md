# Çerezleri dosyadan okuma

Boş bir çerez deposuyla başlamak istenmeyebilir. Neden önceki bir getirme işleminde sakladığınız veya başka bir şekilde edindiğiniz çerezlerle başlamayasınız? curl'ün çerezler için kullandığı dosya formatına Netscape çerez formatı denir çünkü bir zamanlar tarayıcılar tarafından kullanılan dosya formatıydı ve o zamanlar curl'e tarayıcının çerezlerini kullanmasını kolayca söyleyebilirdiniz.

Bir kolaylık olarak, curl ayrıca bir çerez dosyasının çerezleri ayarlayan bir HTTP başlıkları kümesi olmasını da destekler. Bu daha düşük bir formattır ancak sahip olduğunuz tek şey olabilir.

curl'e ilk çerezleri hangi dosyadan okuyacağını söyleyin:

    curl -L -b cookies.txt http://example.com

Bunun dosyadan yalnızca *okuduğunu* unutmayın. Sunucu yanıtında çerezleri güncellerse, curl bu çerezi bellek içi deposunda günceller ancak çıktığında hepsini atar ve aynı giriş dosyasının sonraki çağrısı orijinal çerez içeriğini tekrar kullanır.
