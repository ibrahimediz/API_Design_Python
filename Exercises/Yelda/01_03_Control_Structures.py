"""
x=False

if x:
    print("a")
else:
    print("b")
"""



"""
1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım
"""
liste=[]
for i in range(26):
    if i%4==0:
        liste.append(i*i)
        print(i)
        
else:
    print(liste[:])

    sozluk = {i:i**2 for i in range(1,26) if i % 4 == 0 else}