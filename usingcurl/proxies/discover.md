# Vekil sunucunuzu keşfedin

Bazı ağlar, İnternete veya belki ilgilendiğiniz o özel ağa ulaşmanız için bir vekil sunucu gerektirecek şekilde ayarlanmıştır. Vekil sunucuların kullanımı, ağınızı çalıştıran kişiler ve yönetim tarafından politika veya teknik nedenlerle ağınıza dahil edilir.

Ağ alanında vekil sunucuların otomatik tespiti ve onlara nasıl bağlanılacağı konusunda birkaç yöntem vardır, ancak bu yöntemlerin hiçbiri gerçekten evrensel değildir ve curl bunların hiçbirini desteklemez. Ayrıca, dış dünyayla bir vekil sunucu aracılığıyla iletişim kurduğunuzda, bu genellikle vekil sunucuya çok fazla güvenmeniz gerektiği anlamına gelir çünkü gönderdiğiniz veya onun üzerinden aldığınız tüm güvenli olmayan ağ trafiğini görebilir ve değiştirebilir. Bu güveni otomatik olarak varsaymak kolay değildir.

Tarayıcınızın ağ ayarlarını, bazen gelişmiş ayarlar sekmesi altında kontrol ederseniz, tarayıcınızın hangi vekil sunucuyu veya sunucuları kullanacak şekilde yapılandırıldığını öğrenebilirsiniz. curl kullandığınızda aynı olanı veya olanları kullanmanız gerekme ihtimali büyüktür.

Örnek olarak, [Firefox tarayıcısı için vekil sunucu ayarlarını](https://support.mozilla.org/en-US/kb/connection-settings-firefox) Tercihler => Genel => Ağ Ayarları altında aşağıda gösterildiği gibi bulabilirsiniz:

![Firefox için vekil sunucu ayarları](proxy-firefox-screenshot.png)
