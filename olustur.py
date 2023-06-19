liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris","Cevaplar"]
import os
fileName = "01_03_Control_Structures"
metin = """
\"\"\"
1 sayısı ile 25 sayısı arasındaki 4 e bölünebilen 
sayıların karelerini liste olarak yazdıran python programını yazalım
\"\"\"
"""
for item in liste:
    fPath = f"/workspace/API_Design_Python/Exercises/{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    dosya = open(os.sep.join((fPath,f"{fileName}.py")),"a+")
    dosya.write(metin)
    
