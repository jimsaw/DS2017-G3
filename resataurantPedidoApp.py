from restaurant import Restaurant

class RestaurantPedidoApp(Restaurant):
    __almuerzo = ""
    __lunchBuilder = ""

    def __init__(self, nombre, pago):
        super().__init__(nombre, pago)
        self.__almuerzo = ""
