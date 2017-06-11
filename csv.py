import usuario as usu
import platillo as pla


#Devuelve una lista de usuarios registrados en el sistema
def devolverUsuarios():
    l =  []
    file = open('usuarios.csv')
    for line in file:
        linea = line.split(';')
        usuario = usu.Usuario(linea[0],linea[1],linea[2],linea[3])
        l.append(usuario)
    file.close()
    return l

#Devuelve una lista de platillos ingresados dentro del sistema
def devolverPlatillos():
    l = []
    file = open('platillos.csv','r')
    for line in file:
        if line != '' and line != '\n':
            linea = line.split(';')
            platillos = pla.Platillo(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5], linea[6], linea[7])
            l.append(platillos)
    file.close()
    return l


#Guarda un nuevo platillo dentro del sistema
def escribirPlatillo(platillo):
    file = open('platillos.csv', 'a+',newline='')
    rest = platillo.getRestaurante().replace('\n','')
    plato = platillo.getNombre()+';' + rest +';'+platillo.getCategoria()+';'+platillo.getIngredientes()+';'+platillo.getImagen()+';'+platillo.getDescripcion() +';'+platillo.getServido() +';'+platillo.getTipo()+'\n'
    file.write(plato)
    file.close()