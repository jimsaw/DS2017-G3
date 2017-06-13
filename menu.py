import csv
import sesion as se
import inout
import usuario as usu

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
    3.) Cerrar sesión
    4.) Salir del sistema""")
    opcion = pedirOpcion(1,4)
    print('')
    if opcion == 1:
        menuCategoria(usuario)
        Retorno = str(input('Aplaste cualquier letra para regresar    '))
        print('Volviendo al menu principal..')
        menuCliente(usuario)
    elif opcion == 2:
        menuBusqueda()
        Retorno = str(input('Aplaste cualquier letra para regresar    '))
        print('Volviendo al menu principal..')
        menuCliente(usuario)
    elif opcion == 3:
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
    inout.mostrarPlatillos(l, a[opcion-1].getNombre())

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
    a = inout.mostrarPlatillos(l, listplato[opcion2-1])
    return a

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
    elif opcion == 2:
        l = csv.devolverPlatillos()
        print('Lista de Platos disponibles en el restaurante:')
        lista = inout.mostrarPlatos('', l, usuario)
        print('')
        print('¿Que platillo quiere ver?')
        opcion2 = pedirOpcion(1, len(lista))
        print('')
        plato = inout.mostrarPlatillos(l, lista[opcion2 - 1])
        modificarPlato(usuario, plato)
    elif opcion == 3:
        l = csv.devolverPlatillos()
        a = menuCategoria(usuario)
        modificarPlato(usuario, a)
        Retorno = str(input('Aplaste cualquier letra para regresar    '))
        print('Volviendo al menu principal..')
        menuAsistente(usuario)
        inout.mostrarPlatos('', l, usuario)
    elif opcion == 4:
        print('Sesion Cerrada')
        print('')
        se.iniciarSesion()



def modificarPlato(usuario,plato):
    opcion = str(input('¿Desea modificar el plato? Y/N   '))
    opcion = opcion.upper()
    print(opcion)
    if opcion == 'Y':
        print('')
        print('Modificando plato..')
        cambio = crearPlatoNuevo(plato)
        csv.modificarArchivoPlato(cambio[1], cambio[0])
        print('Plato modificado')
        print('')
        menuAsistente(usuario)
    elif opcion == 'N':
        print('Regresando al menu principal..')
        print('')
        menuAsistente(usuario)
    else:
        print('Respuesta incorrecta, ingrese de nuevo su respuesta')
        modificarPlato(usuario, plato)


def crearPlatoNuevo(plato):
    Nombre = str(input('Ingrese el nuevo nombre del plato: '))
    Restaurante = str(input('Ingrese el nuevo restaurante del plato: '))
    Categoria = str(input('Ingrese la nueva categoria del plato: '))
    Ingredientes = str(input('Ingrese los nuevos ingredientes del plato: '))
    Descripcion = str(input('Ingrese la nueva descripcion del plato: '))
    Servido = str(input('Ingrese la nueva forma de servir el plato: '))
    Tipo = str(input('Ingrese el nuevo tipo del plato: '))
    cambioNombre, cambioRestaurante, cambioCategoria, cambioIngredientes, cambioDescripcion, cambioServido, cambioTipo = 0, 0, 0, 0, 0, 0, 0
    if Nombre != '':
        plato.setNombre(Nombre)
        cambioNombre = 1
    if Restaurante != '':
        plato.setRestaurante(Restaurante)
        cambioRestaurante = 1
    if Categoria != '':
        plato.setCategoria(Categoria)
        cambioCategoria = 1
    if Ingredientes != '':
        plato.setIngredientes(Ingredientes)
        cambioIngredientes = 1
    if Descripcion != '':
        plato.setDescripcion(Descripcion)
        cambioDescripcion = 1
    if Servido != '':
        plato.setServido(Servido)
        cambioServido = 1
    if Tipo != '':
        plato.setTipo(Tipo)
        cambioTipo = 1
    lista = [cambioNombre, cambioRestaurante, cambioCategoria, cambioIngredientes, cambioDescripcion, cambioServido, cambioTipo]
    return lista, plato



#Muestra el menu correspondiente al Administrador
def menuAdmin(usuario):
    print("""
    1.) Agregar restaurante 
    2.) Listar restaurante
    3.) Agregar usuario
    4.) Salir del sistema.""")
    opcion = pedirOpcion(1,4)
    if opcion == 1:
        menuAdmin(usuario)
    elif opcion == 2:
        menuAdmin(usuario)
    elif opcion == 3:
        tipos = ["Administrador", "Asistente", "Cliente"]
        nombre = input("Ingrese nombre: ")
        contra = input("Ingrese contraseña: ")
        tipo = input("Ingrese tipo [administrador, asistente, cliente]: ").capitalize()
        while tipo not in tipos:
            tipo = input("Error. Tipo inválido, ingrese de nuevo el tipo de usuario: ")
        restaurante = input("Ingrese restaurante: ")
        usuario = usu.Usuario(nombre, contra, tipo, restaurante)
        csv.guardarUsuario(usuario)
        menuAdmin(usuario)

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
