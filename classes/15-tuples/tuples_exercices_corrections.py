# Exercícios:
print("----------------Exercícios----------------")
# utilize a função count para printar na tela quantas vezes o primeiro elemento da tuple abaixo aparece na mesma
numbers = (1, 2, 1, 3, 4, 5, 1)
print(numbers.count(numbers[0]))
# crie variáveis os elementos da tuple acima utilizando unpaking e print alguns deles
a, b, c, d, e, f, g = numbers
print(f'{a}, {b}, {c}')
h, i, j = numbers[:3]
print(f'{h}, {i}, {j}')
print("----------------Exercícios----------------")