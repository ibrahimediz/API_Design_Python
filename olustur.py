liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris","Cevaplar"]
import os
fileName = "02_07_builtins"
metin = """
\"\"\"
1. map fonksiyonu ile verilen listedeki sayıların üç katını liste halinde ekrana yazdırınız => [25,76,45,38]
2. map fonksiyonu ile verilen metindeki karakterilerin ASCII kodunu liste halinde ekrana yazdırınız => "Dijital"
3. Verilen sözlükte yer alan anahtarlara göre sözlüğü tekrar sıralayınız => sozluk = {"5":"Ali","6":"Veli","3":"Fatma","2":"Ayşe"} 
\"\"\"
"""
for item in liste:
    fPath = f"/workspace/API_Design_Python/Exercises/{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    dosya = open(os.sep.join((fPath,f"{fileName}.py")),"a+")
    dosya.write(metin)

