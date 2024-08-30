'''
Dada a tupla turma = ('André', 'Fernanda', 'Luiz'), peça ao usuário para digitar o nome de um aluno. 
Cheque se o aluno está na tupla e exiba uma mensagem adequada.
'''

def checar_turma(turma, aluno):

    for aluno in turma:
        if (aluno == aluno_busca):
            print("O aluno está na turma!")
            return
    
    print("O aluno não está na turma!")


turma = ("André", "Fernanda", "Luiz")
aluno_busca = input("Digite o nome do aluno: ")

checar_turma(turma, aluno_busca)