with open("texto.txt" ,"r") as file:
  text = file.read()

letterCount = {}

#adiciona todas as letras do arquivo txt para um dicionário com o número de ocorrências dela correspondendo ao seu valor
for i in text:
  letterCount[i] = letterCount.get(i, 0) + 1

text = sorted(set(text))

#devolve as letras e sua respectiva frequência dentro do arquivo de texto
for i in text:
  print(i+":", letterCount[i])
