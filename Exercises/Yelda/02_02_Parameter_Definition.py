#### 
# 1. yöntem
def fonk(a,b):
    print(a+b)
# 2. yöntem
def fonk(*args):
    # args => tuple
    print(args)

fonk()
fonk(1,2,3,4)
fonk([1,2,3],[1,2,3,],[1,2,23])
# 3. yöntem
def fonk(**kwargs):
    # kwargs => dict
    print(kwargs)
    for key,value in kwargs.items():
        if key=="adi":
            print(value)

fonk()
fonk(adi="Dijital",soyadi="Vizyon")

###### 3 ü birlikte nasıl kullanılır
def fonk(a,b,*args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)


fonk(1,2,3,4,5,6,7,8,param1=1,param2=2)

# 1 2
# (3, 4, 5, 6, 7, 8)
# {'param1': 1, 'param2': 2}