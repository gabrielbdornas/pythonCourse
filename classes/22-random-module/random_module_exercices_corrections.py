import random
# Exercícios:
print("----------------Exercícios----------------")
# Defina uma classe que contenha uma função que retorne uma lista com dois números gerados randomicamente
# class lista_randomica
# def geracao_lista


class ListaRandomica():
    def geracao_lista(self):
        first = random.randint(10, 20)
        second = random.randint(10, 20)
        return first, second


lista_teste = ListaRandomica()
print(lista_teste.geracao_lista())

print("----------------Exercícios----------------")