"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados.

Sintaxe: from arquivo_py import nome_da_funcao ou variavel 

#Pode importar mais de uma coisa especifica:

from arquivo_py import nome_da_funcao, var, x , b 


@Os arquivos devem estar no mesmo local

# Importando uma função específica do nosso módulo
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))






IMPORTANTE
=> # Importando todo o módulo (Temos acesso a TODOS os elementos do módulo)


import funcoes_com_parametro

com alias :

import funcoes_com_parametro as fcp

sem alias e mais explicito:

from funcoes_com_parametro import * 



# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))


from teste2 import soma

dado = [1,2,3,4,5,6]

print(list(map(soma,dado)))

import conjuntos as conj
print(conj.s)
