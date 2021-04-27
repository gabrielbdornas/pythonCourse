print("----------------Exercícios----------------")
# utilizar a lista numeros = [5, 2, 5, 2, 2, 2] para criar um "F" shape
# imagine que em python não temos como fazer "x * 5"
# xxxxx
# xx
# xxxxx
# xx
# xx
# xx
print("Início F shape primeira versão")
numeros = [5, 2, 5, 2, 2, 2]
for numero in numeros:
    linha = ''
    for x in range(numero):
        linha += 'x'
    print(linha)
print("Fim F shape primeira versão")
# simplifique o código acima utilizando "x * 5"
print("Início F shape segunda versão - simplificação")
for numero in numeros:
    print("x" * numero)
print("Fim F shape segunda versão - simplificação")
# crie um "L" shape utilizando um nested loop
print("Início L shape - nested loop")
l_shape_list = [1, 1, 1, 1, 5]
for linha in l_shape_list:
    l_shape = ''
    for x in range(linha):
        l_shape += 'x'
    print(l_shape)
print("Fim L shape - nested loop")
print("----------------Exercícios----------------")