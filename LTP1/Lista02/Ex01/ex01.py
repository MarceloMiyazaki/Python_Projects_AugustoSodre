import turtle as tl

#Classe Base
class Forma():

    def desenhar(self):
        tl.pendown()
        tl.forward(100)


#Classe da forma de círculo
class Circulo(Forma):

    def __init__(self, forma):
        self.forma = forma

    #Sobrescreve método da superclasse Forma
    def desenhar(self):
        tl.color("Red")

        #Cria um círculo
        
        tl.circle(50)

        print("Desenhou um " + self.forma)


#Classe da forma de quadrado
class Quadrado(Forma):

    def __init__(self, forma):
        self.forma = forma

    #Sobrescreve método da superclasse Forma
    def desenhar(self):
        tl.color("Black")

        #Cria um quadrado
        for i in range(4):
            tl.forward(100)
            tl.right(90)
        
        print("Desenhou um " + self.forma)


#Criando objetos de acordo com a forma
forma_1 = Quadrado("Quadrado")
forma_2 = Circulo("Circulo")

#Configurando a caneta do Turtle
tl.pensize(3)
tl.speed(1)

#Invocando métodos
forma_1.desenhar()
forma_2.desenhar()

#Finalizando a Turtle
tl.done()