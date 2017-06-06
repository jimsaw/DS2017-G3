file = open('usuarios.csv','a')
file.write("\nnuevo;nuevo;nuevo")
file.close()
file1 = open('usuarios.csv')
print(file1.readlines())
# for line in file1:
#     linea = line.split(';')
#     usuario = linea[0]
#     contraseña = linea[1]
#     tipo = linea[2]
#     print("Usuario: " + usuario + "\nContraseña: " + contraseña + "\nTipo: " + tipo)
# etc, etc
file1.close()