import turtle as tl

class Ponto():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

x_usuario = int(input("Digite a posição inicial X: "))
y_usuario = int(input("Digite a posição inicial Y: "))
pos_inicial = Ponto(x_usuario, y_usuario)

tl.pensize(4)
tl.color("Blue")
tl.goto((pos_inicial.pos_x, pos_inicial.pos_y))
tl.done()