from ipago import IPago
import random as rd

class TarjetaDeCredito(IPago):
    __numero = ""
    __cvc = ""
    __fechaExp = ""
    __saldo = ""

    def __init__(self, numero, cvc, fechaExp, montoInicial):
        self.__numero = numero
        self.__cvc = cvc
        self.__fechaExp = fechaExp
        self.__saldo = montoInicial

    def __str__(self):
        return "Número de tarjeta: " + str(self.__numero) + "\n" + "Número CVC: " + str(self.__cvc) + "\nFecha de expiración: " + str(
            self.__fechaExp)

    def pagar(self, monto):
        if self.validarCredenciales():
            if monto <= self.__saldo:
                self.__saldo -= monto
                print("El número de su orden es: ", rd.randint(1000, 9999))
            else:
                print("Saldo insuficiente.")
        else:
            print("Los datos ingresados no concuerdan con los de la tarjeta.")

    def validarCredenciales(self):
        numero = input("Ingrese su número de tarjeta: ")
        cvc = input("Ingrese el número CVC de su tarjeta: ")
        fechaExp = input("Ingrese la fecha de expiración de su tarjeta: ")
        return numero == self.__numero and cvc == self.__cvc and fechaExp == self.__fechaExp

    def deposito(self, monto):
        self.__saldo += monto
