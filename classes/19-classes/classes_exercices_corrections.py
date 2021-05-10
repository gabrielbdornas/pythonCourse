# Exercícios:
print("----------------Exercícios----------------")
# Defina uma classe Calculadora com dois métodos, um para somar e outro para subtrair


class Calculadora:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x + y


calculadora = Calculadora()
print(calculadora.soma(2, 2))
print(calculadora.subtracao(3, 1))

# Defina uma classe Pessoa com o atributo nome e um método falar


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self, fala):
        print(f"A fala de {self.nome} é: {fala}")


gabriel = Pessoa("Gabriel")
gabriel.falar("Que exercício legal!")
print("----------------Exercícios----------------")