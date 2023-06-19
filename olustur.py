liste = ["Gonenc","Berkay","Yelda","Can","Eda","Ege","Elifnaz","Kubra","Onur","Baris"]
import os
fileName = "01_02_List_Dict_Tuple"
metin = """
"""
for item in liste:
    fPath = f"/workspace/API_Design_Python/Exercises/{item}"
    if not os.path.exists(fPath):
        os.mkdir(fPath)
    open(os.sep.join((fPath,f"{fileName}.py")),"a+")
    
