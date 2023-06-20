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