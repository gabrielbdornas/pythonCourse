# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# classes
# modelar novos tipos
# objetos são classes instanciadas
# classes são "rascunhos do objeto"
# EmailClient - CammelCase

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

# instancias
point1 = Point()
point1.move()
point1.draw()
point1.x = 10
print(point1.x)

# Outro objetto
point2 = Point()
point2.x = 20
print(point2.x)

# Construtores


class PointConstrutor:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point3 = PointConstrutor(30, 40)
print(point3.x)
print(point3.y)
point3.x = 31
print(point3.x)

# Herança


class Mamifero:
    def andar(self):
        print("andando")


class Cachorro(Mamifero):
    def latir(self):
        print("Latindo")

cachorro = Cachorro()
print(cachorro.andar())
print(cachorro.latir())


# Exercícios:
print("----------------Exercícios----------------")
# Defina uma classe Calculadora com dois métodos, um para somar e outro para subtrair

# Defina uma classe Pessoa com o atributo nome e um método falar
print("----------------Exercícios----------------")