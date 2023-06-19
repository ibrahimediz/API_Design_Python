
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
from random import choice,randrange,shuffle

def generatePassword():
    password = []
    length = randrange(8,16)
    
    password.append(choice(ascii_lowercase))
    password.append(choice(ascii_uppercase))
    password.append(choice(punctuation))
    password.append(choice(digits))

    while len(password) < length:
        password.append(choice(ascii_lowercase + ascii_uppercase + punctuation + digits))

    shuffle(password)
    return ''.join(password)

print(generatePassword())
print(generatePassword())
print(generatePassword())
print(generatePassword())
print(generatePassword())

