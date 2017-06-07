import csv
import usuario as usu

def pedirOpcion(a, b):
    while True:
        try:
            opcion = int(input("Ingrese por favor la opcion: "))
            if a <= opcion <= b:
                return opcion
            else:
                print("Valor fuera de rango.")
        except:
            print("Valor incorrecto, por favor ingrese uno valido.")

def menuCliente():
    print("""\n   1.) Listar categorías de platos
    2.) Buscar plato 
    3.) Cerrar sesión""")
    opcion = pedirOpcion(1,3)
    #if opcion == 1:


def menuAsistente():
    print("""\n   1.) Agregar platillo
    2.) Listar platillos
    3.) llosListar categoria de platillos
    4.) Salir del sistema""")
    opcion = pedirOpcion(1, 4)

def menuAdmin():
    print("""\n    1.) Agregar restaurante 
    2.) Listar restaurante
    3.) Agregar usuario
    4.) Salir del sistema.""")
    opcion = pedirOpcion(1,4)

def menuPrincipal(usuario):
    print("Binvenido señor " + usuario.getNombre())
    if usuario.getTipo() == "Administrador":
        menuAdmin()
    elif usuario.getTipo == "Asistente":
        menuAsistente()
    else:
        menuCliente()




#Devuelve diccionario -> clave: Categoria // valor : numero platos
def busquedaCategoria(listaPlatillos):
    diccionarioCategorias = {}
    for i in listaPlatillos:
        if i.getCategoria() in diccionarioCategorias:
            diccionarioCategorias[i.getCategoria()] += 1
        else:
            diccionarioCategorias[i.getCategoria()] = 1
    return diccionarioCategorias


#Recibiendo un diccionario, lista su categoria con sus platos
def listarCategoria(diccionarioCategorias):
    for i in diccionarioCategorias:
        print("Categoria: " + i + "  Numero de platos: ", diccionarioCategorias[i])


#Recibe una categoria y valida que tipo de usuario es, mostrando los datos pertenecientes a cada uno
def mostrarPlatos(categoria, listaPlatillos, usuario):
    if usuario.getTipo() == "cliente":
        for i in listaPlatillos:
            if i.getCategoria() == categoria:
                print("Nombre del Plato: " + i.getNombre() + "  Restaurante: " + i.getRestaurante())
    else:
        for i in listaPlatillos:
            if i.getRestaurante == usuario.getRestaurante:
                print("Nombre del Plato: " + i.getNombre() + "   Restaurante: " + i.getRestaurante())

def mostrarPlatillos(listaPlatillos, nombre):
    for i in listaPlatillos:
        if i.getNombre() == nombre:
            print(i)

def login(usuario, passw,lista):# la lista que ubicamos aqui es la que cargammos del archivo con la funcion devolver ususarioContrasena, es la lista inicial
    for i in range(len(lista)):
        if usuario in lista[i][0] and lista[i][0] == usuario:
            if passw in lista[i][1] and lista[i][1] == passw:
                return 1
            else:
                return 0
    return -1

def devolverUsuariosContrasena(): #devuelve una lista con las tuplas de usuario y contraseña
    l = []
    file = open('usuarios.csv')
    for line in file:
        linea = line.split(';')
        usuario = usu.Usuario(linea[0], linea[1], linea[2], linea[3])
        pas = usuario.getContrasena()
        l.append((usuario.getNombre(), pas))
    file.close()
    return l

def iniciarSesion():

    registeredUser = devolverUsuariosContrasena() #Lista con todos los usuarios y contraseñas, son los datos iniciales
    continuar = True
    while(continuar):
        usuario = str(input('User: '))
        passw = str(input('Password: '))

        if login(usuario, passw,registeredUser) == 1:
            print('Welcome ', usuario)
            continuar = False
        elif login(usuario, passw,registeredUser) == 0:
            print("\n\tPassword does not match...\n")
            print('Ingrese de nuevo.')
            print('')
        else:
            print('ERROR! User is not registered.')
            print('Ingrese de nuevo.')
            print('')