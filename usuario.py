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

    def __str__(self):
        if self.restaurante != " none":
            return "Nombre: " + self.nombre + "\nContraseña: " + self.contrasena + "\nTipo: " +  self.tipo + "\nRestaurante: " + self.restaurante
        return "Nombre: " + self.nombre + "\nContraseña: " + self.contrasena + "\nTipo: " + self.tipo

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def setNombre(self, nombre):
        self.nombre = nombre