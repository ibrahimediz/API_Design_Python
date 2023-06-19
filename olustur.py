liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris","Cevaplar"]
import os
fileName = "02_07_builtins"
metin = """
"""
for item in liste:
    fPath = f"/workspace/API_Design_Python/Exercises/{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    dosya = open(os.sep.join((fPath,f"{fileName}.py")),"w+")
    dosya.write(metin)

