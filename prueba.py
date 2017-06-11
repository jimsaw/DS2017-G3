import urllib.request
zelda = "file:///home/kvasconezl/Pictures/3cbSRn.jpg"

a = True
try:
    result = urllib.request.urlretrieve(zelda, zelda.split("/")[-1])
except:
    print("Error. No se pudo guardar la imagen.")
    a = False
print(a)
print(result)
