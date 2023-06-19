
"""
1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım
"""
sozluk1 = {i:i**2 for i in range(1,26) if i % 4 == 0}
# sozluk2 = {i:i*100 for i in range(1,26) if i % 4 != 0}
# sozluk1.update(sozluk2)
# print(sozluk1)