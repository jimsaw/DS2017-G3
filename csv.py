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
# <<<<<<< HEAD
#
# =======
# >>>>>>> master


#Guarda un nuevo platillo dentro del sistema
def escribirPlatillo(platillo):
    file = open('platillos.csv', 'a+', newline='')
    rest = platillo.getRestaurante().replace('\n','')
    plato = platillo.getNombre()+';' + rest +';'+platillo.getCategoria()+';'+platillo.getIngredientes()+';'+platillo.getImagen()+';'+platillo.getDescripcion() +';'+platillo.getServido() +';'+platillo.getTipo()+'\n'
    file.write(plato)
    file.close()


def modificarArchivoPlato(platillo, lista):
    lista1 = lista[:4]
    lista2 = lista[4:]
    lista3 = [0]
    listafinal = lista1 + lista3 + lista2
    file = open('platillos.csv', 'r')
    contadorfila = 1

    for line in file:
        new = line.split('\n')
        if len(new) == 2:
            util = new[0].split(';')
            if len(util) > 6:
                if util[4] == platillo.getImagen():
                    for i in range(len(listafinal)):
                        if listafinal[i] == 1:
                            if i == 0:
                                modificar_dato('platillos.csv', [contadorfila], i + 1, platillo.getNombre())
                            if i == 1:
                                modificar_dato('platillos.csv', [contadorfila], i + 1, platillo.getRestaurante())
                            if i == 2:
                                modificar_dato('platillos.csv', [contadorfila], i + 1, platillo.getCategoria())
                            if i == 3:
                                modificar_dato('platillos.csv', [contadorfila], i + 1, platillo.getIngredientes())
                            if i == 5:
                                modificar_dato('platillos.csv', [contadorfila], i + 1, platillo.getDescripcion())
                            if i == 6:
                                modificar_dato('platillos.csv', [contadorfila], i + 1, platillo.getServido())
                            if i == 7:
                                modificar_dato('platillos.csv', [contadorfila], i + 1, platillo.getTipo())
                else:
                    contadorfila += 1
        else:
            new2 = new[0].split(';')
            if len(new2) > 1:
                if new2[4] == platillo.getImagen():
                    for i in range(len(listafinal)):
                        if listafinal[i] == 1:
                            if i == 0:
                                modificar_dato('platillos.csv', [contadorfila], i, platillo.getNombre())
                            if i == 1:
                                modificar_dato('platillos.csv', [contadorfila], i, platillo.getRestaurante())
                            if i == 2:
                                modificar_dato('platillos.csv', [contadorfila], i, platillo.getCategoria())
                            if i == 3:
                                modificar_dato('platillos.csv', [contadorfila], i, platillo.getIngredientes())
                            if i == 5:
                                modificar_dato('platillos.csv', [contadorfila], i, platillo.getDescripcion())
                            if i == 6:
                                modificar_dato('platillos.csv', [contadorfila], i, platillo.getServido())
                            if i == 7:
                                modificar_dato('platillos.csv', [contadorfila], i, platillo.getTipo())
                else:
                    contadorfila += 1
    file.close()


def modificar_dato(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(';')
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ';'.join(columnas)
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)