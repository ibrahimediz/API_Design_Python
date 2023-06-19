
"""
from string import ascii_lowercase,ascii_uppercase,punctuation,digits
from random import choice
yukarıda yer alan değişken ve fonksiyonları kullanarak aşağıdaki kurallara uygun şifre üreten bir fonksiyon yazınız
1. en az 8 karakter uzunluğunda
2. en az bir küçük harf olmalı
3. en az bir büyük harf olmalı
4. en az bir rakam olmalı
5. en az bir noktalama işareti olmalı
"""

from string import ascii_lowercase,ascii_uppercase,punctuation,digits
from random import choice,sample

def passwordGenerate(uzunluk=8):
    sifre = ""
    while not (any(filter(str.isupper,sifre))
                   and any(filter(str.islower,sifre))
                   and any(filter(str.isdigit,sifre))
                   and any(filter(lambda x: x in punctuation ,sifre))) and len(sifre) <= uzunluk:
        # liste = [ascii_lowercase,ascii_uppercase,punctuation,digits]
        # sifre += choice(choice(liste))
        sifre = "".join(sample(ascii_lowercase+ascii_uppercase+punctuation+digits,uzunluk))
    else:
        return sifre

print(passwordGenerate(20))