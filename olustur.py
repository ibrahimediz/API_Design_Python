liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris","Cevaplar"]
import os
fileName = "02_03_return_yield"
metin = """
\"\"\"
from string import ascii_lowercase,ascii_uppercase,punctuation,digits
from random import choice
yukarıda yer alan değişken ve fonksiyonları kullanarak aşağıdaki kurallara uygun şifre üreten bir fonksiyon yazınız
1. en az 8 karakter uzunluğunda
2. en az bir küçük harf olmalı
3. en az bir büyük harf olmalı
4. en az bir rakam olmalı
5. en az bir noktalama işareti olmalı
\"\"\"

"""
for item in liste:
    fPath = f"/Users/ibrahimediz/Documents/GitHub/API_Design_Python/Exercises/{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    dosya = open(os.sep.join((fPath,f"{fileName}.py")),"w+")
    dosya.write(metin)
    
