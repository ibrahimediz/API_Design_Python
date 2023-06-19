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
liste = ["Ali","Ayşe","Fatma","Veli"]
# notlar = [50,60,100,75]
# print(zip(liste,notlar)) # <zip object at 0x7fc6eb1d8240>
# print(*zip(liste,notlar)) # ('Ali', 50) ('Ayşe', 60) ('Fatma', 100) ('Veli', 75)


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


def IDCriteria(Id):
    len(Id)
    Id[0] != "0"
    filter((str.isdigit, Id))

    

def checkID(TCId):
