def fonk(a,b):
    print(a+b)

print(type(fonk))  # <class 'function'>
print(type(fonk(2,3))) # <class 'NoneType'>

############################
# def fonk(a,b):
#     return a+b

# print(type(fonk(2,3))) # <class 'int'>
# print(type(fonk("2","3"))) # <class 'str'>

# sonuc = fonk(2,3)
# print(sonuc)
###################
# def fonk(a,b):
#     return a,b,a+b
# sonuc = fonk(2,3)
# print(f"{sonuc[0]}+{sonuc[1]}={sonuc[2]}") # 2+3=5
############### yield
# def fonk(a):
#     b = 1
#     while a != b:
#         yield b**2
#         b += 1
# print(fonk(5)) # <generator object fonk at 0x104e73510>
# for item in fonk(5):
#     print(item)

# print(*fonk(8))

################################## 
