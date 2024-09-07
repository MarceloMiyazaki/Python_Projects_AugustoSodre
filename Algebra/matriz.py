
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

def troca_linhas(A, k):
    lin = len(A)
    i = k + 1
    while i < lin:
        if A[i][k] != 0:
            for j in range(k, lin):
                A[k][j], A[i][j] = A[i][j], A[k][j]
            return False
        i = i + 1
    else:
        return True

def calc_det(matriz):
    lin = len(matriz)
    col = len(matriz)

    if (lin != col):
        print("Matrizes devem ser de mesma ordem!")
        return

    if (lin == 1):
        return matriz[0][0]
    
    if (lin == 2):
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    

    num_de_troca_de_linhas = 0
    for k in range(lin - 1): # Andando na diagonal
        for i in range(k+1, lin): # Andando as linhas abaixo da diagonal
            if matriz[k][k] == 0: # Verifica se o pivô é zero
                num_de_troca_de_linhas += 1
                if troca_linhas(matriz, k):
                    return 0
            m = -matriz[i][k] / matriz[k][k]
            for j in range(k, col): # Andando nas linhas que estão sendo atualizadas
                matriz[i][j] = matriz[k][j]*m + matriz[i][j]
    resultado = 1
    for k in range(lin): # Multiplicando os elementos da diagonal principal (da matriz triagular)
        resultado = resultado * matriz[k][k] * (-1)**num_de_troca_de_linhas

    return resultado


# matriz_principal  = cria_matriz()
# print_matriz(matriz_principal)

# matriz_secundaria = cria_matriz()
# print_matriz(matriz_secundaria)

#print_matriz(mult_escalar(matriz_secundaria))

# try:
#     print_matriz(opera_matriz(matriz_principal, matriz_secundaria))
# except:
#     print("Algo deu errado!")


matriz = cria_matriz()
print(calc_det(matriz))