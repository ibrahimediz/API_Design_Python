
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

# def fonk(n): # definition
#     a = b = 1
#     for i in range(n):
#         print(a+b)
#         a,b = b,(a+b)
# fonk(5) # calling

##################
# def fonk(a,b,c=0):
#     print(a+b+c)


# fonk(2,3)
# fonk(2,3,2)

# def fonk(a,b):
#     print(a,b)

# fonk(b=1,a=2)
#######
# def fonk(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)
# fonk(12,25,c=12,d=25,e=21,f=23)

