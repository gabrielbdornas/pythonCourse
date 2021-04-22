# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# input(), assim como print() são funções já existentes em python
# utilizar input() para receber informações do usuário e utilizar de alguma maneira, printando na tela, por exemplo

nome = input('Qual o seu nome? ')
print('Olá ' + nome) # concatenando ou combinando variáveis com strings, outro tipo de expressão

# Exercícios:
print("----------------Exercícios----------------")
# Faça duas perguntas, a primeira o nome do usuário e a segunda qual sua cor favorita, em seguida print uma mensagem como
# "Gabriel gosta da cor preto"

# Desafio - Pesquise!
# Vamos criar um pequeno programa para perguntar o usuário seu nome, ano de nascimento, ano atual e retornar sua idade
# O programa criado não está funcionando, sendo printado na tela um erro explicando ao usuário o local aonde o código apresenta o erro
# Leia a mensagem de erro e tente solucionar o problema.
# Dica: Jogue a mensagem de erro no gogle e tente achar a solução.
# Durante a pesquisa no google não esqueça de digitar 'python' para auxiliar o retorno de soluções viáveis para esta linguagem
# Quando conseguir encontrar o erro tente modificar a função de printar retirando a função str(). Qual erro apresentado? O que
# você entendeu desta função str()? qual a relação entre esta função e a utilizada para correção do primeiro erro?
nome = input('Qual seu nome? ')
ano_nascimento = input('Em que ano você nasceu? ')
ano_atual = input('Em que ano estamos? ')
idade = ano_atual - ano_nascimento
print('Olá ' + nome + ' você tem ' + str(idade) + ' anos!')
print("----------------Exercícios----------------")