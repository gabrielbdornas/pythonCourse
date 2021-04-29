# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# tuples
# não é possível modificar este tipo de "lista"
# métodos disponíveis apenas index and count
# count - https://www.w3schools.com/python/ref_tuple_count.asp
tuple_exemple = (1, 2, 3)
# não é possivel mudar ou criar um item na lista como tuple_exemple[0] = 10
print(tuple_exemple[0])
print(tuple_exemple[1])
print(tuple_exemple[2])
print(tuple_exemple.count(1)) # número de vezes que o elemento 1 aparece

# Unpacking
# pode ser utilizado para listas tmb
print("---unpacking exemplos---")
# x = tuple_exemple[0]
# y = tuple_exemple[1]
# z = tuple_exemple[2]
x, y, z = tuple_exemple
print(x)
print(y)
print(z)

# Exercícios:
print("----------------Exercícios----------------")
# utilize a função count para printar na tela quantas vezes o primeiro elemento da tuple abaixo aparece na mesma
numbers = (1, 2, 1, 3, 4, 5, 1)

# crie variáveis os elementos da tuple acima utilizando unpaking e print alguns deles

print("----------------Exercícios----------------")