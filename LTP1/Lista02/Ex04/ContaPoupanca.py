from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    
    def __init__(self, numeroConta, titular, saldo):
        super().__init__(numeroConta, titular, saldo)
    
    def depositar(self, valor):
        self.saldo += valor
        print("Transação bem-sucedida!")
    
    def sacar(self, valor):
        #Conferindo se o valor está no limite da conta
        if (self.saldo - valor >= 0):
            self.saldo -= valor
            print("Transação bem-sucedida!")
        else:
            print("Saldo insuficiente!")
    
    def calcSaldo(self, tempo=1):
        taxa = 0.006
        montante = self.saldo * ((1 + taxa) ** tempo)
        self.saldo = montante
        return montante