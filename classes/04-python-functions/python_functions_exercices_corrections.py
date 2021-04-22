# Exercícios:
print("----------------Exercícios----------------")
# Em sua opinião, qual tipo de dado retornado em uma função input()?
# resposta: o tipo de dado retornando em uma função input() é string, veja
resposta = input("Escreva qualquer coisa, somente um teste: ")
print(type(resposta))
# pesquise uma função python para contar quantos caracteres existem em uma frase
frase_1 = ""
print(len(frase_1))
frase_2 = "Estou contando uma frase"
print(len(frase_2))
# Escreva um programa que pergunte o usuário seu peso em kilos e mostre o resultado deste input converstido para libras(pounds)
# Dica: 1kg = 2.20462 libras
kg_peso = float(input("Qual seu peso em kg? "))
lb_peso = 2.20462 * float(kg_peso)
print(str(kg_peso) + " kg correspondem a " + str(lb_peso) + " libras!")
print("----------------Exercícios----------------")