# Exercícios:
print("----------------Exercícios----------------")
# print todas as letras do seu primeiro nome (cada letra em uma linha)
for letra in "Gabriel":
    print(letra)
# crie uma lista simples (até 4 elementos) e print cada um de seus elementos em uma linha
for item in ['Carro', 'Bicicleta', 'Moto']:
    print(item)
# crie um for loop utilizando a função range com dois critérios
for item in range(5, 11):
    print(item)
# crie um for loop utilizando a função range com três critérios
for item in range(5, 16, 5):
    print(item)
# supondo que vc tenha a seguinte lista de preços [10, 15, 27]
# crie um foor loop para calcular a soma destes itens
# print o valor final da lista ao final do programa
precos = [10, 15, 27]
total = 0
for preco in precos:
    total += preco
print(f'O valor total da lista de compras é {total}')
# crie um foor loop para calcular a soma destes itens
matrix = [[10, 20, 30],
          [40, 50, 60],
          [70, 80, 90]]
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
for linha in matrix:
    linha_coluna = []
    for item in linha:
        print(item)
# escreva um programa para remover itens duplicados de uma lista
# determine voce a lista
# tente utilizar métodos de lista
remover_duplicadas_lista = [5, 4, 5, 4, 3, 5, 2, 1]
uniques = []
for number in remover_duplicadas_lista:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)
print("----------------Exercícios----------------")