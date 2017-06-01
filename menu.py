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

def iniciarSesion():
    pass