

"""
/workspace/API_Design_Python/Documents/03_Moduls_And_Packages/Paket
1. Yukarıdaki adresi sys.path listesini kullanarak kütüphane adresleri listesine ekleyiniz
2. paket2 içerisinde bulunan 
Sinif2 sınıfını çağırıp aşağıdaki satırları kullanarak bir nesne oluşturunuz ve b özelliğini ekrana yazdırınız
obj = Sinif2()
obj.b
"""
import sys
print(*sys.path,sep="\n")
sys.path.append("/workspace/API_Design_Python/Documents/02_Functions")
from ornek import ornekFonk
ornekFonk()

# /workspace/API_Design_Python/Documents/03_Moduls_And_Packages
import Paket
print(Paket.Sinif1().a) # A
from Paket import Sinif1
from Paket import paket2
from Paket.paket2 import Sinif2
obj = Sinif2()
print(obj.b)