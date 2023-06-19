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
# tckimlik = "10000000146"
# liste = list(tckimlik)
# print(liste) # ['1', '0', '0', '0', '0', '0', '0', '0', '1', '4', '6']
# # a = "23"
# # print(int(a)+5)
# liste = list(map(int,liste))
# print(sum(liste))
#############################
