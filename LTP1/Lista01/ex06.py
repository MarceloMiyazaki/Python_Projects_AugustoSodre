'''
Exercício 6: Crie um programa que gerencie o banco de dados de uma biblioteca. 
O programa deve permitir adicionar um novo livro (como uma lista contendo título, autor e ano),
listar todos os livros, e permitir a busca de livros pelo título.
'''

import os

lista_livros_total = []
resposta = 0


def menu_inicial():
    print("--------------Menu--------------")
    print("Selecione o que deseja fazer:")
    print("1: Adicionar novo livro")
    print("2: Deletar livro")
    print("3: Listar todos os livros")
    print("4: Busca de livro por título")
    print("5: Sair")
    print("--------------------------------")


def adicionar_livro():
    print("--------------------------------")
    print("Adicionar livro!")
    titulo = input("Digite o título do livro: ")
    titulo = titulo.title()
    autor  = input("Digite o autor do livro: ")
    autor = autor.title()
    ano    = input("Digite o ano do livro: ")
    novo_livro = {"titulo" : titulo, "autor" : autor, "ano" : ano}
    lista_livros_total.append(novo_livro)
    print()
    


def remover_livro():
    print("--------------------------------")
    print("Remover livro!")
    titulo = input("Digite o título do livro: ")
    titulo = titulo.title()
    print()
    for i in range(len(lista_livros_total)):
        if lista_livros_total[i]["titulo"] == titulo:
            lista_livros_total.pop(i)
            print("Livro Removido!")
            print()
            return
    
    print("Livro não encontrado!")

    print()


def listar_livros():
    print("--------------------------------")
    print("Livros:")
    print()
    for i in lista_livros_total:
        print("Título: ", i["titulo"])
        print("Autor:  ", i["autor"])
        print("Ano:    ", i["ano"])
        print()
    print()


def buscar_livros():
    print("--------------------------------")
    print("Buscar livro!")
    titulo = input("Digite o título do livro: ")
    titulo = titulo.title()
    print()
    for i in range(len(lista_livros_total)):
        if lista_livros_total[i]["titulo"] == titulo:
            print("Título:", lista_livros_total[i]["titulo"])
            print("Autor:", lista_livros_total[i]["autor"])
            print("Ano", lista_livros_total[i]["ano"])
            print()
            return
    
    print("Livro não encontrado!")

    print()


#Adicionando livros default na biblioteca
titulo = "Percy Jackson - A Maldição do Titã"
autor  = "Rick Riordan"
ano    = "2007"
novo_livro = {"titulo" : titulo, "autor" : autor, "ano" : ano}
lista_livros_total.append(novo_livro)

titulo = "Harry Potter E O Enigma do Príncipe"
autor  = "J. K. Rowling"
ano    = "2005"
novo_livro = {"titulo" : titulo, "autor" : autor, "ano" : ano}
lista_livros_total.append(novo_livro)

titulo = "O Hobbit"
autor  = "Tolkien"
ano    = "1937"
novo_livro = {"titulo" : titulo, "autor" : autor, "ano" : ano}
lista_livros_total.append(novo_livro)


#Iniciando o terminal com o usuário
while (True):
    menu_inicial()
    resposta = int(input("Resposta: "))
    if (resposta == 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        adicionar_livro()
    elif (resposta == 2):
        os.system('cls' if os.name == 'nt' else 'clear')
        remover_livro()
    elif (resposta == 3):
        os.system('cls' if os.name == 'nt' else 'clear')
        listar_livros()
    elif (resposta == 4):
        os.system('cls' if os.name == 'nt' else 'clear')
        buscar_livros()
    elif (resposta == 5):
        break
    else:
        print("Resposta inválida!")

