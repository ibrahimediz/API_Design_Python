

"""
Girilen TC Kimlik Numarasını Doğruluğunu Kontrol Eden Python Fonksiyonunu Yazınız
Kurallar:
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
Kurallar http://www.kodaman.org/yazi/t-c-kimlik-no-algoritmasi adresinden alınmıştır.
"""

from string import digits

def validateTCKN(tckn):
    if(len(tckn) != 11):
        print("First Rule Break")
        return False

    for char in tckn:
        if(digits.find(char) == -1):
            print("Second Rule Break")
            return False

    if(char[0] == 0):
        print("Third Rule Break")
        return False

    odd = 0
    even = 0
    for i in range(0,8):
        if((i+1)%2==1):
            odd=+int(tckn[i])
        else:
            even=+int(tckn[i])
            
    if(((odd*7)-even)%10 != tckn[9]):
        print("Forth Rule Break")
        return False

    total = 0
    for i in range(0,9):
        total=+tckn[i]

    if(total%10 != tckn[10]):
        print("Fifth Rule Break")
        return False
    
    return True

print(validateTCKN("10000000146"))
print(validateTCKN("12345678910"))