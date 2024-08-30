'''
Escreva um programa que jogue "pedra, papel ou tesoura" contra o usuário. 
O jogo deve continuar até o usuário escolher parar, e retornar o número de vitórias do usuário, da máquina, e empates.
'''

from random import randint


def show_menu():
    print("-----------------")
    print("Pedra, Papel ou Tesoura!")
    print("1. Jogar")
    print("2. Sair")
    print("-----------------")
    print()

def jogar():
    print()
    print("-----------------")
    print("Vamos lá! Pedra, Papel ou Tesoura?")
    print("1. Pedra")
    print("2. Papel")
    print("3. Tesoura")
    print("-----------------")

    'Loop para pegar resposta do usuário'
    while(True):
        answer = int(input("Resposta: "))
        if (answer == 1 or answer == 2 or answer == 3):
            break
    
    return answer


def checar_vencedor_partida(input_usuario):
    'Gerando a jogada aleatória da máquina'
    input_maquina = int(randint(1, 3))
    output_maquina = ""

    'Mostrando ao usuário qual foi a jogada'
    match input_maquina:
        case 1:
            output_maquina = "Pedra"
        case 2:
            output_maquina = "Papel"
        case 3:
            output_maquina = "Tesoura"

    print("Jogada da máquina:" , output_maquina)
    print()

    'Conferindo os resultados do combate'
    if (input_usuario == input_maquina):
        return "Empate"
    elif (input_usuario == 1 and input_maquina == 3) or (input_usuario == 2 and input_maquina == 1) or (input_usuario == 3 and input_maquina == 2):
        return "Vitoria"
    else:
        return "Derrota"
    
    

def show_resultados(resultados_totais):
    print()
    print("-----------------")
    print("Resultados:")
    print("Vitórias:", resultados_totais[0])
    print("Derrotas:", resultados_totais[1])
    print("Empates:",  resultados_totais[2])
    print("-----------------")

resposta = 0
resultados_totais = [0, 0, 0]
while (resposta != 2):
    show_menu()
    resposta = int(input("Resposta: "))
    if (resposta == 1):
        input_usuario = jogar()
        resultado = checar_vencedor_partida(input_usuario)
        
        match resultado:
            case "Vitoria":
                resultados_totais[0] += 1
                print("Vitória!")
                
            case "Derrota":
                resultados_totais[1] += 1
                print("Derrota!")
                
            case "Empate":
                resultados_totais[2] += 1
                print("Empate!")
                
    elif (resposta == 2):
        break
    else:
        print("Resposta não existe!")
        print()

show_resultados(resultados_totais)



        

