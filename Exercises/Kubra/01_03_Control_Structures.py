
"""
1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım
"""

liste = []
for i in range(1,26):
     if i % 4 == 0:
        result = i*i
        liste.append(result)
        print(liste)
         