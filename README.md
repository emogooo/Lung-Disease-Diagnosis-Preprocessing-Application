# Akciger-Tespit-Programi

Röntgen filminden akciğer kısmını kırpan, yapay zeka destekli zatürre teşhis projesinin veriseti hazırlama (preprocessing) uygulaması.

Pseudo Code:

![image](https://user-images.githubusercontent.com/58745898/190654275-56dc738d-96d7-4875-9073-84e577c7e297.png)

![image](https://user-images.githubusercontent.com/58745898/190654330-da304e38-95ca-4d18-9456-510f9a4cd33a.png)

![image](https://user-images.githubusercontent.com/58745898/190654374-1dfa31a8-9063-4f2d-ae7e-483d3ed2fb01.png)

![image](https://user-images.githubusercontent.com/58745898/190654407-ba1280dd-caec-49ef-a2f7-81fad145d0ab.png)

![image](https://user-images.githubusercontent.com/58745898/190654979-32ca0e15-4f11-421a-a593-a52a69dd19d3.png)



Çalışma adımları kısa ve özetle şu şekildedir:

Algoritmaya verilen röntgen filmi:![00004274_000](https://user-images.githubusercontent.com/58745898/190640588-9fbb80d3-eb1d-404d-9f92-66cf7db25183.png)

1. İlk olarak yüksek bir eşik değeri ile film siyah beyaz hale getirilerek, yazı ve semboller tespit edilir.

![a](https://user-images.githubusercontent.com/58745898/190641086-9acfc9f4-6987-41a7-92c3-b996c5fadb74.jpg)

2. Tespit edilen yazı ve sembollerin filmdeki koordinatları siyaha boyanır.

![BBBlogoveYazilarSiyahaBoyanir](https://user-images.githubusercontent.com/58745898/190644036-cac08058-fcf7-47c3-a5f4-c1ea242c4803.jpg)

3. Film siyah beyaza çekilir

![CCCSiyahBeyazYapilir](https://user-images.githubusercontent.com/58745898/190644129-2c250ecb-255a-4211-b353-06e47661ec0a.jpg)

4. Filme blur uygulanır.

![DDDBlurUygulanir](https://user-images.githubusercontent.com/58745898/190644183-148bcad7-ac4e-4992-98ab-84c2fd2d794d.jpg)

5. Blurlanmış film siyah beyaz hale getirilir.

![EEEBlurlanmisFilmSiyahBeyazaCekilir](https://user-images.githubusercontent.com/58745898/190644402-7a1140f3-8e3a-4dcd-af73-a5c9356915f6.jpg)

6. Filmin en sol, en sağ, en üst ve en altında bulunan beyaz pixeller tespit edilerek, vücudun çerçevesi belirlenir.

![GGGASDASDSADASDADSiyahBeyazaCekilmisResminEnYakinBeyazPikselleriBulunur](https://user-images.githubusercontent.com/58745898/190644517-d84e29b3-bca2-451f-b7d0-607dafb245b5.jpg)

7. Önceki adımda oluşturulan çerçeve orijinal resme giydirilir.

![FFFSiyahBeyazaCekilmisResminEnYakinBeyazPikselleriBulunur](https://user-images.githubusercontent.com/58745898/190644647-93b557d6-f10b-4594-934d-96bd12835ad2.jpg)

8. Çerçeve orijinal resimden kırpılır ve vücut resmi akciğer bulma fonksiyonuna göndermek için hazırlanmış olur.

![HBody](https://user-images.githubusercontent.com/58745898/190645001-51eebf3c-822e-43a0-b3b6-bf192556750a.jpg)

Akciğer bulma fonksiyonu 3 aşamalı çalışmaktadır. Bunlardan ilki akciğerin tamamını şablonlar ile eşleştirerek bulmaya çalışmasıdır. Eğer tam akciğer görüntüsü ile eşleşme sağlanamaz ise ikinci aşamaya geçiş yapılır. Bu aşamada sol ve sağ akciğerler aranmaktadır. Sol akciğer bulunursa sağ akciğer aranır o da bulunursa iki görüntü en uzak koordinatlarından çerçevelenip sonuca ulaşılır. Fakat sol veya sağ akciğerden herhangi biri veya ikisi birden bulunamaz ise 3. aşamaya geçilir. Bu aşama 2. aşamadaki gibi sırasıyla akciğerin sol üst, sol alt, sağ üst, ve sağ alt kısımlarını aramaktadır. 4 köşenin de bulunması halinde en uzak koordinatlardan çerçeve oluşturularak akciğer görüntüsüne ulaşılmış olur.

9. Birinci aşama - Tam akciğer eşleşmesi

![JJJFullLung](https://user-images.githubusercontent.com/58745898/190649793-9c37dd5e-13e7-44c5-b347-97f1bcbbbc0d.jpg)

10. İkinci aşama - Sol akciğerin eşleşmesi

![KKKLeftLung](https://user-images.githubusercontent.com/58745898/190649907-a12a8cc6-47d3-4452-8cd3-26591fbf4586.jpg)

11. İkinci aşama - Sağ akciğerin eşleşmesi

![MMMBothLung](https://user-images.githubusercontent.com/58745898/190650019-cfc8e916-d27f-46d0-9f7e-1d25dd2b166a.jpg)

12. İkinci aşama - İki görüntünün en uzak noktalarından çerçeve oluşturulup ve bu çerçeveden kırpılarak akciğer tespitinin tamamlanması

![NNNBothFullLung](https://user-images.githubusercontent.com/58745898/190650202-61e6c1ad-a864-409e-8ea8-84eb059cdfb1.jpg)

13. Üçüncü aşama - Tüm köşelerin eşleşmesi (Tüm köşeler için ayrı görsel eklemek yerine sadece son köşenin eşleşme görseli eklenmiştir.)

![OOOCorners](https://user-images.githubusercontent.com/58745898/190650525-442aa1d9-0d83-4dc5-90a0-dde1a4e5b0b7.jpg)

14. Dört görüntünün en uzak noktalarından çerçeve oluşturulup akciğer tespitinin tamamlanması

![PPPCornersFull](https://user-images.githubusercontent.com/58745898/190650851-dfbf32bd-f908-4155-adc4-6df28b37b2fa.jpg)

15. Final görüntüsü

![RRRFinal](https://user-images.githubusercontent.com/58745898/190650917-dad02800-032f-412d-abeb-a2c87e09747d.png)

# 16.09.2022 itibariyle algoritma değiştirilmiştir. Eski algoritmanın çalışma prensibi ve pseudo code'u aşağıda bulunmaktadır.
Çalışma adımları kısa ve özetle şu şekildedir:

Algoritmaya verilen röntgen filmi:

![d](https://user-images.githubusercontent.com/58745898/158307662-107506fb-edaa-4460-bc8d-b9fd581bce2e.jpg)

1. İlk olarak yüksek bir eşik değeri ile film siyah beyaz hale getirilerek, yazı ve semboller tespit edilir.

![a](https://user-images.githubusercontent.com/58745898/158308128-d75a6b0e-536c-48ed-8690-fb02222c4288.jpg)

2.T espit edilen yazı ve sembollerin filmdeki koordinatları siyaha boyanır.

![a](https://user-images.githubusercontent.com/58745898/158308404-fbe4cac4-c006-4db4-af32-628e9971674e.jpg)

3. Filme blur uygulanır.

![a](https://user-images.githubusercontent.com/58745898/158308657-f52d49fd-6e06-45f0-a16f-e539cd3440af.jpg)

4. Blurlanmış film siyah beyaz hale getirilir.

![a](https://user-images.githubusercontent.com/58745898/158308790-7b0e7d41-12b5-478f-aeca-6fb68fba7d00.jpg)

5. Filmin en sol, en sağ, en üst ve en altında bulunan beyaz pixeller tespit edilerek, vücudun çerçevesi belirlenir. 4. maddede işlenmiş olan görüntü bu çerçevelerden kırpılarak akciğer bulma fonksiyonuna gönderilir.

![Adsız](https://user-images.githubusercontent.com/58745898/158309814-01622bc7-a118-4b30-83a1-a8c72a78d91b.png)

6. Filmin dışta bulunan tüm siyah pixelleri beyaza boyanır.

![a](https://user-images.githubusercontent.com/58745898/158310148-6b933059-2b21-450f-8af2-fcaba122d0da.jpg)

7. Elde edilen görüntü blurlanır.

![a](https://user-images.githubusercontent.com/58745898/158310363-6233b803-7aee-4451-95af-0bf714084bb9.jpg)

8. Blurlanmış görüntü siyah beyaza çevirilerek göğüs kafesi ortaya çıkarılır.

![a](https://user-images.githubusercontent.com/58745898/158310655-a8acfd73-15fc-4f3d-a1f7-13bf40d1c119.jpg)

9. Görüntünün en sol, en sağ, en üst ve en altında bulunan siyah pixeller tespit edilerek, göğüs kafesinin çerçevesi belirlenir.

![a](https://user-images.githubusercontent.com/58745898/158311151-279416cb-d603-4041-bdcb-192be0719e2f.jpg)

10. Orijinal görüntü bu çerçevelerden kesilerek istenilen görüntüye ulaşılır.

![a](https://user-images.githubusercontent.com/58745898/158311599-b0303496-4b32-46e7-ac5a-103e81cd8721.jpg)

11. Elde edilen görüntü:

![d-9079045](https://user-images.githubusercontent.com/58745898/158310672-3c56a853-088f-4295-a238-c712b75ca318.jpg)

Pseudo Code:

Başla.

Resmi yüksek bir eşik değeri (240/255) ile siyah-beyaza çevir. (a)

Beyaz pixellerin koordinatlarını tut.

Orijinal resimde bu koordinatlara denk gelen pixelleri siyaha boya. (b)

Resme blur ((x/30), (y/15)) uygula ve normal bir eşik değeri (127/255) ile siyah-beyaza çevir. (c)

Dört yöndeki en uzak (yukarı aşağı sağ sol) beyaz pixelleri bul ve bu noktalardan çerçevele.

Çerçevelenmiş resmi kırp ve yeni resmi oluştur. (d)

Resmin dışta bulunan siyah pixellerini beyaza boya. (e)

Resme yüksek oranda blur ((x/5), (y/5)) uygula ve normal bir eşik değeri (127/255) ile siyah-beyaza çevir. (f)

Yeni resimde mevcut dört yöndeki en uzak (yukarı aşağı sağ sol) siyah pixelleri bul ve bu noktalardan çerçevele. 

Çerçevenin koordinatlarını orijinal resimden kırparak akciğeri görüntüsünü elde et. (g)

Bitir.


Parametreler:

X = Resmin yatay uzunluğu (pixel adedi)

Y = Resmin dikey uzunluğu (pixel adedi)


Açıklamalar:

Röntgen filmlerinde biyomedikal görüntülerin yanı sıra röntgen numarası, hasta, hastane ve doktor adı gibi bilgiler de bulunmaktadır. Bu bilgilerin röntgen filminden çıkarılması ve akciğerin tespiti yapılırken hata payını artırmaması için ilk siyah-beyaz çevirme işleminde kullanılan threshold değeri normalden büyüktür. 

Uygulanan ilk blurlama işlemi röntgen filminde bulunan, parazit sayılabilecek aykırı pixellerin giderilmesi içindir.

Uygulanan ikinci blurlama işlemi akciğerin köşelerinin koordinatlarını saptamak için yüksek tutulmuştur. Bu sayede akciğer harici bir varlığın (genelde çocuklarda görülen karın bölgesinde gaz sıkışması akciğerden daha koyu ve yoğun gözükmektedir) görüntülenmesi engellenmiş olur.

![img](https://user-images.githubusercontent.com/58745898/183700555-40b4a4c8-7634-4e61-b859-77cf65a5073a.jpg)
