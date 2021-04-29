# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# functions
# defina sua função primeiro, depois a chame
# duas linhas entre o fim da função e a próxima linha de código (convenção)
def greet_user():
    print("Olá!")
    print("Benvindo a bordo!")


# função com PARAMETRO
def greet_user_name(user_name):
    print(f"Olá, {user_name}!")
    print("Benvindo a bordo!")


# return
# None é retornado como padrão (caso não seja informado o return da função)
# função não deve se preocupar com printar nada e sim retornar
# cada função será responsável por uma função apenas
def square(number):
    return number * number

greet_user()
user_name = input("Qual seu nome? ")
greet_user_name(user_name)  # chamando a função passando um ARGUMENTO
greet_user_name(user_name=user_name)  # chamando a função passando um ARGUMENTO e um keyword argument
# keyword argument pouco utilizado, a menos que vc queiro deixar bastante explicito o que está acontecendo
# chamando função que retorna valores - poderia ter guardado o valor retornado em uma variável também
print(f"O quadrado de 3 é {square(3)}.")

# Exercícios:
print("----------------Exercícios----------------")
# crie uma função que receba o primeiro e o último nome do usuário e print uma mensagem de boas vindas para ele como retorno
# desta função

# escolha um dos exercício já resolvidos e o transforme em uma função
# isso possibilitará sua re-utilização ao longo do projeto

print("----------------Exercícios----------------")