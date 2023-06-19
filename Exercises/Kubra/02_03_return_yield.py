
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
import string
password = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

