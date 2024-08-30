'''
Escreva um programa que imprima os primeiros 10 números da sequência de Fibonacci.
'''

#Os dois primeiros termos da Sequência de Fibonacci, 0 e 1, são fixos!'
a = 0
b = 1

print(a)
print(b)

for i in range(8):
    temp = a + b
    print(temp)
    a = b
    b = temp
    