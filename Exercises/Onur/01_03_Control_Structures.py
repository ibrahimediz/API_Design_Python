
"""
1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım
"""
keys = []
values = []
tmp = {}
for x in range(1,25):
    if (x % 4 == 0):
        keys.append(x)
        values.append(x**2)

print(values)
tmp.update(zip(keys,values))
print(tmp)
