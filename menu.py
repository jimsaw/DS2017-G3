
import csv
import platillo as plat

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


def menuCliente(usuario):
    print("""\n    1.) Listar categorías de platos
    2.) Buscar plato 
    3.) Cerrar sesión""")
    opcion = pedirOpcion(1,3)
    print('')
    if opcion == 1:
        menuCategoria(usuario)
        print('Volviendo al menu principal..')
        menuCliente(usuario)
    elif opcion == 2:
        menuBusqueda()
        print('Volviendo al menu principal..')
        menuCliente(usuario)
    else:
        print('Sesion Cerrada')
        print('')
        iniciarSesion()


def menuBusqueda():
    l = csv.devolverPlatillos()
    a = buscarPlato()
    imprimirBusqueda(a)
    print('¿Que plato desea ver?')
    opcion = pedirOpcion(1, len(a))
    print('')
    mostrarPlatillos(l, a[opcion-1].getNombre())


def buscarPlato():
    name = str(input('Ingrese el nombre o descripcion del Plato: '))
    print('')
    print('Resultado de busqueda:')
    l = csv.devolverPlatillos()
    list = []
    for platillo in l:
        if name in platillo.getNombre() or name in platillo.getDescripcion():
                list.append(platillo)
    return list


def imprimirBusqueda(listaBusqueda):
    if len(listaBusqueda) != 0:
        for j,plato in enumerate(listaBusqueda):
            print(j+1,'.)'+ ' Nombre del plato: '+ plato.getNombre() + '          Restaurante: ' + plato.getRestaurante())
    else:
        print('No se encontro un resultado, por favor ingrese de nuevo')
        print('')
        buscarPlato()
    print('')


def menuCategoria(usuario):
    l = csv.devolverPlatillos()
    d = busquedaCategoria(l)
    inde = listarCategoria(d)
    print('')
    print('¿Que categoria desea revisar?')
    opcion1 = pedirOpcion(1, inde[0])
    print("")
    print('Lista de Platos disponibles:')
    listplato = mostrarPlatos(inde[1][opcion1 - 1], l, usuario)
    print('')
    print('¿Que platillo quiere ver?')
    opcion2 = pedirOpcion(1, len(listplato))
    print('')
    mostrarPlatillos(l, listplato[opcion2-1])


def menuAsistente(usuario):
    print("""\n    1.) Agregar platillo
    2.) Listar platillos
    3.) Listar categoria de platillos
    4.) Salir del sistema""")
    opcion = pedirOpcion(1, 4)
    print('')
    if opcion == 1:
        agregarPlatillo(usuario)
        menuAsistente(usuario)
    elif opcion ==2:
        l = csv.devolverPlatillos()
        mostrarPlatos('', l, usuario)

def menuAdmin(usuario):
    print("""\n    1.) Agregar restaurante 
    2.) Listar restaurante
    3.) Agregar usuario
    4.) Salir del sistema.""")
    opcion = pedirOpcion(1,4)


def menuPrincipal(usuario):
    print("Binvenido señor " + usuario.getNombre())
    print("¿Que desea hacer?")
    if usuario.getTipo() == "Administrador":
        menuAdmin(usuario)
    elif usuario.getTipo() == "Asistente":
        menuAsistente(usuario)
    elif usuario.getTipo() == "Cliente":
        menuCliente(usuario)


def agregarPlatillo(usuario):
    print('Agregando Platillo..')
    nombre = str(input('Ingrese el nombre: '))
    categoria = str(input('Ingrese la categoria: '))
    descripcion = str(input('Ingrese la descripcion: '))
    servido = str(input('Ingrese como esta servido el platillo: '))
    tipo = str(input('Ingrese el tipo de platillo: '))
    restaurante = usuario.getRestaurante()
    plato = plat.Platillo(nombre, restaurante, categoria, "no data", "no data", descripcion, servido, tipo)
    csv.escribirPlatillo(plato)
    print('')
    print('Platillo Agregado')
    print('Regresando al menu principal..')


# Devuelve diccionario -> clave: Categoria // valor : numero platos
def busquedaCategoria(listaPlatillos):
    diccionarioCategorias = {}
    for i in listaPlatillos:
        if i.getCategoria() in diccionarioCategorias:
            diccionarioCategorias[i.getCategoria()] += 1
        else:
            diccionarioCategorias[i.getCategoria()] = 1
    return diccionarioCategorias


# Recibiendo un diccionario, lista su categoria con sus platos
def listarCategoria(diccionarioCategorias):
    print("Estas son las opciones de categorias de platillos disponibles: ")
    lista = []
    for m, i in enumerate(diccionarioCategorias):
        print(m+1,'.)  ',i , '{:>30}'.format("Numero de platos: "+str(diccionarioCategorias[i])))
        lista.append(i)
    return m+1, lista


# Recibe una categoria y valida que tipo de usuario es, mostrando los datos pertenecientes a cada uno
def mostrarPlatos(categoria, listaPlatillos, usuario):
    if usuario.getTipo() == "Cliente":
        list = []
        k = 1
        for i in listaPlatillos:
            if i.getCategoria() == categoria:
                print(str(k)+' .)'+" Nombre del Plato: " + i.getNombre() + "         Restaurante: " + i.getRestaurante())
                list.append(i.getNombre())
                k += 1
    else:
        list = []
        e = 1
        for i in listaPlatillos:
            if i.getRestaurante == usuario.getRestaurante:
                print(str(e)+' .)'+" Nombre del Plato: " + i.getNombre() + "         Restaurante: " + i.getRestaurante())
                list.append(i.getNombre())
                e += 1
    return list


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
    h = []
    l = csv.devolverUsuarios()
    for i in l:
        a = (i.getNombre(), i.getContrasena())
        h.append(a)
    return h


def iniciarSesion():

    registeredUser = devolverUsuariosContrasena() #Lista con todos los usuarios y contraseñas, son los datos iniciales
    continuar = True
    print('Iniciando sesion..')
    while(continuar):
        usuario = str(input('User: '))
        passw = str(input('Password: '))

        if login(usuario, passw,registeredUser) == 1:
            continuar = False
            lista = csv.devolverUsuarios()
            obje = convertirStringUsuario(usuario,lista)
            menuPrincipal(obje)
        elif login(usuario, passw,registeredUser) == 0:
            print("\n\tPassword does not match...\n")
            print('Ingrese de nuevo.')
            print('')
        else:
            print('ERROR! User is not registered.')
            print('Ingrese de nuevo.')
            print('')


def convertirStringUsuario(nombre,listaobje):

    for i in listaobje:
        if nombre == i.getNombre():
            return i

