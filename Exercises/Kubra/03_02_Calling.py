

"""
/workspace/API_Design_Python/Documents/03_Moduls_And_Packages/Paket
1. Yukarıdaki adresi sys.path listesini kullanarak kütüphane adresleri listesine ekleyiniz
2. paket2 içerisinde bulunan 
Sinif2 sınıfını çağırıp aşağıdaki satırları kullanarak bir nesne oluşturunuz ve b özelliğini ekrana yazdırınız
obj = Sinif2()
obj.b
"""


import sys
sys.path.append("/workspace/API_Design_Python/Documents/03_Moduls_And_Packages/Paket")
print(*sys.path,sep="\n")


import Paket
from Paket.paket2 import Sinif2
obj = Sinif2()
print(obj.b)