from abc import ABC, abstractmethod

class IPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        """Pago al restaurante"""
        return

    @abstractmethod
    def validarCredenciales(self):
        """Valida credenciales"""
        return