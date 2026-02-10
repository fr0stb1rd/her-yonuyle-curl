# İstek yöntemi (Request method)

Bir HTTP isteğinin ilk satırı *yöntemi* (method) içerir - bazen fiil (verb) olarak da adlandırılır. Bu komut satırının yapacağı gibi basit bir GET isteği yaparken:

    curl http://example.com/file

…ilk istek satırı şöyle görünür:

    GET /file HTTP/1.1

`-X` veya `--request` komut satırı seçeneklerini ve ardından gerçek yöntem adını kullanarak curl'e yöntemi başka bir şeye değiştirmesini söyleyebilirsiniz. Örneğin, `GET` yerine `DELETE`'i şöyle gönderebilirsiniz:

    curl http://example.com/file -X DELETE

Bu komut satırı seçeneği yalnızca giden istekteki metni değiştirir, herhangi bir davranışı değiştirmez. Bu özellikle önemlidir; örneğin, curl'den `-X` ile bir HEAD göndermesini isterseniz, çünkü HEAD bir GET yanıtının alacağı tüm başlıkları göndermek ancak *asla* bir yanıt gövdesi göndermemek üzere belirtilmiştir (başlıklar aksi takdirde bir tane geleceğini ima etse bile). Bu nedenle, aksi takdirde bir GET yapacak olan bir komut satırına `-X HEAD` eklemek, curl'ün asılı kalmasına ve gelmeyen bir yanıt gövdesini beklemesine neden olur.

curl'den HTTP transferleri gerçekleştirmesini isterken, seçeneğe göre doğru yöntemi seçer, bu nedenle nadiren `-X` ile açıkça istemek zorunda kalırsınız. Ayrıca, curl `-L` ile istendiği gibi yönlendirmeleri izlediğinde, `-X` ile ayarlanan istek yönteminin sonraki yönlendirmelerde bile gönderildiğini belirtmek gerekir.
