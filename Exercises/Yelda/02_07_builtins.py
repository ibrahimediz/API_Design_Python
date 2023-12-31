"""
filter
map
any,all
zip
sorted
reversed
enumerate
min,max,sum
"""
###### filter
# liste = [1,2,3,4,5,6,7]
# print(filter(lambda x:x%2==0,liste)) # <filter object at 0x7f7aca7c3820>
# print(*filter(lambda x:x%2==0,liste))
# print(list(filter(lambda x:x%2==0,liste)))
# print([item for item in liste if item % 2 == 0])
###### map
# liste = [1,2,3,4,5,6]
# def fonk(a):
#     return a**3
# print(map(fonk,liste)) # <map object at 0x7f4739f9b7f0>
# print(*map(fonk,liste))
# print(list(map(fonk,liste)))
################ örnek map kullanımı
tckimlik = "10000000146"
liste = list(tckimlik)
print(liste) # ['1', '0', '0', '0', '0', '0', '0', '0', '1', '4', '6']
print(map(int,liste))
print(*map(int,liste))
a = "23"
print(int(a)+5)
liste = list(map(int,liste))
print(sum(liste))
#############################
liste = ["Ali","Ayşe","Fatma","Veli","Kim"]
notlar = [50,60,100,75,200,100]
print(zip(liste,notlar)) # <zip object at 0x7fc6eb1d8240>
print(*zip(liste,notlar,strict=True)) # ('Ali', 50) ('Ayşe', 60) ('Fatma', 100) ('Veli', 75)
print(*zip(*zip(liste,notlar))) # ('Ali', 50) ('Ayşe', 60) ('Fatma', 100) ('Veli', 75)


"""
Girilen TC Kimlik Numarasını Doğruluğunu Kontrol Eden Python Fonksiyonunu Yazınız
Kurallar:
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
Kurallar http://www.kodaman.org/yazi/t-c-kimlik-no-algoritmasi adresinden alınmıştır.
"""
#######################################
liste1 = ["",0,[],{},set(),()]
liste2 = [1,1,1,1,1,1,1,1,0,1,1]
print(all(liste2))
print(any(liste1))
print(all(liste1))
print(any(liste2))
#########################################

liste = [1,2,6,4,3,2,3,4,5,6]
liste.sort()
print(liste)
metin = "Jamiryo"
sonuc = list(metin)
sonuc.sort()
print(sonuc) # ['J', 'a', 'i', 'm', 'o', 'r', 'y']
print("b" > "a")
print(ord("ş"))

"""
1. map fonksiyonu ile verilen listedeki sayıların üç katını liste halinde ekrana yazdırınız => [25,76,45,38]
2. map fonksiyonu ile verilen metindeki karakterilerin ASCII kodunu liste halinde ekrana yazdırınız => "Dijital"
3. Verilen sözlükte yer alan anahtarlara göre sözlüğü tekrar sıralayınız => sozluk = {"5":"Ali","6":"Veli","3":"Fatma","2":"Ayşe"} 
"""

list1 = [25,76,45,38]
print(*map((lambda x:x**3),map(int,list1)))

str1 = "Dijital"
print(list(map(ord, str1)))


sozluk = {"5":"Ali","6":"Veli","3":"Fatma","2":"Ayşe"}
print(dict(sorted(sozluk.items())))




liste = ["Ali","Ayşe","Çiğdem","Kamil","Şule","Sevgi","Zeynep","Işılsu","Ceren"]
alfabe = "ABCDEFGHIİJKLMNOPRESŞTUÜVYZ"
cevrim = {x:alfabe.index(x) for x in alfabe}
siralama=dict(enumerate(alfabe))
print(*siralama.items())
print(dict(sorted(liste, key=siralama.items())))

print(sorted(liste,key=lambda k:cevrim.get(k[0])))
