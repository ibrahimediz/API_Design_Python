# ############ list
# liste = [1,2,3,4,5]
# print(liste[4]) # 5
# print(liste[-1]) # 5
# #        0 1 2 3 4
# #       -5-4-3-2-1
# #########
# print(liste[1:4]) # 1 2 3 indis numaraları ile => 2,3,4
# ################
# print(type(liste)) # <class 'list'>
# print(dir(liste))
# ###### ekleme 
# # append
# # insert
# # extend
# liste = [1,2,3]
# liste.append(4)
# print(liste) # [1,2,3,4]
# liste.insert(0,100) # indis numarası,değer
# print(liste) # [100,1,2,3,4]
# #### concat => concatenate
# liste1 = [1,2,3,4]
# liste2 = [5,6,7,8]
# print(liste1+liste2) # [1, 2, 3, 4, 5, 6, 7, 8]
# liste1.extend(liste2)
# print(liste1) # [1, 2, 3, 4, 5, 6, 7, 8]
# ############ 
# # liste = []
# # var1 = 1,2 # tuple
# #####################
# # a = 1
# # b = a
# # b = b + 1
# # print(a) # 1
# ####################
# a = [1,2,3]
# b = a
# b.append(1000)
# print(a) # [1, 2, 3, 1000]
# ###################
# a = [1,2,3]
# b = a.copy()
# b.append(1000)
# print(a) # [1, 2, 3]
# ###################
# a = [1,2,3]
# #    0 1 2
# print(a.pop(1)) # 2
# print(a) # [1,3]
# print(a.pop()) # 3
# print(a) # [1]
# #########
# a = [1,2,2,3,2,2,2,1,1,1,1,1]
# a.remove(1)
# print(a) # [2,2,3,2,2,2,1,1,1,1,1]
# ############
# a = [1,2,1,5,5,5,3,2,3,3,4,6,78,8]
# a.sort(reverse=True)
# #########
# liste = [1,2,3,4,5,6]
# print(liste[::2]) # 0 2 4 => [1, 3, 5]
# print(liste[::-1]) # [6, 5, 4, 3, 2, 1]
################################ Dictionary
sozluk = {"1":"Bir"}
#         key:value
#          item
# key için immutable veri tipleri,sayısal veri tipleri
sozluk = {"1":"Bir","2":"İki"}
####### erişim 
# get
# setdefault
print(sozluk["1"])
# print(sozluk["3"])
print(sozluk.get("3"))
print(sozluk.setdefault("1","One"))
print(sozluk)
print(sozluk.setdefault("3","Üç"))
print(sozluk)
##################### Güncelleme
# sozluk = {'1': 'Bir', '2': 'İki', '3': 'Üç',"1":"One"}
# print(sozluk["1"])
# sozluk["1"] = "Uno"
###########  Silme
# popitem
# pop
# sozluk = {'1': 'Bir', '2': 'İki', '3': 'Üç'}
# print(sozluk.pop("1"))
# print(sozluk.popitem())
################## Diğer Fonksiyonlar
sozluk = {
    "Adi":"Dijital",
    "Soyadi":"Vizyon",
    "Telefon":1213123123123,
    "Adres":["Ankara","İstanbul"],
    "Detay":{"1":"Bir"}
}
sozluk1 = {'1': 'Bir', '2': 'İki', '3': 'Üç'}
sozluk2 = {'1': 'One', '2': 'Two', '4':"Four"}
sozluk1.update(sozluk2)
print(sozluk1) # {'1': 'One', '2': 'Two', '3': 'Üç', '4': 'Four'}
####### keys,values,items
# sozluk1 = {'1': 'Bir', '2': 'İki', '3': 'Üç'}
# print(sozluk1.keys()) # dict_keys(['1', '2', '3'])
# print(sozluk1.values()) # dict_values(['Bir', 'İki', 'Üç'])
# print(sozluk1.items()) # dict_items([('1', 'Bir'), ('2', 'İki'), ('3', 'Üç')])
# for key,value in sozluk1.items():
#     print(key,value)
########## 
# liste = ["adi","soyadi","telefon"]
# sozluk = dict.fromkeys(liste,"")
# print(sozluk) # {'adi': '', 'soyadi': '', 'telefon': ''}
# liste1 = ["adi","soyadi","telefon"]
# liste2 = ["Dijital","Vizyon",123123123123]
# sozluk = {}
# sozluk.update(zip(liste1,liste2))
# print(sozluk) # {'adi': 'Dijital', 'soyadi': 'Vizyon', 'telefon': 123123123123}
#############################
# demet = 1,2,
# print(type(demet)) # <class 'tuple'>
# demet = (1)
# print(type(demet)) # <class 'int'>
# demet = (1,)
# print(type(demet)) # <class 'tuple'>