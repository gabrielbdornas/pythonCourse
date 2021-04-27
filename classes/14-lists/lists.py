# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# lists
# importante entender 0 base lista, ou primeiro elemento está no index 0
# último elemento -1
lista = ["Palio", "Uno", "Strada", "Mobi", "Siena"]
print(lista)
print(lista[0])
print(lista[-1])
print(lista[2:])
print(lista[2:4]) # exclui o último elemento
print(lista[2:-1]) # igual ao de cima - exclui o último elemento
# modificando elemento de uma lista
lista[0] = "PALIO"
print(lista)

# 2d list - cada elemento em uma lista é outra lista
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
for linha in matrix:
    linha_coluna = []
    for item in linha:
        print(item)

# list methods
# Documentação - https://docs.python.org/3/tutorial/datastructures.html
# list.append()
# list.insert() - dois parametros
# list.remove()
# list.clear - limpa toda a lista removendo todos os seus itens
# list.pop() - remove o último elemento
# list.index(5) - retorna o index da primeira ocorrência do 5. Erro mostra a não existência do número pesquisado
numbers = [5, 6, 7]
print(50 in numbers) # retornará falso, pois não há 50 na lista, sem gerar um erro
# list.count()
# list.sort() - organiza a lista
# list.reverse() - coloca todos os elementos em ordem inversa
# list.copy() - copia a lista

# Exercícios:
print("----------------Exercícios----------------")
# crie um programa que ache o maior número de uma lista, por exemplo numeros = [10, 8, 7, 11, 13, 4]

# crie uma lista 2d e um nested loop para printar todos os seu elementos

# escreva um programa para remover itens duplicados de uma lista
# determine voce a lista

print("----------------Exercícios----------------")