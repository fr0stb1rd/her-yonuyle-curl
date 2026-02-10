# Easy handle'lar ve bağlantılar (Easy handles and connections)

Kaynak kodunu okurken bilmek ve akılda tutmakta fayda olan bazı temel bilgiler vardır:

 - 'data', üzerinde çalışılan transfer için easy handle'a (`struct Curl_easy`) atıfta bulunmak için her yerde kullandığımız değişken adıdır. Bunun için başka bir ad kullanılmamalı ve başka hiçbir şey bu adı kullanmamalıdır. Easy handle, bir transferi tanımlayan ana nesnedir. Bir transfer genellikle bir noktada bir bağlantı kullanır ve genellikle aynı anda yalnızca bir tane kullanır. Bu transfer tarafından şu anda kullanılan bağlantıyı tanımlayan bir `data->conn` işaretçisi vardır. Çoğullanmış (multiplexed) bağlantılar kullanıldığında, tek bir bağlantı zaman içinde ve hatta aynı anda birkaç transfer (ve dolayısıyla easy handle'lar) tarafından kullanılabilir.

 - `conn`, kodun üzerinde çalıştığı mevcut *bağlantıya* (`struct connectdata`) atıfta bulunmak için iç yapıların her yerinde kullandığımız değişken adıdır.

 - `result`, işlevlerden dönüş değerlerini tutmak için `CURLcode` değişkeni için kullandığımız olağan addır ve bu dönüş değeri sıfırdan farklıysa, bu bir hatadır ve işlev temizlenmeli ve dönmelidir (genellikle aynı hata kodunu üst işlevine ileterek).
