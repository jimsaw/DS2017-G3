class Restaurant:
    __nombre = ""
    __pago = ""
    __staff = {"asistentes":[], "administradores":[]}

    def __init__(self, nombre, pago):
        self.__nombre = nombre
        self.__pago = pago

    def __str__(self):
        return "Nombre: " + self.__nombre + "\n" + "Tipo de pago: " + str(self.__pago)


    def addAdmin(self, admin):
        if admin in self.__staff["administradores"]:
            print("Ya se ha agregado ese administrador.")
        else:
            self.__staff["administradores"].append(admin)

    def addAsistente(self, asistente):
        if asistente in self.__staff["asistentes"]:
            print("Ya se ha agregado ese asistente.")
        else:
            self.__staff["asistentes"].append(asistente)

    def getStaff(self):
        return self.__staff

    def getAdmins(self):
        return self.__staff["administradores"]

    def getAsistentes(self):
        return self.__staff["asistentes"]

