import usuario as usu
import platillo as pla

def devolverUsuarios():
    l =  []
    file = open('usuarios.csv')
    for line in file:
        linea = line.split(';')
        usuario = usu.Usuario(linea[0],linea[1],linea[2],linea[3])
        l.append(usuario)
    file.close()
    return l

def devolverPlatillos():
    l = []
    file = open('platillos.csv')
    for line in file:
        linea = line.split(';')
        platillos = pla.Platillo(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5], linea[6], linea[7])
        l.append(platillos)
    file.close()
    return l
# file1 = open('usuarios.csv')
# print(file1.readlines())
# for line in file1:
#     linea = line.split(';')
#     usuario = linea[0]
#     contraseña = linea[1]
#     tipo = linea[2]
#     print("Usuario: " + usuario + "\nContraseña: " + contraseña + "\nTipo: " + tipo)
# etc, etc
# file1.close()

def escribirPlatillo(platillo):
    file = open('platillos.csv', 'a+',newline='')
    rest = platillo.getRestaurante().replace('\n','')
    plato = platillo.getNombre()+';' + rest +';'+platillo.getCategoria()+';'+platillo.getIngredientes()+';'+platillo.getImagen()+';'+platillo.getDescripcion() +';'+platillo.getServido() +';'+platillo.getTipo()+'\n'
    file.write(plato)
    file.close()