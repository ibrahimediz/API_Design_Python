"""

1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım

"""

liste = [i*i for i in range(1,26) if i %4 == 0]
print(liste) # [16, 64, 144, 256, 400, 576]