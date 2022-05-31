"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos builtin|
------------------------
Para economizar espaço de memória, o python não carrega todos os seus módulos
builtin, para carregar algum módulo builtin, basta importar.

Ex: import random, import statistics, import numpy... 


# Utilizando alias (apelidos) para módulos/funções

import random as rdm


print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

#Nesse tipo de import, pode-se utilizar simplesmente as funçoes do modulo,
sem especificar de qual módulo se trata.

Ex: from random import * 

print(random())
print(choice(lista1))
print(sample(lista 1, 5))
print(shuffle(lista1))


# Importando todo o módulo

import random


print(random.random())

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())


https://docs.python.org/3/py-modindex.html

"""
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))

from math import * 

print(pi)
print(e)


