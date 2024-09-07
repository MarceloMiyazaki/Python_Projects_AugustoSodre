
def cria_matriz():
    print()
    lin = int(input("Digite o número de linhas da sua matriz: "))
    col = int(input("Digite o número de colunas da sua matriz: "))
    mat = []

    for i in range(lin):
        linha = []
        for j in range(col):
            num = int(input(f"Insira o número da posição [{i}, {j}]: "))
            linha.append(num)
        mat.append(linha)
    
    return mat

def mult_escalar(matriz):
    matriz_copia = [row[:] for row in matriz]
    lin = len(matriz_copia)
    col = len(matriz_copia[0])
    
    print()
    escalar = int(input("Digite o valor do escalar: "))

    for i in range(lin):
        for j in range(col):
            matriz_copia[i][j] *= escalar
    
    return matriz_copia

def print_matriz(matriz):
    lin = len(matriz)
    col = len(matriz[0])

    print()
    print("Matriz:")
    for i in range(lin):
        print("[", end="")
        for j in range(col):
            print(f"{matriz[i][j]:5.2f}", end=" ")
        print("]")


def opera_matriz(matriz_1, matriz_2):
    lin1 = len(matriz_1)
    col1 = len(matriz_1[0])
    lin2 = len(matriz_2)
    col2 = len(matriz_2[0])
    
    opcao = -1
    while (True):
        print()
        opcao = int(input("\nO que deseja fazer? \n1. Soma de matrizes \n2. Subtração de matrizes \n3. Multiplicação de matrizes \n\nResposta: "))
        if opcao == 1 or opcao == 2 or opcao == 3:
            break
    
    if opcao == 1:

        if lin1 != lin2 and col1 != col2:
            print("As matrizes devem ser de mesma ordem!")
            return

        mat_resultado = []
        for i in range(lin1):
            linha = []

            for j in range(col1):
                num = matriz_1[i][j] + matriz_2[i][j]
                linha.append(num)

            mat_resultado.append(linha)
        
        return mat_resultado
    
    elif opcao == 2:
        
        if lin1 != lin2 and col1 != col2:
            print("As matrizes devem ser de mesma ordem!")
            return

        mat_resultado = []
        for i in range(lin1):
            linha = []

            for j in range(col1):
                num = matriz_1[i][j] - matriz_2[i][j]
                linha.append(num)

            mat_resultado.append(linha)
        
        return mat_resultado

    elif opcao == 3:
        return multiplica_matriz(matriz_1, matriz_2)

def multiplica_matriz(matriz_1, matriz_2):
    lin1 = len(matriz_1)
    col1 = len(matriz_1[0])
    lin2 = len(matriz_2)
    col2 = len(matriz_2[0])

    if col1 != lin2:
        print("O número de colunas da Matriz 1 deve ser igual ao número de linhas da Matriz 2!")
        return
    
    mat_resultado = []
    for i in range(lin1):
        linha = []
        for j in range(col2):
            num = 0
            for k in range(col1):
                num += matriz_1[i][k] * matriz_2[k][j]
            linha.append(num)
        mat_resultado.append(linha)
    
    return mat_resultado


    


matriz_principal  = cria_matriz()
print_matriz(matriz_principal)

matriz_secundaria = cria_matriz()
print_matriz(matriz_secundaria)

#print_matriz(mult_escalar(matriz_secundaria))

try:
    print_matriz(opera_matriz(matriz_principal, matriz_secundaria))
except:
    print("Deu algo errado!")

