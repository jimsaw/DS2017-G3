class Platillo:
    nombre = ""
    restaurante = ""
    categoria = ""
    ingredientes = ""
    imagenes = ""
    descripcion = ""
    servido = ''
    tipo = ''

    def __init__(self, nombre, restaurante, categoria, ingredientes, imagenes, descripcion,servido,tipo):
        self.nombre = nombre
        self.restaurante = restaurante
        self.categoria = categoria
        self.ingredientes = ingredientes
        self.imagenes = imagenes
        self.descripcion = descripcion
        self.servido = servido
        self.tipo = tipo

    def __str__(self):
        return 'Nombre del platillo: %s \nRestaurante: %s \nCategoria: %s \nIngredientes: %s \nDescripcion: %s \nServido: %s \nTipo: %s' % (self.nombre, self.restaurante, self.categoria, self.ingredientes, self.descripcion, self.servido, self.tipo)

    def getCategoria(self):
        return self.categoria

    def getNombre(self):
        return self.nombre

    def getRestaurante(self):
        return self.restaurante

    def getDescripcion(self):
        return self.descripcion

    def getIngredientes(self):
        return self.ingredientes

    def getServido(self):
        return self.servido

    def getTipo(self):
        return self.tipo

    def getImagen(self):
        return self.imagenes

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRestaurante(self, restaurante):
        self.restaurante = restaurante

    def setCategoria(self, categoria):
            self.categoria = categoria

    def setIngredientes(self, ingredientes):
        self.ingredientes = ingredientes

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setServido(self, servido):
        self.servido = servido

    def setTipo(self, tipo):
        self.tipo = tipo