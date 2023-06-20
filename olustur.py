liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris","Cevaplar"]
import os
fileName = "03_02_Calling"
metin = """

\"\"\"
/workspace/API_Design_Python/Documents/03_Moduls_And_Packages/Paket
1. Yukarıdaki adresi sys.path listesini kullanarak kütüphane adresleri listesine ekleyiniz
2. paket2 içerisinde bulunan 
Sinif2 sınıfını çağırıp aşağıdaki satırları kullanarak bir nesne oluşturunuz ve b özelliğini ekrana yazdırınız
obj = Sinif2()
obj.b
\"\"\"
"""
for item in liste:
    fPath = f"/workspace/API_Design_Python/Exercises/{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    dosya = open(os.sep.join((fPath,f"{fileName}.py")),"w+")
    dosya.write(metin)



