from ipago import IPago
import random as rd

class CarneInteligente(IPago):
    __matricula = ""
    __usuario = ""
    __clave = ""
    __saldo = ""
    __movimientos = []

    def __init__(self, matricula, usuario, clave, saldo):
        self.__matricula = matricula
        self.__usuario = usuario
        self.__clave = clave
        self.__saldo = saldo

    def pagar(self, monto):
        if self.validarCredenciales():
            if monto <= self.__saldo:
                self.__saldo -= monto
                print("El número de su orden es: ", rd.randint(1000, 9999))
            else:
                print("Saldo insuficiente.")
        else:
            print("Usuario o contraseña incorrectos.")


    def validarCredenciales(self):
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        return usuario == self.__usuario and contrasena == self.__clave

    def consultaDeSaldo(self):
        return self.__saldo

    def deposito(self, monto):
        self.__saldo += monto

    def ingresoDeNotaDeDebito(self):
        print("Se ha ingresado nota de débito.")

    def ingresoDeNotaDeCredito(self):
        print("Se ha ingresado nota de crédito.")

    def consultaDeMovimientosFechas(self):
        return

    def consultaCompraFechas(self):
        return

    def reposicionPorPerdida(self):
        return
