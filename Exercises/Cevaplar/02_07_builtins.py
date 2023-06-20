"""
Girilen TC Kimlik Numarasını Doğruluğunu Kontrol Eden Python Fonksiyonunu Yazınız
Kurallar:
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, 
elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından 
elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
Kurallar http://www.kodaman.org/yazi/t-c-kimlik-no-algoritmasi adresinden alınmıştır.
"""
tcKimlikNo = "10000000146"
#             012345678910
# print(len(tcKimlikNo)==11)
# print(tcKimlikNo.isdigit())
# print(tcKimlikNo[0]!="0")
# 1 3 5 7 9 => 0 2 4 6 8
# print(*range(0,9,2)) # 0 2 4 6 8
# print(sum(map(int,tcKimlikNo[0:9:2])))
# liste = list(map(int,tcKimlikNo))
# print(liste)
# print(sum(liste[0:9:2]))
# # 2 4 6 8 => 1 3 5 7
# print(sum(liste[1:8:2]))
# print((sum(liste[0:9:2])*7-sum(liste[1:8:2]))%10 == liste[9])
# print(sum(liste[:10])%10==liste[10])
def tckimlikkontrol(tcKimlikNo):
    if len(tcKimlikNo)==11:
        if tcKimlikNo.isdigit():
            if tcKimlikNo[0]!="0":
                liste = list(map(int,tcKimlikNo))
                if (sum(liste[0:9:2])*7-sum(liste[1:8:2]))%10 == liste[9]:
                    if sum(liste[:10])%10==liste[10]:
                        return "T.C Kimlik Numarası Doğru"
                    else:
                        return "5. Kural Hatası"
                else:
                    return "4. Kural Hatası"
            else:
                return "3. Kural Hatası"
        else:
            return "2. Kural Hatası"
    else:
        return "1. Kural Hatası"


print(tckimlikkontrol("12345678910"))
"""
1. map fonksiyonu ile verilen listedeki sayıların üç katını liste halinde ekrana yazdırınız => [25,76,45,38]
2. map fonksiyonu ile verilen metindeki karakterilerin ASCII kodunu liste halinde ekrana yazdırınız => "Dijital"
3. Verilen sözlükte yer alan anahtarlara göre sözlüğü tekrar sıralayınız => sozluk = {"5":"Ali","6":"Veli","3":"Fatma","2":"Ayşe"} 
"""
