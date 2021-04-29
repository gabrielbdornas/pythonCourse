# https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s

# dictionaries
# objetos em js ou hashes em ruby
# keys deverão ser únicos
aluno = {
    "nome": "Gabriel Dornas",
    "idade": 36,
    "cliente_ativo": True
}
print(aluno["nome"])
print(aluno["idade"])
# key não existentes retornará erro (case sensitivo)
print(aluno.get("key_inexistente")) # .get trocará o erro por None ou a inexistência de algo
print(aluno.get("key_inexistente", "Key Inexistente, tente novamente")) # .get trocará o erro por None ou valor padrão configurado
aluno["nome"] = "Júlio Amaral" # atualiza o valor inicial
aluno["casado"] = True # cria um novo key
print(aluno)

# Exercícios:
print("----------------Exercícios----------------")
# solicite o número do telefone do usuário (receba como input numerais de 0 a 9) e retorne a transformação destes numerais
# em palavras. Exemplo: usuário digital 0123 retorno zero um dois tres

# trate erro no exercício acima, caso usuário digite algum valor que não é um número de 0 a 9

print("----------------Exercícios----------------")