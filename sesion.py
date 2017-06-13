import csv
import menu

# la lista que ubicamos aqui es la que cargammos del archivo con la funcion devolver ususarioContrasena, es la lista inicial
def login(usuario, passw,lista):
    for i in range(len(lista)):
        if usuario in lista[i][0] and lista[i][0] == usuario:
            if passw in lista[i][1] and lista[i][1] == passw:
                return 1
            else:
                return 0
    return -1

#devuelve una lista con las tuplas de usuario y contraseña
def devolverUsuariosContrasena():
    h = []
    l = csv.devolverUsuarios()
    for i in l:
        a = (i.getNombre(), i.getContrasena())
        h.append(a)
    return h

#Retorna el objeto de usuario
def convertirStringUsuario(nombre,listaobje):

    for i in listaobje:
        if nombre == i.getNombre():
            return i

#Inicia sesion
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
            menu.menuPrincipal(obje)
        elif login(usuario, passw,registeredUser) == 0:
            print("\n\tPassword does not match...\n")
            print('Ingrese de nuevo.')
            print('')
        else:
            print('ERROR! User is not registered.')
            print('Ingrese de nuevo.')
            print('')