'''
Dada uma lista de notas de alunos notas = [6.3, 7.5, 9.2, 5.1, 6.8], calcule e exiba a média das notas. 
Além disso, exiba a quantidade de notas acima da média (6)
'''

def calc_media(notas):
    total = 0
    
    for n in notas:
        total += n

    return total / len(notas)

def calc_acima_media(media, notas):
    acima_media = 0

    for n in notas:
        if (n > media):
            acima_media += 1
    
    return acima_media

notas = [6.3, 7.5, 9.2, 5.1, 6.8]
media = calc_media(notas)

print(f"Média da turma: {media:.2f}")
print(f"Notas acima da média: {calc_acima_media(6, notas)}")
