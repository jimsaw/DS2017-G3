class Usuario:
    nombre = ""
    contrasena = ""
    tipo = ""
    restaurante = ""


    def __init__(self, nombre, contrasena, tipo, restaurante):
        self.nombre = nombre
        self.contrasena = contrasena
        self.tipo = tipo
        self.restaurante = restaurante

    #Metodo para la impresion de los datos
    def __str__(self):
        if self.restaurante != "none":
            return "Nombre: " + self.nombre + "\nContraseña: " + self.contrasena + "\nTipo: " +  self.tipo + "\nRestaurante: " + self.restaurante
        return "Nombre: " + self.nombre + "\nContraseña: " + self.contrasena + "\nTipo: " + self.tipo


    #Retorna la contraseña del usuario
    def getContrasena(self):
        return self.contrasena

    #Retorna el nombre del usuario
    def getNombre(self):
        return self.nombre

    #Retorna el tipo de usuario que es
    def getTipo(self):
        return self.tipo

    #Retorna el restaurante al que pertenece, siendo un cliente retorna 'none'
    def getRestaurante(self):
        return self.restaurante

    ## Sets de atributos
    def setNombre(self, nombre):
        self.nombre = nombre

    def setContrasena(self, contrasena):
        self.contrasena = contrasena

    def setRestaurante(self, restaurante):
        self.restaurante = restaurante