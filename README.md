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

## Operadores Aritiméticos 
```buildoutcfg
+                # adição
-                # subtração
*                # multiplicação
/                # retorna um float
//               # retorna um int
%                # resto da divisão
**               # exponenciação

```

Simplificação:
```buildoutcfg
x = x + 10
x += 10
```

Procedência:
1. parenthesis
2. exponentiation
3. multiplication / division
4. addition / subtraction 

## If Statements
```buildoutcfg
if is_hot:
 print(“hot day”)
elif is_cold:
 print(“cold day”)
else:
 print(“beautiful day”)
```

### Logical operators:
```buildoutcfg
if has_high_income and has_good_credit:
 ...
if has_high_income or has_good_credit:
is_day = True
is_night = not is_day
```

### Comparison operators
```buildoutcfg
a > b
a >= b # (greater than or equal to)
a < b
a <= b
a == b # (equals)
a != b # (not equals) 
```

## While loops
```buildoutcfg
i = 1
while i < 5:
 print(i)
 i += 1
```

## For loops
```buildoutcfg
for i in range(1, 5):
 print(i)
# range(5): generates 0, 1, 2, 3, 4
# range(1, 5): generates 1, 2, 3, 4
# range(1, 5, 2): generates 1, 3 
```

## Lists
```buildoutcfg
numbers = [1, 2, 3, 4, 5]
numbers[0] # retorna o primeiro item da lista numbers
numbers[1] # retorna o segundo item da lista numbers
numbers[-1] # retorna o último item da lista numbers
numbers[-2] # retorna o penúltimo item da lista numbers 

# métodos de lista

numbers.append(6) # adiciona 6 no final da lista
numbers.insert(0, 6) # adiciona 6 no index 0 ou primeiro elemento
numbers.remove(6) # remove o 6
numbers.pop() # remove o último item da lista
numbers.clear() # limpa a lista, removendo todos os seus itens
numbers.index(8) # retorna o index da primeira ocorrência do 8
numbers.sort() # classifica a lista
numbers.reverse() # invert a lista
numbers.copy() # retorna uma cópia da lista 
```

## Tuples
São listas de leitura apenas. Uma vez definida, não é possível adicionar, remover
ou modificar seus itens.
```buildoutcfg
coordinates = (1, 2, 3)
# podemos utilizar unpack (assim como em listas)
x, y, z = coordinates 
print(x)
print(y)
print(z)
```

## Dictionaries - Dicionários
São utilizados para armazenar key/values(chaves/valores) pares
pense em um dicionário mesmo
```buildoutcfg
customer = {
 “name”: “John Smith”,
 “age”: 30,
 “is_verified”: True
}

# utilize strings ou numeros para definir keys, devendo estes serem únicos
# values podem ser qualquer tipo de dado

customer[“name”] # retorna “John Smith”
customer[“type”] # gerará um erro, pois o dicionário não possui key type
customer.get(“type”, “silver”) # retorna “silver”
customer[“name”] = “new name” # atribui novo valor para key name
```

## Functions / Funções
Utilizamos funções para quebrar o código em pequenos pedaços. Este pedaços, então,
ficam mais fáceis de ler, entender e dar manutenção. Em caso de bugs é mais fácil
encontrar o problema em partes pequenas do que no programa inteiro. 
Podemos também reutilizar estas partes ao longo de nosso programa

```buildoutcfg
def greet_user(name):
 print(f”Hi {name}”)


greet_user(“John”)

```

Parametros são informações passadas para funções. Argumentos são os valores reais passados
quando chamamos a função
Temos dois tipos de argumentos:
- Positional arguments: ordem importa
- Keyword arguments: ordem não importa, são prefixados com o nome do parametro

```buildoutcfg
# dois positional arguments
greet_user(“John”, “Smith”)

# Keyword arguments
calculate_total(order=50, shipping=5, tax=0.1)
```

Funções podem (devem) retornar valores. Se você não utilizar "return", por padrão
None é retornado. None é um objeto que representa ausênicia de valor.

```buildoutcfg
def square(number):
 return number * number


result = square(2)
print(result) # prints 4
```

## Exceptions 
Exceptions são erros que quebram nosso programa. Usualmente acontecem devido a 
inputs errados ou erros do próprio programa. É noss tarefa antecipar e tratar estes
erros, evitando que nossos programas quebrem.

```buildoutcfg
try:
 age = int(input(‘Age: ‘))
 income = 20000
 risk = income / age
 print(age)
except ValueError:
 print(‘Not a valid number’)
except ZeroDivisionError:
 print(‘Age cannot be 0’)
```
