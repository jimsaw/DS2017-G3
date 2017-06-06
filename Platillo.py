class Platillo:
    nombre = ""
    restaurante = ""
    categoria = ""
    ingredientes = ""
    imagenes = ""
    descripcion = ""

    def __init__(self, nombre, restaurante, categoria, ingredientes, imagenes, descripcion):
        self.nombre = nombre
        self.restaurante = restaurante
        self.categoria = categoria
        self.ingredientes = ingredientes
        self.imagenes = imagenes
        self.descripcion = descripcion

    def __str__(self):
        return 'Nombre del platillo: %s \nRestaurante: %s \nCategoria: %s \nIngredientes: %s \nDescripcion: %s' % (self.nombre, self.restaurante, self.categoria, self.ingredientes, self.descripcion)

