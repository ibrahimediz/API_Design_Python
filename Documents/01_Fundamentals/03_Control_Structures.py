################ if else elif
#### tek satırda if else
a = 3
sonuc = "Çift" if a % 2 == 0 else "Tek" 
print(sonuc)
sonuc = "Tek" if a % 2 else "Çift"
print(sonuc)

############## Loop Yapıları
########### for 
# print(*range(1,9)) # unpacking operator
# print(*[1,2,3,4,5],sep="-")
# for i in range(1,5):
#     print(i)
# liste = [1,2,3,4]
# for item in liste: # foreach
#     print(item)
############ while
# while True:
#     print(1)

# for i in range(1,5):
#     print(i)
# else:
#     print("Döngü Bitti")
######### break
# for i in range(1,5):
#     print(i)
#     if i == 3:
#         break
# else:
#     print("Döngü Bitti") # break ten dolayı çalışmaz

############ continue
# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("Döngü Bitti") # break ten dolayı çalışmaz
################################# Tek satırda for 
# liste = [ i for i in range(1,26) ]
# print(liste)
# liste = [ i for i in range(1,26) if i % 4 == 0]
# print(liste)
# liste = [ i**2 for i in range(1,26) if i % 4 == 0]
# print(liste)
#################
# sozluk1 = {i:i**2 for i in range(1,26) if i % 4 == 0}
# sozluk2 = {i:i*100 for i in range(1,26) if i % 4 != 0}
# sozluk1.update(sozluk2)
# print(sozluk1)