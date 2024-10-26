from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    
    def __init__(self, numeroConta, titular, saldo, chequeEspecial):
        super().__init__(numeroConta, titular, saldo)
        self.chequeEspecial = chequeEspecial
    
    def depositar(self, valor):
        self.saldo += valor
        print("Transação bem-sucedida!")
    
    def sacar(self, valor):
        #Conferindo o Cheque Especial de R$1000
        if (self.saldo - valor >= self.chequeEspecial * -1):
            self.saldo -= valor
            print("Transação bem-sucedida!")
        else:
            print("Saldo insuficiente!")
    
    def calcSaldo(self):
        return self.saldo