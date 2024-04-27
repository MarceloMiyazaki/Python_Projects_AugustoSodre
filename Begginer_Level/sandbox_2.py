number  = int(input("Dê-me um número: "))
milhar  = (number)//1000
centena = (number - milhar * 1000)//100
dezena  = (number - milhar * 1000 - centena * 100)//10
unidade = (number - milhar * 1000 - centena * 100 - dezena * 10)
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")