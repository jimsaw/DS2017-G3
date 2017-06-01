class Usuario:
    nombre = ""
    contrasena = ""
    tipo = ""

    def __init__(self, nombre, contrasena, tipo):
        self.nombre = nombre
        self.contrasena = contrasena
        self.tipo = tipo

    def __str__(self):
        return "Nombre: " + self.nombre + "\nContraseña: " + self.contrasena + "\nTipo: " +  self.tipo

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo