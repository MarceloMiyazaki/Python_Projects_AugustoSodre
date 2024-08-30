'''
Peça ao usuário que insira um número. Se o número for par, exiba "Número par". Se for ímpar, exiba "Número ímpar".
'''

num = input("Digite um número: ")

if (int(num) % 2 == 0):
    print("Par")
else:
    print("Ímpar")