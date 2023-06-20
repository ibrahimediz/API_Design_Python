"""
filter
map
zip
any,all
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
# kup = lambda x:x**3
# print(map(lambda x:x**3,liste)) # <map object at 0x7f4739f9b7f0>
# print(*map(lambda x:x**3,liste))
# print(list(map(lambda x:x**3,liste)))
################ örnek map kullanımı
# tckimlik = "10000000146"
# liste = list(tckimlik)
# print(liste) # ['1', '0', '0', '0', '0', '0', '0', '0', '1', '4', '6']
# # a = "23"
# # print(int(a)+5)
# liste = list(map(int,liste))
# print(sum(liste))
#############################
############# zip
# liste = ["Ali","Ayşe","Fatma","Veli"]
# notlar = [50,60,100,75]
# print(zip(liste,notlar)) # <zip object at 0x7fc6eb1d8240>
# print(*zip(liste,notlar)) # ('Ali', 50) ('Ayşe', 60) ('Fatma', 100) ('Veli', 75)
# print(list(zip(liste,notlar))) # [('Ali', 50), ('Ayşe', 60), ('Fatma', 100), ('Veli', 75)]
# print(*zip(*zip(liste,notlar))) #  ('Ali', 'Ayşe', 'Fatma', 'Veli') (50, 60, 100, 75)
# # --------------------------
# print(dict(zip(liste,notlar)))
# # --------------------------
# sozluk = {}
# sozluk.update(zip(liste,notlar))
# print(sozluk) # {'Ali': 50, 'Ayşe': 60, 'Fatma': 100, 'Veli': 75}
############### enumerate
# liste = ["Ali","Ayşe","Fatma","Veli"]
# print(enumerate(liste)) # <enumerate object at 0x7fb9bcc5b0b0>
# print(*enumerate(liste))  # (0, 'Ali') (1, 'Ayşe') (2, 'Fatma') (3, 'Veli')
# print(list(enumerate(liste))) # [(0, 'Ali'), (1, 'Ayşe'), (2, 'Fatma'), (3, 'Veli')]
############### any,all
# liste1 = ["",1,[],{},set(),()]
# liste2 = [1,1,1,1,1,1,1,1,0,1,1]
# print(all(liste2))
# print(any(liste1))
############## sorted,reversed
# liste = [1,2,6,4,3,2,3,4,5,6]
# liste.sort()
# print(liste)
# metin = "Jamiryo"
# sonuc = list(metin)
# sonuc.sort()
# print(sonuc) # ['J', 'a', 'i', 'm', 'o', 'r', 'y']
# # print("Ali" > "ali")
# print(ord("ş"))
liste = ["Ali","Ayşe","Çiğdem","Kamil","Şule","Sevgi","Zeynep","Işılsu","Ceren"]
liste.sort()
print(liste)
################ sorted örnek
liste = ["Ali","Ayşe","Çiğdem","Kamil","Şule","Sevgi","Zeynep","Işılsu","Ceren"]
alfabe = "ABCDEFGHIİJKLMNOPRESŞTUÜVYZ"
cevrim = {x:alfabe.index(x) for x in alfabe}
print(sorted(liste,key=lambda k:cevrim.get(k[0])))