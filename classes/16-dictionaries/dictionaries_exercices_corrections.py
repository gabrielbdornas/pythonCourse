# Exercícios:
print("----------------Exercícios----------------")
# solicite o número do telefone do usuário (receba como input numerais de 0 a 9) e retorne a transformação destes numerais
# em palavras. Exemplo: usuário digital 0123 retorno zero um dois tres
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
telefone_usuario = input("Qual o número do seu telefone? ")
telefone_usuario_palavras = ''
for numero in telefone_usuario:
    telefone_usuario_palavras += f"{numeros[numero]} "
print(telefone_usuario_palavras)
# trate erro no exercício acima, caso usuário digite algum valor que não é um número de 0 a 9
telefone_usuario_erro = input("Qual o número do seu telefone? Erro será tratado como!")
telefone_usuario_palavras_tratamento_erro = ''
for numero in telefone_usuario_erro:
    telefone_usuario_palavras_tratamento_erro += f'{numeros.get(numero, "!")} '
print(telefone_usuario_palavras_tratamento_erro)
print("----------------Exercícios----------------")