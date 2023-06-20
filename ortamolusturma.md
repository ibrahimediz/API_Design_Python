# Windows
## Ortamı oluşturmak için
* python -m venv ["ortamismi"]
* örnek : python -m venv env
## Ortamı aktif hale getirmek için
* env\Scripts\activate
## Ortamı pasif hale getirmek için
* env\Scripts\deactivate
## Kütüphane kurmak için
* pip install  ["kütüphane ismi"]
## Kütüphane Listesi Almak için
* pip list
* pip freeze 
### dosyaya yedeklemek için
* pip freeze > requirements.txt
### dosyadan yükleme yapmak için
* pip install -r requirements.txt

# Linux and Mac
## Ortamı oluşturmak için
* python3 -m venv ["ortamismi"]
* örnek : python3 -m venv env
## Ortamı aktif hale getirmek için
* source env/bin/activate
## Kütüphane kurmak için
* pip install  ["kütüphane ismi"]
## Kütüphane Listesi Almak için
* pip list
* pip freeze 
### dosyaya yedeklemek için
* pip freeze > requirements.txt
### dosyadan yükleme yapmak için
* pip install -r requirements.txt