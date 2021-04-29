# Exercícios:
print("----------------Exercícios----------------")
# crie uma função que receba o primeiro e o último nome do usuário e print uma mensagem de boas vindas para ele como retorno
# desta função
def ola_usuario(primeiro_nome, segundo_nome):
    print(f'Olá {primeiro_nome} {segundo_nome}! Bem vindo!')

# escolha um dos exercício já resolvidos e o transforme em uma função
# isso possibilitará sua re-utilização ao longo do projeto
# exercício escolhido:
# solicite o número do telefone do usuário (receba como input numerais de 0 a 9) e retorne a transformação destes numerais
# em palavras. Exemplo: usuário digital 0123 retorno zero um dois tres
def dicionario_numeros(texto):
    numeros = {
        "1": "um",
        "2": "dois",
        "3": "tres",
        "4": "quatro",
        "5": "cinco",
        "6": "seis",
        "7": "sete",
        "8": "oito",
        "9": "nove"
    }
    texto_palavras = ''
    for numero in texto:
        texto_palavras += f"{numeros.get(numero, '!')} "
    return texto_palavras


telefone_usuario = input("Qual o número do seu telefone? ")
print(dicionario_numeros(telefone_usuario))
print("----------------Exercícios----------------")