# Exercícios:
print("----------------Exercícios----------------")
# crie um while loop e print uma sequencia de 0 a 10
i = 0
print("Início while loop")
while i <= 10:
    print(i)
    i += 1 # loop infinito sem este acrescimo
print("Final while loop")
# crie um while loop e print uma sequencia de 0 a 10 de 2 a 2
i = 0
print("Início while loop")
while i <= 10:
    print(i)
    i += 2 # loop infinito sem este acrescimo
print("Final while loop")
# crie um jogo com as seguintes regras:
# usuário digitar start - resposta "Carro ligado"
# usuário digitar stop - resposta "Carro desligado"
# usuário digitar help - resposta para usuário suas opções
# usuário digitar sair - resposta "Você saiu do jogo" e finalizar o programa
# usuário digitar qualquer outra coisa - resposta "Desculpe, não entendi, tente novamente" e reinicia o jogo
resposta_jogo_carro = ""
while True:
    resposta_jogo_carro = input("> ").lower()
    if resposta_jogo_carro == "start":
        print("Carro ligado")
    elif resposta_jogo_carro == "stop":
        print("Carro desligado")
    elif resposta_jogo_carro == "help":
        print("> start: Ligar o carro")
        print("> stop: Desligar o carro")
        print("> quit: Sair do jogo")
    elif resposta_jogo_carro == "quit":
        print("Você saiu do jogo")
        break
    else:
        print("Desculpe, não entendi, tente novamente")
print("----------------Exercícios----------------")