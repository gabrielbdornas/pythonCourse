# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# exceptions
# erros durante a execução
# função int() não conseguir converter letras, caso informado pelo usuário
# preste atenção na mensagem ao final da execução do programa
# exit code 0 indica a execução sem nenhum erro
# havendo erro, exit code será maior que zero, sendo informado o tipo do erro
try:
    idade = int(input("Qual sua idade? "))
    print(idade)
except ValueError: # informando o tipo de erro a resolução abaixo funcionará apenas para este erro
    print('Input Inválido')


try:
    primeiro_numero = int(input('Vamos dividir. Fale o primeiro número: '))
    segundo_numero = int(input('Fale o segundo número: '))
    divisao = primeiro_numero / segundo_numero
    print(f'O valor da divisão é: {divisao}')
except ValueError:
    print('Informe apenas números')
except ZeroDivisionError:
    print('Segundo número não pode ser 0')

# Exercícios:
print("----------------Exercícios----------------")
# previna o erro para a função abaixo
print(int('abc'))

print("----------------Exercícios----------------")