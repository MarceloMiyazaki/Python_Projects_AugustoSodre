
class Motor():
    def status(self):
        return "Motor funcionando!"


class Pneu():
    def status(self):
        return "Pneus cheios!"


class Veiculo(Motor, Pneu):
    def __init__(self, marca, cor, preco):
        super().__init__()
        self.marca = marca
        self.cor = cor
        self.preco = preco

    def status(self):
        result = []
        result.append(Motor.status(self))
        result.append(Pneu.status(self))
        result.append("Marca: " + self.marca)
        result.append("Cor: " + self.cor)
        result.append("Preço: R$" + str(self.preco))
        return result

def print_pesquisa(pesquisa):
    for i in pesquisa:
        print(i)
    print()

carro_1 = Veiculo("BMW", "Azul", 85000)
carro_2 = Veiculo("Mercedes", "Preto", 90000)
moto = Veiculo("Yamaha", "Branco", 35000)

print_pesquisa(carro_1.status())
print_pesquisa(carro_2.status())
print_pesquisa(moto.status())
