# Exercícios:
print("----------------Exercícios----------------")
# Faça duas perguntas, a primeira o nome do usuário e a segunda qual sua cor favorita, em seguida print uma mensagem como
# "Gabriel gosta da cor preto"
user_name = input("Qual seu primeiro nome? ")
print("Olá " + user_name + "!")
# Desafio - Pesquise!
# Vamos criar um pequeno programa para perguntar o usuário seu nome, ano de nascimento, ano atual e retornar sua idade
# O programa criado não está funcionando, sendo printado na tela um erro explicando ao usuário o local aonde o código apresenta o erro
# Leia a mensagem de erro e tente solucionar o problema.
# Dica: Jogue a mensagem de erro no gogle e tente achar a solução.
# Durante a pesquisa no google não esqueça de digitar 'python' para auxiliar o retorno de soluções viáveis para esta linguagem
# Quando conseguir encontrar o erro tente modificar a função de printar retirando a função str(). Qual erro apresentado? O que
# você entendeu desta função str()? qual a relação entre esta função e a utilizada para correção do primeiro erro?
nome = input('Qual seu nome? ')
ano_nascimento = int(input('Em que ano você nasceu? ')) # int() transforma string em inteiro
ano_atual = int(input('Em que ano estamos? ')) # int() transforma string em inteiro
idade = ano_atual - ano_nascimento # cálculos matemáticos são realizados apenas com números
print('Olá ' + nome + ' você tem ' + str(idade) + ' anos!')  # str() transforma inteiro em string, concatenação exige string
print("----------------Exercícios----------------")