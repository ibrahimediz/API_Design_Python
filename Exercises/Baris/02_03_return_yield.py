
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
from random import choice
def generate_pw():
    min_length = 8
    
    length = int(input("Enter the length of the pw"))
    if length < min_length:
        print("min length should be 8")
    else:
        print("Length: " + str(length))
        
    lowercase = True
    uppercase = True
    digit=True
    punctuation=True
    
    pw =""
    
    if lowercase and uppercase and digit and punctuation:
        pw+=choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.punctuation)
    
    #4 chars left
    remaining = min_length - len(pw)

    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pw += ''.join(choice(all_chars) for i in range(remaining))
    return pw

pw1 = generate_pw()
print("pw is " + pw1)
