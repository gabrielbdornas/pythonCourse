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