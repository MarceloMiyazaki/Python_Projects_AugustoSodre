
from abc import abstractmethod

class ContaBancaria():
    
    def __init__(self, numeroConta, titular, saldo):
        self.numeroConta = numeroConta
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    @abstractmethod
    def calcSaldo(self):
        pass
