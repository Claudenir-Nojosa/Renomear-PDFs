Variável é um container de um valor. Ele representa o valor que contém.

Variáveis tem vários tipos, são esses:

Strings - Uma série de caracteres, para escrever uma string, precisa ser utilizado aspas simples ou duplas.

Há a possibilidade de juntar uma string com uma variável string, o nome disso é 'concatenação'.

Para verificar qual o tipo da variável, basta utilizar a função 'type', da seguinte maneira:

name = 'Bro'
print(type(name))


Existe uma convenção para nomear variáveis, que se a variável tem mais de um nome, é utilizado camelCase ou '_', por exemplo:
first_name
firstName


Int - São números inteiros, não há necessidade de utilizar aspas. Com os números inteiros há a possibilidade de realizar operações matemáticas.

age = 21
age += 1
print (age)
print(type(age)) # class 'int'

Não há a possibilidade de concatenar uma variável string com uma variável numérica, para realizar a concatenação, basta utilizar a função 'str' e envolver a variável numérica. Por exemplo:

age = 21
print ('Your age is: '+ str(age))

Float - Valor numérico que não é inteiro, ou seja, possui valor decimal

height = 250.5
print(height)
print(type(height)) # class 'float'

Boolean - São variáveis bastante importantes para 'if statements'.

human = False

print(type(human)) # class 'boo'
