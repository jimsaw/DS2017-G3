import csv
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

# def iniciarSesion():
#     pass


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