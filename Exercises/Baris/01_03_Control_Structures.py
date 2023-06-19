
"""
1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım
"""
b = []
for a in range(1,25):
    if a%4==0:
        b.append(a*a)
print(b)        