# Curso de Python
Este material cobre o que foi ensinado no [YouTube](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=215s), e servirá como futuras referências/consultas sobre a linguagem.

## Variáveis
Utilizamos variáveis para armazenar temporariamente data na memória do computador

```
price = 10
rating = 4.9
course_name = ‘Python for Beginners’
is_published = True
```

* Nestes exemplos:
    - a variável "price" é um integer (número sem casa decimal)
    - a variável "rating" é um float (número com casa decimal)
    - a variável "course_name" é uma string (uma sequência de caracteres)
    - a variável "is_published" é um boolean (True ou False)

## Comentários 
Uma linha de comentário se inicia com o caractere "#". Utilizamos comentários para adicionar notas em nosso código. Comentários explicam o que foi feito.
Eles devem refletir o código e servem para facilitar o entendimento do mesmo por você e até outras pessoas.

```buildoutcfg
# Isto é um comentário e não será executado
# Os comentários podem ser feitos em múltiplas linhas 
```

## Recebendo input
Podemos receber input dos usuários chamando a função input().

```buildoutcfg
birth_year = int(input(‘Birth year: ‘))
```

O função input() sempre retorna uma string. Então se você necessitar realizar algum cálculo com o que foi informado, é necessário utilizar funções de conversão, int(), por exemplo.
O exemplo acima está fazendo exatamente isto.

## Strings
Definimos strings utilizando aspas simples (‘ ‘) ou duplas (“ “).
Para definir string em mais de uma linha utilizamos aspas tripas (“””).
É possível extrair um caractere isolado de uma string utilizando colchetes [ ].

```buildoutcfg
course = ‘Python for Beginners’
course[0] # retorna o primeiro caracter
course[1] # retorna o segundo caracter
course[-1] # retorna o primeiro caracter do final para o início
course[-2] # retorna o segundo caracter do final para o início
```

Podemos fatiar uma string utilizando ":", como course[1:5]. Isso retornará todos os caracteres do index 1 até o 5 (excluindo o 5).
O resultado será "ytho". Se o index inicial for deixado em branco ([:5]), 0 será assumido. O mesmo ocorrerá para o index final

É possível formatar uma string dinamicamente da seguinte maneira:

```buildoutcfg
name = ‘Mosh’
message = f’Hi, my name is {name}’
```

Alguns métodos de strings 

```buildoutcfg
message.upper() # para converter todo texto em letra maiúscula
message.lower() # para converter todo texto em letra minúscula
message.title() # para colocar apenas a primeira letra em maiúscula
message.find(‘p’) # retorna o index do primeiro p, caso ele exista (-1 será retornado caso ele não exista)
message.replace(‘p’, ‘q’) # substitui caracteres na string
```

Para checar se uma string contem um caracter (ou uma sequência), podemos utilizar o operador "in":
```buildoutcfg
course = ‘Python for Beginners’
contains_true = ‘Python’ in course # retornará True
contains_false = ‘python’ in course # retornará False - case sensitive
```


