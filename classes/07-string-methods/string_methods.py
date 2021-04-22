# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# len() - tamanho do caracter
# general porpuse function - pode ser utilizada em listas, por exemplo
# functions - pertencem a vários objetos (strings, integer...)
# methods - apenas um tipo de objeto (string apenas, por exemplo)
# string. abrirá uma lista de opções de methods já disponíveis
curso = 'Python para iniciantes'
print(len(curso))
print(f'"Python para iniciantes" possui {len(curso)} caracteres!')

# .upper(), .lower()
# transforma todas as letras em maiúsculas ou minúsculas
print(curso.upper())
print(curso.lower())

# .find()
print(curso.find('t')) # index 2
print(curso.find('O')) # -1 pois não existe este caracter

# .replace() - substitui, case sensitive
print(curso.replace('iniciantes', 'iniciantes absolutos'))
print(curso.replace('Iniciantes', 'iniciantes absolutos')) # não substituirá nada

# boolean expression
print('Python' in curso) # retorna um booleano True
print('python' in curso) # retorna um booleano False


# Exercícios:
print("----------------Exercícios----------------")
# Solicite o nome do usuário(input()) e retorne para ele quantos caracteres existem em seu nome

# qual a diferença do metodo .find e a expressao booleana "in"

print("----------------Exercícios----------------")