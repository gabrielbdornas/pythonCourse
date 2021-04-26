# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# while loop
i = 1
print("Início while loop")
while i <= 5:
    print(i)
    i += 1 # loop infinito sem este acrescimo
print("Final while loop")

i = 1
print("Início while loop shape")
while i < 10:
    print("*" * i)
    i += 1
print("Fim while loop shape")

# jogo de adivinhação - break e else para while loop
numbero_secreto = 9 # usuário terá 3 tentativas para adivinhar este número
tentativas = 3 # usuário terá 3 tentativas
tentativas_usuário = 1 # início do jogo ele utilizou 0 tentativas
print("Início do jogo. Você terá 3 tentativas para acertar um número de 0 a 10.")
while tentativas_usuário < 4:
    chute_usuario = int(input(f'Você tem {tentativas} para adivinhar um número de 0 a 10. Esta é sua {tentativas_usuário} tentativa. Advinhe: '))
    tentativas_usuário += 1
    if chute_usuario == numbero_secreto:
        print(f"Muito bem! Você acertou o número na {tentativas_usuário} tentativa!")
        break # Para o código aonde ele esteja, sendo completado a condição do while loop ou não
else: # python permite else para while loop, assim como para if
    print("Você perdeu")
print("Fim do jogo. Você teve 3 tentativas para acertar um número de 0 a 10.")

# for loop

# Exercícios:
print("----------------Exercícios----------------")
# crie um while loop e print uma sequencia de 0 a 10

# crie um while loop e print uma sequencia de 0 a 10 de 2 a 2

# crie um jogo com as seguintes regras:
# usuário digitar start - resposta "Carro ligado"
# usuário digitar stop - resposta "Carro desligado"
# usuário digitar help - resposta para usuário suas opções
# usuário digitar sair - resposta "Você saiu do jogo" e finalizar o programa
# usuário digitar qualquer outra coisa - resposta "Desculpe, não entendi, tente novamente" e reinicia o jogo

print("----------------Exercícios----------------")