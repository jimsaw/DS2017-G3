class Usuario:
    __nombre = ""
    __contrasena = ""
    __tipo = ""
    __restaurante = ""


    def __init__(self, nombre, contrasena, tipo, restaurante):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__tipo = tipo
        self.__restaurante = restaurante

    #Metodo para la impresion de los datos
    def __str__(self):
        if self.__restaurante != "none":
            return "Nombre: " + self.__nombre + "\nContraseña: " + self.__contrasena + "\nTipo: " +  self.__tipo + "\nRestaurante: " + \
                   self.__restaurante
        return "Nombre: " + self.__nombre + "\nContraseña: " + self.__contrasena + "\nTipo: " + self.__tipo


    #Retorna la contraseña del usuario
    def getContrasena(self):
        return self.__contrasena

    #Retorna el nombre del usuario
    def getNombre(self):
        return self.__nombre

    #Retorna el tipo de usuario que es
    def getTipo(self):
        return self.__tipo

    #Retorna el restaurante al que pertenece, siendo un cliente retorna 'none'
    def getRestaurante(self):
        return self.__restaurante

    ## Sets de atributos
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setContrasena(self, contrasena):
        self.__contrasena = contrasena

    def setRestaurante(self, restaurante):
        self.__restaurante = restaurante