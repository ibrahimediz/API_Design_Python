
# DRY Dont Repeat Yourself
# def fonk():
#     print("Merhaba")
# a = 1
# b = 1
# for i in range(10):
#     c = a+b
#     print(c)
#     a = b
#     b = c
################# 
# a = b = 1
# for i in range(10):
#     print(a+b)
#     a,b = b,(a+b)

def fonk(n): # definition
    a = b = 1
    for i in range(n):
        print(a+b)
        a,b = b,(a+b)
fonk(5) # calling