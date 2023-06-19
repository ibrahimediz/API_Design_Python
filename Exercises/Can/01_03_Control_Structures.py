
"""
1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım
"""
for i in range(1,25):
    if i%4 == 0:
        print (i*i)