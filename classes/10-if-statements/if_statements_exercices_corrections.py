# Exercícios:
print("----------------Exercícios----------------")
# Uma casa custa R$100000.00. Pergunte ao futuro comprador se ele tem muita vontade de comprar
# se o futuro comprador tiver muita vontade de comprar reduza o preço em 10%
# se o comprador não tiver muita vontade de comprar reduza o preço em 20% (a pouca vontade poderá crescer com um preço ainda melhor)
# print o preço final
# Dica: não esqueça de converter o valor informado pelo usuário em booleano
valor_casa = 100000
deseja_muito = bool(input(f'Esta casa custa {valor_casa}. Você quer muito comprar(True para sim/False para não)? '))
if deseja_muito:
    valor_final = valor_casa * 0.9
else:
    valor_final = valor_casa * 0.8
print(f'O valor final da casa será {valor_final}!')
#Reproduza o exemplo acima possibilitando que o usuário digite s(True) ou n(False) em sua resposta
valor_casa = 100000
deseja_muito = input(f'Esta casa custa {valor_casa}. Você quer muito comprar(s/f para não)? ')
if deseja_muito == 's':
    deseja_muito = True
elif deseja_muito == 'n':
    deseja_muito = False
if deseja_muito:
    valor_final = valor_casa * 0.9
else:
    valor_final = valor_casa * 0.8
print(f'O valor final da casa será {valor_final}!')
# pergunte o usuário a temperatura do dia. Temperatura maior que 30 está quente, caso contrário dia agradável
# dica: não esqueça de converter a input
temperatura = int(input("Qual a temperatura hoje? "))
if temperatura > 30:
    print("Dia quente!")
else:
    print("Dia agradável!")
print("----------------Exercícios----------------")