## global ve nonlocal kavramları
# a = 4
# def fonk(b):
#     global a
#     a = 2
#     print("Fonksiyonun içinden:",a)
 
# print("1. Adım",a) # 4
# fonk(6) # 2
# print("2. Adım",a) # 2



# a = 4 # global
# def fonk(b):
#     a = 2
#     print("1. Fonksiyonun içinden :",a)
#     def icfonk(b):
#         global a 
#         a = 8
#         print("iç fonksiyonda:",a)
#     icfonk(b)
#     print("2. Fonksiyon içinden :",a)
 
# print("1. Adım",a) 
# fonk(6) 
# print("2. Adım",a) 


#######################

a = 4 # global

def fonkdis():
    a = 5
    print("1. dis fonksiyon",a)
    def fonk(b):
        nonlocal a
        a = 2
        print("1. Fonksiyonun içinden :",a)
        def icfonk(b):
            nonlocal a 
            a = 8
            print("iç fonksiyonda:",a)
        icfonk(b)
        print("2. Fonksiyon içinden :",a)
    fonk(6)
    print("2. dis fonksiyon",a)
 
print("1. Adım",a) 
fonkdis() 
print("2. Adım",a) 