liste = [1,2,3,4,5,6]
print(liste[1:4]) #2,3,4

print(liste[:])
print(liste[::-1])
print(liste[::1])
print(liste[::2])
print(liste[::3])

liste.insert(0,100)
print(liste[:])

liste.insert(3,100)
print(liste[:])


sozluk = {
    "Adi":"Dijital",
    "Soyadi":"Vizyon",
    "Telefon":1213123123123,
    "Adres":["Ankara","İstanbul"],
    "Adresler": {"Ev": "EvAdresi", "İş": "İşAdresi"},
    "Detay":{"1":"Bir"}
}

print(sozluk)

#######
liste2 = [1,2,3]
print(liste.extend(liste2))


