class Movimiento:
    __fecha = ""
    __tipo = ""
    __monto = ""

    def __init__(self, fecha, tipo, monto):
        self.__fecha = fecha
        self.__tipo = tipo
        self.__monto = monto

    def __str__(self):
        return "Fecha: " + str(self.__fecha) + "\nTipo: " + str(self.__tipo) + "\nMonto: " + str(self.__monto)

