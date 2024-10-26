import os
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_contas():
    limpa_tela()
    print("--------------------")
    print("BANCO CEUB")
    print()
    print("Qual conta deseja acessar?")
    print("1. Conta Corrente")
    print("2. Conta Poupança")
    print("3. Sair")
    print("--------------------")

def menu_operacoes():
    print("--------------------")
    print("Digite qual operação deseja realizar:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Mostrar Informações")
    print("4. Sair")
    print("--------------------")

def operacao(tipo_conta, operacao):
    
    match operacao:
        case 1:
            if (tipo_conta == "corrente"):
                valor = float(input("Digite o valor a ser depositado: "))
                contaCorrente.depositar(valor)
            elif (tipo_conta == "poupanca"):
                valor = float(input("Digite o valor a ser depositado: "))
                contaPoupanca.depositar(valor)
        case 2:
            if (tipo_conta == "corrente"):
                valor = float(input("Digite o valor a sacar: "))
                contaCorrente.sacar(valor)
            elif (tipo_conta == "poupanca"):
                valor = float(input("Digite o valor a sacar: "))
                contaPoupanca.sacar(valor)
        case 3:
            limpa_tela()
            if (tipo_conta == "corrente"):
                print("Número da conta: " + str(contaCorrente.numeroConta))
                print("Titular: " + contaCorrente.titular)
                print(f"Saldo: R$ {contaCorrente.calcSaldo():,.2f}")
            
            elif(tipo_conta == "poupanca"):
                print("Número da conta: " + str(contaPoupanca.numeroConta))
                print("Titular: " + contaPoupanca.titular)
                print(f"Saldo: R$ {contaPoupanca.calcSaldo():,.2f}")

        case 4:
            return
        case _:
            print("Resposta inválida!")


#Main function

dados = []

print("--------------------")
print("BANCO CEUB")
print()
print("Vamos criar uma nova conta!")
dados.append(int(input("Digite o número da conta corrente: ")))
dados.append(int(input("Digite o número da conta poupança: ")))
dados.append(input("Digite o nome do titular: "))
print()
print("--------------------")   


contaCorrente = ContaCorrente(dados[0], dados[2], 0, 1000)
contaPoupanca = ContaPoupanca(dados[1], dados[2], 0)

resposta_contas = 0
#Loop até pedir pra sair
while resposta_contas != 3:
    menu_contas()
    resposta_contas = int(input("Resposta: "))
    limpa_tela()

    match resposta_contas:
        #Usando conta corrente
        case 1:
            resposta_operacoes = 0
            while resposta_operacoes != 4:
                menu_operacoes()
                resposta_operacoes = int(input("Resposta: "))
                limpa_tela()
                operacao("corrente", resposta_operacoes)

        
        #Usando conta poupança
        case 2:
            resposta_operacoes = 0
            while resposta_operacoes != 4:
                menu_operacoes()
                resposta_operacoes = int(input("Resposta: "))
                limpa_tela()
                operacao("poupanca", resposta_operacoes)
        
        case 3:
            break

        case _:
            print("Resposta inválida!")
