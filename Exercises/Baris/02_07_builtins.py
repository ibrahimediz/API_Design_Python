

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

def tc_validation(tc):
    digits = [int(digit) for digit in tc]
    tek = sum(digits[0:9:2])
    cift = sum(digits[1:8:2])
"""
1. map fonksiyonu ile verilen listedeki sayıların üç katını liste halinde ekrana yazdırınız => [25,76,45,38]
2. map fonksiyonu ile verilen metindeki karakterilerin ASCII kodunu liste halinde ekrana yazdırınız => "Dijital"
3. Verilen sözlükte yer alan anahtarlara göre sözlüğü tekrar sıralayınız => sozluk = {"5":"Ali","6":"Veli","3":"Fatma","2":"Ayşe"} 
"""
a = [25,76,45,38]

b = lambda x: x*3

result = map(b,a)

for i in result:
    print(i)

####################################

c = "Dijital"


d = list(map(ord,c))

for i in b:
    print(i)



