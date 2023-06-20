# import os
# print(os.sep) # "/" windows için "\"
# print(os.name) # posix nt
# #### getcwd
# print(os.getcwd())
# ### curdir
# print(os.curdir)
# ### pardir
# print(os.pardir)
# ### listdir
# print(os.listdir("/workspace/API_Design_Python/Exercises"))
# ### mkdir
# # os.mkdir("BIZOLUSTURDUK")
# ### makedirs
# from datetime import datetime
# simdi = datetime.now()
# liste = [simdi.year,simdi.month,simdi.day,simdi.hour]
# print(os.sep.join(map(str,liste))) # 2023/6/20/11
# #### path exists
# if not os.path.exists(os.sep.join(map(str,liste))):
#     os.makedirs(os.sep.join(map(str,liste)))
# ### walk
# print(*os.walk("/workspace/API_Design_Python/ornek1"),sep="\n")
# for kokdizin,altdizin,dosyalar in os.walk("/workspace/API_Design_Python/ornek1"):
#     for dosya in dosyalar:
#         print(os.sep.join([kokdizin,dosya]))

# dosya  = os.stat("/workspace/API_Design_Python/ornek1/aaa.jpg")
# print(dosya)
# """
# os.stat_result(st_mode=33188, 
# st_ino=761277200, 
# st_dev=2053, 
# st_nlink=1, 
# st_uid=33333, 
# st_gid=33333, 
# st_size=0, 
# st_atime=1687261105, 
# st_mtime=1687261102, 
# st_ctime=1687261102)
# """
# print(os.environ.get("UYGULAMA"))


#################### sys
import sys
print(sys.path)
print(sys.argv) # ['Documents/03_Moduls_And_Packages/03_os_and_sys.py', 'ali=deneme', 'veli=deneme2', '--deneme']
print(sys.platform)
print(sys.prefix)
print(sys.version_info)


