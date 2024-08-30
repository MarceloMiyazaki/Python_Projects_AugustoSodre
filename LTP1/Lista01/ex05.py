
'''
Escreva um programa que jogue "pedra, papel ou tesoura" contra o usuário. 
O jogo deve continuar até o usuário escolher parar, e retornar o número de vitórias do usuário, da máquina, e empates.
'''

def show_menu():
    print("-----------------")
    print("Pedra, Papel ou Tesoura!")
    print("1. Jogar")
    print("2. Sair")
    print("-----------------")

    resposta = input("Resposta: ")
    return resposta

def jogar():
    print("-----------------")
    print("Vamos lá! Pedra, Papel ou Tesoura?")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    print("-----------------")

    resposta = input("Resposta: ")
    return resposta


