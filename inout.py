import platillo as plat
import csv
import urllib.request
import menu as me
from PIL import Image

#Devuelve diccionario -> clave: Categoria // valor : numero platos
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

#Pide los datos correspondientes del platillo la usuario para luego guardarlo en nuestro CSV
def agregarPlatillo(usuario):
    print('Agregando Platillo..')
    nombre = str(input('Ingrese el nombre: '))
    categoria = str(input('Ingrese la categoria: '))
    descripcion = str(input('Ingrese la descripcion: '))
    servido = str(input('Ingrese como esta servido el platillo: '))
    tipo = str(input('Ingrese el tipo de platillo: '))
    ingredientes = str(input('Ingrese los ingredientes del platillo: '))
    imagen = obtenerImagen()[1]
    restaurante = usuario.getRestaurante()
    plato = plat.Platillo(nombre, restaurante, categoria, ingredientes, imagen, descripcion, servido, tipo)
    csv.escribirPlatillo(plato)
    print('')
    print('Platillo Agregado')
    print('Regresando al menu principal..')

# Imprime los platillos que tenga el parametro especificado en el nombre
def mostrarPlatillos(listaPlatillos, nombre):
    afirmativo = ["si", "SI", "Si", "sI", "s", "S", "Y", "yes", "y", "Yes"]
    for i in listaPlatillos:
        if i.getNombre() == nombre:
            print(i)
            pregunta = input("Desea ver una imagen del platillo? [si/no] ")
            if pregunta in afirmativo:
                mostrarImagen(i.getImagen())


# Imprime el menu resultante con todas las coincidencias de platillos de la busqueda
def imprimirBusqueda(listaBusqueda):
    if len(listaBusqueda) != 0:
        for j, plato in enumerate(listaBusqueda):
            print(j + 1,
                  '.)' + ' Nombre del plato: ' + plato.getNombre() + '          Restaurante: ' + plato.getRestaurante())
    else:
        print('No se encontro un resultado, por favor ingrese de nuevo')
        print('')
        buscarPlato()
    print('')

#Pide al usuario la opcion de busqueda y devuelve una lista con todas las coincidencias encontradas
def buscarPlato():
    name = str(input('Ingrese el nombre o descripcion del Plato: '))
    print('\nResultado de busqueda:')
    l = csv.devolverPlatillos()
    list = []
    for platillo in l:
        if name in platillo.getNombre() or name in platillo.getDescripcion():
                list.append(platillo)
    return list

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
            nuevoResta = usuario.getRestaurante().replace('\n','')
            if i.getRestaurante() == nuevoResta:
                print(str(e)+' .)'+" Nombre del Plato: " + i.getNombre() + "         Categoria: " + i.getCategoria())
                list.append(i.getNombre())
                e += 1
    return list

# Pide al usuario la ruta o url de una imagen, ser válido, guarda la imagen; retorna True y el nombre de la imagen si fue guardada con éxito.
def obtenerImagen():
    print("""
    1) Ingresar imagen local con ruta absoluta
    2) Ingresar url de una imagen de internet""")
    opcion = me.pedirOpcion(1, 2)
    if opcion == 1:
        zelda = input("Ingrese la ruta de la imagen: ")
        zelda = "file://" + zelda.strip(" ")
    else:
        zelda = input("Ingrese la url de la imagen: ").strip(" ")
    ban = validarImagen(zelda)
    while ban != 1:
        zelda = input("La ruta o url ingresada no pertenece a una imagen, ingrese la ruta o url de una imagen: ")
        ban = validarImagen(zelda)
    try:
        urllib.request.urlretrieve(zelda, zelda.split("/")[-1])
    except:
        print("Error. No se pudo guardar la imagen.")
        return False, "default.jpg"
    return True, zelda.split("/")[-1]


# Valida que el link ingresado sea de una imagen
def validarImagen(link):
    extensiones = [".jpg", ".png", ".bmp", ".gif", ".jpeg", ".tiff", ".bpg"]
    ban = 0
    for elem in extensiones:
        if link.endswith(elem):
            ban = 1
    return ban

# Muestra la imagen correspondiente a al nombre dado
def mostrarImagen(nombreImagen):
    imag = Image.open(nombreImagen)
    imag.show()