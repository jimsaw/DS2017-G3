class Platillo:
    __nombre = ""
    __restaurante = ""
    __categoria = ""
    __ingredientes = ""
    __imagenes = ""
    __descripcion = ""
    __servido = ''
    __tipo = ''

    def __init__(self, nombre, restaurante, categoria, ingredientes, imagenes, descripcion,servido,tipo):
        self.__nombre = nombre
        self.__restaurante = restaurante
        self.__categoria = categoria
        self.__ingredientes = ingredientes
        self.__imagenes = imagenes
        self.__descripcion = descripcion
        self.__servido = servido
        self.__tipo = tipo

    def __str__(self):
        return 'Nombre del platillo: %s \nRestaurante: %s \nCategoria: %s \nIngredientes: %s \nDescripcion: %s \nServido: %s \nTipo: %s' % (self.__nombre, self.__restaurante, self.__categoria, self.__ingredientes, self.__descripcion, self.__servido, self.__tipo)

    def getCategoria(self):
        return self.__categoria

    def getNombre(self):
        return self.__nombre

    def getRestaurante(self):
        return self.__restaurante

    def getDescripcion(self):
        return self.__descripcion

    def getIngredientes(self):
        return self.__ingredientes

    def getServido(self):
        return self.__servido

    def getTipo(self):
        return self.__tipo

    def getImagen(self):
        return self.__imagenes

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setRestaurante(self, restaurante):
        self.__restaurante = restaurante

    def setCategoria(self, categoria):
            self.__categoria = categoria

    def setIngredientes(self, ingredientes):
        self.__ingredientes = ingredientes

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setServido(self, servido):
        self.__servido = servido

    def setTipo(self, tipo):
        self.__tipo = tipo