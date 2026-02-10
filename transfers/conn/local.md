# Yerel adres ve port numarası

Neredeyse tüm durumlarda, bir bağlantı kurarken sistemin varsayılan kaynak IP adresini ve yerel port numarasını seçmesine izin vermek istersiniz.

Bunun yeterince iyi olmadığı nadir durumlar için libcurl geçersiz kılma özellikleri sunar.

## Yerel adres

libcurl tarafından oluşturulan bir bağlantının, bu ana bilgisayara geri yönlenen bir kaynak IP'ye sahip olması gerekir. Bir uygulama, kullanmak istediği herhangi bir IP adresini rastgele seçip bunun çalışmasını bekleyemez. Makinedeki bir ağ arayüzünün atanmış IP adresine sahip olması gerekir.

`CURLOPT_INTERFACE` ile libcurl'den varsayılan olmayan bir IP adresi kullanmasını isteyebilirsiniz. Adından da anlaşılacağı gibi, girdi olarak adlandırılmış bir ağ arayüzü almak üzere tasarlanmıştır ve daha sonra giden trafik için o arayüzün IP adresini kullanmaya çalışacaktır.

Ancak ad, bir IP adresi veya bir ana bilgisayar adı da olabilir, ancak **bu sürümleri kullanmanızı önermiyoruz**.

libcurl'ün sağlanan girdinin ne tür olduğunu tahmin etmesini önlemek için, adın bir ana bilgisayar adıyla karıştırılmadığından emin olmak üzere arayüz adının önüne "if!" ekleyin.

Benzer şekilde, adresin bir ana bilgisayar adı veya IP numarası olduğunda ısrar etmek için sağlanan adın önüne "host!" eklersiniz.

## Yerel port numarası

Varsayılan olarak, bağlantılar için sözde *geçici port* (ephemeral port) aralığından 16 bitlik rastgele kaynak yerel port numaraları kullanılır. Bir uygulama, `CURLOPT_LOCALPORT` ve `CURLOPT_LOCALPORTRANGE` seçenekleriyle kullanılacak belirli bir port aralığı isteyebilir. Port numaraları sınırlı kaynaklar olduğundan, seçilecek portların seçimini daraltmak, denenen port numaralarından hiçbiri şu anda kullanılabilir değilse bağlantının kurulamama riskini artıracaktır.
