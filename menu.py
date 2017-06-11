
import csv
import inout
import sesion as se

#Valida el pedido de alguna opcion de ingreso para menu
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

#Mostrar el menu correspondiente a un cliente
def menuCliente(usuario):
    print("""
    1.) Listar categorías de platos
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
        se.iniciarSesion()

#Menu de presentacion de busqueda de platillos imprimiendo el que el usuario ha pedido
def menuBusqueda():
    l = csv.devolverPlatillos()
    a = inout.buscarPlato()
    inout.imprimirBusqueda(a)
    print('¿Que plato desea ver?')
    opcion = pedirOpcion(1, len(a))
    print('')
    inout.mostrarPlatillos(l, a[opcion - 1].getNombre())

#Lista las categorias del platillo, mostrando tambien los platos disponibles e ingresand el usuario su pedid, le muestra su platillo
def menuCategoria(usuario):
    l = csv.devolverPlatillos()
    d = inout.busquedaCategoria(l)
    inde = inout.listarCategoria(d)
    print('')
    print('¿Que categoria desea revisar?')
    opcion1 = pedirOpcion(1, inde[0])
    print("")
    print('Lista de Platos disponibles:')
    listplato = inout.mostrarPlatos(inde[1][opcion1 - 1], l, usuario)
    print('')
    print('¿Que platillo quiere ver?')
    opcion2 = pedirOpcion(1, len(listplato))
    print('')
    inout.mostrarPlatillos(l, listplato[opcion2 - 1])

#Muestra el menu correspondiente al Asistente
def menuAsistente(usuario):
    print("""
    1.) Agregar platillo
    2.) Listar platillos
    3.) Listar categoria de platillos
    4.) Salir del sistema""")
    opcion = pedirOpcion(1, 4)
    print('')
    if opcion == 1:
        inout.agregarPlatillo(usuario)
        menuAsistente(usuario)
    elif opcion ==2:
        l = csv.devolverPlatillos()
        print('Lista de Platos disponibles en el restaurante:')
        inout.mostrarPlatos('', l, usuario)
    elif opcion == 4:
        print('Sesion Cerrada')
        print('')
        se.iniciarSesion()

#Muestra el menu correspondiente al Administrador
def menuAdmin(usuario):
    print("""
    1.) Agregar restaurante 
    2.) Listar restaurante
    3.) Agregar usuario
    4.) Salir del sistema.""")
    opcion = pedirOpcion(1,4)

#Menu principal
def menuPrincipal(usuario):
    print("Binvenido señor " + usuario.getNombre().title())
    print("¿Que desea hacer?")
    if usuario.getTipo() == "Administrador":
        menuAdmin(usuario)
    elif usuario.getTipo() == "Asistente":
        menuAsistente(usuario)
    elif usuario.getTipo() == "Cliente":
        menuCliente(usuario)












